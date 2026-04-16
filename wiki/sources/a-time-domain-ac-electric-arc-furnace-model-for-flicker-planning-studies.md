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


