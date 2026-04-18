---
title: "Comparison between electromechanical transient model and electromagnetic transient model of DC in lo"
type: source
authors: ['未知']
year: 2013
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Wang 等 - 2013 - Comparison between electromechanical transient model and electromagnetic transient model of DC in lo.pdf"]
---

# Comparison between electromechanical transient model and electromagnetic transient model of DC in lo

**作者**: 
**年份**: 2013
**来源**: `10/Wang 等 - 2013 - Comparison between electromechanical transient model and electromagnetic transient model of DC in lo.pdf`

## 摘要

For AC and DC operating system Low Frequency Oscillation (LFO) Analysis, DC system usually adopts electromechanical transient model. This paper introduces the DC electromechanical transient and electromagnetic transient model, and then establishes the electromechanical transient model and the electromechanical-electromagnetic transient hybrid simulation model on the Advanced Digital Power System Simulator (ADPSS) platform for the LFO analysis respectively. Adopting the total least squares method-rotational invariance techniques of signal parameter estimation (TLS-ESPRIT) algorithm, the oscillation power after failure is analyzed. After extracting the LFO dominant oscillation frequency and damping ratio for making the modal analysis, it compares the LFO analysis results of the two simulatio

## 核心贡献


- 构建直流机电暂态与机电-电磁混合仿真模型，实现交直流系统低频振荡对比分析。
- 引入TLS-ESPRIT算法提取故障后功率信号特征，完成主导频率与阻尼比模态分析。
- 验证直流准稳态模型在低频振荡分析中的有效性，为工程仿真模型选型提供依据。


## 使用的方法


- [[tls-esprit算法|TLS-ESPRIT算法]]
- [[隐式梯形积分法|隐式梯形积分法]]
- [[节点分析法|节点分析法]]
- [[机电-电磁暂态混合仿真|机电-电磁暂态混合仿真]]
- [[准稳态等值建模|准稳态等值建模]]


## 涉及的模型


- [[直流准稳态模型|直流准稳态模型]]
- [[12脉冲换流器|12脉冲换流器]]
- [[换流变压器|换流变压器]]
- [[平波电抗器|平波电抗器]]
- [[交直流滤波器|交直流滤波器]]
- [[直流线路t型集中参数模型|直流线路T型集中参数模型]]
- [[同步发电机|同步发电机]]


## 相关主题


- [[低频振荡分析|低频振荡分析]]
- [[交直流混合系统|交直流混合系统]]
- [[混合仿真|混合仿真]]
- [[模态分析|模态分析]]
- [[直流输电系统建模|直流输电系统建模]]


## 主要发现


- 两种模型仿真结果趋势一致，主导振荡频率接近，阻尼比差异小于0.3%。
- 电磁暂态混合模型能更详细描述故障暂态过程，机电模型可准确反映总体振荡趋势。
- 直流机电暂态准稳态模型在低频振荡分析中具备较高精度与工程实用价值。



## 方法细节

### 方法概述

本文在ADPSS平台上构建交直流混合系统的机电暂态（直流准稳态）模型与机电-电磁暂态混合仿真模型。针对低频振荡分析，交流电网采用机电暂态模型，直流系统分别采用准稳态等值模型和详细电磁暂态模型（含晶闸管阀、R-C缓冲电路、隐式梯形积分离散化元件及详细控制保护）。通过UD模块在机电-电磁接口处进行无功差值补偿以实现数据交互。故障后采集发电机功角及线路功率振荡信号，应用TLS-ESPRIT算法进行高分辨率模态辨识，提取主导振荡频率与阻尼比，并在EPRI36标准系统及实际大电网中对比两种模型在交流故障与直流故障下的低频振荡特性，验证准稳态模型在工程LFO分析中的适用边界。

### 数学公式


**公式1**: $$$$\begin{cases} V_{d0} = \frac{3\sqrt{2}}{\pi} B T V \\ V_d = V_{d0} \cos \alpha - \frac{3}{\pi} X_c I_d B \\ P = V_d I_d \\ Q = P \tan \phi \\ \phi = \arccos \frac{V_d}{V_{d0}} = \theta_V - \theta_I \\ I = \frac{6}{\pi} B T I_d \end{cases}$$$$

*直流12脉动换流器准稳态运行方程组，用于机电暂态模型中计算换流母线注入有功、无功及电流，忽略换相动态过程。*


**公式2**: $$$$Y_{con} U_{con} = H_{con} + n_1 P_{con1} i_{\alpha1} + \frac{1}{3} n_2 P_{con2} i_{\alpha2} + P_{con\beta} i_{\beta}$$$$

*电磁暂态模型中12脉动换流器的节点电压方程，基于隐式梯形积分法离散化后形成的导纳矩阵与历史电流源向量，用于精确求解阀开关状态。*


**公式3**: $$$$Y_{dc}U_{dc} =H_{dc} +P_{dc1}i_{\beta1i} +P_{dc2} i_{\beta1j} +P_{dc3}i_{\beta2i} +P_{dc4} i_{\beta2j}$$$$

*双极直流线路T型集中参数模型的节点电压方程，结合历史电流源项实现直流网络电磁暂态求解。*


### 算法步骤

1. 信号采集与预处理：在故障清除后截取发电机相对功角或交流线路传输功率的振荡信号序列，去除直流分量并进行归一化处理。

2. 构造Hankel矩阵：将一维时间序列数据按固定窗口长度重排为Hankel矩阵形式，利用数据的平移不变性构建状态空间表征。

3. 奇异值分解(SVD)：对Hankel矩阵进行SVD分解，根据奇异值能量分布设定截断阈值，将矩阵空间严格划分为信号子空间与噪声子空间。

