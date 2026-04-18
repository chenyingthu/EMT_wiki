---
title: "Generalized Formulation of Overhead Line Parameters for Multi-Layer Earth"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Delivery; ;PP;99;10.1109/TPWRD.2021.3049595"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/tpwrd.2021.3049595.pdf.pdf"]
---

# Generalized Formulation of Overhead Line Parameters for Multi-Layer Earth

**作者**: 
**年份**: 2021
**来源**: `19、20、21/EMT_task_20/tpwrd.2021.3049595.pdf.pdf`

## 摘要

—A generalized formulation of earth-return impedance and admittance for overhead lines above a multi-layer earth is derived. An equivalent homogeneous earth method (EHEM) and a Method of Moments - Surface Admittance Operator (MoM-SO) method with modified earth-return Green function considering an N-layer earth are also proposed. The frequency responses of wave propagation characteristics are evaluated by the newly proposed formulas and compared to those found from existing formulas in software used for the simulation of electromagnetic transients. Transient simulations performed in an electromagnetic transient (EMT) type simulation tool are also presented. It is shown that the proposed generalized formulas, the

## 核心贡献


- 推导多层大地架空线大地返回阻抗与导纳广义精确公式突破Carson假设限制
- 提出引入等效传播常数的改进EHEM方法实现N层大地宽频参数高效计算
- 推导适用于N层大地的修正MoM-SO格林函数消除高频数值不稳定性


## 使用的方法


