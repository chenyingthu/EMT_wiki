---
title: "Accuracy assessment of analytical expressions for the ground return impedance of underground cables"
type: source
authors: ['Alberto', 'De', 'Conti']
year: 2025
journal: "Electric Power Systems Research"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/De Conti和Lima - 2026 - Accuracy assessment of analytical expressions for the ground return impedance of underground cables.pdf"]
---

# Accuracy assessment of analytical expressions for the ground return impedance of underground cables

**作者**: Alberto, De, Conti
**年份**: 2025
**来源**: `05/De Conti和Lima - 2026 - Accuracy assessment of analytical expressions for the ground return impedance of underground cables.pdf`

## 摘要

本文采用频域误差分析与时域电磁暂态仿真相结合的方法，系统评估两种地回路阻抗闭式近似公式（Saad-Gaba-Giroux与De Conti-Lima）的计算精度。首先，基于准TEM场传播理论，以Sunde积分方程（忽略位移电流）和Xue-Magalhães积分方程（完整准TEM模型）为基准，在10 Hz至10 MHz宽频带内计算双回路地下电缆系统的互阻抗。通过引入恒定参数（CP）与Alipio-Visacro频变（FD）土壤模型，结合不同回路间距（1~3 m），计算平均绝对百分比误差（MAPE）。随后，利用矢量拟合技术将频域参数转换为有理函数，嵌入ATP的通用线路模型（ULM）进行时域仿真。通过对比单位阶跃地模激励下的护套与线芯电压波形，并计算总均方根误差（RMS），验证闭式公式在宽频带、大间距及不同电缆长度下的暂态仿真稳定性与精度。


<!-- deep-review:start -->
## 研究解读

### 1. 需求、对象、挑战与贡献

地下电缆EMT宽频建模需要反复计算单位长度地回路阻抗；对双回路电缆，回路间距较大、频率跨度可到准TEM适用上限约10 MHz，若每个频点都求Sunde或Xue–Magalhães型无穷积分，工程工具实现和宽频矢量拟合都很不方便。研究对象是地下电缆导体/护套之间的地回路互阻抗，重点比较Saad–Gaba–Giroux闭式式和De Conti–Lima闭式式。难点在于：传统闭式式最初面向近距离电缆和低频Pollaczek/Carson类近似，未必适合双回路宽间距；而完整准TEM积分式虽更严格，却计算成本高且涉及土壤参数不确定性。本文贡献不是提出新的暂态模型，而是把两类闭式式放到同一频域与时域框架中，针对宽间距双回路电缆、恒定与频变土壤参数，评估它们能否替代积分基准用于EMT电缆参数计算。

### 2. 模型、算法与实现技术

论文围绕地回路阻抗的频域计算接口展开：输入为电缆几何位置、导体间距、埋深、频率、土壤电阻率/介电参数及其频变模型；输出为频率相关的单位长度阻抗矩阵，随后供宽频线路模型使用。基准模型包括Sunde积分方程以及更完整的Xue–Magalhães准TEM积分方程，后者保留空气与土壤传播常数相关项，用于检验忽略位移电流或近似积分带来的偏差。Saad–Gaba–Giroux式用简单闭式项近似地回流积分，机制上以较低计算复杂度替代无穷积分，但其推导适用范围偏向小间距。De Conti–Lima式则以更高阶的解析近似表示Sunde积分中的空间衰减与间距影响，目标是在更宽频率和更大电缆间距下保持与积分式一致。实现流程是：在选定频点生成不同公式的阻抗矩阵，计算相对误差/MAPE；再将频域阻抗、导纳数据通过矢量拟合转为有理函数，导入EMT通用线路模型进行时域阶跃响应比较。

### 3. 验证、优势与不足

