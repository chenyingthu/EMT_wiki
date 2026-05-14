---
title: "Back-to-back HVDC"
type: method
tags: [back-to-back-hvdc, lcc-hvdc, vsc-hvdc, hvdc-interconnection, asynchronous-interconnection]
created: "2026-05-10"
updated: "2026-05-12"
---

# Back-to-back HVDC

## 1. 物理背景与工程需求

Back-to-back HVDC 是一种两端换流器位于同一换流站内、直流侧不承担长距离输电功能的 HVDC 结构。其核心工程角色是作为两个**异步交流系统**之间的可控有功功率接口：两端的交流频率、相位和短路容量可以完全独立，因此无需像交流联络线那样要求两端同步运行。典型的工程需求包括：

- **异频互联**：连接不同额定频率的交流系统（如 50 Hz/60 Hz 电网互联）；
- **异步解耦**：在同一同步电网中隔离故障传播路径，限制交流扰动在系统间的扩散；
- **功率可控交换**：通过换流器控制实现两个交流系统之间有功功率的调度，而非由交流联络线的自然潮流决定；
- **黑启动与孤岛供电**：在受端交流系统全黑或孤岛运行时，通过背靠背 HVDC 提供电压和频率支撑。

Back-to-back 结构可采用**电网换相换流器（LCC）** 或**电压源换流器（VSC/MMC）** 两种技术路线。LCC 型背靠背站主电路为两个六脉波或十二脉波晶闸管换流桥经直流电抗器背靠背连接，适用于大容量（数百 MW 至 GW 级）功率传输；VSC/MMC 型可实现有功/无功独立调节、无需交流侧无功补偿，适用于弱电网互联或多端直流接入。两类换流器在主电路拓扑、控制方式和故障特性上的差异较大，**本页不将任一路线的性能结论外推至另一路线**（Sultan et al., 1998; Mengjia & Xiao, 2015）。

## 2. 数学描述

### 2.1 有功传输基本关系

忽略换流器内部损耗时，背靠背 HVDC 的有功传输关系为：

$$
P_{\text{dc}} = V_{\text{dc}} I_{\text{dc}}, \quad P_{\text{ac1}} = P_{\text{ac2}} = P_{\text{dc}}
$$

其中 $P_{\text{dc}}$ 为直流传输有功，$V_{\text{dc}}$ 和 $I_{\text{dc}}$ 为直流侧电压和电流。两端换流站与交流系统交换的无功功率 $Q_1, Q_2$ 由各自的换流器控制独立调节。

### 2.2 LCC 型平均电压方程

对于 LCC 型背靠背站，整流侧直流平均电压近似为（Zhou, 2021）：

$$
V_{\text{dr}} = V_{\text{d0r}} \cos\alpha - \frac{3\omega L_{\text{cr}}}{\pi} I_{\text{d}}
$$

逆变侧为：

$$
V_{\text{di}} = V_{\text{d0i}} \cos\gamma - \frac{3\omega L_{\text{ci}}}{\pi} I_{\text{d}}
$$

其中 $\alpha$ 为触发角，$\gamma$ 为关断角，$L_{\text{c}}$ 为换相电抗，$V_{\text{d0}} = 3\sqrt{2}V_{\text{LL}}/\pi$ 为理想空载直流电压。稳态运行时，$V_{\text{dr}}$ 与 $V_{\text{di}}$ 之差恰好等于直流电抗器及直流母线电阻上的压降。

### 2.3 VSC 型 d-q 矢量控制模型

对于 VSC/MMC 型背靠背站，有功和无功在同步旋转 d-q 坐标系中解耦控制。与交流系统交换的有功和无功为：

$$
P = \frac{3}{2} (v_{\text{d}} i_{\text{d}} + v_{\text{q}} i_{\text{q}}), \quad
Q = \frac{3}{2} (v_{\text{q}} i_{\text{d}} - v_{\text{d}} i_{\text{q}})
$$

当 d 轴定向于交流母线电压矢量时 $v_{\text{q}} = 0$，则有 $P = 1.5 v_{\text{d}} i_{\text{d}}$，$Q = -1.5 v_{\text{d}} i_{\text{q}}$，实现有功和无功的独立调节（Mengjia & Xiao, 2015）。

