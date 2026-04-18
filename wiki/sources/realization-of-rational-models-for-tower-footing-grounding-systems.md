---
title: "Realization of rational models for tower-footing grounding systems"
type: source
authors: ['Antonio', 'C.S.', 'Lima']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112222. doi:10.1016/j.epsr.2025.112222"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/33/Lima 等 - 2026 - Realization of rational models for tower-footing grounding systems.pdf"]
---

# Realization of rational models for tower-footing grounding systems

**作者**: Antonio, C.S., Lima
**年份**: 2025
**来源**: `33/Lima 等 - 2026 - Realization of rational models for tower-footing grounding systems.pdf`

## 摘要

Realization of rational models for tower-footing grounding systems$ a Universidade Federal do Rio de Janeiro, P.O. Box. 68504, 21945-970, Rio de Janeiro, RJ, Brazil A tower footing grounding system plays an essential role in lightning-related overvoltages. For time-domain analysis, using an Electromagnetic Transient (EMT) program, one typically has to resort to a rational approximation of the harmonic impedance or a frequency-dependent network equivalent (FDNE) for the

## 核心贡献



- 对比了接地系统有理逼近的两种拓扑结构在最小阶数表示方面的差异
- 探讨了有效长度对有理逼近实现的影响及其与模型阶数的关系

## 使用的方法


- [[nodal-analysis]]
- [[passivity]]

## 涉及的模型


- [[fdne]]
- [[network-equivalent]]
- [[transmission-line]]

## 相关主题


- [[harmonic]]
- [[frequency-dependent]]

## 主要发现



- 准确的频变网络等效（FDNE）在遵循有效长度时具有略高的数值鲁棒性
- 传统降阶方法在高频范围内精度不足，需采用新方法以实现最小阶数表示

## 方法细节

### 方法概述

本文采用改进的混合电磁模型(mHEM)建立杆塔接地系统的频域模型，通过两种拓扑结构实现有理逼近：直接谐波导纳(impedance/admittance)逼近和频变网络等效(FDNE)。首先利用mHEM计算接地系统的横向和纵向阻抗矩阵，组装等效节点导纳矩阵；然后采用Vector Fitting(VF)算法进行有理逼近，提出基于均方根误差(rms-error)的启发式阶数确定方法；最后通过主导极点(dominant pole)准则进行模型降阶，实现最小阶数表示。研究重点比较了两种拓扑在数值鲁棒性和模型阶数方面的差异，并分析了有效长度(effective length)对有理逼近实现的影响。

### 数学公式


**公式1**: $$$Z_{Tik} = \frac{\exp(-\gamma R)}{4\pi(\sigma+j\omega\varepsilon)} P_{ik}$$$

*横向互阻抗，描述电极i和k之间的横向电磁耦合，其中γ为传播常数，R为距离，Pik为几何积分项*


**公式2**: $$$Z_{Lik} = \frac{j\omega\mu \cos\phi \exp(-\gamma R)}{4\pi} P_{ik}$$$

*纵向互阻抗，描述沿电极纵向的电磁耦合，μ为磁导率，φ为电极间夹角*


**公式3**: $$$\mathbf{Y}_n = \mathbf{m}_A^T \cdot \mathbf{Z}_T^{-1} \cdot \mathbf{m}_A + \mathbf{m}_B \cdot \mathbf{Z}_L^{-1} \cdot \mathbf{m}_B$$$

*等效节点导纳矩阵，通过关联矩阵mA和mB将横向和纵向阻抗转换为节点导纳形式*


**公式4**: $$$Y_g(s) \approx Y_{fit}(s) = R_0 + \sum_{k=1}^{N} \frac{R_k}{s-p_k}$$$

*谐波导纳的有理函数逼近，N为逼近阶数，Rk为留数，pk为极点，可为实数或共轭复数对*


**公式5**: $$$e_{rms} = \sqrt{\frac{\sum_{m=1}^{N_s} |Y_g(s_m) - Y_{fit}(s_m)|^2}{N_s}} \cdot \min(|Y_g(s)|) \leq \frac{\min(|Y_g(s)|)}{1000}$$$

*均方根误差停止准则，用于确定有理逼近的阶数，要求相对误差小于0.1%*


**公式6**: $$$\arctan\left(\frac{r_{ir}}{p_{ir}}\right) \geq \xi$$$

*主导极点判别准则，其中rir为第i个极点留数的实部，pir为第i个极点的实部，ξ为预定义容差*


### 算法步骤

1. 基于mHEM建立接地系统几何模型，将电极分割为长度不超过λ/10的段（λ为土壤中最高频率10MHz对应的波长）

2. 计算横向阻抗矩阵ZT和纵向阻抗矩阵ZL，其中几何积分项Pik仅计算一次以提高效率

3. 利用镜像法处理空气-土壤界面，组装等效节点导纳矩阵Yn = mA^T·ZT^(-1)·mA + mB·ZL^(-1)·mB

4. 求解线性方程组Yn·V = In计算节点电压，其中In在接地极注入点(A-D节点)施加1/4A电流

5. 计算谐波阻抗Zg = VA(ω)/1A，获取谐波导纳Yg = Zg^(-1)

6. 初始化Vector Fitting算法，设置初始极点数为2，最大允许极点数为20

7. 在100Hz至10MHz频率范围内，使用250个对数间隔频率样本进行VF迭代

