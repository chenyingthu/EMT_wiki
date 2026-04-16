---
title: "MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Systems;2025;40;5;10.1109/TPWRS.2025.3535841"
tags: ['fpga']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/MTOF A Novel FPGA-Based EMT Toolbox in MATLAB.pdf"]
---

# MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB

**作者**: 
**年份**: 2025
**来源**: `27&28/MTOF A Novel FPGA-Based EMT Toolbox in MATLAB.pdf`

## 摘要

—Field programmable gate array (FPGA) is becom- ing an attractive solution for real-time electromagnetic transient (EMT) simulations. FPGA-based EMT simulation uses thousands of lines of code and sophisticated architecture to satisfy executable requirements ranging from the low-level analog signal to the ad- vanced EMT mathematics. The coding would place a tremendous burden on beginners to take at least 6 months. To provide more straightforward solutions, this paper develops the MATLAB-to- FPGA EMT toolbox (MTOF) in the computational engine frame of MATLAB. Based on Input Data, MTOF under a user-friendly MATLAB environment can generate transparent FPGA-based code while complex programming under FPGA can be avoided. This brings a dramatic coding simpliﬁcation and results in sig- niﬁcant sav

## 核心贡献


- 开发MTOF工具箱实现MATLAB至FPGA代码自动透明生成显著降低编程门槛
- 提出即插即用架构与浮点运算格式在FPGA上兼顾高精度计算与硬件资源效率
- 内置自动计算序列排序与内存分配机制支持任意拓扑电网的快速建模部署


## 使用的方法


- [[梯形积分法|梯形积分法]]
- [[节点分析法|节点分析法]]
- [[行波法|行波法]]
- [[浮点运算硬件映射|浮点运算硬件映射]]
- [[自动代码生成|自动代码生成]]


## 涉及的模型


- [[rlc支路|RLC支路]]
- [[三相变压器|三相变压器]]
- [[分布参数输电线路|分布参数输电线路]]
- [[同步电机|同步电机]]
- [[节点导纳矩阵|节点导纳矩阵]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[fpga硬件加速|FPGA硬件加速]]
- [[自动代码生成|自动代码生成]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力系统建模|电力系统建模]]


## 主要发现


- 工具箱可在五十秒内完成四机十一节点系统代码生成三百秒内完成十机三十九节点生成
- 单块FPGA板卡测试验证表明生成代码在复杂电网拓扑下仍保持高精度仿真结果
- 浮点数据格式与优化架构有效平衡了硬件资源占用与电磁暂态计算的实时性要求


