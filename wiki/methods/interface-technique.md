---
title: "接口技术 (Interface Technique)"
type: method
tags: [interface, coupling, subnetwork, connection, partitioning]
created: "2026-05-02"
---

# 接口技术 (Interface Technique)

## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

接口技术是 EMT 仿真中连接两个或多个子系统的方法集合。接口可以连接同一 EMT 程序内的分区网络，也可以连接 EMT、机电暂态、控制器、硬件在环或场求解器等不同求解域。它定义接口变量、等值电路、数据交换时序和稳定性处理。

本页是总览页。[[direct-interface-technique]] 只覆盖强耦合矩阵接口；[[electromechanical-electromagnetic-hybrid-simulation]] 只覆盖机电相量域与 EMT 瞬时域的混合仿真；[[hybrid-modeling]] 讨论模型层级组合，不等同于接口算法本身。

## EMT 中的作用

EMT 网络通常按节点电压法或改写后的微分-代数方程推进。接口技术把边界一侧的行为转换为另一侧可接受的输入，常见输入输出包括电压、电流、功率、相量、开关状态和控制信号。接口质量决定了：

- 接口处是否满足电压连续和电流守恒。
- 外部网络频率响应是否在研究频带内被保留。
- 多速率或通信延迟是否造成虚假能量注入。
- 事件、保护动作和控制限幅是否在两侧一致更新。

## 接口变量与等值形式

### 电压型接口

电压型接口向另一侧施加边界电压，常用 Thevenin 形式表达：

$$
v_p(t) = v_{th}(t) - Z_{th} i_p(t)
$$

它适合把外部网络表现为电压源加源阻抗。若源阻抗被忽略，强电压源对强电压源连接可能形成代数冲突或数值振荡。

### 电流型接口

电流型接口向节点注入边界电流，常用 Norton 形式表达：

$$
i_p(t) = i_n(t) - Y_n v_p(t)
$$

它与 EMT 节点电压法匹配较好，因为等效导纳可进入节点矩阵，等效电流进入右端项。若接口侧近似为理想电流源而缺少并联阻尼，开路或弱网条件下可能产生不合理电压。

### 功率型接口

功率型接口交换有功、无功或瞬时功率：

$$
p(t) = v^\mathsf{T}(t)i(t)
$$

在相量域，接口通常使用 $P+jQ$ 与基频电压相量计算等效电流；在 EMT 域，瞬时三相电压电流需要滤波、相量提取或功率平均。功率型接口容易解释能量交换，但会受测量窗、相角参考和不平衡分量影响。

### 多端口等值

多端口接口保留端口间耦合：

$$
i_p(s) = Y_p(s)v_p(s) + i_{hist}(s)
$$

若外部网络的频率相关性重要，$Y_p(s)$ 可由 [[fdne-model]] 或 [[network-equivalent]] 构建。若只保留对角单端口项，可能丢失并行线路、多馈入直流或接地回路的互耦。

## 时间同步与数据交换

接口时序通常有三类：

- 强耦合同步：同一时间步求解统一边界方程，见 [[direct-interface-technique]]。
- 串行松耦合：一侧先推进并把边界量传给另一侧，简单但存在一步或半步延迟。
- 并行松耦合：多侧并行推进，用预测、保持、插值或迭代修正边界量，适合 [[real-time-simulation]] 但需要稳定性检查。

多速率接口需要定义快侧到慢侧的聚合方式和慢侧到快侧的保持方式。常用处理包括零阶保持、线性插值、相量提取、低通滤波和波形松弛。任何处理都应说明采样窗、参考相角、延迟和事件对齐规则。

## 稳定性与一致性检查

接口不是单纯的数据格式转换。最低限度的检查包括：

- 电压、电流方向和基准值一致。
- 接口注入功率在两侧符号约定下闭合。
- 等效导纳或阻抗在目标频带内不引入明显非无源行为。
- 延迟、插值和滤波不会掩盖研究对象的快速动态。
- 故障、开关和控制限幅在两侧时间轴上有明确触发顺序。

若接口基于频域等值，还应检查有理拟合的稳定极点、无源性和时域实现方式。相关背景见 [[vector-fitting]]、[[fdne-model]] 和 [[frequency-scan]]。

## 主要变体

- 等效源接口：Thevenin、Norton 或混合源形式，适合外部网络简化。
- 直接接口：用 Schur 补或补偿方程同步求解边界变量。
- 功率/相量接口：常用于 EMT-机电混合仿真。
- 延迟型接口：利用传输线延迟、离散电感或历史源实现解耦。
- 场路接口：把 [[fdtd]] 或 [[finite-element-method]] 的端口电压、电流、磁链、力或等效阻抗传给电路求解器。
- 工具协同接口：通过 [[co-simulation]] 或模型兼容层交换数据，重点在时间管理和语义一致性。

## 适用边界与失败模式

- 弱耦合接口在强电气耦合、低阻抗连接或快速控制闭环中可能不稳定。
- 相量接口不应直接解释高频谐波、非周期暂态或强不平衡瞬时量，除非提取算法和误差边界已说明。
- 频率相关等值只在拟合频带和端口定义内有效。
- 接口位置过近可能让 EMT 侧畸变直接污染相量域；过远则增加详细 EMT 区域规模。
- 实时接口受通信延迟和固定步长约束，不能仅用离线仿真精度证明。

## 代表性证据与证据边界

接口论文常报告特定算例中的误差、加速比或稳定性改进。这些结论应保留在原算例、步长、端口数、平台和扰动条件内。可作为入口的来源包括 [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb]]、[[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu]]、[[an-interface-method-for-co-simulation-of-emt-model-and-shifted-frequency-emt-mod]] 和 [[co-simulation-of-electromagnetic-transients-and-phasor-models-a-relaxation-appro]]。

## 与相关页面的关系

- [[direct-interface-technique]]：强耦合分区接口。
- [[hybrid-modeling]]：模型层级和物理域组合。
- [[electromechanical-electromagnetic-hybrid-simulation]]：机电相量域与 EMT 瞬时域接口。
- [[model-compatibility-layer]]：工具间模型语义和参数映射。
- [[offline-to-realtime-porting]]：离线模型迁移到实时平台时的接口约束。
- [[emt-simulation-verification]]：接口误差的验证和证据边界。
