---
title: "A Time-Domain AC Electric Arc Furnace Model for Flicker Planning Studies"
type: source
year: 2009
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/TPWRD.2008.2007021.pdf.pdf"]
---

# A Time-Domain AC Electric Arc Furnace Model for Flicker Planning Studies

**年份**: 2009
**来源**: `04/TPWRD.2008.2007021.pdf.pdf`

## 摘要

—A time-domain model of an AC electric arc furnace (EAF) was developed for power system (ﬂicker) planning studies. The proposed model was implemented in the Electro Magnetic Transient Program (EMTP), and it focuses on the behavior of the EAF during the early stages of the melt cycle, thus providing an accurate prediction of the short term ﬂicker created by the EAF, speciﬁcally P 99% . The primary advantages of the proposed model over existing models are: 1) it uses system data that is readily available to the planning engineer; 2) it is a three phase model and can accurately model imbalance and predict ﬂicker at the point of common coupling (PCC) as well as remote buses in the power system; and 3) its accuracy has been veriﬁed using synchronized ﬂicker measurements of an actual EAF. Existi

## 核心贡献


- 提出基于EMTP的交流电弧炉时域模型，仅需常规规划数据即可构建
- 建立三相非对称电弧模型，精准模拟熔炼初期弧长随机与周期性变化
- 实现公共连接点及远端母线闪变预测，克服频域法常数因子误差局限


## 使用的方法


- [[时域仿真|时域仿真]]
- [[emtp建模|EMTP建模]]
- [[电弧长度时变建模|电弧长度时变建模]]
- [[三相不平衡分析|三相不平衡分析]]
- [[gps同步测量验证|GPS同步测量验证]]


## 涉及的模型


- [[交流电弧炉-eaf|交流电弧炉(EAF)]]
- [[非线性电弧模型|非线性电弧模型]]
- [[iec闪变仪模型|IEC闪变仪模型]]
- [[电力系统网络|电力系统网络]]
- [[svc-statcom补偿装置|SVC/STATCOM补偿装置]]


## 相关主题


- [[闪变规划研究|闪变规划研究]]
- [[电能质量评估|电能质量评估]]
- [[电弧炉时域建模|电弧炉时域建模]]
- [[三相不平衡分析|三相不平衡分析]]
- [[频域与时域方法对比|频域与时域方法对比]]


## 主要发现


- 模型预测的Pst99%与实际GPS同步测量数据高度吻合，验证了时域方法精度
- 频域法因采用固定增益与补偿系数，在远端母线闪变预测中存在显著误差
- 三相时域模型能准确捕捉熔炼初期弧长波动引发的系统电压闪变特征



## 方法细节

### 方法概述

提出一种基于EMTP的交流电弧炉(EAF)时域模型，专用于电力系统闪变规划研究。模型聚焦于熔炼初期的“钻孔期”(bore-in period)，该阶段弧长剧烈波动产生最严重的短时闪变(P_st99%)。核心思想是将电弧等效为时变电阻，其阻值变化由随机分量与周期分量叠加构成。随机分量采用Park-Miller最小标准均匀分布随机数生成器，每约半个工频周期更新一次，模拟废钢塌落引起的弧长突变；周期分量采用固定频率与幅值的正弦波进行幅度调制，模拟熔池电磁力引起的流体动力学波动。模型参数仅需常规规划数据（系统短路容量、变压器阻抗等）即可通过频域等效电路与功率因数-弧阻曲线反演确定，无需依赖难以获取的实测统计量。最终在EMTP中搭建三相独立模块，结合IEC闪变仪算法输出P_st统计值。

### 数学公式


**公式1**: $$P_{st99\%} = C \frac{S_{sc}}{S_{sys}}$$

*频域闪变估算公式，C为特征发射系数(48-85)，S_sc为电极处短路容量，S_sys为PCC处系统短路容量*


**公式2**: $$V_{arc} = V_0 + k \cdot l$$

*电弧电压有效值与弧长关系式，V_0≈40V为常数，k为增益系数(3.9-11.8 V/cm)，l为弧长(cm)*


**公式3**: $$X_{arc} = \frac{R_{arc}^2}{X_{th}}$$

*给定弧阻下的等效电弧电抗估算公式，用于频域等效电路分析，X_th为从电极看入的系统正序戴维南等效电抗*


**公式4**: $$pf = \frac{P}{\sqrt{P^2+Q^2}}$$

*电炉输入功率因数计算公式，用于建立弧阻与功率因数的映射关系以确定模型边界参数*


### 算法步骤

1. 收集规划阶段可用系统数据：PCC短路容量、降压变压器与电炉变压器正序阻抗、系统戴维南等效参数。

2. 设定初始弧阻R_arc（通常从0.1Ω开始），利用公式X_arc = R_arc^2 / X_th计算等效电弧电抗。

3. 基于正序等效电路计算电炉输入有功功率P与无功功率Q，进而求得功率因数pf。

