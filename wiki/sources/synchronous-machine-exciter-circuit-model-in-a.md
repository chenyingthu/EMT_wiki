---
title: "Synchronous Machine Exciter Circuit Model In A"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/pesmg.2013.6672704.pdf.pdf"]
---

# Synchronous Machine Exciter Circuit Model In A

**作者**: 
**年份**: 2013
**来源**: `37/pesmg.2013.6672704.pdf.pdf`

## 摘要

—This paper presents the implementation of a phase domain (PD) synchronous machine (SM) model through modified-augmented-nodal-analysis (MANA) formulation for the computation of electromagnetic transients. This formulation provides a direct and simultaneous electrical connection to the SM field winding, and enables accurate modeling of its exciter as an electrical side. Detailed exciter modeling can be used to study exciters transient performance and potential failure conditions in its circuit components. This paper also presents and tests a simple current source interface for existing dq0-type SM machine models with control signal input for field control. Realistic test cases are used to validate and compare the proposed models. Index Terms—synchronous machine, excitation system, EMTP. I.

## 核心贡献



- 基于改进增广节点分析（MANA）公式实现了相域同步电机模型，提供与励磁绕组直接同步的电气连接，实现励磁系统精确电路建模。
- 为现有dq0型同步电机模型提出并验证了一种简单的电流源接口，用于励磁控制信号输入，提升了模型兼容性与仿真灵活性。

## 使用的方法


- [[nodal-analysis]]
- [[numerical-integration]]

## 涉及的模型


- [[synchronous-machine]]

## 相关主题


- [[synchronous-machine]]
- [[parallel]]

## 主要发现



- 基于MANA的相域同步电机模型可实现励磁绕组与外部电路的直接同步连接，显著提升励磁系统瞬态性能及元件故障分析的准确性。
- 提出的电流源接口能有效兼容现有dq0型同步电机模型，在保证精度的同时简化励磁控制接入，并通过并联机组实际案例验证了其有效性。