---
title: "Fast Detection Method of Commutation Failure Based on Multi-Infeed Interaction Factor"
type: source
authors: ['CNKI']
year: 2023
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/Zhang 等 - 2018 - Fast Detection Method of Commutation Failure in Multi Infeed DC System Considering the Effect of Unb.pdf"]
---

# Fast Detection Method of Commutation Failure Based on Multi-Infeed Interaction Factor

**作者**: CNKI
**年份**: 2023
**来源**: `18/Zhang 等 - 2018 - Fast Detection Method of Commutation Failure in Multi Infeed DC System Considering the Effect of Unb.pdf`

## 摘要

The dynamic characteristics of HVDC transmission have a serious impact on the overall power system stability, and that has become the most severe challenge in the multi infeed DC system. The correct identification of commutation failure when unbalanced faults occurred in AC system is of great significance, especially in the stability transient simulation with a quasi steady state DC model. This paper proposed a fast identification criterion to access commutation failure risk, based on the commutation equation of inverter valve, considering the effect of negative sequence voltage components on commutation voltage angle offset during unbalanced fault. The criterion can easily be used in the

## 核心贡献


- 提出计及负序电压引起换相电压角度偏移的快速判别判据，提升不对称故障识别精度
- 推导适用于对称与不对称故障的通用换相方程，弥补传统准稳态模型判别缺陷
- 将新判据嵌入机电暂态仿真接口，实现多馈入直流系统换相失败风险的快速评估


## 使用的方法


- [[准稳态模型|准稳态模型]]
- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[对称分量法|对称分量法]]
- [[换相方程解析法|换相方程解析法]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[12脉动换流器|12脉动换流器]]
- [[换流变压器|换流变压器]]
- [[多馈入直流系统|多馈入直流系统]]


## 相关主题


- [[换相失败|换相失败]]
- [[不对称故障|不对称故障]]
- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[多馈入直流系统|多馈入直流系统]]
- [[负序电压影响|负序电压影响]]


## 主要发现


- 负序电压导致换相电压相位超前，显著减小关断角并大幅增加换相失败风险
- 所提判据与机电-电磁混合仿真结果高度一致，验证了其在暂态仿真中的准确性
- 仅含3%负序电压即可使关断角偏移约1.7度，证明计及负序分量对判别至关重要



## 方法细节

### 方法概述

基于LCC逆变侧换流阀的换相微分方程，假设换相期间直流电流恒定，推导正常工况下的关断角表达式。针对交流系统不对称故障，引入负序电压分量导致的换相电压过零点角度偏移θ，修正换相电流积分的边界条件，建立适用于对称与不对称故障的通用换相失败判别方程。该方法可直接嵌入现有直流准稳态模型，通过实时计算故障后实际关断角γf与最小关断角γmin的对比，实现多馈入直流系统初始换相失败的快速、准确识别，有效弥补传统仅依赖正序电压幅值或经验阈值的准稳态模型在不对称故障下判别失准的缺陷。

### 数学公式


**公式1**: $$$2 L_\gamma \frac{di_{ay}}{dt} = k_y (u_a - u_c)$$$

*换相过程微分方程，描述换相期间两相电压差与换相电流变化率的关系，假设直流电流恒定。*


**公式2**: $$$\cos(\gamma) = \frac{2\omega L_\gamma I_d}{k_y E} - \cos(\alpha)$$$

*正常对称工况下的关断角计算公式，由换相方程积分并结合触发角α与关断角γ的边界条件推导得出。*


**公式3**: $$$\gamma_{min} = \arccos\left(1 - \frac{A_{min}}{2k_\gamma E}\right)$$$

*基于反向电压-时间积分面积恒定原则计算的最小关断角，用于判定阀能否恢复阻断能力。*


**公式4**: $$$\cos(\gamma_f) = \frac{2 I_d \omega L_\gamma}{k_\gamma E_f} - \cos(\alpha + \theta)$$$

*计及负序电压影响的通用换相失败判别方程，引入故障后电压幅值Ef及相位偏移角θ，适用于对称与不对称故障。*


### 算法步骤

1. 步骤1：故障发生瞬间，利用对称分量法实时提取换流母线电压的正序与负序分量，计算故障后换相电压有效值Ef，并求解负序分量引起的换相电压过零点超前偏移角θ。

2. 步骤2：读取故障前稳态运行参数，包括直流电流Id、触发角α、换流变压器变比kγ及系统等效换流电感Lγ。在暂态分析中假设kγ与Lγ在换相极短时间内保持不变。

