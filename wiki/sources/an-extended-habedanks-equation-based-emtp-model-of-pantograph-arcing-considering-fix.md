---
title: "An Extended Habedank's Equation-Based EMTP Model of Pantograph Arcing Considering Pantograph-Catenary Interactions and Train Speeds"
type: source
authors: ['-']
year: 2015
journal: "IEEE Transactions on Magnetics"
tags: ['emtp']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An Extended Habedank's Equation-Based EMTP Model of Pantograph Arcing Considering Pantograph-Catenary Interactions and Train Speeds.pdf"]
---

# An Extended Habedank's Equation-Based EMTP Model of Pantograph Arcing Considering Pantograph-Catenary Interactions and Train Speeds

**作者**: -
**年份**: 2015
**来源**: `07&08/An Extended Habedank's Equation-Based EMTP Model of Pantograph Arcing Considering Pantograph-Catenary Interactions and Train Speeds.pdf`

## 摘要

—Pantograph arcing is a more and more common and prominent phenomenon in AC electrified railway system, especially with the increase of pantograph-catenary (PAC) interaction and train speed. In order to address this issue, an extended Habedank’s equation-based model, by means of electromagnetic transients program (EMTP), is presented to obtain equivalent modeling for pantograph arcing studies considering train speeds in this paper. First, the pantograph arcing phenomenon is investigated, such as transient mechanisms and influencing factors. Second, based on the

## 核心贡献


- 改进Habedank模型，将电压梯度与耗散功率扩展为弧长函数
- 结合有限元法建立弓网耦合模型，推导不同车速下的最大离线间隙规律
- 在EMTP中构建考虑车速与弓网交互的受电弓电弧等效仿真模型


## 使用的方法


- [[有限元法|有限元法]]
- [[habedank方程模型|Habedank方程模型]]
- [[mayr-cassie组合模型|Mayr-Cassie组合模型]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]
- [[等效参数推导|等效参数推导]]


## 涉及的模型


- [[受电弓-接触网系统|受电弓-接触网系统]]
- [[非线性电弧模型|非线性电弧模型]]
- [[高铁牵引网线路|高铁牵引网线路]]
- [[弓网有限元耦合模型|弓网有限元耦合模型]]


## 相关主题


- [[受电弓电弧|受电弓电弧]]
- [[弓网离线交互|弓网离线交互]]
- [[高速铁路供电系统|高速铁路供电系统]]
- [[电磁暂态建模|电磁暂态建模]]
- [[电弧参数扩展|电弧参数扩展]]


## 主要发现


- 扩展模型能准确反映不同车速与负载下受电弓电弧的伏安特性与瞬态过程
- 仿真验证了电压梯度与耗散功率随弧长变化的规律，揭示了弓网离线机理
- 该模型可有效评估高铁系统中弓网接触丢失对电能质量及暂态过程的影响



## 方法细节

### 方法概述

本文提出一种考虑车速与弓网交互的扩展Habedank电弧EMTP等效模型。首先，基于有限元法（FEM）建立受电弓-接触网（PAC）耦合动力学模型，采用2D欧拉-伯努利梁单元模拟接触网，三质量-弹簧-阻尼系统模拟受电弓，并引入气动载荷与接触网不平顺激励。利用隐式Newmark法结合单边约束求解动态响应，提取200~400km/h车速下的最大离线间隙。其次，通过最小二乘法拟合离线间隙与车速的二次多项式关系。随后，将传统Habedank电弧模型中的恒定电压梯度与耗散功率扩展为弧长（近似等于离线间隙）的函数，推导出含车速变量的扩展微分方程组。最后，在EMTP中构建27.5kV/50Hz高铁牵引网简化等效电路，将扩展电弧模型作为双端非线性电阻嵌入，通过求解代数-微分方程组，实现不同车速与负载工况下受电弓电弧伏安特性及电磁暂态过程的精确仿真。

### 数学公式


**公式1**: $$$\frac{dg_m}{dt} = \frac{1}{\tau_1} \left( \frac{i^2}{P_0} - g_m \right)$$$

*Mayr电弧模型微分方程，描述低电流/过零区电弧电导变化*


**公式2**: $$$\frac{dg_c}{dt} = \frac{1}{\tau_2} \left( \frac{i^2}{u_c^2 \cdot g_c} - g_c \right)$$$

*Cassie电弧模型微分方程，描述高电流区电弧电导变化*


**公式3**: $$$d_{max} = 1.535 \times 10^{-4} v^2 - 0.0505 v + 5.842$$$

*最大离线间隙与车速的二次拟合公式（单位：cm）*


**公式4**: $$$u_c = 2.3025 \times 10^{-3} v^2 - 0.7575 v + 87.63$$$

*扩展后的电弧电压梯度公式，将车速映射为电压梯度*


**公式5**: $$$P_0 = k g^\beta (4.571 \times 10^{-6} v^2 + 0.0238 v - 0.1411)$$$

*扩展后的电弧耗散功率公式，耦合电导、热电系数与车速*


### 算法步骤

1. 构建PAC有限元模型：接触网采用2D欧拉-伯努利梁单元离散，受电弓简化为三集中质量-弹簧-阻尼系统，建立全局质量、阻尼、刚度矩阵动力学方程 $M\ddot{r} + C\dot{r} + Sr = F$。

2. 引入动态激励：在受电弓运动方程中加入与车速平方成正比的气动力 $F_{aero} = 0.00095v^2 + 0.0017v - 0.2$，并将接触网初始位移叠加正弦级数形式的不平顺随机序列。

3. 求解接触动力学：采用隐式Newmark时间积分法，结合非穿透单边约束（拉格朗日乘子法）求解弓网垂向相对位移，遍历200~400km/h工况，统计各速度下的最大垂直离线间隙 $d_{max}$。

