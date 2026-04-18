---
title: "Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Gu 等 - 2015 - Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene.pdf"]
---

# Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene

**作者**: CNKI
**年份**: 2022
**来源**: `17/Gu 等 - 2015 - Electromechanical transient-electromagnetic transient hybrid simulation of doubly-fed induction gene.pdf`

## 摘要

To analyze the dynamic response of double-fed induction generator (DFIG) in-depth, based on the operation principle of DFIG an electromagnetic transient model of DFIG is built and the electromagnetic transient-electromechanical transient hybrid simulation of DFIG is performed. The hybrid simulation of DFIG is implemented by the self-developed large-scale power system analysis software package based hybrid simulation platform named Power System Department- Power System Model (PSD-PSModel), and the frame of the basic model of DFIG is established. The wind farm is equivalently simulated by single machine, and IEEE 14-bus test system is utilized for the detailed simulation to analyze the dynamic behavior of the system, the control strategy and dynamic response. The achievement can contribute t

## 核心贡献


- 基于dq0坐标系构建双馈风机电磁暂态模型采用梯形积分法离散求解
- 在PSD-PSModel平台实现机电与电磁暂态混合仿真接口及迭代算法
- 提出定子端口并联大电阻与补偿电流法有效解决电机开路数值不稳定问题


## 使用的方法


- [[dq0坐标变换|dq0坐标变换]]
- [[梯形积分法|梯形积分法]]
- [[戴维南等值|戴维南等值]]
- [[混合仿真接口|混合仿真接口]]
- [[单台机等值|单台机等值]]


## 涉及的模型


- [[dfig-model|DFIG]]
- [[双质量块轴系模型|双质量块轴系模型]]
- [[转子侧换流器|转子侧换流器]]
- [[网侧换流器|网侧换流器]]
- [[同步发电机|同步发电机]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[风电场等值建模|风电场等值建模]]
- [[暂态稳定性分析|暂态稳定性分析]]
- [[故障动态响应|故障动态响应]]
- [[控制系统建模|控制系统建模]]


## 主要发现


- 三相与单相短路故障下双馈风机有功无功解耦控制策略均能快速恢复平稳
- 暂态过程中转子电流与直流母线电压受冲击显著是触发机组保护动作主因
- 桨距角控制能有效抑制机械转速突变混合仿真可清晰揭示风机内部动态响应



## 方法细节

### 方法概述

基于自主开发的PSD-PSModel平台，构建双馈风机（DFIG）电磁暂态-机电暂态混合仿真框架。外部大电网采用基波相量机电暂态模型，局部DFIG采用dq0旋转坐标系下的详细耦合电路电磁暂态模型。通过戴维南等值实现接口数据交互，采用梯形积分法对微分方程进行离散求解。针对电机开路或轻载工况下的数值不稳定问题，创新性地提出在定子三相端口并联大电阻并引入补偿电流的接口稳定技术。风电场采用单台机等值策略，实现多时间尺度动态过程的协同迭代仿真。

### 数学公式


**公式1**: $$$P = \frac{1}{2} \rho \pi R^2 C_P V_{\text{wind}}^3$$$

*风力机气动功率方程，用于计算不同风速、桨距角及转速下的机械输入功率，是转速与桨距控制的基础*


**公式2**: $$$\begin{cases} \frac{d\omega_t}{dt} = \frac{T_t - T_{\text{shaft}}}{2H_t} \\ \frac{d\omega_g}{dt} = \frac{T_{\text{shaft}} - T_e}{2H_g} \\ T_{\text{shaft}} = K_{\text{damping}}(\omega_r - \omega_g) + K_{\text{stiffness}}\theta_k \\ \frac{d\theta_k}{dt} = \omega_r - \omega_g \end{cases}$$$

*双质量块轴系动力学方程，描述风轮与发电机转子之间的机械转矩传递与扭转振荡，用于分析暂态过程中的转速突变与轴系应力*


**公式3**: $$$\begin{cases} V_P = -R_P i_P - \frac{d\lambda_P}{dt} + \omega N \lambda_P \\ V_E = -R_E i_E - \frac{d\lambda_E}{dt} \end{cases}$$$

*DFIG dq0坐标系电压方程，描述定转子绕组在旋转坐标系下的电磁耦合关系，采用梯形法离散求解*


### 算法步骤

1. 初始化全网机电暂态状态变量与DFIG电磁暂态初始值，设定仿真步长与故障触发时刻。

2. 机电暂态程序计算接口母线处的戴维南等值电压与等效阻抗，将等值参数传递至电磁暂态模块。

3. 电磁暂态模块接收等值参数，在DFIG定子三相端口并联大电阻以维持开路工况下的数值稳定性，并实时计算补偿电流以消除并联电阻引入的功率误差。

