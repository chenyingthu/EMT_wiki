---
title: "An EMT based dynamic frequency scanning tool for stability analysis of inverter based systems"
type: source
authors: ['Chen Jiang']
year: 2025
journal: "Electric Power Systems Research, 251 (2026) 112226. doi:10.1016/j.epsr.2025.112226"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/An EMT based dynamic frequency scanning tool for stability analysis of inverter based systems.pdf"]
---

# An EMT based dynamic frequency scanning tool for stability analysis of inverter based systems

**作者**: Chen Jiang
**年份**: 2025
**来源**: `07&08/An EMT based dynamic frequency scanning tool for stability analysis of inverter based systems.pdf`

## 摘要

An EMT based dynamic frequency scanning tool for stability analysis of b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, Canada This paper introduces an automated dynamic frequency scanning tool designed to predict stability in power systems. The tool integrates frequency scanning and stability analysis into a single, user-friendly platform, which is validated through Electromagnetic Transients (EMT) simulations and traditional small-signal stability tech­

## 核心贡献


- 开发基于EMT的自动化动态频率扫描工具，集成阻抗扫描与稳定性分析流程
- 提出在dq坐标系下进行频率扫描的方法，有效消除逆变器系统的频率耦合效应
- 对比分析电压源型与电流源型构网型VSG控制策略的稳定性差异与适用场景


## 使用的方法


- [[动态频率扫描|动态频率扫描]]
- [[离散傅里叶变换|离散傅里叶变换]]
- [[根轨迹分析|根轨迹分析]]
- [[伯德图分析|伯德图分析]]
- [[小信号稳定性分析|小信号稳定性分析]]
- [[dq坐标系解耦扫描|dq坐标系解耦扫描]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[电压源型虚拟同步机|电压源型虚拟同步机]]
- [[电流源型虚拟同步机|电流源型虚拟同步机]]
- [[构网型变流器|构网型变流器]]
- [[等效rl交流网络|等效RL交流网络]]


## 相关主题


- [[稳定性分析|稳定性分析]]
- [[构网型控制|构网型控制]]
- [[频率扫描|频率扫描]]
- [[阻抗建模|阻抗建模]]
- [[逆变器并网系统|逆变器并网系统]]
- [[临界短路比|临界短路比]]


## 主要发现


- 电流源型VSG无需PI限流器，在强交流电网中仍能保持稳定运行
- 电压源型VSG因引入PI电流限幅控制，在强电网下易引发系统失稳
- 频率扫描工具预测的临界短路比与根轨迹分析及EMT时域仿真结果高度一致



## 方法细节

### 方法概述

提出一种基于EMT仿真的自动化动态频率扫描工具，集成于PSCAD/EMTDC平台。该方法通过在系统稳态运行点注入多频正弦扰动信号（电流或电压），记录PCC处的电压电流响应，利用离散傅里叶变换（DFT）提取频域幅值与相位。为消除电力电子系统的频率耦合效应，扫描在dq0坐标系下进行。通过矩阵运算获取变流器与电网的阻抗/导纳矩阵，构建闭环传递函数，并计算开环增益矩阵的特征值。最终利用特征值的伯德图分析增益裕度与相位裕度，预测系统的临界短路比（CSCR）及振荡频率，实现黑盒模型下的稳定性评估。

### 数学公式


**公式1**: $$$Z_{MMC}^{abc}(f) = V_{PCC}^{abc}(f) \cdot [I_{MMC}^{abc}(f)]^{-1}$$$

*通过三次独立相注入获取的PCC电压矩阵与MMC电流矩阵求逆相乘，得到MMC在频率f下的三相阻抗矩阵*


**公式2**: $$$\frac{\Delta V_{PCC}}{\Delta I_{Dis}} = \frac{Z_{MMC}}{1 + Z_{MMC} \cdot Y_{ac}}$$$

*基于扫描得到的MMC阻抗与电网导纳构建的闭环系统传递函数，用于稳定性分析*


**公式3**: $$$CSCR = \frac{SCR_{initial}}{|\lambda|_{180^\circ}}$$$

*根据伯德图中相位为180°时特征值的幅值反推临界短路比，幅值越接近1系统越接近失稳边界*


### 算法步骤

1. 1. 初始化EMT仿真，等待系统达到指定稳态运行点（如额定功率输出），确保小信号线性化假设成立。

2. 2. 在公共连接点（PCC）注入幅值约为额定值0.5%的多频正弦扰动信号（通常包含最多30个频率点），扰动类型根据系统特性选择电流或电压注入。

3. 3. 待暂态过程衰减后，同步采集稳态下的三相电压与电流时域波形数据。

4. 4. 对采集的时域信号应用离散傅里叶变换（DFT），提取各注入频率下的幅值与相位信息。

