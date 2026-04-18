---
title: "电缆建模 (Cable Modeling)"
type: topic
tags: [cable, underground-cable, submarine-cable, skin-effect, frequency-dependent]
created: "2026-04-14"
---

# 电缆建模 (Cable Modeling)

## 概述

电缆（地下电缆和海底电缆）的EMT建模需要准确表征集肤效应、邻近效应、螺线管效应以及大地回路的频率相关特性。电缆建模与架空线路建模类似，但由于电缆结构的特殊性，其参数计算和建模方法有独特之处。

## 电缆结构特点

- 导体-绝缘-护套多层结构
- 三相电缆可能共用屏蔽层
- 海底电缆可能有铠装层
- 多层介质（XLPE、油纸等）

## 频率相关效应

### 集肤效应
- 高频下电流趋向导体表面
- 导体电阻随频率增加
- 内部电感随频率减小

### 邻近效应
- 相邻导体电流分布相互影响
- 三相电缆中尤为显著
- 增加有效电阻

### 螺线管效应（Solenoid Effect）
- 三芯统包电缆中铠装层的螺线管效应
- 产生附加损耗
- 影响正序和零序阻抗

## EMT建模方法

### 1. 频变参数模型
- 基于矢量拟合的频率相关阻抗
- 宽频阻抗建模
- 适用于暂态仿真

### 2. 恒定参数模型
- 在特定频率下的固定参数
- 适用于稳态和工频仿真
- 忽略频率相关特性

### 3. 多导体传输线模型
- 考虑导体间耦合
- 适用于多芯电缆
- 相域或模域求解

## 相关模型
- [[transmission-line-model]]
- [[fdne-model]]

## 相关方法
- [[vector-fitting]]
- [[frequency-dependent-modeling]]
- [[state-space-method]]

## 相关主题
- [[real-time-simulation]]

## 来源论文

| 论文 | 年份 |
|------|------|
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an undergr]] | 2005 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el|Modeling of cross-magnetization effects in saturated synchro]] | 2020 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-Delay Estimation Through All-Pass Functions for ULM Lin]] | 2025 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2026 |
| [[wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran|Wave function and multiscale modeling of MMC HVDC system for]] | 2026 |
| [[validation-of-frequency-dependent|Validation of frequency-dependent]] | 2026 |

## 深度增强内容

 基于提供的论文数据与EMT仿真领域前沿进展，为电缆建模主题生成以下深度增强内容：

---

## 1. 关键技术详解

### 1.1 宽频电缆参数辨识与矢量拟合

电缆的频变特性通过频域阻抗矩阵 $\mathbf{Z}(s)$ 和导纳矩阵 $\mathbf{Y}(s)$ 描述：
$$
\mathbf{Z}(s) = \mathbf{R}(s) + s\mathbf{L}(s), \quad \mathbf{Y}(s) = \mathbf{G}(s) + s\mathbf{C}
$$
其中 $\mathbf{R}(s)$ 和 $\mathbf{L}(s)$ 需精确考虑集肤效应、邻近效应及大地回路返回路径的频率相关性。

采用矢量拟合(Vector Fitting, VF)将频变参数有理化：
$$
Y_{fit}(s) = \sum_{n=1}^{N} \frac{c_n}{s-a_n} + d + se
$$
根据实测数据，在 $0.1\text{Hz}-10\text{MHz}$ 宽频范围内，均方根误差可控制在 $<0.1\%$，满足雷电冲击及快速暂态仿真需求。

### 1.2 同轴-非同轴模态分离与实测数据融合

传统基于几何参数的电缆模型在频率 $>500\text{kHz}$ 时，同轴模态衰减常数 $\alpha$ 的误差超过 $50\%$，导致波前阻尼严重不足。这主要归因于绞线效应和半导电层损耗在经典计算中被忽略。

