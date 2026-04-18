---
title: "Saturation in Transient and Stability Phenomena for Cylindrical"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/pesgm.2012.6344723.pdf.pdf"]
---

# Saturation in Transient and Stability Phenomena for Cylindrical

**作者**: 
**年份**: 2012
**来源**: `13&14/files/pesgm.2012.6344723.pdf.pdf`

## 摘要

This paper presents the influence of reactance saturation in transient and stability phenomena for cylindrical synchronous machine. For this purpose the authors have examined various equivalent circuit models using electromagnetic transients program (EMTP-ATP). Index Terms—turbine generator, flux saturation, operational- impedance, EMTP I.  INTRODUCTION urbine generators are extensively used for power generation since many years ago. The capacity of single unit is significantly increasing to catch up with the

## 核心贡献



- 研究了电抗饱和对圆柱形同步电机暂态和稳定现象的影响
- 基于EMTP-ATP对比评估了传统线性Park模型与考虑磁饱和及q轴暂态电抗的改进Park模型
- 揭示了磁饱和与q轴暂态电抗对大容量汽轮发电机暂态特性分析的重要性

## 使用的方法


- [[numerical-integration]]
- [[state-space]]
- [[nodal-analysis]]

## 涉及的模型


- [[synchronous-machine]]

## 相关主题


- [[synchronous-machine]]
- [[network-equivalent]]

## 主要发现



- 磁饱和对同步电机的暂态和稳定特性有显著影响
- 在等效电路中考虑磁饱和与q轴暂态电抗（x'q）能显著提高大容量汽轮发电机暂态过程（如甩负荷）的仿真精度
- 传统恒定电抗的线性Park模型不足以准确评估大容量机组的暂态行为

## 方法细节

### 方法概述

本研究采用EMTP-ATP电磁暂态仿真程序，系统性地评估了三种等效电路模型在圆柱形同步电机（特别是大容量汽轮发电机）暂态分析中的精度差异。研究方法包括：(1)建立传统线性Park模型（恒定电抗）作为基准；(2)构建考虑磁饱和的改进Park模型，采用多段线性近似(polyline-approximated)技术处理d轴和q轴电枢反应电抗的饱和特性；(3)进一步引入q轴暂态电抗$x'_q$（即$x_{fq}$和$R_{fq}$等效回路）建立高精度模型。仿真中考虑了自动电压调节器(AVR)和电力系统稳定器(PSS)的影响，针对500,000 kVA和800,000 kVA等级的实心转子圆柱形发电机进行瞬态过程分析，计算步长设定为几十微秒(several tens μsec)以准确捕捉瞬态直流分量。

### 数学公式


**公式1**: $$$k = f(\phi)$, where $\phi = \sqrt{\phi_{ad}^2 + \phi_{aq}^2}$$$

*饱和系数k的计算公式，其中$\phi_{ad}$和$\phi_{aq}$分别为d轴和q轴磁链，f(φ)为基于无负载饱和曲线获得的二次函数，用于近似0.8pu及以上端电压区域的饱和特性*


**公式2**: $$$x_{ad(sat)} = k \cdot x_{ad(unsat)}$, $x_{aq(sat)} = k \cdot x_{aq(unsat)}$$$

*考虑饱和后的d轴和q轴电枢反应电抗计算，通过饱和系数k对未饱和电抗进行修正*


**公式3**: $$$x'_q = x_{aq} // x_{fq}$ (parallel with $R_{fq}$)$$

*q轴暂态电抗定义，考虑q轴阻尼绕组（等效为$x_{fq}$和$R_{fq}$回路）与q轴电枢反应电抗的并联效应*


### 算法步骤

1. 建立同步电机Park方程，区分d轴（直轴）和q轴（交轴）电路拓扑，包括定子电阻$R_a$、漏抗$x_l$、励磁绕组($x_{fd}$,$R_{fd}$)和阻尼绕组

2. 在每一步长计算d轴磁链$\phi_{ad}$和q轴磁链$\phi_{aq}$，基于当前电压和电流状态

3. 计算合成磁链幅值$\phi = \sqrt{\phi_{ad}^2 + \phi_{aq}^2}$，作为饱和特性的判断依据

4. 根据无负载饱和曲线(no-load saturation curve)的多段线性近似，确定当前工作点的饱和系数k值（在0.8pu端电压以上区域采用二次函数近似）

5. 更新d轴和q轴电枢反应电抗：$x_{ad} = k \cdot x_{ad(unsa)}$，$x_{aq} = k \cdot x_{aq(unsa)}$，实现电抗的瞬时变化

6. 对于改进Park模型(2)，额外考虑q轴暂态电抗$x'_q$的影响，即在q轴等效电路中加入$x_{fq}$和$R_{fq}$支路，模拟实心转子表面的涡流效应

