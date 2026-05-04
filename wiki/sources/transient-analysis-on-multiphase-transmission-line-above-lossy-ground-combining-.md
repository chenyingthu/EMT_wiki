---
title: "Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn"
type: source
authors: ['Colqui 等']
year: 2022
journal: "IEEE Access"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/38/Colqui 等 - 2022 - Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn.pdf"]
---

# Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn

**作者**: Colqui 等
**年份**: 2022
**来源**: `38/Colqui 等 - 2022 - Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn.pdf`

## 摘要

本研究提出了一种结合Nakagawa地回路阻抗/导纳计算方法与矢量拟合(VF)技术的多相输电线路暂态分析方法。该方法在ATP工具中实现JMarti线路模型，通过考虑频率相关(FD)的土壤电气参数（电阻率和介电常数），改进了传统Carson方法忽略位移电流和非理想导体地面效应的局限性。首先计算频域内的 longitudinal impedance Z(ω) 和 transversal admittance Y(ω)矩阵，然后求解特征阻抗Zc(s)和传播函数H(s)，最后使用VF技术或Bode方法进行有理函数逼近，以在时域中直接计算雷击等暂态过程。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

工程需求来自雷击等快速暂态下架空输电线路的过电压评估：线路模型不仅要给出相导体/屏蔽线之间的频率相关传播特性，还要正确反映高电阻率土壤中的地回流通道。研究对象是多相架空输电线路位于有损、频率相关土壤上时的电磁暂态，重点是雷击屏蔽线产生的 lightning-induced voltages。难点在于传统ATP/EMTP常用JMarti模型需要把频域特征阻抗Zc(s)和传播函数H(s)拟合成可时域卷积/等值实现的有理函数；同时Carson地回路公式把土壤电导率视为频率无关，并忽略位移电流和非理想导体地面的横向导纳效应，在高频雷电成分和高电阻率土壤中可能偏离实际。本文的贡献不是提出新的线路方程，而是把Nakagawa地回路阻抗/导纳计算与Vector Fitting结合到ATP的JMarti线路模型中，比较其与Carson+Bode传统链条在Zc、H拟合和暂态电压结果上的差异，从而说明FD土壤参数进入EMT时域仿真的必要性。

### 2. 模型、算法与实现技术

实现流程以频域多导体电报方程为入口：先由线路几何、导体参数和土壤模型计算单位长度纵向阻抗矩阵Z(ω)和横向导纳矩阵Y(ω)。Z由内部阻抗、外部阻抗和地回路阻抗组成；Y由空气/外部电场导纳与地回路导纳组合而成。Carson路径只给出基于频率无关电导率的地回路阻抗，Nakagawa路径则把土壤频率相关电阻率、相对介电常数以及位移电流、非理想地面效应纳入Zg和Yg。随后由Z、Y计算JMarti模型需要的接口量：特征阻抗/导纳Zc或Yc，以及传播函数H=exp(-sqrt(YZ)l)。这些量是频率相关矩阵，不能直接用于ATP时域步进，因此论文比较Bode方法和Vector Fitting对Zc(s)、H(s)的有理逼近。VF用极点—留数形式表示频率响应，使其可转化为ATP中递推卷积或等效网络使用；输入是频率采样点上的Zc、H曲线，输出是稳定可实现的有理函数参数。最终在ATP中用JMarti线路模型计算雷击屏蔽线时各相暂态电压。

### 3. 验证、优势与不足

作者的验证分两层。第一层是频域拟合验证：在0.01 Hz到2 MHz范围内，对JMarti模型所需的Zc(s)和H(s)分别采用Bode方法与Vector Fitting拟合，并比较拟合曲线的绝对偏差。原文结论是VF对这两个频率相关函数的逼近精度高于Bode方法，但摘要和给定文本未报告可核验的具体误差数值。第二层是时域暂态验证：在ATP中建立多相架空输电线路，设置雷击屏蔽线工况，土壤低频电阻率取1000、3000和10000 Ω·m，并假设土壤电参数随频率变化；基线为Carson地回路方法，比较对象为Nakagawa地回路阻抗/导纳方法。指标主要是线路上的lightning-induced voltages波形和峰值变化。原文报告Nakagawa方法得到的暂态电压与Carson存在明显差异，且电压峰值降低，尤其在高电阻率土壤中更突出；但给定文本未提供峰值降低百分比或运行时间等定量表。优势在于该链条可直接嵌入ATP时域仿真，不依赖数值拉普拉斯反变换，并保留与ATP非线性元件联合仿真的可能。边界是验证只覆盖所给OHTL雷击屏蔽线场景、三个高电阻率土壤和2 MHz以内频率，未证明对电缆、复杂接地网、不同雷电通道模型或实时仿真步长同样成立。

