---
title: "配电测试馈线入口"
type: test-system
tags: [distribution-test-feeders, feeder, benchmark, distribution-system, test-system]
created: "2026-05-05"
updated: "2026-05-06"
---

# 配电测试馈线入口

## 定义与边界

配电测试馈线通常指 IEEE 或工程文献中反复使用的标准配电 feeder 场景，用于验证潮流、保护、分布式电源接入和配电级 EMT 模型。在本 Wiki 中，本页作为场景入口，承接相关测试系统和方法页面。

本页不是电压互感器参数计算页，也不是任意单篇论文摘要。

## EMT 中的作用

配电测试馈线入口常用于：

- 组织配电级 EMT 测试系统与 benchmark；
- 对比分布式电源、故障、保护和实时仿真方法；
- 为随机扰动、配电自动化和配网并网研究提供共同背景。

## 常见类型

- 经典 IEEE 配电馈线 benchmark；
- 含分布式电源或储能的扩展 feeder；
- 面向保护、暂态过电压或实时仿真的专用 feeder；
- 与微电网或柔性配电网相结合的混合场景。

## 形式化表达

配电馈线场景的核心通常仍由网络约束和负荷/分布式电源注入组成：

$$
\mathbf{Y}_{feeder}\mathbf{v} = \mathbf{i}_{load} + \mathbf{i}_{dg}
$$

## 相关页面

- [[distribution-network]]：配电网络方法页。
- [[ieee-57-bus-system]]、[[ieee-30-bus-system]]：测试系统目录中的相关 benchmark。
- [[model-verification-benchmark]]：benchmark 使用边界。
- [[microgrid-test-system]]：含分布式资源的相关测试背景。

## 代表性来源

- [[a-testing-tool-for-converter-dominated-power-system-stochastic-electromagnetic-t]]：说明配电和变流器主导场景中的随机 EMT 测试背景。
- [[an-fpga-based-electromagnetic-transient-analysis-of-power-distribution-network]]：说明配电网络实时/硬件加速背景。
- [[lightning-impulse-voltage-distribution-over-voltage-transformer-windings-simulat]]：说明配电设备和测试场景的相关背景。

## 证据边界

本页不写具体 feeder 参数或节点数，具体配置应回到测试系统页。

## 开放问题

- 当前页尚未把“验证潮流/保护/实时仿真”三类 feeder 的用途完全拆开。
- 同名 feeder 在不同论文中的参数改写，后续应在测试系统页进一步区分。