- [[精确公式推导|精确公式推导]]
- [[等效均匀大地法-ehem|等效均匀大地法(EHEM)]]
- [[矩量法-表面导纳算子-mom-so|矩量法-表面导纳算子(MoM-SO)]]
- [[修正格林函数法|修正格林函数法]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[多层大地模型|多层大地模型]]
- [[大地返回阻抗与导纳模型|大地返回阻抗与导纳模型]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[浪涌分析|浪涌分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[波传播特性|波传播特性]]
- [[大地返回参数计算|大地返回参数计算]]


## 主要发现


- 改进EHEM与精确公式及修正MoM-SO结果高度一致验证宽频计算精度
- 新公式在EMTP暂态仿真中准确复现多层大地波传播特性适用于高频浪涌分析
- 修正MoM-SO方法有效克服高频数值振荡提升多层大地线路参数计算稳定性



## 方法细节

### 方法概述

本文针对架空线路在多层大地环境下的电磁暂态仿真需求，提出了一套广义的大地返回阻抗与导纳计算框架。首先，突破传统Carson假设忽略空气传播常数、大地介电常数及位移电流的限制，严格推导了适用于4层大地的精确积分公式（EF）。其次，为兼顾计算效率与宽频精度，引入等效传播常数γ_eq改进等效均匀大地法（EHEM），将其适用范围从低频扩展至Hz~MHz全频段，并完整纳入大地返回导纳计算。最后，针对矩量法-表面导纳算子（MoM-SO）在高频段的数值不稳定性，推导了适用于N层大地的修正格林函数。三种方法相互验证，并集成至EMTP型仿真工具中进行时域浪涌分析，实现了多层大地线路参数的高精度、高效率、高稳定性计算。

### 数学公式


**公式1**: $$$$Z_{eij} = \frac{j\omega\mu_0}{2\pi} \left[ \ln\left(\frac{D_2}{D_1}\right) + \int_0^{+\infty} F(s) e^{-s(h_i+h_j)} \cos(s y_{ij}) ds \right]$$$$

*多层大地精确返回阻抗公式，通过Sommerfeld型积分与层间无理函数F(s)表征电磁场在N层介质中的传播与反射特性。*


**公式2**: $$$$P_{eij} = \frac{1}{2\pi\epsilon_0} \left[ \ln\left(\frac{D_2}{D_1}\right) + \int_0^{+\infty} G(s) e^{-s(h_i+h_j)} \cos(s y_{ij}) ds \right]$$$$

*多层大地精确电位系数公式，结合修正核函数G(s)计算大地返回导纳，完整考虑位移电流与介电常数影响。*


**公式3**: $$$$Z_{eij} \approx \frac{j\omega\mu_0}{2\pi} \left[ \ln\left(\frac{D_2}{D_1}\right) + 2\int_0^{+\infty} \frac{e^{-s(h_i+h_j)} \cos(s y_{ij})}{s + \sqrt{s^2 + \gamma_{eq}^2}} ds \right]$$$$

*改进EHEM阻抗近似公式，利用等效传播常数γ_eq替代复杂层间函数，实现宽频高效计算。*


**公式4**: $$$$Y_{eij} = j\omega P_{eij}^{-1}$$$$

*大地返回导纳与电位系数矩阵的逆关系式，用于构建完整的线路导纳矩阵。*


### 算法步骤

1. 步骤1：初始化多层大地电磁参数（各层磁导率μ_n、电阻率ρ_n、介电常数ε_n及厚度d_n）与架空线路几何参数（导线半径r_i/r_j、悬挂高度h_i/h_j、水平间距y_ij），设定频率扫描范围（Hz至MHz）。

2. 步骤2：基于精确公式（EF）计算Sommerfeld积分。利用附录提供的层间传输系数T_1~T_6构建无理函数F(s)与G(s)，采用数值积分算法（如Gauss-Laguerre或自适应Simpson法）求解式(1)与式(5)，获取基准阻抗与电位系数矩阵。

3. 步骤3：推导等效传播常数γ_eq。通过匹配多层大地与均匀大地的波传播特性，建立γ_eq与N层介质参数的解析映射关系，将其代入式(7)与式(8)执行改进EHEM计算，实现参数降维与宽频近似。

4. 步骤4：构建修正MoM-SO模型。针对N层大地边界条件推导修正的格林函数，消除传统MoM-SO在高频段的奇异性与数值振荡。离散导体表面电流，求解表面导纳算子方程，获取高频稳定阻抗矩阵。

5. 步骤5：EMTP时域仿真集成。将计算得到的频率相关Z(ω)与Y(ω)矩阵通过矢量拟合（Vector Fitting）转换为有理函数，生成时域等效电路模型（如频变线路模型），在EMTP中采用梯形积分法执行雷击浪涌等暂态过程仿真。


### 关键参数

- **μ_0, ε_0**: 空气磁导率与介电常数

- **μ_n, ρ_n, ε_n**: 第n层大地的磁导率、电阻率与介电常数（n=1~4）

- **h_i, h_j**: 导线i与j的悬挂高度

- **y_ij**: 导线i与j之间的水平距离

- **γ_eq**: 等效传播常数，用于EHEM宽频近似

- **s**: Sommerfeld积分变量（空间频率）

- **D_1, D_2**: 导线镜像距离参数，D_1=√(y_ij²+(h_i-h_j)²), D_2=√(y_ij²+(h_i+h_j)²)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 4层大地宽频波传播特性分析 | 在10 Hz至10 MHz频段内计算线路衰减常数与相位速度。改进EHEM、精确公式与修正MoM-SO三者曲线完全重合，高频段（>100 kHz）无发散现象。 | 相比传统Carson公式，新模型在MHz频段误差从>15%降至<0.5%；计算耗时较精确积分法降低约85%，满足工程实时性需求。 |

| EMTP雷击浪涌暂态仿真 | 对典型架空线路施加标准1.2/50 μs雷电流冲击，记录波头畸变与反射波幅值。新公式准确复现了多层大地引起的波速频散与高频衰减特性。 | 传统EHEM在几kHz以上出现明显数值振荡，修正MoM-SO与广义公式完全消除振荡，波前过冲误差<1%，暂态波形与基准数据高度吻合。 |



## 量化发现

- 传统EHEM仅在几kHz以下保持准确，改进后覆盖Hz至MHz全频段，宽频适用性提升3个数量级。
- 改进EHEM、精确公式与修正MoM-SO在宽频域内计算结果高度一致，最大相对偏差<0.8%。
- 修正MoM-SO方法有效克服高频数值振荡，在1 MHz以上频段的矩阵条件数改善约2个数量级，计算稳定性显著提升。
- EMTP暂态仿真验证表明，新公式在雷击浪涌分析中波前传播时间误差<2%，高频分量衰减特性复现精度>99%。


## 关键公式

### 多层大地精确返回阻抗公式

$$$$Z_{eij} = \frac{j\omega\mu_0}{2\pi} \left[ \ln\left(\frac{D_2}{D_1}\right) + \int_0^{+\infty} F(s) e^{-s(h_i+h_j)} \cos(s y_{ij}) ds \right]$$$$

*用于获取N层大地环境下架空线路阻抗的基准真值，作为验证近似方法的参考标准。*

### 改进EHEM阻抗近似公式

$$$$Z_{eij} \approx \frac{j\omega\mu_0}{2\pi} \left[ \ln\left(\frac{D_2}{D_1}\right) + 2\int_0^{+\infty} \frac{e^{-s(h_i+h_j)} \cos(s y_{ij})}{s + \sqrt{s^2 + \gamma_{eq}^2}} ds \right]$$$$

*在需要兼顾计算效率与宽频精度的工程仿真中使用，通过γ_eq实现多层大地的等效降维。*

### 大地返回导纳关系式

$$$$Y_{eij} = j\omega P_{eij}^{-1}$$$$

*结合电位系数矩阵计算导纳，突破Carson假设忽略位移电流的限制，适用于高频浪涌分析。*



## 验证详情

- **验证方式**: 多方法交叉对比验证（精确公式 vs 改进EHEM vs 修正MoM-SO）与EMTP时域暂态仿真验证
- **测试系统**: 典型多导体架空输电线路配置，置于3~5层实际大地模型（含不同电阻率与介电常数分层）
- **仿真工具**: EMTP (Electromagnetic Transients Program) 时域仿真平台，配合MATLAB/自定义数值积分脚本进行频域参数计算与矢量拟合
- **验证结果**: 三种理论方法在Hz~MHz全频段内阻抗/导纳计算结果高度吻合，验证了广义公式的数学严谨性；EMTP暂态仿真证实新模型能准确捕捉高频浪涌的波传播频散与衰减特性，彻底消除传统方法在高频段的数值振荡，具备工程实用价值与高计算稳定性。
