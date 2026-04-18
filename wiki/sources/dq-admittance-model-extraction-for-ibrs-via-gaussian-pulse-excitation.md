---
title: "DQ Admittance Model Extraction for IBRs via Gaussian Pulse Excitation"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Power Systems;2023;38;3;10.1109/TPWRS.2023.3256119"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/DQ_Admittance_Model_Extraction_for_IBRs_via_Gaussian_Pulse_Excitation.pdf"]
---

# DQ Admittance Model Extraction for IBRs via Gaussian Pulse Excitation

**作者**: 
**年份**: 2023
**来源**: `13&14/files/DQ_Admittance_Model_Extraction_for_IBRs_via_Gaussian_Pulse_Excitation.pdf`

## 摘要

—While dq admittance models have shown to be very useful for stability analysis, extracting admittance models of inverter-based resources (IBRs) from the electromagnetic transient (EMT) simulation environment using frequency scans takes time. In this letter, a new perturbation method based on Gaussian pulses in combination with the system identiﬁcation algorithms shows great promise for parametric dq admittance model extraction. We present the dq admittance model extracting method for a type-4 wind turbine. Challenges in implementing Gaussian pulse excitation are also pointed out. The extracted dq admittance model via the new method shows to have a high matching degree with the measurements obtained from frequency scans. Index Terms—Inverter-based resources, admittance model, measurement. 

## 核心贡献


- 提出高斯脉冲激励法替代传统扫频，实现IBR参数化dq导纳模型快速提取。
- 结合系统辨识工具变量法，直接从时域数据辨识传递函数，避免非参数拟合步骤。
- 揭示高斯脉冲在EMT仿真中的实现难点，并通过扫频与调频信号验证模型高精度。


## 使用的方法


- [[高斯脉冲激励|高斯脉冲激励]]
- [[系统辨识|系统辨识]]
- [[工具变量法|工具变量法]]
- [[频率扫描法|频率扫描法]]
- [[线性调频信号注入|线性调频信号注入]]


## 涉及的模型


- [[type-4风电机组|Type-4风电机组]]
- [[dq导纳模型|dq导纳模型]]
- [[永磁同步发电机|永磁同步发电机]]
- [[网侧变流器|网侧变流器]]
- [[逆变器并网资源|逆变器并网资源]]


## 相关主题


- [[导纳模型提取|导纳模型提取]]
- [[稳定性分析|稳定性分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统辨识|系统辨识]]
- [[风电机组建模|风电机组建模]]


## 主要发现


- 高斯脉冲激励大幅缩短仿真时间，单次实验即可替代数百次传统扫频获取完整频响。
- 提取的参数化dq导纳模型与扫频测量数据高度吻合，验证了频域辨识精度。
- 工具变量法辨识的传递函数模型，相比状态空间预测误差法具有更高的训练数据匹配度。



## 方法细节

### 方法概述

本文提出一种基于高斯脉冲激励与系统辨识相结合的参数化dq导纳模型快速提取方法，以替代传统耗时的频率扫描法。该方法在电磁暂态（EMT）仿真环境中，向逆变器并网资源（IBR）的d轴和q轴电压端口注入平滑的高斯脉冲信号，记录对应的dq轴电流响应。利用MATLAB系统辨识工具箱中的`tfest`函数，结合工具变量法（IV）直接从时域输入输出数据中辨识出传递函数形式的2×2 dq导纳矩阵。通过从低阶开始逐步增加模型阶数直至拟合优度不再显著提升的策略，避免过拟合。最终利用线性调频（Chirp）信号进行独立验证，并与传统扫频结果进行频域对比，确保模型在次同步频段的精度与可靠性。

### 数学公式


**公式1**: $$$g(t) = \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{t^2}{2\sigma^2}}$$$

*高斯脉冲时域表达式，用于生成平滑无突变的激励信号，σ控制脉冲宽度*


**公式2**: $$$G(f) = e^{-\frac{1}{2}(2\pi\sigma f)^2}$$$

*高斯脉冲频域表达式，表明其频谱同样为高斯分布，窄时域脉冲可覆盖宽频带*


**公式3**: $$$\begin{bmatrix} i_d(s) \\ i_q(s) \end{bmatrix} = \begin{bmatrix} Y_{dd}(s) & Y_{dq}(s) \\ Y_{qd}(s) & Y_{qq}(s) \end{bmatrix} \begin{bmatrix} v_d(s) \\ v_q(s) \end{bmatrix}$$$

*dq坐标系下IBR的导纳模型定义，建立电压输入与电流输出的频域线性关系*


**公式4**: $$$m_1 = \begin{bmatrix} Y_{dd}(s) \\ Y_{qd}(s) \end{bmatrix}, \quad m_2 = \begin{bmatrix} Y_{dq}(s) \\ Y_{qq}(s) \end{bmatrix}$$$

*系统辨识目标传递函数矩阵，将2×2导纳矩阵解耦为两个双输入单输出模型进行独立辨识*


### 算法步骤

1. 步骤1：在MATLAB/Simscape中搭建Type-4风电机组EMT仿真模型，包含永磁同步发电机、整流器、DC-DC升压变换器及处于交流/直流电压控制模式的网侧变流器，并连接至可控三相电压源。

2. 步骤2：设计高斯脉冲激励参数，设定脉冲宽度σ=0.01 s，幅值为额定电压的0.05 p.u.（5%），采样率设为10 kHz，确保信号平滑且满足小信号线性假设。

3. 步骤3：执行两次独立激励实验（Event 1与Event 2），分别向d轴和q轴电压端口注入高斯脉冲，同步记录对应的dq轴电压输入与电流输出时域数据作为训练集。

