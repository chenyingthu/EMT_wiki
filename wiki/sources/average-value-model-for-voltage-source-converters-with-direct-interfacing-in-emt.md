---
title: "Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Transactions on Energy Conversion;2023;38;3;10.1109/TEC.2022.3220085"
tags: ['average-value', 'emtp']
created: "2026-04-13"
sources: ["EMT_Doc/09/Ebrahimi和Jatskevich - 2023 - Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution.pdf"]
---

# Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution

**作者**: 
**年份**: 2023
**来源**: `09/Ebrahimi和Jatskevich - 2023 - Average-Value Model for Voltage-Source Converters With Direct Interfacing in EMTP-Type Solution.pdf`

## 摘要

—Average-value models (AVMs) of high-frequency switching voltage-source converters (VSCs) are indispensable for fast/efﬁcient simulation of VSC-based power systems. However, in EMT/EMTP-type programs large simulation time-steps cannot be utilized with conventional non-iterative interfacings of AVMs due to numerical inaccuracy/instability as a result of a one-time-step interfacing delay. In this letter, a directly-interfaced AVM has been developed for the VSCs which eliminates the interfacing delay and allows large time-steps. This is achieved by formulating the AVM in the nodal form that is solved simultaneously with the overall network nodal equations. The new proposed model is demonstrated to outperform the existing AVMs of VSCs in terms of accuracy at fairly large time steps. Index Term

## 核心贡献


- 提出VSC平均值模型直接接口方法，消除传统间接接口的一步延迟
- 将AVM重构为节点导纳形式，与外部网络节点方程联立同步求解
- 突破大仿真步长下的数值不稳定瓶颈，显著提升系统级仿真效率


## 使用的方法


- [[平均值建模|平均值建模]]
- [[直接接口技术|直接接口技术]]
- [[节点分析法|节点分析法]]
- [[dq坐标变换|dq坐标变换]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[交直流系统|交直流系统]]
- [[戴维南等效电路|戴维南等效电路]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[大时间步长仿真|大时间步长仿真]]
- [[vsc-model|VSC]]
- [[数值稳定性|数值稳定性]]


## 主要发现


- 消除接口延迟后，仿真步长可显著增大且保持数值稳定与高精度
- 在大时间步长下，新模型精度优于传统间接接口平均值模型
- 节点联立求解有效避免了传统方法因单步延迟引发的数值发散问题



## 方法细节

### 方法概述

针对传统VSC平均值模型（AVM）在EMTP类程序中采用受控源间接接口导致的一步时间步延迟问题，本文提出一种直接接口平均值模型（DI-AVM）。该方法首先利用Park变换将交流变量转换至旋转qd坐标系，建立交直流平均变量间的解析关系，并引入阻尼电阻构建直流侧接口。随后，将模型方程重构为阻抗矩阵与历史电压项形式，通过坐标反变换得到abc坐标系下的等效阻抗矩阵。对该矩阵求逆获得节点导纳矩阵，并结合历史电压项计算等效历史电流源。最终，将导纳矩阵与历史电流源直接嵌入外部网络的节点导纳方程中，实现VSC模型与全网方程的同步联立求解，彻底消除接口延迟，从而在大幅增大仿真步长的同时保证数值稳定性与精度。

### 数学公式


**公式1**: $$$\bar{v}_{qd} = \frac{1}{2} M \begin{bmatrix} \cos(\delta) \\ \sin(\delta) \end{bmatrix} \bar{v}_{dc}$$$

*交流侧qd轴平均电压与直流侧平均电压的调制关系，由调制比M和功角δ决定*


**公式2**: $$$\bar{i}_{dc} = \frac{3}{4} M \cos(\phi) \|\bar{i}_{qd}\|$$$

*直流侧平均电流与交流侧qd轴电流幅值及功率因数角φ的关系*


