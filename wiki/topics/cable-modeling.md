---
title: "电缆建模 (Cable Modeling)"
type: topic
tags: [cable, underground-cable, submarine-cable, skin-effect, frequency-dependent]
created: "2026-04-14"
---

# 电缆建模 (Cable Modeling)

## 定义与概述

电缆建模研究地下电缆、海底电缆和混合架空-电缆线路在 EMT 仿真中的参数计算、频率相关效应和时域实现。与架空线路相比，电缆具有导体、绝缘、屏蔽、护套、铠装和土壤/海水回路等多层结构，集肤效应、邻近效应、护套回流和介质损耗会显著影响暂态传播。

在 EMT 语境下，电缆模型通常需要在宽频精度、数值稳定性和计算成本之间折中。工频或慢暂态可使用固定参数模型；雷电、开关冲击、直流故障行波和 VSC-HVDC 宽频振荡则需要频率相关模型。

## 作用机制

电缆模型通常先在频域获得单位长度阻抗矩阵和导纳矩阵：

$$
Z(s)=R(s)+sL(s), \qquad Y(s)=G(s)+sC(s)
$$

随后再转换为适合时域 EMT 的形式。常见机制包括：

- **频变参数计算**：考虑导体集肤效应、邻近效应、护套/铠装回流、大地或海水返回路径。
- **多导体传输线模型**：在相域或模域处理芯线、护套和铠装之间的耦合。
- **矢量拟合与有理逼近**：把频域阻抗、导纳或传播函数拟合为可在时域递推的有理函数。
- **状态空间实现**：将拟合结果写成状态方程，便于和 [[state-space-method|状态空间法]] 或 [[fdne-model|频变网络等值]] 接口。
- **宽频/ULM 类模型**：在传播时延、模态变换和无源性之间做平衡，适用于长电缆和混合线路。
- **测量融合**：当几何参数不足以解释高频传播时，可用阻抗测量、S 参数或时域反射数据修正模型。

## 适用边界

- 固定参数电缆模型适合工频、准稳态和低频控制研究，但不应直接用于快速暂态或行波保护精度判断。
- 频率相关模型适合雷电冲击、开关暂态、VSC-HVDC 宽频相互作用和长距离电缆传播问题。
- 三芯、铠装、交叉互联或共沟敷设电缆需要显式考虑导体间耦合；单芯简化模型不一定适用。
- 频域拟合模型必须检查稳定性和无源性，否则在闭环 HIL 或长时域仿真中可能出现非物理发散。
- 电缆参数依赖几何、材料、敷设方式和环境；缺少证据时应避免给出固定的宽频误差或通用参数。

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an underground transmission cable]] | 2005 | 讨论地下电缆快速暂态中的邻近效应。 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2009 | 线路与电缆参数计算工具。 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-conductor cable modeling with inclusion of measured coaxial wave propagation]] | 2022 | 将测量传播特性纳入多导体电缆模型。 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core armoured cables]] | 2023 | 关注三芯铠装电缆的螺线管效应。 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 | 海底埋设电缆的时域建模。 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-Delay Estimation Through All-Pass Functions for ULM Line and Cable Models]] | 2025 | ULM 线路/电缆模型的时延估计。 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and rational Krylov fitting]] | 2026 | 宽频电缆/线路模型的降阶拟合。 |
| [[validation-of-frequency-dependent|Validation of frequency-dependent]] | 2026 | 频率相关模型验证。 |

## 技术演进脉络

### 1999-2005年：早期线路建模探索
- **小波变换多分辨率线路模型** (2001)
  - 突破J. Marti模型模变换矩阵常数假设，利用DWT实现多分辨率时域仿真
- **非均匀线路(NUL)建模** (2001)
  - 基于链式矩阵乘法处理参数随距离变化特性，扩展线路模型适用范围
- **混合换位线路模型** (2001)
  - 利用连续换位特性简化频域矩阵，提升多导体线路仿真效率

### 2006-2010年：模型稳定性贡献
- **ULM无源性强制方法** (2008)
  - 解决有理函数带外逼近误差导致的数值不稳定，三层防御策略确保稳定性
- **数值稳定性改进方法** (2010)
  - 基于留极点比值约束的频域拟合，消除宽频模型时域失稳问题

### 2011-2015年：状态空间与并行计算
- **状态空间π型线路模型** (2011)
  - 采用级联π型电路空间离散化，RL模块拟合频变参数
- **平行线路模态解耦** (2012)
  - 解耦与宽频有理拟合结合，解决平行线路互感耦合精度问题
- **FPGA实时非线性求解器** (2011)
  - 补偿法解耦非线性元件，实现迭代式实时电磁暂态求解

### 2016-2020年：多层土壤与全频变建模
- **多层大地广义参数框架** (2021)
  - 突破Carson假设，严格推导多层大地返回阻抗与导纳
- **全频变FLE延迟利用模型** (2017)
  - 折叠线等效与延迟利用结合，降低大规模仿真计算复杂度
- **频域双端口模态解耦评估** (2017)
  - 系统评估实常数变换矩阵近似精度与线路长度关系

