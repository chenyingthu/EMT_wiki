---
title: "A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation"
type: source
year: 2024
journal: "IEEE Open Access Journal of Power and Energy;2024;11; ;10.1109/OAJPE.2024.3444272"
created: "2026-04-13"
sources: ["EMT_Doc/03/Xiong 等 - 2024 - A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation.pdf"]
---

# A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation

**年份**: 2024
**来源**: `03/Xiong 等 - 2024 - A Semi-Analytical Approach for State-Space Electromagnetic Transient Simulation.pdf`

## 摘要

This paper proposes a semi-analytical approach for efficient and accurate electromagnetic transient (EMT) simulation of a power grid. The approach first derives a high-order semi-analytical solution (SAS) of the grid’s state-space EMT model using the differential transformation (DT), and then evaluates the solution over enlarged, variable time steps to significantly accelerate the simulations while maintaining its high accuracy on detailed fast EMT dynamics. The approach also addresses switches during large time steps by using a limit violation detection algorithm with a binary search-enhanced quadratic interpolation. Case studies are conducted on EMT models of the IEEE 39-bus system and large-scale systems to demonstrate the merits of the new simulation approach against traditional numeri

## 核心贡献


- 基于微分变换推导状态空间EMT模型高阶半解析解，实现灵活选择求解阶数与步长
- 提出基于截断误差估计的多阶段变步长策略，在保持精度的同时显著提升计算效率
- 设计二分搜索增强二次插值的越限检测算法，精准定位大步长下的开关切换时刻


## 使用的方法


- [[半解析解法|半解析解法]]
- [[微分变换法|微分变换法]]
- [[状态空间法|状态空间法]]
- [[变步长仿真|变步长仿真]]
- [[密集输出机制|密集输出机制]]
- [[二分搜索增强二次插值|二分搜索增强二次插值]]


## 涉及的模型


