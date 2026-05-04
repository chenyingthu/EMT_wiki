---
title: "EEAC (Extended Equal Area Criterion)"
type: method
tags: [eeac, equal-area, transient-stability, direct-method, single-machine-equivalent]
created: "2026-05-02"
---

# 扩展等面积准则 (EEAC)

## 定义与边界

扩展等面积准则（Extended Equal Area Criterion, EEAC）是把多机暂态功角稳定问题映射为等效单机无穷大系统（OMIB）后应用 [[equal-area-criterion]] 的直接法路线。它的核心不是重建完整 EMT 模型，而是识别临界机群与其余系统的相对运动，并把该相对运动转化为一条等效功率角曲线。

本页讨论 EEAC 的方法框架。关于 EEAC 的提出年份、工程系统实现和具体性能数字，若没有可核验来源，不在本页写成强结论。EEAC 不能自动覆盖多摆失稳、电压失稳、保护连锁、换流器限流和详细 EMT 高频暂态。

## EMT 中的作用

EEAC 可作为 EMT 或 EMT-TS 混合仿真后的解释工具：从时域轨迹中识别领先机群、构造等效功角、计算加速/减速面积，并把稳定裕度与故障切除时间联系起来。它特别适合解释“哪个机群在首摆中被故障加速、切除后网络是否提供足够制动功率”。

若 EMT 细节会改变临界机群或等效电磁功率，例如 HVDC 控制、构网型变换器限流、动态负荷恢复或保护动作，则 EEAC 结果必须与完整时域轨迹互相校核。

## 核心机制

设多机系统被划分为临界群 $C$ 和非临界群 $N$。用惯性加权平均定义群角和群速：

$$
\delta_C=\frac{\sum_{i\in C}M_i\delta_i}{\sum_{i\in C}M_i},
\qquad
\delta_N=\frac{\sum_{j\in N}M_j\delta_j}{\sum_{j\in N}M_j}
$$

$$
\omega_C=\frac{\sum_{i\in C}M_i\omega_i}{\sum_{i\in C}M_i},
\qquad
\omega_N=\frac{\sum_{j\in N}M_j\omega_j}{\sum_{j\in N}M_j}
$$

等效 OMIB 变量为：

$$
\delta_{eq}=\delta_C-\delta_N,\qquad
\omega_{eq}=\omega_C-\omega_N
$$

等效惯性可写为：

$$
M_{eq}=\frac{M_C M_N}{M_C+M_N},
\qquad
M_C=\sum_{i\in C}M_i,\quad M_N=\sum_{j\in N}M_j
$$

等效摇摆方程为：

$$
M_{eq}\frac{d^2\delta_{eq}}{dt^2}
=P_{m,eq}-P_{e,eq}(\delta_{eq},t)
$$

若故障期间和切除后可得到等效功率角曲线，则：

$$
A_{\mathrm{acc}}
=\int_{\delta_0}^{\delta_c}
\left(P_{m,eq}-P_{e,eq}^{fault}\right)d\delta
$$

$$
A_{\mathrm{dec,max}}
=\int_{\delta_c}^{\delta_u}
\left(P_{e,eq}^{post}-P_{m,eq}\right)d\delta
$$

首摆稳定的等效判据是 $A_{\mathrm{acc}}<A_{\mathrm{dec,max}}$。该判据的可信度取决于机群识别、等效功率曲线和故障后稳定边界是否与原多机轨迹一致。

## 分类与变体

- 静态分群 EEAC：基于故障后早期角速度或功角差识别临界群，适合首摆主导场景。
- 动态分群 EEAC：沿时域轨迹更新机群和等效参数，适合临界群不明显或机群可能变化的场景。
- 时域-EEAC 混合：先短时域仿真生成轨迹，再做 OMIB 等效和面积裕度计算。
- 多群扩展：当不止一个机群相互分离时，需要多自由度能量或分群方法；简单二群 OMIB 可能过度压缩信息。
- 与 SIME 的关系：二者都使用单机等效和面积解释，但机群识别、轨迹使用方式和实现细节可能不同。

## 适用边界与失败模式

- 临界机群识别错误会直接导致裕度符号和 CCT 判断错误。
- 首摆稳定不等于多摆稳定；后续控制器、调速器和保护动作可能改变结论。
- 等效功率角曲线若不是单值函数，面积解释会变弱。
- 含强电力电子控制、限流和不平衡故障时，$P_{e,eq}$ 可能依赖状态切换而非仅依赖 $\delta_{eq}$。
- 任何“速度提升”“误差小于某值”或“实时应用”说法都必须绑定来源、系统规模、硬件和判据。

## 代表性来源

- [[transient-stability-analysis]]：说明 EEAC 所属的直接法位置，以及 CCT 和时域验证的证据要求。
- [[equal-area-criterion]]：提供 EEAC 最终使用的面积判据和单自由度边界。
- [[energy-function]]：提供与面积裕度相邻的能量函数解释。
- [[electromechanical-transient]]：给出 EEAC 所在的机电暂态时间尺度，不应与 EMT 高频暂态混淆。

## 与相关页面的关系

- [[equal-area-criterion]] 是 EEAC 的单机判据基础。
- [[energy-function]] 提供更一般的能量裕度背景。
- [[swing-equation]] 给出机组和等效机群的运动方程。
- [[transient-stability-analysis]] 组织故障、判据、CCT 和验证流程。
- [[time-domain-simulation]] 用于生成或复核机群轨迹。
- [[transient-stability]] 定义本方法服务的稳定性问题。