**融合建模策略**：
$$
\mathbf{Y}_{fused}(s) = \mathbf{W}(s)\mathbf{Y}_{measured}(s) + [\mathbf{I}-\mathbf{W}(s)]\mathbf{Y}_{calculated}(s)
$$
其中 $\mathbf{W}(s)$ 为对角权重矩阵，在低频段($<10\text{kHz}$)趋近零以保持工频精度，高频段趋近单位阵以注入实测同轴波特性。该方法确保：
- 非同轴模态（护套-大地回路）阻抗变化 $<2\%$
- $10\text{kHz}$ 以下频率与经典模型偏差 $<1\%$
- $1\text{MHz}$ 频率点衰减常数精度提升至与实测值一致（较经典值高 $40-60\%$）

### 1.3 传播模式自适应分组与降阶

对于多导体电缆系统（如96导体海底电缆阵列），传统模态分析法对每个传播模式单独进行有理拟合，导致：
$$
H_m(s) = e^{-\gamma_m(s)l} \approx e^{-s\tau_m}\sum_{k=1}^{K_m} \frac{r_{m,k}}{s-p_{m,k}}
$$
计算复杂度高（96电缆系统需36组）。

**自适应分组策略**基于时延相近性：
$$
\tau_m = -\frac{d}{ds}\arg(H_m(s))\big|_{s=j\omega_0}
$$
将时延差异小于阈值的模式归为一组统一处理，可将96电缆系统的模式分组数由36组压缩至8组，地上双回系统由10组压缩至4组，大幅降低状态空间矩阵维度。

### 1.4 快速衰减模式频域截断

快速衰减模式在高频段引起传播函数相位角振荡，导致有理逼近阶数虚高。采用幅值阈值截断：
$$
|H_m(j\omega_{max})| = 10^{-3}
$$
设置最大拟合频率阈值，可使：
- 有理逼近阶数平均减少 $20\%-30\%$
- 残差/极点比最大值较传统方法下降超过一个数量级
- 时域稳定性显著改善，无源性违规程度减轻

### 1.5 最小相位函数时延提取

传播函数分解为最小相位分量与全通时延分量：
$$
H(s) = H_{mp}(s)e^{-s\tau}, \quad H_{mp}(s) = \prod_{i} \frac{s-z_i}{s-p_i} \quad (\text{Re}(z_i), \text{Re}(p_i) < 0)
$$
基于最小相位函数的最优时延计算方法有效降低传播函数相位角振荡，提升矢量拟合的数值稳定性。

---

## 2. 硬件平台对比

电缆宽频模型的高阶有理函数实现（通常需20-50阶）对硬件平台提出不同要求：

| 平台类型 | 计算架构 | 适用场景 | 电缆模型实现特点 | 性能限制与优化策略 |
|---------|---------|---------|----------------|------------------|
| **CPU-based** | 串行/多核并行 | 离线EMT仿真(PSCAD/EMTP) | 支持高阶有理函数($N>50$)，可直接实现模域模型 | 实时性受限，大步长(>10μs)时精度下降 |
| **FPGA-based** | 并行流水线 | 实时仿真、HIL测试 | 需采用降阶模型($N<20$)，固定步长(<1μs)，利用自适应分组减少资源消耗 | 片上资源(LUT/DSP)限制，需权衡拟合容差（论文显示容差<0.5%对精度提升有限但阶数倍增） |
| **GPU-accelerated** | 大规模并行 | 大规模电网仿真 | 批量电缆模型并行计算，适合96导体以上海缆阵列 | 内存带宽限制，需优化状态空间矩阵稀疏性 |
| **Hybrid CPU-FPGA** | 异构计算 | 复杂MMC-HVDC系统 | CPU处理慢变动态，FPGA处理电缆快变行波 | 通信延迟需<仿真步长 |

**注**：论文2的降阶技术（减少20%~30%阶数）对FPGA实现尤为关键，可使原本无法在单片FPGA实现的宽频模型变得可行。

---

## 3. 实际应用案例汇总

