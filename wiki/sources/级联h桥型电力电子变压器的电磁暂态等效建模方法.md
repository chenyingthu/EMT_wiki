---
title: "级联H桥型电力电子变压器的电磁暂态等效建模方法"
type: source
authors: ['CNKI']
year: 2022
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/16/丁江萍 等 - 2020 - 级联H桥型电力电子变压器的电磁暂态等效建模方法.pdf"]
---

# 级联H桥型电力电子变压器的电磁暂态等效建模方法

**作者**: CNKI
**年份**: 2022
**来源**: `16/丁江萍 等 - 2020 - 级联H桥型电力电子变压器的电磁暂态等效建模方法.pdf`

## 摘要

The power electronic transformer (PET) applied to the medium and high voltage distribution network widely adopts a two-stage cascade structure of a cascaded H-bridge rectifier and a dual-active bridge DC/DC converter. Aiming at the problem of extremely slow simulation speed in offline simulation platforms such as PSCAD/EMTDC and MATLAB, based on the Thévenin’s equivalent and nested fast simultaneous solving algorithm, an electromagnetic transient simulation accelerated model of cascaded H-bridge PET was proposed. Specifically, by arranging the decoupling companion network of the primary/secondary side of the high-frequency transformer flexibly, the cascaded sub-modules were divided into two single-port networks, and then the equivalent part of the Thévenin’s (Norton’s) equivalent parameter

## 核心贡献



- 提出基于戴维南/诺顿等效与嵌套快速同时求解算法的级联H桥型电力电子变压器电磁暂态仿真加速模型
- 通过构造高频变压器解耦伴随网络将级联子模块等效为仅含4个外部节点的单端口网络，使系统整体求解的计算复杂度几乎不随子模块数量增加

## 使用的方法


- [[network-equivalent]]
- [[nodal-analysis]]

## 涉及的模型


- [[transformer]]

## 相关主题


- [[network-equivalent]]
- [[transformer]]

## 主要发现



- 所提等效模型在PSCAD/EMTDC平台中能够精确复现级联H桥型电力电子变压器的暂态与稳态过程
- 模型外部等效节点数固定，计算复杂度不随子模块数量增长，相比详细模型具有极高的仿真加速比

## 方法细节

### 方法概述

基于诺顿/戴维南等效与嵌套快速同时求解算法，通过灵活构造高频变压器原/副边的解耦伴随网络，将级联H桥型PET的CHB单元分割为原边侧(P1)和副边侧(P2)两个单端口网络，实现对外仅保留4个外部节点的等效电路。该方法采用正向求解等效参数、系统整体求解节点电压方程、反解更新内部状态的三步循环机制，使得系统整体求解的计算复杂度几乎不随子模块数量增加，解决了传统详细模型在PSCAD/EMTDC等平台仿真速度极慢的问题。

### 数学公式


**公式1**: $$$$\begin{bmatrix} I_1(t) \\ I_2(t) \end{bmatrix} = \begin{bmatrix} G_{AA} & G_{AB} \\ G_{BA} & G_{BB} \end{bmatrix} \left( \begin{bmatrix} V_1(t) \\ V_2(t) \end{bmatrix} + \begin{bmatrix} V_1(t-\Delta T) \\ V_2(t-\Delta T) \end{bmatrix} \right) + \begin{bmatrix} I_1(t-\Delta T) \\ I_2(t-\Delta T) \end{bmatrix}$$$$

*高频隔离变压器原始端口电压电流关系，基于梯形积分法离散化得到，其中G为等效电导矩阵，I为历史电流项*


**公式2**: $$$$\begin{bmatrix} G_{AA} & G_{AB} \\ G_{BA} & G_{BB} \end{bmatrix} = \frac{\Delta T}{2} \begin{bmatrix} \frac{L_m}{k^2} + L_1 & -\frac{L_m}{k} \\ -\frac{L_m}{k} & L_m + L_2 \end{bmatrix}^{-1}$$$$

*变压器等效电导矩阵计算式，k为变比，L1、L2为漏感，Lm为励磁电感，ΔT为仿真步长*


**公式3**: $$$$\begin{bmatrix} I_1(t) \\ I_2(t) \end{bmatrix} = \begin{bmatrix} G_{AA}^D & 0 \\ 0 & G_{BB}^D \end{bmatrix} \begin{bmatrix} V_1(t) \\ V_2(t) \end{bmatrix} + \begin{bmatrix} J_{TEQ\_HIS1}^D \\ J_{TEQ\_HIS2}^D \end{bmatrix}$$$$

*解耦后的变压器伴随网络方程，原边与副边电气量解耦，相互独立求解*


**公式4**: $$$$\begin{cases} G_{AA}^D = G_{AA} \\ G_{BB}^D = G_{BB} \\ J_{TEQ\_HIS1}^D = J_{TEQ\_HIS1}^{PI} + G_{AB}V_2(t) \\ J_{TEQ\_HIS2}^D = J_{TEQ\_HIS2}^{PI} + G_{BA}V_1(t) \end{cases}$$$$

*解耦伴随网络与原始电路等价的条件，通过受控电流源引入对侧信息实现解耦*


**公式5**: $$$$G_L = \frac{\Delta T}{2L}, \quad J_{LEQ} = G_L V_L(t-\Delta T) + I_L(t-\Delta T)$$$$

*附加电感离散化等效参数，等效为电导GL与历史电流源JLEQ并联*


**公式6**: $$$$G_C = \frac{2C}{\Delta T}, \quad J_{CEQ} = V_C(t-\Delta T) \cdot G_C + I_C(t-\Delta T)$$$$

*直流侧电容离散化等效参数，等效为电导GC与历史电流源JCEQ并联*


