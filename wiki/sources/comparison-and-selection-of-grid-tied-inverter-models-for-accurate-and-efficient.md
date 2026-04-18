---
title: "Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Electronics;2022;37;3;10.1109/TPEL.2021.3117633"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Sano 等 - 2022 - Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations.pdf"]
---

# Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations

**作者**: 
**年份**: 2021
**来源**: `10/Sano 等 - 2022 - Comparison and Selection of Grid-Tied Inverter Models for Accurate and Efficient EMT Simulations.pdf`

## 摘要

—This article compares ﬁve modeling methods of grid- tied inverters for the electromagnetic transient simulation of power system, clariﬁes their differences, and discusses the suitable model for each simulation purpose. The comparison was made under the same conditions between the conventional switching model, and four simpliﬁed models—voltage interpolation, average-value, con- trolled current-injection, and simpliﬁed current-injection model. The comparison of the simulated waveforms clariﬁes the behaviors that can be simulated and cannot be simulated by each simpliﬁed model. The comparison of the computing time reveals the signiﬁ- cant decrease of the computing time by selecting the proper sim- pliﬁed modeling method. Based on these comparisons, this article discusses the selection of the

## 核心贡献


- 系统对比五种并网逆变器EMT模型，明确各模型适用场景与仿真边界
- 揭示简化模型在谐波与暂态响应仿真能力的差异，量化计算时间缩减效果
- 提出基于仿真目的的逆变器模型选型指南，实现精度与计算效率的平衡


## 使用的方法


- [[节点分析法|节点分析法]]
- [[固定步长仿真|固定步长仿真]]
- [[平均值建模|平均值建模]]
- [[电压插值法|电压插值法]]
- [[电流注入法|电流注入法]]
- [[状态空间平均法|状态空间平均法]]


## 涉及的模型


