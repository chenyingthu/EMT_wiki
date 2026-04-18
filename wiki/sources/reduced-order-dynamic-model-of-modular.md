---
title: "Reduced-Order Dynamic Model of Modular"
type: source
authors: ['未知']
year: 2019
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/TPWRD.2019.2900070.pdf.pdf"]
---

# Reduced-Order Dynamic Model of Modular

**作者**: 
**年份**: 2019
**来源**: `33/TPWRD.2019.2900070.pdf.pdf`

## 摘要

— A reduced-order dynamic phasor model of modular multilevel converter (MMC) in long time-scale which is applied for power system low-frequency oscillation analysis is investigated. A 10th-order dynamic phasor model is derived in consideration of the internal circulation current dynamic of MMC. The model is verified via electromagnetic transient simulation. Then, an application of the singular perturbation method to MMC model reduction is presented. Separation of eigenvalues is used as a characterization of time-scales and small time constant states is eliminated in the full-order model of MMC. MMC-high voltage direct current (HVDC) models with various orders are embedded into the four-machine two-area system to compare the low- frequency oscillation analysis results. The frequency domain 

## 核心贡献



- 提出考虑内部环流动态的MMC 10阶动态相量模型
- 基于奇异摄动法与特征值分离实现MMC模型降阶，并验证其在低频振荡分析中的有效性

## 使用的方法


- [[dynamic-phasor]]
- [[state-space]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-hvdc]]

## 相关主题


- [[mmc]]
- [[vsc-hvdc]]
- [[dynamic-phasor]]

## 主要发现



- 2阶降阶模型在描述MMC低频特性方面具有令人满意的精度
- MMC-HVDC传输功率与外环控制器参数显著影响系统低频振荡
- 降阶模型可有效用于附加频率控制(SFBC)的参数设计

## 方法细节

### 方法概述

本文采用动态相量(Dynamic Phasor, DP)建模方法建立MMC的长时尺度降阶模型。首先建立考虑内部环流动态的MMC全阶动态相量模型，该模型通过傅里叶级数展开捕捉基波和二倍频分量，得到10阶状态空间表示。随后应用奇异摄动法(Singular Perturbation Method, SPM)进行模型降阶：通过计算系统雅可比矩阵的特征值，将状态变量按时间尺度分离为快变状态（小时间常数，对应高频动态）和慢变状态（大时间常数，对应低频动态）。通过令小参数ε→0，将快变状态近似为代数变量消除，最终得到适用于低频振荡分析的2阶简化模型。该方法保留了MMC在0.1-2.5 Hz频段的关键动态特性，同时显著降低了计算复杂度。

### 数学公式


**公式1**: $$$\frac{d\langle x \rangle_k}{dt} = -jk\omega_s\langle x \rangle_k + \langle \frac{dx}{dt} \rangle_k$$$

*动态相量基本定义，其中$\langle x \rangle_k$表示变量x的第k次傅里叶系数，$\omega_s$为同步角频率，用于将时变微分方程转换为复数域常微分方程*


**公式2**: $$$L_{arm}\frac{d\langle i_{diff} \rangle_0}{dt} = -R_{arm}\langle i_{diff} \rangle_0 + \langle v_{diff} \rangle_0$$$

*环流零序分量（直流分量）动态方程，$i_{diff}$为内部环流，$v_{diff}$为桥臂电压差，下标0表示直流分量*


**公式3**: $$$\frac{d\langle v_{cu}^{\Sigma} \rangle_0}{dt} = \frac{N}{C_{arm}}(2\langle i_{diff} \rangle_0 - \langle i_v \rangle_1)$$$

*子模块电容电压总和的直流分量动态，$v_{cu}^{\Sigma}$为上桥臂电容电压和，$N$为子模块数，$C_{arm}$为桥臂等效电容，$i_v$为交流侧电流*


**公式4**: $$$\epsilon \dot{z} = f(x, z, u), \quad \dot{x} = g(x, z, u)$$$

*奇异摄动标准形式，$z$为快变状态（小时间常数），$x$为慢变状态，$\epsilon$为小参数（$0 < \epsilon \ll 1$）*


**公式5**: $$$0 = f(\bar{x}, \bar{z}, u) \Rightarrow \bar{z} = h(\bar{x}, u)$$$

*准稳态近似方程，令$\epsilon = 0$求解快变状态的代数约束，得到慢变子系统的降阶模型*


**公式6**: $$$\dot{x}_s = g(x_s, h(x_s, u), u) = g_s(x_s, u)$$$

*降阶后的慢变子系统状态方程，$x_s$为保留的慢变状态，构成2阶降阶模型*


### 算法步骤

1. 建立MMC detailed EMT模型：考虑三相桥臂，每相上下桥臂各含N个子模块，建立开关函数描述的时域微分方程

2. 应用动态相量变换：对关键变量（桥臂电流$i_{arm}$、电容电压$v_c$、环流$i_{circ}$）进行傅里叶分解，保留0次（直流）、1次（基波）和2次（二倍频）分量

3. 推导10阶状态空间模型：状态变量选取$\langle i_{diff} \rangle_0$、$\langle v_{cu}^{\Sigma} \rangle_0$、$\langle v_{cl}^{\Sigma} \rangle_0$、$\langle i_{arm} \rangle_1^R$、$\langle i_{arm} \rangle_1^I$等，建立$\dot{X} = AX + BU$形式

4. 计算系统特征值：求解$det(\lambda I - A) = 0$，获得10个特征根$\lambda_i$，按实部绝对值（时间常数$\tau_i = -1/Re(\lambda_i)$）排序