**公式7**: $$$$G_k = \begin{cases} G_{ON}, & T_k=1 \\ G_{Off}, & T_k=0 \end{cases}, \quad k=1,2,\cdots,12$$$$

*IGBT/二极管开关组等效电导，根据触发信号Tk状态在高、低阻值间切换*


### 算法步骤

1. 伴随电路构造：将IGBT/二极管开关组等效为二值电阻（导通电阻GON或关断电阻GOff）；采用梯形积分法将附加电感离散化为等效电导GL与历史电流源JLEQ并联形式；将电容C1、C2离散化为等效电导GC与历史电流源JCEQ并联；构造高频变压器解耦伴随网络，将原边和副边分别等效为受控电流源并联电阻的诺顿形式，实现电气量解耦

2. 单端口网络分割：基于变压器解耦伴随网络，将CHB单元分割为P1（原边侧，包含H桥、电容C1、附加电感及变压器原边）和P2（副边侧，包含变压器副边、H桥及电容C2）两个独立的单端口网络，两侧通过受控电流源JDTEQ_HIS1和JDTEQ_HIS2在计算环节保持信息交互

3. 正向求解等效参数：对每个CHB单元的P1和P2部分分别计算诺顿等效参数，包括等效电导（GEQ）和等效历史电流源（JEQ），将多个子模块级联结构等效为仅含4个外部节点（输入正负极、输出正负极）的诺顿/戴维南等效电路

4. 系统整体求解：将等效后的4节点网络代入电磁暂态程序（EMTP），构建系统节点导纳矩阵，求解得到外部节点电压

5. 反解与状态更新：根据求解得到的外部节点电压，反解各CHB单元内部节点电压和支路电流，更新电感电流IL(t)、电容电压VC(t)及变压器端口电压电流，计算下一时步的历史电流源值，初始化下一个仿真步长的电气网络


### 关键参数

- **仿真步长ΔT**: 10μs及以下（针对5kHz开关频率的DAB）

- **DAB工作频率**: 5kHz（单移相控制）

- **级联模块数**: 3模块（验证用例），方法支持任意数量

- **等效外部节点数**: 4个（输入正负极、输出正负极）

- **IGBT导通电阻**: GON（用户自定义参数）

- **IGBT关断电阻**: GOff（用户自定义参数）

- **变压器变比**: k:1

- **漏感参数**: L1（原边）、L2（副边折合到一次侧）

- **励磁电感**: Lm



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 变压器伴随电路精度验证 | 在PSCAD/EMTDC中搭建测试电路，对比本文提出的解耦伴随电路与软件自带变压器模型，端口电压V1、V2和电流I1、I2波形均较为吻合，验证了等效建模方法的精确性 | 与PSCAD/EMTDC详细变压器模型相比，波形一致性良好 |

| 级联H桥型PET闭环系统仿真 | 在PSCAD/EMTDC中搭建3模块级联H桥型PET闭环控制系统，所提等效模型能够精确复现PET的暂态与稳态过程，包括电容电压、输出电流等电气量的动态特性 | 与详细模型相比，计算复杂度几乎不随子模块数量增加，而详细模型仿真速度随模块数增加显著下降 |



## 量化发现

- 所提模型对外等效为仅包含4个外部节点的戴维南/诺顿等效电路
- 系统整体求解的计算复杂度几乎不随子模块个数增加（O(1)复杂度），而详细模型复杂度随模块数线性或超线性增长
- 针对5kHz开关频率的DAB，需设置10μs及以下的仿真步长才能精确控制移相角
- 验证用例采用3模块级联H桥型PET结构
- 变压器端口电气量（电压、电流）与详细模型相比误差极小，波形吻合度良好
- 所提模型属于精确等效模型，能够复现开关动作产生的谐波，区别于忽略谐波的平均值模型


## 关键公式

### 变压器解耦伴随网络端口方程

$$$$\begin{bmatrix} I_1(t) \\ I_2(t) \end{bmatrix} = \begin{bmatrix} G_{AA}^D & 0 \\ 0 & G_{BB}^D \end{bmatrix} \begin{bmatrix} V_1(t) \\ V_2(t) \end{bmatrix} + \begin{bmatrix} J_{TEQ\_HIS1}^{PI} + G_{AB}V_2(t-\Delta T) \\ J_{TEQ\_HIS2}^{PI} + G_{BA}V_1(t-\Delta T) \end{bmatrix}$$$$

*将高频变压器原/副边解耦为两个独立的诺顿等效电路，用于分割CHB单元为P1和P2两个单端口网络，是实现计算复杂度不随模块数增加的关键*

### 变压器等效电导矩阵

$$$$\begin{bmatrix} G_{AA} & G_{AB} \\ G_{BA} & G_{BB} \end{bmatrix} = \frac{\Delta T}{2( \frac{L_1L_m}{k^2} + L_1L_2 + \frac{L_mL_2}{k} )} \begin{bmatrix} \frac{L_m}{k^2} + L_2 & -\frac{L_m}{k} \\ -\frac{L_m}{k} & L_1 + L_m \end{bmatrix}$$$$

*基于梯形积分法对变压器T型等效电路离散化得到，用于计算伴随网络中的等效电导参数*



## 验证详情

- **验证方式**: 仿真对比验证（与详细模型在PSCAD/EMTDC平台对比）
- **测试系统**: 级联H桥型PET闭环控制系统，包含3个CHB单元（A相），采用ISOP（输入串联输出并联）结构，配置双有源桥DC-DC变换器（DAB）
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 所提模型能够精确仿真PET的暂态与稳态过程，变压器端口电压电流波形与详细模型吻合良好，验证了等效模型的精确性；同时具有极高的仿真加速比，计算复杂度几乎不随子模块数量增加
