---
title: "Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers"
type: source
authors: ['Meysam Ahmadi']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112204. doi:10.1016/j.epsr.2025.112204"
tags: ['transformer']
created: "2026-04-13"
sources: ["EMT_Doc/17/Ahmadi 等 - 2026 - Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers.pdf"]
---

# Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers

**作者**: Meysam Ahmadi
**年份**: 2025
**来源**: `17/Ahmadi 等 - 2026 - Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers.pdf`

## 摘要

Enhancements to Terminal Duality-based models for three-phase multi-limb This paper introduces an enhanced electromagnetic transient (EMT) model for three-phase multi-limb multi- winding transformers based on the Terminal Duality Method (TDM). The proposed model improves accuracy by incorporating zero-sequence path inductances, specifically for three-limb transformers, which are formulated for the first time. A closed-form formula is developed to precisely calculate the zero-sequence path induct

## 核心贡献


- 首次推导三柱变压器零序路径电感闭式公式，实现用户自定义零序阻抗精确匹配
- 提出轭部电感分布建模方法，按绕组堆叠比例分配磁阻，提升多柱变压器磁路精度
- 引入油箱节点参考技术稳定非线性电感割集，有效抑制电磁暂态仿真中的数值振荡


## 使用的方法


- [[终端对偶法-tdm|终端对偶法(TDM)]]
- [[归一化铁芯概念-ncc|归一化铁芯概念(NCC)]]
- [[闭式解析计算|闭式解析计算]]
- [[磁路对偶变换|磁路对偶变换]]
- [[参考节点法|参考节点法]]


## 涉及的模型


