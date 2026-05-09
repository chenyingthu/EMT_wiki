---
title: "特征值分析 (Eigenvalue Analysis)"
type: method
tags: [eigenvalue, linear-algebra, stability, numerical-methods, modal, small-signal]
created: "2026-05-02"
---

# 特征值分析 (Eigenvalue Analysis)


```mermaid
graph TD
    subgraph Ncmp[特征值分析 (Eigenvalue Analysis)]
        N0[QR/Schur: 中小规模稠密标准特征值问题]
        N1[QZ/广义 Schur: 矩阵束 $(\mathbf{A…]
        N2[Arnoldi/Krylov: 大规模稀疏非对称矩阵]
        N3[Shift-invert: 靠近指定频率或虚轴的特征值]
        N4[幂法/反幂法: 简单主导特征值或教学场景]
    end
```


## 定义与边界

特征值分析是求解线性算子或矩阵谱结构的数学操作。对标准问题，

$$
\mathbf{A}\mathbf{v}=\lambda\mathbf{v},
$$

$\lambda$ 为特征值，$\mathbf{v}$ 为右特征向量。在线性化动态系统中，特征值可用于解释局部增长、衰减、振荡频率和时间尺度。

本页覆盖特征值作为数学和数值方法的角色。它不等同于[[small-signal-stability]]，也不等同于完整的[[modal-analysis]]。只有当矩阵来源、运行点、坐标系和线性化假设明确时，特征值才可被解释为 EMT 或电力系统动态模态。

## EMT 中的作用

EMT 相关研究中，特征值分析常出现在四类位置：

- 对连续时间状态矩阵 $\mathbf{A}$ 求谱，判断运行点附近的小扰动趋势。
- 对离散状态矩阵 $\mathbf{A}_d$ 或周期状态转移矩阵 $\mathbf{\Phi}(T)$ 求谱，分析采样或周期开关系统。
- 对 DAE 线性化后的矩阵束使用[[generalized-eigenvalue-method]]。
- 对频域阻抗/导纳矩阵或闭环增益矩阵求特征值轨迹，辅助 MIMO 小信号稳定判断。

这些对象都叫“特征值”，但稳定判据不同。连续时间通常看实部，离散时间通常看单位圆内外，频域矩阵通常看随频率变化的矩阵谱或 Nyquist 类判据。

## 核心机制

若状态空间模型为

$$
\Delta\dot{\mathbf{x}}=\mathbf{A}\Delta\mathbf{x},
$$

且 $\mathbf{A}$ 可对角化，则

$$
\mathbf{A}=\mathbf{V}\mathbf{\Lambda}\mathbf{V}^{-1},\quad
\Delta\mathbf{x}(t)=\sum_i c_i\mathbf{v}_i e^{\lambda_i t}.
$$

复特征值 $\lambda_i=\sigma_i+j\omega_i$ 中，$\sigma_i$ 控制指数增长或衰减，$\omega_i$ 控制振荡角频率。阻尼比可写为

$$
\zeta_i=-\frac{\sigma_i}{\sqrt{\sigma_i^2+\omega_i^2}}.
$$

若模型为离散时间

$$
\Delta\mathbf{x}_{k+1}=\mathbf{A}_d\Delta\mathbf{x}_k,
$$

则模态响应为 $z_i[k]=\mu_i^k z_i[0]$。局部稳定解释通常与 $|\mu_i|<1$ 相关。若要换算到连续时间，需要说明采样周期 $T_s$ 和映射，例如

$$
\lambda_i=\frac{1}{T_s}\log(\mu_i),
$$

并处理复对数分支带来的频率混叠问题。

## 数值算法

| 算法 | 适用对象 | 输出 | 注意事项 |
|---|---|---|---|
| QR/Schur | 中小规模稠密标准特征值问题 | 全部或大部分特征值 | 数值实现通常通过 Schur 形式，而不是显式求特征向量矩阵逆 |
| QZ/广义 Schur | 矩阵束 $(\mathbf{A},\mathbf{B})$ | 广义特征值 | 适合[[generalized-eigenvalue-method]]；避免显式 $\mathbf{B}^{-1}\mathbf{A}$ |
| Arnoldi/Krylov | 大规模稀疏非对称矩阵 | 部分 Ritz 值和向量 | 需选择目标谱区、重启策略和残差容差 |
| Shift-invert | 靠近指定频率或虚轴的特征值 | 目标附近特征值 | 每步需要求解线性系统；矩阵病态会影响结果 |
| 幂法/反幂法 | 简单主导特征值或教学场景 | 单个或少量特征值 | 对非正规矩阵和聚集特征值不稳健 |

