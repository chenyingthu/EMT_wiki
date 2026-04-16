---
title: "A Time-Domain Harmonic Power-Flow Algorithm"
type: source
year: 2010
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/04/tpwrd.2010.2043547.pdf.pdf"]
---

# A Time-Domain Harmonic Power-Flow Algorithm

**年份**: 2010
**来源**: `04/tpwrd.2010.2043547.pdf.pdf`

## 摘要

—Steady-state simulation plays a vital role in power system analysis and design. Over the past 25 plus years, various steady-state methods have been proposed. Most of these methods only deal with how to obtain steady-state waveforms of a system in an efﬁcient manner. Only a few of them also take power-ﬂow con- straints into account. The majority of these “power-ﬂow” methods are implemented in the frequency domain, which inevitably suffers from harmonic truncation errors. Moreover, the problem of model incompatibility will rise when they are used for the steady-state initialization of a time-domain electromagnetic transient (EMT) program. This paper presents a harmonic power-ﬂow method, which is implemented entirely in the time domain. The proposed method essentially extends a time-domain s

## 核心贡献


- 提出全时域谐波潮流算法，避免频域截断误差及与EMT程序模型不兼容问题
- 将潮流约束与聚合负荷计算融入打靶法，实现时域稳态分析扩展
- 基于基波与广义功率理论，建立非正弦条件下时域有功无功计算方法


## 使用的方法


- [[打靶法|打靶法]]
- [[牛顿-拉夫逊法|牛顿-拉夫逊法]]
- [[灵敏度电路分析|灵敏度电路分析]]
- [[时域谐波潮流算法|时域谐波潮流算法]]
- [[快速傅里叶变换|快速傅里叶变换]]


## 涉及的模型


- [[发电机|发电机]]
- [[聚合负荷|聚合负荷]]
- [[非线性元件|非线性元件]]
- [[电力电子装置|电力电子装置]]


## 相关主题


- [[谐波分析|谐波分析]]
- [[潮流计算|潮流计算]]
- [[时域稳态仿真|时域稳态仿真]]
- [[emt初始化|EMT初始化]]
- [[非正弦稳态|非正弦稳态]]
- [[非线性系统|非线性系统]]


## 主要发现


- 算法有效求解非正弦稳态波形，同时满足基波与谐波潮流约束条件
- 全时域实现消除频域谐波截断误差，且与现有EMT程序模型完全兼容
- 灵敏度电路法构建雅可比矩阵显著提升牛顿迭代求解效率与收敛性