7. 采用状态空间法和节点分析法在EMTP-ATP中进行时域仿真，积分步长设置为几十微秒(several tens μsec)以确保瞬态直流分量的计算精度

8. 执行甩负荷(load rejection)和相间短路(line-to-line sudden short circuit)等暂态工况仿真，对比三种模型的响应差异


### 关键参数

- **machine_capacity**: 500,000 kVA和800,000 kVA（模型机），实际机组达900,000-1,200,000 kVA

- **pole_number**: 2极

- **saturation_threshold**: 0.8 pu端电压（饱和特性起始点）

- **time_step**: 几十微秒(several tens μsec)，用于瞬态直流分量分析

- **saturation_function_type**: 二次函数(quadratic function)近似，用于0.8pu以上区域

- **external_system**: 连接至无穷大母线(infinite bus)，含外部阻抗



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 甩负荷(Load Rejection)暂态过程 | 在甩负荷工况下，传统Park模型(1)（恒定电抗）与考虑饱和和$x'_q$的Park模型(2)表现出显著差异。当不考虑$x'_q$时，甩负荷后电压立即出现轻微下降然后上升；而考虑$x'_q$和饱和效应后，电压下降得到缓解，波形与实测数据吻合 | Park模型(2)相比传统Park模型(1)，在甩负荷后的电压峰值预测误差显著降低，特别是d轴电压$E_d$的暂态行为描述准确性大幅提升 |

| 三相平衡暂态（含AVR和PSS） | 在考虑AVR和PSS的闭环系统中，磁饱和对暂态稳定性有显著影响。采用多段线性近似饱和特性的模型相比恒定饱和值模型，能更准确地反映电抗的瞬时变化 | 考虑瞬时饱和变化的模型(case 2-2)比采用恒定饱和电抗的模型(case 1)能更精确地捕捉电压恢复过程的时间常数 |

| 三相不平衡暂态（相间短路） | 通过在外部虚拟安装变压器模型(case 2-2)来考虑复杂饱和特性，成功在EMTP中实现了不平衡暂态下的饱和模拟，解决了直接在建模中考虑复杂饱和特性导致的收敛性问题 | 该方法突破了传统EMTP在相间短路等不平衡暂态中难以考虑饱和特性的限制，虽然未涉及详细饱和特性，但相比完全忽略饱和的模型有显著改进 |



## 量化发现

- 计算步长需设置为几十微秒(several tens μsec)级别，才能准确分析含瞬态直流分量的暂态现象（相比AC频域分析的毫秒级步长要求更严格）
- 饱和特性显著影响区域为端电压0.8pu及以上，此时饱和系数k通过二次函数定义
- 对于500,000 kVA等级圆柱形发电机，忽略$x'_q$会导致甩负荷后电压预测出现明显偏差（立即下降现象），而考虑$x'_q$后电压波形与实测值吻合
- 实心转子汽轮发电机的$x'_q$对d轴电压$E_d$的暂态行为影响显著，必须纳入等效电路以提高大容量机组(800,000-1,200,000 kVA)暂态评估精度
- 磁饱和与$x'_q$的耦合效应在甩负荷等电压上升暂态中尤为关键，二者共同决定了电压恢复的时间常数和超调量


## 关键公式

### 综合磁链饱和系数

$$$k = f\left(\sqrt{\phi_{ad}^2 + \phi_{aq}^2}\right)$$$

*用于在每个计算步长中根据d轴和q轴磁链的矢量和确定当前饱和程度，进而动态调整电枢反应电抗值*

### q轴暂态电抗

$$$x'_q = \frac{x_{aq} \cdot x_{fq}}{x_{aq} + x_{fq}}$ (with $R_{fq}$ time constant)$$

*在Park模型(2)中用于描述圆柱形发电机q轴的暂态特性，对甩负荷等暂态过程中电压行为建模至关重要*



## 验证详情

- **验证方式**: 对比验证（与实际机组特性试验数据对比）
- **测试系统**: 单机-无穷大母线系统(single machine to infinite bus)，包含外部阻抗、AVR和PSS，采用500,000 kVA和800,000 kVA圆柱形实心转子模型机
- **仿真工具**: EMTP-ATP（电磁暂态程序），利用其Type-59或自定义模型实现Park模型(1)和(2)的搭建，采用多段线性近似处理饱和特性
- **验证结果**: 基于实际测量的$x'_q$数据验证表明，Park模型(2)（同时考虑磁饱和和$x'_q$）能准确预测甩负荷后的电压恢复特性，特别是消除了忽略$x'_q$时出现的电压立即下降误差；对于大容量汽轮发电机(>800,000 kVA)，该模型显著优于传统恒定电抗Park模型(1)
