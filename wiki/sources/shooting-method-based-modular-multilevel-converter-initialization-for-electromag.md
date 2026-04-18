---
title: "Shooting method based modular multilevel converter initialization for electromagnetic transient analysis"
type: source
authors: ['D.', 'del', 'Giudice']
year: 2024
journal: "International Journal of Electrical Power and Energy Systems, 161 (2024) 110163. doi:10.1016/j.ijepes.2024.110163"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf"]
---

# Shooting method based modular multilevel converter initialization for electromagnetic transient analysis

**作者**: D., del, Giudice
**年份**: 2024
**来源**: `34/del Giudice 等 - 2024 - Shooting method based modular multilevel converter initialization for electromagnetic transient anal.pdf`

## 摘要

International Journal of Electrical Power and Energy Systems Shooting method based modular multilevel converter initialization for D. del Giudice a,∗, F. Bizzarri a,b, D. Linaro a, A. Brambilla a a Dipartimento di Elettronica, Informazione e Bioingegneria, Politecnico di Milano, p.za Leonardo da Vinci, 32, I20133, Milano, Italy b Advanced Research Center on Electronic Systems ‘‘E. De Castro’’ (ARCES), University of Bologna, Italy

## 核心贡献



- 提出了一种基于打靶法的模块化多电平换流器（MMC）初始化策略，用于电磁暂态仿真
- 该策略兼容不同详细程度的MMC模型及包含调制与电容电压平衡的控制算法，能显著减少初始化暂态及额外CPU时间

## 使用的方法


- [[numerical-integration]]
- [[network-equivalent]]
- [[state-space]]

## 涉及的模型


- [[mmc]]
- [[mmc-model]]
- [[average-value-model]]

## 相关主题


- [[mmc]]
- [[hvdc]]
- [[vsc-hvdc]]

## 主要发现



- 基于打靶法的初始化策略可使仿真直接从接近稳态的条件启动，有效抑制了初始化暂态过程
- 在含128电平MMC的NORDIC32系统测试中，该方法大幅缩短了达到稳态所需的仿真时间，提升了EMT计算效率

## 方法细节

### 方法概述

本文提出了一种基于打靶法(Shooting Method, SHM)的两阶段MMC初始化策略。第一阶段采用平均值模型(AVM)忽略开关细节和电容电压平衡动态，将稳态求解转化为非线性边值问题，通过牛顿迭代寻找使状态变量经过一个基波周期后回到初始值的状态向量，即稳定极限环上的不动点。第二阶段将AVM求得的稳态解（包括电容电压和电感电流）映射到Thévenin等效模型(TEM)，恢复详细模型（包含最近电平调制NLCM和基于交换的电容电压平衡算法CBA）后继续仿真。该方法直接作用于仿真器层级，无需手动推导MMC及控制方程，可灵活适应不同详细程度的模型和包含正负序dq控制、环流抑制(PR控制)的复杂控制系统。

### 数学公式


**公式1**: $$$$\mathbf{F}(\mathbf{x}_0) = \mathbf{\Phi}(\mathbf{x}_0, T) - \mathbf{x}_0 = \mathbf{0}$$$$

*打靶法核心边值条件，其中$\mathbf{\Phi}$为状态转移函数，$T$为基波周期，要求状态变量经过一个周期后回到初值*


**公式2**: $$$$\mathbf{J}(\mathbf{x}_k) \Delta\mathbf{x}_k = -\mathbf{F}(\mathbf{x}_k), \quad \mathbf{x}_{k+1} = \mathbf{x}_k + \Delta\mathbf{x}_k$$$$

*牛顿迭代求解格式，其中$\mathbf{J} = \frac{\partial\mathbf{F}}{\partial\mathbf{x}_0}$为灵敏度矩阵（雅可比矩阵）*


**公式3**: $$$$v_{ceq}(t) = v_c(t-\Delta t) + R_{ceq} \cdot i_c(t)$$$$

*Thévenin等效模型中子模块电容的伴随模型方程，$R_{ceq}$为等效电阻，$\Delta t$为仿真步长*


**公式4**: $$$$m_{u,l}^{a,b,c} = \frac{u_{a,b,c} \pm e_{a,b,c}}{v_{dc}/2}$$$$

*上下桥臂调制指数计算，其中$u$为内环电流控制输出电压，$e$为环流抑制控制输出，$v_{dc}$为直流侧电压*


### 算法步骤

1. 构建MMC的平均值模型(AVM)，将子模块串等效为受控电压源，忽略最近电平调制(NLCM)和电容电压平衡算法(CBA)的开关细节

2. 设定打靶周期$T$（通常为基波周期，如50Hz系统取20ms）

3. 猜测初始状态向量$\mathbf{x}_0$（包括桥臂电流、电容电压平均值等）