4. 步骤4：调用MATLAB系统辨识工具箱的`tfest`函数，采用工具变量法（IV）对训练数据进行传递函数辨识，初始设定较低模型阶数。

5. 步骤5：逐步增加传递函数阶数，监控归一化均方根误差（NRMSE）拟合优度，当阶数增加不再显著提升匹配度时停止，确定最优模型阶数以平衡精度与复杂度。

6. 步骤6：生成独立验证数据集，向系统注入频率范围为0.1 Hz至30 Hz的线性调频（Chirp）信号，记录响应数据。

7. 步骤7：将辨识得到的参数化模型$m_1$和$m_2$分别应用于训练集与验证集进行时域仿真对比，并将模型频域响应与传统1-100 Hz频率扫描（200次实验）结果进行Bode图对比，完成模型精度验证。


### 关键参数

- **高斯脉冲宽度(σ)**: 0.01 s（有效覆盖至30 Hz动态）

- **激励幅值**: 0.05 p.u.（5%额定电压，保证小信号线性区）

- **数据采样率**: 10 kHz

- **传统扫频范围**: 1 Hz 至 100 Hz

- **验证信号范围**: 0.1 Hz 至 30 Hz (Chirp信号)

- **辨识算法**: 工具变量法 (Instrumental Variables, IV)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 高斯脉冲激励模型训练与交叉验证 | 使用0.05 p.u.高斯脉冲数据训练得到的传递函数模型，在训练集和Chirp验证集上均表现出极高的时域波形匹配度，NRMSE拟合优度保持在较高水平。 | 单次高斯脉冲实验（含两次轴向注入）即可替代传统方法所需的200次独立正弦扫频实验，数据生成时间大幅缩短。 |

| 大扰动非线性失效测试 | 当高斯脉冲幅值增大至0.5 p.u.时，模型在训练集上拟合良好，但在Chirp验证集上的匹配度骤降至8%，表明系统已偏离线性工作区。 | 验证了小信号假设的必要性，证明0.05 p.u.幅值在避免触发非线性动态与保证信噪比之间取得最佳平衡。 |

| 频域导纳特性对比 | 辨识得到的dq导纳模型幅频与相频特性曲线在0.1 Hz至30 Hz范围内与传统频率扫描测量数据高度重合，准确捕捉次同步频段动态。 | 避免了传统扫频中逐点提取谐波相量的繁琐后处理步骤，直接输出连续频域参数化模型，且30 Hz以下频段误差极小。 |



## 量化发现

- 传统频率扫描需执行200次独立实验（1-100 Hz），而高斯脉冲法仅需2次轴向激励实验即可完成全频段数据获取，仿真效率提升超两个数量级。
- 高斯脉冲宽度σ=0.01 s时，其频谱能量可有效覆盖并激发0.1 Hz至30 Hz的次同步频段动态特性；若σ增大至0.1 s，则10 Hz以上频段激励能量不足。
- 激励幅值必须控制在0.05 p.u.（5%额定电压）以内以维持系统线性；幅值增至0.5 p.u.将导致独立验证集匹配度暴跌至8%。
- 采用工具变量法（IV）辨识的传递函数模型，其训练数据匹配度显著优于基于预测误差法（PEM）的状态空间辨识函数（ssest）。
- 提取的参数化dq导纳模型在30 Hz以下频段的频域响应与传统扫频基准数据高度一致，验证了该方法在次同步振荡分析中的工程适用性。


## 关键公式

### 高斯脉冲时域激励函数

$$$g(t) = \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{t^2}{2\sigma^2}}$$$

*用于EMT仿真中替代理想冲激信号，提供平滑、无突变且频谱连续的宽频带小扰动输入*

### dq坐标系导纳矩阵模型

$$$\begin{bmatrix} i_d(s) \\ i_q(s) \end{bmatrix} = \begin{bmatrix} Y_{dd}(s) & Y_{dq}(s) \\ Y_{qd}(s) & Y_{qq}(s) \end{bmatrix} \begin{bmatrix} v_d(s) \\ v_q(s) \end{bmatrix}$$$

*描述IBR端口电压与电流的频域线性耦合关系，是稳定性分析与阻抗建模的核心数学表达*

### 解耦辨识目标传递函数

$$$m_1 = \begin{bmatrix} Y_{dd}(s) \\ Y_{qd}(s) \end{bmatrix}, \quad m_2 = \begin{bmatrix} Y_{dq}(s) \\ Y_{qq}(s) \end{bmatrix}$$$

*将2×2多变量导纳矩阵拆分为两个独立的双输入单输出传递函数，便于使用`tfest`进行系统辨识*



## 验证详情

- **验证方式**: 仿真对比验证（时域交叉验证 + 频域扫频基准对比）
- **测试系统**: 基于MATLAB/Simscape搭建的Type-4风电机组并网系统（含永磁同步发电机、整流器、DC-DC升压变换器及处于交流电压/直流电压控制模式的网侧变流器），连接至可控三相电压源
- **仿真工具**: MATLAB/Simscape (EMT电磁暂态仿真环境), MATLAB System Identification Toolbox (`tfest`函数)
- **验证结果**: 提取的参数化dq导纳模型在时域上对高斯脉冲训练数据和线性调频（Chirp）验证数据均表现出高匹配度；在频域上，模型幅频/相频特性在0.1-30 Hz次同步范围内与传统200点频率扫描结果高度一致。验证了该方法在保证精度的前提下大幅缩短仿真时间，且明确了小扰动幅值（≤5%）对维持线性辨识精度的关键作用。