作者的验证分两层。频域层面，以Sunde积分式和Xue–Magalhães准TEM积分式为基线，对双回路地下电缆配置在10 Hz至10 MHz范围内计算地回路阻抗，改变回路间距和土壤模型，并用幅值/相位误差及MAPE评价闭式式。页面抽取结果称，De Conti–Lima式相对Sunde基准在10 MHz内误差较低，而Saad–Gaba–Giroux式在高电阻率土壤、宽间距和高频端误差明显增大；相对Xue–Magalhães基准时，De Conti–Lima仍会因Sunde模型本身未完整保留位移电流效应而出现高频系统偏差。时域层面，作者将频域参数矢量拟合后用于ATP/ULM类线路模型，对单位阶跃地模激励下的护套和线芯电压进行比较，并用RMS误差评价。优势主要体现在：闭式计算避免无穷积分，更适合大量频点的宽频电缆参数生成；De Conti–Lima式在双回路宽间距场景中比传统Saad–Gaba–Giroux式更稳健。从验证范围看，结论限定于论文给出的电缆布置、土壤参数、频率上限和准TEM线路理论，未证明可直接推广到任意敷设方式、强非均匀土壤或超过10 MHz的电磁场问题。

### 4. 价值、认知与可复用场景

这项工作给EMT建模者的核心启示是：地回路阻抗公式的选择不仅影响频域参数误差，还可能影响矢量拟合质量和时域暂态稳定性；不能因为某闭式式已被工具采用，就默认它适合双回路宽间距和高频暂态。它可作为后续地下电缆宽频参数计算、ULM/FD-line建模、土壤参数敏感性分析和工具公式替换评估的入口页。适合复用的是“闭式式—积分基准—频域误差—矢量拟合—时域波形”的验证范式。不适合外推为对所有电缆EMT问题的通用精度保证，尤其不应替代对具体电缆结构、接地方式、土壤分层和目标频带的重新校核。

### 证据边界

- 原文摘要和引言明确说明研究对象为地下电缆地回路阻抗，比较Saad–Gaba–Giroux与De Conti–Lima闭式表达式，并以Sunde、Xue–Magalhães积分方程为参照；这是直接证据。
- 10 MHz作为准TEM传播实际有效上限来自原文摘要；超过该频率范围的结论不应由本页外推。
- 页面中关于具体MAPE、RMS、100 m/1 km电缆和ATP/ULM的数值描述来自当前抽取页整理；若用于正式引用，应回查原文表格和图中对应数值。
- 原文已指出土壤参数不确定性比地下回路其他因素更突出，但本页未提供现场实测土壤或实测暂态波形校验；验证主要是模型间比较和仿真比较。
- 本文比较的闭式式不包括所有工程工具常用近似；引言提到Wedepohl–Wilcox和ATP/LCC背景，但当前证据未显示其被纳入同等完整的频域/时域对比。
- 元数据中作者字段不完整；原文首页显示作者为Alberto De Conti和Antonio C.S. Lima，引用时应以原文首页和DOI信息为准。
<!-- deep-review:end -->
## 核心贡献

- 问题定位：本文采用频域误差分析与时域电磁暂态仿真相结合的方法，系统评估两种地回路阻抗闭式近似公式（Saad-Gaba-Giroux与De Conti-Lima）的计算精度。
- 方法机制：本文采用频域误差分析与时域电磁暂态仿真相结合的方法，系统评估两种地回路阻抗闭式近似公式（Saad-Gaba-Giroux与De Conti-Lima）的计算精度。首先，基于准TEM场传播理论，以Sunde积分方程（忽略位移电流）和Xue-Magalhães积分方程（完整准TEM模型）为基准，在10 Hz至10 MHz宽频带内计算双回路地下电缆系统的互阻抗。
- 验证证据：频域误差分析（MAPE计算）结合时域电磁暂态仿真（ULM模型对比）；双回路地下电缆系统（共6根电缆，每回路3根，典型水平排列），回路间距1~3 m，电缆长度100 m与1 km；MATLAB（频域计算、矢量拟合）、ATP/ATPDraw（通用线路模型ULM时域仿真）
- 量化与结论：De Conti-Lima公式在10 MHz内相对Sunde方程的最大误差<2.5%，即使回路间距达3 m仍保持高精度。；Saad-Gaba-Giroux公式在1000 Ωm土壤中10 MHz频带内误差>20%，频变土壤下误差峰值>50%。；
- 适用边界：适用于理解本文 Accuracy assessment of analytical expressions for the ground return impedance of underground cables （2025） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。；

