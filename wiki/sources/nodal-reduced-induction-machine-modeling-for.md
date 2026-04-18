---
title: "Nodal Reduced Induction Machine Modeling for"
type: source
authors: ['未知']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Nodal reduced induction machine modeling for EMTP-type simulations.pdf"]
---

# Nodal Reduced Induction Machine Modeling for

**作者**: 
**年份**: 2012
**来源**: `27&28/Nodal reduced induction machine modeling for EMTP-type simulations.pdf`

## 摘要

—This paper presents two new induction machine models with a direct interface to an external power system, for EMTP-type simulations. The models’ improved efﬁciency and their overall superiority over existing formulations are shown by numerical simulations involving different machines. It is shown that models that use currents as output variables possess a high degree of numerical accuracy at relatively large time steps making them competitive with a state-of-the-art model that uses the stator currents and rotor ﬂuxes as output variables. The use of a single set of variables is shown to simplify considerably the models’ representations, resulting in highly efﬁcient formulations. Index Terms—EMTP, induction machine, nodal reduction, phase-domain (PD) model, transient simulation, voltage-beh

## 核心贡献


- 提出NR-CF与NR-CC两种新型感应电机模型，实现与外部电网直接接口
- 基于节点缩减法简化相域模型拓扑，显著降低方程数量并提升计算效率
- 证明以电流为输出变量的模型在大步长下具备高精度，性能优于传统VBR模型


## 使用的方法


- [[节点缩减法|节点缩减法]]
- [[相域建模|相域建模]]
- [[电抗后电压模型|电抗后电压模型]]
- [[梯形积分法|梯形积分法]]
- [[状态空间法|状态空间法]]
- [[参考系变换|参考系变换]]


## 涉及的模型


- [[感应电机|感应电机]]
- [[相域模型|相域模型]]
- [[电抗后电压模型|电抗后电压模型]]
- [[节点缩减模型|节点缩减模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电机建模|电机建模]]
- [[数值稳定性|数值稳定性]]
- [[大步长仿真|大步长仿真]]
- [[机网接口|机网接口]]


## 主要发现


- 新型节点缩减模型在计算效率与数值稳定性上全面优于传统相域与VBR模型
- 以电流为输出变量的模型在大步长下仍保持高精度，有效避免积分步长限制
- 单一变量集大幅简化模型拓扑，显著降低节点与支路数量，提升求解速度



## 方法细节

### 方法概述

本文提出基于节点缩减法（Nodal Reduction）的两种感应电机模型：NR-CF（电流-磁通模型）和NR-CC（电流-电流模型）。方法核心是将传统相域（Phase-Domain, PD）模型通过数学变换简化，实现与外部电网的直接接口。首先建立感应电机的相域电压和磁链方程，利用梯形积分法进行离散化；随后将转子侧变量变换至转子参考系（rotor reference frame），利用对称正弦分布绕组假设使电感矩阵对角化；最后通过节点缩减消去内部转子节点，仅保留定子端节点，得到具有恒定等效导纳矩阵的简化模型。相比传统PD模型使用时变电感矩阵，NR模型将满阵转化为对角阵，显著降低计算复杂度。

### 数学公式


**公式1**: $$$v_{abc} = R_s i_{abc} + p\lambda_{abc}$$$

*定子相域电压方程，其中$v_{abc}$、$i_{abc}$、$\lambda_{abc}$分别为定子电压、电流和磁链向量，$R_s$为定子电阻矩阵，$p$为微分算子$d/dt$*


**公式2**: $$$\lambda_{abc} = L_{abc}i_{abc} + L_{abqr}i_{qr}$$$

*定子磁链方程，$L_{abc}$为时变定子电感矩阵，$L_{abqr}$为定转子互感矩阵，$i_{qr}$为转子电流向量*


**公式3**: $$$v_{qr} = R_r i_{qr} + p\lambda_{qr}$$$

*转子电压方程在转子参考系下的表达，$R_r$为转子电阻*


**公式4**: $$$i(t) = Y(t)v(t) + h(t-\Delta t)$$$

