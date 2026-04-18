---
title: "A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT and Transient Stability"
type: source
year: 2017
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/TPWRD.2017.2690145.pdf.pdf"]
---

# A Novel Interfacing Technique for Distributed Hybrid Simulations Combining EMT and Transient Stability

**年份**: 2017
**来源**: `03/TPWRD.2017.2690145.pdf.pdf`

## 摘要

—The steady increase of power electronic devices and nonlinear dynamic loads in large scale AC/DC systems desperately requires an efﬁcient simulation method. However, the traditional hybrid simulation, which incorporates various components into a single EMT subsystem, causes great difﬁculty in network partitioning and signiﬁcant deterioration in simu- lation efﬁciency. To resolve these issues, a distributed hybrid simulation method is proposed in this paper. The key factor leading the success of this method is a distinct interfacing technique, which includes: i) a new approach based on the two- level Schur complement to update the interfaces by taking full consideration of the couplings between different EMT subsys- tems; and ii) a combined interaction protocol to further improve the efﬁci

## 核心贡献


- 提出基于两级舒尔补的接口更新策略，充分计及多EMT子系统间动态耦合
- 构建三相戴维南与三序诺顿等效接口模型，突破传统三相平衡假设限制
- 设计组合式交互协议实现多程序并行协调，显著提升大规模系统仿真效率


## 使用的方法


- [[分布式混合仿真|分布式混合仿真]]
- [[两级舒尔补法|两级舒尔补法]]
- [[节点分析法|节点分析法]]
- [[组合交互协议|组合交互协议]]
- [[网络等值|网络等值]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[非线性动态负荷|非线性动态负荷]]
- [[同步电机|同步电机]]
- [[输电线路|输电线路]]
- [[机电暂态模型|机电暂态模型]]
- [[电磁暂态模型|电磁暂态模型]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[分布式仿真|分布式仿真]]
- [[网络等值|网络等值]]
- [[接口技术|接口技术]]
- [[并行协调仿真|并行协调仿真]]
- [[vsc-model|VSC]]


## 主要发现


- IEEE 39节点及实际系统验证表明，该方法精度与效率显著优于传统混合仿真
- 舒尔补策略有效消除多EMT子系统耦合误差，避免网络划分不当引发的数值失稳
- 组合交互协议在保证接口数据同步精度的同时，大幅降低了多机通信与计算开销



## 方法细节

### 方法概述

本文提出一种面向大规模交直流系统的分布式混合仿真接口技术。该方法将电网划分为一个机电暂态（TS）中心子系统和多个电磁暂态（EMT）子系统，各子系统独立部署于局域网计算机上并行求解。接口建模方面，EMT子系统采用三相戴维南等效，TS子系统采用三序诺顿等效，彻底突破传统三相平衡假设限制。核心创新包含两点：一是基于两级舒尔补（Two-level Schur complement）的接口参数更新策略，通过对全局分块导纳矩阵进行同步消元，充分计及多个EMT子系统间的动态耦合及与TS子系统的交互，消除传统方法忽略跨子系统耦合导致的数值失稳；二是设计组合式交互协议，根据接口电流相对变化率动态切换串行与并行通信模式，在暂态过程保证高精度同步，在稳态过程大幅降低通信与计算开销，实现精度与效率的自适应平衡。

### 数学公式


**公式1**: $$$\tilde{Z}_j^{abc} = \tilde{R}_{e,j}^{abc} + j\omega \tilde{L}_{e,j}^{abc}$$$

*计算第j个EMT子系统接口的三相戴维南等效阻抗矩阵*


**公式2**: $$$\tilde{V}_j^{abc} = V_{e,j}^{abc} + \tilde{Z}_j^{abc} I_{e,j}^{abc}$$$

*基于TS侧接口电压电流相量计算戴维南等效电压相量*


**公式3**: $$$\tilde{v}_{lj} = \tilde{V}_{jl} \cos(\delta + \tilde{\theta}_{jl})$$$

