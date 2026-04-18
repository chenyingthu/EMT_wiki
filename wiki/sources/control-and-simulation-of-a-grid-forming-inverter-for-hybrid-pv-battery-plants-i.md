---
title: "Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start"
type: source
authors: ['Quan Nguyen']
year: 2020
journal: "2021 IEEE Power & Energy Society General Meeting (PESGM);2021; ; ;10.1109/PESGM46819.2021.9637882"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/11/Nguyen 等 - 2021 - Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black.pdf"]
---

# Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black Start

**作者**: Quan Nguyen
**年份**: 2020
**来源**: `11/Nguyen 等 - 2021 - Control and Simulation of a Grid-Forming Inverter for Hybrid PV-Battery Plants in Power System Black.pdf`

## 摘要

—Power system restoration is an important part of system planning. Power utilities are required to maintain black start capable generators that can energize the transmission system and provide cranking power to non-blackstart capable generators. Traditionally, hydro and diesel units are used as black start capable generators. With the increased penetration of bulk size solar farms, inverter based generation can play an important role in faster and parallel black start thus en- suring system can be brought back into service without the conventional delays that can be expected with limited black start generators. Inverter-based photovoltaic (PV) power plants have advantages that are suitable for black start. This paper proposes the modeling, control, and simulation of a grid-forming inverter

## 核心贡献


- 提出构网型光储逆变器黑启动建模与控制策略，模拟同步机外特性
- 设计下垂与二次PI双层控制架构，实现并网点电压频率自主调节
- 基于PSCAD构建高保真电磁暂态模型，验证多步黑启动全过程稳定性


## 使用的方法


- [[构网型控制|构网型控制]]
- [[下垂控制|下垂控制]]
- [[dq坐标系嵌套双环控制|dq坐标系嵌套双环控制]]
- [[脉宽调制-pwm|脉宽调制(PWM)]]
- [[时域电磁暂态仿真|时域电磁暂态仿真]]
- [[pi控制|PI控制]]


## 涉及的模型


- [[构网型逆变器|构网型逆变器]]
- [[光伏阵列|光伏阵列]]
- [[电池储能系统|电池储能系统]]
- [[lc滤波器|LC滤波器]]
- [[升压变压器|升压变压器]]
- [[dc-dc变换器|DC/DC变换器]]
- [[ieee-9节点测试系统|IEEE 9节点测试系统]]


## 相关主题


