---
title: "Multiphase power flow solutions using EMTP and Newtons method - Power Systems, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Multiphase power flow solutions using EMTP and Newtons method.pdf"]
---

# Multiphase power flow solutions using EMTP and Newtons method - Power Systems, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Multiphase power flow solutions using EMTP and Newtons method.pdf`

## 摘要

This paper describes a reliable and veay flexible multiphase load-flow solution process which is applicable for large trans- mission systems (up to 500 nodes). The process consists of an interface between the Electromagnetic Transients Rogram (EMTP) and a newly developed multiphase load flow algo- rithm that is based on the Newton-Raphson metbod. Subjects discussed include derivation of basic algorithm, s~ucture of the Jacobian matrix, and convergence charactaistics. INTRODUCTION Well known and reliable methods exist today for solving AC single-phase power flow pblems. Most of tbese are based on the Newton-Raphson method, which has become the method of choice. Single-phase load flows always assume balanced rhree-phase system opeaation, aod are ideaUy suited for representing large transmiss

## 核心贡献


- 提出基于支路电流法与直角坐标的牛顿拉夫逊多相潮流算法，提升不平衡系统建模灵活性
- 实现算法与EMTP无缝接口，直接复用网络导纳矩阵，避免重复构建
- 为大型输电系统提供精确稳态初始化方案，有效支持后续电磁暂态仿真


## 使用的方法


- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[支路电流法|支路电流法]]
- [[直角坐标法|直角坐标法]]
- [[雅可比矩阵构建|雅可比矩阵构建]]
- [[emtp接口集成|EMTP接口集成]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[pq负荷|PQ负荷]]
- [[电压源|电压源]]
- [[电流源|电流源]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]


## 相关主题


- [[多相潮流计算|多相潮流计算]]
- [[不平衡系统分析|不平衡系统分析]]
- [[稳态初始化|稳态初始化]]
- [[emtp集成|EMTP集成]]
- [[大型输电网络|大型输电网络]]


## 主要发现


- 算法在500节点系统中验证可靠，有效克服传统EMTP相量法收敛性差的问题
- 支路电流法显著提升三角形接线与相间电源等复杂负荷的建模灵活性与精度
- 与EMTP集成可直接获取精确稳态导纳矩阵，为暂态仿真提供高质量初始条件



## 方法细节

### 方法概述

本文提出一种基于牛顿-拉夫逊法的多相潮流计算方法，采用直角坐标系（rectangular coordinates）和支路电流法（branch current method）而非传统的节点功率法。该方法与电磁暂态程序（EMTP）深度集成，直接利用EMTP生成的YBUS导纳矩阵，避免了重复构建网络方程。算法通过建立支路层面的约束方程（包括KCL方程和各类非线性元件约束），构建非对称的雅可比矩阵，并采用改进的Tinney排序算法处理矩阵中的零对角线问题。该方法支持三相不平衡系统建模，可处理三角形连接负荷、相间电压源等复杂接线方式，适用于最多500个节点的大型输电系统。

### 数学公式


**公式1**: $$$$\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \mathbf{J} \begin{bmatrix} \Delta \theta \\ \Delta V \end{bmatrix}$$$$

*传统单相潮流牛顿-拉夫逊法的基本形式，基于功率失配与电压/角度失配的关系*


**公式2**: $$$$[Y]V = [I_s] + [I_u]$$$$

*基尔霍夫电流定律（KCL）的矩阵形式，其中[Y]为节点导纳矩阵，V为节点电压向量，[Is]为已知电流源向量，[Iu]为未知电流源向量*


**公式3**: $$$$\begin{bmatrix} Y_R & -Y_I \\ Y_I & Y_R \end{bmatrix} \begin{bmatrix} V_R \\ V_I \end{bmatrix} = \begin{bmatrix} I_{sR} \\ I_{sI} \end{bmatrix} + \begin{bmatrix} I_{uR} \\ I_{uI} \end{bmatrix}$$$$

*直角坐标系下的KCL方程实数形式，YR和YI分别为导纳矩阵的实部和虚部，VR和VI为电压的实部和虚部*


**公式4**: $$$$V_k - E_m = 0$$$$

*电压源约束方程，表示节点k的电压受内部电压Em控制*


**公式5**: $$$$f_{2k} = V_k^*(V_k - V_m)y^* - (P + jQ)M = 0$$$$

*单相PQ负荷约束方程（load-2），其中y为负荷导纳参数，M为负荷连接矩阵，P和Q为有功和无功功率设定值*


**公式6**: $$$$I_{u3} = [V][y][W]V$$$$

*三相静态负荷方程（load-3），其中[y]为静态负荷导纳参数矩阵，[W]为对称比例矩阵（表示零序与正序阻抗比）*


**公式7**: $$$$I_{mR} + jI_{mI} = [y_g](E_R + jE_I - V_R - jV_I)$$$$

*同步电机电流方程，[yg]为电机3×3内部导纳矩阵，E为内部电压向量*


### 算法步骤

1. 数据准备与网络构建：通过EMTP数据组装程序构建节点导纳矩阵YBUS，该矩阵包含所有线性支路（输电线路、变压器）和并联元件的影响，保持最优稀疏性结构

2. 变量初始化：设置节点电压初始值（实部VR和虚部VI）、电流源初始值、电机内部电压E和静态负荷参数y的初始猜测值。注：传统1.0∠0° p.u.初始值在三相不平衡情况下通常不适用

