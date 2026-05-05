---
title: "Half Bridge Submodule"
type: method
tags: [half-bridge-submodule]
created: "2026-05-05"
---

# Half Bridge Submodule

## 定义与边界

本文提出了一种二极管钳位半桥MMC拓扑结构，通过在每个子模块(SM)中集成一个钳位二极管和阻尼电阻，并在三相之间配置四个辅助电压平衡电路，实现了子模块电容电压的自发并联平衡。该拓扑重构了传统半桥MMC，使所有子模块属于6个自发电容并联行为(SCPBs)组。当某个SM被插入而相邻SM被旁路时，通过钳位二极管和辅助电路形成并联路径，使电容电压自然平衡。通过设计适当的RC时间常数，确保相邻SM具有相等的电容电压纹波。虽然电压平衡是自发实现的，但为了均衡开关损耗，系统采用开环最近电平调制(NLM)和载波移相正弦脉宽调制(CPS-SPWM)技术。...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，half-bridge-submodule在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

### 核心数学表达

半桥子模块的电容电压平衡方程：

$$C_{SM} rac{dv_c}{dt} = i_{arm} \cdot s$$

其中：
- $C_{SM}$：子模块电容
- $v_c$：电容电压
- $i_{arm}$：桥臂电流
- $s$：开关状态（插入=1，旁路=0）

最近电平调制(NLM)输出电平数：
$$N_{level} = N_{SM} + 1$$

$N_{SM}$为每桥臂子模块数。




## 适用边界与失败模式

**适用条件**：
- 适用于半桥MMC拓扑的电磁暂态仿真
- 电容电压自发平衡适用于稳态运行
- NLM调制适用于电平数较高的场合（$N_{SM} \geq 20$）

**失效边界**：
- 电容参数失配严重时平衡效果下降
- 故障期间自发平衡可能失效
- RC时间常数设计不当导致电压纹波过大


**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-]]
- [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour]]
- [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