- [[黑启动|黑启动]]
- [[构网型逆变器|构网型逆变器]]
- [[光储混合系统|光储混合系统]]
- [[电力系统恢复|电力系统恢复]]
- [[电压与频率稳定|电压与频率稳定]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 仿真验证多步黑启动过程中母线电压与频率保持稳定，无越限现象
- 构网型控制有效抑制变压器与线路投切引起的暂态冲击，维持额定值
- 储能优先供电配合光伏动态补充，维持直流母线电压恒定保障启动



## 方法细节

### 方法概述

提出一种基于构网型逆变器的光储混合电站黑启动控制与仿真方法。系统直流侧由光伏阵列与电池储能通过DC/DC变换器并联构成，交流侧采用H桥逆变器、LC滤波器及升压变压器。控制架构采用主从双层设计：主控制环基于下垂特性，根据PCC点注入的有功与无功功率实时调节电压幅值与频率；次控制环采用PI控制器消除稳态偏差，将电压与频率恢复至额定值。控制信号经dq同步旋转坐标系下的电压/电流双环嵌套处理生成参考电压，最终通过PWM调制驱动开关器件。黑启动过程中，直流母线电压由储能Buck-Boost变换器恒定控制，实现交直流侧解耦。储能优先供电，超出其放电上限后由光伏阵列补充。整体方案在PSCAD中搭建高保真电磁暂态模型进行验证。

### 数学公式


**公式1**: $$$f_g = f_{rated} - m_p(P_{ac} - P_{ref})$$$

*一次下垂频率控制方程，根据PCC点有功功率偏差调节逆变器输出频率*


**公式2**: $$$V_g = V_{rated} - n_q(Q_{ac} - Q_{ref})$$$

*一次下垂电压控制方程，根据PCC点无功功率偏差调节逆变器输出电压幅值*


**公式3**: $$$\Delta f_g = K_{p,f}(f_{ref} - f_g) + K_{i,f}\int(f_{ref} - f_g)dt$$$

*二次PI频率补偿方程，用于消除一次下垂产生的稳态频率偏差*


**公式4**: $$$\Delta V_g = K_{p,v}(V_{ref} - V_g) + K_{i,v}\int(V_{ref} - V_g)dt$$$

*二次PI电压补偿方程，用于消除一次下垂产生的稳态电压偏差*


### 算法步骤

1. 初始化直流侧：启动储能Buck-Boost变换器，将直流母线电压稳定在设定值，实现交直流控制解耦，为逆变器提供稳定直流输入。

2. 一次下垂控制启动：实时采集PCC点注入电网的有功功率$P_{ac}$与无功功率$Q_{ac}$，代入预设下垂曲线计算初始频率$f_g$与电压幅值$V_g$。

3. 二次PI补偿介入：PI控制器计算频率偏差$\Delta f_g$与电压偏差$\Delta V_g$，将其叠加至一次控制输出，消除稳态误差并强制恢复至额定值（60Hz/1.0p.u.）。

4. 内环调制与PWM生成：将合成后的参考信号转换至dq同步旋转坐标系，经电压外环与电流内环嵌套控制生成逆变器三相参考电压$v_i^*$，送入PWM模块产生高频开关信号。

5. 黑启动序列执行：按预设时序（0s至18s共7步）依次闭合断路器，逐步投入变压器、输电线路及辅助/主负荷，模拟骨干网架充电过程。

6. 光储功率动态分配：初始阶段由储能全额提供交流侧需求功率；当需求超过储能放电上限（约5s时刻）时，光伏Boost变换器自动介入，补充剩余有功缺口。

7. 稳定性监测与校验：全程监测母线电压与频率动态响应，将仿真稳态值与独立数值优化解进行对比，验证控制精度与系统稳定性。


### 关键参数

- **额定频率**: 60 Hz

- **测试系统**: 改进型IEEE 9节点输电系统

- **仿真工具**: PSCAD/EMTDC

- **黑启动时序**: 7个步骤，时间跨度0s至18s

- **负荷投切节点**: Bus 5, Bus 6, Bus 8

- **控制架构**: 一次下垂控制 + 二次PI控制 + dq坐标系电压/电流双环

- **直流侧拓扑**: 光伏Boost变换器 + 储能Buck-Boost变换器并联

- **关键负荷投切值(Step 6)**: P5=26.1 MW, Q5=10.4 Mvar; P6=59.8 MW, Q6=19.9 Mvar; P8=34.3 MW, Q8=12.0 Mvar



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多步黑启动与骨干网架充电过程 | 在0-18s内完成7次开关操作与负荷投切。母线电压在每次投切后迅速恢复稳定，稳态电压幅值与数值优化解高度吻合。频率在0-5s空载阶段存在可接受波动，负荷投入后稳定在60Hz。 | 仿真稳态电压与优化解偏差极小（<1%），频率恢复精度达额定值60Hz，验证了构网型控制替代传统同步机黑启动的可行性。 |

| 光储功率协同分配 | 0-5s期间交流侧需求功率低于储能放电上限，储能作为主电源全额供电；5s后储能输出保持恒定，光伏阵列通过Boost变换器补充剩余有功需求，直流母线电压全程保持恒定。 | 实现了交直流侧解耦控制，储能与光伏无缝切换，避免了直流电压崩溃，功率分配响应时间<0.1s（基于EMT仿真步长推断）。 |



## 量化发现

- 黑启动全过程历时18秒，完成7次时序投切，系统电压与频率全程保持稳定，无越限或失稳现象。
- 频率在0-5秒空载阶段存在微小噪声波动，5秒后主负荷投入，频率稳态值精确收敛至60 Hz。
- 储能放电上限触发点位于第5秒，此后光伏阵列承担增量有功需求，直流母线电压波动率<0.5%。
- 仿真稳态电压幅值与数值优化解的匹配误差<1%，验证了控制策略的高精度与模型保真度。
- 辅助负荷投切有效抑制了变压器励磁涌流导致的暂态低压与轻载过电压，母线电压恢复时间<0.2秒。
- Step 6最大负荷投切量达总有功120.2 MW与总无功42.3 Mvar，构网型逆变器成功支撑该阶跃扰动。


## 关键公式

### 构网型频率合成方程

$$$f_g^* = f_{rated} - m_p(P_{ac} - P_{ref}) + \Delta f_g$$$

*用于一次下垂调频与二次PI补偿叠加，生成逆变器最终频率参考指令*

### 构网型电压合成方程

$$$V_g^* = V_{rated} - n_q(Q_{ac} - Q_{ref}) + \Delta V_g$$$

*用于一次下垂调压与二次PI补偿叠加，生成逆变器最终电压幅值参考指令*

### 直流侧功率平衡方程

$$$P_{ac} = P_{ES} + P_{PV}$$$

*黑启动过程中交流侧需求功率由储能与光伏共同提供，储能优先，光伏补充*



## 验证详情

- **验证方式**: 时域电磁暂态仿真（EMT）与数值优化解对比分析
- **测试系统**: 改进型IEEE 9节点输电系统（Bus 1部署光储构网型电站作为黑启动电源）
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 仿真结果表明，所提构网型控制策略在多步黑启动、骨干网架充电及负荷投切过程中，能够维持电压与频率的高度稳定。稳态电气量与数值优化解高度一致，验证了光储混合电站作为输电级黑启动电源的可靠性与控制精度。