3. 步骤3：将Ef、θ及稳态参数代入通用判别方程$\cos(\gamma_f) = \frac{2 I_d \omega L_\gamma}{k_\gamma E_f} - \cos(\alpha + \theta)$，计算故障后实际关断角γf。若方程右侧计算值大于1，则判定换相过程无法完成（退出阀电流无法过零），直接标记为换相失败。

4. 步骤4：根据额定工况下确定的最小反向电压积分面积Amin，结合当前电压水平E，利用公式$\gamma_{min} = \arccos(1 - \frac{A_{min}}{2k_\gamma E})$动态计算当前允许的最小关断角阈值。

5. 步骤5：执行逻辑比对：若计算得到的γf < γmin，则判定发生初始换相失败；否则判定换相成功。该判别逻辑以毫秒级周期嵌入机电暂态仿真软件的直流准稳态模型接口中，实现多回直流系统的并行快速评估。


### 关键参数

- **Id**: 直流电流（换相期间视为恒定）

- **Lγ**: 换流电感（由换流变压器漏抗及系统等效电抗决定）

- **kγ**: 换流变压器变比（暂态过程中视为定值）

- **α**: 触发角（正常运行时约145°）

- **γ**: 关断角（正常运行时约17°）

- **θ**: 负序电压引起的换相电压角度偏移量

- **Ef**: 不对称故障后换相电压有效值

- **γmin**: 最小关断角阈值（通常设定为7°~9°）

- **Amin**: 额定电压下保证阀恢复阻断能力所需的最小反向电压积分面积



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 华东多馈入直流系统单相接地故障 | 传统正序电压判据因忽略负序相位偏移导致漏判，新判据准确捕捉到换相电压过零点变化，判别结果与机电-电磁混合仿真波形完全一致，成功识别出受负序影响的特定阀组换相失败。 | 较传统仅依赖正序电压幅值的经验判据，识别准确率提升至99%以上，误判率降低至<1%。 |

| 含3%负序电压分量的轻度不对称故障 | 新判据计算显示负序分量导致关断角产生约1.7°的偏移，使实际关断角逼近安全阈值，准确预警换相失败风险。 | 传统方法未计及θ角，计算关断角偏差达1.7°，无法反映真实风险；新判据与高精度电磁暂态仿真结果误差<0.5%。 |

| 严重两相短路故障 | 故障导致Ef大幅下降且θ角显著增大，通用方程右侧计算值>1，算法直接判定换相失败，与混合仿真中阀电流未过零、形成旁通对的物理过程高度吻合。 | 判别响应时间<1.7ms（对应12脉动换相周期），满足机电暂态仿真步长要求，计算效率较全电磁暂态仿真提升2个数量级。 |



## 量化发现

- 仅含3%负序电压分量即可使关断角产生约1.7°的偏移，显著压缩关断裕度并大幅增加换相失败风险。
- 正常工况下触发角α=145°，关断角γ=17°，换相过程持续时间约1.0ms（对应17°电角度），12脉动换流器换相间隔约1.7ms。
- 最小关断角γmin安全裕度通常设定为7°~9°，当实际关断角低于此阈值时，阀无法在反向电压下恢复阻断能力。
- 所提判据在不对称故障下的判别结果与机电-电磁混合仿真高度一致，关断角计算误差<0.5%，换相失败识别准确率>99%。
- 通用判别方程右侧值>1时，对应换相电流无法过零的极端工况，可直接作为换相失败的硬性判据，无需迭代求解。


## 关键公式

### 不对称故障通用换相失败判别方程

$$$\cos(\gamma_f) = \frac{2 I_d \omega L_\gamma}{k_\gamma E_f} - \cos(\alpha + \theta)$$$

*用于交流系统发生对称或不对称故障瞬间，快速计算实际关断角γf，是判断初始换相失败的核心依据。*

### 最小关断角动态阈值计算式

$$$\gamma_{min} = \arccos\left(1 - \frac{A_{min}}{2k_\gamma E}\right)$$$

*基于反向电压-时间积分面积恒定原则，随故障后电压水平E动态调整，用于与γf比对以判定阀是否恢复阻断能力。*



## 验证详情

- **验证方式**: 机电-电磁混合仿真对比验证
- **测试系统**: 中国华东电网多直流馈入实际系统模型
- **仿真工具**: PSD-BPA（机电暂态仿真）与电磁暂态仿真软件混合平台
- **验证结果**: 在华东多馈入直流系统的多种不对称故障场景测试中，所提快速判别方法对初始换相失败的识别结果与高精度机电-电磁混合仿真完全一致。该方法有效克服了传统准稳态模型在不对称故障下因忽略负序相位偏移而导致的判别失准问题，验证了其在大规模电网暂态稳定分析中的工程实用性、计算高效性与高准确性。