4. 采用梯形积分法对dq0坐标系下的DFIG微分代数方程进行离散化求解，更新定转子电流、磁链、直流母线电压及轴系机械状态。

5. 将DFIG定子侧计算得到的瞬时三相注入电流进行傅里叶提取或相量转换，反馈至机电暂态网络接口。

6. 机电暂态程序利用注入电流更新全网潮流与节点电压相量，完成一个机电步长计算，并判断是否满足收敛容差。

7. 若未收敛或到达下一仿真时刻，则重复步骤2-6进行迭代；若满足条件则推进至下一时间步，直至完成故障全过程仿真。


### 关键参数

- **DFIG单机额定功率**: 1.5 MW

- **风电场等值机组数**: 24台

- **等值总出力**: 36 MW

- **故障切除时间**: 0.1 s

- **有功恢复时间**: 约3 s

- **轴系模型**: 双质量块

- **积分方法**: 梯形法

- **接口稳定技术**: 定子并联大电阻+补偿电流法



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相接地对称短路故障（母线4-5支路） | 故障持续0.1s切除后，DFIG有功出力经历剧烈波动，在约3s后恢复至稳态；无功出力在扰动时刻剧烈变化后迅速按解耦控制策略恢复平稳；转子电流与直流母线电压出现显著冲击峰值；桨距角控制动作有效抑制了机械转速突变。 | 相比传统机电暂态简化模型（忽略转子与换流器动态），混合仿真清晰揭示了转子电流与直流电压的内部冲击动态，为保护定值整定提供精确时域波形，避免了简化模型可能导致的保护误动评估偏差。 |

| 单相接地短路故障（母线4-5支路） | 非对称故障下，DFIG有功无功解耦控制策略依然保持快速响应，系统电压与电流波形呈现典型不对称特征，控制系统在0.1s故障切除后迅速调节至新稳态，验证了模型在不对称工况下的数值稳定性。 | 验证了定子并联大电阻与补偿电流法在不对称故障开路工况下的有效性，未出现数值发散，仿真步长保持稳定，计算效率较全电磁暂态仿真提升显著，满足大电网混合仿真需求。 |



## 量化发现

- 24台1.5MW双馈风机等值为单台36MW机组接入IEEE 14节点系统，等值策略在工程允许误差范围内有效表征风电场群动态。
- 三相短路故障切除后，DFIG有功出力在约3s内完成动态恢复并达到平稳状态，验证了有功无功解耦控制策略的快速性。
- 故障持续时间为0.1s，期间转子电流与直流母线电压冲击幅值显著，是触发机组保护动作的主要量化指标。
- 采用梯形积分法离散求解，结合定子端口并联大电阻与补偿电流技术，有效消除了电机开路时的数值振荡，保证混合仿真迭代收敛。


## 关键公式

### 风力机气动功率方程

$$$P = \frac{1}{2} \rho \pi R^2 C_P V_{\text{wind}}^3$$$

*用于计算不同风速、桨距角及转速下的机械输入功率，是转速与桨距控制的基础*

### 双质量块轴系动力学方程

$$$\begin{cases} \frac{d\omega_t}{dt} = \frac{T_t - T_{\text{shaft}}}{2H_t} \\ \frac{d\omega_g}{dt} = \frac{T_{\text{shaft}} - T_e}{2H_g} \\ T_{\text{shaft}} = K_{\text{damping}}(\omega_r - \omega_g) + K_{\text{stiffness}}\theta_k \\ \frac{d\theta_k}{dt} = \omega_r - \omega_g \end{cases}$$$

*描述风轮与发电机转子之间的机械转矩传递与扭转振荡，用于分析暂态过程中的转速突变与轴系应力*

### DFIG dq0坐标系电压方程

$$$\begin{cases} V_P = -R_P i_P - \frac{d\lambda_P}{dt} + \omega N \lambda_P \\ V_E = -R_E i_E - \frac{d\lambda_E}{dt} \end{cases}$$$

*电磁暂态核心模型，描述定转子绕组在旋转坐标系下的电磁耦合关系，采用梯形法离散求解*



## 验证详情

- **验证方式**: 数字仿真验证
- **测试系统**: IEEE 14节点测试系统（含5台同步发电机、3台同步调相机、15条支路，节点2接入36MW等值DFIG）
- **仿真工具**: PSD-PSModel（中国电科院自主研发的电磁暂态-机电暂态混合仿真平台）
- **验证结果**: 成功实现DFIG详细电磁模型与大电网机电模型的混合仿真。在对称与非对称故障工况下，模型数值稳定，控制策略响应符合预期，清晰捕捉到转子电流、直流电压冲击及桨距角调节过程，验证了混合接口算法与补偿技术的工程实用性，为后续与风机厂家合作建立实际机组详细模型提供了可靠平台。
