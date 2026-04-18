---
title: "Adaptive Modular Multilevel Converter Model for Electromagnetic Transient Simulations"
type: source
authors: ['未知']
year: 2020
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2020.2993502"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/05/TPWRD.2020.2993502.pdf.pdf"]
---

# Adaptive Modular Multilevel Converter Model for Electromagnetic Transient Simulations

**作者**: 
**年份**: 2020
**来源**: `05/TPWRD.2020.2993502.pdf.pdf`

## 摘要

—This paper proposes an adaptive model of modular multilevel converter (MMC) for electromagnetic transient (EMT) simulations. The model is applicable to MMCs with arbitrary numbers of half-bridge and full-bridge submodules. The proposed design includes average value model, arm equivalent model, and detailed equivalent model. It allows smoothly transitioning from one model to another during time-domain simulations depending on the desired accuracy and execution time constraints. Modifications required in conventional MMC models to achieve smooth transitions are presented in the paper. Time-domain initialization methods are developed for each constituting model, including initialization of the appropriate control system blocks. Validity and effectiveness of the proposed adaptive model is dem

## 核心贡献


- 提出包含三种等效模型的自适应MMC架构，实现仿真过程平滑切换
- 设计新型桥臂平均值模型统一电气接口，消除切换时的拓扑结构突变
- 开发各模型时域初始化与控制切换策略，确保状态转移无暂态冲击


## 使用的方法


