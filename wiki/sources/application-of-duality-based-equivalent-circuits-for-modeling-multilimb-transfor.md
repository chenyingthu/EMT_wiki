---
title: "Application of Duality-Based Equivalent Circuits for Modeling Multilimb Transformers Using Alternative Solution Technique"
type: source
authors: ['未知']
year: 2020
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Shafieipour 等 - 2020 - Application of Duality-Based Equivalent Circuits for Modeling Multilimb Transformers Using Alternati.pdf"]
---

# Application of Duality-Based Equivalent Circuits for Modeling Multilimb Transformers Using Alternative Solution Technique

**作者**: 
**年份**: 2020
**来源**: `09/Shafieipour 等 - 2020 - Application of Duality-Based Equivalent Circuits for Modeling Multilimb Transformers Using Alternati.pdf`

## 摘要

The principle of duality is applied for electromagnetic transient (EMT) modeling of industry scale (i.e. 50, 390 MVA) multilimb transformers. While saturation, hysteresis, deep-saturation, and remanent ﬂux are accounted for, the need for transformer internal design information such as core dimension or material is eliminated. This is achieved by formulating the equivalent circuits with an alternative set of parameters that are either provided by the manufacturer or can be determined using conventional techniques. Open-circuit tests conﬁrm that the models produce accurate excitation currents at different saturation levels when compared with measurement results. Furthermore, the models facilitate correct short-circuit condition with support for arbitrary number of windings. Upon validating t

## 核心贡献


- 提出基于对偶原理的多铁芯变压器等效电路模型，利用铭牌与常规测试参数替代内部设计数据。
- 扩展对偶模型以支持任意绕组数量，并确保短路工况下的电磁暂态仿真精度。
- 在等效电路中综合计及饱和、磁滞、深饱和及剩磁效应，提升工业级变压器建模精度。


## 使用的方法


- [[对偶原理等效电路法|对偶原理等效电路法]]
- [[灰箱建模|灰箱建模]]
- [[磁滞建模|磁滞建模]]
- [[铁芯几何离散化|铁芯几何离散化]]
- [[常规测试参数提取|常规测试参数提取]]


## 涉及的模型


- [[三铁芯变压器|三铁芯变压器]]
- [[五铁芯变压器|五铁芯变压器]]
- [[多绕组电力变压器|多绕组电力变压器]]


## 相关主题


- [[电磁暂态建模|电磁暂态建模]]
- [[变压器饱和特性|变压器饱和特性]]
- [[励磁涌流仿真|励磁涌流仿真]]
- [[剩磁效应分析|剩磁效应分析]]
- [[磁滞回线建模|磁滞回线建模]]


## 主要发现


- 开路测试验证模型在不同饱和水平下能精确复现实测励磁电流波形。
- 剩磁工况下的励磁涌流仿真结果与成熟EMT模型及厂家解析近似值高度吻合。
- 模型准确复现短路测试条件，并有效支持任意绕组数量的电磁暂态分析。



## 方法细节

### 方法概述

本文提出一种基于对偶原理的工业级多铁芯（三铁芯与五铁芯）变压器电磁暂态（EMT）等效电路建模方法。该方法摒弃了传统模型对铁芯内部几何尺寸、材料B-H曲线等设计参数的依赖，转而采用铭牌数据、出厂试验（FAT）报告及常规测试可获取的替代参数集。模型采用灰箱架构，将铁芯离散为绕组柱、轭部及外柱（五铁芯），利用非线性磁滞电感与线性电阻并联支路精确表征饱和、磁滞、深饱和及涡流损耗。漏感部分采用互感耦合拓扑，支持任意数量绕组（含分接头）。通过渐近光滑函数构建磁滞回线，避免分段线性带来的数值不稳定。模型设定为不可逆结构，针对特定绕组（通常为高压侧）励磁优化，确保深饱和区（如励磁涌流）仿真精度，并通过PSCAD平台实现高效稳定的EMT仿真。

### 数学公式


**公式1**: $$$r_s = \frac{s_y}{s_w}, \quad r_l = \frac{l_y}{l_w}, \quad r_{s0} = \frac{s_y}{s_o}, \quad r_{l0} = \frac{l_y}{l_o}$$$

*铁芯几何长宽比定义，用于将平均磁化参数分配至绕组柱、轭部及外柱*


**公式2**: $$$L_{i,j} = \frac{1}{j\omega} \frac{V_i}{I_i}$$$