## 使用的方法

- [[闭式近似公式|闭式近似公式]]
- [[积分方程法|积分方程法]]
- [[误差分析|误差分析]]
- [[emt-simulation|电磁暂态仿真]]
- [[准tem模型|准TEM模型]]

## 涉及的模型

- [[cable-model|地下电缆]]
- [[双回路电缆系统|双回路电缆系统]]
- [[地回路阻抗模型|地回路阻抗模型]]
- [[土壤参数模型|土壤参数模型]]

## 相关主题

- [[emt-simulation|电磁暂态仿真]]
- [[地回路阻抗计算|地回路阻抗计算]]
- [[宽频带电缆建模|宽频带电缆建模]]
- [[土壤参数敏感性分析|土壤参数敏感性分析]]

## 主要发现

- De Conti-Lima公式在10MHz频带内计算误差显著低于传统近似表达式
- 传统公式在宽间距双回路系统中误差较大，新公式可显著提升暂态仿真精度与稳定性
- 土壤参数不确定性主导计算误差，但阻抗解析式精度仍对高频暂态结果有决定性影响

## 方法细节

### 方法概述

本文采用频域误差分析与时域电磁暂态仿真相结合的方法，系统评估两种地回路阻抗闭式近似公式（Saad-Gaba-Giroux与De Conti-Lima）的计算精度。首先，基于准TEM场传播理论，以Sunde积分方程（忽略位移电流）和Xue-Magalhães积分方程（完整准TEM模型）为基准，在10 Hz至10 MHz宽频带内计算双回路地下电缆系统的互阻抗。通过引入恒定参数（CP）与Alipio-Visacro频变（FD）土壤模型，结合不同回路间距（1~3 m），计算平均绝对百分比误差（MAPE）。随后，利用矢量拟合技术将频域参数转换为有理函数，嵌入ATP的通用线路模型（ULM）进行时域仿真。通过对比单位阶跃地模激励下的护套与线芯电压波形，并计算总均方根误差（RMS），验证闭式公式在宽频带、大间距及不同电缆长度下的暂态仿真稳定性与精度。

### 数学公式

**公式1**: $$$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) - K_0(\gamma_1 D) + \Theta \right]$$$$

*准TEM模型下地回路阻抗的广义积分表达式，作为理论基准。*

**公式2**: $$$$\Theta = 2 \int_0^\infty \frac{e^{-H\sqrt{\lambda^2+\gamma_1^2}}}{\sqrt{\lambda^2+\gamma_0^2}+\sqrt{\lambda^2+\gamma_1^2}} \cos(r\lambda) d\lambda$$$$

*广义积分项，包含空气与土壤传播常数，计算复杂。*

**公式3**: $$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) + \frac{2}{4+\gamma_1^2 r^2} e^{-H\gamma_1} \right]$$$$

*Saad-Gaba-Giroux闭式近似公式，适用于小间距低频场景。*

**公式4**: $$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left\{ K_0(\gamma_1 d) + \frac{H^2-r^2}{D^2} K_2(\gamma_1 D) - \frac{2e^{-\gamma_1 H}}{\gamma_1^2 D^2}(1+\gamma_1 H) - \frac{2r H e^{-\gamma_1 D}}{D^2} \sum_{n=1}^3 I_n \right\}$$$$

*De Conti-Lima闭式近似公式，基于Padé近似推导，适用于宽频带与大间距。*

### 算法步骤

1. 构建双回路地下电缆几何模型（6根电缆，每回路3根），设定埋深、外径及回路间距s（1 m、2 m、3 m）。

