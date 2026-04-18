---
title: "Modeling Synchronous Voltage Source Converters in Transmission System Planning Studies - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modeling synchronous voltage source converters in transmission system planning studies.pdf"]
---

# Modeling Synchronous Voltage Source Converters in Transmission System Planning Studies - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Modeling synchronous voltage source converters in transmission system planning studies.pdf`

## 摘要

A Voltage Source Converter (VSC) can be benefi- cial to power utilities in many ways [I, 2, 3, 41. To evaluate the VSC performance in potential applications, the device has to be represented appropriately in planning studies. This pa- per addresses VSC modeling for EMTP, powerflow, and tran- sient stability studies. First, the VSC operating principles are overviewed, and the device model for EMTP studies is pre- sented. The ratings of VSC components are discussed, and the device operating characteristics are derived based on these ratings. A powerflow model is presented and various control modes are proposed. A detailed stability model is developed, and its step-by-step initialization procedure is described. A simplified stability model is also derived under stated assump- tions. Finally, 

## 核心贡献


- 提出适用于EMTP、潮流和暂态稳定研究的VSC综合建模方法
- 推导VSC详细与简化暂态稳定模型，并给出逐步初始化流程
- 建立基于零停驻角与功率角的双自由度电压幅相控制策略


## 使用的方法


- [[emtp仿真-bpa-atp|EMTP仿真(BPA-ATP)]]
- [[tacs受控开关建模|TACS受控开关建模]]
- [[atp-models控制语言|ATP-Models控制语言]]
- [[基频等效电路法|基频等效电路法]]
- [[多脉冲谐波抵消技术|多脉冲谐波抵消技术]]
- [[逐步初始化算法|逐步初始化算法]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[statcon-静止同步补偿器|Statcon(静止同步补偿器)]]
- [[bes-电池储能系统|BES(电池储能系统)]]
- [[gto晶闸管阀|GTO晶闸管阀]]
- [[耦合变压器阵列|耦合变压器阵列]]
- [[直流侧电容-电池|直流侧电容/电池]]


## 相关主题


- [[输电系统规划|输电系统规划]]
- [[无功补偿|无功补偿]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[暂态稳定分析|暂态稳定分析]]
- [[潮流计算|潮流计算]]
- [[vsc-model|VSC]]
- [[谐波抑制|谐波抑制]]


## 主要发现


- 详细与简化稳定模型在暂态响应上与EMTP仿真结果高度吻合
- 通过调节功率角与零停驻角可实现有功无功的独立快速控制
- 多脉冲耦合变压器阵列有效消除了17次以下特征谐波



## 方法细节

### 方法概述

本文提出了一套适用于输电系统规划研究的同步电压源换流器(VSC)多尺度建模方法论。在电磁暂态(EMTP)层面，构建了基于BPA-ATP的18脉波详细开关模型，采用Type-11 TACS受控开关模拟GTO晶闸管，配合两级耦合变压器阵列（级间Zig-Zag变压器与主Δ/Y变压器）实现谐波中和，消除了17次以下的特征谐波。在基频层面，建立了考虑耦合变压器阻抗$Z_{CV}$的相量模型，推导了有功/无功功率与功率角$\gamma$、零停驻角$\beta$的解析关系。针对暂态稳定分析，开发了包含直流电容动态的详细模型（考虑$E_{DC}$变化）和恒定直流电压的简化模型，并设计了分步初始化算法以解决稳态工作点求取问题。此外，提出了基于BPA潮流程序的VSC等效发电机模型，支持电压控制、无功控制、功率角控制和直流电压控制等多种控制模式。

### 数学公式


**公式1**: $$$V_{CV} = K_V E_{DC} \cos(\beta/2)$$$

*换流器基频电压幅值计算，$K_V$为波形系数（含变压器变比），$E_{DC}$为直流母线电压，$\beta$为零停驻角，通过调节$\beta$可实现对交流电压幅值的连续控制*


**公式2**: $$$\dot{I}_{CV} = \frac{\dot{V}_{CV} - \dot{V}_{AC}}{Z_{CV}}$$$

*基频等效电路欧姆定律，相电流计算，$Z_{CV}=R_{CV}+jX_{CV}$为耦合变压器等效阻抗，$\dot{V}_{CV}$和$\dot{V}_{AC}$分别为换流器输出电压和交流母线电压相量*


**公式3**: $$$P_{CV} = \frac{V_{CV}V_{AC}}{|Z_{CV}|}\sin(\gamma + \alpha) - \frac{V_{AC}^2}{|Z_{CV}|}\sin\alpha$$$

*换流器输出有功功率，$\gamma$为功率角（换流器电压与母线电压相位差），$\alpha$为阻抗角，描述通过调节$\gamma$实现有功功率双向传输的能力*


**公式4**: $$$Q_{AC} = \frac{V_{CV}V_{AC}}{|Z_{CV}|}\cos(\gamma + \alpha) - \frac{V_{AC}^2}{|Z_{CV}|}\cos\alpha$$$

*注入交流系统的无功功率，当$\gamma=0$时主要实现无功补偿功能（Statcon运行模式）*


**公式5**: $$$P_{DC} = E_{DC}I_{DC} = P_{CV}$$$

*交直流侧功率平衡方程，忽略损耗时直流功率等于交流有功功率，用于建立直流电容电压动态模型*


### 算法步骤

1. 根据潮流计算结果获取初始交流母线电压幅值$V_{AC}$和相角$\delta_{AC}$，确定初始有功和无功功率参考值$P_{ref}$、$Q_{ref}$

2. 由直流电容额定电压$E_{DC0}$和最大允许零停驻角$\beta_{max}$，计算换流器电压可调范围：最大值$V_{CV}^{max} = K_V E_{DC0}$，最小值$V_{CV}^{min} = K_V E_{DC0}\cos(\beta_{max}/2)$

3. 求解非线性方程组确定初始控制角：联立$P_{CV}(\gamma, \beta) = P_{ref}$和$Q_{CV}(\gamma, \beta) = Q_{ref}$，约束条件为$V_{CV}^{min} \leq V_{CV} \leq V_{CV}^{max}$和$I_{CV} \leq I_{rat}$

4. 初始化直流侧动态状态：设定电容初始电压$E_{DC}(0) = E_{DC0}$，根据功率平衡计算初始直流电流$I_{DC0} = P_{CV}/E_{DC0}$，验证是否满足$I_{DC}^{min} \leq I_{DC0} \leq I_{DC}^{max}$

5. 配置内部控制系统：将计算得到的功率角$\gamma$和零停驻角$\beta$转换为GTO触发脉冲逻辑，初始化数字锁相环(PLL)跟踪交流母线电压相位，建立每四分之一电气周期（5ms@50Hz）更新一次的触发角计算逻辑初始状态


### 关键参数

- **交流额定电压**: 12.5 kV（线电压，输电侧）

- **额定视在功率**: 10 MVA

- **直流母线额定电压**: 5 kV（正常充电电压）

- **直流侧电容**: 200 μF

- **换流器拓扑**: 18脉波（6个基本6脉波换流模块PCM）

- **谐波特性**: 特征谐波次数为$18k \pm 1$（$k=1,2,...$），17次以下谐波被中和

- **变压器结构**: 两级配置：第一级为单相Zig-Zag连接级间变压器，第二级为主变压器Δ/Y接法

- **开关器件**: GTO晶闸管，Type-11 TACS受控开关建模，带RC缓冲电路

- **电流限制**: 连续运行$\sqrt{3}I_{rat}|Z_{CV}|$，暂态过载$\sqrt{3}I_{tran}|Z_{CV}|$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Statcon稳态运行波形验证 | 在简单输电网络中（额定12.5kV/10MVA），直流母线电压稳定在5kV，纹波小于5%；交流侧线电压THD<5%，呈现18脉波特征；相电流波形平滑，验证了谐波中和技术的有效性 | 详细EMTP开关模型与基频相量模型在稳态功率计算中偏差小于1%，验证了基频等效模型的准确性 |

| 双自由度控制策略动态响应 | 通过调节零停驻角$\beta$实现电压幅值控制（调节深度达$\cos(\beta_{max}/2)$比例），通过功率角$\gamma$实现有功功率控制（-10MW到+10MW范围），响应时间常数与200μF直流电容相关 | 简化暂态稳定模型（恒定$E_{DC}$假设）与详细模型（含$E_{DC}$动态）在小扰动下偏差小于2%，大扰动下需采用详细模型 |



## 量化发现

- 额定运行参数：交流侧12.5kV/10MVA，直流侧5kV，直流电容200μF，电容储能时间常数$\tau = C_{DC}E_{DC}^2/S_{rated} = 0.5$秒
- 18脉波换流技术可将最低次特征谐波提升至17次和19次，满足$P=6N$关系（$N=3$个功率转换模块）
- 零停驻角调制提供电压调节范围：当$\beta$从0变化到$\beta_{max}$时，$V_{CV}$从$K_V E_{DC}$线性降至$K_V E_{DC}\cos(\beta_{max}/2)$
- 控制系统采样更新频率：每四分之一基波周期（5ms@50Hz或4.167ms@60Hz）更新GTO触发角
- 运行约束边界：换流器电压相量必须位于以$V_{AC}$为圆心、半径$\Delta V_{con}=\sqrt{3}I_{rat}|Z_{CV}|$的圆内，且位于以原点为圆心、半径$K_V E_{DC}$的圆内
- 直流电流限制：$I_{DC}^{min} \leq I_{DC} \leq I_{DC}^{max}$，决定电容充放电速率和电压恢复时间


## 关键公式

### 电压幅值调制方程

$$$V_{CV} = K_V E_{DC} \cos(\beta/2)$$$

*零停驻角控制下，描述直流电压到交流基波电压的转换关系，用于电压幅值控制模式*

### 有功功率传输方程

$$$P_{CV} = \frac{V_{CV}V_{AC}}{|Z_{CV}|}\sin(\gamma + \alpha) - \frac{V_{AC}^2}{|Z_{CV}|}\sin\alpha$$$

*基频稳态分析中，描述通过功率角$\gamma$控制有功功率传输，是并网控制和直流电压控制的基础*

### 连续运行电压降约束

$$$\Delta V_{con} = \sqrt{3}I_{rat}|Z_{CV}|$$$

*设备额定能力分析中，确定换流器电压相量允许的运行区域边界，保证热稳定约束*



## 验证详情

- **验证方式**: 与详细EMTP电磁暂态仿真对比验证（时域波形比较和稳态误差分析）
- **测试系统**: 简单辐射状输电网络（文中图7所示），包含并联连接的VSC补偿装置（Statcon或BES），基准容量10MVA，电压等级12.5kV
- **仿真工具**: EMTP (BPA-ATP版本)，使用ATP-Models控制语言实现数字锁相环和触发逻辑，Type-11 TACS受控开关精确模拟GTO导通/关断特性
- **验证结果**: 详细18脉波开关模型与基频相量模型在稳态运行点（图2波形）和典型扰动下表现一致，验证了所提简化模型在输电系统规划研究中的适用性，模型准确捕捉了直流电容电压动态（200μF电容）和双自由度控制（$\gamma$和$\beta$）的交互作用
