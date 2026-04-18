---
title: "A steady-state initialization procedure for generic voltage-source converters in electromagnetic transient simulations"
type: source
authors: ['Guilherme', 'Cirilo', 'Leandro']
year: 2023
journal: "Electric Power Systems Research, 221 (2023) 109404. doi:10.1016/j.epsr.2023.109404"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/1-s2.0-S0378779623002936-main.pdf"]
---

# A steady-state initialization procedure for generic voltage-source converters in electromagnetic transient simulations

**作者**: Guilherme, Cirilo, Leandro
**年份**: 2023
**来源**: `04/1-s2.0-S0378779623002936-main.pdf`

## 摘要

0378-7796/© 2023 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- A steady-state initialization procedure for generic voltage-source converters ENIC Division, Grid Innovation Research Laboratory, Central Research Institute of Electric Power Industry (CRIEPI), 2-6-1 Nagasaka, Electromagnetic transient (EMT) simulations are often performed to analyze disturbances which occur during a steady-state operati

## 核心贡献


- 提出通用VSC稳态初始化启发式流程，系统化设定电路与控制部分初值
- 基于正序与三相交流潮流解，直接计算并赋值VSC内部状态变量与历史项
- 消除零初值启动的漫长过渡过程，实现含多VSC电网EMT仿真的直接稳态启动


## 使用的方法


