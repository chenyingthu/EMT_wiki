---
title: "Ccvt"
type: method
tags: [ccvt]
created: "2026-05-05"
---

# Ccvt

## 定义与边界

基于EMTP平台构建TEHMP161A型CCVT全元件级时域数字模型。模型涵盖电容分压器(C1/C2)、排流线圈(Ld)、带多分接头与非线性饱和特性的降压变压器(SDT)、串联电抗器(Lc)、集中参数杂散电容(Cm/Ct/Cc)、谐波抑制滤波器及MOV/晶闸管/火花隙等保护装置。研究首先基于线性化等效电路开展频域灵敏度扫描，量化各寄生参数对幅频/相频特性的影响边界；随后在时域中施加近端接地故障与二次侧短路等典型暂态激励，利用EMTP的梯形积分法与补偿法求解含非线性磁化曲线与MOV伏安特性的微分代数方程组，精确捕捉铁磁谐振起振、次谐波振荡及高频衰减过程；最终通过实验室物理测试波形进行交叉验证，迭...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，ccvt在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达


### 核心数学表达

从相关研究提取的关键公式：

$$-\frac{dV(x,s)}{dx}=Z(s)I(x,s),\qquad -\frac{dI(x,s)}{dx}=Y(s)V(x,s)$$

$$Z(s)=Z_C(s)+Z_E(s)+Z_G(s)$$

$$Z_G(s)=sL_0$$

$$Y(s)=sC_0$$

$$-\frac{dV(x,s)}{dx}=\left(R'(s)+L_0s\right)I(x,s)$$





## 适用边界与失败模式


基于证据边界的分析：




**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[digital-time-domain-investigation-of-transient-behavior-of-coupling-capacitor-vo]]
- [[single-ended-travelling-wave-based-protection-scheme-for-double-circuit-transmis]]
- [[using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
