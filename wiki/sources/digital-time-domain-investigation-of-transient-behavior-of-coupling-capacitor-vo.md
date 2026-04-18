---
title: "Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Voltage Transformer - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/61.660947.pdf.pdf"]
---

# Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Voltage Transformer - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `13&14/files/61.660947.pdf.pdf`

## 摘要

This paper reports a set of digital time-domain simulation studies conducted on TEHMPl61A Coupling Capacitor Voltage Transformer (CCVT) of Haefely-Trench. The Electro-Magnetic Transients Program (EMTP) is used to develop the CCVT model and conduct the transient studies. The accuracy of the CCVT model is verified through comparison of the EMTP simulation results with those obtained from test results. The investigations demonstrate that the developed model can accurately predict CCVT transient response, e.g. the phenomenon of ferroresonance. The model is developed (1) to determine impact of transients on CCVT response, (2) to design, optimize and compare protective and ferroresonance suppressor devices of CCVT, and (3) to predict CCVT transient response on power system monitoring and protect

## 核心贡献


- 基于EMTP构建含非线性饱和特性与多分接头的CCVT高精度时域数字模型
- 通过频域灵敏度分析量化杂散电容、阻尼电感及负载功率因数对频响的影响
- 验证模型预测铁磁谐振及故障暂态响应的准确性，为保护装置优化提供依据


## 使用的方法


- [[emtp时域仿真|EMTP时域仿真]]
- [[频域灵敏度分析|频域灵敏度分析]]
- [[物理试验对比验证|物理试验对比验证]]


## 涉及的模型


- [[ccvt|CCVT]]
- [[降压变压器|降压变压器]]
- [[串联电抗器|串联电抗器]]
- [[阻尼线圈|阻尼线圈]]
- [[杂散电容|杂散电容]]
- [[mov-晶闸管-火花隙保护装置|MOV/晶闸管/火花隙保护装置]]
- [[负载模型|负载模型]]


## 相关主题


- [[铁磁谐振|铁磁谐振]]
- [[暂态响应分析|暂态响应分析]]
- [[频域灵敏度分析|频域灵敏度分析]]
- [[继电保护影响评估|继电保护影响评估]]
- [[数字时域仿真|数字时域仿真]]


## 主要发现


- 仿真与实测波形高度吻合，模型可准确复现铁磁谐振起振与衰减过程
- 负载功率因数与串联电抗器杂散电容显著影响高频段频响特性
- 近端接地故障会在CCVT二次侧激发高频振荡暂态，影响保护判据



## 方法细节

### 方法概述

基于EMTP平台构建TEHMP161A型CCVT全元件级时域数字模型。模型涵盖电容分压器(C1/C2)、排流线圈(Ld)、带多分接头与非线性饱和特性的降压变压器(SDT)、串联电抗器(Lc)、集中参数杂散电容(Cm/Ct/Cc)、谐波抑制滤波器及MOV/晶闸管/火花隙等保护装置。研究首先基于线性化等效电路开展频域灵敏度扫描，量化各寄生参数对幅频/相频特性的影响边界；随后在时域中施加近端接地故障与二次侧短路等典型暂态激励，利用EMTP的梯形积分法与补偿法求解含非线性磁化曲线与MOV伏安特性的微分代数方程组，精确捕捉铁磁谐振起振、次谐波振荡及高频衰减过程；最终通过实验室物理测试波形进行交叉验证，迭代优化Q值与饱和参数，形成可用于继电保护评估与装置选型的高保真仿真框架。

### 数学公式


**公式1**: $$$H(f) = 20 \log_{10}\left(\frac{V_{out}(f)}{V_{in}(f)}\right)$$$

*频域幅频响应计算式，用于评估CCVT在不同频率下的电压传递衰减特性*


**公式2**: $$$f_n = \frac{1}{2\pi\sqrt{L_d \cdot \frac{C_1 C_2}{C_1 + C_2}}}$$$

*分压器与排流线圈构成的LC回路自然振荡频率公式，决定暂态高频振荡主频*


### 算法步骤

1. 1. 拓扑建模与参数初始化：在EMTP中搭建CCVT完整电路拓扑，录入C1(14611pF)、C2(118400pF)、Ld(10mH)、Lc(42H)等基准参数，配置SDT多分接头切换逻辑与杂散电容(Cm/Ct/Cc)集中等效节点。

2. 2. 频域灵敏度扫描：将非线性元件线性化，施加扫频电压源，计算幅频曲线，遍历Ld、Lc、Cc、Ct及负载VA/pf等变量，识别对>300Hz及<60Hz频段敏感的关键寄生参数。

3. 3. 时域暂态激励注入：设置开关S1~S4模拟系统近端接地故障(S3闭合/断开)与二次侧短路(S2闭合/断开)，在电压峰值或过零点触发操作，生成阶跃与短路电流冲击波形。

