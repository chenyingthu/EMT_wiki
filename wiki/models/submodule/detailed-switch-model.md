---
title: "Detailed Switch Model"
type: model
tags: [switch-model, power-electronics, detailed-modeling, transient-analysis, igbt, mosfet, thyristor, diode, snubber-circuit]
created: "2026-05-02"
updated: "2026-05-12"
updated: "2026-05-11"
---

# Detailed Switch Model


## 定义与边界

详细开关模型是 EMT 中对电力电子开关器件导通、关断、反向恢复、寄生电容电感、门极驱动和损耗过程的显式等效。它的物理对象是 IGBT、MOSFET、二极管、晶闸管及其封装、驱动和缓冲网络；EMT 等效对象则是会随门极信号、器件状态和网络电压电流改变的受控电导、受控源、寄生支路和状态机。

本页讨论详细开关模型的层级与接口，不把器件数据手册中的典型参数写成通用数值。若只关心开关周期平均行为，应使用 [[average-value-model]] 或 [[switching-function-method]]；若只关心拓扑通断逻辑，可用 [[ideal-switch-model]]。

## EMT 建模对象

详细开关模型通常包含：

- 主电气端口：集电极/发射极、漏极/源极、阳极/阴极等功率端口。
- 控制端口：门极电压、电流、触发脉冲、驱动电阻和保护逻辑。
- 寄生网络：结电容、封装电感、母排电感、缓冲电阻电容和反并联二极管。
- 状态转换：导通、关断、反向恢复、尾电流、锁定或保护关断状态。
- 热或损耗接口：瞬时功率、开关能量、结温输入或热网络反馈。

## 模型结构与接口变量

详细开关可抽象为混合系统：

$$
\mathbf{x}_{s,n+1} = f_s(\mathbf{x}_{s,n}, v_s, i_s, u_g, \mathbf{p}_s),
\qquad
i_s = h_s(v_s, \mathbf{x}_{s,n}, u_g, \mathbf{p}_s).
$$

其中 $\mathbf{x}_s$ 包括门极电荷、结电容电压、反向恢复电荷、热状态或开关状态；$v_s$ 和 $i_s$ 是功率端口电压电流；$u_g$ 是驱动或触发信号；$\mathbf{p}_s$ 是器件和封装参数。

在节点分析中，开关常被线性化为当前步等效电导和历史源：

$$
i_s(t_n) \approx G_{eq,n} v_s(t_n) + I_{hist,n}.
$$

事件发生时，$G_{eq}$、历史源或拓扑状态改变。若每次事件都重构矩阵，计算代价和数值噪声会增加；若采用 [[fixed-admittance]]，则需要用补偿源或状态变量保持物理一致性。

## 建模层级

| 层级 | 表示方式 | 适用用途 | 主要边界 |
|------|----------|----------|----------|
| 理想开关 | 开/关两态电阻或电导 | 拓扑逻辑、控制初步验证 | 无法计算损耗、尖峰和恢复过程 |
| 电阻型开关 | 状态相关 $R_{on}/R_{off}$ 和过渡函数 | 开关事件和粗略导通损耗 | 参数依赖器件，难以表示高频寄生 |
| 寄生详细模型 | 加入电容、电感、反并联二极管和缓冲支路 | 开关暂态、过电压和 EMI 倾向分析 | 需要小步长和器件参数 |
| 半导体行为模型 | 门极电荷、尾电流、反向恢复和温度依赖 | 器件级损耗和保护策略研究 | 参数识别难，数值刚性较强 |
| 实时等效模型 | 预计算、分段线性或 FPGA/实时友好实现 | HIL 和大规模换流器实时仿真 | 需说明降阶误差和硬件限制 |

## 量化性能边界

详细开关模型在 EMT 仿真中已有可核验的量化结果，但以下数据均绑定具体器件类型、算法和测试条件，不能外推为通用能力：

- **Yu (2014)** 在 PSCAD/EMTDC 中提出了 MMC 快速数值仿真模型（平均比较电压均衡 + 受控电压源桥臂等效 + 线性化 IGBT/二极管开关模型）。在 201 电平（每臂 216 个 SM）MMC-HVDC 系统中，快速模型与详细开关模型波形几乎相同，仿真速度约为详细开关模型的 **5 000 倍**（5 s 暂态从约一周缩短至分钟级）。采用线性化开关模型（阈值电压 + 导通电阻）近似 IGBT/二极管伏安特性，保留每个 SM 电容电压动态。混合仿真模型可将特定 SM 替换为详细开关电路，兼顾全局效率与局部细节。原文未给出逐点误差表或系统误差统计 (Yu 2014)。

- **Gao (2023)** 在半桥子模块(HBSM)中提出了混合积分方法：开关事件期间的刚性微分方程用指数积分器局部求解，非事件期间用梯形法大步长推进。与固定 1 μs 步长详细开关模型相比，在保持相同精度（波形几乎重合）的前提下获得 **5-15 倍**加速。加速比随子模块数量增加和开关频率降低而提高，验证限于 HBSM 和特定 MMC 配置 (Gao 2023)。

- **Zhang (2023)** 在 Xilinx Ultrascale+ FPGA 上实现了宽禁带器件（GaN HEMT、SiC IGBT）的物理特征神经网络(PFNN)实时 HIL 模型。PFNN 通过预测波形特征点（拐点、峰值、谷值）实现变步长（低至 **1 ns**）建模，再经分段线性插值重构高分辨率波形。系统级采用传输线法(TLM)分区解耦。原文报告波形与 SaberRD 和 PSCAD/EMTDC 离线仿真一致，但未给出可核验的详细误差百分比、资源占用表或加速倍数 (Zhang 2023)。

