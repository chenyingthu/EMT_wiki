#!/usr/bin/env python3
"""Small provider adapter for wiki enrichment scripts."""

from __future__ import annotations

import os
import json
from pathlib import Path
import tomllib
import urllib.error
import urllib.request
from typing import Protocol


class LLMClient(Protocol):
    def complete(self, prompt: str, *, max_tokens: int, temperature: float, timeout: float) -> str:
        """Return plain text completion for a single prompt."""


class AnthropicLLMClient:
    def __init__(self, model: str | None = None, base_url: str | None = None, api_key: str | None = None):
        try:
            import anthropic
        except ImportError as exc:
            raise RuntimeError("anthropic package is required for --llm-provider anthropic") from exc

        self.model = model or os.environ.get("ANTHROPIC_MODEL", "kimi-k2.5")
        self.client = anthropic.Anthropic(
            api_key=api_key or os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_API_KEY"),
            base_url=base_url or os.environ.get("ANTHROPIC_BASE_URL", "https://qianfan.baidubce.com/anthropic/coding"),
        )

    def complete(self, prompt: str, *, max_tokens: int, temperature: float, timeout: float) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            temperature=temperature,
            timeout=timeout,
            messages=[{"role": "user", "content": prompt}],
        )
        return _anthropic_text(response)


class OpenAILLMClient:
    def __init__(self, model: str | None = None, base_url: str | None = None, api_key: str | None = None):
        self.model = model or os.environ.get("OPENAI_MODEL", "gpt-4.1")
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.base_url = (base_url or os.environ.get("OPENAI_BASE_URL") or "https://api.openai.com/v1").rstrip("/")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY is required for --llm-provider openai")

    def complete(self, prompt: str, *, max_tokens: int, temperature: float, timeout: float) -> str:
        payload = {
            "model": self.model,
            "input": prompt,
            "max_output_tokens": max_tokens,
            "temperature": temperature,
        }
        request = urllib.request.Request(
            f"{self.base_url}/responses",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "OpenAI/Python 1.0 EMT-Wiki/1.0",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"OpenAI API HTTP {exc.code}: {body[:500]}") from exc
        if data.get("output_text"):
            return data["output_text"]
        parts = []
        for item in data.get("output", []) or []:
            for content in item.get("content", []) or []:
                text = content.get("text")
                if text:
                    parts.append(text)
        return "\n".join(parts)


def make_codex_client(model: str | None = None) -> LLMClient:
    """Build an OpenAI-compatible client from ~/.codex/config.toml."""
    config_path = Path(os.environ.get("CODEX_CONFIG", "~/.codex/config.toml")).expanduser()
    if not config_path.exists():
        raise RuntimeError(f"Codex config not found: {config_path}")

    with config_path.open("rb") as f:
        config = tomllib.load(f)

    provider_name = config.get("model_provider", "codex")
    provider_config = config.get("model_providers", {}).get(provider_name, {})
    wire_api = provider_config.get("wire_api", "responses")
    if wire_api != "responses":
        raise RuntimeError(f"Unsupported Codex wire_api for wiki tools: {wire_api}")

    base_url = provider_config.get("base_url")
    resolved_model = model or config.get("model")
    api_key = _load_codex_api_key(config_path.parent, provider_name)
    return OpenAILLMClient(model=resolved_model, base_url=base_url, api_key=api_key)


def _load_codex_api_key(codex_home: Path, provider_name: str) -> str:
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]

    auth_candidates = [
        codex_home / "auth.json",
        codex_home / f"auth_{provider_name}.json",
    ]
    for auth_path in auth_candidates:
        if not auth_path.exists():
            continue
        try:
            data = json.loads(auth_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for key_name in ("OPENAI_API_KEY", "api_key", "token"):
            if data.get(key_name):
                return data[key_name]
    raise RuntimeError("No OpenAI-compatible API key found in environment or ~/.codex/auth*.json")


def make_llm_client(provider: str | None = None, model: str | None = None) -> LLMClient:
    resolved = (provider or os.environ.get("WIKI_LLM_PROVIDER") or "codex").lower()
    if resolved == "codex":
        return make_codex_client(model=model)
    if resolved == "openai":
        return OpenAILLMClient(model=model)
    if resolved == "anthropic":
        return AnthropicLLMClient(model=model)
    raise ValueError(f"Unsupported LLM provider: {provider}")


def _anthropic_text(response) -> str:
    parts = []
    for block in getattr(response, "content", []) or []:
        text = getattr(block, "text", None)
        if text:
            parts.append(text)
    return "\n".join(parts)
