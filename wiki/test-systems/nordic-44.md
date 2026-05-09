---
title: "Nordic 44 场景入口"
type: test-system
tags: [nordic-44, benchmark, voltage-stability, test-system, nordic]
created: "2026-05-04"
updated: "2026-05-06"
---

# Nordic 44 场景入口


```mermaid
graph TD
    subgraph S0[Nordic 44 场景入口]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见用途]
        N3[形式化表达]
        N4[相关页面]
        N5[代表性来源]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

Nordic 44 通常作为 Nordic 32 的扩展系统或相关北欧 benchmark 场景，用于更复杂的电压稳定和大系统动态研究。在本 Wiki 中，本页作为场景入口，用于组织与该系统相关的方法和测试背景。

本页不是频变线路论文页，也不是设备模型页。

## EMT 中的作用

Nordic 44 场景常用于：

- 研究扩展北欧系统中的稳定边界和控制影响；
- 作为大型系统 EMT 扩展与混合仿真的背景；
- 对比与 Nordic 32 不同规模和结构下的方法表现。

## 常见用途

- 作为扩展北欧系统的大规模 benchmark；
- 作为 EMT/混合仿真对比 Nordic 32 的场景延伸；
- 作为控制、初始化或系统等值方法在更复杂网络中的验证背景；
- 作为大系统场景页而非单一设备模型页的入口。

## 形式化表达

系统级入口可抽象写为：

$$
\mathbf{Y}_{N44}\mathbf{v} = \mathbf{i}
$$

它强调 benchmark 的网络背景，而不替代具体设备和控制建模。

## 相关页面

- [[nordic-32-system]]：测试系统目录中的相关 benchmark 页。
- [[nordic-32-system]]：相关基础场景入口。
- [[large-scale-power-system]]：大规模系统主题背景。
- [[model-verification-benchmark]]：benchmark 使用边界。
- [[ieee-39-bus-system]]：另一类经典稳定性 benchmark 对照背景。
- [[transient-stability-analysis]]：动态稳定研究背景。

## 代表性来源

- [[shooting-method-based-modular-multilevel-converter-initialization-for-electromag]]：说明大型系统初始化与 EMT 背景。
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：说明大规模 benchmark 扩展的相关背景。

## 证据边界

本页不写固定网络参数或统一性能结论，只作为 Nordic 44 场景入口。

## 开放问题

- 当前页尚未继续说明 Nordic 44 相比 Nordic 32 的结构扩展重点。
- 相关论文对 Nordic 44 的改造差异，后续应在测试系统页中进一步拆开。
