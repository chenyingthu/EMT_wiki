---
title: "Detailed Switch Model"
type: model
tags: [switch-model, power-electronics, detailed-modeling, transient-analysis, igbt, mosfet, thyristor, diode, snubber-circuit]
created: "2026-05-02"
updated: "2026-05-03"
---

# Detailed Switch Model


```mermaid
graph TD
    subgraph Ncmp[Detailed Switch Model]
        N0[理想开关: 开/关两态电阻或电导]
        N1[电阻型开关: 状态相关 $R_{on}/R_{off}$…]
        N2[寄生详细模型: 加入电容、电感、反并联二极管和缓冲支路]
        N3[半导体行为模型: 门极电荷、尾电流、反向恢复和温度依赖]
        N4[实时等效模型: 预计算、分段线性或 FPGA/实时友好实现]
    end
```


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

## 适用边界与失败模式

- 详细开关模型不自动“更准确”；若缺少器件数据、布局寄生或驱动模型，复杂模型可能只是引入未校准自由度。
- 开关事件会改变导纳矩阵或等效源，可能触发数值振荡、代数环或刚性问题；相关处理见 [[numerical-integration]]、[[interpolation-method]] 和 [[stiff-system-handling]]。
- 固定步长 EMT 可能错过实际开关时刻，插值或事件定位会影响尖峰和损耗计算。
- 寄生电感、电容和缓冲网络对过电压敏感，不能用默认参数替代布局或数据手册。
- 大规模 MMC、VSC 或逆变器研究中，详细开关模型的计算量可能不可接受，需要与 [[average-value-model]] 或等效子模块模型比较。

## 验证需求

详细开关模型的验证应至少说明：

- 器件类型、额定条件和参数来源，例如数据手册、双脉冲试验或论文模型。
- 参考波形：开通/关断电压电流、反向恢复、电压尖峰、门极波形或损耗。
- EMT 设置：步长、事件定位、积分方法、缓冲支路和网络寄生。
- 层级对比：与理想开关、平均值模型或更详细器件模型的差异。
- 实时模型需报告资源占用、延迟和可接受的降阶误差，而不是笼统宣称实时可用。

## 代表性来源

- [[modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s]] 代表在 EMTP 中用 TACS 受控开关表示 VSC 详细开关层级，并与较简化模型比较；页面证据提醒部分数值需回查 PDF。
- [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode]] 可作为宽禁带器件实时 HIL 建模的来源入口；具体加速和误差必须绑定其测试系统。
- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] 与 [[average-value-model]] 说明在 VSC-HVDC 中用降阶或平均化模型替代详细开关的动机。

## 与相关页面的关系

- [[ideal-switch-model]] 是最简开关等效，用于拓扑和控制逻辑。
- [[diode-model]]、[[igbt-model]] 和 [[thyristor-control]] 分别展开具体器件或触发控制。
- [[power-electronics]] 是电力电子系统主题入口，[[vsc-model]]、[[mmc-model]] 和 [[inverter-model]] 是使用开关模型的设备页。
- [[switching-transient]] 关注开关事件引发的系统暂态，详细开关模型是其可能的局部对象。

## 来源论文

参见 [[index]] 获取更多详细开关模型相关文献。
