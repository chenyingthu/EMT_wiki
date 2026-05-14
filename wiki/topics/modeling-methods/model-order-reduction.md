---
title: "模型降阶与动态等值 (Model Order Reduction and Dynamic Equivalents)"
type: topic
tags: [model-order-reduction, mor, dynamic-equivalent, network-equivalent, emt]
created: "2026-05-01"
book-chapter: "16"
---

# 模型降阶与动态等值 (Model Order Reduction and Dynamic Equivalents)


```mermaid
graph TD
    subgraph Ncmp[模型降阶与动态等值 (Model Order Reduc…]
        N0[轻度降阶: $\eta < 50\%$]
        N1[中度降阶: $50\% \leq \eta < 90\%$]
        N2[深度降阶: $90\% \leq \eta < 99\%$]
        N3[极限降阶: $\eta \geq 99\%$]
    end
```


## 概述

模型降阶（Model Order Reduction, MOR）是将高维复杂系统转化为低维等效表示的数学技术，在保持关键动态特性的同时显著提升计算效率。动态等值（Dynamic Equivalent）则是面向外部网络或子系统的简化表示，通过端口特性匹配实现大系统解耦。

在EMT仿真中，模型降阶与动态等值解决的核心矛盾：
- **规模增长**：含数千子模块的MMC、大规模新能源场站导致维数灾难
- **精度需求**：电力电子设备暂态细节不可忽略
- **计算限制**：实时仿真和在线应用的时间约束

降阶比定义：
$$
\eta = \frac{N - n}{N} \times 100\%
$$
其中 $N$ 为原始阶数，$n$ 为降阶后阶数。

## 作用机制

### 16.1 数学基础

**状态空间降阶框架**

原始高阶系统：
$$
\dot{x} = Ax + Bu, \quad y = Cx + Du, \quad x \in \mathbb{R}^N
$$

降阶目标：构造低阶系统
$$
\dot{\hat{x}} = \hat{A}\hat{x} + \hat{B}u, \quad \hat{y} = \hat{C}\hat{x} + \hat{D}u, \quad \hat{x} \in \mathbb{R}^n
$$

使输出误差 $||y - \hat{y}||$ 在关注频段内最小化。

**降阶等级分类**

| 降阶等级 | 降阶比 | 典型应用 | 精度水平 |
|----------|--------|----------|----------|
| 轻度降阶 | $\eta < 50\%$ | 变压器多绕组等效 | 极高(误差<1%) |
| 中度降阶 | $50\% \leq \eta < 90\%$ | FDNE有理函数拟合 | 高(误差<5%) |
| 深度降阶 | $90\% \leq \eta < 99\%$ | MMC桥臂整体等效 | 中(误差<10%) |
| 极限降阶 | $\eta \geq 99\%$ | 平均值模型 | 低(系统级适用) |

### 16.2 基于投影的降阶方法

**Krylov子空间法**

匹配传递函数矩：
$$H(s) = m_0 + m_1 s + m_2 s^2 + ...$$

Arnoldi算法构造投影矩阵：
$$
\mathcal{K}_n = \text{span}\{B, AB, A^2B, ..., A^{n-1}B\}
$$

优势：计算高效，适合单端口/少端口网络。

**平衡截断法**

基于可控/可观Gramian矩阵：
$$W_c = \int_0^{\infty} e^{At}BB^Te^{A^Tt}dt$$
$$W_o = \int_0^{\infty} e^{A^Tt}C^TCe^{At}dt$$

截断弱可控/弱可观状态，保证全局误差界：
$$
||H - H_r||_{\infty} \leq 2\sum_{i=n+1}^{N}\sigma_i$$

其中 $\sigma_i$ 为Hankel奇异值。

**模态分析法**

保留主导特征值：
$$\lambda_1, \lambda_2, ..., \lambda_n \quad (n \ll N)$$

适用条件：特征值分离度好，快动态可忽略。

### 16.3 基于电路综合的降阶方法

**Brune综合法**

直接从阻抗频响表格综合RLCM网络：

步骤1：移除虚轴极点（s=0, s=∞, 谐振点）  
步骤2：移除虚轴零点（导纳域极点）  
步骤3：提取最小实部电阻  
步骤4：Tellegen-Brune循环提取耦合电感

优势：物理网络天然无源，无需后处理。

**Kron节点消去法**