- [[潮流计算|潮流计算]]
- [[三相交流稳态计算|三相交流稳态计算]]
- [[启发式初始化|启发式初始化]]
- [[梯形积分法|梯形积分法]]
- [[numerical-integration|数值积分]]
- [[dq坐标变换|dq坐标变换]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[lc滤波器|LC滤波器]]
- [[直流电容|直流电容]]
- [[配电网络|配电网络]]
- [[同步发电机|同步发电机]]
- [[rlc负荷|RLC负荷]]
- [[锁相环-pll|锁相环(PLL)]]
- [[自动电压-电流调节器|自动电压/电流调节器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[稳态初始化|稳态初始化]]
- [[vsc-model|VSC]]
- [[潮流计算|潮流计算]]
- [[配电系统仿真|配电系统仿真]]
- [[控制系统初始化|控制系统初始化]]


## 主要发现


- 采用所提流程初始化后，6.6kV双VSC配网仿真几乎无暂态过程，直接达到稳态
- 未初始化时仿真运行300毫秒仍无法收敛，验证了直接稳态启动的必要性
- 电路与控制状态变量初值精准匹配潮流解，有效抑制了启动瞬间的数值振荡



## 方法细节

### 方法概述

本文提出一种面向通用电压源换流器（VSC）的系统化启发式稳态初始化流程，旨在消除电磁暂态（EMT）仿真中因零初值启动导致的漫长过渡过程。该方法分为三个阶段：首先进行正序潮流计算，将发电机、负荷及VSC分别等效为P-V、P-Q节点或三相平衡源；其次基于潮流解在$j\omega$域计算三相交流稳态解（实际为不对称稳态）；最后利用梯形积分法的历史项（$x_0$）特性，将稳态相量解逐一映射至VSC主电路（互联变压器、LC滤波器、直流电容）与控制系统（低通滤波器、PLL、DCAVR/AQR/ACAVR/ACR调节器）的动态状态变量中。通过精确设定各积分器的初始历史值，实现电路与控制状态的完美匹配，使EMT仿真可直接从稳态启动。

### 数学公式


**公式1**: $$$\int_0^h x dt \cong \frac{h}{2}(x_0 + x_1)$$$

*梯形积分法近似公式，$x_0$为$t=0$时刻的过去历史项，用于初始化EMT仿真中的状态变量*


**公式2**: $$$I_s = \frac{I_g}{\sqrt{3}} \exp\left(j\frac{\pi}{6}\right)$$$

*计算Δ接法变压器二次侧绕组电流，基于电网连接点正序电流$I_g$*


**公式3**: $$$V_h = \frac{V_{h\Delta}}{\sqrt{3}} \exp\left(-j\frac{\pi}{6}\right)$$$

*将滤波器线电压$V_{h\Delta}$转换为相电压$V_h$，用于初始化滤波器电容电压*


**公式4**: $$$H(j\omega) = \frac{1}{1+j\omega\tau}$$$

*电压/电流测量模块中一阶低通滤波器（LPF）的传递函数，用于初始化测量延迟环节*


**公式5**: $$$\hat{\theta} = \theta + \angle H(j\omega)$$$

*PLL积分器输出初值，$\theta$为电网电压相位，$\angle H(j\omega)$为LPF在工频下的相移*


**公式6**: $$$\hat{i}_d^* = \frac{\hat{P}^*}{\hat{V}_g}$$$

*DCAVR调节器PI控制器输出初值，基于目标有功功率$\hat{P}^*$与电网电压幅值$\hat{V}_g$计算*


**公式7**: $$$\hat{i}_q^* = \frac{\hat{Q}^*}{\hat{V}_g} + \omega_0 \hat{C}_h \hat{V}_h$$$

*AQR/ACAVR调节器PI控制器输出初值，包含目标无功功率项与滤波器电容电流补偿项*


### 算法步骤

1. 阶段1（正序潮流计算）：构建系统正序网络，将同步发电机与高压母线等效为P-V节点，负荷等效为P-Q节点。根据VSC控制模式（AQR或ACAVR）将其分别替换为P-Q或P-V节点，求解正序潮流获得各节点电压幅值、相角及注入功率。

2. 阶段2（三相交流稳态计算）：基于阶段1结果，将P-V节点替换为三相电压源，P-Q负荷替换为等效RLC电路，VSC替换为三相平衡电流源（AQR模式）或电压源（ACAVR模式）。在$j\omega$域进行三相不对称交流稳态计算，获取各支路电压、电流相量。

3. 阶段3-电路初始化：利用梯形积分历史项$x_0$赋值。①互联变压器：根据电网侧电流$I_g$计算二次侧电流$I_s$与一次侧电流$I_p$，设定电感电流$x_0$；②LC滤波器：通过变压器压降计算滤波器端电压$V_h$，结合电容阻抗计算电感电流$I$，设定电容电压与电感电流$x_0$；③直流侧：将直流电容电压初值设为用户指定的额定值，设定电容电压$x_0$；④开关器件：忽略ON/OFF状态初始化（影响极小）。

4. 阶段3-控制系统初始化：①测量模块：将稳态交直流电压/电流代入LPF传递函数$H(j\omega)$，计算输出相量并转换为时域初值，设定LPF状态变量$x_0$；②PLL模块：PI控制器输出$x_0$设为0（稳态频差为0），积分器输出$x_0$设为$\hat{\theta}=\theta+\angle H(j\omega)$；③调节器模块：DCAVR的PI输出$x_0$设为$\hat{P}^*/\hat{V}_g$，AQR/ACAVR的PI输出$x_0$设为$\hat{Q}^*/\hat{V}_g+\omega_0\hat{C}_h\hat{V}_h$，ACR的PID积分部分$x_0$设为0（稳态误差为0）；④PWM模块：死区发生器动态状态忽略初始化。


### 关键参数

- **仿真时间步长**: 0.5 μs

- **电网基频**: 50 Hz

- **直流电容电压设定值**: 额定电压（用户指定）

- **变压器接线方式**: Δ-Δ（示例，可推广至任意接线）

- **滤波器拓扑**: Y型或Δ型LC滤波器

- **数值积分方法**: 梯形积分法（或2S-DIRK）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 6.6 kV双VSC配电网络（含1.8 MW光伏PCS与STATCOM） | 未采用初始化时，仿真运行300 ms后系统仍未收敛，电压电流从零快速上升后因控制反馈过大导致调节器发散，工作点偏离正确值，波形出现严重低频畸变；采用所提流程初始化后，仿真启动瞬间仅存在极微小暂态（源于未初始化开关状态），随后立即锁定稳态，且高频开关谐波在t=0后迅速建立，波形平滑无振荡。 | 相比零初值启动，所提方法将收敛时间从>300 ms（发散未收敛）缩短至几乎瞬时（<1个基波周期），彻底消除启动数值振荡，计算效率提升显著。 |



## 量化发现

- 仿真时间步长固定为0.5 μs以精确解析VSC开关动作
- 未初始化仿真持续300 ms仍无法达到稳态，控制变量发散且波形畸变率极高
- 初始化后系统暂态幅值可忽略不计，直接匹配潮流解对应的稳态工作点
- 控制系统积分器初值误差被完全消除，避免了启动瞬间的数值振荡与低频谐波畸变
- 开关状态未初始化引入的暂态影响极小，验证了启发式忽略该步骤的合理性


## 关键公式

### 梯形积分历史项初始化公式

$$$\int_0^h x dt \cong \frac{h}{2}(x_0 + x_1)$$$

*用于将稳态相量解转换为EMT仿真中所有动态元件（电感、电容、积分器）在t=0时刻的过去历史值$x_0$*

### PLL相位同步初值公式

$$$\hat{\theta} = \theta + \angle H(j\omega)$$$

*用于初始化PLL积分器输出，确保abc-dq坐标变换在仿真起始时刻即与电网电压相位精确同步*

### 无功/电压调节器电流参考初值公式

$$$\hat{i}_q^* = \frac{\hat{Q}^*}{\hat{V}_g} + \omega_0 \hat{C}_h \hat{V}_h$$$

*用于初始化AQR与ACAVR调节器PI控制器输出，精确补偿滤波器电容电流并匹配目标无功/电压设定值*



## 验证详情

- **验证方式**: 电磁暂态仿真对比分析（有/无初始化）
- **测试系统**: 6.6 kV配电网络，包含18.5 km水平排列架空线路（导线OC 150/60 mm²，大地电阻率100 Ωm）、1.8 MW光伏功率调节系统（PCS，AQR模式，Q*=0）与STATCOM（ACAVR模式，V*=1 pu/6.6 kV）
- **仿真工具**: eXpandable Transient Analysis Program (XTAP)
- **验证结果**: 验证了所提启发式初始化流程的有效性。未初始化时系统长时间无法收敛且波形严重畸变；初始化后系统几乎无暂态过程直接达到稳态，证明该方法可大幅缩短含多VSC电网EMT仿真的计算时间并保证数值稳定性，适用于通用两电平VSC模型。