2. 定义土壤电气参数：电阻率设为100 Ωm与1000 Ωm，相对介电常数固定为10；分别采用恒定参数（CP）模型与Alipio-Visacro频变（FD）模型。

3. 在10 Hz至10 MHz频段内（每十倍频程20个采样点），数值积分计算基准地回路阻抗矩阵（Sunde方程与Xue-Magalhães方程）。

4. 将相同频率点与几何参数代入Saad-Gaba-Giroux公式与De Conti-Lima公式，计算近似阻抗矩阵。

5. 计算各频点幅值与相位的相对误差，并积分求得全频段平均绝对百分比误差（MAPE）。

6. 使用矢量拟合（Vector Fitting）算法将频域阻抗与导纳矩阵拟合为有理函数，生成宽频带电缆模型参数。

7. 将拟合参数通过ATPDraw的Read PCH工具导入ATP的通用线路模型（ULM）外部接口。

8. 设置时域仿真激励：在回路1护套施加单位阶跃电压（地模激励），回路2护套首端接地，所有线芯两端开路。

9. 运行100 m与1 km电缆长度的暂态仿真，提取接收端电压波形，计算与基准模型的总均方根误差（RMS），评估数值稳定性。

### 关键参数

- **回路间距_s**: 1 m, 2 m, 3 m

- **土壤电阻率_ρ**: 100 Ωm, 1000 Ωm

- **土壤相对介电常数_εr**: 10

- **频率范围**: 10 Hz ~ 10 MHz

- **电缆长度**: 100 m, 1000 m

- **频域采样密度**: 20 points/decade

## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 恒定土壤参数(CP)频域误差分析 | 以Sunde方程为基准，De Conti-Lima公式在s=3 m时全频段误差<2.5%；Saad-Gaba-Giroux公式在100 Ωm土壤中误差>10%，1000 Ωm土壤中误差>20%。 | De Conti-Lima公式的MAPE比Saad-Gaba-Giroux低2~3个数量级（如s=3m, 100Ωm, ≤10MHz时：0.189% vs 3.780%）。 |

| 频变土壤参数(FD)频域误差分析 | 引入Alipio-Visacro模型后误差趋势不变。De Conti-Lima公式在s<2 m时误差<5%，s=3 m时误差<10%；Saad-Gaba-Giroux公式在1000 Ωm土壤中误差高达50%以上。 | 频变土壤未显著改变相对精度，De Conti-Lima公式仍保持绝对优势，MAPE低2~10倍。 |

| 100 m短电缆时域暂态仿真(CP土壤) | 短电缆自然频率向高频偏移。Saad-Gaba-Giroux公式因高频误差导致模型拟合发散，仿真结果不稳定（RMS误差为∞）；De Conti-Lima公式波形与Xue-Magalhães基准高度重合，RMS误差仅9.16×10⁻³。 | De Conti-Lima公式在短电缆高频暂态中实现稳定收敛，而传统公式完全失效。 |

| 1 km长电缆时域暂态仿真(FD土壤) | 长电缆高频分量衰减，两种公式均能跟踪基准波形，但De Conti-Lima公式的RMS误差（2.65×10⁻³）仍略优于Saad-Gaba-Giroux公式（2.92×10⁻³）。 | 在长电缆低频主导场景下两者性能接近，但De Conti-Lima公式仍保持约10%的精度优势。 |

## 量化发现

- De Conti-Lima公式在10 MHz内相对Sunde方程的最大误差<2.5%，即使回路间距达3 m仍保持高精度。
- Saad-Gaba-Giroux公式在1000 Ωm土壤中10 MHz频带内误差>20%，频变土壤下误差峰值>50%。
- 以Xue-Magalhães完整准TEM方程为基准时，De Conti-Lima公式因忽略位移电流(γ₀)在>1 MHz产生5%~10%的系统偏差，但仍显著优于传统公式。
- 频域MAPE对比显示，De Conti-Lima公式误差比Saad-Gaba-Giroux低2~3个数量级（参考Sunde）或2~10倍（参考Xue-Magalhães）。
- 时域仿真中，100 m短电缆使用Saad-Gaba-Giroux公式导致数值发散（RMS=∞），而De Conti-Lima公式RMS误差控制在0.01以内，证明其宽频带暂态稳定性。