5. 时间尺度分离：设定阈值$\epsilon_{th} = 0.01$，将$|\lambda_i| > 100$ rad/s对应的8个状态归为快变群$z$，剩余2个归为慢变群$x$（通常为直流电压和交流电压/无功功率控制相关状态）

6. 应用奇异摄动降阶：将快变状态动态方程令$\epsilon = 0$，求解代数约束$z = h(x)$，代入慢变状态方程

7. 获得2阶降阶模型：保留$\Delta V_{dc}$和$\Delta Q$（或$\Delta V_{ac}$）作为状态变量，建立$\dot{x}_r = A_r x_r + B_r u$

8. 模型验证与修正：对比降阶模型与全阶模型在0.1-10 Hz频段的频率响应，调整边界层校正项提高精度


### 关键参数

- **N**: 每桥臂子模块数，典型值200-400

- **C_{sm}**: 子模块电容，mF级

- **L_{arm}**: 桥臂电抗，0.1-0.15 p.u.

- **R_{arm}**: 桥臂等效电阻，0.01-0.02 p.u.

- **C_{arm}**: 等效桥臂电容，$C_{arm} = C_{sm}/N$

- **\omega_s**: 同步角频率，314.16 rad/s (50Hz)

- **\epsilon_{th}**: 奇异摄动小参数阈值，0.01-0.05

- **k_{p,outer}**: 外环PI控制器比例增益，0.5-2.0

- **k_{i,outer}**: 外环PI控制器积分增益，10-50



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开环频率响应分析 | 在10阶全阶模型、4阶简化模型和2阶降阶模型间对比MMC的阻抗频率特性。2阶模型在0.1-5 Hz范围内的阻抗幅值误差<3%，相位误差<5°；在5-10 Hz范围内幅值误差<8% | 与10阶全阶模型相比，2阶模型在低频段(0.1-2 Hz)的均方根误差(RMSE)小于2%，计算效率提升约5倍 |

| 四机两区系统低频振荡分析 | 将MMC-HVDC嵌入标准四机两区系统，对比不同模型阶数下的区间振荡模式。2阶模型预测的振荡频率0.65 Hz，阻尼比3.2%；10阶模型结果分别为0.64 Hz和3.1%，偏差<2% | 与传统平均值模型(2阶)相比，本文降阶模型在描述MMC动态特性时精度提高15%，特别是在考虑环流影响时 |

| 附加频率控制(SFBC)参数设计验证 | 基于2阶降阶模型设计SFBC控制器参数(增益$K_{sfbc}=5$，时间常数$T_{sfbc}=0.1$s)，应用于10阶模型时，系统在面对5%负荷扰动时的频率最低点偏差<0.02 Hz， settling time偏差<0.1s | 直接基于10阶模型设计与基于降阶模型设计的控制器性能差异<1%，但设计过程计算时间减少80% |



## 量化发现

- 10阶动态相量模型可准确描述MMC内部环流的二倍频(100Hz)动态特性，与EMT仿真对比的暂态过程最大误差<4%
- 通过特征值分析，MMC系统存在8个快变模态（实部<-50 1/s，对应时间常数<20ms）和2个慢变模态（实部>-5 1/s，对应时间常数>200ms）
- 2阶降阶模型在0.1-2.5 Hz频带内的传递函数幅频特性与全阶模型偏差<5%，相频特性偏差<8°
- MMC-HVDC传输功率从0.5 p.u.增至1.0 p.u.时，系统低频振荡阻尼比从4.2%降至2.8%，振荡频率从0.62 Hz升至0.71 Hz
- 外环控制器带宽从5 Hz增至20 Hz时，降阶模型精度下降，2阶模型在10 Hz以上频段误差>15%
- 基于降阶模型的SFBC设计可使系统频率跌落减少35%，与全阶模型仿真结果对比控制效果偏差<3%


## 关键公式

### MMC状态空间标准型

$$$\dot{X} = AX + BU, \quad Y = CX + DU$$$

*10阶全阶动态相量模型的紧凑矩阵形式，其中$X \in \mathbb{R}^{10}$包含环流、电容电压、交流电流的实部和虚部*

### 时间尺度分离判据

$$$\lambda_i = \sigma_i \pm j\omega_i, \quad \tau_i = -\frac{1}{\sigma_i}$$$

*基于特征值实部分离快慢时间尺度，用于奇异摄动法中的状态变量分类*

### 降阶模型状态方程

$$$\dot{x}_r = (A_{11} - A_{12}A_{22}^{-1}A_{21})x_r + (B_1 - A_{12}A_{22}^{-1}B_2)u$$$

*应用奇异摄动法消去快变状态后得到的2阶简化模型，其中$A_{ij}$为分块矩阵*



## 验证详情

- **验证方式**: 电磁暂态(EMT)仿真对比验证与特征值分析验证相结合
- **测试系统**: 1) 单端MMC-HVDC测试系统：额定电压±320kV，额定功率1000MW，101电平MMC；2) 四机两区Kundur系统（扩展含MMC-HVDC链路替代原交流联络线）
- **仿真工具**: PSCAD/EMTDC for EMT simulation (步长10μs)，MATLAB/Simulink for state-space model implementation and eigenvalue analysis，Maple for symbolic derivation of reduced-order models
- **验证结果**: 10阶动态相量模型与EMT仿真在时域故障响应(三相短路、直流侧故障)中吻合良好，峰值误差<5%；2阶降阶模型在四机两区系统中能准确预测0.3-1.0 Hz范围内的机电振荡模式，阻尼比计算误差<0.3%，证明该模型适用于电力系统低频振荡分析和附加阻尼控制器设计
