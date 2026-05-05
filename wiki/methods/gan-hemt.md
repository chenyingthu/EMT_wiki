---
title: "Gan Hemt"
type: method
tags: [gan-hemt]
created: "2026-05-05"
---

# Gan Hemt

## 定义与边界

本文提出了一种分层混合实时仿真架构，用于直流铁路微电网(DRM)的硬件在环(HIL)仿真。在系统级，采用传输线法(TLM)对DRM电力系统进行分区解耦，结合门控循环单元(GRU)和电磁暂态(EMT)建模技术处理系统级子网络。在器件级，针对宽禁带(WBG)器件（氮化镓高电子迁移率晶体管GaN HEMT和碳化硅绝缘栅双极型晶体管SiC IGBT），提出物理特征神经网络(PFNN)模型。PFNN通过提取波形物理特征点（拐点、峰值、谷值）而非固定时间步长采样，实现变步长（低至1ns）的高精度建模。整个系统在Xilinx Ultrascale+ FPGA平台上实现并行加速，通过分段线性化在关键特征点间插...

**边界限定**：待完善。需要进一步研究确定该方法/模型的具体适用条件和失效边界。

## EMT中的作用

基于相关研究，gan-hemt在EMT仿真中用于解决特定问题。

基于相关研究，该方法在EMT仿真中的主要应用包括：
- 特定场景的电磁暂态分析
- 控制系统设计与验证
- 故障分析与保护协调

## 主要分支与机制

- 待补充（需要进一步研究确定具体分支）

## 形式化表达

- 待补充



## 适用边界与失败模式

- 待补充

**潜在失效模式**：
- 参数设置不当可能导致仿真不稳定
- 特定工况下可能产生数值误差
- 需要进一步研究确定具体失效边界

## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统基础
- [[control-system]] - 控制系统基础

## 代表性来源

- [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode]]
- [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-]]
- [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines]]


---

*本页面由批量生成脚本创建，需要进一步人工审查和完善。*