### 2.4 交直流系统功率平衡

对于嵌入式（与交流联络线并联运行）的背靠背 VSC-HVDC，受端母线的总有功功率满足：

$$
P_{\text{Bus}} = P_{\text{dc}} + P_{\text{ac}}
$$

其中 $P_{\text{ac}}$ 为并联交流线路的传输功率，由两端电压幅值、线路电抗和相角差决定（Mengjia & Xiao, 2015）：

$$
P_{\text{ac}} = \frac{E_1 E_2}{x_{12}} \sin(\delta_1 - \delta_2)
$$

## 3. 计算模型与离散化

### 3.1 EMT 仿真中的伴随模型

在 EMT 程序中，背靠背 HVDC 的两端换流器需建立**伴随电路（companion circuit）模型**，离散化后接入节点导纳矩阵求解。对于 LCC 型，每个晶闸管桥臂用开关电阻模型结合过零检测和插值算法表示；对于 MMC 型，桥臂子模块电容通过梯形积分法离散为诺顿等效：

$$
i_{\text{arm}}(t) = G_{\text{eq}} v_{\text{arm}}(t) + I_{\text{hist}}
$$

### 3.2 混合仿真接口模型

当背靠背 HVDC 系统与大规模交流电网联合仿真时，可采用 TSP/EMTP 混合仿真架构（Sultan et al., 1998）：

- **外部交流系统**（TSP 侧）通过**时变诺顿频变等值（NFDE）** 映射至 EMT 区域：
  $$
  \mathbf{I}_{\text{eq}}(s) = \mathbf{Y}_{\text{eq}}(s) \mathbf{V}_{\text{bus}}(s) + \mathbf{I}_{\text{source}}(s)
  $$
  
- **EMT 详细区域**（含背靠背 HVDC）以 50 μs 步长推进，接口母线的三相瞬时波形通过最小二乘曲线拟合提取基波正序相量反馈给 TSP。

- **步长配合**：TSP 步长 8-10 ms，EMTP 步长 50 μs，时间步协调比可达 160:1。

对于 VSC-HVDC 系统，混合仿真接口需要额外处理故障后交流系统等效阻抗重构和相量提取窗口问题（van der Meer et al., 2015）。采用一阶保持（FOH）替代零阶保持（ZOH）更新戴维南源可使系统级误差降低约 41%。

## 4. 实现方法与算法细节

### 4.1 LCC 型背靠背站控制

LCC 型背靠背站的控制通常包含以下层级：

1. **整流侧**：定电流控制或定功率控制，通过调节触发角 $\alpha$ 维持直流电流或功率于参考值；
2. **逆变侧**：定关断角控制或定直流电压控制，通过调节 $\gamma$ 维持直流电压或换相裕度；
3. **无功/交流电压控制**：通过换流变压器分接头投切和交流滤波器/无功补偿设备维持交流母线电压。

在实时仿真中，Zhou（2021）在 Nelson River 三双极 LCC-HVDC 系统中采用 RTDS 标准库逻辑模块重构控制系统（取代 PSCAD/EMTDC 自定义模块），并将接口信号统一为标幺量。该平台含 Bipole I（1854 MW, ±463.5 kV）和 Bipole II（2000 MW, ±500 kV）的软件模型。

### 4.2 VSC/MMC 型背靠背站控制

VSC/MMC 型背靠背站的控制为双环 d-q 矢量结构（Mengjia & Xiao, 2015）：

1. **外环控制**：根据有功/直流电压和无功/交流电压参考值生成 d、q 轴电流指令 $i_{\text{d}}^*$ 和 $i_{\text{q}}^*$；
2. **内环电流控制**：通过 PI 调节器及前馈解耦项生成调制电压信号，经 PWM 或最近电平调制（NLM）产生开关脉冲；
3. **附加控制**：可叠加频率阻尼、功率振荡抑制等附加功能。

Xu et al.（2014）指出，当使用 MMC 平均值模型（AVM）进行 VSC-HVDC 系统级仿真时，AVM 仅在子模块电容 $C_{\text{sm}} \ge 20$ mF（电压纹波 <2%）时有效。改进型 AVM 引入受控开关和二极管路径后，可在正常运行时退化为传统 AVM，在闭锁或直流故障时激活续流和放电支路。