3. 约束方程建立：针对各类非线性元件建立约束方程，包括：电压源方程（3）、单相PQ负荷方程（4）、三相静态负荷方程（5）、同步电机有功/无功约束及内部电压方程（6-8）

4. 雅可比矩阵构建：计算约束方程对节点电压V、支路电流Iv、IL、Im、Iu、电机内部电压E和负荷参数y的偏导数，形成非对称的雅可比矩阵J

5. 矩阵重排序：采用改进的Tinney方案2处理非对称矩阵，计算每行和每列非零元素数量的乘积作为排序指标，选择乘积最小的行/列作为下一个主元。将具有零对角线的电压约束相关行（电压源、摇摆机、PV机的V部分）强制移至矩阵底部

6. 高斯消元与填充优化：基于重排序后的矩阵结构进行符号消元，模拟消元过程中的填充元（fill-ins）产生情况，更新行列非零元素计数，确保零对角线元素在消元过程中被填充后再处理

7. 牛顿-拉夫逊迭代求解：求解线性方程组J·Δx = -f，其中f为残差向量（指定值-计算值），Δx包含电压修正量ΔVR、ΔVI、电流修正量等状态变量修正值

8. 变量更新与收敛检查：更新所有状态变量x^(k+1) = x^(k) + Δx，计算新的功率失配和电流残差。若最大残差小于收敛阈值则停止，否则返回步骤3继续迭代

9. EMTP稳态初始化：将收敛后的稳态电压和电流作为EMTP暂态仿真的初始条件，实现精确的动态和暂态仿真启动


### 关键参数

- **max_nodes**: 500个节点（适用的大型输电系统规模）

- **coordinate_system**: 直角坐标系（rectangular coordinates）

- **matrix_type**: 非对称雅可比矩阵（unsymmetric Jacobian）

- **ordering_scheme**: 改进的Tinney Scheme 2（针对非对称矩阵）

- **zero_diagonal_handling**: 电压约束行强制置底（forced to bottom）

- **initial_voltage**: 非1.0 p.u.（需根据系统不平衡度调整）

- **convergence_criterion**: 功率/电流残差足够小（具体数值未明确给出）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 124节点系统雅可比矩阵稀疏性分析 | 原始排序下上三角元素数量为21,321个，矩阵填充率为24.82%；采用非对称重排序算法后，上三角元素数量降至3,781个，填充率降至4.40%。消元后的矩阵结构显示原始排序产生大量填充元（图4黑色区域），而重排序后保持稀疏性（图5） | 稀疏性改善：填充率从24.82%降低至4.40%，减少约82.3%的存储需求；上三角元素减少17,540个（减少82.3%） |

| 443节点多相潮流收敛性测试 | 在443节点大型系统上验证算法可靠性，证明传统1.0∠0° p.u.初始电压不适用于三相不平衡潮流计算。通过采用EMTP稳态解作为初始值，成功实现大系统收敛 | 克服了传统EMTP相量法在大型不平衡系统中的收敛性差的问题 |



## 量化发现

- 算法适用规模：可处理最多500个节点的大型输电系统
- 雅可比矩阵稀疏性：原始排序填充率为24.82%，重排序后降至4.40%
- 矩阵元素数量：124节点系统消元后上三角元素从21,321个减少至3,781个
- 计算效率提升：通过支路电流法和矩阵重排序，显著降低内存需求和计算量
- 建模灵活性：支持三角形连接负荷、相间电压源等复杂接线方式，相比节点功率法具有更高的建模精度
- 收敛特性：对初始电压敏感，需采用非1.0 p.u.的合理初始值以保证牛顿-拉夫逊法收敛


## 关键公式

### 直角坐标系KCL方程

$$$$\begin{bmatrix} Y_R & -Y_I \\ Y_I & Y_R \end{bmatrix} \begin{bmatrix} V_R \\ V_I \end{bmatrix} = \begin{bmatrix} I_{sR} \\ I_{sI} \end{bmatrix} + \begin{bmatrix} I_{uR} \\ I_{uI} \end{bmatrix}$$$$

*在每次牛顿迭代中求解节点电压的实部和虚部，是算法核心线性方程组*

### 非对称矩阵重排序准则

$$$$\text{Minimize: } (\text{row\_count}[i] \times \text{col\_count}[i])$$$$

*基于Tinney Scheme 2改进的排序算法，选择行和列非零元素数量乘积最小的行作为主元，用于减少高斯消元过程中的填充元*

### 同步电机电流约束

$$$$I_{m} = [y_g](E - V)$$$$

*建立电机内部电压E与节点电压V之间的关系，用于PV机和摇摆机的控制约束建模*



## 验证详情

- **验证方式**: 仿真验证与对比分析
- **测试系统**: 124节点系统和443节点实际大型输电系统（American Electric Power系统）
- **仿真工具**: EMTP（Electromagnetic Transients Program）EPRI DCG版本，集成多相潮流模块
- **验证结果**: 在124节点系统上验证雅可比矩阵重排序效果显著（填充率从24.82%降至4.40%）；在443节点系统上验证算法对大型系统的适应性和收敛可靠性；与EMTP的集成验证表明可直接利用EMTP的网络建模能力（如输电线路、变压器详细模型）获取精确的稳态导纳矩阵，为暂态仿真提供准确的初始条件
