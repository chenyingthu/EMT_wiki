---
title: "Parametric Study of Transient Electromagnetic Fields"
type: source
authors: ['未知']
year: 2011
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/TPWRD.2011.2158592.pdf.pdf"]
---

# Parametric Study of Transient Electromagnetic Fields

**作者**: 
**年份**: 2011
**来源**: `31/TPWRD.2011.2158592.pdf.pdf`

## 摘要

—In this paper, the problem of calculating transient electromagnetic ﬁelds due to frequency-dependent multicon- ductor overhead transmission lines above lossy ground and underground cables buried in lossy soil is studied by decomposing the transmission line into a number of small segments. A modiﬁed ﬁnite-difference time-domain technique is applied to ﬁnd the current passing through each segment of the excited transmis- sion line. The contribution of each segment on the total electric and magnetic ﬁelds is calculated using two frequency-domain analytical techniques. The theoretical background and extent of validity of each technique are presented, and the results derived by applying each method are compared with those obtained using a commercial software package. The time-domain solution i

## 核心贡献


- 提出结合改进FDTD与偶极子分解的暂态电磁场计算方法精确计及频变参数与损耗大地
- 将复镜像理论与King近似公式引入多导体线路电磁场计算提升有限长线路建模精度
- 在PSCAD平台实现该算法支持导体弧垂与电缆屏蔽等复杂几何电气参数影响分析


## 使用的方法


- [[改进有限差分时域法-mfdtd|改进有限差分时域法(MFDTD)]]
- [[偶极子分解法|偶极子分解法]]
- [[复镜像理论|复镜像理论]]
- [[king近似公式|King近似公式]]
- [[傅里叶变换|傅里叶变换]]
- [[矩量法-mom|矩量法(MoM)]]


## 涉及的模型


- [[多导体架空输电线路|多导体架空输电线路]]
- [[地下电缆|地下电缆]]
- [[损耗大地模型|损耗大地模型]]
- [[频变线路参数模型|频变线路参数模型]]


## 相关主题


- [[暂态电磁场计算|暂态电磁场计算]]
- [[电磁干扰分析|电磁干扰分析]]
- [[频变参数建模|频变参数建模]]
- [[损耗大地效应|损耗大地效应]]
- [[导体弧垂影响|导体弧垂影响]]
- [[参数化研究|参数化研究]]


## 主要发现


- 忽略大地有限电导率与相对介电常数会导致暂态电磁场计算结果出现显著误差
- 导体弧垂变化会显著改变线路周围电磁场空间分布需在精确建模中予以考虑
- 复镜像理论与King近似公式计算结果与商业软件高度吻合验证了算法有效性