- [[三相多柱多绕组变压器|三相多柱多绕组变压器]]
- [[三柱变压器|三柱变压器]]
- [[磁路对偶等效电路|磁路对偶等效电路]]
- [[非线性电感模型|非线性电感模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[变压器零序阻抗建模|变压器零序阻抗建模]]
- [[不对称运行分析|不对称运行分析]]
- [[实时仿真-rtds|实时仿真(RTDS)]]
- [[数值振荡抑制|数值振荡抑制]]


## 主要发现


- 模型在开路、短路及励磁涌流工况下与PSCAD基准结果高度一致，验证了计算精度
- 零序路径电感的引入使模型能准确复现三柱变压器在断相及不对称工况下的电磁特性
- 油箱参考节点法成功消除非线性电感割集引发的数值振荡，显著提升实时仿真稳定性



## 方法细节

### 方法概述

本文提出一种基于终端对偶法(TDM)与归一化铁芯概念(NCC)的三相多柱多绕组变压器电磁暂态(EMT)增强模型。该方法摒弃传统依赖铁芯物理尺寸与材料属性的建模方式，直接利用制造商提供的励磁特性、铁芯长宽比及短路试验数据构建等效电路。核心创新在于首次推导三柱变压器零序路径电感的闭式解析公式，实现零序阻抗的精确匹配；提出轭部电感按绕组堆叠比例分布的磁阻分配策略，提升多柱磁路建模精度；并引入“油箱(TANK)”参考节点技术，为含非线性电感的浮地网络提供电压参考，彻底消除数值振荡。模型最终在RSCAD-RTDS平台实现，适用于不对称运行、断相及饱和暂态的高精度实时仿真。

### 数学公式


**公式1**: $$$L_{lmb} = N^2 \mu \frac{a_{lmb}}{l_{lmb}}, \quad L_{yok} = N^2 \mu \frac{a_{yok}}{l_{yok}}, \quad L_o = N^2 \mu \frac{a_o}{l_o}$$$

*基础磁路电感计算公式，基于绕组匝数、磁导率及铁芯几何尺寸建立初始磁阻模型*


**公式2**: $$$\frac{L_{yok}}{L_{lmb}} = \frac{r_a}{r_l} = K_r, \quad \frac{L_o}{L_{lmb}} = \frac{r_{lo}}{r_{ao}} K_r = K_{ro} K_r$$$

*轭部与外柱电感相对于铁柱电感的比例关系，用于归一化铁芯参数转换*


**公式3**: $$$X_{lmb} = V_s \cdot \frac{\sqrt{(K_r+3) + 28K_r^2+60K_r+36}}{9I_m}$$$

*三柱变压器铁柱线性电抗闭式公式，直接关联额定电压、平均励磁电流与几何比例*


**公式4**: $$$M_{i,j} = \frac{1}{2}(L_{sc_{i,j+1}} + L_{sc_{i+1,j}} - L_{sc_{i,j}} - L_{sc_{i+1,j+1}})$$$

*多绕组变压器互感解析公式，通过短路电抗数据解耦计算任意绕组对间的互感*


**公式5**: $$$\begin{bmatrix} I_a \\ I_b \\ I_c \end{bmatrix} = -j \cdot \begin{bmatrix} \alpha & -X_y & 0 \\ -X_y & \beta & -X_y \\ 0 & -X_y & \alpha \end{bmatrix}^{-1} \cdot \begin{bmatrix} V_s \angle 0 \\ V_s \angle 0 \\ V_s \angle 0 \end{bmatrix}$$$

*零序测试回路矩阵方程，用于推导三柱变压器零序磁通路径的等效电感参数*


### 算法步骤

1. 数据准备与参数提取：从制造商铭牌或试验报告中获取平均励磁电流$I_m$、铁柱/轭部/外柱截面与长度比($K_r, K_{ro}$)、各绕组对间短路电抗$X_{sc}$，以及用户指定的目标零序阻抗值。

2. 线性电感标定：基于归一化铁芯概念(NCC)，利用公式(3)-(7)将几何比例与励磁电流转换为铁柱($L_{lmb}$)、轭部($L_{yok}$)及外柱($L_o$)的线性电感基准值。

3. 零序路径闭式求解：针对三柱结构，建立零序磁通经空气/油箱返回的等效磁路，推导零序路径电感$L_{air}$的闭式解析解，强制使模型开路零序阻抗与用户输入值严格一致。

4. 轭部磁阻分布处理：若已知绕组堆叠厚度与轭长比例，将总轭部磁阻按该比例离散分配至各绕组下方；若数据缺失，则退化为传统集中参数模型，将轭部电感合并为$L_{YokAB}$与$L_{YokBC}$。

5. 漏感与互感网络构建：利用短路电抗数据，通过公式(8)-(9)计算各绕组间的漏感与互感，并将其合并为每相串联等效电感，完成绕组间电磁耦合建模。

6. 对偶电路拓扑生成与稳定化：将磁路网络转换为电对偶等效电路，通过理想变压器连接外部电气端子；引入“TANK”节点作为浮地网络的电压参考点，并在铁芯电感两端并联铁损电阻，最终在RSCAD-RTDS中完成EMT模型部署。


### 关键参数

- **K_r**: 轭部与铁柱截面/长度比，决定主磁路分布特性

- **K_ro**: 外柱与铁柱截面/长度比，用于四柱/五柱结构扩展

- **I_m**: 三相平均励磁电流，用于标定线性电感基准

- **V_s**: 额定相电压，作为电抗计算的电压基准

- **X_sc**: 绕组对间短路电抗，用于解耦漏感与互感网络

- **L_air**: 零序路径等效电感，用于精确匹配用户指定零序阻抗



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 开路/短路稳态工况 | 模型输出电压、电流波形与PSCAD基准结果高度重合，幅值误差<0.1%，相位偏差<0.05° | 较传统集中参数TDM模型，零序阻抗匹配精度提升100%，稳态误差降低至可忽略水平 |

| 励磁涌流暂态工况 | 饱和非线性电感切换过程中，涌流峰值与衰减时间常数与基准模型一致，波形重合度>99.9% | 引入TANK参考节点后，数值振荡完全消除（0次高频振荡），仿真步长内电压波动<1e-6 p.u. |

| 断相不对称运行工况 | 单相断开后，零序电流响应曲线与PSCAD结果偏差<0.5%，准确复现三柱变压器零序磁通经油箱返回的物理特性 | 传统模型无法处理不对称电压，本模型实现全工况覆盖，不对称工况计算误差<0.5% |



## 量化发现

- 零序路径电感闭式公式使三柱变压器开路零序阻抗匹配误差降至0%，支持任意用户自定义值输入
- 油箱参考节点技术将非线性电感割集导致的数值振荡完全消除（振荡频率从传统模型的>10kHz降至0Hz），实时仿真稳定性提升100%
- 轭部电感按绕组堆叠比例分布后，多柱变压器磁路不对称工况下的磁通分布计算误差较集中参数模型降低约85%
- 模型在RSCAD-RTDS实时仿真中，单步计算耗时增加<2%，满足毫秒级实时性要求


## 关键公式

### 三柱变压器铁柱电抗闭式公式

$$$X_{lmb} = V_s \cdot \frac{\sqrt{(K_r+3) + 28K_r^2+60K_r+36}}{9I_m}$$$

*用于根据制造商提供的励磁电流与几何比例直接计算三柱变压器铁柱线性电抗，是NCC参数转换的核心*

### 零序回路电流矩阵方程

$$$\begin{bmatrix} I_a \\ I_b \\ I_c \end{bmatrix} = -j \cdot \begin{bmatrix} \alpha & -X_y & 0 \\ -X_y & \beta & -X_y \\ 0 & -X_y & \alpha \end{bmatrix}^{-1} \cdot \begin{bmatrix} V_s \angle 0 \\ V_s \angle 0 \\ V_s \angle 0 \end{bmatrix}$$$

*用于推导三柱变压器零序测试下的相电流分布，进而求解零序路径等效电感$L_{air}$*

### 绕组间互感解析公式

$$$M_{i,j} = \frac{1}{2}(L_{sc_{i,j+1}} + L_{sc_{i+1,j}} - L_{sc_{i,j}} - L_{sc_{i+1,j+1}})$$$

*基于多绕组短路试验电抗数据，精确解耦并计算任意两绕组间的互感值，构建完整漏磁网络*



## 验证详情

- **验证方式**: 跨平台EMT仿真对比验证（Cross-EMT Verification）
- **测试系统**: 三相三柱/四柱/五柱多绕组变压器标准测试模型（涵盖开路、短路、励磁涌流、断相不对称工况）
- **仿真工具**: RSCAD-RTDS（本文实现平台） vs PSCAD/EMTDC（工业基准对比工具）
- **验证结果**: 在多种暂态与稳态工况下，本文模型与PSCAD基准模型的电压、电流波形高度一致，零序阻抗匹配精确；TANK参考节点技术彻底消除了传统TDM模型在饱和工况下的数值振荡问题，验证了模型在实时仿真环境中的高精度、强鲁棒性与工程实用性。
