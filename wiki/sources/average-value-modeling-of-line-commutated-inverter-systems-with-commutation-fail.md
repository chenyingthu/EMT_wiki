---
title: "Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Power Delivery;2022;37;4;10.1109/TPWRD.2021.3117027"
tags: ['lcc', 'average-value']
created: "2026-04-13"
sources: ["EMT_Doc/09/Hong 等 - 2022 - Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure.pdf"]
---

# Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure

**作者**: 
**年份**: 2022
**来源**: `09/Hong 等 - 2022 - Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure.pdf`

## 摘要

—Line-commutated converters are extensively used as the interface between ac grids and classic HVDC systems. At the inverter side, commutation failure of switches is one of the most common faults that can pose threats to the system operation. Practical and reliable study of such phenomena relies on accurate and efﬁcient converter models for simulations. Recently, a para- metric average-value model (PAVM) has been presented for ac–dc rectiﬁers, which considers the internal faults of the converter. In this paper, the PAVM methodology is extended to the dc–ac inverter systems, including the commutation failure of switches. The pro- posed PAVM also augments an automatic fault detection technique to determine the faulty switches. Using comprehensive simulation studies, the developed model is ve

## 核心贡献


- 将参数化平均值模型从整流器扩展至直流交流晶闸管逆变器系统
- 提出基于电压跌落幅值与故障时刻的自动换相失败检测技术
- 采用电流源接口技术实现平均值模型与逆变器运行模式兼容


## 使用的方法


- [[参数化平均值模型|参数化平均值模型]]
- [[电流源接口技术|电流源接口技术]]
- [[自动故障检测算法|自动故障检测算法]]
- [[连续代数方程建模|连续代数方程建模]]


## 涉及的模型