工程页面不应把某个算法写成固定优选。算法选择取决于矩阵规模、稀疏性、是否广义问题、目标频段、条件数和需要的特征向量精度。

## 解释要点

### 特征值

特征值给出线性模型的自然响应时间尺度。实部接近零或离散特征值接近单位圆的模态通常更需要关注，但“接近”的工程含义必须由具体准则或研究目标定义。

### 右特征向量

右特征向量描述模态在状态变量上的相对幅值和相位，是[[modal-analysis]]中模态形状的基础。其数值受归一化和状态单位影响，不能单独当作能量贡献。

### 左特征向量

左特征向量描述扰动投影到模态坐标的权重。左、右特征向量共同用于参与因子、留数和参数灵敏度。

### 残差与可信度

特征值结果应至少检查残差：

$$
r_i=\|\mathbf{A}\mathbf{v}_i-\lambda_i\mathbf{v}_i\|.
$$

对于广义问题，应检查 $\|\mathbf{A}\mathbf{v}_i-\lambda_i\mathbf{B}\mathbf{v}_i\|$。若矩阵病态、特征值重合或系统非正规，特征向量和参与因子可能比特征值本身更敏感。

## 适用边界与失败模式

- 未说明矩阵来源时，特征值没有工程含义。
- 把离散特征值、Floquet 乘子和连续特征值混用会导致错误频率或阻尼解释。
- 显式求逆 $\mathbf{A}^{-1}$ 或 $\mathbf{B}^{-1}\mathbf{A}$ 可能放大数值误差。
- 对代数约束消元后的矩阵求谱时，应检查消元矩阵是否奇异或近奇异。
- 参与因子受状态缩放影响，不能不加说明地比较不同模型。
- 大扰动、保护动作、饱和和模式切换不由局部特征值直接覆盖。

## 代表性证据

| 来源 | 特征值作用 | 可采信边界 |
|---|---|---|
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-]] | 对 EMT companion-circuit 形成的离散状态转移矩阵求特征值 | 支撑采样数据小信号分析机制；需剔除或解释数值伪模态 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana]] | 对 Modelica 线性化 A 矩阵做特征值扫描 | 支撑 PV 场站运行点筛查；定量效率和精度需回到原文 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 对单周期状态转移矩阵求 Floquet 乘子并计算参与因子 | 支撑周期 EMT 模态解释；不覆盖非周期强暂态 |
| [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits]] | 用状态空间特征值说明频移和步长对暂态模态的影响 | 可用于说明特征值解释步长边界；不提供普遍加速结论 |

## 与相关页面的关系

- [[small-signal-stability]]：使用特征值判断局部扰动趋势。
- [[small-signal-stability-analysis]]：把特征值求解放入完整分析流程。
- [[modal-analysis]]：在特征值基础上解释特征向量、参与因子和灵敏度。
- [[modal-decomposition]]：用特征值和特征向量展开时间响应。
- [[generalized-eigenvalue-method]]：处理矩阵束和 DAE 相关谱问题。
- [[dae-solvers]]：解释状态矩阵或矩阵束来自何种 DAE/残差结构。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[damping-multimodal-subsynchronous-resonance-using-a-generator-terminal-subsynchr|Damping multimodal subsynchronous resonance using a generato]] | 2013 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[damping-of-subsynchronous-control-interactions-in-large-scale-pv-installations-t|Damping of Subsynchronous Control Interactions in Large-Scal]] | 2021 |
| [[an-automatable-approach-for-small-signal-stability-analysis-of-power-electronic-|An Automatable Approach for Small-Signal Stability Analysis ]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[fast-investigation-of-control-interaction-risks-in-pv-parks-using-eigenvalue-ana|Fast investigation of control interaction risks in PV parks ]] | 2025 |
