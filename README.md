# EMT Wiki

电力系统电磁暂态（EMT）仿真领域知识库，基于 [Karpathy LLM Wiki Pattern](https://github.com/karpathy/llm-wiki) 构建。

## 概览

| 指标 | 数值 |
|------|------|
| 论文总数 | 699 |
| 已分析 | 699 (100%) |
| 主题页 | 11 |
| 方法页 | 10 |
| 模型页 | 10 |
| 实体页 | 9 |

## 目录结构

```
wiki/
├── index.md          # 完整索引
├── overview.md       # EMT 领域概览
├── log.md            # 构建日志
├── sources/          # 699 篇论文来源页
├── topics/           # 11 个主题页（混合仿真、实时仿真等）
├── methods/          # 10 个方法页（矢量拟合、平均值模型等）
├── models/           # 10 个模型页（MMC、VSC、变压器等）
└── entities/         # 9 个实体页（工具、机构、学者）
```

## 快速导航

- **[Wiki 索引](wiki/index.md)** — 所有页面一览
- **[领域概览](wiki/overview.md)** — EMT 仿真核心概念
- **[构建日志](wiki/log.md)** — 完整构建历史

## 工具

| 工具 | 说明 |
|------|------|
| `tools/analyze_sources.py` | 规则分析来源页，填充贡献/方法/模型/主题章节 |
| `tools/build_backrefs.py` | 构建分类页的来源论文反向引用 |
| `tools/extract_metadata.py` | 从 PDF 批量提取元数据 |
| `tools/ingest_folder.py` | 批量摄入论文文件夹 |

## 构建方式

```bash
# 分析所有来源页
python3 tools/analyze_sources.py

# 更新分类页反向引用
python3 tools/build_backrefs.py
```

## License

Knowledge content for academic research purposes.