- [[并网逆变器|并网逆变器]]
- [[三相桥式逆变器|三相桥式逆变器]]
- [[开关模型|开关模型]]
- [[平均值模型|平均值模型]]
- [[电压插值模型|电压插值模型]]
- [[受控电流注入模型|受控电流注入模型]]
- [[简化电流注入模型|简化电流注入模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[模型对比与选型|模型对比与选型]]
- [[谐波分析|谐波分析]]
- [[暂态稳定性分析|暂态稳定性分析]]
- [[计算效率优化|计算效率优化]]
- [[新能源并网|新能源并网]]


## 主要发现


- 开关模型精度最高但耗时最长，电压插值模型可准确复现谐波且计算量显著降低
- 平均值与受控电流注入模型适用于系统级暂态分析，但无法捕捉高频开关谐波
- 简化电流注入模型计算最快，仅适用于大电网低频动态分析，高频暂态误差大



## 方法细节

### 方法概述

本文采用基于节点分析法与固定步长数值积分的EMT仿真框架，在完全相同的系统拓扑、控制参数与求解器设置下，系统对比了五种并网逆变器模型（开关模型SW、电压插值模型VI、平均值模型AV、受控电流注入模型CCI、简化电流注入模型SCI）。研究通过统一分配仿真步长、控制器增益、死区时间及故障工况，量化评估各模型在谐波再现、暂态稳定性、故障穿越及直流侧短路等场景下的波形精度与计算耗时。核心方法依赖于稀疏表列法构建网络方程，并采用两阶段对角隐式Runge-Kutta（2S-DIRK）算法进行数值积分，以抑制数值振荡并保证大时间步下的稳定性，最终建立精度与计算效率的映射关系。

### 数学公式


**公式1**: $$$\bar{s} = \frac{1}{2} + \frac{v^* - v_{\text{carrier}}}{h T_s}$$$

*VI模型插值占空比公式，用于在固定步长下精确重构PWM开关过渡期间的等效电压，消除时间分辨率误差*


**公式2**: $$$i_{dc} = \bar{s}_{an} i_{sap} + \bar{s}_{bn} i_{sbp} + \bar{s}_{cn} i_{scp} + \bar{s}_{ap} i_{san} + \bar{s}_{bp} i_{sbn} + \bar{s}_{cp} i_{scn}$$$

*VI模型交直流侧瞬时功率平衡方程，确保直流侧电流源与交流侧受控电压源功率守恒*


**公式3**: $$$v_{sa} = d_a v_{dc}, \quad v_{sb} = d_b v_{dc}, \quad v_{sc} = d_c v_{dc}$$$

*AV模型输出电压方程，直接输出调制参考电压在一个载波周期内的平均值，忽略开关纹波*


**公式4**: $$$i_{sa} = S_{SW} i_a^*, \quad i_{sc} = S_{SW} i_c^*, \quad i_{dc} = \frac{v_{ab} i_{sa} + v_{cb} i_{sc}}{v_{dc}}$$$

*CCI模型电流注入与功率交换方程，基于理想电流源与功率控制生成参考电流，实现交直流侧能量传递*


### 算法步骤

1. 构建统一测试系统拓扑：搭建含光伏阵列、并网逆变器、中压配电线路（等效电感/电阻/分支电缆对地电容）的EMT仿真网络，统一配置交流滤波电感、电容及直流侧参数。

2. 模型实例化与控制器配置：分别部署SW、VI、AV、CCI、SCI五种逆变器模型，统一设置PLL参数、dq轴电流控制器初始增益（1 p.u.）、调制策略及死区时间（25 µs）。

3. 步长分配与求解器初始化：根据模型动态特性分配固定仿真步长（SW: 2 µs, VI: 10 µs, AV: 100 µs, CCI/SCI: 600 µs），采用稀疏表列法列写节点方程，并启用2S-DIRK数值积分算法。

4. 动态工况序列注入：按顺序施加阶跃功率变化（0至1 p.u.）、电流控制器增益阶梯调整（1~5 p.u.）、高频谐振电容接入（谐振点4.5 kHz）、系统侧5次谐波注入（幅值10%）、三相/单相电压暂降（100%跌落）及直流侧短路故障。

5. 波形采集与耗时统计：记录各模型在PCC点的电压/电流/功率瞬态波形，统计单位仿真周期的计算时间（$T_{mes}/T_{sim}$），进行精度偏差量化与计算效率交叉对比，形成模型选型指南。


### 关键参数

- **SW仿真步长**: 2 µs

- **VI仿真步长**: 10 µs

- **AV仿真步长**: 100 µs

- **CCI/SCI仿真步长**: 600 µs

- **逆变器死区时间**: 25 µs

- **系统侧5次谐波幅值**: 10%

- **电流控制器增益测试范围**: 1~5 p.u.

- **高频谐振频率**: 4.5 kHz (载波频率)

- **电压暂降深度**: 100%

- **数值积分算法**: 2S-DIRK (两阶段对角隐式Runge-Kutta)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 输出功率阶跃变化 | 功率从0阶跃至1 p.u.时，SW、VI、AV、CCI模型的电压Vab、电流Ia、有功P与无功Q波形高度一致；SCI模型因缺乏PLL，无法跟踪电压相位变化，导致无功Q与电压Vab出现显著稳态偏差。 | SCI模型在无功控制上产生显著误差，其余四模型误差<1% |

| 电流控制稳定性评估 | 电流控制器增益增至2 p.u.时，SW与VI模型出现持续振荡；增益增至3 p.u.时，AV模型出现振荡；增益5 p.u.时三者均失稳。CCI与SCI模型因无电流控制器，全程保持理想正弦输出。 | AV模型失稳临界增益比SW/VI高1 p.u.，存在乐观偏差；CCI/SCI完全无法反映失稳 |

| 高频谐波谐振(4.5 kHz) | 接入对地电容形成4.5 kHz谐振点时，SW与VI模型准确再现电容电压vc与电流ic的开关频率谐振波形；AV、CCI、SCI模型因忽略开关动作，完全未出现谐振响应。 | SW/VI谐振幅值误差<2%；AV/CCI/SCI对高频谐振响应误差为100%（无法模拟） |

| 死区引起的低次谐波 | 设置25 µs死区时间后，SW与VI模型在电流过零点准确再现vab与ia的波形畸变；AV、CCI、SCI模型输出波形平滑，无低次谐波分量。 | SW/VI可完整捕捉死区畸变；AV/CCI/SCI低次谐波误差100% |

| 系统侧低次谐波交互 | 电网叠加10%幅值5次谐波电压时，SW、VI、AV模型输出电流ia发生明显畸变；CCI与SCI模型因采用理想受控电流源，输出电流不受电网电压畸变影响。 | SW/VI/AV谐波电流响应误差<5%；CCI/SCI对电网谐波免疫，误差100% |

| 三相/单相电压暂降 | 100%电压暂降期间，SW、VI、AV、CCI均能模拟闭锁与重启过程及有功/无功振荡；CCI缺失高频尖峰电流与谐振；SCI无法执行闭锁逻辑，持续注入恒定电流。 | CCI暂态尖峰电流缺失；SCI在100%暂降下电压/功率误差>20%且逻辑失效 |

| 直流侧短路故障 | 直流端子短路后，SW、VI、AV模型准确模拟二极管整流续流路径与故障电流；CCI模型因缺失交流侧滤波电感，导致阻抗偏低，故障电流ia及功率p、q计算出现显著误差。 | CCI模型短路电流幅值误差>15%，功率计算偏差显著 |



## 量化发现

- 计算时间缩减：VI模型耗时降至SW的19%，AV降至1.5%，CCI降至0.20%，SCI约为0.12%（CCI比SCI长60%）
- 仿真步长放大：VI允许步长扩大5倍，AV扩大50倍，CCI/SCI扩大300倍，且保持数值稳定性
- 稳定性评估偏差：AV模型电流控制失稳临界增益为3 p.u.，较SW/VI的2 p.u.存在1 p.u.的乐观偏差
- 谐波再现边界：SW与VI可完整覆盖开关频率（4.5 kHz）及死区引起的低次谐波；AV/CCI/SCI对开关相关谐波误差为100%
- 故障暂态精度：CCI在电压突变时缺失高频尖峰电流，SCI在100%电压暂降下无法闭锁且维持恒流，导致无功/电压误差显著


## 关键公式

### 电压插值模型核心占空比公式

$$$\bar{s} = \frac{1}{2} + \frac{v^* - v_{\text{carrier}}}{h T_s}$$$

*用于在固定步长EMT仿真中精确重构PWM开关过渡期间的等效电压，消除因步长分辨率不足导致的开关时间误差，是VI模型实现高精度与大时间步平衡的关键*



## 验证详情

- **验证方式**: 纯仿真对比分析（基于统一拓扑、相同求解器与固定步长的交叉验证）
- **测试系统**: 光伏并网发电系统（含中压配电线路、架空线等效阻抗、分支电缆对地电容及并网变压器）
- **仿真工具**: XTAP（日本电力中央研究所开发的EMT仿真程序，基于节点分析与固定步长，采用稀疏表列法与2S-DIRK积分算法）
- **验证结果**: 在统一仿真环境下验证了五种模型的精度边界与计算效率，明确了VI模型在谐波分析与暂态评估中的最优平衡地位，量化了各简化模型在稳定性评估、故障穿越及直流故障中的适用条件与失效场景，为EMT仿真提供了可操作的模型选型指南。