**公式3**: $$$\begin{bmatrix} \bar{v}_{qd} \\ \bar{v}_{dc} \end{bmatrix} = Z_{VSC}^{qd,dc} \begin{bmatrix} \bar{i}_{qd} \\ \bar{i}_{dc} \end{bmatrix} + e_{h,VSC}^{qd,dc}$$$

*qd坐标系下VSC的阻抗-历史项电压方程，是推导节点形式的核心*


**公式4**: $$$G_{VSC}^{abc,dc} \begin{bmatrix} v_{abc}^1 \\ \bar{v}_{dc} \end{bmatrix} = \begin{bmatrix} i_{abc}^1 \\ \bar{i}_{dc} \end{bmatrix} + i_{h,VSC}^{abc,dc}$$$

*最终导出的abc坐标系节点导纳方程形式，用于与外部网络联立求解*


### 算法步骤

1. 1. 坐标变换与变量初始化：利用Park变换矩阵将三相交流电压/电流转换至同步旋转qd坐标系，提取基波分量对应的平均变量。

2. 2. 建立交直流耦合关系：根据调制比M、功角δ和功率因数角φ，推导交流侧平均电压/电流与直流侧平均电压/电流的解析表达式。

3. 3. 引入直流侧接口与阻尼：在直流侧并联阻尼电阻Rx，并定义补偿电流源icomp(t)=v̄dc(t-Δt)/Rx，用于提供数值阻尼并稳定直流电压求解。

4. 4. 推导qd域阻抗矩阵与历史项：将电压-电流关系整理为矩阵形式，提取出仅依赖于当前步电流的阻抗矩阵Z_VSC^{qd,dc}，以及仅依赖于上一时刻直流电压的历史电压项e_{h,VSC}^{qd,dc}。

5. 5. 坐标反变换至abc域：利用逆Park变换将阻抗矩阵和历史电压项转换回三相abc坐标系，得到Z_VSC^{abc,dc}和e_{h,VSC}^{abc,dc}。

6. 6. 矩阵求逆获取导纳阵：对abc域阻抗矩阵求逆，计算得到节点导纳矩阵G_VSC^{abc,dc} = (Z_VSC^{abc,dc})^{-1}。

7. 7. 计算等效历史电流源：将导纳矩阵与历史电压项相乘，得到等效历史电流源i_{h,VSC}^{abc,dc} = G_VSC^{abc,dc} e_{h,VSC}^{abc,dc}。

8. 8. 组装全网节点方程：将VSC的导纳子矩阵和等效历史电流源直接叠加至EMTP程序的全局节点导纳矩阵和注入电流向量中。

9. 9. 同步联立求解：在每个仿真步长内，直接求解包含VSC节点的全局线性方程组，无需迭代或引入人工时间步延迟。


### 关键参数

- **阻尼电阻_Rx**: 10 Ω（用于IDI-AVM对比测试）

- **开关频率**: 1620 Hz

- **调制策略**: 正弦脉宽调制（SPWM）

- **交流侧额定参数**: 线电压有效值100 kV，频率60 Hz，电阻1.5 Ω，电感37.14 mH

- **直流侧额定参数**: 电压200 kV，电阻5.99 Ω，电感84 mH，电容74.25 μF

- **初始运行点**: δ = -25°，M = 0.5，整流模式传输200 MW

- **阶跃扰动**: t=50 ms时，δ跳变至25°，M跳变至0.7，逆变模式传输240 MW



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 小步长基准测试（Δt = 10 μs） | 在10 μs步长下，DI-AVM与IDI-AVM的暂态响应（相电压、相电流、直流电压、直流电流）均与0.1 μs参考解高度吻合，准确捕捉了t=50 ms时的功率反转动态。 | 两者精度一致，误差可忽略，验证了DI-AVM在小步长下的等效性。 |

| 中大步长稳定性测试（Δt = 400 μs） | IDI-AVM在此步长下出现数值发散或严重失真；DI-AVM保持稳定，波形平滑且与参考解趋势一致。 | DI-AVM在400 μs步长下仍稳定运行，而传统IDI-AVM已失效。 |