*将戴维南电压相量转换为瞬时值，用于EMT侧时域求解*


**公式4**: $$$\frac{d}{dt} i_{e,j}^{abc} = [\tilde{L}_{e,j}^{abc}]^{-1} (v_{e,j}^{abc} - \tilde{R}_{e,j}^{abc} i_{e,j}^{abc} - \tilde{v}_j^{abc})$$$

*接口支路微分方程，采用隐式梯形法离散后融入EMT节点导纳矩阵*


**公式5**: $$$I_j^{120} = I_{t,j}^{120} + Y_j^{120} V_{t,j}^{120}$$$

*计算TS子系统接口的三序诺顿等效电流源*


**公式6**: $$$Y_j^{120} = [R_{t,j}^{120} + j\omega L_{t,j}^{120}]^{-1}$$$

*计算TS子系统接口的三序诺顿等效导纳矩阵*


**公式7**: $$$\Delta(t_k) = \max_{j,l} \left\{ \frac{|I_{e,lj}(t_k) - I_{e,lj}(t_{k-1})|}{|I_{e,lj}(t_{k-1})|} \right\}$$$

*计算所有EMT接口各相电流的相对变化率，作为组合协议切换判据*


**公式8**: $$$\begin{bmatrix} Y_{11}^{abc} & \cdots & \bar{Y}_{1t}^{abc}S^{-1} \\ \vdots & \ddots & \vdots \\ Y_{t1}^{120}S & \cdots & Y_{tt}^{120} \end{bmatrix} \begin{bmatrix} V_{emt,1}^{abc}(t_k) \\ \vdots \\ V_{TS}^{120}(t_k) \end{bmatrix} = \begin{bmatrix} I_{emt,1}^{abc}(t_k) \\ \vdots \\ I_{TS}^{120}(t_k) \end{bmatrix}$$$

*全局网络分块导纳方程，作为两级舒尔补消元求解等效参数的基础*


### 算法步骤

1. 系统初始化与网络划分：基于潮流计算获取初始运行点，将目标系统划分为1个中心TS子系统和N个EMT子系统，选取电力电子设备与非线性负荷的公共耦合点（PCC）作为接口边界。

2. 步长配置：为所有EMT子系统设置统一小步长$h$（典型值10-100µs），为TS子系统设置大步长$h_{ts}$，计算步长比$n = h_{ts}/h$。

3. 交互判据计算：在每个交互时刻$t_k$，采集所有EMT子系统各相接口电流$I_{e,lj}$，按公式计算最大相对变化率$\Delta(t_k)$。

4. 动态协议路由：若$\Delta(t_k) > \varepsilon$，触发串行协议：TS向EMT传输数据→更新各EMT戴维南参数→EMT子系统并行推进$n$步→EMT向TS回传数据→TS推进1步。若$\Delta(t_k) \le \varepsilon$，触发并行协议：TS与EMT完全并行推进各自步长，在$t_{k+1}$时刻同步交换接口参数。

5. 两级舒尔补参数更新：构建全局分块导纳矩阵，利用两级舒尔补法同步消去各子系统内部节点，求解计及多EMT间耦合的戴维南等效电压/阻抗及TS侧诺顿等效参数。

6. 循环迭代与终止：重复步骤3-5，直至仿真时间达到$T_{max}$，输出各子系统动态响应数据。


### 关键参数

- **EMT仿真步长(h)**: 10-100 µs

- **TS仿真步长(h_ts)**: 由步长比n决定，通常远大于h

- **步长比(n)**: n = h_ts / h，根据精度与数值稳定性要求选取

- **协议切换阈值(ε)**: 2%-10%（每交互步的接口电流相对变化率）

- **接口等效模型**: EMT侧：三相戴维南等效；TS侧：三序诺顿等效

- **数值积分算法**: 隐式梯形法（Implicit Trapezoidal Algorithm）

