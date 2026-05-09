---
title: "模型降阶方法 (Model Order Reduction)"
type: method
tags: [model-reduction, state-space, balancing, krylov, network-equivalent]
created: "2026-05-04"
---

# 模型降阶方法 (Model Order Reduction)


```mermaid
graph TD
    subgraph Ncmp[模型降阶方法 (Model Order Reduction)]
        N0[平衡截断: 保留强可控且强可观状态]
        N1[Krylov/矩匹配: 匹配传递函数局部矩]
        N2[模态截断: 保留主导极点或弱阻尼模态]
        N3[Kron 节点消去: 消去内部节点，保留端口导纳]
        N4[平均值/聚合模型: 聚合开关或子模块细节]
        N5[无源网络综合: 由频响综合 RLCM 网络]
    end
```


## 定义与边界

模型降阶（Model Order Reduction, MOR）是在保留指定输入输出行为或关键状态特征的前提下，把高阶模型替换为低阶模型的技术集合。在 EMT 中，它可作用于 [[state-space-method]] 模型、[[fdne-model]]、MMC 桥臂、线路/电缆宽频模型、变压器端口模型或外部网络等值。

降阶不是无损压缩。它必须说明保留的端口、频段、工况、状态量和误差指标。若研究目标涉及未保留的开关细节、局部能量、保护峰值或高频过电压，低阶模型可能给出误导性结果。

## EMT 中的作用

EMT 仿真中，降阶主要用于降低单步求解维度、减少递推状态数、满足 [[real-time-simulation]] deadline，以及把非研究区域替换为端口等值。典型场景包括频率相关网络等值、[[mmc-model]] 子模块聚合、[[pet-sst-model]] 高频链路端口化、变压器宽频模型和大规模外部网络的 [[network-equivalent]]。

降阶模型进入 EMT 前仍需离散化、初始化、接口变量定义和时域验证。频域误差小不等于故障暂态、开关事件或控制器饱和时都可靠。

## 核心机制

状态空间降阶可写为：原模型 $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}\mathbf{u}$、$\mathbf{y}=\mathbf{C}\mathbf{x}+\mathbf{D}\mathbf{u}$，低阶模型 $\dot{\hat{\mathbf{x}}}=\hat{\mathbf{A}}\hat{\mathbf{x}}+\hat{\mathbf{B}}\mathbf{u}$、$\hat{\mathbf{y}}=\hat{\mathbf{C}}\hat{\mathbf{x}}+\hat{\mathbf{D}}\mathbf{u}$。降阶目标是让 $\mathbf{y}$ 与 $\hat{\mathbf{y}}$ 在关注频段和工况下接近，而不是让每个内部状态一一对应。

频域模型常先由 [[vector-fitting]] 或 [[prony-analysis]] 得到极点-留数模型，再通过截断弱模态、平衡截断、Krylov 矩匹配或物理网络综合降低阶数。电路拓扑类降阶则通过 Kron 消去、戴维南/Norton 等值或子模块聚合减少外部网络可见维度。

## 分类与变体

| 类型 | 核心思想 | 适用对象 | 主要风险 |
|------|----------|----------|----------|
| 平衡截断 | 保留强可控且强可观状态 | 线性状态空间模型 | 物理状态解释可能丢失 |
| Krylov/矩匹配 | 匹配传递函数局部矩 | 端口网络、宽频阻抗 | 频段外误差可能增大 |
| 模态截断 | 保留主导极点或弱阻尼模态 | 振荡和等值模型 | 弱但关键的高频模态可能被删 |
| Kron 节点消去 | 消去内部节点，保留端口导纳 | 模块化网络、SST、子网络 | 内部变量不可直接观察 |
| 平均值/聚合模型 | 聚合开关或子模块细节 | MMC、VSC、风电场 | 开关级暂态和局部不平衡被弱化 |
| 无源网络综合 | 由频响综合 RLCM 网络 | 多端口 FDNE | 实现复杂，适用对象受正实性约束 |