分块导纳方程消去内部节点：
$$
\begin{bmatrix} I_E \\ 0 \end{bmatrix} = \begin{bmatrix} Y_{EE} & Y_{EI} \\ Y_{IE} & Y_{II} \end{bmatrix} \begin{bmatrix} V_E \\ V_I \end{bmatrix}
$$

等效导纳矩阵：
$$Y_{EX} = Y_{EE} - Y_{EI}Y_{II}^{-1}Y_{IE}$$

应用：MMC子模块内部节点消去、变压器绕组等效。

### 16.4 基于物理近似的降阶方法

**多时间尺度分解**

快慢变量分离：
$$x = \begin{bmatrix} x_f \\ x_s \end{bmatrix}, \quad \dot{x}_f = A_f x_f + B_f u$$

准稳态近似：
$$x_f \approx -A_f^{-1}B_f u$$

降阶后仅求解慢动态，计算量显著降低。

**开关周期平均化**

将离散开关变量替换为连续调制量：
$$\bar{v}_{out}(t) = d(t) \cdot V_{dc}$$

适用于控制策略验证和系统级分析。

### 16.5 外部网络动态等值

**频率相关网络等值（FDNE）**

宽频阻抗有理函数逼近：
$$Z(s) \approx \sum_{m=1}^{n}\frac{R_m}{s-p_m} + D + sE$$

降阶效果：数千个频域采样点 → 数十个极点。

**Ward等值**

静态等值：仅保留基频特性
$$Y_{eq} = Y_{EE} - Y_{EI}Y_{II}^{-1}Y_{IE}$$

适用：潮流计算，不适用于暂态分析。

**多端口等值**

保留端口间耦合：
$$
\begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_m \end{bmatrix} = Y_{eq}^{m \times m} \begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_m \end{bmatrix}
$$

应用于多馈入直流系统接口。

## 适用边界

- **线性/弱非线性系统**：RLC网络、线性化控制系统适合降阶；强非线性（电弧、饱和）降阶误差难控制
- **频段限制明确**：关注频段外动态可忽略；全频段细节需求限制降阶比
- **拓扑稳定性**：Kron消去法要求拓扑相对固定，频繁开关系统需配合其他方法
- **实时约束**：降阶后计算量仍需满足步长时限
- **精度要求**：保护整定误差<1%，系统级暂态<5%，概念验证<10%

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[model-order-reduction]] | 综合 | 降阶方法综述与分类 |
| [[vector-fitting]] | 2006+ | FDNE频域降阶核心算法 |
| [[fdne-model]] | 2010+ | 频率相关网络等值 |
| [[mmc-model]] | 2015+ | 桥臂戴维南等效降阶 |
| [[network-equivalent]] | 综合 | 外部网络动态等值 |
| [[electromechanical-electromagnetic-hybrid]] | 2017+ | 混合仿真接口等值 |
| [[thevenin-norton-equivalent]] | 综合 | 端口等效基础理论 |

## 技术演进脉络

### 1960s-1980s：经典等值理论
- **Ward等值**：静态网络简化
- **REI等值**：保留外部网络发电机的动态影响
- **Prony分析**：从时域响应提取等值模型

### 1990s-2000s：频域降阶突破
- **矢量拟合（VF）**：1999年Gustavsen提出，成为FDNE标准算法
- **Krylov子空间**：矩匹配方法应用于电力系统
- **平衡截断**：Hankel范数降阶理论成熟

### 2000s-2010s：宽频与实时化
- **多端口FDNE**：考虑端口间耦合
- **Brune综合**：保证无源性的网络综合
- **实时降阶**：RTDS平台实现降阶模型实时运行

### 2010s-2020s：电力电子专项
- **MMC戴维南等效**：2010年提出，支持千级子模块
- **SST高频链路降阶**：节点消去法应用
- **风电场聚合**：等效降阶用于大规模新能源

### 2020s-2026：智能化降阶
- **数据驱动降阶**：机器学习辅助模型简化
- **自适应降阶**：在线调整降阶阶数
- **多物理场降阶**：电磁-热-机械联合简化

## 关键发现汇总

### FDNE降阶效果
- **[2008]** 230kV三相输电网络：原始640ms仿真 → FDNE降阶后194ms（3.3倍加速）
- **[2012]** 三端口网络仅需80个RLCM模块等效，频带0.1Hz-2kHz
- **[2019]** 整体矢量拟合法相比基频等值，多馈入场景误差从8-12%降至<1%