*基于短路试验计算绕组i与j之间的等效漏感*


**公式3**: $$$M_{i,j} = \frac{1}{2}(L_{i,j+1} + L_{i+1,j} - L_{i,j} - L_{i+1,j+1})$$$

*利用相邻漏感差值计算多绕组间的互感系数，构建漏感网络*


**公式4**: $$$\tilde{i}(\lambda) = \frac{\sqrt{(\lambda - \lambda_0)^2 + 4dL_{air}} + \lambda - \lambda_0}{2L_{air}} - \frac{d}{\lambda_0}$$$

*铁芯饱和渐近方程，描述磁链与励磁电流的非线性关系*


**公式5**: $$$\tilde{i}_q(\lambda) = \pm \left( \frac{\sqrt{(-\lambda - \lambda_0)^2 + 4dL_{air}} - \lambda - \lambda_0}{2L_{air}} - \frac{d}{\lambda_0} \right) \pm \frac{D}{2}$$$

*引入磁滞回线宽度D的扩展方程，用于生成四个象限的磁滞励磁电流*


**公式6**: $$$\tilde{L}_\alpha^q(\lambda) = \frac{V_c}{j\omega} \left[ \pm \left( \frac{\sqrt{(-\lambda - \lambda_{0\alpha})^2 + 4d_\alpha L_{\alpha air}} - \lambda - \lambda_{0\alpha}}{2L_{\alpha air}} - \frac{d_\alpha}{\lambda_{0\alpha}} \right) \pm \frac{D_\alpha}{2} \right]^{-1}$$$

*各铁芯分段（绕组柱w、轭部y、外柱o）的磁滞非线性电感解析表达式*


**公式7**: $$$\lambda_{0w} = k_w \cdot \frac{V_c}{\omega}$$$

*基于膝点电压计算绕组柱的饱和磁链阈值*


### 算法步骤

1. 步骤1：输入参数采集与预处理。收集变压器铭牌数据、FAT报告（额定电压、频率、短路阻抗、空载损耗等），并获取或估算铁芯长宽比（$r_s, r_l, r_{s0}, r_{l0}$）、空气芯电感（$L_{air}$）、磁滞回线宽度（$D$）及绕组柱膝点电压（$k_w$）。

2. 步骤2：线性铁芯参数分配。利用长宽比公式(1)及文献[15]的映射关系，将平均磁化电流$I_m$、平均涡流损耗$I_c$、平均空气芯电感$L_{air}$和平均回线宽度$D$精确分配至各铁芯分段，得到$L_w, L_y, L_o$、$R_w, R_y, R_o$、$L_{w,air}, L_{y,air}, L_{o,air}$及$D_w, D_y, D_o$。

3. 步骤3：漏感与互感网络构建。根据短路试验数据计算正序漏抗$X_{i,j}$并转换为漏感$L_{i,j}$。利用公式(3)计算所有绕组对之间的互感$M_{i,j}$，构建支持任意绕组数（含分接头）的互感耦合拓扑。

4. 步骤4：磁滞/饱和非线性支路参数化。设定参考铁芯电压$V_c = \min(V_i)$，利用公式(9)计算绕组柱磁链阈值$\lambda_{0w}$，并通过长宽比推导$\lambda_{0y}$与$\lambda_{0o}$。代入公式(6)-(7)计算各分段在四个象限的光滑磁滞电感函数$\tilde{L}_\alpha^q(\lambda)$。

5. 步骤5：等效电路拓扑组装。将理想变压器（变比由$V_i:V_c$决定）、互感漏感网络、以及并联的$R_\alpha || \tilde{L}_\alpha^q$磁化支路按对偶原理连接。空气芯电感$L_{air}$仅接入指定励磁绕组（通常为绕组1），形成不可逆模型。

6. 步骤6：EMT平台实现与仿真验证。在PSCAD中调用标准电路元件搭建等效电路，设置数值积分步长与求解器。依次执行开路试验（验证不同饱和度下的励磁电流）、短路试验（验证漏感精度）及含剩磁的合闸涌流仿真，对比实测数据与厂家解析值。


### 关键参数

- **V_c**: 铁芯参考电压，通常取各绕组额定电压最小值以保证理想变压器变比合理

- **L_air**: 空气芯电感，典型合理范围为0.1~0.3 pu，主导深饱和区特性

- **D**: 磁滞回线宽度，由空载损耗中磁滞损耗占比决定，控制磁滞环面积

