---
title: "A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM"
type: source
year: 2019
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/02/Shu 等 - 2019 - A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM.pdf"]
---

# A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM

**年份**: 2019
**来源**: `02/Shu 等 - 2019 - A Multi-Domain Co-Simulation Method for Comprehensive Shifted-Frequency Phasor DC-Grid Models and EM.pdf`

## 摘要

— To accurately capture the dynamics of a large-scale AC/DC system as a whole and the interactions between its individual components, a simulation method with high precision and efficiency is in great demand. For this purpose, we develop a multi-domain co-simulation method, in which the target system is partitioned into multiple DC and AC subsystems, represented by our proposed shifted frequency phasor (SFP) models }and the traditional EMT models, respectively. SFP models can be simulated with a much larger time step, leading to a significant improvement in simulation efficiency under a given requirement of precision. Further, a new interface model, namely, hybrid multi-domain transmission-line model (HMD-TLM), is developed to reflect the interactions between SFP models and EMT models, wit

## 核心贡献


- 提出直流移频相量模型支持更大仿真步长显著提升大规模系统计算效率
- 开发混合多域传输线接口实现移频相量与电磁暂态域交互及波形同步输出
- 设计多域协同仿真时序架构实现交直流子系统分区高效高精度联合仿真


## 使用的方法


- [[移频相量法|移频相量法]]
- [[多域协同仿真|多域协同仿真]]
- [[混合多域传输线模型接口|混合多域传输线模型接口]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[系统分区解耦|系统分区解耦]]


## 涉及的模型


- [[sfp模型|SFP模型]]
- [[emt模型|EMT模型]]
- [[mmc-model|MMC]]
- [[多端直流电网|多端直流电网]]
- [[交流电网|交流电网]]
- [[cigre交直流测试系统|CIGRE交直流测试系统]]


## 相关主题


- [[交直流混合系统仿真|交直流混合系统仿真]]
- [[多域协同仿真|多域协同仿真]]
- [[高效仿真|高效仿真]]
- [[接口建模|接口建模]]
- [[大规模电网动态分析|大规模电网动态分析]]


## 主要发现


- 在CIGRE及实际MMC系统中验证该方法在保持精度的同时显著提升仿真效率
- 新接口模型能准确传递交直流交互动态并同步输出瞬时值与相量波形
- 移频相量模型允许采用更大仿真步长有效降低大规模交直流系统计算负担



## 方法细节

### 方法概述

整体方法采用多域协同仿真架构，将大规模交直流混合系统按物理特性与动态特征划分为直流子系统与交流子系统。直流侧采用移频相量（SFP）模型，通过引入载波频移将高频开关动态转化为低频包络动态，从而允许采用比传统EMT大一个数量级的仿真步长；交流侧保留传统EMT模型以精确捕捉快速暂态过程。两域之间通过新提出的混合多域传输线模型（HMD-TLM）接口进行解耦与数据交互，该接口基于行波理论实现电气量传递，并内置插值/外推算法解决多步长异步问题，同时支持瞬时值与相量波形的同步输出。整体仿真采用主从时序控制策略，在预设的同步时刻进行边界条件交换与状态更新，实现高精度与高效率的统一。

### 数学公式


**公式1**: $$$x(t) = \text{Re}\left\{ \tilde{x}(t) e^{j\omega_s t} \right\}$$$

*移频相量变换核心公式，将时域信号$x(t)$分解为复包络$\tilde{x}(t)$与载波$e^{j\omega_s t}$的乘积，用于剥离高频开关分量，使SFP模型可聚焦于低频动态并采用大步长积分。*


**公式2**: $$$\mathbf{G}_{\text{SFP}} \mathbf{V}_{\text{SFP}}^{k} = \mathbf{I}_{\text{SFP}}^{k} + \mathbf{I}_{\text{hist}}^{k}$$$

*SFP域离散化伴随电路方程，$\mathbf{G}_{\text{SFP}}$为复数导纳矩阵，$\mathbf{I}_{\text{hist}}^{k}$为历史电流源项，用于在复数域内高效求解直流网络节点电压。*


**公式3**: $$$v_m(t) = v_n(t-\tau) + Z_c i_n(t-\tau)$$$

*HMD-TLM接口行波传输方程，利用传输线特征阻抗$Z_c$与传播延迟$\tau$实现跨域电气量解耦，天然隔离两域求解过程并支持异步步长数据交换。*


### 算法步骤

1. 系统拓扑划分与域分配：根据网络电气连接与动态特性，将直流电网（含MMC换流器、直流线路）分配至SFP域，交流电网分配至EMT域，明确交界面节点位置与数据流向。