### 4.3 嵌入式背靠背 HVDC 的频率控制

当背靠背 VSC-HVDC 与交流联络线并联运行时（两端处于同一同步网络），可利用两端频率差实现对交流功率振荡的主动阻尼（Mengjia & Xiao, 2015）：

1. 实时监测两端频率差 $\Delta \omega = \omega_1 - \omega_2$ 和相角差；
2. 对交流联络线功率方程做小信号线性化，提取振荡分量 $P_{\text{oscillation}}$；
3. 将振荡分量叠加至直流有功参考：$P_{\text{dc}}^{\text{NEW}*} = P_{\text{dc}}^* + P_{\text{oscillation}}$；
4. 常规 d-q 外环按新参考调节 VSC 有功输出。

## 5. 适用边界与失效模式

### 适用条件

- 需要在两个异步或弱耦合交流系统之间实现可控功率交换；
- 两端交流系统的频率、相位和短路容量可以独立；
- 直流侧不承担长距离输电功能，直流母线通常仅包含电抗器和限流设备；
- LCC 型适用于大容量（数百 MW 级以上）功率传输，要求两端交流系统具有足够短路容量以保证晶闸管正常换相；
- VSC/MMC 型适用于弱电网互联、独立调节无功功率或需要黑启动能力的场景。

### 失效模式

- **LCC 换相失败**：当逆变侧交流电压跌落或波形畸变时，晶闸管换相裕度不足 $\gamma < \gamma_{\text{min}}$ 引发换相失败，导致直流电压骤降、电流冲击（据方法推断）；
- **直流母线故障**：背靠背站直流侧长度短，故障后放电速度快，需高速 DCCB 或换流器闭锁配合；
- **功率容量饱和**：当附加的阻尼控制要求 $P_{\text{dc}}^{\text{NEW}*}$ 超出换流器容量时，补偿量被限幅截断，超出部分仍由交流联络线承担（Mengjia & Xiao, 2015）；
- **混合仿真接口失真**：当 EMT 区域和 TSP 区域之间的交互步长、等值阶数或相量提取窗口设置不当时，混合仿真结果中的控制响应可能出现误差（Sultan et al., 1998; van der Meer et al., 2015）。

### 关键约束

| 约束维度 | LCC 型 | VSC/MMC 型 |
|---------|--------|-----------|
| 有功容量 | 数百 MW 至 GW 级（据工程数据） | 数十 MW 至 1 GW 级（据工程数据） |
| 无功能力 | 需外部无功补偿（滤波器+电容器） | 可独立调节 Q（±0.9 p.u. 典型值） |
| 换相要求 | 需强交流系统（SCR ≥ 2.5，据方法推断） | 可接入弱电网（SCR ≥ 1.0） |
| 直流电压纹波 | 12 脉波时特征谐波 12k±1（据方法推断） | MMC 纹波取决于子模块电容和 NLM 电平数 |

## 6. 应用案例

### 案例 1：LCC 背靠背测试系统（Sultan et al., 1998）

2 端背靠背 LCC HVDC 系统用于验证 TSP/EMTP 混合仿真方法：
- 每端含 8 个交流节点的等效交流系统；
- EMTP 步长 50 μs，TSP 步长 8-10 ms，交互步长比 160:1；
- 通过 NFDE 将外部交流系统映射至 EMT 详细区域。

### 案例 2：嵌入式 VSC-HVDC 暂态稳定增强（Mengjia & Xiao, 2015）

在 IEEE 4 机 6 节点系统（230 kV, 60 Hz）中嵌入与交流联络线并行的 VSC-HVDC：
- 频率阻尼控制使平均 CCT 提高 22.93%；
- 故障后受端功率振荡在约 6 秒内衰减至稳态水平；
- 直流链路容量限制导致补偿功率在前 3 秒呈方波截断。

### 案例 3：Nelson River 多馈入 LCC-HVDC 实时 HIL（Zhou, 2021）

Manitoba Hydro Nelson River 三双极系统（Bipole I/II/III）：
- Bipole I: 1854 MW / ±463.5 kV；Bipole II: 2000 MW / ±500 kV；
- RTDS 软件模型 + Bipole III 硬件保护副本的混合实时 HIL 平台；
- Dorsey 站含 14 个等效换流阀组和 9 台同步调相机。