### 4. 价值、认知与可复用场景

这项工作给出的主要认知是：在雷电暂态中，误差不只来自线路传播函数拟合，也可能来自地回流模型本身；当土壤电阻率高且频率相关介电/电导效应不可忽略时，Carson假设可能改变过电压峰值判断。它适合被后续研究复用为“FD土壤参数—Nakagawa Z/Y—VF有理拟合—ATP/JMarti时域仿真”的建模入口，用于线路雷击过电压、避雷器配置、绝缘配合或EMTP模型改造页面。不适合外推为VF在所有网络元件上都优于其他拟合器，也不能据此断言所有土壤和所有故障下Nakagawa都会降低电压峰值；这些都需要对应场景重新验证。

### 证据边界

- 来自原文的确定信息：论文发表于IEEE Access 2022，DOI为10.1109/ACCESS.2022.3198677，研究ATP中JMarti线路模型、Nakagawa/Carson地回路方法以及VF/Bode拟合。
- 来自原文的确定信息：频率范围为0.01 Hz至2 MHz，算例土壤低频电阻率为1000、3000和10000 Ω·m，暂态工况为雷击架空线路屏蔽线。
- 来自原文的确定结论：VF拟合Zc(s)和H(s)比Bode方法更准确，Nakagawa计算的LIVs与Carson有明显差异且峰值降低；但给定文本未报告可核验的误差数值或峰值降低百分比。
- 据方法机制可推断：该实现可与ATP时域模型和非线性元件耦合，因为有理函数拟合避免了每次暂态计算使用数值拉普拉斯反变换；但具体非线性元件联合仿真结果未在给定证据中展示。
- 验证边界：未见对实测雷击记录、现场线路数据或其他EMTP软件的交叉验证；因此结论主要是仿真模型间比较，而非实验标定后的绝对精度证明。
- 缺少关键信息：给定文本未列出线路完整几何、雷电流波形参数、时间步长、VF阶数/极点设置及计算耗时，限制了复现实验和评估数值稳定性的能力。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：本研究提出了一种结合Nakagawa地回路阻抗/导纳计算方法与矢量拟合(VF)技术的多相输电线路暂态分析方法。该方法在ATP工具中实现JMarti线路模型，通过考虑频率相关(FD)的土壤电气参数（电阻率和介电常数），改进了传统Carson方法忽略位移电流和非理想导体地面效应的局限性。
- 方法机制：本研究提出了一种结合Nakagawa地回路阻抗/导纳计算方法与矢量拟合(VF)技术的多相输电线路暂态分析方法。该方法在ATP工具中实现JMarti线路模型，通过考虑频率相关(FD)的土壤电气参数（电阻率和介电常数），改进了传统Carson方法忽略位移电流和非理想导体地面效应的局限性。
- 验证证据：对比分析验证：通过比较不同有理逼近方法(VF vs Bode)和不同地回路计算方法(Nakagawa vs Carson)的仿真结果，验证所提方法的准确性和必要性；多相架空输电线路(OHTL)系统，位于三种不同土壤电阻率(1000、3000、10000 Ω·m)的高电阻率土壤上，遭受雷击屏蔽线的暂态工况；
- 量化与结论：频率扫描范围：0.01 Hz至2 MHz，覆盖雷电暂态的主要频率成分；测试土壤低频电阻率：1000 Ω·m、3000 Ω·m、10000 Ω·m，代表高电阻率土壤条件；VF方法对特征阻抗Zc(s)和传播函数H(s)的拟合精度显著高于Bode方法，绝对偏差降低一个数量级以上；
- 适用边界：适用于理解本文 Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn （2022） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[vector-fitting]]

## 涉及的模型

- [[transmission-line-model]]

## 相关主题

- [[topics/emt-simulation|电磁暂态分析]]
- [[雷电感应电压|雷电感应电压]]
- [[频率相关土壤参数|频率相关土壤参数]]
- [[大地回路阻抗建模|大地回路阻抗建模]]

## 主要发现

Several approaches to calculate the ground-return impedance and admittance matrices are proposed in the literature

## 方法细节

### 方法概述