## 适用边界与失败模式

- 端口边界：降阶只保证选定端口的行为；内部节点电压、电容应力和支路电流可能不可恢复。
- 频段边界：模型应报告关注频段和权重；超出频段的雷电、VFTO 或 EMI 不能外推。
- 工况边界：平均值和线性降阶模型通常只在指定工作点、控制模式或拓扑下成立。
- 无源性边界：FDNE 和宽频端口模型降阶后可能破坏正实性，需要 [[passivity-enforcement]]。
- 初始化边界：低阶状态的初值必须与潮流、稳态或历史源一致，否则会产生伪暂态。
- 证据边界：原页面中”15-20 倍””10-100 倍””误差 <1%”等数字来自特定论文或自动汇总，本页不作为通用参数保留。

### 阶数选择准则

| 准则 | 方法 | 适用场景 |
|------|------|----------|
| 奇异值阈值 | 保留 $\sigma_i > \epsilon\sigma_{max}$ | 平衡截断 |
| 误差界 | $2\sum_{i=r+1}^{n}\sigma_i < \epsilon_{tol}$ | 有明确误差要求 |
| 频率响应 | 在关注频段内 $|G(j\omega) - \hat{G}(j\omega)|$ 足够小 | 宽频等值 |
| 物理意义 | 保留有明确物理对应的状态 | 可解释性优先 |

## 代表性来源

| 来源或论文线索 | 支撑内容 | 证据边界 |
|----------------|----------|----------|
| A review of efficient modeling methods for modular multilevel converters | MMC 高效建模可通过戴维南、受控源和平均值等策略降阶 | 具体提速和误差需绑定原文电平数、步长和模型 |
| Accelerated EMT equivalent model of solid-state transformer | SST 高频链路可通过节点消去形成端口等值 | 结论限于原文 DAB/拓扑和连接方式 |
| A guaranteed passive model for multi-port FDNE using network synthesis | 网络综合可生成无源多端口 FDNE | 适用于满足正实性和频响表格要求的对象 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] | VF 把频域响应压缩为有限阶极点-留数模型 | VF 本身不保证无源或最小阶 |
| [[a-time-domain-approach-to-transmission-network-equivalents-via-prony-analysts-fo]] | Prony 可从时域响应生成外部网络等值 | 假设外部系统线性时不变 |

## 形式化表达

### 状态空间降阶框架

原高阶系统：
$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \quad \mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

其中 $\mathbf{x} \in \mathbb{R}^n$，$n$ 为原始阶数。

低阶近似系统：
$$\dot{\hat{\mathbf{x}}} = \hat{\mathbf{A}}\hat{\mathbf{x}} + \hat{\mathbf{B}}\mathbf{u}, \quad \hat{\mathbf{y}} = \hat{\mathbf{C}}\hat{\mathbf{x}} + \hat{\mathbf{D}}\mathbf{u}$$

其中 $\hat{\mathbf{x}} \in \mathbb{R}^r$，$r \ll n$ 为降阶后阶数。

### 平衡截断方法

通过求解Lyapunov方程获得可控性格拉姆矩阵 $\mathbf{W}_c$ 和可观测性格拉姆矩阵 $\mathbf{W}_o$：

$$\mathbf{A}\mathbf{W}_c + \mathbf{W}_c\mathbf{A}^T + \mathbf{B}\mathbf{B}^T = 0$$
$$\mathbf{A}^T\mathbf{W}_o + \mathbf{W}_o\mathbf{A} + \mathbf{C}^T\mathbf{C} = 0$$

计算平衡变换 $\mathbf{T}$ 使得：
$$\mathbf{T}\mathbf{W}_c\mathbf{T}^T = \mathbf{T}^{-T}\mathbf{W}_o\mathbf{T}^{-1} = \Sigma = \text{diag}(\sigma_1, \sigma_2, ..., \sigma_n)$$

其中Hankel奇异值 $\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_n > 0$。保留前 $r$ 个状态即得降阶模型。