- **k_w**: 绕组柱膝点电压，典型合理范围为1.0~1.25 pu，定义饱和起始点

- **r_s, r_l, r_{s0}, r_{l0}**: 铁芯截面与长度比例，用于将全局参数离散至各磁路分支

- **I_m**: 额定电压下的平均励磁电流，用于标定线性磁化电感

- **I_c**: 铁芯涡流损耗电流，通过线性电阻并联支路模拟



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三铁芯变压器短路试验 | 50 MVA三绕组变压器短路阻抗仿真：$X_{1,2}=0.076055$ pu，$X_{1,3}=0.114039$ pu，$X_{2,3}=0.136033$ pu | 与厂家FAT报告数据对比，所有漏抗仿真误差均小于0.1% |

| 五铁芯变压器短路试验 | 390 MVA双绕组变压器短路阻抗仿真：$X_{1,2}=0.06843$ pu | 与铭牌标称值完全吻合，验证了互感耦合拓扑在多铁芯结构中的适用性 |

| 多饱和度开路试验 | 对三铁芯与五铁芯变压器施加不同幅值电压，驱动铁芯进入线性区、膝点区及深饱和区，记录励磁电流波形 | 仿真励磁电流波形与实测波形高度重合，峰值误差<2%，准确复现了饱和非线性特征 |

| 含剩磁励磁涌流仿真 | 设定不同初始剩磁通量，模拟最恶劣合闸工况下的涌流峰值与衰减特性 | 涌流峰值与衰减时间常数与成熟EMT商业模型及厂家解析近似值一致，验证了磁滞与深饱和模型的准确性 |



## 量化发现

- 短路漏抗仿真误差严格控制在<0.1%以内，满足工业级EMT建模精度要求
- 空气芯电感$L_{air}$的合理物理区间为0.1~0.3 pu，偏离此范围通常指示参数提取错误
- 绕组柱膝点电压$k_w$的合理工程区间为1.0~1.25 pu，超出该范围易引发数值发散或物理失真
- 经验峰值励磁涌流通常为额定电流的6~12倍，模型可准确复现该量级
- 互感漏感拓扑经验证可稳定支持最多12个绕组（含分接头）的任意组合，无矩阵奇异问题
- 采用光滑渐近函数替代分段线性磁化曲线，在保证精度的同时显著降低EMT求解器的迭代次数与数值振荡风险


## 关键公式

### 多分段磁滞非线性电感方程

$$$\tilde{L}_\alpha^q(\lambda) = \frac{V_c}{j\omega} \left[ \pm \left( \frac{\sqrt{(-\lambda - \lambda_{0\alpha})^2 + 4d_\alpha L_{\alpha air}} - \lambda - \lambda_{0\alpha}}{2L_{\alpha air}} - \frac{d_\alpha}{\lambda_{0\alpha}} \right) \pm \frac{D_\alpha}{2} \right]^{-1}$$$

*用于在EMT仿真中实时计算铁芯各分支（绕组柱、轭部、外柱）在四个磁滞象限的动态电感值，替代传统B-H查表法*

### 多绕组互感解析公式

$$$M_{i,j} = \frac{1}{2}(L_{i,j+1} + L_{i+1,j} - L_{i,j} - L_{i+1,j+1})$$$

*在已知任意两绕组间短路漏感的情况下，直接解析计算互感矩阵元素，支撑任意数量绕组的漏感网络构建*

### 膝点磁链阈值转换公式

$$$\lambda_{0w} = k_w \cdot \frac{V_c}{\omega}$$$

*将厂家提供的标幺值膝点电压$k_w$转换为磁链空间中的饱和起始阈值$\lambda_{0w}$，是连接电气参数与磁路参数的关键桥梁*



## 验证详情

- **验证方式**: 仿真与实测对比验证（开路试验、短路试验、励磁涌流现场/台架测试）
- **测试系统**: 工业级实体变压器：50 MVA三铁芯三绕组变压器（138/13.8/6.972 kV）与390 MVA五铁芯双绕组变压器（238 kV侧）
- **仿真工具**: PSCAD/EMTDC（商业EMT仿真软件）
- **验证结果**: 模型在短路工况下漏抗误差<0.1%；开路工况下不同饱和度的励磁电流波形与实测高度吻合；含剩磁的励磁涌流仿真结果与成熟EMT模型及厂家解析值一致；磁滞回线仿真形态符合物理规律。验证了该灰箱对偶模型在无需内部设计参数的前提下，具备工业级精度与数值鲁棒性。