| 极大步长精度测试（Δt = 1000 μs） | DI-AVM在1000 μs步长下依然保持数值稳定，暂态超调与稳态值与0.1 μs参考解偏差极小；IDI-AVM若不加阻尼电阻则直接发散，加入Rx=10 Ω阻尼后虽稳定但产生显著稳态误差。 | DI-AVM在1000 μs步长下的精度显著优于带阻尼的IDI-AVM，且无需牺牲稳态精度换取稳定性。 |



## 量化发现

- DI-AVM允许的最大可用仿真步长可达1000 μs，相比传统IDI-AVM的极限步长（约100 μs）提升约10倍。
- 在Δt = 1000 μs时，DI-AVM的交流电流2-范数误差保持在极低水平，而IDI-AVM（无阻尼）误差呈指数级增长导致发散，IDI-AVM（带阻尼）稳态误差显著增大。
- DI-AVM彻底消除了传统方法中因受控源接口引入的1个时间步（Δt）人工延迟，使节点方程求解实现真正的同步。
- 相较于详细开关模型（需Δt < 10 μs且依赖插值算法），DI-AVM作为连续模型无需开关时刻插值，计算效率提升两个数量级以上。


## 关键公式

### VSC直接接口节点导纳方程

$$$G_{VSC}^{abc,dc} \begin{bmatrix} v_{abc}^1 \\ \bar{v}_{dc} \end{bmatrix} = \begin{bmatrix} i_{abc}^1 \\ \bar{i}_{dc} \end{bmatrix} + i_{h,VSC}^{abc,dc}$$$

*用于将VSC模型直接嵌入EMTP全网节点矩阵，实现无延迟同步求解*

### qd坐标系VSC阻抗矩阵

$$$Z_{VSC}^{qd,dc} = \begin{bmatrix} \frac{3}{8}M^2 R_x \cos^2(\delta) & \frac{3}{16}M^2 R_x \sin(2\delta) & -\frac{1}{2}M R_x \cos(\delta) \\ \frac{3}{16}M^2 R_x \sin(2\delta) & \frac{3}{8}M^2 R_x \sin^2(\delta) & -\frac{1}{2}M R_x \sin(\delta) \\ \frac{3}{4}M R_x \cos(\delta) & \frac{3}{4}M R_x \sin(\delta) & -R_x \end{bmatrix}$$$

*描述VSC交直流端口在旋转坐标系下的动态阻抗特性，是推导导纳矩阵的基础*

### abc坐标系历史电压项

$$$e_{h,VSC}^{abc,dc} = \begin{bmatrix} e_h^{abc} \\ e_h^{dc} \end{bmatrix}, \quad e_h^{abc} = \frac{1}{2} M \begin{bmatrix} \cos(\theta_s - \delta) \\ \cos(\theta_s - \delta - 2\pi/3) \\ \cos(\theta_s - \delta + 2\pi/3) \end{bmatrix} \bar{v}_{dc}(t-\Delta t)$$$

*携带上一时刻直流电压信息，用于构建等效历史电流源，体现系统记忆效应*



## 验证详情

- **验证方式**: 离线电磁暂态仿真对比验证（与详细开关模型及传统间接接口AVM进行多维度对比）
- **测试系统**: 典型VSC交直流互联系统（代表HVDC Light整流/逆变侧），包含交流戴维南等效源、VSC两电平拓扑、直流线路及负载
- **仿真工具**: EMTP类程序架构（基于节点分析法实现，兼容PSCAD/EMTDC等求解器逻辑）
- **验证结果**: 验证表明DI-AVM在Δt=10 μs时与参考解完全一致；在Δt=400~1000 μs大时间步长下，DI-AVM保持数值稳定且暂态/稳态精度极高，而传统IDI-AVM出现发散或需引入阻尼电阻导致精度严重下降。DI-AVM成功突破大时间步长仿真瓶颈，适用于大规模VSC系统的高效离线与实时仿真。