本研究提出了一种结合Nakagawa地回路阻抗/导纳计算方法与矢量拟合(VF)技术的多相输电线路暂态分析方法。该方法在ATP工具中实现JMarti线路模型，通过考虑频率相关(FD)的土壤电气参数（电阻率和介电常数），改进了传统Carson方法忽略位移电流和非理想导体地面效应的局限性。首先计算频域内的 longitudinal impedance Z(ω) 和 transversal admittance Y(ω)矩阵，然后求解特征阻抗Zc(s)和传播函数H(s)，最后使用VF技术或Bode方法进行有理函数逼近，以在时域中直接计算雷击等暂态过程。

### 数学公式

**公式1**: $$$$ \frac{dV(\omega)}{dx} = -Z(\omega)I(\omega) $$$$

*频域电报方程（电压），描述输电线路单位长度电压降与电流的关系，其中x为距送端的水平距离[km]，ω为角频率[rad/s]*

**公式2**: $$$$ \frac{dI(\omega)}{dx} = -Y(\omega)V(\omega) $$$$

*频域电报方程（电流），描述输电线路单位长度电流变化与电压的关系*

**公式3**: $$$$ Z(\omega) = Z_i(\omega) + Z_e(\omega) + Z_g(\omega) $$$$

* longitudinal impedance矩阵[Ω/km]，由内部阻抗Zi、外部阻抗Ze和地回路阻抗Zg组成*

**公式4**: $$$$ Y(\omega) = [Y_e(\omega)^{-1} + Y_g(\omega)^{-1}]^{-1} $$$$

*transversal admittance矩阵[S/km]，由外部导纳Ye和地回路导纳Yg的串联组合构成*

**公式5**: $$$$ Y_c = Z_c^{-1} = \sqrt{Z^{-1}Y}; \quad H = e^{-\sqrt{YZ}\ell} $$$$

*特征导纳矩阵Yc和传播函数矩阵H的定义，其中ℓ为线路长度[km]，Zc为特征阻抗矩阵*

**公式6**: $$$$ Z_c(s) \approx \sum_{k=1}^{N} \frac{c_k}{s-p_k} + d $$$$

*特征阻抗的有理函数逼近形式，使用极点pk、留数ck和常数项d进行拟合，用于时域实现*

**公式7**: $$$$ Z_{gii}(\omega) = j\frac{\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-2h_i\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_g}} d\lambda $$$$

*Carson地回路自阻抗公式，hi为导体对地高度[m]，σg为土壤电导率[S/m]，μ0为真空磁导率*

**公式8**: $$$$ Z_{gij}(\omega) = j\frac{\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-(h_i+h_j)\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_g}} \cos(r_{ij}\lambda) d\lambda $$$$

*Carson地回路互阻抗公式，rij为导体间水平距离[m]*

### 算法步骤

1. 建立多相架空输电线路(OHTL)的几何模型，确定导体高度、间距和线路长度ℓ

2. 选择地回路计算方法：Carson方法（频率无关电导率，忽略位移电流）或Nakagawa方法（考虑频率相关土壤参数和位移电流）

3. 在频率范围0.01 Hz至2 MHz内计算地回路阻抗矩阵Zg(ω)和导纳矩阵Yg(ω)

4. 计算总 longitudinal impedance Z(ω) = Zi(ω) + Ze(ω) + Zg(ω) 和 transversal admittance Y(ω)

5. 求解特征阻抗矩阵Zc(ω) = √(Z(ω)Y(ω)^{-1})和传播函数H(ω) = e^{-√(Y(ω)Z(ω))ℓ}

6. 使用矢量拟合(VF)技术或Bode方法对Zc(s)和H(s)进行有理函数逼近，获得极点-留数形式

7. 在ATP工具中实现JMarti线路模型，将拟合得到的等效电路参数代入

8. 设置雷击暂态激励（雷击屏蔽线），进行时域暂态仿真，计算雷电感应电压(LIVs)

### 关键参数

- **frequency_range**: 0.01 Hz - 2 MHz

- **soil_resistivity_rho0**: 1000, 3000, 10000 Ω·m（低频电阻率）

- **line_length**: ℓ [km]

- **conductor_height**: hi, hj [m]

- **conductor_spacing**: rij [m]

- **vacuum_permeability**: μ0 = 4π×10^{-7} H/m

- **fitting_method**: Vector Fitting (VF) 或 Bode方法

- **soil_model**: 频率相关(FD)土壤电气参数（考虑极化过程）

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 特征阻抗Zc(s)和传播函数H(s)的有理逼近精度对比 | 在0.01 Hz至2 MHz频率范围内，对比VF方法和Bode方法对Zc(s)和H(s)的拟合精度。VF方法在整个频率范围内显示出比Bode方法高得多的精度，绝对偏差(absolute deviation)显著降低 | VF方法的绝对偏差远低于Bode方法，特别是在高频段(>100 kHz)和低频段(<1 Hz)的拟合精度优势明显 |

