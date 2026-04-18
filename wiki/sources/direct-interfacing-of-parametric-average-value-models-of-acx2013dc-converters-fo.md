---
title: "Direct Interfacing of Parametric Average-Value Models of AC&#x2013;DC Converters for Nodal Analysis-Based Solution"
type: source
authors: ['未知']
year: 2022
journal: "IEEE Transactions on Energy Conversion;2022;37;4;10.1109/TEC.2022.3177131"
tags: ['average-value']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/Direct_Interfacing_of_Parametric_Average-Value_Models_of_ACDC_Converters_for_Nodal_Analysis-Based_Solution.pdf"]
---

# Direct Interfacing of Parametric Average-Value Models of AC&#x2013;DC Converters for Nodal Analysis-Based Solution

**作者**: 
**年份**: 2022
**来源**: `13&14/files/Direct_Interfacing_of_Parametric_Average-Value_Models_of_ACDC_Converters_for_Nodal_Analysis-Based_Solution.pdf`

## 摘要

—AC–DC converters are widely used in many power- electronic-based systems. There is an increasing need to simulate such systems using larger time-steps in ofﬂine and/or real-time elec- tromagnetic transient (EMT or EMTP) simulators. The so-called parametric average-value models (PAVMs) have been developed to allow larger time-steps and provide fast simulations. However, the application of PAVMs in nodal-analysis-based EMTP programs typically requires a one-time-step delay between the interfacing sources and the network solution (i.e., indirect interfacing), causing inaccuracy and numerical instability at medium-to-large time- steps. This paper presents a direct interfacing method for PAVMs of line-commutated rectiﬁers (LCRs). The proposed method lin- earizes the PAVM interfacing equations 

## 核心贡献


- 提出PAVM直接接口方法，线性化接口方程并嵌入节点矩阵，消除传统一步延迟
- 实现模型与外部网络非迭代同步求解，突破EMTP仿真大步长下的数值稳定性瓶颈
- 适用于各类线换相整流器，支持千微秒级仿真步长且保持系统级动态高精度


## 使用的方法


- [[节点分析法|节点分析法]]
- [[参数化平均值建模|参数化平均值建模]]
- [[直接接口技术|直接接口技术]]
- [[方程线性化|方程线性化]]
- [[离散化|离散化]]


## 涉及的模型