- **Yu (2013)** 系统比较了 MMC 的六种模型保真度（详细开关、Thevenin 等效、简化 Thevenin、连续、解析、稳态），结论是 Thevenin 等效模型在精度上与详细开关模型几乎一致，而平均值模型在特定工况下误差可达 **>300%**。该比较为模型层级选择提供了定量参考，但结论限于 MMC 拓扑和文中测试工况 (Yu 2013)。

- **Stepanov (2020)** 提出了桥臂等效模型(AEM)的自适应切换方法，在 EMT 仿真中根据子模块电压偏差动态选择 DEM 或 AEM 模式。在 Delta 连接全桥 MMC-STATCOM 系统中，自适应切换模型与详细开关模型的误差 < **0.5%**，计算耗时较 DEM 显著降低。加速比随工况变化，需参考原文具体数值 (Stepanov 2020)。

这些量化数据不构成对所涉建模方法的全面性能评价，只说明在特定测试条件下可获得的能力边界。

## 适用边界与失败模式

- 详细开关模型不自动"更准确"；若缺少器件数据、布局寄生或驱动模型，复杂模型可能只是引入未校准自由度。
- 开关事件会改变导纳矩阵或等效源，可能触发数值振荡、代数环或刚性问题；相关处理见 [[numerical-integration]]、[[interpolation-method]] 和 [[stiff-system-handling]]。
- 固定步长 EMT 可能错过实际开关时刻，插值或事件定位会影响尖峰和损耗计算。
- 寄生电感、电容和缓冲网络对过电压敏感，不能用默认参数替代布局或数据手册。
- 大规模 MMC、VSC 或逆变器研究中，详细开关模型的计算量可能不可接受，需要与 [[average-value-model]] 或等效子模块模型比较。
- 线性化开关模型的精度受阈值电压和导通电阻近似影响，在宽工作点范围内需重新校核 (Yu 2014)。
- NN 加速的器件模型（如 PFNN）的泛化能力受训练数据覆盖范围限制，未经训练的故障或极端工况可能产生不可预测误差 (Zhang 2023)。
- 自适应等效模型在频繁切换边界附近可能引入额外数值振荡，需验证阈值设置的鲁棒性 (Stepanov 2020)。

## 验证需求

详细开关模型的验证应至少说明：

- 器件类型、额定条件和参数来源，例如数据手册、双脉冲试验或论文模型。
- 参考波形：开通/关断电压电流、反向恢复、电压尖峰、门极波形或损耗。
- EMT 设置：步长、事件定位、积分方法、缓冲支路和网络寄生。
- 层级对比：与理想开关、平均值模型或更详细器件模型的差异，并参考 Yu (2013) 的六模型比较框架。
- 实时模型需报告资源占用、延迟和可接受的降阶误差，而不是笼统宣称实时可用。

## 开放问题

- MMC 快速数值模型（Yu 2014）的 5 000 倍加速基于平均比较和线性化开关近似，其误差边界在不同电平数和故障场景下的量化特征尚未系统报告。
- 混合积分方法（Gao 2023）在更多器件类型（如 SiC、GaN）和复杂拓扑下的加速比和适用条件需要更多验证。
- 机器学习加速器件模型的泛化能力和训练数据需求尚缺乏标准化评估方法（Zhang 2023）。
- 详细开关模型与降阶模型之间的误差在换流器型电源高渗透系统中的累积效应尚不明确。
- 当前 EMT 框架中缺乏统一的可变保真度开关模型选择准则，用户依赖经验从五层级中做出选择。

## 代表性来源

- [[fast-voltage-balancing-control-and-fast|Yu (2014)]] 支撑 MMC 快速数值模型（线性化开关 + 平均比较）：5 000 倍加速、201 电平 MMC-HVDC。原文未给出逐点误差统计。
- [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Zhang (2023)]] 支撑 WBG 器件 PFNN 实时 HIL：变步长低至 1 ns、TLM 分区解耦。原文未给出可核验的误差百分比或加速倍数。
- [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s|Kosterev (2004)]] 代表在 EMTP 中用 TACS 受控开关表示 VSC 详细开关层级：18 脉波 GTO、12.5 kV/10 MVA。
- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] 说明用降阶或平均化模型替代详细开关的动机。
- [[detailed-equivalent-model]] 和 [[average-value-model]] 是详细开关模型在 MMC 和 VSC 研究中的主要替代方案。

## 与相关页面的关系

- [[ideal-switch-model]] 是最简开关等效，用于拓扑和控制逻辑。
- [[diode-model]]、[[igbt-model]] 和 [[thyristor-control]] 分别展开具体器件或触发控制。
- [[power-electronics]] 是电力电子系统主题入口，[[vsc-model]]、[[mmc-model]] 和 [[inverter-model]] 是使用开关模型的设备页。
- [[switching-transient]] 关注开关事件引发的系统暂态，详细开关模型是其可能的局部对象。
- [[detailed-equivalent-model]] 给出 DEM 在 MMC 中的具体实现和精度边界。

## 来源论文

参见 [[index]] 获取更多详细开关模型相关文献。
---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[fast-voltage-balancing-control-and-fast-19、20、21|Fast Voltage-Balancing Control and Fast]] | 2014 |
| [[fast-voltage-balancing-control-and-fast|Fast Voltage-Balancing Control and Fast Numerical Simulation]] | 2014 |
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system|Parallel-in-Time Simulation Algorithm for Power Electronics:]] | 2019 |
| [[numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal|Numerically Efficient Average-Value Model for Voltage-Source]] | 2024 |
