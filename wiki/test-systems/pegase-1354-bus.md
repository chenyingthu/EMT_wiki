---
title: "PEGASE 1354 节点场景入口"
type: test-system
tags: [pegase-1354-bus, pegase, benchmark, large-scale-system, test-system]
created: "2026-05-04"
updated: "2026-05-07"
---

# PEGASE 1354 节点场景入口

## 定义与边界

PEGASE 1354 节点系统是大规模输电网络与潮流/稳定性研究中的 benchmark 场景之一。在本 Wiki 中，本页作为场景入口，用于承接围绕该 benchmark 展开的潮流初始化、网络等值、并网改造和 EMT 扩展研究。

本页不是光伏 ELST 建模页，也不是任何单一设备模型页。

## EMT 中的作用

该入口常用于：

- 说明超千节点 benchmark 如何被扩展到 EMT 或混合仿真研究；
- 对比初始化、网络等值和大系统提速方法在更高规模网络中的适用边界；
- 为测试系统页、潮流页和验证页提供大规模 benchmark 背景。

## 常见用途

- 作为超大规模网络潮流和初始工况构造背景；
- 作为频变线路、网络等值和混合仿真的扩展对象；
- 作为新能源接入、控制器改造或 EMT 局部细化的大系统 benchmark；
- 作为与 IEEE 118、IEEE 300 等 benchmark 的规模对照场景。

## 形式化表达

作为场景入口，其系统级最小关系仍可抽象为：

$$
\mathbf{Y}_{1354}\mathbf{v} = \mathbf{i}
$$

实际 EMT 研究通常还需要在此基础上叠加动态负荷、详细设备、控制器和扰动脚本。

## 相关页面

- [[power-flow-calculation]]：稳态运行点计算入口。
- [[model-verification-benchmark]]：benchmark 使用边界。
- [[large-scale-power-system]]：大规模系统主题背景。
- [[ieee-300-bus-system]]：较小规模输电 benchmark 的对照背景。
- [[network-equivalent]]：超大规模系统局部细化前常用的等值背景。

## 代表性来源

- [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee]]：说明大系统潮流与 EMTP 背景。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：说明大系统等值与混合研究背景。
- [[real-time-transient-simulation-based-on-a-robust]]：说明大型系统实时/暂态仿真相关背景。

## 证据边界

本页不写具体线路、负荷和设备参数，只作为 PEGASE 1354 benchmark 场景入口。

## 开放问题

- 当前页尚未区分“原始 PEGASE benchmark”与“加入 EMT 细节后的扩展 benchmark”之间的边界。
- 不同论文对 PEGASE 1354 的网络改写和设备细化方式，后续应在测试系统页进一步拆开。