4. 逐步递增R_arc并重复步骤2-3，直至功率因数达到最大值（通常0.9~0.95，超过此值电弧不稳定）。

5. 绘制“输入功率-功率因数”及“功率因数-弧阻”曲线，结合实测钻孔期功率因数范围（0.25~0.9），反推确定模型所需的R_min与R_max。

6. 设定调制参数：调制深度m=0.2，调制频率f_m=8.8 Hz（典型经验值）。

7. 在EMTP中配置三相独立模块：为每相分配不同种子（建议>10000以保证20%~30%相位差异）的Park-Miller均匀分布随机数生成器。

8. 每约半个工频周期生成新随机数，将弧阻在[R_min, R_max]间随机跳变，并叠加正弦幅度调制。

9. 运行电磁暂态仿真，提取PCC及远端母线三相电压波形，输入IEC 61000-4-15标准闪变仪模型计算P_st序列。

10. 对至少一周（1008个10分钟区间）的P_st数据进行统计排序，提取P_st99%作为规划评估指标。


### 关键参数

- **V_0**: ≈40 V (电弧电压常数)

- **k**: 3.9 ~ 11.8 V/cm (弧长增益系数)

- **调制深度_m**: 0.2

- **调制频率_f_m**: 8.8 Hz

- **随机数种子范围**: 1 ~ 2147483646 (建议最小值10000以保证三相差异)

- **弧阻更新周期**: 约1/2个工频周期

- **运行功率因数范围**: 0.25 ~ 0.9

- **频域特征系数_C**: 48 ~ 85 (规划常用75)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 频域法(C=60) | PCC处P_st99%预测值为1.2，远端Bus 1为0.59 | 比实测值低约43%，严重低估闪变水平 |

| 频域法(C=75) | PCC处P_st99%预测值为1.5，远端Bus 1为0.74 | 比实测值低约29%，仍显著低于实际水平 |

| 现有正弦时域模型 | PCC处P_st99%预测值为2.8，远端Bus 1为1.4 | 比实测值高约32%，结果过于保守，易导致过度投资 |

| 现有BLW时域模型 | PCC处P_st99%预测值为0.8，远端Bus 1为0.4 | 比实测值低约62%，完全无法用于规划评估 |

| 本文提出时域模型 | PCC处P_st99%预测值为2.1，远端Bus 1为1.05 | 与实测值(2.12/1.08)误差分别<1%和2.8%，精度显著优于传统方法 |



## 量化发现

- PCC处P_st99%预测误差<1%（仿真2.1 vs 实测2.12）
- 远端母线闪变预测误差约2.8%（仿真1.05 vs 实测1.08）
- 频域法预测偏差达30%~43%，且无法准确反映远端母线闪变传递特性
- 传统正弦时域模型高估32%，带限白噪声(BLW)模型低估62%
- 三相仿真结果中，最高相P_st99%误差<1%，其余两相最大偏差达8.5%（主要源于模型假设系统电压平衡，而实测不平衡度为1.5%~2.0%）
- 模型仅需常规规划参数，无需依赖难以获取的现场统计量或实测波形


## 关键公式

### 频域闪变估算公式

$$P_{st99\%} = C \frac{S_{sc}}{S_{sys}}$$

*用于传统规划阶段快速估算PCC处闪变水平，依赖经验系数C*

### 电弧电压-弧长特性方程

$$V_{arc} = V_0 + k \cdot l$$

*建立电弧物理长度与电气量之间的映射关系，是时变电阻建模的理论基础*

### 等效电弧电抗公式

$$X_{arc} = \frac{R_{arc}^2}{X_{th}}$$

*在频域等效电路分析中，将非线性电弧阻抗线性化，用于反演R_min和R_max*

### 功率因数计算式

$$pf = \frac{P}{\sqrt{P^2+Q^2}}$$

*结合系统阻抗与弧阻迭代计算，确定电炉实际运行时的弧阻波动边界*



## 验证详情

- **验证方式**: 现场实测数据对比（GPS时间同步）+ 多模型交叉验证（频域法、正弦时域法、BLW时域法）
- **测试系统**: 美国Southern Company实际工业供电系统（含230kV PCC母线、34.5kV电炉变压器T2、远端230kV Bus 1及配套谐波滤波器组）
- **仿真工具**: EMTP (Electro Magnetic Transient Program), IEC 61000-4-15标准闪变仪（硬件/软件），GPS同步时钟
- **验证结果**: 通过GPS同步的IEC合规闪变仪连续一周采集1008个10分钟区间数据，验证了所提模型在PCC及远端母线的P_st99%预测精度。最高相预测误差<1%，远端母线误差<3%，显著优于频域法（误差>30%）和传统时域模型。误差主要来源于模型假设三相电压平衡（实测不平衡度1.5%~2.0%）及未考虑非电炉负荷潮流，但完全满足闪变规划工程精度要求。
