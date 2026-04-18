---
title: "Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Open Journal of Power Electronics;2023;4; ;10.1109/OJPEL.2023.3297449"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/32/Zhang 等 - 2023 - Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models.pdf"]
---

# Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models

**作者**: 
**年份**: 2023
**来源**: `32/Zhang 等 - 2023 - Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models.pdf`

## 摘要

The proliferation of artiﬁcial intelligence (AI) has opened up new avenues for the modeling of power electronics with ultra-fast transient responses, such as wide-bandgap (WBG) devices. This arti- cle highlights the signiﬁcance of ultra-fast transient device-level hardware emulation for the DC railway microgrid (DRM) in real-time. To this end, the proposed approach partitions the DRM power system by transmission line method (TLM) and employs gated recurrent unit (GRU) and electromagnetic transient (EMT) modeling techniques for system-level subsystems. Meanwhile, for WBG devices, gallium nitride (GaN) high electron mobility transistors (HEMT) and silicon carbide (SiC) insulated gate bipolar transistors (IGBT) are modeled using a novel physical feature neuron network (PFNN), which offers hig

## 核心贡献


- 提出物理特征神经网络模型，实现宽禁带器件纳秒级变步长高精度建模
- 采用传输线法对直流铁路微电网解耦，结合门控循环单元实现系统级并行仿真
- 构建基于FPGA的器件级机器学习与系统级电磁暂态混合实时硬件在环架构


## 使用的方法


- [[传输线法-tlm|传输线法(TLM)]]
- [[门控循环单元-gru|门控循环单元(GRU)]]
- [[电磁暂态-emt-建模|电磁暂态(EMT)建模]]
- [[物理特征神经网络-pfnn|物理特征神经网络(PFNN)]]
- [[fpga并行计算|FPGA并行计算]]
- [[硬件在环-hil-仿真|硬件在环(HIL)仿真]]


## 涉及的模型


- [[直流铁路微电网-drm|直流铁路微电网(DRM)]]
- [[氮化镓高电子迁移率晶体管-gan-hemt|氮化镓高电子迁移率晶体管(GaN HEMT)]]
- [[碳化硅绝缘栅双极型晶体管-sic-igbt|碳化硅绝缘栅双极型晶体管(SiC IGBT)]]
- [[宽禁带功率器件|宽禁带功率器件]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环|硬件在环]]
- [[机器学习加速建模|机器学习加速建模]]
- [[变步长仿真|变步长仿真]]
- [[fpga并行架构|FPGA并行架构]]
- [[功率器件级建模|功率器件级建模]]


## 主要发现


- 新模型实现纳秒级变步长仿真，精度与商业离线软件结果高度一致
- 相比传统固定步长网络，新方法显著提升宽禁带器件超快暂态过程的计算效率
- 基于传输线解耦与FPGA并行架构，成功实现直流微电网系统级实时稳定运行



## 方法细节

### 方法概述

本文提出了一种分层混合实时仿真架构，用于直流铁路微电网(DRM)的硬件在环(HIL)仿真。在系统级，采用传输线法(TLM)对DRM电力系统进行分区解耦，结合门控循环单元(GRU)和电磁暂态(EMT)建模技术处理系统级子网络。在器件级，针对宽禁带(WBG)器件（氮化镓高电子迁移率晶体管GaN HEMT和碳化硅绝缘栅双极型晶体管SiC IGBT），提出物理特征神经网络(PFNN)模型。PFNN通过提取波形物理特征点（拐点、峰值、谷值）而非固定时间步长采样，实现变步长（低至1ns）的高精度建模。整个系统在Xilinx Ultrascale+ FPGA平台上实现并行加速，通过分段线性化在关键特征点间插值生成纳秒级分辨率波形，解决了传统固定步长方法在纳秒级瞬态仿真中的计算资源消耗和延迟问题。

### 数学公式


**公式1**: $$$v(t) = v_i + \frac{v_{i+1}-v_i}{t_{i+1}-t_i}(t-t_i), \quad t_i \leq t < t_{i+1}$$$

*分段线性化插值公式，用于在PFNN输出的关键特征点$(t_i, v_i)$和$(t_{i+1}, v_{i+1})$之间插入中间数据点，以生成所需时间分辨率（如1ns或10ns）的连续波形*


**公式2**: $$$\mathbf{y}_{t} = f_{NN}(\mathbf{x}_{t-1}, \mathbf{x}_{t-2}, ..., \mathbf{x}_{t-n}; \mathbf{W}, \mathbf{b})$$$

*PFNN前向计算方程，其中$\mathbf{x}$为历史电压/电流输入向量，$\mathbf{y}$为当前时刻输出（包含关键数据点的时间和幅值），$f_{NN}$为前馈神经网络映射函数*


### 算法步骤

1. 原始数据采集：构建3D数据集$\{(v, i, t)\}$，包含器件开关瞬态过程中的电压、电流和时间信息，覆盖GaN HEMT约10ns的开关瞬态过程

2. 物理特征提取：基于器件物理特性对原始数据进行筛选，识别并提取关键特征点（波形拐点、峰值点、谷值点），剔除冗余的平稳段数据，构建压缩的2D电压-时间（或电流-时间）数据集

3. 神经网络训练：使用全连接前馈神经网络(FNN)训练PFNN模型，输入为历史时刻的电压/电流状态，输出为下一个关键特征点的坐标$(t_k, v_k)$或$(t_k, i_k)$

4. TLM分区解耦：采用传输线法将DRM系统划分为多个子网络，在接口处设置延迟，使各子网络可独立并行计算

