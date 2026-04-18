---
title: "Analysis on non-characteristic harmonic circulating current in parallel inverter system and its suppression"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Hu et al. - 2016 - Analysis on non-characteristic harmonic circulating current in parallel inverter system and its supp.pdf"]
---

# Analysis on non-characteristic harmonic circulating current in parallel inverter system and its suppression

**作者**: CNKI
**年份**: 2022
**来源**: `07&08/Hu et al. - 2016 - Analysis on non-characteristic harmonic circulating current in parallel inverter system and its supp.pdf`

## 摘要

In Jibei power grid, non-characteristic harmonic circulating current appeared several times and a fault occurred in parallel converters in a 500 kV station. Taking this fault as an example, recorded fault data were analyzed, finding out non-characteristic harmonic circulating current existing in several parallel converters. Analysis of relationship between the problem and parallel converter topology indicated that the problem was liable to appear in cascaded H-bridge multilevel converters. Reappearance of the phenomenon was realized with electromagnetic transient simulation. Simulation results showed validity of the proposed conclusion. Finally, countermeasures were proposed to solve the problem.

## 核心贡献


- 揭示级联H桥变流器并列运行时载波相位差引发非特征谐波环流的机理
- 提出基于高通滤波增大连接电抗及差异化开关频率的环流抑制策略
- 构建双重傅里叶级数模型解析开关频率次谐波相位与幅值耦合特性


## 使用的方法


- [[电磁暂态仿真|电磁暂态仿真]]
- [[双重傅里叶级数分析|双重傅里叶级数分析]]
- [[快速傅里叶变换|快速傅里叶变换]]
- [[spwm调制分析|SPWM调制分析]]


## 涉及的模型


- [[级联h桥多电平变流器|级联H桥多电平变流器]]
- [[并联逆变器|并联逆变器]]
- [[dfig-model|DFIG]]
- [[升压变压器|升压变压器]]
- [[连接电抗|连接电抗]]


## 相关主题


- [[谐波环流分析|谐波环流分析]]
- [[变流器并列运行|变流器并列运行]]
- [[非特征次谐波|非特征次谐波]]
- [[风电场并列运行|风电场并列运行]]
- [[环流抑制策略|环流抑制策略]]


## 主要发现


- 仿真验证载波相位差180度时并联变流器间形成低阻抗高频环流通路
- 级联H桥拓扑因电容充放电易致直流电压波动加剧非线性区谐波环流
- 增大连接电抗或提高开关频率可显著降低非特征谐波环流幅值



## 方法细节

### 方法概述

本文采用“现场录波数据分析-理论建模-电磁暂态仿真复现-抑制策略对比”的综合研究方法。首先对冀北电网500kV变电站及风电场故障录波数据进行FFT频谱分析，定位非特征次谐波环流频率与幅值特征。其次，基于SPWM调制原理，利用双重傅里叶级数建立变流器输出电压谐波解析模型，推导载波相位差对谐波幅值与相位的影响机理。随后，在电磁暂态仿真平台中搭建级联H桥多电平变流器并列运行模型，复现载波相位差180°极端工况下的低阻抗高频环流通路。最后，系统评估高通滤波、增大连接电抗、差异化开关频率、控制器参数解耦及PLL载波同步等五种抑制策略的有效性，并结合工程可行性给出最优方案。

### 数学公式


**公式1**: $$$u_{car} = \begin{cases} \frac{2\omega_c t}{\pi} - 2k\pi, & -\frac{\pi}{2} + 2k\pi < \omega_c t + \theta_c < \frac{\pi}{2} + 2k\pi \\ -\frac{2\omega_c t}{\pi} + 2k\pi, & \frac{\pi}{2} + 2k\pi < \omega_c t + \theta_c < \frac{3\pi}{2} + 2k\pi \end{cases}$$$

*三角载波电压表达式，用于定义SPWM调制中的载波波形，其中$\omega_c$为载波角频率，$\theta_c$为载波初始相位。*


**公式2**: $$$u_o(t) = \sum_{n=1}^{\infty} [A_{0n}\cos(ny) + B_{0n}\sin(ny)] + \sum_{m=1}^{\infty} [A_{m0}\cos(mx) + B_{m0}\sin(mx)] + \sum_{m=1}^{\infty} \sum_{n=\pm 1}^{\pm \infty} [A_{mn}\cos(mx+ny) + B_{mn}\sin(mx+ny)]$$$

*单桥臂输出电压的双重傅里叶级数展开式，用于解析SPWM调制产生的基波、载波谐波及其边带分量，其中$x=\omega_c t+\theta_c$，$y=\omega_r t+\theta_r$。*


**公式3**: $$$A_{mn} + jB_{mn} = \frac{1}{2\pi^2} \int_{0}^{2\pi} \int_{0}^{2\pi} u_p(t) e^{j(m\omega_c t + n\omega_r t)} d(\omega_c t) d(\omega_r t)$$$

*双重傅里叶系数计算公式，用于求解各次谐波分量的幅值与相位，$u_p(t)$为调制后的方波电压。*


### 算法步骤

1. 步骤1：现场故障录波数据采集与预处理。提取变流器出口电流及升压变压器高压侧电流波形，进行快速傅里叶变换(FFT)获取频谱特征，识别主导谐波频率(如720Hz)及环流路径。

2. 步骤2：理论机理建模。基于SPWM调制原理，建立三角载波与正弦调制波的数学模型，引入双重傅里叶级数分析开关频率次谐波的生成机制，推导载波相位差($\theta_c$)对谐波相位与幅值的耦合关系。

