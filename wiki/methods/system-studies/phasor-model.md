---
title: "相量模型 (Phasor Model)"
type: method
tags: [phasor, rms, steady-state, frequency-domain, electromechanical]
created: "2026-05-02"
---

# 相量模型 (Phasor Model)


```mermaid
graph TD
    subgraph Ncmp[相量模型 (Phasor Model)]
        N0[静态相量: 潮流、稳态短路、基频等值]
        N1[RMS 动态模型: 机电暂态和控制慢动态]
        N2[对称分量相量: 线性不平衡故障的序网络分析]
        N3[动态相量: 用时变傅里叶系数描述选定频率分量]
        N4[谐波相量: 多个谐波频率的相量耦合]
    end
```


## 定义与边界

相量模型把单一频率正弦量表示为复数有效值和相角。若

$$
v(t)=\sqrt{2}V\cos(\omega_0 t+\theta_v),\qquad
i(t)=\sqrt{2}I\cos(\omega_0 t+\theta_i),
$$

则相量为

$$
\bar{V}=Ve^{j\theta_v},\qquad \bar{I}=Ie^{j\theta_i}.
$$

这个表示只保留选定频率的幅值和相位，不保留开关沿、非周期暂态、高频谐波和直流偏移。它不同于 [[three-phase-instantaneous-model]]：后者直接求解 $abc$ 时域瞬时值，适合 EMT 中的开关、饱和、故障行波和宽频暂态。

## EMT 中的作用

在 EMT 知识体系中，相量模型主要用于边界、初始化和近似接口，而不是替代详细 EMT 求解：

- 为 EMT 初始条件提供潮流或稳态相量解。
- 在 [[electromechanical-electromagnetic-hybrid-simulation]] 中连接机电暂态侧和 EMT 侧。
- 表示外部交流系统的基频等值，配合 [[thevenin-equivalent]] 或 [[norton-equivalent]] 使用。
- 为频域阻抗、动态相量和小信号分析提供基频参考。

因此，相量模型适合描述慢变化基频包络；当研究对象依赖瞬时波形、开关函数、谐波相互作用或暂态过电压时，应回到 [[time-domain-formulation]]、[[three-phase-instantaneous-model]] 或 [[dynamic-phasor]]。

## 核心方程

在线性正弦稳态条件下，微分关系可写为代数阻抗：

$$
\frac{d}{dt}\rightarrow j\omega_0,\qquad
\int(\cdot)\,dt\rightarrow \frac{1}{j\omega_0}.
$$

常见元件的相量关系为：

$$
\bar{V}_R=R\bar{I},\qquad
\bar{V}_L=j\omega_0 L\bar{I},\qquad
\bar{I}_C=j\omega_0 C\bar{V}.
$$

网络节点方程写为：

$$
\mathbf{Y}(\omega_0)\mathbf{V}=\mathbf{I}.
$$

复功率采用共轭电流定义：

$$
\bar{S}=\bar{V}\bar{I}^{*}=P+jQ.
$$

这些方程的证据边界是线性、单频、稳态或准稳态。若电感饱和、开关状态突变或频率含量宽，$j\omega_0$ 代换不能代表完整时域响应。

## 变体

| 变体 | 主要用途 | 与 EMT 的关系 |
|------|----------|---------------|
| 静态相量 | 潮流、稳态短路、基频等值 | 常用于 EMT 初始化或外部系统等值 |
| RMS 动态模型 | 机电暂态和控制慢动态 | 可作为混合仿真慢侧模型 |
| 对称分量相量 | 线性不平衡故障的序网络分析 | 适合基频故障近似，不保留暂态波形 |
| 动态相量 | 用时变傅里叶系数描述选定频率分量 | 比静态相量更接近 EMT，但仍是频带截断模型 |
| 谐波相量 | 多个谐波频率的相量耦合 | 可分析周期稳态谐波，不等同于开关级 EMT |

## 适用边界与失败模式

- **非正弦波形**：相量只代表某一频率分量；谐波和直流分量必须另建模或后处理。
- **快速暂态**：断路器操作、行波、换流器开关沿和雷电暂态不满足准稳态假设。
- **强非线性**：饱和、限幅、保护动作和器件状态切换会使固定阻抗矩阵失效。
- **频率偏移**：频率快速变化时，固定 $\omega_0$ 的相量模型会产生幅相解释误差。
- **不平衡系统**：单一正序相量不足以描述负序、零序和相间耦合；必要时应使用 [[symmetrical-components]] 或相域瞬时模型。

## 代表性证据边界

本页采用的是教材级和方法页级的基础关系，不把任何单篇论文结果外推为领域结论。相关证据边界包括：

- [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-]] 代表相量域与时域混合仿真的接口问题，不能证明相量模型可替代所有 EMT 细节。
- [[a-harmonic-phasor-domain-co-simulation-method-and-new-insight-for-harmonic-analy]] 代表谐波相量域用于周期谐波分析，证据范围不同于开关瞬时波形仿真。
- [[dynamic-phasor]] 页面讨论时变频率系数，适合作为静态相量和 EMT 之间的中间表示。

## 与相关页面的关系

- [[three-phase-instantaneous-model]]：保留 $abc$ 瞬时值，是详细 EMT 建模的直接对照。
- [[average-value-model]]：平均掉开关周期细节，通常仍在时域中保留控制和低频动态。
- [[state-space-average-method]]：把开关状态方程按占空比平均，常用于变换器平均模型推导。
- [[switching-function-method]]：从二值开关函数出发，可得到详细开关模型或平均值模型。
- [[power-flow-calculation]]：提供相量稳态初值，但不验证 EMT 暂态精度。

## 开放问题

相量模型在混合仿真中的主要风险不是公式本身，而是接口边界：哪些频率分量被传递、哪些状态被丢弃、以及相量侧延迟如何影响 EMT 侧能量一致性。具体工程模型应通过时域波形、功率平衡和故障工况复核，而不是只检查基频相量误差。
