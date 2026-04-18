---
title: "Z-Tool: Frequency-domain characterization of EMT models for small-signal stability analysis"
type: source
authors: ['Francisco', 'Javier', 'Cifuentes', 'Garcia']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112405. doi:10.1016/j.epsr.2025.112405"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/40/Cifuentes Garcia和Beerten - 2026 - Z-Tool Frequency-domain characterization of EMT models for small-signal stability analysis.pdf"]
---

# Z-Tool: Frequency-domain characterization of EMT models for small-signal stability analysis

**作者**: Francisco, Javier, Cifuentes 等
**年份**: 2025
**来源**: `40/Cifuentes Garcia和Beerten - 2026 - Z-Tool Frequency-domain characterization of EMT models for small-signal stability analysis.pdf`

## 摘要

Z-Tool: Frequency-domain characterization of EMT models for small-signal a Department of Electrical Engineering (ESAT-ELECTA), KU Leuven, 3000, Leuven, Belgium This paper presents a novel frequency-domain identiﬁcation tool based on Electromagnetic Transient (EMT) simulations: Z-tool. This is the ﬁrst open source program oﬀering a versatile automated scan and state-of-the- art small-signal analysis of multi-terminal AC, DC and AC/DC power systems. The approach is introduced with

## 核心贡献



- 开发了首个开源的基于EMT仿真的频域识别工具Z-Tool，支持多端交直流系统的自动化扫描与小信号稳定性分析
- 提出了多频激励与对称性利用等优化策略，显著降低计算耗时，并量化了时间步长依赖下的精度与效率权衡

## 使用的方法


- [[numerical-integration]]
- [[state-space]]
- [[frequency-dependent]]

## 涉及的模型


- [[mmc-model]]
- [[vsc-hvdc]]
- [[hvdc]]

## 相关主题


- [[harmonic]]
- [[passivity]]
- [[network-equivalent]]

## 主要发现



- 基于EMT的频域识别误差具有时间步长依赖性，需在计算效率与模型精度之间进行合理权衡
- 采用多频激励与对称性优化可大幅缩短扫描时间，同时保持对次同步振荡等小信号稳定性评估的准确性

## 方法细节

### 方法概述

提出基于EMT仿真的频域系统识别方法，通过并联理想电压源实现子系统解耦，采用dq坐标系描述三相系统动态，使用正弦扰动信号激励系统，利用FFT提取频域响应构建导纳矩阵。核心创新包括多频激励（Multi-frequency excitation）和对称性利用优化，支持多端AC/DC混合系统（包括3×3 AC/DC导纳矩阵的HVDC换流器）的自动化扫描。通过贪婪算法调度扰动序列，实现对所有网络边缘组件（换流器、电机）的并发识别，显著降低计算耗时。

### 数学公式


**公式1**: $$$T_{dq}(\theta) = \frac{2}{3}\begin{pmatrix} \cos(\theta) & \cos(\theta - 2\pi/3) & \cos(\theta + 2\pi/3) \\ \sin(\theta) & \sin(\theta - 2\pi/3) & \sin(\theta + 2\pi/3) \end{pmatrix}$$$

*幅值不变的abc-to-dq坐标变换矩阵，d轴与a相电压对齐，q轴滞后d轴，用于将三相量转换为旋转坐标系下的直流量，便于小信号分析*


**公式2**: $$$\mathbf{Y}(j\omega) = [\Delta \mathbf{i}_1 \quad \cdots \quad \Delta \mathbf{i}_N][\Delta \mathbf{v}_1 \quad \cdots \quad \Delta \mathbf{v}_N]^{-1}$$$

*导纳矩阵计算公式，通过N个线性独立的电压扰动向量及其对应的电流响应向量，计算N×N维频域导纳矩阵，适用于任意AC/DC子系统*


**公式3**: $$$\Delta v(t) = \sum_{i=1}^{m} a_i \sin(\omega_i t + \phi_i)$$$

*多频（多音）扰动信号表达式，用于同时激励多个频率点以加速扫描，需优化选择相位角φi和幅值ai以最小化波峰因数（Crest Factor）*


### 算法步骤

1. 稳态运行与采样：系统运行至稳态，当freeze变量为1时采样并保持稳态电压电流值作为工作点

2. 子系统解耦：通过理想断路器插入受控并联电压源（零阻抗），断开原始连接以保持各子系统独立运行

3. 快照保存：解耦后创建仿真快照，用于加速后续多次扰动仿真

4. 扰动信号生成：生成正弦单频或多频扰动信号，频率覆盖关注频段（如次同步振荡频段），相位优化以降低波峰因数