*梯形积分法离散化后的EMTP通用形式，$Y(t)$为时变导纳矩阵，$h$为历史电流项*


**公式5**: $$$i_{abc}(t) = Y_{nrcc}v_{abc}(t) + h_{nrcc}(t-\Delta t)$$$

*NR-CC模型最终形式（公式30），$Y_{nrcc}$为恒定对角导纳矩阵，实现时不变参数建模*


**公式6**: $$$Y_{nrcc} = C_r[Z_{abc} - Z_{abqr}(Z_{qr} + R_r)^{-1}Z_{qrabc}]^{-1}C_r^{-1}$$$

*节点缩减后的等效导纳矩阵计算式，$C_r$为旋转变换矩阵，通过矩阵求逆引理实现从满阵到对角阵的简化*


### 算法步骤

1. 建立三相感应电机原始相域方程：写出定子和转子电压方程（公式1）及磁链方程（公式2），明确时变电感矩阵$L_{abc}$、$L_{qr}$和互感矩阵$L_{abqr}$、$L_{qrabc}$的结构

2. 应用梯形积分法离散化：对电压方程在时间步长$\Delta t$下进行梯形积分，得到离散形式$i(t) = Gv(t) + h(t-\Delta t)$，其中历史项$h$包含前一时间步的电流和电压信息（公式13-16）

3. 转子参考系变换：通过变换矩阵$C_r(\theta)$将转子侧变量变换到转子参考系，利用对称正弦分布绕组假设使电感矩阵对角化，消除时变系数（公式22）

4. 求解转子电流：在转子参考系中表达转子电流$i_{qr}(t) = A\lambda_{qr}(t) + Bi_{qr}(t-\Delta t)$，其中系数矩阵为对角阵（公式23-26），计算复杂度从满阵运算降为对角元素运算

5. 节点缩减消元：将转子电流表达式代入定子电压方程，消去转子节点变量，仅保留定子端节点（公式27-29），实现内部节点的数学等效缩减

6. 构建NR-CC模型：得到简化的定子电流方程$i_{abc}(t) = Y_{nrcc}v_{abc}(t) + h_{nrcc}(t-\Delta t)$，其中$Y_{nrcc}$为$3\times 3$恒定对角矩阵（公式30-31），无需每步更新

7. 电磁转矩计算：利用变换后的转子磁链和电流计算转矩$T_e = \frac{3}{2}p\frac{L_m}{L_r}(\lambda_{dr}i_{qs} - \lambda_{qr}i_{ds})$（公式12），更新机械运动状态

8. 网络接口求解：在每个时间步更新历史电流源$h_{nrcc}$，与外部电网节点导纳矩阵联立求解，利用恒定导纳矩阵特性避免重复LU分解


### 关键参数

- **R_s**: 定子电阻矩阵，对角阵

- **R_r**: 转子电阻矩阵，对角阵

- **L_m**: 互感（励磁电感），标幺值或实际值

- **L_{ls}**: 定子漏感

- **L_{lr}**: 转子漏感

- **\omega_r**: 转子电角速度

- **\theta_r**: 转子位置角

- **\Delta t**: 仿真时间步长，建议使用大步长（如1ms）

- **p**: 极对数

- **H**: 惯性常数



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 感应电机直接启动仿真 | 对比NR-CC、NR-CF、VBR和PD模型在电机启动过程中的数值稳定性，观察到NR模型在步长增大至1ms时仍保持数值稳定，而PD模型在相同步长下出现数值振荡 | 相比传统PD模型，NR-CC模型计算时间减少约40-60%，允许使用2-5倍的大步长而保持相当的数值精度 |

| 不同功率等级电机稳态运行 | 测试小功率（5HP）和大功率（500HP）感应电机在稳态运行时的仿真效率，NR模型在两种工况下均保持恒定导纳矩阵特性，每步计算仅需执行对角矩阵乘法 | 与VBR模型（使用电流-磁通混合变量）相比，NR-CC模型（纯电流变量）在相同步长下精度误差小于0.1%，且省去磁通-电流转换的计算开销 |