4. 4. 非线性暂态求解：启用EMTP梯形积分算法，结合SDT分段线性磁化曲线与MOV非线性电阻模型，采用补偿法迭代求解网络节点电压与支路电流，记录二次侧输出电压瞬态波形。

5. 5. 保护装置效能评估：对比无保护、火花隙限压与MOV吸收三种工况下的过电压峰值与能量积分，量化铁磁谐振抑制效果与热应力分布。

6. 6. 试验数据交叉验证：将仿真输出与实验室实测波形进行时域对齐，调整Ld品质因数(Q值)与滤波器饱和阈值，直至振荡频率、衰减时间常数及谐振起振点误差收敛至工程允许范围。


### 关键参数

- **C1**: 14611 pF

- **C2**: 118400 pF

- **Ld**: 10 mH

- **Lc**: 42 H

- **Cc**: 242 pF

- **SDT_R1**: 284.5 Ω

- **SDT_L1**: 7.37 H

- **SDT_Rm**: 4.96 MΩ

- **谐波抑制滤波器线性支路**: 75 Ω

- **典型负载**: 400 VA, pf=0.8滞后

- **自然振荡频率**: 13.956 kHz



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 近端接地故障暂态响应 | S3闭合引发系统故障，二次侧激发高频振荡，主频锁定于13.956 kHz。无保护时过电压峰值显著，火花隙动作后将电压钳位于设定阈值，振荡衰减时间常数受Ld Q值主导。 | 相比忽略杂散电容的简化模型，全参数模型准确复现了>10 kHz频段的高频模态，波形重合度提升显著，高频振荡幅值预测误差<3%。 |

| 二次侧短路铁磁谐振测试 | S2在电压峰值闭合后10周期断开，SDT铁芯饱和引发次谐波铁磁谐振。MOV投入后有效吸收谐振能量，抑制电压畸变，仿真记录MOV吸收能量曲线用于热应力评估。 | 传统线性模型无法预测次谐波起振，本非线性EMTP模型准确复现了谐振建立与衰减全过程，与实测波形相位偏差<2%，起振时刻误差<0.5 ms。 |

| 频域灵敏度与负载特性分析 | 负载容量(200~1200 VA)变化对频响影响微弱；但功率因数从1.0降至0.4滞后时，>300 Hz频段幅频响应出现明显衰减，<60 Hz低频段相角偏移加剧。 | 量化了负载功率因数对高频保护判据的潜在干扰，为继电器整定提供频域修正依据，频响偏差在pf=0.4时较pf=1.0增大逾15 dB。 |



## 量化发现

- 分压器-排流线圈回路自然振荡频率精确测定为13.956 kHz，该模态主导近端故障下的高频暂态响应。
- 串联电抗器杂散电容Cc从0 pF增至1500 pF时，频响曲线第一谷点频率偏移至约640 Hz，证实Cc对低频段谐振特性具有决定性影响。
- 负载功率因数低于0.6滞后时，>300 Hz频段幅频响应衰减显著增加，直接影响高频保护元件的动作裕度。
- 排流线圈Ld的Q值直接决定13.956 kHz振荡模态的衰减速率，准确表征Ld损耗是抑制高频过电压仿真的关键。
- MOV保护装置在铁磁谐振工况下可有效限制二次侧过电压，其吸收能量积分曲线为热容量选型提供直接量化依据。
- SDT饱和特性曲线电流单位需修正为mA级（非A级），磁化特性对谐振起振阈值敏感，修正后仿真与实测波形高度吻合。


## 关键公式

### CCVT幅频响应传递函数

$$$H(f) = 20 \log_{10}\left(\frac{V_{out}(f)}{V_{in}(f)}\right)$$$

*用于频域灵敏度分析，评估不同寄生参数与负载条件下CCVT的电压传递衰减特性*

### LC回路自然振荡频率

$$$f_n = \frac{1}{2\pi\sqrt{L_d \cdot \frac{C_1 C_2}{C_1 + C_2}}}$$$

*计算分压器电容与排流电感构成的谐振回路主频，解释故障暂态中13.956 kHz高频振荡的物理来源*

### 铁芯磁链与饱和特性积分关系

$$$\Psi = \int (V_{sec} \cdot i_{mag}) dt$$$

*在EMTP中构建SDT非线性磁化曲线，用于精确模拟铁磁谐振起振阈值与次谐波振荡过程*



## 验证详情

- **验证方式**: 物理试验对比验证（实验室台架测试与数字仿真交叉验证）
- **测试系统**: Haefely-Trench TEHMP161A型耦合电容器电压互感器（CCVT）
- **仿真工具**: EMTP (Electro-Magnetic Transients Program)
- **验证结果**: 仿真波形与实测波形在暂态起振时刻、13.956 kHz高频振荡频率、铁磁谐振衰减包络及保护装置动作阈值上高度一致。模型成功复现了次谐波铁磁谐振现象，验证了非线性饱和特性与杂散电容参数设置的准确性，满足继电保护暂态评估与装置优化设计的工程精度要求。
