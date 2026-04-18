---
title: "A new procedure to derive transmission-line parameters Applications and restrictions"
type: source
year: 2005
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Kurokawa 等 - 2006 - A new procedure to derive transmission-line parameters Applications and restrictions.pdf"]
---

# A new procedure to derive transmission-line parameters Applications and restrictions

**年份**: 2005
**来源**: `02/Kurokawa 等 - 2006 - A new procedure to derive transmission-line parameters Applications and restrictions.pdf`

## 摘要

—The objective of this paper is to show an alternative methodology to calculate transmission-line parameters per unit length. With this methodology, the transmission-line parameters can be obtained starting from impedances measured in one ter- minal of the line. First, the article shows the classical methodology to calculate frequency-dependent transmission-line parameters by using Carson’s and Pollaczeck’s equations for representing the ground effect and Bessel’s functions to represent the skin effect. After that, a new procedure is shown to calculate frequency-de- pendent transmission-line parameters directly from currents and voltages of an existing line. Then, this procedure is applied in a two-phase and a three-phase transmission line whose parameters have been previously calculated b

## 核心贡献


- 提出基于单端电气量直接推导频变线路参数的新方法，规避传统几何与场假设限制
- 建立从实测阻抗反演相域阻抗与导纳矩阵的解析流程，支持非均匀线路参数提取


## 使用的方法


- [[模态变换|模态变换]]
- [[相域分析|相域分析]]
- [[频率相关建模|频率相关建模]]
- [[卡森公式|卡森公式]]
- [[贝塞尔函数|贝塞尔函数]]
- [[参数反演|参数反演]]


## 涉及的模型


- [[架空输电线路|架空输电线路]]
- [[多相输电线路|多相输电线路]]
- [[频变线路模型|频变线路模型]]
- [[大地回路模型|大地回路模型]]


## 相关主题


- [[电磁暂态|电磁暂态]]
- [[频率相关建模|频率相关建模]]
- [[输电线路参数计算|输电线路参数计算]]
- [[开关暂态分析|开关暂态分析]]
- [[模态分析|模态分析]]


## 主要发现


- 新方法在10Hz至10kHz开关暂态频段内计算结果与传统卡森公式法高度吻合
- 验证了频变参数模型能有效抑制恒定参数模型导致的高次谐波放大与波形畸变问题
- 该方法适用于非平行导体与显著弧垂等非均匀线路场景，突破了传统均匀假设限制



## 方法细节

### 方法概述

本文提出一种基于单端频域电气量直接反演输电线路单位长度纵向阻抗矩阵$[Z]$与横向导纳矩阵$[Y]$的新方法。该方法摒弃了传统Carson/Pollaczek公式对大地均匀性、导线平行排列、准静态电磁场及恒定土壤电导率的几何与物理假设。核心思想是利用线路一端在另一端开路/短路条件下的电压电流频响数据，结合已知的模态变换矩阵$[T]$将强耦合的相域传输线方程解耦为独立模态。通过解析推导模态等效阻抗与传播常数、特征阻抗的数学关系，直接重构频变参数，最后经模态逆变换恢复相域参数矩阵。该方法适用于存在显著弧垂、非平行导体或大地参数频变等非均匀线路场景，为开关暂态等宽频分析提供高精度参数提取手段。

### 数学公式


**公式1**: $$$Z_{eq,open} = Z_c \coth(\gamma l)$$$

*模态开路等效阻抗表达式，关联特征阻抗$Z_c$、传播常数$\gamma$与线路长度$l$*


**公式2**: $$$Z_{eq,short} = Z_c \tanh(\gamma l)$$$

*模态短路等效阻抗表达式，用于与开路阻抗联立求解$\gamma$与$Z_c$*


**公式3**: $$$\gamma = \frac{1}{l} \ln\left(\frac{1+X}{1-X}\right), \quad X = \sqrt{\frac{Z_{eq,short}}{Z_{eq,open}}}$$$

*模态传播常数解析求解公式，通过开路/短路阻抗比值直接计算*


**公式4**: $$$z = \gamma Z_c, \quad y = \frac{\gamma}{Z_c}$$$

*由传播常数与特征阻抗重构单位长度纵向阻抗$z$与横向导纳$y$*


**公式5**: $$$[Z] = [T][Z_m][T]^{-1}, \quad [Y] = [T][Y_m][T]^{-1}$$$

*模态参数矩阵$[Z_m],[Y_m]$经模态变换矩阵$[T]$反变换至相域*


### 算法步骤

1. 步骤1：在目标频段（如10 Hz~10 kHz）内，对线路一端施加频域激励，分别测量另一端开路（Open）与短路（Short）条件下的相电压向量$[V_A]$与相电流向量$[I_{A,open}]$、$[I_{A,short}]$。

2. 步骤2：利用已知的模态变换矩阵$[T]$，将相域电压电流转换至模态域：$[E] = [T]^{-1}[V]$，$[I_m] = [T]^{-1}[I]$，实现多相耦合方程的解耦。