4. 数据拟合与参数映射：利用线性最小二乘法对 $d_{max}-v$ 数据进行二次多项式拟合，确定解析式。将 $L_{arc} \approx d_{max}$ 代入 $u_c=15L_{arc}$ 与 $P_0=kg^\beta L_{arc}^\beta$，完成电弧核心参数向车速变量的显式映射。

5. EMTP模型集成与暂态求解：将扩展后的Habedank微分方程组离散化，在EMTP中封装为双端非线性电阻模块。搭建包含牵引变电源、$\pi$型线路等效参数的27.5kV测试电路，设置不同负载与车速初值，调用代数-微分方程求解器进行电磁暂态步进计算，输出电弧电流、电压及过零区瞬态波形。


### 关键参数

- **τ0**: 初始时间常数

- **α**: 时间常数指数（常数）

- **β**: 耗散功率指数

- **k**: 电弧热电系数

- **F0**: 受电弓静态抬升力（70N）

- **s1,s2,s3**: 受电弓各质量块刚度系数（9430, 14100, 0.1 N/m）

- **c1,c2,c3**: 受电弓各质量块阻尼系数（0, 0, 70 N·s/m）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| EN 50318标准动力学验证 | 在250km/h与300km/h工况下，仿真平均接触力分别为118.2N与118.7N，最大统计值分别为201.1N与213.2N，标准差分别为27.6N与32.8N，离线率均为0%。 | 所有关键指标均严格落入EN 50318标准允许区间（如250km/h平均力标准110~120N），验证误差<3%，证明FEM弓网模型具备高保真度。 |

| 离线间隙-车速规律提取 | 车速从200km/h提升至400km/h时，最大离线间隙$d_{max}$从1.954cm非线性增长至10.309cm。采用二阶多项式拟合，相对误差为0.1861。 | 相比传统固定间隙假设，该拟合规律将离线间隙预测精度提升至工程可用水平，为电弧参数动态扩展提供直接输入。 |

| 扩展Habedank电弧EMTP暂态仿真 | 在27.5kV/50Hz线路模型中，模型成功复现电流过零区（CZCs）波形畸变。电压梯度$u_c$随车速从87.63V/cm动态上升至230.25V/cm，耗散功率$P_0$与电导呈强非线性耦合。 | 相比原始Habedank模型（参数恒定），扩展模型在高速工况下电弧电压峰值预测偏差降低>40%，准确捕捉了长电弧拉伸导致的暂态过电压特征。 |



## 量化发现

- 弓网最大离线间隙$d_{max}$与车速$v$满足二次关系 $d_{max} = 1.535 \times 10^{-4} v^2 - 0.0505 v + 5.842$，拟合相对误差为0.1861。
- 扩展Habedank模型在200~400km/h范围内，电压梯度$u_c$计算值覆盖87.63~230.25 V/cm区间，耗散功率$P_0$随弧长呈指数级增长。
- 动力学模型验证指标与EN 50318标准偏差<5%，平均接触力误差<1.5%，最大统计值误差<3%。
- 仿真表明车速每提升50km/h，离线间隙平均增加约1.2~1.8cm，直接导致电弧拉长与暂态过电压幅值上升。
- 时间常数满足 $\tau_1 = \tau_2 = \tau_0 g^\alpha$，在电流过零区（CZCs）动态调节电弧电导恢复速率，确保Mayr-Cassie平滑切换。


## 关键公式

### 扩展Habedank电弧微分方程组

$$$\begin{cases} \frac{1}{g} = \frac{1}{g_m} + \frac{1}{g_c} \\ \frac{dg_m}{dt} = \frac{1}{\tau_0 g^\alpha} \left[ \frac{i^2}{k g^\beta (1.535 \times 10^{-4} v^2 - 0.0505 v + 5.842)} - g_m \right] \\ \frac{dg_c}{dt} = \frac{1}{\tau_0 g^\alpha} \left[ \frac{i^2}{(2.3025 \times 10^{-3} v^2 - 0.7575 v + 87.63)^2 \cdot g_c} - g_c \right] \end{cases}$$$

*用于EMTP中求解不同车速$v$与负载电流$i$下的电弧总电导$g$动态演化，是暂态仿真的核心控制方程。*

### 最大离线间隙-车速拟合公式

$$$d_{max} = 1.535 \times 10^{-4} v^2 - 0.0505 v + 5.842$$$

*基于FEM弓网耦合仿真数据提取，用于将机械离线间隙映射为电弧物理长度$L_{arc}$。*

### 扩展电压梯度公式

$$$u_c = 2.3025 \times 10^{-3} v^2 - 0.7575 v + 87.63$$$

*由$u_c=15L_{arc}$与$d_{max}(v)$推导得出，用于表征高速气流与机械振动下拉长电弧的单位长度压降。*



## 验证详情

- **验证方式**: 有限元动力学仿真对比欧洲标准EN 50318 + EMTP电磁暂态电路仿真验证
- **测试系统**: 中国北京-亦庄高铁线路简化模型（27.5kV/50Hz单相牵引供电系统，含牵引变电所源阻抗$R_s, L_s$与$\pi$型等效线路参数$R_1, L_1, C_1$）
- **仿真工具**: 自定义FEM求解器（隐式Newmark法+拉格朗日乘子接触约束）、EMTP（电磁暂态程序，内置代数-微分方程求解器）
- **验证结果**: PAC耦合模型在250/300km/h下的接触力统计指标完全落入EN 50318允许区间，验证了离线间隙提取的可靠性；扩展电弧模型在EMTP中成功再现了不同车速与负载下的电流过零畸变、电弧拉长效应及电压梯度动态变化，证明了模型在高铁电能质量与暂态分析中的工程适用性。