5. 5. 在dq0坐标系下重复注入过程（分别注入d轴、q轴、0轴扰动），将abc域测量值通过逆Park变换转换至dq0域，构建完整的频域电压与电流矩阵。

6. 6. 通过矩阵求逆与乘法运算计算目标元件（如MMC或电网）在各频率点的阻抗/导纳矩阵。

7. 7. 计算开环增益矩阵 $Z_{MMC}Y_{ac}$ 的特征值，绘制各特征值的幅频与相频伯德图。

8. 8. 定位相频曲线穿越180°的频率点，读取对应幅值，计算增益裕度并推导临界短路比（CSCR）与潜在振荡频率。


### 关键参数

- **直流侧电压**: ±150 kV

- **MMC额定容量**: 270 MVA

- **MMC额定电压**: 180 kV

- **子模块数量**: 每桥臂20个

- **基准短路比(SCR)**: 2.5

- **电压源型VSG惯量/阻尼(J,D)**: (0.04, 1.0)

- **电压源型VSG交流控制器增益(Kp,Ki)**: (2.5, 10)

- **电流源型VSG惯量常数H**: 3.42

- **电流源型VSG阻尼常数**: 5.0

- **扰动信号幅值**: 额定值的0.5%

- **扫描频率点数**: 最多30个



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 电压源型VSG系统变SCR稳定性测试 | 当SCR从3.6阶跃至3.8时，系统在10s后失稳，EMT时域波形显示有功功率出现持续振荡，实测振荡频率为1.15 Hz。频率扫描预测的CSCR为3.7，与根轨迹法预测的3.7~3.8高度吻合。 | 频率扫描预测的CSCR(3.7)与根轨迹分析结果误差<2.7%，振荡频率预测值(1.15 Hz)与根轨迹(1.05 Hz)偏差约9.5%，时域仿真完全复现失稳边界。 |

| 电流源型VSG系统宽范围SCR测试 | 在SCR从1.2（弱网）至100.0（强网）的宽范围内进行扫描，伯德图显示所有特征值相位均未在幅值>1时穿越180°，系统始终保持稳定。 | 相较于电压源型VSG在SCR>3.8即失稳，电流源型VSG在强网下无需PI限流器即可稳定运行，稳定性裕度提升显著，验证了控制架构的优越性。 |



## 量化发现

- 电压源型VSG的临界短路比(CSCR)精确预测值为3.7，失稳振荡频率为1.15 Hz。
- 在相位180°处特征值幅值为0.67，据此推算CSCR = 2.5 / 0.67 ≈ 3.73，与理论值高度一致。
- 电流源型VSG在SCR高达100.0的强交流系统中仍保持稳定，无右半平面特征值。
- 动态频率扫描采用最多30个频率点的多频正弦注入，扰动幅值设定为额定值的0.5%即可保证信噪比与线性度。
- dq0坐标系扫描有效消除了正负序频率耦合，使阻抗矩阵非对角元素（如Zd0, Zq0）幅值极小可忽略，大幅简化计算维度。


## 关键公式

### 频域阻抗矩阵计算公式

$$$Z_{MMC}^{abc}(f) = V_{PCC}^{abc}(f) \cdot [I_{MMC}^{abc}(f)]^{-1}$$$

*用于通过三次独立相注入的DFT频域电压电流数据，直接求解MMC在特定频率下的全阶阻抗矩阵*

### 闭环系统传递函数

$$$\frac{\Delta V_{PCC}}{\Delta I_{Dis}} = \frac{Z_{MMC}}{1 + Z_{MMC} \cdot Y_{ac}}$$$

*基于扫描得到的MMC阻抗与电网导纳构建，用于推导开环增益矩阵并评估系统稳定性裕度*

### 临界短路比推算公式

$$$CSCR = \frac{SCR_{initial}}{|\lambda|_{180^\circ}}$$$

*利用伯德图中相位穿越180°时的特征值幅值，线性缩放初始SCR以预测系统失稳临界点*



## 验证详情

- **验证方式**: 对比验证：将EMT动态频率扫描结果与传统小信号根轨迹分析法及EMT时域阶跃仿真结果进行交叉验证
- **测试系统**: 简化MMC-交流电网系统（270 MVA，±150 kV，每桥臂20子模块，通过等效RL支路连接至PCC）
- **仿真工具**: PSCAD/EMTDC（内置自动化频率扫描组件与EMT仿真）、MATLAB/解析工具（根轨迹与伯德图绘制）
- **验证结果**: 频率扫描工具预测的CSCR(3.7)与根轨迹法(3.7~3.8)及EMT时域仿真(SCR=3.8失稳)完全一致；振荡频率预测值(1.15 Hz)与根轨迹(1.05 Hz)高度接近。验证了该工具在黑盒模型下无需内部控制器参数即可实现高精度、高效率的稳定性预测，且自动化流程显著降低了人工干预成本。
