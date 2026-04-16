---
title: "Application of EMTP in the research of UHV AC power transmission"
type: source
authors: ['未知']
year: 2006
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/09/Cao - 2006 - Application of EMTP in the research of UHV AC power transmission.pdf"]
---

# Application of EMTP in the research of UHV AC power transmission

**作者**: 
**年份**: 2006
**来源**: `09/Cao - 2006 - Application of EMTP in the research of UHV AC power transmission.pdf`

## 摘要

：EMTP(E1ectro-magnetic Transient Program)is the program to analyze the electro-magnetic transient phenomenon being used most extensively in the world．This paper introduces the EMTP modeling method first，and refers to the contributions of the author of this paper too。such as the development of phase-domain synchronous machine model and the improvement of control system and others．And then this paper introduces how to use EMTP in each research subject of UHV AC power transmission．The UHV AC power transmission is an economical and effective power transmission fonn，but it comes with various technological problems caused by high voltage，big charging capacity and small resistance of the ultra-high voltage transmission line，such as zero offset phenomena， resonance overvoltage，secondary

## 核心贡献


- 开发了基于相坐标的同步电机模型，避免坐标转换引起的数值不稳定问题
- 改进了EMTP的TACS控制系统，引入滤波器与迭代算法消除时延振荡
- 系统总结了特高压交流输电各类过电压及特有现象的EMTP建模与计算方法


## 使用的方法


- [[频率扫描法|频率扫描法]]
- [[相坐标建模|相坐标建模]]
- [[统计开关法|统计开关法]]
- [[tacs迭代控制|TACS迭代控制]]
- [[暂态数值计算|暂态数值计算]]


## 涉及的模型


- [[同步电机|同步电机]]
- [[j-marti输电线路模型|J.Marti输电线路模型]]
- [[饱和变压器|饱和变压器]]
- [[并联电抗器|并联电抗器]]
- [[金属氧化物避雷器|金属氧化物避雷器]]
- [[隔离开关电弧重燃模型|隔离开关电弧重燃模型]]
- [[tacs控制系统|TACS控制系统]]


## 相关主题


- [[特高压交流输电|特高压交流输电]]
- [[过电压计算|过电压计算]]
- [[零点偏移现象|零点偏移现象]]
- [[谐振过电压|谐振过电压]]
- [[潜供电流熄弧|潜供电流熄弧]]
- [[暂态恢复电压|暂态恢复电压]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 主要发现


- 相坐标同步电机模型有效避免了dq0坐标转换带来的数值预测与不稳定问题
- 特高压线路大电容小电阻特性易引发零点偏移与谐振过电压，需详细暂态模拟
- TACS接口插入低通滤波器及反馈环迭代计算可有效抑制数值振荡与内部时延