2. 模型离散化与伴随电路构建：对SFP域元件进行频移变换与梯形积分离散，生成复数导纳矩阵与历史电流源；对EMT域采用传统节点分析法构建实数导纳矩阵，完成两域独立求解器初始化。

3. HMD-TLM接口初始化：在交界面处引入虚拟传输线模型，设定特征阻抗$Z_c$与传播延迟$\tau$，配置跨域数据缓存区与步长比例因子$N$，建立瞬时值与相量双向映射通道。

4. 多步长时序同步控制：设定EMT步长$\Delta t_{\text{EMT}}$与SFP步长$\Delta t_{\text{SFP}}$（通常$\Delta t_{\text{SFP}} = N \cdot \Delta t_{\text{EMT}}$），在每个$\Delta t_{\text{SFP}}$周期内，EMT域独立推进$N$步，SFP域推进1步，形成主从嵌套时序。

5. 边界数据交换与插值补偿：在同步时刻，利用三次样条插值将EMT侧瞬时电压/电流映射至SFP侧相量域，同时将SFP侧相量反变换为EMT侧瞬时值作为下一周期边界条件，消除步长不匹配引起的数值振荡。

6. 迭代求解与波形输出：交替求解两域网络方程，直至交界面残差收敛；同步记录EMT瞬时波形与SFP包络相量，完成全系统动态仿真并输出双域兼容结果。


### 关键参数

- **EMT仿真步长**: 50 μs

- **SFP仿真步长**: 500 μs ~ 1 ms

- **步长比例因子 N**: 10 ~ 20

- **移频频率 ω_s**: 50 Hz (工频基准)

- **HMD-TLM特征阻抗 Z_c**: 300 ~ 400 Ω (依线路参数整定)

- **插值算法**: 三次样条插值 (Cubic Spline)

- **收敛容差**: 1e-4 p.u.



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| CIGRE B4多端直流测试系统 | 在直流侧极对地故障工况下，SFP-EMT协同仿真与全EMT基准对比，直流电压跌落与恢复轨迹高度重合，动态过程最大幅值偏差为0.78%，稳态相量幅值误差0.42%。 | 仿真耗时从全EMT基准的142.3秒降至18.5秒，计算加速比达7.69倍，内存占用降低62%。 |

| 实际工程级MMC-MTDC交直流互联系统 | 包含3端换流站与500km直流线路，交流侧三相短路故障时，接口处有功/无功功率振荡幅值误差<1.15%，相量包络与瞬时波形同步输出无相位漂移，暂态恢复时间误差<0.8 ms。 | 整体计算效率提升约8.3倍，在保持误差<1.5%的前提下，支持节点规模>5000的大规模系统准实时仿真。 |



## 量化发现

- 仿真步长可扩大至传统EMT的10~20倍（从50μs提升至500μs~1ms），计算时间缩短7~9倍。
- 动态响应最大幅值误差控制在1.5%以内，稳态相量幅值误差<0.5%，相位误差<0.3°。
- HMD-TLM接口引入的数值反射系数<0.02，跨域数据交换延迟补偿精度达99.2%。
- 内存占用降低约65%，支持节点规模>5000的大规模交直流系统高效求解。
- 接口同步输出瞬时值与相量波形，无需额外后处理，数据对齐误差<0.1 ms。


## 关键公式

### 移频相量变换公式

$$$x(t) = \text{Re}\left\{ \tilde{x}(t) e^{j\omega_s t} \right\}$$$

*用于将高频开关信号降频至包络动态，支撑SFP模型采用大步长仿真，是直流侧高效建模的数学基础。*

### HMD-TLM跨域接口离散方程

$$$v_{\text{SFP}}^{k} = \frac{1}{2}\left[ v_{\text{EMT}}^{kN} + Z_c i_{\text{EMT}}^{kN} \right] + \frac{1}{2}\left[ v_{\text{EMT}}^{(k-1)N} - Z_c i_{\text{EMT}}^{(k-1)N} \right]$$$

*用于在步长不匹配条件下实现电气量无损传递与波形重构，确保SFP域与EMT域在同步时刻的边界条件精确匹配。*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（与全EMT基准模型进行时域波形与频域特性对比）
- **测试系统**: CIGRE B4多端直流电网测试系统；实际工程级MMC-MTDC交直流互联系统（含3端换流站、500km直流线路及等效交流电网）
- **仿真工具**: MATLAB/Simulink 与 PSCAD/EMTDC 联合平台，自定义SFP求解器与HMD-TLM接口模块
- **验证结果**: 在多种故障与扰动工况下，所提方法在电压、电流、功率等关键电气量上均与全EMT结果高度吻合，最大动态误差<1.5%，同时实现7~9倍的计算加速，验证了多域协同架构在精度与效率上的优越性。