4. 在区间$[0,T]$内对AVM模型进行数值积分，得到周期末状态$\mathbf{x}(T) = \mathbf{\Phi}(\mathbf{x}_0, T)$

5. 计算残差向量$\mathbf{F}(\mathbf{x}_0) = \mathbf{x}(T) - \mathbf{x}_0$，判断$\|\mathbf{F}\| < \epsilon$是否满足

6. 若未收敛，通过数值差分或伴随灵敏度分析计算雅可比矩阵$\mathbf{J} = \frac{\partial\mathbf{F}}{\partial\mathbf{x}_0}$

7. 执行牛顿迭代修正：$\mathbf{x}_{new} = \mathbf{x}_0 - \mathbf{J}^{-1}\mathbf{F}(\mathbf{x}_0)$，返回步骤4

8. 收敛后获得AVM稳态解，将电容电压平均值和桥臂电流映射到Thévenin等效模型(TEM)的相应变量

9. 对TEM模型中的$N$个子模块电容进行初始化，设置$v_c$为AVM求得的平均值

10. 从映射后的状态启动详细EMT仿真，此时模型包含NLCM调制和Swap-based CBA算法，仿真从接近稳态开始


### 关键参数

- **N**: 128（MMC每桥臂子模块数/电平数）

- **T**: 基波周期（如20ms对应50Hz系统）

- **R_S, L_S**: 桥臂电阻和电感（限流电抗器参数）

- **R_T, L_T**: 交流侧滤波器电阻和电感

- **R_{on}, R_{off}**: IGBT/Diode等效电阻，闭合时~mΩ，断开时~MΩ

- **N_{swap}**: 每次电平切换时交换的子模块对数（电容电压平衡算法参数）

- **epsilon**: 牛顿迭代收敛容差（如$10^{-6}$或机器精度）

- **v_{dc}**: 直流侧额定电压



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| NORDIC32标准测试系统含128电平MMC-HVDC链路 | 在修改后的NORDIC32系统中，两个换流站均采用128电平MMC，分别运行于P/Q控制和DC-SLACK/Q控制模式。使用打靶法初始化后，电容电压平衡算法(CBA)和最近电平调制(NLCM)在仿真启动时刻即工作在稳态附近，桥臂电流包含正确的直流分量、基频分量和二次谐波分量（环流抑制控制产生） | 相比从零初始状态启动或使用启动电阻序列的方法，消除了长达数秒甚至数十秒的初始化暂态过程，避免了因错误初始条件导致的数值不稳定或仿真失败 |



## 量化发现

- MMC电平数：128级（每桥臂含128个子模块）
- 子模块电容等效电阻范围：开关闭合时~mΩ级，断开时~MΩ级
- 环流抑制控制针对的谐波频率：2倍基频（正负零序二次谐波）
- 电容电压平衡算法(Swap-based CBA)每次电平切换交换的子模块对数：$N_{swap}$对
- 打靶法收敛精度：牛顿迭代达到机器精度或$\|\Delta\mathbf{x}\| < 10^{-6}$量级
- 计算复杂度：相比详细模型打靶，AVM模型将状态变量数从$O(N)$降至$O(1)$，显著降低雅可比矩阵维度和计算量


## 关键公式

### 打靶法周期稳态条件

$$$$\mathbf{\Phi}(\mathbf{x}_0, T) - \mathbf{x}_0 = \mathbf{0}$$$$

*用于确定AVM模型的稳态初始条件，要求状态变量经过周期$T$后精确回到初始值*

### 二次环流产生机制

$$$$i_{diff}^{(2)} = i_{arm}^{(2)} \propto v_{dc} - (v_{cu} + v_{cl})$$$$

*说明子模块串电压不等（$v_{cu} \neq v_{cl}$）导致二次谐波环流，用于验证初始化后环流抑制控制的有效性*



## 验证详情

- **验证方式**: 电磁暂态(EMT)数值仿真验证，对比从零启动与打靶法初始化的暂态过程
- **测试系统**: NORDIC32标准电力系统，修改后加入基于128电平MMC的HVDC直流链路，包含完整的外环功率控制、内环电流控制、正负序分离控制、二次谐波环流抑制(PR控制)、最近电平调制(NLCM)和基于交换的电容电压平衡算法(CBA)
- **仿真工具**: 自主开发的专有EMT仿真器（proprietary simulator），具备完整访问权限以实现打靶法与牛顿迭代的深度集成
- **验证结果**: 提出的初始化策略允许EMT仿真直接从接近稳态的条件启动，显著限制了初始化暂态及其对应的额外CPU时间，兼容详细模型（TEM）和平均值模型(AVM)，适用于含复杂控制策略（包括调制和电容电压平衡）的MMC系统