### MMC高效建模
- **[2015]** 戴维南模型使计算复杂度从$O(N^2)$降至$O(N)$
- **[2021]** 200子模块MMC：详细模型指数增长 vs 等效模型线性增长，提速15-20倍
- **[2024]** 解耦详细等效模型支持5000+子模块实时仿真

### 固态变压器降阶
- **[2022]** 高频链路Kron消去法实现1-2个数量级提速（10-100倍）
- **[2023]** DAB模块端口等效消除单步矩阵求逆运算

### 实时仿真应用
- **[2020]** FPGA实现80模块RLC网络实时运行
- **[2023]** 稀疏求解器MKLU集成，实时EMT仿真效率大幅提升

## 深度增强内容

### 1. 降阶方法选择指南

| 应用场景 | 推荐方法 | 关键参数 | 注意事项 |
|---------|---------|---------|---------|
| **FDNE宽频等值** | 矢量拟合+Brune综合 | 极点数10-30 | 无源性验证 |
| **MMC桥臂建模** | 戴维南等效 | 子模块数N | 电容电压均衡 |
| **SST高频链路** | Kron节点消去 | 内部节点数k | 拓扑固定 |
| **变压器宽频** | 平衡截断 | 保留阶数15-25 | 频段覆盖 |
| **外部网络等值** | 多端口FDNE | 端口数m | 耦合保留 |
| **控制设计** | 平均值模型 | 开关频率比 | 适用边界验证 |

### 2. 误差控制策略

**频域验证**：
$$\epsilon(\omega) = \frac{|H(j\omega) - \hat{H}(j\omega)|}{|H(j\omega)|} \times 100\%$$

**时域验证**：
- 与详细模型波形对比
- 特征量（峰值、超调、稳定时间）误差<5%

**无源性强制**：
$$\text{Re}\{u^*Y(s)u\} > 0, \quad \forall \text{Re}\{s\} > 0$$

### 3. 典型参数参考表

| 应用场景 | 原始阶数 | 降阶后 | 降阶比 | 误差 | 加速比 |
|---------|---------|-------|-------|------|-------|
| FDNE输电网络 | 100-500 | 10-30 | 70-95% | <2% | 3-5x |
| MMC桥臂 | 50-1000 | 1-2 | 99%+ | <0.5% | 15-20x |
| SST高频链路 | 20-100 | 2 | 90-98% | <1% | 10-100x |
| 变压器宽频 | 50-150 | 10-25 | 80-90% | <3% | 2-4x |
| 风电场聚合 | 100-1000 | 5-20 | 95-99% | <5% | 5-10x |

### 4. 前沿研究方向

**数据驱动降阶**：
- 神经网络逼近高维系统动态
- 强化学习优化降阶阶数
- 在线参数自适应更新

**多物理场耦合降阶**：
- 电磁-热联合降阶
- 电-磁-机-热统一简化
- 多域接口等值方法

**实时自适应降阶**：
- 根据扰动强度动态调整阶数
- 事件触发的模型切换
- 数字孪生在线更新

### 5. 软件实现要点

**PSCAD/EMTDC**：
- FDNE模块：外部网络频域扫描+矢量拟合
- 戴维南MMC模型：桥臂等效构建

**MATLAB**：
- Control System Toolbox：balreal/modred
- 自定义Krylov实现

**实时仿真器**：
- RTDS：预计算降阶参数，固定步长
- FPGA：流水线并行加速状态更新

## 相关方法
- [[vector-fitting]] - FDNE频域降阶核心算法
- [[thevenin-norton-equivalent]] - 端口等效建模基础
- [[iterative-solvers]] - 矩匹配降阶方法
- 平衡截断 - Hankel范数降阶
- [[network-equation-solution]] - 节点消去等效
- [[wideband-modeling]] - 频变参数降阶应用

## 相关模型
- [[fdne-model]] - 外部网络降阶等值
- [[mmc-model]] - 桥臂整体降阶应用
- [[pet-sst-model]] - 高频链路多端口降阶
- [[transformer-model]] - 宽频特性降阶
- [[wind-farm-modeling]] - 大规模新能源聚合

## 相关主题
- [[network-equivalent]] - 系统级降阶应用
- [[electromechanical-electromagnetic-hybrid]] - 混合接口等值
- [[real-time-simulation]] - 降阶实现实时计算
- [[frequency-dependent-modeling]] - 频域降阶基础
- [[co-simulation]] - 多求解器协同降阶

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第四篇第16章"模型降阶与动态等值"*

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