- [[r-l-c电路|R-L-C电路]]
- [[vbr同步发电机模型|VBR同步发电机模型]]
- [[发电机控制器|发电机控制器]]
- [[逆变器型资源-ibr-模型|逆变器型资源(IBR)模型]]
- [[ieee-39节点系统|IEEE 39节点系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[状态空间建模|状态空间建模]]
- [[变步长算法|变步长算法]]
- [[开关事件处理|开关事件处理]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 在IEEE 39节点及大规模系统测试中，该方法相比传统数值法显著加速且保持高精度
- 变步长策略结合密集输出机制，可在扩大步长时准确重构内部高频动态细节
- 改进的越限检测算法能精准捕捉大步长下的开关切换时刻，有效避免仿真误差累积



## 方法细节

### 方法概述

本文提出一种基于微分变换（DT）的半解析解（SAS）电磁暂态（EMT）仿真方法。首先将电网状态空间模型转化为高阶时间幂级数形式的SAS，通过递归计算各阶系数实现灵活选择求解阶数。在此基础上，引入基于截断误差估计的多阶段变步长策略，动态调整仿真步长以平衡计算效率与精度。针对大步长下可能遗漏的快速暂态细节，利用SAS的密集输出机制在步长内任意时刻重构高分辨率波形。此外，设计了一种结合二分搜索与二次插值的越限检测算法，通过SAS多项式快速定位开关切换时刻，并在检测到越限时截断当前步长、更新初值后重新计算，从而彻底解决传统线性插值在大步长下定位不准的问题。

### 数学公式


**公式1**: $$$x(t) = \sum_{k=0}^{\infty} x[k]t^k \approx \sum_{k=0}^{N} x[k]t^k, \quad t < T_x$$$

*N阶半解析解（SAS）的时间幂级数近似表达式，$x[k]$为微分变换系数，$T_x$为收敛域。*


**公式2**: $$$g[k] = \frac{1}{k!} \left[ \frac{d^k g(t)}{dt^k} \right]_{t=t_0}$$$

*函数$g(t)$在$t_0$处的$k$阶微分变换（DT）定义式。*


**公式3**: $$$(k+1)g[k+1] = f[k] = \sum_{m=0}^{k} g[m]h[k-m]$$$

*微分方程$\dot{g}(t)=g(t)h(t)$对应的DT递归计算规则，用于高效推导SAS系数。*


**公式4**: $$$E(\Delta t) = \| A x[N] + B u[N] \|_\infty (\Delta t)^N$$$

*基于状态空间模型最高阶项的截断误差估计公式，用于动态确定最大允许步长。*


**公式5**: $$$x(t_0 + t_n) \approx \sum_{k=0}^{N} x[k] t_n^k \quad (t_n < \Delta t)$$$

*密集输出机制公式，利用已求得的SAS系数在步长内任意内部时刻$t_n$重构状态变量。*


### 算法步骤

1. 初始化：设定$t=t_0$时刻的状态向量初值$x_1[0], x_2[0], x_3[0]$，预设SAS阶数$N$与初始步长$\Delta t$。

2. 递归求导：令$k=0$至$N$，依次利用DT变换规则（表1及命题1）计算发电机、控制器、网络R-L-C支路及IBR模型的各阶SAS系数$x_1[k], x_2[k], x_3[k]$。

3. 误差评估与步长调整：代入最高阶系数计算截断误差$E(\Delta t)$。若$E(\Delta t) > \varepsilon_E$（通常取$10^{-2}$ p.u.），则按公式反推缩小$\Delta t$并重新计算系数；若满足阈值，则接受当前步长。

4. 状态更新与密集输出：利用SAS多项式计算$t_0+\Delta t$时刻的状态值作为下一阶段的初值。若需高分辨率波形，按密集输出公式在步长内插入多个计算点。

5. 越限检测与开关处理：在步长内利用二分搜索快速缩小区间$[a,b]$（满足$b-a < \varepsilon_t$，如10-20 $\mu s$）。在区间内取中点$c$，结合$x(a), x(b), x(c)$与限值$x_{limit}$进行二次插值，精确求解越限时刻$t_{limit}$。若检测到越限，则在$t_{limit}$处截断步长，更新状态初值，并立即调整步长重新执行SAS计算。


### 关键参数

- **SAS阶数_N**: 可灵活配置，通常根据系统非线性程度与收敛性动态选择

- **截断误差阈值_εE**: 1 × 10⁻² p.u.（用于控制变步长策略的精度边界）

- **二分搜索时间容差_εt**: 10~20 μs（用于快速定位开关事件的时间区间）

- **初始步长_Δt**: 微秒级至毫秒级自适应变化，稳态时显著放大



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统（含同步机） | 在包含详细VBR同步发电机模型、励磁/调速器控制器的EMT模型中，SAS方法成功捕捉了转子角、机端电压及电流的快速暂态过程。在系统趋于稳态时，步长自动放大，仿真耗时显著降低，且关键状态变量轨迹与传统数值积分法高度吻合。 | 相比固定步长传统数值法，在保持误差<0.5%的前提下，计算效率提升显著（具体加速比取决于系统稳态占比，原文指出可大幅减少计算步数）。 |

| IEEE 39节点系统（含逆变器型资源IBR） | 针对含跟网型IBR的修改版39节点系统，SAS方法准确复现了PLL动态、内外环控制及PWM等效接口的电磁暂态响应。密集输出机制有效还原了高频开关动作引起的电压/电流毛刺。 | 在IBR高频动态仿真中，变步长策略避免了传统方法为捕捉细节而强制使用极小步长的瓶颈，仿真速度提升的同时，越限检测定位误差控制在微秒级。 |

| 大规模合成电网系统 | 在扩展至数百节点的大规模系统中验证了算法的可扩展性。状态空间分组（$x_1, x_2, x_3$）与DT递归计算有效降低了矩阵运算维度，内存占用与单步计算时间均保持线性增长趋势。 | 相较于传统梯形法或节点导纳矩阵法，SAS方法在大规模网络中展现出更优的数值稳定性与步长自适应能力，整体仿真加速效果随系统规模扩大而更加明显。 |



## 量化发现

- 截断误差控制阈值设定为 $\varepsilon_E = 1 \times 10^{-2}$ p.u.，确保状态变量近似误差始终处于工程可接受范围。
- 开关事件定位时间区间容差 $\varepsilon_t$ 可压缩至 10~20 $\mu s$，结合二次插值后，越限时刻定位精度达微秒级，远优于大步长下的线性插值。
- 变步长策略使仿真步长在系统平稳期可动态放大至数十微秒甚至毫秒级，相比传统固定微秒级步长，总计算步数呈数量级下降。
- 密集输出机制无需重新求解微分方程，仅需多项式求值即可在单个大步长内生成任意高分辨率波形，计算开销可忽略不计。
- DT递归算法将非线性项（如Park变换、乘积项）转化为代数卷积运算，避免了传统数值法中的雅可比矩阵迭代，单步计算复杂度显著降低。


## 关键公式

### 变步长截断误差控制方程

$$$E(\Delta t) = \| A x[N] + B u[N] \|_\infty (\Delta t)^N \le \varepsilon_E$$$

*用于在每一步仿真结束时评估当前步长$\Delta t$下的近似误差，若超限则自动缩小步长，是变步长策略的核心判据。*

### 状态空间DT递归公式

$$$(k+1)x[k+1] = A x[k] + B u[k]$$$

*将连续状态空间方程$\dot{x}=Ax+Bu$转化为离散系数递推关系，是高效生成SAS系数的基础。*

### SAS密集输出重构公式

$$$x(t_0 + t_n) \approx \sum_{k=0}^{N} x[k] t_n^k$$$

*在已求得SAS系数的前提下，用于在任意内部时刻$t_n$快速计算状态值，支撑高分辨率波形输出与越限检测。*

### 二分搜索增强二次插值越限定位公式

$$$t_{limit} = \text{QuadraticInterp}(a, b, c, x(a), x(b), x(c), x_{limit})$$$

*当二分搜索将越限区间缩小至$\varepsilon_t$后，利用三点二次多项式拟合精确求解状态变量穿越限值$x_{limit}$的准确时刻$t_{limit}$。*



## 验证详情

- **验证方式**: 数值仿真对比验证（自研SAS算法 vs 传统数值积分法/商业软件逻辑）
- **测试系统**: IEEE 39节点系统（标准同步机版与含IBR修改版）、大规模合成电网系统
- **仿真工具**: 自研状态空间SAS求解器（对比基准为传统梯形法/节点法及PSCAD/EMTDC的线性插值逻辑）
- **验证结果**: 在IEEE 39节点及大规模系统测试中，SAS方法在保持电磁暂态高频细节精度（误差<1%）的同时，通过变步长策略显著减少了总仿真步数。密集输出与改进的越限检测算法有效克服了大步长下的信息丢失与开关定位偏差问题，验证了该方法在兼顾计算效率与数值精度方面的优越性。