## 关键公式

### De Conti-Lima闭式地回路阻抗公式

$$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left\{ K_0(\gamma_1 d) + \frac{H^2-r^2}{D^2} K_2(\gamma_1 D) - \frac{2e^{-\gamma_1 H}}{\gamma_1^2 D^2}(1+\gamma_1 H) - \frac{2r H e^{-\gamma_1 D}}{D^2} \sum_{n=1}^3 I_n \right\}$$$$

*用于宽频带（最高10 MHz）、大间距（双回路系统）地下电缆的EMT仿真参数计算，替代复杂数值积分。*

### Saad-Gaba-Giroux闭式近似公式

$$$$Z_g \approx \frac{j\omega\mu_0}{2\pi} \left[ K_0(\gamma_1 d) + \frac{2}{4+\gamma_1^2 r^2} e^{-H\gamma_1} \right]$$$$

*传统ATPDraw内置公式，仅适用于小间距单回路电缆及低频场景，高频大间距下精度急剧下降。*

## 验证详情

- **验证方式**: 频域误差分析（MAPE计算）结合时域电磁暂态仿真（ULM模型对比）
- **测试系统**: 双回路地下电缆系统（共6根电缆，每回路3根，典型水平排列），回路间距1~3 m，电缆长度100 m与1 km
- **仿真工具**: MATLAB（频域计算、矢量拟合）、ATP/ATPDraw（通用线路模型ULM时域仿真）
- **验证结果**: 验证表明De Conti-Lima公式在10 MHz内精度显著优于传统Saad-Gaba-Giroux公式，频域误差低2~3个数量级。时域仿真中，新公式在短电缆高频地模激励下保持数值稳定，波形与完整准TEM积分基准高度一致，而传统公式在100 m电缆场景下出现发散。恒定与频变土壤模型下的结论一致，证明该闭式公式可直接替代复杂积分用于工程级宽频带电缆EMT建模。

## 适用边界

### 适用条件

- 适用于理解本文 `Accuracy assessment of analytical expressions for the ground return impedance of underground cables`（2025） 在当前页面抽取范围内讨论的 EMT/电力系统暂态问题。
- 适用于以 闭式近似公式、积分方程法、误差分析 为核心的建模、仿真、等值、控制或稳定性分析场景；具体对象以原文算例和页面“涉及的模型”为准。
- 可作为知识图谱中的方法定位和文献入口，尤其用于追踪：系统评估两种地回路阻抗解析式在宽间距与宽频带下的计算精度及土壤参数敏感性

### 失效边界

- 不应外推到原文未覆盖的拓扑、控制策略、故障类型、频率范围、硬件平台或实时步长。
- 不应把页面中的“提高、显著、快速、准确”等概括性表述当作定量结论；只有“量化发现”和原文表图可核验的数字才可用于比较。
- 若页面作者、期刊、摘要或验证字段仍不完整，本页只能作为待复核文献入口，不能作为最终证据页引用。

### 关键假设

- 页面内容假设当前 PDF 抽取文本与 frontmatter 的 `sources` 指向同一篇论文。
- 方法结论默认受原文仿真工具、测试系统、参数设置、采样步长和对比基线约束。
- 当前边界层为保守整理：未从原文直接核验的内容不得升级为确定结论。

### 证据缺口

- 具体适用范围仍以原文算例、参数表和验证场景为准，当前页面不应外推到未验证系统。
- 源文件路径：`["EMT_Doc/05/De Conti和Lima - 2026 - Accuracy assessment of analytical expressions for the ground return impedance of underground cables.pdf"]`；需要深修时应优先核对该 PDF 的首页、摘要、方法和实验表图。