5. 系统级EMT计算：使用GRU-EMT混合方法计算系统级慢变动态，采用较大时间步长（约10μs）

6. 器件级PFNN并行计算：在FPGA上并行执行PFNN推理，一次性输出关键特征点序列$\{(t_1,v_1), (t_2,v_2), ..., (t_n,v_n)\}$，避免传统逐点迭代的顺序依赖

7. 波形重构：通过分段线性化方法在关键特征点之间插值，生成时间步长为1ns或10ns的高分辨率瞬态波形，满足实时HIL仿真输出要求


### 关键参数

- **minimum_time_step**: 1ns（PFNN变步长模式下可达的最小等效时间分辨率）

- **fixed_time_step_ftpnn**: 20ns或50ns（FTPNN方法的固定时间步长示例）

- **ftpnn_data_points**: 50个数据点（用于表示1μs瞬态波形，步长20ns）或20个数据点（步长50ns）

- **gan_transient_duration**: 约10ns（GaN HEMT开关瞬态持续时间）

- **system_level_timestep**: 约10μs（传统EMT系统级仿真典型步长）

- **fpga_platform**: Xilinx Ultrascale+架构

- **tline_delay**: 传输线法分区引入的接口延迟，用于解耦并行计算



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| GaN HEMT开关瞬态实时仿真 | PFNN方法成功实现了纳秒级瞬态波形实时仿真，可捕捉约10ns持续时间的开关过程。通过输出关键物理特征点后插值，相比固定时间步长方法显著降低了FPGA硬件资源消耗，同时保持与SaberRD离线仿真一致的波形细节 | 相比FTPNN方法，PFNN在保持相同精度的前提下，通过减少输出数据点数量（仅输出拐点而非全时段数据），显著降低了硬件资源占用和计算延迟；相比传统EMT点对点计算，实现了并行加速，突破了顺序迭代的瓶颈 |

| DRM系统级实时HIL仿真 | 采用TLM分区的GRU-EMT混合模型在FPGA上实现了实时仿真，系统级动态响应与PSCAD/EMTDC离线仿真结果一致，验证了ML加速的WBG器件模型在复杂微电网环境中的有效性 | 与PSCAD/EMTDC（系统级）和SaberRD（器件级）离线仿真对比，验证了实时HIL仿真的准确性；相比传统固定步长方法，PFNN实现了变步长（1ns-μs范围）的灵活建模能力 |



## 量化发现

- PFNN支持变步长仿真，最低等效时间分辨率可达1ns，满足GaN HEMT纳秒级开关瞬态建模需求
- 传统EMT点对点计算在10μs系统级步长下难以解析10ns级器件瞬态（时间尺度相差1000倍），PFNN通过物理特征提取解决了这一多时间尺度仿真难题
- FTPNN方法在1μs瞬态过程中需输出20-50个固定间隔数据点（对应20ns或50ns步长），而PFNN通过智能选择特征点，在波形变化平缓时段大幅减少输出数据量，降低FPGA资源消耗
- GaN HEMT开关瞬态持续时间约为10ns，要求仿真步长至少小于该值的1/10（即<1ns）才能准确捕捉，PFNN通过分段线性化插值实现了这一需求
- 相比LSTM网络，GRU在保持相近精度的同时减少了约25-33%的门控参数数量，更适合FPGA实时实现
- TLM分区使DRM系统可分解为多个独立子网络，各子网络可在FPGA上并行计算，整体加速比与子网络数量成正比


## 关键公式

### 分段线性化波形重构公式

$$$v(t) = v_i + \frac{v_{i+1}-v_i}{t_{i+1}-t_i}(t-t_i)$$$

*在PFNN输出关键特征点$(t_i, v_i)$后，用于在两个特征点之间插值生成高分辨率（1ns或10ns步长）的连续电压波形，实现变步长到固定步长的转换*

### PFNN前馈神经网络输出层计算

$$$\hat{y} = \sigma(\mathbf{W}_{out} \cdot \tanh(\mathbf{W}_{h} \cdot \mathbf{h} + \mathbf{b}_h) + \mathbf{b}_{out})$$$

*PFNN使用简化的FNN结构（而非复杂RNN/LSTM），通过权重矩阵$\mathbf{W}$和偏置$\mathbf{b}$将历史状态映射到下一个物理特征点的预测值，$\sigma$为激活函数*



## 验证详情

- **验证方式**: 对比验证（Comparison-based validation）：将实时HIL仿真结果与成熟商业软件离线仿真结果进行波形对比和误差分析
- **测试系统**: 直流铁路微电网(DRM)系统，包含GaN HEMT和SiC IGBT宽禁带功率器件的电力电子变换器、传输线分区接口、以及系统级微电网网络
- **仿真工具**: 系统级验证：PSCAD/EMTDC（用于对比系统级暂态响应）；器件级验证：SaberRD（用于对比GaN HEMT和SiC IGBT的纳秒级开关瞬态波形）；实时硬件平台：基于Xilinx Ultrascale+ FPGA的实时仿真器
- **验证结果**: 所提出的PFNN方法在FPGA上成功实现了器件级纳秒瞬态与系统级微秒动态的混合实时仿真。与SaberRD的器件级仿真结果相比，PFNN准确再现了开关波形的关键特征（拐点、峰值）；与PSCAD/EMTDC的系统级仿真结果相比，GRU-EMT混合模型准确捕捉了系统级动态响应。验证了机器学习加速的WBG器件模型在实时HIL应用中的可行性和准确性，特别是在处理10ns级超快瞬态时的变步长优势。