- **通信协议**: 局域网TCP/UDP Socket Server



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进型IEEE 39节点系统 | 系统包含两端VSC-HVDC及非线性动态负荷。在不对称故障与大扰动工况下，验证了分布式混合仿真的动态响应精度。接口电流变化率阈值ε设定为5%时，组合协议在暂态期自动切换至串行模式，稳态期切换至并行模式。 | 相比传统单EMT子系统混合仿真，网络划分难度显著降低，避免了因划分不当引发的数值失稳；两级舒尔补策略消除了多EMT耦合误差，整体仿真精度与全EMT基准一致，但计算效率提升显著。 |

| 实际大规模交直流混合系统 | 含多端电力电子换流器与复杂非线性负荷。验证了组合交互协议在稳态与暂态切换过程中的自适应能力。EMT步长设为50µs，TS步长比n=10，通信开销在稳态阶段降低约50%以上。 | 组合协议使稳态/缓变过程的通信频率大幅降低，暂态过程保持串行高精度同步。整体仿真速度较传统串行混合仿真提升显著，接口数据同步误差控制在工程允许范围内，有效解决了传统方法效率恶化问题。 |



## 量化发现

- 接口电流相对变化率阈值ε设定为2%-10%时，可实现仿真精度与计算效率的最优平衡。
- EMT子系统采用10-100µs小步长，TS子系统步长比n=h_ts/h可根据系统动态特性灵活配置，保证数值稳定性。
- 两级舒尔补更新策略完全消除了多EMT子系统间动态耦合带来的接口等效误差，避免了传统方法因忽略耦合导致的数值发散。
- 组合交互协议在稳态阶段采用并行模式，多机通信与计算开销降低50%以上；在暂态阶段切换至串行模式，接口数据同步精度与全EMT仿真一致。
- 实际系统验证表明，该方法在保持与全EMT仿真同等精度的前提下，显著降低了网络划分难度与整体计算时间，仿真效率较传统混合方法提升显著。


## 关键公式

### 接口电流变化率判据公式

$$$\Delta(t_k) = \max_{j,l} \left\{ \frac{|I_{e,lj}(t_k) - I_{e,lj}(t_{k-1})|}{|I_{e,lj}(t_{k-1})|} \right\}$$$

*用于组合交互协议中动态切换串行与并行仿真模式，实时判断系统处于暂态还是稳态，决定数据交换时序。*

### 全局网络分块导纳方程（两级舒尔补基础）

$$$\begin{bmatrix} Y_{jj}^{abc} & \cdots & \bar{Y}_{jt}^{abc}S^{-1} \\ \vdots & \ddots & \vdots \\ Y_{tj}^{120}S & \cdots & Y_{tt}^{120} \end{bmatrix} \begin{bmatrix} V_{emt,j}^{abc}(t_k) \\ \vdots \\ V_{TS}^{120}(t_k) \end{bmatrix} = \begin{bmatrix} I_{emt,j}^{abc}(t_k) \\ \vdots \\ I_{TS}^{120}(t_k) \end{bmatrix}$$$

*在每次交互迭代时构建，通过两级舒尔补消去内部节点，同步求解考虑多EMT耦合的戴维南/诺顿等效参数，是接口更新的核心数学基础。*



## 验证详情

- **验证方式**: 数字仿真对比验证（与传统混合仿真及全EMT仿真进行精度与效率对比）
- **测试系统**: 改进型IEEE 39节点系统、实际大规模交直流混合系统（均含两端VSC-HVDC及非线性动态负荷）
- **仿真工具**: 分布式仿真平台（基于局域网TCP/UDP Socket通信，TS与EMT程序独立部署于多台计算机并行执行，EMT侧采用节点分析法与隐式梯形法）
- **验证结果**: 仿真结果表明，所提接口技术成功克服了传统混合仿真中网络划分困难、多EMT子系统耦合误差大及效率低下的问题。组合协议实现了精度与效率的自适应平衡，两级舒尔补更新策略保证了接口等效的高保真度，验证了该方法在大规模电力电子化电网暂态分析中的有效性与工程实用性。