8. 检查均方根误差erms是否满足erms ≤ min(|Yg(s)|)/1000的停止准则，若不满足则增加极点数

9. 应用主导极点准则arctan(|rir/pir|) ≥ ξ筛选有效极点，剔除不满足条件的极点-留数对

10. 利用筛选后的极点集重新进行VF拟合，获得最终降阶模型

11. 对于FDNE拓扑，在得到节点导纳矩阵后，提取多端口网络参数进行有理逼近


### 关键参数

- **frequency_range**: 100 Hz to 10 MHz

- **frequency_samples**: 250 logarithmically spaced points

- **max_electrode_segment_length**: λ/10 (wavelength/10 at 10 MHz in soil)

- **soil_resistivity_cases**: 100 Ω·m (low) and 1000 Ω·m (high)

- **relative_permittivity**: 10

- **initial_poles**: 2

- **max_poles**: 20

- **final_model_order**: 11 poles after reduction

- **rms_error_tolerance**: min(|Yg(s)|)/1000 (0.1% relative error)

- **dominant_pole_tolerance**: ξ (pre-defined angle threshold in radians)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Low resistivity soil (ρ=100 Ω·m) with 30m counterpoise | 有理逼近阶数为11，均方根误差erms×10^-5=3.6925，实现了高精度拟合 | 相比初始40阶试探模型，降阶后减少约72.5%的极点数 |

| Low resistivity soil (ρ=100 Ω·m) with 60m counterpoise | 有理逼近阶数为11，均方根误差erms×10^-5=6.4058，满足精度要求 | 误差略高于30m场景但仍远低于0.1%容差 |

| High resistivity soil (ρ=1000 Ω·m) with 90m counterpoise | 有理逼近阶数为11，均方根误差erms×10^-5=2.7303，验证了高电阻率长电极配置的有效性 | 当电极长度接近或超过有效长度时，振荡行为降低，所需阶数保持较低水平 |

| High resistivity soil (ρ=1000 Ω·m) with 120m counterpoise | 有理逼近阶数为11，均方根误差erms×10^-5=2.2772，为所有测试案例中误差最低 | 验证了有效长度概念：当电极长度≥有效长度时，高频振荡减弱，模型更易收敛 |

| Disregarding effective length (short counterpoise in high ρ) | 当在高电阻率土壤(1000 Ω·m)中使用短于有效长度的counterpoise时，谐波导纳Y(ω)在高频呈现更强的振荡行为 | 需要显著高于11阶的模型才能实现同等精度，验证了有效长度对最小阶数实现的关键影响 |



## 量化发现

- 采用主导极点准则后，模型阶数减少近50%（从约20-40极点降至11极点）
- 最终模型在100 Hz至10 MHz范围内均满足erms ≤ min(|Yg|)/1000，即相对误差<0.1%
- 对于符合有效长度条件的配置，11阶有理模型可实现与详细电磁模型偏差至少三个数量级以内的精度
- 在1000 Ω·m高电阻率土壤中，90m和120m电极的拟合误差分别为2.7303×10^-5和2.2772×10^-5，优于低电阻率案例
- 当电极长度短于有效长度且土壤电阻率高时，谐波导纳在高频段呈现显著振荡，导致传统降阶方法失效
- FDNE拓扑在遵循有效长度原则时，相比直接阻抗逼近具有略高的数值鲁棒性


## 关键公式

### 有理函数逼近模型

$$$Y_g(s) \approx R_0 + \sum_{k=1}^{N} \frac{R_k}{s-p_k}$$$

*用于将频变谐波导纳转换为时域EMT程序可实现的有理模型，是本文两种拓扑结构（直接导纳逼近和FDNE）的基础*

### 等效节点导纳矩阵

$$$\mathbf{Y}_n = \mathbf{m}_A^T \cdot \mathbf{Z}_T^{-1} \cdot \mathbf{m}_A + \mathbf{m}_B \cdot \mathbf{Z}_L^{-1} \cdot \mathbf{m}_B$$$

*基于mHEM方法，将分段电极的横向和纵向阻抗转换为节点导纳矩阵，用于计算接地系统的谐波响应*

### 主导极点筛选准则

$$$\arctan\left(\frac{r_{ir}}{p_{ir}}\right) \geq \xi$$$

*模型降阶关键步骤，通过剔除留数实部与极点实部比值过小的极点，实现最小阶数表示而不损失精度*



## 验证详情

- **验证方式**: 对比验证（与mHEM计算的基准频响对比）
- **测试系统**: Counterpoise接地配置（图2所示），包含四根放射状水平接地极，测试长度30m、60m、90m、120m；土壤电阻率100 Ω·m和1000 Ω·m；相对介电常数εr=10
- **仿真工具**: mHEM（modified Hybrid Electromagnetic Model）用于基准计算；Vector Fitting算法用于有理逼近；ATP/EMTP/PSCAD类EMT程序为最终目标实现平台
- **验证结果**: 所有测试案例在100Hz-10MHz范围内，11阶有理模型与mHEM基准的均方根误差均小于6.5×10^-5（相对误差<0.1%）。验证了在高电阻率土壤中，当电极长度≥有效长度时，11阶模型即可准确捕捉接地系统频变特性；若忽视有效长度，则需要显著更高阶数。FDNE拓扑在保持有效长度时表现出略优的数值鲁棒性。
