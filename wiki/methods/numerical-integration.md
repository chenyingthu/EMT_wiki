---
title: "数值积分"
type: method
tags: []
created: "2026-04-13"
---

# 数值积分

## 论文方法分析
> 基于 5 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 混合数值积分法 | 1 | An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on H |
| 诺顿等效电路法 | 1 | An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on H |
| 蛙跳积分法(Leapfrog) | 1 | An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on H |
| 恒定电导法 | 1 | An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on H |
| 平均值建模 | 1 | Field Validated Generic EMT-Type Model of a Full Converter Wind Turbin |
| 开关等效电路法 | 1 | Field Validated Generic EMT-Type Model of a Full Converter Wind Turbin |
| 混合建模技术 | 1 | Field Validated Generic EMT-Type Model of a Full Converter Wind Turbin |
| 故障穿越控制策略 | 1 | Field Validated Generic EMT-Type Model of a Full Converter Wind Turbin |
| 2S-DIRK数值积分法 | 1 | Numerical Integration by the 2-Stage Diagonally |
| 梯形法 | 1 | Numerical Integration by the 2-Stage Diagonally |
| 后向欧拉法 | 1 | Numerical Integration by the 2-Stage Diagonally |
| Gear-Shichman法 | 1 | Numerical Integration by the 2-Stage Diagonally |
| 临界阻尼调整(CDA) | 1 | Numerical Integration by the 2-Stage Diagonally |
| 频率匹配线性数值积分技术 | 1 | Optimization of numerical integration methods for the simulation of dy |
| 动态相量法(DPA) | 1 | Optimization of numerical integration methods for the simulation of dy |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 模块化多电平换流器(MMC) | 1 |
| 半桥子模块 | 1 |
| 桥臂等效电路 | 1 |
| 全功率变流器风力发电机(Type-IV) | 1 |
| 无齿轮外励磁同步发电机 | 1 |
| 六脉冲二极管整流器 | 1 |
| DC-DC升压变换器 | 1 |
| 两电平电压源型变流器(VSC) | 1 |
| 电感 | 1 |
| 电容 | 1 |
| 电力电子变换器/半导体开关 | 1 |
| 分布参数线路 | 1 |
| 非线性元件 | 1 |
| 动态相量模型 | 1 |
| 电力系统（含电机、FACTS装置、电力变换器） | 1 |
### 验证方式分布
- **仿真/对比**: 2 篇
- **仿真验证与对比**: 1 篇
- **现场实测数据验证**: 1 篇
- **仿真对比**: 1 篇
## 技术演进脉络
### 2008年 (1篇)
- **Numerical Integration by the 2-Stage Diagonally**
  - 💡 将2S-DIRK积分法引入EMT仿真，在无需事件检测的前提下同时实现了高精度与无振荡特性。
  - 推导了适用于线性和非线性电感、电容的2S-DIRK离散化公式。
  - 证明了2S-DIRK具备与梯形法相当的二阶精度和A稳定性，且能消除突变引起的数值振荡。
### 2009年 (1篇)
- **Optimization of numerical integration methods for the simulation of dynamic phas**
  - 💡 提出基于频域截断误差最小化的频率匹配数值积分方法，专门优化动态相量模型在系统频率附近的仿真精度与计算效率。
  - 提出专用于动态相量模型的频率匹配线性数值积分技术。
  - 通过在频域分析并最小化局部截断误差，推导出积分方法的优化系数。
### 2018年 (1篇)
- **Field Validated Generic EMT-Type Model of a Full Converter Wind Turbine Based on**
  - 💡 提出了一种结合开关等效电路与平均值模型的通用混合EMT建模方法，在保持高精度的同时显著提升了全功率风电机组暂态仿真的计算效率。
  - 提出了一种基于外励磁同步发电机和全功率变流器的Type-IV风电机组通用EMT模型。
  - 开发了结合开关等效电路与平均值模型的混合EMT模型，支持更大仿真步长以提升计算效率。
### 2023年 (2篇)
- **An Efficient Half-Bridge MMC Model for EMTP-Type Simulation Based on Hybrid Nume**
  - 💡 基于混合数值积分与蛙跳计算构建恒定电导的MMC桥臂等效模型，实现动态方程完全解耦，在保证精度的前提下显著提升EMTP型仿真效率。
  - 提出了一种基于混合数值积分的高效MMC电磁暂态仿真模型。
  - 将MMC桥臂简化为两节点诺顿等效电路，并实现电容与电感动态方程的解耦。
- **Study of a numerical integration method using the compact scheme for electromagn**
  - 💡 提出了一种兼具L稳定性与单阶段特性的紧凑格式数值积分算法，无需事件检测即可同步解决电磁暂态仿真中的数值振荡与非线性尖峰问题。
  - 提出了一种基于紧凑格式的单阶段数值积分方法用于电磁暂态仿真。
  - 证明了该方法在电路突变为刚性系统时具备L稳定性，可自动抑制虚假数值振荡。
## 关键发现汇总
- [2008] **Numerical Integration by the 2-Stage Diagonally**: 2S-DIRK在保持二阶精度和A稳定性的同时，彻底消除了梯形法在变量突变时产生的虚假数值振荡。
- [2008] **Numerical Integration by the 2-Stage Diagonally**: 相较于EMTP的CDA方法，2S-DIRK无需依赖突变事件检测即可自动抑制振荡，在复杂控制或分布参数线路场景下更具鲁棒性。
- [2009] **Optimization of numerical integration methods for the simula**: 频率匹配积分方法在目标频率附近的数值精度显著优于传统欧拉法、梯形法等。
- [2009] **Optimization of numerical integration methods for the simula**: 该方法允许使用更大的积分步长，从而在保证精度的前提下大幅降低计算时间。
- [2018] **Field Validated Generic EMT-Type Model of a Full Converter W**: 混合模型允许使用更大的仿真时间步长，显著提高了暂态仿真的计算速度。
- [2018] **Field Validated Generic EMT-Type Model of a Full Converter W**: 模型仿真波形与实际风电机组的现场测量数据高度吻合，验证了模型的准确性。
- [2018] **Field Validated Generic EMT-Type Model of a Full Converter W**: 所提模型成功复现了两种故障穿越控制策略的动态响应，满足电网规范要求。
- [2023] **An Efficient Half-Bridge MMC Model for EMTP-Type Simulation **: 在不同规模电力系统测试中，模型仿真结果与详细模型高度一致，验证了其精度。
- [2023] **An Efficient Half-Bridge MMC Model for EMTP-Type Simulation **: 恒定电导与解耦策略显著减少了系统节点数与计算量，大幅提升了离线EMT仿真效率。
- [2023] **Study of a numerical integration method using the compact sc**: 紧凑格式方法在电路状态突变时能完全消除梯形法固有的虚假数值振荡。
- [2023] **Study of a numerical integration method using the compact sc**: 相较于2S-DIRK和TR-BDF2等多阶段方法，该单阶段方法在处理非线性元件时不产生虚假电压/电流尖峰。
- [2023] **Study of a numerical integration method using the compact sc**: 该方法在保持二阶计算精度的同时实现了L稳定，无需依赖临界阻尼调整或插值等额外振荡抑制技术。