## 7. 量化性能边界

**Sultan 1998 TSP/EMTP混合仿真（背靠背LCC HVDC测试系统）**:
- 构建2端背靠背LCC HVDC测试系统，每端含8个交流节点的等效交流系统
- EMTP步长50μs，TSP步长8-10ms，交互步长比160:1
- 通过NFDE将外部交流系统映射至EMT详细区域
- 数据缺口：NFDE等值的阶数和频率范围对混合仿真精度的影响未系统评估

**Mengjia & Xiao 2015 嵌入式VSC-HVDC暂态稳定增强**:
- 在IEEE 4机6节点系统（230kV, 60Hz）中嵌入与交流联络线并行的VSC-HVDC
- 频率阻尼控制使平均CCT提高22.93%
- 故障后受端功率振荡在约6秒内衰减至稳态水平
- 直流链路容量限制导致补偿功率在前3秒呈方波截断
- 数据缺口：仅在单机-无穷大和4机系统中验证，多机大系统下的有效性未报告

**van der Meer 2015 VSC-HVDC混合TS-EMT仿真接口**:
- 采用一阶保持（FOH）替代零阶保持（ZOH）更新戴维南源
- 系统级误差降低约41%
- 数据缺口：FOH接口在不同故障类型（单相/三相/不对称）下的误差改善程度未分别报告

**Xu 2014 MMC AVM在VSC-HVDC系统级仿真中的适用性**:
- MMC平均值模型在子模块电容Csm≥20mF（电压纹波<2%）时有效
- 改进型AVM引入受控开关和二极管路径后，可在正常运行时退化为传统AVM
- 在闭锁或直流故障时激活续流和放电支路
- 数据缺口：AVM精度边界仅在特定MMC参数下验证，不同电平数（N>200）下的适用性未讨论

**数据缺口声明**：背靠背HVDC的量化性能数据分散在混合仿真、控制策略和实时仿真三个不同方向，缺乏在统一测试系统下的横向对比。LCC与VSC/MMC两种技术路线的性能数字不可相互外推。混合仿真接口的精度高度依赖交互步长比、等值阶数和故障场景，不能以单一误差百分数概括。

## 8. 延伸阅读

### 相关方法
- [[hvdc-control]]：站级控制方法集合（含 LCC 触发角控制、VSC d-q 矢量控制）
- [[co-simulation]]：TSP/EMTP 混合仿真框架
- [[average-value-model]]：LCC 和 MMC 的平均值模型
- [[dccb]]：直流断路器与保护配合

### 相关模型
- [[lcc-model]]：电网换相换流器模型
- [[vsc-model]]：电压源换流器模型
- [[mmc-model]]：模块化多电平换流器模型

### 相关主题
- [[vsc-hvdc]]：VSC-HVDC 系统
- [[multi-terminal-dc]]：多端直流网络
- [[real-time-simulation]]：实时仿真
- [[hil-simulation]]：硬件在环仿真

### 主要来源
- [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems|Sultan et al. (1998)]] — 背靠背 LCC HVDC 测试系统与 TSP/EMTP 混合仿真
- [[dynamic-performance-of-embedded-hvdc-with-13&14|Mengjia & Xiao (2015)]] — 嵌入式 VSC-HVDC 频率控制
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Zhou (2021)]] — Nelson River 多馈入 LCC-HVDC 实时建模
- [[advanced-hybrid-transient-stability-and-emt-simulation-for-vsc-hvdc-systems|van der Meer et al. (2015)]] — VSC-HVDC 混合 TS-EMT 仿真接口
- [[average-value-models-for-modular-multilevel-converters-operating-in-a-vsc-hvdc-grid|Xu et al. (2014)]] — MMC AVM 在 VSC-HVDC 中的适用性
- [[mmc-21-level-hvdc]] — MMC-HVDC 测试系统（含背靠背运行结构）

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies|A Wideband Equivalent Model of Type-3 Wind Power Plants for ]] | 2016 |
| [[current-source-modular-multilevel-converter-modeling-and-control|Current Source Modular Multilevel Converter Modeling and Con]] | 2016 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