### Krylov子空间矩匹配

构建 $r$ 维Krylov子空间：
$$\mathcal{K}_r(\mathbf{A}, \mathbf{b}) = \text{span}\{\mathbf{b}, \mathbf{A}\mathbf{b}, \mathbf{A}^2\mathbf{b}, ..., \mathbf{A}^{r-1}\mathbf{b}\}$$

通过Arnoldi或Lanczos过程生成正交基，使得降阶系统传递函数在原点附近展开匹配原系统前 $2r$ 个矩。

### 误差界

平衡截断的 $H_\infty$ 误差界：
$$\|\mathbf{G} - \hat{\mathbf{G}}\|_\infty \leq 2\sum_{i=r+1}^{n}\sigma_i$$

## 与相关页面的关系

- [[state-space-method]]：许多 MOR 算法以状态空间模型为输入和输出。
- [[vector-fitting]]：VF 是频域模型压缩的入口，降阶和无源性检查通常在其后进行。
- [[prony-analysis]]：Prony 通过主导模态提取形成时域等值，可视为数据驱动降阶。
- [[fdne-model]]：FDNE 是 MOR 在外部网络和混合仿真接口中的典型应用。
- [[average-value-model]]：平均值模型是一种物理近似降阶，适合系统级动态，不适合开关纹波研究。
- [[sparse-matrix-solver]]：降阶减少矩阵维度，稀疏求解器减少剩余系统的求解成本；两者不是同一类方法。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[noda-a-binary-frequency-region-partitioning-algorithm-for-the-identification-of-|Noda | A Binary Frequency-Region Partitioning Algorithm for ]] | 2007 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[39pes20116039582|39/pes.2011.6039582]] | 2011 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[electromechanical-transient-modeling-of-modular-multilevel-converter-based-multi|Electromechanical Transient Modeling of Modular Multilevel C]] | 2013 |
| [[comparative-study-on-electromechanical-and-electromagnetic-transient-model-for-g|Comparative study on electromechanical and electromagnetic t]] | 2014 |
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies|A Wideband Equivalent Model of Type-3 Wind Power Plants for ]] | 2016 |
| [[flexible-extended-harmonic-domain-approach-for-transient-state-analysis-of-switc|Flexible extended harmonic domain approach for transient sta]] | 2017 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[dual-band-reduced-order-model-of-an-hvdc-link-embedded-into-a-power-network-for-|Dual-Band Reduced-Order Model of an HVDC Link Embedded into ]] | 2019 |
| [[dynamic-model-reduction-of-power-electronic-interfaced-generators-based-on-singu|Dynamic model reduction of power electronic interfaced gener]] | 2019 |
| [[dynamic-model-reduction-of-power-electronic-interfaced-generators-based-on-singu|Dynamic model reduction of power electronic interfaced gener]] | 2019 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[hierarchical-modeling-scheme-for-high-speed-electromagnetic-transient-emt-simula|Hierarchical Modeling Scheme for High-Speed Electromagnetic ]] | 2021 |
| [[exhaustive-modal-analysis-of-large-scale-power-systems-using-model-order-reducti|Exhaustive modal analysis of large-scale power systems using]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[fast-electromagnetic-transient-simulation-of-modular-multilevel-converter-based-|Fast electromagnetic transient simulation of modular multile]] | 2023 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e|Optimized high-frequency white-box transformer model for imp]] | 2023 |
| [[adaptive-variable-step-size-calculation-method-for-transient-temperature-rise-and-fall|Adaptive Variable Step Size Calculation Method for Transient]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod|A State Variables Elimination-Based EMTP-Type Constant Admit]] | 2025 |
| [[a-state-space-approach-for-accelerated-simulation-of-modular-multilevel-converte|A state-space approach for accelerated simulation of modular]] | 2025 |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based|A state-variable-preserving method for the efficient modelli]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor|EMT Model Boundary Determination Using Floquet Theory-based ]] | 2026 |