- [[线换相整流器|线换相整流器]]
- [[ac-dc变换器|AC-DC变换器]]
- [[戴维南等效网络|戴维南等效网络]]
- [[直流滤波器|直流滤波器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[实时仿真|实时仿真]]
- [[大步长仿真|大步长仿真]]
- [[节点分析|节点分析]]
- [[平均值建模|平均值建模]]
- [[数值稳定性|数值稳定性]]


## 主要发现


- 仿真验证表明，直接接口法在1000至2000微秒大步长下仍保持高精度与数值稳定性
- 消除一步延迟后，PAVM在EMTP型求解器中可实现与外部网络的同步非迭代计算
- 相比传统间接接口，新方法有效避免了中等至大步长下的精度下降与数值振荡问题



## 方法细节

### 方法概述

本文提出一种针对线换相整流器（LCR）参数化平均值模型（PAVM）的直接接口方法，旨在解决传统EMTP节点分析中因间接接口引入的一步时间延迟所导致的数值不稳定与精度下降问题。该方法首先将PAVM的非线性接口方程在上一时刻工作点处进行一阶泰勒展开线性化，推导出包含交流/直流端口的等效阻抗子矩阵与历史电流项。随后，通过Park反变换将dq坐标系下的线性化模型映射至abc三相静止坐标系，并将其直接组装至全网节点导纳矩阵中。最终，PAVM与外部交直流网络在同一时间步内实现非迭代同步求解，彻底消除接口延迟，使仿真步长可大幅提升至千微秒级而不牺牲数值稳定性与动态精度。

### 数学公式


**公式1**: $$$V = G^{-1} \cdot I$$$

*EMTP节点分析基本方程，V为节点电压向量，I为注入电流向量，G为系统节点导纳矩阵*


**公式2**: $$$V_{LCR} = Z_{LCR} I_{LCR} + e_{h,LCR}$$$

*LCR离散化后的标准节点方程形式，用于直接嵌入全网矩阵*


**公式3**: $$$f(x, y) \approx f(x_0, y_0) + \frac{\partial f}{\partial x}(x-x_0) + \frac{\partial f}{\partial y}(y-y_0)$$$

*一阶泰勒线性化公式，用于将非线性电压-电流关系在$(t-\Delta t)$点展开*


**公式4**: $$$\begin{bmatrix} \bar{v}_q^s \\ \bar{v}_d^s \\ \bar{v}_{dc} \end{bmatrix} = \begin{bmatrix} Z_{qq} & Z_{qd} & Z_{qdc} \\ Z_{dq} & Z_{dd} & Z_{ddc} \\ -Z_{dcq} & -Z_{dcd} & -Z_{dcdc} \end{bmatrix} \begin{bmatrix} \bar{i}_q^s \\ \bar{i}_d^s \\ \bar{i}_{dc} \end{bmatrix} + \begin{bmatrix} e_{h,q} \\ e_{h,d} \\ e_{h,dc} \end{bmatrix}$$$

*线性化后的dq坐标系电压-电流关系，包含阻抗子矩阵与历史项*


**公式5**: $$$\begin{bmatrix} Z_{aa} & Z_{ab} & Z_{ac} \\ Z_{ba} & Z_{bb} & Z_{bc} \\ Z_{ca} & Z_{cb} & Z_{cc} \end{bmatrix} = [K(\theta_s)]^{-1} \begin{bmatrix} Z_{qq} & Z_{qd} \\ Z_{dq} & Z_{dd} \end{bmatrix} [K(\theta_s)]$$$

*通过Park反变换矩阵将dq轴阻抗子矩阵转换至abc三相坐标系*


### 算法步骤

1. 步骤1：初始化与参数获取。读取上一时刻($t-\Delta t$)的交直流电流、直流电压及触发角，计算动态阻抗$z_d$，通过预存查找表获取参数化函数$w_i(\cdot)$、$w_v(\cdot)$及功率因数角$\phi(\cdot)$。

2. 步骤2：计算补偿电流与线性化系数。根据上一时刻直流电压计算补偿电流$i_{comp}$，并基于式(31)计算线性化所需的中间系数$A, B, C, D, E, F, G$，这些系数依赖于上一时刻的电流幅值与参数化函数值。

3. 步骤3：构建dq坐标系阻抗矩阵与历史项。利用式(29)计算各偏导数得到阻抗子矩阵元素$Z_{qq}, Z_{qd}, Z_{qdc}, \dots$，利用式(30)计算历史电压项$e_{h,q}, e_{h,d}, e_{h,dc}$，完成非线性方程的线性化离散。

4. 步骤4：坐标系变换与矩阵组装。通过Park反变换矩阵$[K(\theta_s)]^{-1}$将dq坐标系下的阻抗子矩阵与历史项转换至abc三相静止坐标系（式36、37），形成完整的$Z_{LCR}$与$e_{h,LCR}$向量。

5. 步骤5：嵌入全网节点方程并求解。将$Z_{LCR}$的等效导纳及历史电流项直接叠加至EMTP全网节点导纳矩阵$G$与注入电流向量$I$中，执行LU分解与前代回代求解当前时刻全网电压/电流，全程无需迭代或引入时间步延迟。


### 关键参数

- **R_x**: 缓冲/等效串联电阻，用于消除稳态误差并参与补偿电流计算

- **w_i(·), w_v(·)**: 电流/电压参数化函数，通过离线数值仿真预计算并存于多维查找表

- **φ(·)**: 功率因数角参数化函数，表征LCR交流侧电压与电流的相位关系

- **z_d**: 动态阻抗，定义为$\bar{v}_{dc}/|\bar{i}_{qd}^e|$，用于表征LCR实时负载工况

- **Δt**: 仿真时间步长，所提方法支持1000~2000 µs量级的大步长

- **θ_s**: 等效三相交流电源电压基波相位角，用于同步参考系变换



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 通用三相AC-DC系统（含6脉冲晶闸管LCR） | 在1000~2000 µs仿真步长下，所提直接接口法保持高精度波形跟踪与数值稳定性，传统间接接口在此步长下出现严重数值振荡或发散 | 消除1个时间步延迟，实现非迭代同步求解，在千微秒级步长下计算效率与稳定性显著优于传统间接接口方法 |



## 量化发现

- 仿真步长可安全提升至1000~2000 µs量级，突破传统间接接口因一步延迟导致的步长限制
- 彻底消除接口处的1个时间步延迟（Δt），实现模型与外部网络的严格同步求解
- 采用非迭代求解架构，单次时间步计算复杂度与标准EMTP节点法一致，无额外迭代开销
- 参数化函数通过离线查表获取，在线仅需矩阵运算与偏导数更新，计算负担极低


## 关键公式

### LCR直接接口节点方程

$$$V_{LCR} = Z_{LCR} I_{LCR} + e_{h,LCR}$$$

*用于将PAVM离散化模型直接嵌入EMTP全网节点导纳矩阵，实现无延迟同步求解*

### 线性化dq轴电压-电流关系

$$$\begin{bmatrix} \bar{v}_q^s \\ \bar{v}_d^s \\ \bar{v}_{dc} \end{bmatrix} = \mathbf{Z}_{qd,dc} \begin{bmatrix} \bar{i}_q^s \\ \bar{i}_d^s \\ \bar{i}_{dc} \end{bmatrix} + \mathbf{e}_{h}$$$

*在上一时刻工作点处对非线性PAVM接口方程进行一阶泰勒展开后得到的标准线性形式*

### 坐标系变换阻抗矩阵

$$$\mathbf{Z}_{abc} = [K(\theta_s)]^{-1} \mathbf{Z}_{qd} [K(\theta_s)]$$$

*将同步旋转坐标系下的线性化阻抗子矩阵映射至三相静止坐标系，以便与外部交流网络直接拼接*



## 验证详情

- **验证方式**: 离线电磁暂态仿真对比分析（基于节点分析法架构）
- **测试系统**: 含任意交流电网（戴维南等效）与直流低通滤波器的通用三相AC-DC系统，核心为6脉冲晶闸管/二极管线换相整流器(LCR)
- **仿真工具**: EMTP型节点分析仿真程序（如PSCAD/EMTDC、EMTP-RV等底层求解器架构）
- **验证结果**: 验证表明所提直接接口法在1000~2000 µs大步长下保持高精度与数值稳定性，克服了传统间接接口因一步延迟导致的精度下降与失稳问题，适用于大规模电力电子系统的实时/离线EMT仿真。