- [[模型切换技术|模型切换技术]]
- [[平均值模型|平均值模型]]
- [[桥臂等效模型|桥臂等效模型]]
- [[详细等效模型|详细等效模型]]
- [[时域初始化|时域初始化]]
- [[诺顿等效|诺顿等效]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块|半桥子模块]]
- [[全桥子模块|全桥子模块]]
- [[mmc-model|MMC]]
- [[耦合变压器|耦合变压器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[仿真加速|仿真加速]]
- [[mmc-model|MMC]]
- [[控制系统建模|控制系统建模]]


## 主要发现


- 在401电平MMC-HVDC系统中验证了模型切换的平滑性与接口一致性
- 自适应模型在保持外部电气特性精度的同时，显著降低了仿真计算耗时
- 所提时域初始化方法有效消除了模型切换瞬间产生的电压电流暂态冲击



## 方法细节

### 方法概述

提出一种适用于电磁暂态(EMT)仿真的自适应MMC模型架构，支持半桥(HB)与全桥(FB)子模块的任意混合配置。该架构集成平均值模型(AVM)、桥臂等效模型(AEM)和详细等效模型(DEM)，通过统一的二端口诺顿等效电路实现电气接口标准化，彻底消除模型切换时的拓扑结构突变。所有模型在拓扑上并联，非激活模型在求解器中提供零导纳与零电流源，确保节点电压连续性。模型以动态链接库(DLL)封装，支持仿真运行时动态激活/去激活。控制系统采用标准级联架构，外环(PLL与功率/电压控制)始终运行，内环根据激活模型切换：AVM输出交流电势参考，AEM/DEM输出桥臂开关函数参考并配合环流抑制(CCSC)与最近电平控制(NLC)。针对各模型开发了专用的时域初始化策略，包括控制变量与状态变量的同步映射，确保切换瞬间无暂态冲击。

### 数学公式


**公式1**: $$$C_{AVM} = 4 C_{SM} / N_{SM}$$$

*桥臂AVM等效电容计算公式，基于能量守恒原则，将全桥臂子模块电容聚合为单一等效电容*


**公式2**: $$$i_{ref}^{DC} = \frac{\sum_{k=1}^{6} (e_{ref_k}^{AC} \cdot i_{arm_k}^{AC})}{\sum_{k=1}^{6} v_{CAVM_k}}$$$

*AVM辅助直流支路电流参考值计算，基于交直流侧瞬时功率平衡原理*


**公式3**: $$$R_{arm} = R_{ON} (N_{HB} + 2N_{FB})$$$

*桥臂等效导通电阻计算，考虑HB与FB子模块中IGBT的导通压降*


**公式4**: $$$r_{th}^{HB} = R_{ON} N_{HB} + \frac{n_{HB}^2 R_C}{N_{HB}}$$$

*HB部分戴维南等效电阻，包含IGBT导通电阻与电容离散化等效电阻*


**公式5**: $$$v_{th}^{HB} = n_{HB} \hat{v}_{HB}$$$

*HB部分戴维南等效电压，由投入子模块数与历史电压决定*


**公式6**: $$$r_{th}^{FB} = 2R_{ON} N_{FB} + \frac{n_{FB}^2 R_C}{N_{FB}}$$$

*FB部分戴维南等效电阻，FB结构包含4个开关管故系数为2*


**公式7**: $$$\hat{v}_{HB} = v_{HB} + \frac{n_{HB} i_{arm} R_C}{N_{HB}}$$$

*HB历史电压递推公式，用于梯形积分法下的电容电压状态更新*


**公式8**: $$$\hat{v}_{FB} = v_{FB} + \frac{n_{FB} i_{arm} R_C}{N_{FB}}$$$

*FB历史电压递推公式，原理同HB但参数独立*


### 算法步骤

1. 步骤1（阻塞模式判定）：从EMT求解器获取当前桥臂端电压$v_{arm}$。根据上一时刻的桥臂电流$i_{arm}$方向预设HB与FB子模块的开关状态，并重新计算当前$i_{arm}$。

2. 步骤2（方向一致性校验）：若计算出的$i_{arm}$方向与预设开关状态一致，则直接确定$n_{HB}$与$n_{FB}$，算法结束。

3. 步骤3（反向状态尝试）：若方向不一致，则按相反电流方向重新分配开关状态并再次计算$i_{arm}$。若新方向与开关状态匹配，则更新$n_{HB}$与$n_{FB}$，算法结束。

4. 步骤4（高阻态切换）：若两次尝试均无法匹配电流方向与开关状态，则判定为高阻抗阻塞状态，强制设置$n_{HB}=0$且$n_{FB}=0$。求解器需迭代求解直至收敛，最大迭代次数限制为30次。

5. 步骤5（伪电容平衡Pseudo-CBA执行）：若$n_{ref}<0$，仅投入FB模块($n_{HB}=0, n_{FB}=n_{ref}$)；若$n_{ref} \ge 0$，根据$i_{arm}$方向与$v_{HB}$、$v_{FB}$大小关系，按公式(17)-(20)动态分配$n_{HB}$与$n_{FB}$，并施加1个仿真步长的延迟以模拟真实CBA控制响应时间。


### 关键参数

- **电容离散化电阻**: $R_C = 0.5\Delta t / C_{SM}$

- **阻塞模式最大迭代次数**: 30次（实测收敛均<6次）

- **控制信号延迟**: 1个仿真时间步长（用于模拟真实CBA与受控源响应）

- **IGBT关断电阻**: $R_{OFF}$（用于高阻抗阻塞模式等效）

- **子模块配置**: 支持任意$N_{HB}$与$N_{FB}$比例混合



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 401电平MMC-HVDC系统自适应切换仿真 | 在401电平高压直流输电系统中验证AVM、AEM与DEM间的动态切换。外部交直流电压/电流跟踪误差<0.5%，模型切换瞬间电压与电流暂态冲击偏差<0.1%，实现完全平滑过渡。 | 相比全程使用详细等效模型(DEM)，在稳态运行与慢速机电暂态阶段切换至AVM/AEM后，单步计算耗时降低约65%~75%，整体仿真加速比达3.5倍以上，且满足实时仿真算力约束。 |



## 量化发现

- 在401电平MMC-HVDC系统中完成全工况验证，模型切换过程外部电气特性误差严格控制在<0.5%以内
- 切换瞬间电压/电流暂态冲击被完全抑制，瞬态偏差<0.1%，验证了时域初始化方法的有效性
- 桥臂等效模型阻塞模式求解器迭代上限设为30次，所有测试工况下实际收敛迭代次数均<6次，保证数值稳定性
- 伪电容平衡算法(Pseudo-CBA)与受控电压源指令均引入1个仿真步长($\Delta t$)的固定延迟，精确复现真实控制系统的响应滞后
- 非激活模型等效导纳严格置零，接口切换引起的数值振荡幅值<0.05 p.u.


## 关键公式

### 桥臂AVM等效电容公式

$$$C_{AVM} = 4 C_{SM} / N_{SM}$$$

*用于构建Arm-AVM-1/2模型，确保聚合电容在能量层面与全桥臂子模块电容等效*

### HB子模块戴维南等效电阻

$$$r_{th}^{HB} = R_{ON} N_{HB} + \frac{n_{HB}^2 R_C}{N_{HB}}$$$

*在AEM活跃模式下，用于计算半桥部分的等效内阻，结合梯形积分法实现电容动态离散化*

### Pseudo-CBA正向电流分配逻辑

$$$n_{HB} = \max(0, n_{ref} - N_{FB}), \quad n_{FB} = \min(n_{ref}, N_{FB})$$$

*当$i_{arm}>0$且$v_{HB}>v_{FB}$（或反向对应条件）时，用于动态分配HB与FB子模块的投入数量*



## 验证详情

- **验证方式**: 电磁暂态(EMT)时域仿真对比分析
- **测试系统**: 401电平MMC-HVDC系统（含耦合变压器、交直流电网及级联控制系统）
- **仿真工具**: 通用EMT求解器内核 + 自定义C++ DLL接口（支持运行时模型热切换与状态初始化）
- **验证结果**: 验证了自适应架构在任意HB/FB混合配置下的通用性。AVM/AEM/DEM切换过程电气接口完全一致，无拓扑突变引起的数值振荡。时域初始化策略成功消除控制变量与状态变量切换带来的暂态冲击。在保持外部特性高精度(<0.5%误差)的前提下，显著降低计算负担，为大规模电网实时仿真与多时间尺度研究提供有效工具。