### 2021-2026年：开源实现与测量融合
- **ULM在ATP开源实现** (2021)
  - 两阶段混合架构实现免费平台的通用线路模型
- **大地返回导纳电缆模型** (2021)
  - 准TEM近似闭式解析替代Pollaczek积分，提升埋地电缆仿真效率
- **宽频Krylov降阶拟合** (2026)
  - 恒变矩阵与有理Krylov拟合结合，实现宽频模型高效降阶

## 关键发现汇总

### 建模精度与效率权衡
- **[2001]** 小波变换多分辨率分析可突破常数模变换矩阵限制，提升非均匀线路精度
- **[2008]** ULM无源性强制三层防御策略可有效消除带外逼近导致的数值发散
- **[2017]** 实常数变换矩阵精度随线路长度增加而下降，需根据精度要求选择解耦策略

### 关键技术贡献
- **[2010]** 留极点比值约束拟合方法成功解决宽频线路模型时域数值失稳
- **[2016]** 多层大地广义框架突破传统Carson积分单一土壤假设限制
- **[2021]** 闭式解析表达式替代无穷积分，埋地电缆参数计算效率显著提升

### 计算效率提升
- **[2017]** 折叠线等效与延迟利用结合，大规模系统仿真复杂度显著降低
- **[2021]** 两阶段混合架构实现通用线路模型在开源平台的零成本部署
- **[2026]** 有理Krylov降阶在保持宽频精度同时大幅减少状态变量数量

## 深度增强内容

### 1. 电缆模型分类体系

| 模型类型 | 适用频段 | 计算复杂度 | 典型应用 |
|---------|---------|-----------|---------|
| 恒定参数模型 | DC-60Hz | O(n) | 工频潮流、稳态分析 |
| 频率相关模型(FD) | 0.1Hz-10kHz | O(n²) | 开关暂态、机电振荡 |
| 通用线路模型(ULM) | DC-1MHz | O(n³) | 雷电冲击、行波保护 |
| 宽频降阶模型 | DC-100kHz | O(n log n) | VSC-HVDC宽频相互作用 |

### 2. 关键参数与典型值

**单芯电缆单位长度参数（典型值）**:
| 参数 | 典型范围 | 频变特性 |
|-----|---------|---------|
| R (Ω/km) | 0.02-0.5 | 集肤效应显著 |
| L (mH/km) | 0.2-2.0 | 大地返回影响 |
| C (μF/km) | 0.1-0.5 | 介质损耗 |
| G (μS/km) | 0.01-1.0 | 绝缘老化 |

**三芯铠装电缆特殊考虑**:
- 螺线管效应：铠装钢丝磁化导致的附加阻抗
- 护套回流：金属护套中的环流损耗
- 交叉互联：大长度电缆的接地方式优化

### 3. 模型选择指南

| 应用场景 | 推荐模型 | 关键考量 |
|---------|---------|---------|
| 工频负载流 | 恒定参数 | 精度足够，计算最快 |
| 开关过电压 | FD/ULM | 捕捉高频振荡 |
| 雷电冲击 | ULM | 行波传播精度 |
| VSC-HVDC | 宽频降阶 | 宽频相互作用 |
| 实时仿真 | 状态空间实现 | 固定步长稳定性 |
| 参数不确定 | 测量融合模型 | S参数修正 |

### 4. 前沿研究方向

**机器学习辅助建模**:
- 神经网络替代矢量拟合，加速频域到有理函数转换
- 数据驱动模型降阶，从仿真数据学习低阶等效

**多物理场耦合**:
- 热-电耦合模型，考虑载流量与温度的动态反馈
- 老化模型融合，绝缘退化对暂态响应的影响

**数字孪生应用**:
- 在线参数辨识，利用PMU数据实时校正模型
- 故障定位增强，利用行波反射特性精确定位

## 相关方法
- [[vector-fitting|矢量拟合]] - 频变参数有理函数拟合
- [[state-space-method|状态空间法]] - 频变模型状态空间实现
- [[nodal-analysis|节点分析]] - 电缆网络节点方程求解
- [[numerical-integration|数值积分]] - 频变模型离散化实现
- [[passivity-enforcement|无源性强制]] - 宽频模型稳定性保证

## 相关模型
- [[cable-model|电缆模型]] - 地下/海底电缆元件模型
- [[transmission-line-model|输电线路模型]] - 架空线路与电缆联合建模
- [[fdne-model|频变网络等值(FDNE)]] - 电缆网络宽频等值
- [[transformer-model|变压器模型]] - 电缆-变压器接口建模
- [[grounding-system-model|接地系统模型]] - 电缆护套与接地

## 相关主题
- [[frequency-dependent-modeling|频率相关建模]] - 宽频参数建模框架
- [[real-time-simulation|实时仿真]] - 电缆模型实时实现
- [[co-simulation|混合仿真]] - 电缆-设备联合仿真
- [[parallel-computing|并行计算]] - 大规模电缆网络并行求解
- [[harmonic-analysis|谐波分析]] - 电缆谐波阻抗分析