3. 步骤3：电磁暂态仿真模型构建。搭建包含级联H桥拓扑、直流侧电容、连接电抗及升压变压器的双变流器并列运行EMT模型，设置系统电压380V、基准开关频率6.4kHz、连接电抗3mH。

4. 步骤4：基线工况与极端工况仿真。设置两台变流器载波相位差为0°(理想)与180°(最恶劣)，记录输出电流波形、相位差及系统侧谐波含量，验证低阻抗环流通路的形成条件。

5. 步骤5：抑制策略参数扫描与对比。依次引入高通滤波器、将连接电抗增至5mH、提升开关频率至12.8kHz、设置差异化开关频率(6.45kHz/6.35kHz)及PLL载波同步，分别记录环流幅值衰减率与系统动态响应。

6. 步骤6：工程适用性评估。综合对比各策略的谐波抑制效果、无功损耗、开关热应力及控制复杂度，确定最优工程实施方案。


### 关键参数

- **基准开关频率**: 6.4 kHz

- **基准连接电抗**: 3 mH

- **测试系统电压**: 380 V

- **拓扑结构**: 级联H桥多电平变流器

- **主导环流频率**: 720 Hz

- **载波相位差极端工况**: 180°



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 基线工况(载波相位差180°) | 两台变流器输出电流脉动相位完全相反，形成高频环流通路。FFT分析显示720Hz谐波在变流器侧电流中占比高达60%，而66kV系统侧谐波含量极低，验证了非特征次谐波环流现象。 | 与理想同相位工况相比，环流幅值显著增大，系统侧谐波被限制在变流器并联回路内。 |

| 增加高通滤波器 | 在变流器出口串联高通滤波器后，非特征次谐波被有效滤除，环流幅值大幅下降，系统电流波形恢复平滑，未引入额外的控制阶数失稳问题。 | 相比基线工况，环流抑制效果最彻底，且不改变变流器原有控制特性与无功容量。 |

| 增大连接电抗至5mH | 连接电抗由3mH提升至5mH后，回路阻抗增加，谐波环流幅值显著降低。但大电抗导致无功容量占用增加，直流侧电压利用率下降。 | 环流幅值较基线工况下降约30%-40%，但牺牲了设备容量与直流电压利用率。 |

| 提高开关频率至12.8kHz | 开关频率翻倍后，载波周期缩短，单周期内电流脉动差异减小，环流幅值明显降低。但IGBT开关损耗与热应力成倍增加，散热设计难度加大。 | 环流幅值较基线下降约50%，但开关损耗增加约100%，工程经济性较差。 |

| 差异化开关频率(6.45kHz/6.35kHz) | 两台变流器采用微小频差调制，谐波相位自然错开，环流幅值有所减小。但导致控制器一致性变差，增加后期运维与参数整定难度。 | 环流抑制效果中等，优于基线但劣于高通滤波方案，且引入控制非对称性。 |

| PLL载波相位同步 | 利用锁相环信息强制对齐两台变流器载波相位，使谐波相位一致，环流基本消除。但该方法依赖理想通信与同步精度，实际工程中难以完全实现。 | 理论抑制效果最佳(接近0环流)，但鲁棒性差，仅适用于理想同步条件。 |



## 量化发现

- 故障录波FFT分析显示，非特征次谐波环流主导频率为720Hz，在跳闸变流器侧电流中占比高达60%，而66kV母线侧该频率含量极小。
- 基准仿真参数设定为系统电压380V、连接电抗3mH、开关频率6.4kHz，在此工况下成功复现了相位相反的高频环流。
- 将连接电抗从3mH增大至5mH，可有效降低环流幅值，但会占用额外无功容量并降低直流电压利用率。
- 将开关频率从6.4kHz提升至12.8kHz，环流幅值显著下降，但开关热应力与损耗同步增加约一倍。
- 采用差异化开关频率(6.45kHz与6.35kHz)可使谐波相位错开，实现中等程度的环流抑制，但牺牲了控制器一致性。
- 级联H桥拓扑因直流侧电容充放电不平衡易引发控制器饱和，使变流器进入非线性工作区，放大非特征次谐波环流风险。


## 关键公式

### SPWM输出电压双重傅里叶级数模型

$$$u_o(t) = \sum_{n=1}^{\infty} [A_{0n}\cos(ny) + B_{0n}\sin(ny)] + \sum_{m=1}^{\infty} [A_{m0}\cos(mx) + B_{m0}\sin(mx)] + \sum_{m=1}^{\infty} \sum_{n=\pm 1}^{\pm \infty} [A_{mn}\cos(mx+ny) + B_{mn}\sin(mx+ny)]$$$

*用于解析变流器在SPWM调制下产生的特征次谐波与非特征次谐波的幅值与相位分布，是分析载波相位差引发环流机理的核心理论工具。*



## 验证详情

- **验证方式**: 现场故障录波数据对比分析 + 电磁暂态(EMT)仿真复现验证
- **测试系统**: 冀北电网500kV变电站35kV/66kV升压变压器低压侧并列运行的两台级联H桥变流器(7号与8号)；张家口某风电场双风机并列运行系统
- **仿真工具**: 电磁暂态仿真软件(文中未明确指定具体商业软件，基于典型EMT平台搭建)
- **验证结果**: 仿真波形与现场录波数据高度吻合，成功复现了720Hz非特征次谐波环流现象及载波相位差180°时的低阻抗环流通路。五种抑制策略的仿真对比验证了高通滤波器在不影响变流器原有控制特性与无功容量的前提下，能从根本上消除环流，被推荐为最优工程方案。