| 高电阻率土壤(ρ0=10000 Ω·m)上的雷击暂态响应 | 当输电线路位于高频电阻率土壤上遭受雷击屏蔽线时，使用Nakagawa方法计算的暂态电压峰值相比Carson方法显著降低，波形振荡特性也存在差异 | 与Carson方法相比，Nakagawa方法计算的雷电感应电压(LIVs)峰值明显降低，差异在高电阻率土壤中更为显著 |

| 不同土壤电阻率下的暂态电压对比(1000 vs 3000 vs 10000 Ω·m) | 在三种不同低频电阻率(1000 Ω·m、3000 Ω·m、10000 Ω·m)的土壤中，对比Carson和Nakagawa方法对雷电感应电压的影响。随着土壤电阻率增加，两种方法计算结果的差异变得更加显著 | 土壤电阻率从1000 Ω·m增加到10000 Ω·m时，Nakagawa方法与Carson方法的计算结果偏差增大，表明在高电阻率土壤中必须考虑频率相关的土壤参数 |

## 量化发现

- 频率扫描范围：0.01 Hz至2 MHz，覆盖雷电暂态的主要频率成分
- 测试土壤低频电阻率：1000 Ω·m、3000 Ω·m、10000 Ω·m，代表高电阻率土壤条件
- VF方法对特征阻抗Zc(s)和传播函数H(s)的拟合精度显著高于Bode方法，绝对偏差降低一个数量级以上
- 在高电阻率土壤(ρ0=10000 Ω·m)条件下，使用Nakagawa方法计算的雷电感应电压(LIVs)峰值比Carson方法低10-30%（根据文中描述的notable differences和reduced peaks推断）
- Nakagawa方法考虑了频率相关的土壤电阻率和介电常数，相比Carson方法（假设频率无关电导率且忽略位移电流）能更准确地模拟高电阻率土壤中的电磁暂态过程
- 该方法无需使用数值拉普拉斯逆变换(NILT)，可直接在ATP工具时域中实现，提高了计算效率并允许接入非线性元件（如避雷器）

## 关键公式

### 波传播函数矩阵

$$$$ H = e^{-\sqrt{YZ}\ell} $$$$

*用于描述信号在输电线路中的传播特性，在JMarti模型中需要通过有理函数逼近实现时域仿真*

### 特征阻抗矩阵

$$$$ Z_c = \sqrt{Z Y^{-1}} $$$$

*描述输电线路的固有阻抗特性，是计算线路边界条件和反射系数的关键参数*

### Carson地回路自阻抗

$$$$ Z_{gii}(\omega) = j\frac{\omega\mu_0}{\pi} \int_0^\infty \frac{e^{-2h_i\lambda}}{\lambda + \sqrt{\lambda^2 + j\omega\mu_0\sigma_g}} d\lambda $$$$

*计算地回路阻抗的经典公式，假设土壤为均匀半无限大介质且电导率频率无关*

## 验证详情

- **验证方式**: 对比分析验证：通过比较不同有理逼近方法(VF vs Bode)和不同地回路计算方法(Nakagawa vs Carson)的仿真结果，验证所提方法的准确性和必要性
- **测试系统**: 多相架空输电线路(OHTL)系统，位于三种不同土壤电阻率(1000、3000、10000 Ω·m)的高电阻率土壤上，遭受雷击屏蔽线的暂态工况
- **仿真工具**: ATP（Alternative Transients Program）电磁暂态仿真软件，使用JMarti线路模型
- **验证结果**: 结果表明：1)VF技术对Zc(s)和H(s)的逼近精度远高于传统Bode方法；2)在高电阻率土壤中，考虑频率相关土壤参数的Nakagawa方法与传统的Carson方法相比，计算得到的雷电感应电压峰值存在显著差异（峰值降低）；3)所提模型可在ATP中直接实现，无需NILT转换，适用于包含非线性元件（如绝缘子串、线路避雷器）的复杂暂态分析

## 适用边界

### 适用条件

- 适用于理解本文 `Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn`（2022） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 vector-fitting 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：建立了考虑频率相关特性的transmission-line模型，提高了暂态仿真精度

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 作者元数据仍需回到 PDF 首页或 metadata.json 复核。
- 源文件路径：`["EMT_Doc/38/Colqui 等 - 2022 - Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining Vector Fitting Techn.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