4. 旋转不变性提取：利用信号子空间的前后行块矩阵之间的旋转不变关系，构造特征值问题矩阵，消除噪声子空间干扰。

5. 特征值求解与参数映射：求解特征值，将其映射为复平面上的极点，通过极点实部计算衰减因子，虚部计算振荡角频率，进而求得阻尼比。

6. 模态筛选与输出：根据幅值与能量贡献度筛选主导振荡模式，输出低频振荡的主导频率、阻尼比及初始相位，完成模态分析。


### 关键参数

- **故障设置**: 交流单相瞬时接地短路，接地电阻0.1Ω，故障持续时间0.1s；直流故障为第一极断线。

- **直流系统参数**: 双极运行，直流电压±250kV，单极传输功率150MW。

- **控制策略**: 整流侧：定电流、低压限流控制；逆变侧：定熄弧角、定电压、定电流、低压限流控制。

- **仿真平台**: ADPSS（电力系统全数字仿真装置），支持10000节点规模机电-电磁混合实时仿真。

- **接口处理**: 通过UD模块测量直流所需无功与机电侧提供无功的差值，在接口处并联感性/容性无功负荷进行动态补偿。



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| EPRI36系统交流故障（BUS24-BUS9单相接地） | 机电暂态模型主导频率为0.3567 Hz，阻尼比范围0.0162~0.0175；混合仿真模型主导频率为0.3703~0.3708 Hz，阻尼比范围0.0183~0.0207。发电机功角曲线趋势高度一致。 | 主导频率偏差约0.014 Hz，阻尼比绝对差值<0.003，相对误差<0.3%，机电模型可准确反映系统低频振荡特征。 |

| 实际电网交流故障（单相接地重合闸成功） | 线路1：机电模型频率0.3588 Hz，阻尼比0.0649；混合模型频率0.3399 Hz，阻尼比0.0637。线路2：机电模型频率0.4079 Hz，阻尼比0.0334；混合模型频率0.4009 Hz，阻尼比0.0330。 | 两种模型下主导频率接近，阻尼比差异均在0.1%以内，机电模型计算结果略偏保守但趋势完全吻合。 |

| 实际电网直流故障（第一极断线） | 机电模型提取出0.3522 Hz（阻尼比0.1325）和0.4605 Hz（阻尼比0.1317）模式；混合模型提取出0.4430 Hz（阻尼比0.1001）和0.3538 Hz（阻尼比0.0972）模式。 | 直流故障下机电模型无法模拟换流阀详细暂态，其阻尼比计算结果显著偏大（如0.1325 vs 0.0972，高估约36%），结果偏乐观，需采用电磁暂态模型。 |



## 量化发现

- 交流故障引发的低频振荡中，机电准稳态模型与电磁暂态混合模型的主导频率偏差小于0.02 Hz，阻尼比相对误差严格控制在0.3%以内。
- 实际电网交流故障场景下，两种模型提取的线路功率振荡阻尼比差异小于0.1%，验证了准稳态模型在交流扰动LFO分析中的高精度。
- 直流线路故障场景下，机电暂态模型计算的阻尼比（0.1325/0.1317）较电磁暂态模型（0.1001/0.0972）高估约30%~36%，表明其对电力电子器件暂态过程描述不足导致结果偏乐观。
- 机电暂态模型计算量显著小于电磁暂态模型，在交流系统故障主导的低频振荡分析中具备工程实用价值，可大幅缩短仿真时间且满足精度要求。


## 关键公式

### 直流换流器准稳态代数方程

$$$$\begin{cases} V_{d0} = \frac{3\sqrt{2}}{\pi} B T V \\ V_d = V_{d0} \cos \alpha - \frac{3}{\pi} X_c I_d B \\ P = V_d I_d \\ Q = P \tan \phi \end{cases}$$$$

*用于机电暂态仿真中，将直流系统线性化为等值电路，忽略换相过程动态，适用于交流系统扰动下的低频振荡分析。*

### 电磁暂态换流器节点导纳方程

$$$$Y_{con} U_{con} = H_{con} + n_1 P_{con1} i_{\alpha1} + \frac{1}{3} n_2 P_{con2} i_{\alpha2} + P_{con\beta} i_{\beta}$$$$

*基于隐式梯形积分法将R、L、C微分方程离散为差分方程后构建，用于精确求解晶闸管导通/关断状态下的瞬时电压电流。*

### 双极直流线路T型等值节点方程

$$$$Y_{dc}U_{dc} =H_{dc} +P_{dc1}i_{\beta1i} +P_{dc2} i_{\beta1j} +P_{dc3}i_{\beta2i} +P_{dc4} i_{\beta2j}$$$$

*电磁暂态模型中直流网络求解核心方程，结合历史电流源项实现直流线路分布参数的集中参数暂态计算。*



## 验证详情

- **验证方式**: 对比仿真验证与模态分析（TLS-ESPRIT算法提取特征参数）
- **测试系统**: EPRI36标准测试系统；某实际大电网系统（9个厂站，6000+母线，700+发电机，电压等级6.3kV~800kV，含3条直流线）
- **仿真工具**: ADPSS（电力系统全数字仿真装置）
- **验证结果**: 在交流系统故障引发的低频振荡中，直流准稳态（机电）模型与详细电磁暂态模型的仿真结果高度吻合，主导频率与阻尼比误差极小（<0.3%），证明准稳态模型完全满足工程LFO分析需求且计算效率高。在直流系统自身故障引发的振荡中，机电模型因无法刻画换流阀开关暂态，导致阻尼比被高估约30%以上，结果偏乐观，此时必须采用电磁暂态模型以保证分析精度。
