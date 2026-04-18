---
title: "Full-wave black-box transmission line tower model for the assessment of lightning backflashover"
type: source
authors: ['Bamdad Salarieh']
year: 2021
journal: "Electric Power Systems Research, 199 (2021) 107399. doi:10.1016/j.epsr.2021.107399"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/j.epsr.2021.107399.pdf.pdf"]
---

# Full-wave black-box transmission line tower model for the assessment of lightning backflashover

**作者**: Bamdad Salarieh
**年份**: 2021
**来源**: `19、20、21/EMT_task_20/j.epsr.2021.107399.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. Full-wave black-box transmission line tower model for the assessment of Department of Electrical & Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada In order to calculate the overvoltages across the insulator strings of overhead lines, electromagnetic transient (EMT)-type simulators require a model of the tower and its grounding system. In this paper, an electromagnetic

## 核心贡献


- 基于全波频域麦克斯韦方程建立杆塔电磁场模型，生成EMT兼容黑盒等效模型
- 采用矢量拟合将频域多端口网络转化为状态空间FDNE模型，直接接入时域仿真
- 综合考虑杆塔精细几何结构与接地极，并精确计及土壤参数的频率依赖性


## 使用的方法


- [[有限元法-fem|有限元法(FEM)]]
- [[全波频域麦克斯韦方程求解|全波频域麦克斯韦方程求解]]
- [[vector-fitting|矢量拟合]]
- [[多端口网络建模|多端口网络建模]]
- [[fdne-model|FDNE]]
- [[诺顿等效与卷积算子|诺顿等效与卷积算子]]


## 涉及的模型


- [[400kv双回输电杆塔|400kV双回输电杆塔]]
- [[接地系统-水平接地极|接地系统(水平接地极)]]
- [[避雷线与相导线|避雷线与相导线]]
- [[绝缘子串|绝缘子串]]
- [[fdne-model|FDNE]]


## 相关主题


- [[雷击反击闪络评估|雷击反击闪络评估]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关土壤建模|频率相关土壤建模]]
- [[网络等值|网络等值]]
- [[防雷保护|防雷保护]]
- [[暂态过电压分析|暂态过电压分析]]


## 主要发现


- 黑盒模型能精确计算绝缘子串暂态过电压，显著优于IEEE与CIGRE简化模型
- 计及土壤频率特性可大幅提升接地系统暂态响应与反击闪络率计算精度
- 结合DE与LP闪络模型的概率分析，可准确评估不同土壤条件下的反击闪络率



## 方法细节

### 方法概述

本文提出一种基于全波频域麦克斯韦方程的输电杆塔电磁场仿真方法，旨在生成可直接接入电磁暂态(EMT)仿真器的黑盒等效模型。首先利用有限元法(FEM)对包含杆塔精细几何结构（横担、斜材）、避雷线、相导线及水平接地极的系统进行三维建模，并引入土壤参数的频率依赖性。通过单轴完美匹配层(UPML)截断计算域，并采用体积扰动技术提高细导线网格精度。在频域(10 kHz~10 MHz)内求解多端口网络传递函数后，采用矢量拟合(Vector Fitting)技术将其转化为40~50阶的状态空间模型(FDNE)。最后，通过诺顿等效与卷积算子将该频变网络无缝集成至PSCAD/EMTDC中，实现时域暂态过电压与反击闪络率(BFR)的高效精确计算，无需手动推导等效电路参数。

### 数学公式


**公式1**: $$$\nabla \times \left( \frac{1}{\mu} \nabla \times \mathbf{E}(x,y,z) \right) - k^2 \mathbf{E}(x,y,z) = 0$$$

*频域全波麦克斯韦波动方程，用于求解复杂介质中的电场分布*


**公式2**: $$$k = \omega \sqrt{\varepsilon \left(1 - j\frac{\sigma}{\varepsilon\omega}\right)}$$$

*复波数表达式，显式包含介电常数、电导率及角频率，用于表征土壤等色散介质的频变特性*


**公式3**: $$$Z_{\text{surge}} = 60 \ln\left(\frac{2h}{r}\right) = 518.8\,\Omega$$$

*雷击通道连接导线的波阻抗计算公式，用于确定端口匹配条件*


### 算法步骤

1. 构建三维几何模型：在FEM软件中精确建立400kV双回杆塔、横担、斜材、避雷线、相导线及不同长度水平接地极的拓扑结构。

2. 定义材料与边界条件：设置空气、金属及土壤的电磁参数，启用土壤频变特性模型；在计算域外边界施加单轴完美匹配层(UPML)以吸收 outgoing 电磁波。

3. 网格优化处理：针对细导线采用体积扰动技术提升曲面网格精度，确保高频电磁场求解的数值稳定性。

4. 端口定义与频域求解：在塔顶设置电流注入端口（雷击点），在绝缘子串位置设置输出端口；在10 kHz~10 MHz频段内执行频域FEM扫描，获取多端口导纳/传递函数矩阵。

5. 矢量拟合与状态空间转换：利用矢量拟合算法对频域响应进行有理函数逼近，生成40~50阶的状态空间模型，并严格校验模型的无源性(Passivity)。

6. EMT接口转换：将状态空间模型转换为诺顿等效电路形式，结合卷积算子处理频变特性，封装为FDNE黑盒组件。

7. 时域暂态仿真集成：将FDNE组件导入PSCAD/EMTDC，注入标准雷电流波形，直接计算绝缘子串两端的暂态过电压。

8. 闪络与概率评估：基于DE(破坏效应)与LP(先导发展)闪络模型，结合两种实测首回雷电流波形，计算临界闪络电流并统计反击闪络率(BFR)。


### 关键参数

- **频率扫描范围**: 10 kHz ~ 10 MHz

- **FDNE拟合极点数**: 40 ~ 50

- **雷击通道导线长度**: 500 m

- **通道内阻**: 500 Ω

- **通道总输入阻抗**: 1018 Ω

- **相导线型号**: CURLEW (直径31.63 mm, 直流电阻0.05501 Ω/km)

- **避雷线型号**: 94S (直径12.6 mm, 直流电阻0.642 Ω/km)

- **线路终端匹配距离**: 100 m

- **吸收边界条件**: 单轴完美匹配层(UPML)

- **闪络评估模型**: DE模型与LP模型



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 400kV双回杆塔雷击塔顶暂态过电压计算 | 在10 kHz~10 MHz频段内提取多端口传递函数，经矢量拟合后生成FDNE黑盒模型，输入标准雷电流波形计算绝缘子串两端暂态电压 | 相较于IEEE 1243与CIGRÉ TB 63采用的Sargent-Darveniza及Chisholm简化模型，传统方法误差达11.5%且随土壤电阻率升高而恶化，本模型通过全波FEM与频变土壤建模显著提升精度 |

| 不同土壤条件下的反击闪络率(BFR)概率评估 | 结合Visacro与Anderson-Eriksson两种首回雷电流波形，采用DE与LP闪络准则计算临界闪络电流，统计负向首回雷击导致反击闪络的百分比 | 克服了传统方法将接地系统简化为低频固定电阻的缺陷，精确计及接地极高频频变特性与电磁耦合效应，使BFR预测更贴近实际物理过程 |



## 量化发现

- 传统IEEE/CIGRÉ简化模型在单回杆塔绝缘子串电压计算中误差达11.5%，且随土壤电阻率升高误差显著增大
- 全波黑盒模型在10 kHz~10 MHz频段内实现无源稳定拟合，极点数控制在40~50个，计算效率满足EMT实时性要求
- 雷击通道等效输入阻抗精确设定为1018 Ω（500 Ω内阻+518.8 Ω波阻抗），有效消除端口反射并匹配实际通道阻抗范围
- FDNE模型直接嵌入EMT仿真器，避免传统多节/多层模型需手动计算分布参数的繁琐过程，实现端到端黑盒调用


## 关键公式

### 频域全波麦克斯韦波动方程

$$$\nabla \times \left( \frac{1}{\mu} \nabla \times \mathbf{E}(x,y,z) \right) - k^2 \mathbf{E}(x,y,z) = 0$$$

*用于在FEM中求解包含频变土壤、金属导体及空气的复杂三维电磁场分布，是生成多端口频响数据的基础*

### 复波数表达式

$$$k = \omega \sqrt{\varepsilon \left(1 - j\frac{\sigma}{\varepsilon\omega}\right)}$$$

*嵌入波动方程中，显式表征土壤电导率与介电常数随频率变化的色散特性，确保高频接地系统响应准确*



## 验证详情

- **验证方式**: 数值仿真对比与EMT时域验证
- **测试系统**: 400 kV双回路输电杆塔（含横担、斜材、避雷线、相导线及不同长度水平接地极，终端100m处接匹配网络）
- **仿真工具**: ANSYS HFSS (频域FEM求解), Vector Fitting (频域-状态空间转换), PSCAD/EMTDC (时域EMT仿真)
- **验证结果**: 黑盒模型成功复现绝缘子串暂态过电压波形，无源性验证通过，与IEEE/CIGRÉ简化模型相比显著降低计算误差，支持不同雷电流波形与闪络准则下的BFR概率评估，验证了全波建模与FDNE接口在防雷暂态分析中的工程适用性