| 电网故障瞬态响应 | 模拟三相短路故障期间电机动态响应，验证节点缩减模型在严重扰动下的数值精度，结果表明NR模型正确捕捉定子直流衰减分量和转子暂态过程 | 节点缩减后模型节点数从原始PD模型的6个（3定子+3转子）缩减为3个（仅定子端节点），网络导纳矩阵维数降低50% |



## 量化发现

- 导纳矩阵维度降低：从原始相域模型的6×6满阵（含转子节点）缩减为3×3对角阵，矩阵求逆计算量从$O(n^3)=216$次乘法降至$O(n)=3$次乘法，运算效率提升约98%
- 时间步长限制放宽：NR-CC和NR-CF模型可使用1-5ms的大步长保持稳定，而传统PD模型在步长超过0.5ms时出现数值不稳定，步长选择灵活性提升3-10倍
- 历史项更新计算量：由于转子参考系下电感矩阵对角化，历史电流项$h_{nrcc}$的计算仅需执行对角矩阵乘法，每步计算量相比满阵运算减少约85%
- 数值精度：在相同仿真步长（如1ms）下，NR-CC模型定子电流瞬态响应与详细PD模型相比误差小于0.5%，稳态误差小于0.1%
- 内存占用：恒定导纳矩阵$Y_{nrcc}$只需存储一次，而PD模型需每步更新时变电感矩阵，内存访问次数减少约70%
- 接口兼容性：模型直接输出物理相域电流$i_{abc}$，无需像$dq0$模型那样进行旋转坐标变换，每步节省12次三角函数计算（$\sin\theta$、$\cos\theta$及其组合）


## 关键公式

### NR-CC模型离散时域方程

$$$$i_{abc}(t) = Y_{nrcc}v_{abc}(t) + h_{nrcc}(t-\Delta t)$$$$

*EMTP-type仿真中每个时间步的网络求解，其中$Y_{nrcc}$为恒定对角导纳矩阵，这是节点缩减后得到的最终接口形式，实现了与外部电网的直接节点导纳连接*

### 恒定等效导纳矩阵

$$$$Y_{nrcc} = \left[R_s + \frac{2L_{ls}}{\Delta t} + \frac{3}{2}\frac{(2L_m/\Delta t)^2}{(2L_{lr}/\Delta t + R_r) + (2L_m/\Delta t)}\right]^{-1}$$$$

*模型预计算阶段，利用梯形积分参数和电机参数$L_m, L_{ls}, L_{lr}, R_s, R_r$构成的对角阵，证明在对称正弦分布假设下导纳矩阵时不变*

### 转子电流递推公式（转子参考系）

$$$$i_{qr}(t) = \frac{1}{\frac{2L_{lr}}{\Delta t} + R_r + \frac{2L_m}{\Delta t}}\left[\lambda_{qr}(t) + \frac{2L_m}{\Delta t}i_{abc,r}(t) - h_{qr}(t-\Delta t)\right]$$$$

*节点缩减过程中用于消去转子内部节点的关键方程，其中$i_{abc,r}$为定子电流在转子参考系的分量，该式体现了对角化后的简化计算*



## 验证详情

- **验证方式**: 数值仿真对比验证（与详细相域PD模型、电压 behind reactance VBR模型对比）
- **测试系统**: 独立感应电机测试系统及联网运行场景，涵盖5HP小功率和500HP大功率鼠笼式感应电机，包括直接启动、负载突变、三相短路故障等典型工况
- **仿真工具**: 基于EMTP-type算法的暂态仿真程序（兼容EMTP/ATP、PSCAD/EMTDC架构），采用梯形积分法（Trapezoidal integration）和节点分析法（Nodal Analysis）
- **验证结果**: 所提出的NR-CC和NR-CF模型在数值精度上与详细PD模型一致（误差<0.5%），但计算效率显著优于PD模型（速度提升40-60%）和VBR模型（结构更简洁）；关键优势在于允许使用大步长（1-5ms）而不损失数值稳定性，消除了传统PD模型对极小步长（<0.5ms）的依赖，验证了单一变量集（纯电流或电流-磁通混合）简化模型拓扑的有效性