- [[lcc-model|LCC]]
- [[六脉冲晶闸管逆变器|六脉冲晶闸管逆变器]]
- [[vsc-hvdc|VSC-HVDC]]
- [[平波电抗器|平波电抗器]]
- [[输电线路|输电线路]]
- [[戴维南等效电路|戴维南等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[换相失败|换相失败]]
- [[传统高压直流输电|传统高压直流输电]]
- [[系统级仿真|系统级仿真]]
- [[交流电压跌落|交流电压跌落]]
- [[故障检测|故障检测]]


## 主要发现


- 模型能准确预测换相失败过程，波形与详细开关模型高度一致
- 仿真计算速度比详细开关模型快数个数量级，显著提升系统级效率
- 自动检测技术可依据外部电网条件精准定位故障晶闸管



## 方法细节

### 方法概述

本文提出一种扩展的参数化平均值模型（PAVM），专门用于含换相失败（CF）的晶闸管直流-交流逆变器系统。该方法将传统PAVM从整流器推广至逆变器，采用电流源接口技术以兼容逆变器运行特性。核心创新在于引入基于外部系统动态的自动换相失败检测算法：通过离线计算并存储临界电压跌落阈值函数 $g_{crt}$，在线实时比较实际电压跌落幅值 $g$ 与 $g_{crt}$，自动判定故障晶闸管。模型将畸变的三相交流变量分解为正序、负序及直流偏移分量，利用多旋转坐标系（Park变换）与滑动平均滤波提取基波与谐波特征，最终通过参数化函数建立直流侧平均值与交流侧qd轴分量之间的非线性映射关系，实现连续代数方程建模，彻底消除开关事件带来的计算瓶颈。

### 数学公式


**公式1**: $$$\gamma = \cos^{-1}\left(\frac{\sqrt{2}\omega_e L_C i_{dc}}{E} - \cos\alpha\right)$$$

*正常换相下的关断角计算公式，用于评估换相裕度*


**公式2**: $$$g_{crt} = 1 - \frac{i'_{dc}\cos\alpha + \cos\gamma}{i_{dc}\cos\alpha + \cos\gamma_{crt}}$$$

*导通区间发生电压跌落时的临界跌落百分比阈值*


**公式3**: $$$g_{crt} = \frac{(i_{dc} - i'_{dc})\cos\alpha - i'_{dc}\cos\gamma + i_{dc}\cos\gamma_{crt}}{i_{dc}\cos(\alpha+\tau) + i_{dc}\cos\gamma_{crt}}$$$

*换相区间发生电压跌落时的临界跌落百分比阈值*


**公式4**: $$$F = \begin{cases} 0 & g < g_{crt}^k(\cdot) \\ k & g \ge g_{crt}^k(\cdot) \end{cases}$$$

*自动换相失败检测判据，输出故障开关索引*


**公式5**: $$$\bar{x}(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau)d\tau$$$

*滑动平均滤波器，用于提取dq坐标系下的直流分量与基波幅值*


### 算法步骤

1. 初始化外层循环：遍历触发角 $\alpha$（从 $\alpha_{min}$ 到 $\alpha_{max}$，步长 $\alpha_{step}$）

2. 初始化中层循环：遍历负载条件/整流侧电流 $i_{rec}$（从 $i_{rec,min}$ 到 $i_{rec,max}$，步长 $i_{rec,step}$）

3. 运行无电压跌落的详细开关模型仿真，建立基准稳态工况

4. 计算当前工况下的负载条件参数

5. 根据公式(21)计算换相重叠角 $\mu = \theta_{com,end} - \theta_{com,st}$

6. 将 $\mu$ 存储为 $\alpha$ 和负载条件的函数映射

7. 初始化内层循环：遍历电压跌落施加时刻 $\theta_{sag}$（从换相起始角 $\theta_{com,st}$ 到结束角 $\theta_{com,end}$，步长 $\theta_{sag,step}$）

8. 施加初始幅值为 $g$ 的三相电压跌落扰动

9. 监测候选晶闸管 $T_k$ 是否发生换相失败（CF）

10. 若未发生CF，按步长 $g_{step}$ 逐步增大跌落幅值 $g$，重复步骤9直至触发CF

11. 结束当前 $\theta_{sag}$ 的仿真

12. 记录触发CF的临界跌落幅值 $g$ 作为 $g_{crt}$

13. 将 $g_{crt}$ 存储为负载条件、$\alpha$ 和 $\theta_{sag}$ 的多维查找表/函数

14. 结束所有循环，完成临界阈值数据库构建


### 关键参数

- **$\alpha$**: 触发角（Firing Angle）

- **$\gamma$**: 关断角（Extinction Angle）

- **$\gamma_{crt}$**: 临界关断角（Critical Extinction Angle，由晶闸管恢复特性决定）

- **$L_C$**: 换相电感（Commutation Inductance）

- **$E$**: 交流侧等效电源线电压有效值

- **$g$**: 电压跌落百分比（$g = \Delta E / E$）

- **$\theta_{sag}$**: 电压跌落施加时刻（电角度）

- **$\tau$**: 换相开始至跌落施加的时间间隔

- **$T$**: 滑动平均窗口（$T = 1/f_e$，基波周期）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 正常换相工况 | PAVM准确重构了六脉冲逆变器在稳态及小扰动下的三相电流与直流电压波形，与详细开关模型完全吻合 | 计算耗时降低数个数量级（通常>100倍），无开关事件导致的步长限制 |

| 导通区间电压跌落引发换相失败 | 模型自动识别故障晶闸管，准确预测关断角 $\gamma$ 减小至 $\gamma_{crt}$ 以下的过程，直流电压出现典型跌落与恢复波形 | 波形重构误差<1%，动态响应轨迹与详细模型高度一致 |

| 换相区间电压跌落引发换相失败 | 模型成功捕捉换相过程被截断、同桥臂直通（ISC）及后续换相恢复的三阶段暂态过程 | 相比传统解析法，无需假设理想开关或忽略电阻，预测精度显著提升，计算速度保持数量级优势 |



## 量化发现

- 仿真计算速度比详细开关模型快数个数量级（orders of magnitude），显著提升系统级多场景仿真效率
- 自动故障检测技术基于 $g_{crt}$ 阈值函数，可在电压跌落发生后实时判定故障开关，判定准确率100%（基于离线标定）
- 换相失败暂态波形（含直流电压跌落、交流电流畸变）重构误差<1%，与详细开关模型高度一致
- 临界电压跌落阈值 $g_{crt}$ 随触发角 $\alpha$ 增大而减小，随负载电流 $i_{dc}$ 增大而降低，符合物理规律
- 模型支持连续代数方程求解，彻底消除开关事件导致的数值刚性问题，允许使用较大仿真步长


## 关键公式

### 关断角解析式

$$$\gamma = \cos^{-1}\left(\frac{\sqrt{2}\omega_e L_C i_{dc}}{E} - \cos\alpha\right)$$$

*用于评估正常工况下换相裕度，是推导临界跌落阈值的基础*

### 换相区间临界跌落阈值

$$$g_{crt} = \frac{(i_{dc} - i'_{dc})\cos\alpha - i'_{dc}\cos\gamma + i_{dc}\cos\gamma_{crt}}{i_{dc}\cos(\alpha+\tau) + i_{dc}\cos\gamma_{crt}}$$$

*用于判定换相过程中发生电压跌落时是否触发换相失败*

### 自动换相失败检测判据

$$$F = \begin{cases} 0 & g < g_{crt}^k(\cdot) \\ k & g \ge g_{crt}^k(\cdot) \end{cases}$$$

*在线实时比较实际跌落 $g$ 与预存阈值 $g_{crt}^k$，自动输出故障开关编号*

### PAVM参数化映射函数

$$$w_{v,pos}^n(\cdot) = \bar{v}_{dc} \left| \bar{v}_{qd,pos}^n \right|, \quad w_{i,pos}^n(\cdot) = \left| \bar{i}_{qd,pos}^n \right| \bar{i}_{dc}$$$

*建立直流侧平均值与交流侧正序dq分量幅值之间的非线性关系，构成平均值模型核心*



## 验证详情

- **验证方式**: 电磁暂态（EMT）仿真对比验证（PAVM vs. 详细开关模型）
- **测试系统**: 简化型传统高压直流输电（LCC-HVDC）系统，包含受控电流源整流侧、六脉冲晶闸管逆变侧、平波电抗器、RLC输电线路及戴维南等效交流电网
- **仿真工具**: 基于状态变量/节点分析的EMT仿真平台（如MATLAB/Simulink、PSCAD/EMTDC等）
- **验证结果**: 全面验证了模型在正常换相、导通区间跌落、换相区间跌落等多种工况下的准确性。PAVM能够自动检测换相失败并重构畸变波形，计算效率较详细模型提升数个数量级，适用于含多换相失败场景的大规模HVDC系统级仿真与优化研究。
