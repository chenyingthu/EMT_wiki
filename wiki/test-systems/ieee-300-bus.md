---
title: "IEEE 300 节点场景入口"
type: test-system
tags: [ieee-300-bus, benchmark, large-scale-system, test-system]
created: "2026-05-04"
updated: "2026-05-06"
---

# IEEE 300 节点场景入口

## 定义与边界

IEEE 300 节点系统是大规模输电网络 benchmark 的一个常见入口。在本 Wiki 中，本页作为场景入口，用于承接围绕该 benchmark 展开的潮流、稳定性、并网改造和 EMT 扩展研究。

本页不是光伏 ELST 建模页，也不是特定设备模型页。

## EMT 中的作用

该入口常用于：

- 说明大规模网络 benchmark 如何被扩展到 EMT 研究；
- 对比不同初始化、并网和加速方法在大系统背景下的适用边界；
- 为测试系统页、潮流页和验证页提供大型 benchmark 背景。

## 常见用途

- 作为大系统潮流和初始工况构造背景；
- 作为频变线路、网络等值和混合仿真扩展对象；
- 作为大规模并网改造或控制策略外推时的 benchmark 背景；
- 作为与 IEEE 118 等更小系统对照的规模型案例。

## 形式化表达

作为 benchmark 入口，其系统级最小关系仍可抽象为：

$$
\mathbf{Y}_{300}\mathbf{v} = \mathbf{i}
$$

实际 EMT 研究通常还需要在此基础上补充频变线路、控制器、保护和扰动脚本。

## 相关页面

- [[ieee-300-bus-system]]：主题层面的 IEEE 300 场景页。
- [[power-flow-calculation]]：稳态运行点计算入口。
- [[model-verification-benchmark]]：benchmark 使用边界。
- [[large-scale-power-system]]：大规模系统主题背景。
- [[ieee-118-bus-system]]：较小规模输电 benchmark 的对照背景。

## 代表性来源

- [[multiphase-power-flow-solutions-using-emtp-and-newtons-method-power-systems-ieee]]：说明大系统潮流与 EMTP 背景。
- [[real-time-transient-simulation-based-on-a-robust]]：说明大型系统实时/暂态仿真相关背景。
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]：说明大系统等值与混合研究背景。

## 证据边界

本页不写具体线路、负荷和设备参数，只作为 IEEE 300 benchmark 场景入口。

## 开放问题

- 当前页尚未区分“原始 benchmark”与“加入 EMT 细节后的扩展 benchmark”之间的证据边界。
- 不同论文对 IEEE 300 的改造方式，后续应在测试系统页中进一步拆开。