5. 正交扰动注入：对每个AC节点注入标准基扰动向量（如Δv₁=[Δv,0]ᵀ, Δv₂=[0,Δv]ᵀ），DC节点注入标量扰动，确保线性独立性

6. 并发测量：利用多端子系统结构，在所有终端同时注入扰动并测量电流响应，通过贪婪算法优化调度序列

7. 频域提取：应用FFT从时域响应中提取频域电压和电流分量Δv(jω)和Δi(jω)

8. 矩阵求逆计算：按公式(2)构造导纳矩阵，通过矩阵求逆得到Y(jω)

9. 稳定性分析：基于识别得到的频域模型进行小信号稳定性评估（如奈奎斯特判据、阻抗比分析）


### 关键参数

- **perturbation_amplitude**: 额定电压的0.02%至2%，电压控制单元建议更小值

- **max_voltage_deviation**: ±5%（正常运行范围）

- **coordinate_transformation**: 幅值不变abc-to-dq变换，d轴对齐a相电压

- **time_step**: EMT仿真时间步长（识别误差具有时间步长依赖性）

- **frequency_range**: 根据研究目标选择（如次同步振荡研究选择特定频段）

- **excitation_type**: 正弦波（优先于PRBS和Chirp信号）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| VSC经长距离串联补偿线路连接系统 | 针对次同步振荡（Sub-synchronous Oscillation）筛选研究，识别系统导纳并评估稳定性，验证了Z-Tool对小信号交互作用的分析能力 | 相比传统单端扫频方法，支持多端同时扫描，实现AC/DC耦合全面表征 |

| MMC-HVDC换流站3×3 AC/DC导纳识别 | 完整识别模块化多电平换流器的3×3维AC/DC导纳矩阵，包含AC侧dq轴与DC侧之间的耦合项 | 克服了现有商业软件（如DIgSILENT PowerFactory频域计算）不考虑电力电子动态影响的局限性 |

| 多频激励优化验证 | 采用多正弦（multi-sine）同时激励多个频率点，相比单频顺序扫描显著减少仿真时间 | 实现显著的时间节省（significant time-savings），具体加速比取决于频率点数量和系统对称性利用程度 |



## 量化发现

- 识别误差具有时间步长依赖性（time-step-dependent），EMT数值积分步长选择需在计算效率与模型精度间权衡
- 推荐扰动幅度范围为额定电压的0.02%至2%，最大电压偏差应控制在±5%以内以保证线性化精度
- 对于电压控制模式下的换流器，建议采用更小的扰动幅度（<0.5%）因其对电压偏差更敏感
- 利用系统对称性（dq对称）可减少50%的所需扰动次数，将仿真时间降低近一半
- 多频激励技术通过同时扫描多个频率点，可将总仿真时间从N×T_single缩短至接近T_single（N为频率点数量）
- Z-Tool支持任意N×N维导纳矩阵识别，其中N为子系统AC/DC节点总数，突破了传统单端扫描限制


## 关键公式

### 频域导纳矩阵识别公式

$$$\mathbf{Y}(j\omega) = [\Delta \mathbf{i}_1 \quad \cdots \quad \Delta \mathbf{i}_N][\Delta \mathbf{v}_1 \quad \cdots \quad \Delta \mathbf{v}_N]^{-1}$$$

*通过N次线性独立电压扰动实验，测量相应电流响应，构建并求逆得到N端口网络在频率ω处的导纳矩阵，适用于AC、DC及AC/DC混合系统*

### Park变换（幅值不变型）

$$$T_{dq}(\theta) = \frac{2}{3}\begin{pmatrix} \cos(\theta) & \cos(\theta - 2\pi/3) & \cos(\theta + 2\pi/3) \\ \sin(\theta) & \sin(\theta - 2\pi/3) & \sin(\theta + 2\pi/3) \end{pmatrix}$$$

*将三相abc坐标系转换为旋转dq坐标系，用于三相AC系统的时不变建模，是小信号稳定性分析的基础*



## 验证详情

- **验证方式**: 基于EMT仿真的案例对比验证，与理论模型和现场工程经验对比
- **测试系统**: 1) VSC经串联补偿长线路系统（次同步振荡研究）；2) MMC-HVDC换流站（多端AC/DC系统）；3) 基础电力系统元件（用于精度-效率权衡分析）
- **仿真工具**: PSCAD/EMTDC（利用其并行计算能力和快照功能），Z-Tool开源程序（Python实现）
- **验证结果**: 验证了Z-Tool对多端系统（包括3×3 AC/DC导纳）的准确识别能力，证实了多频激励和对称性优化在保持精度（误差<典型工程容忍限）前提下显著降低计算耗时，时间步长依赖性误差规律为EMT仿真参数选择提供指导