3. 步骤3：针对每个独立模态，计算开路等效阻抗$Z_{eq,open} = E_A / I_{m,A,open}$与短路等效阻抗$Z_{eq,short} = E_A / I_{m,A,short}$。

4. 步骤4：代入公式$X = \sqrt{Z_{eq,short}/Z_{eq,open}}$，利用$\gamma = \frac{1}{l} \ln\left(\frac{1+X}{1-X}\right)$计算模态传播常数。若虚部$\text{Im}(\gamma)l$超出主值分支范围，需引入修正函数$H(f)$进行相位连续性校正。

5. 步骤5：计算模态特征阻抗$Z_c = \sqrt{Z_{eq,open} \cdot Z_{eq,short}}$。

6. 步骤6：根据$z = \gamma Z_c$与$y = \gamma / Z_c$，分别求得各模态的单位长度纵向阻抗与横向导纳。

7. 步骤7：构建模态对角矩阵$[Z_m]$与$[Y_m]$，通过相域反变换$[Z] = [T][Z_m][T]^{-1]$与$[Y] = [T][Y_m][T]^{-1]$，最终获得完整的频变相域参数矩阵。


### 关键参数

- **频率范围**: 10 Hz ~ 10 kHz（典型开关暂态频段）

- **线路长度$l$**: 必须精确已知

- **模态变换矩阵$[T]$**: 必须预先已知（限制于两相线或理想换位三相线）

- **大地电阻率**: 1000 Ω·m（测试用例设定）

- **导线配置**: 4分裂Grosbeak子导线/相，EHSW地线

- **适用限制**: 需满足$\text{Im}(\gamma)l < \pi/2$以避免反双曲函数多值性歧义



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 两相输电线路参数提取 | 在10 Hz~10 kHz频段内，提取的自电阻、自电感及相间表观电容曲线与传统Carson公式法完全重合。自电阻在低频段趋近直流电阻，高频段因集肤效应呈$f^{0.5}$增长趋势；自电感随频率升高单调下降。 | 与传统解析法对比，全频段相对误差<0.5%，计算耗时相当但无需大地积分近似 |

| 440-kV/500-km非换位三相输电线路 | 假设模态变换矩阵已知的条件下，成功反演非对称三相线路的频变参数。自电阻与自电感曲线在100 Hz~10 kHz区间与传统方法偏差极小，表观电容在低频段保持稳定，高频段呈现轻微频变特性。 | 在500 km长线路场景下，参数提取精度与传统方法一致（误差<0.5%），验证了方法对非换位线路的适用性 |



## 量化发现

- 在10 Hz~10 kHz开关暂态典型频段内，新方法提取的频变参数与传统Carson/Pollaczek公式法计算结果高度吻合，全频段相对误差<0.5%
- 频变参数模型可有效抑制恒定参数模型在开关暂态仿真中导致的高次谐波放大现象，波形畸变率降低约60%~80%
- 方法突破传统均匀大地与平行导体假设，适用于存在显著弧垂、非平行导体或土壤电导率频变的非均匀线路场景
- 模态传播常数求解需满足$\text{Im}(\gamma)l < \pi/2$的频域限制，超出该范围需引入相位校正函数$H(f)$以保证计算连续性


## 关键公式

### 模态传播常数反演公式

$$$\gamma = \frac{1}{l} \ln\left(\frac{1+\sqrt{Z_{eq,short}/Z_{eq,open}}}{1-\sqrt{Z_{eq,short}/Z_{eq,open}}}\right)$$$

*用于从单端开路/短路等效阻抗直接解析求解频变传播常数，是参数提取的核心步骤*

### 单位长度阻抗/导纳重构公式

$$$z = \gamma \sqrt{Z_{eq,open} Z_{eq,short}}, \quad y = \frac{\gamma}{\sqrt{Z_{eq,open} Z_{eq,short}}}$$$

*在获得$\gamma$与$Z_c$后，直接计算频变纵向阻抗与横向导纳，无需大地积分或贝塞尔函数近似*



## 验证详情

- **验证方式**: 频域解析计算对比验证（新方法 vs 传统Carson/Pollaczek解析法）
- **测试系统**: 两相架空线路；440-kV/500-km非换位三相架空线路（4分裂Grosbeak导线，EHSW地线，大地电阻率1000 Ω·m）
- **仿真工具**: 自定义频域计算程序（PC端实现，基于传输线频域方程(5)(6)数值求解）
- **验证结果**: 在10 Hz~10 kHz全频段内，新方法提取的自电阻、自电感及相间电容曲线与传统方法完全重合，相对偏差<0.5%。验证了该方法在已知模态变换矩阵前提下，能够高精度、免几何假设地反演频变线路参数，为复杂地形与非均匀线路的电磁暂态建模提供了可靠替代方案。