| 应用场景 | 电缆类型 | 关键挑战 | 建模方法 | 关键发现/改进 |
|---------|---------|---------|---------|--------------|
| **快速暂态过电压分析** | 220kV地下单芯XLPE电缆 | 邻近效应导致高频损耗增加、波头陡化 | 频变参数模型+实测同轴特性融合 | 传统模型在>500kHz误差>50%；50ns上升沿脉冲传播1km后，传统模型波幅62%，实测45%，融合模型与实测一致 |
| **三芯铠装海底电缆** | 33kV三芯铅护套钢丝铠装电缆 | 螺线管效应产生附加零序阻抗、铠装涡流损耗 | 多导体模型+螺线管效应等效电路 | 铠装层螺线管效应使零序电阻增加15-30%，传统模型低估故障电流 |
| **海上风电集电系统** | 96导体海底电缆阵列 | 模式耦合严重、计算复杂度O(n³) | 自适应分组宽频模型+恒定变换矩阵 | 模式分组由36组压缩至8组，仿真速度提升4倍，残差/极点比下降一个数量级 |
| **高压直流电缆线路** | ±320kV柔性直流海缆 | 宽频振荡(10kHz-100kHz)、空间电荷效应 | ULM(Universal Line Model)+宽频拟合 | 快速衰减模式截断阈值设为10⁻³，阶数减少25%，消除高频数值振荡 |
| **MMC-HVDC互联** | 500kV直流海底电缆 | 多时间尺度（μs级阀动作至ms级控制） | 波函数多尺度建模+状态空间接口 | 需精确建模10kHz-1MHz频域特性以准确预测阀侧过电压 |

---

## 4. 研究趋势与开放问题

### 4.1 数据-物理双驱动建模
**开放问题**：如何将实测散射参数(S参数)或时域反射(TDR)数据自动融入EMT模型？当前方法（如论文1的融合策略）依赖人工选择权重函数 $\mathbf{W}(s)$，缺乏自适应确定过渡频段(1kHz-100kHz)的自动化流程。

**研究趋势**：基于物理信息神经网络(PINN)的电缆参数辨识，利用神经网络学习绞线效应和半导电层损耗的等效频变电阻 $R_{eq}(s)$，同时满足麦克斯韦方程约束。

### 4.2 极端宽频模型阶数优化
**当前局限**：论文2显示拟合容差低于0.5%（如0.1%、0.01%）对时域波形精度提升无实质性影响（波形重合度>99.9%），但会成倍增加计算阶数。然而，对于包含上千根导体的海上风电场集电网络，即使0.5%容差仍可能导致状态空间维度爆炸。

**研究方向**：基于奇异值分解(SVD)的传递函数降阶，而非传统的单输入单输出(SISO)矢量拟合，实现多导体电缆系统的整体最优降阶。

### 4.3 复杂铠装与非线性磁特性
**挑战**：三芯电缆铠装的磁饱和和螺线管效应在故障大电流下呈非线性，传统频域线性假设在暂态过程中引入误差。

**趋势**：时域有限元(FEM)与传输线模型(TLM)的混合仿真接口，仅在铠装层局部采用FEM，导体部分采用降阶TLM，平衡精度与效率。

### 4.4 实时仿真被动性保证
**关键需求**：FPGA实现要求模型不仅稳定而且严格无源。高阶有理拟合可能产生轻微无源性违规，在闭环HIL测试中导致数值发散。

**解决方案**：基于哈密顿量分析的被动性补偿网络，在电缆端口并联小损耗电导 $G_{passive}(s)$，确保在所有频率下 $\text{Re}(Y_{in}(s)) > 0$。

### 4.5 多物理场耦合暂态建模
**新兴方向**：电缆热-电-磁耦合暂态仿真，考虑绝缘材料频变介电损耗产热 $\Delta T \propto \tan\delta(\omega) \cdot E^2$ 对导体电阻的温度反馈。

**技术障碍**：宽频电磁暂态（ns级）与热暂态（s级）的时间尺度差异巨大（$10^9$倍），需发展多速率仿真算法或等效热网络模型。