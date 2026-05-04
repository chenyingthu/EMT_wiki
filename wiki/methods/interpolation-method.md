---
title: "插值方法 (Interpolation Method)"
type: method
tags: [interpolation, numerical-method, time-step, multi-rate, accuracy]
created: "2026-04-14"
---

# 插值方法 (Interpolation Method)

## 定义与边界

插值方法是在已知离散时刻数据之间构造中间时刻变量的数值技术。EMT 中的插值主要服务于两类问题：开关或过零事件落在固定步长内部时的事件定位，以及多速率、联合仿真或实时接口中的时间同步。

本页讨论插值作为 EMT 求解过程的一部分，而不是一般数据平滑。外推是用历史点预测未来点，稳定边界通常更窄，应与插值分开处理。事件后的数值阻尼见 [[stiff-system-handling]]；多速率接口见 [[multirate-method]]。

## EMT 中的作用

固定步长 EMT 求解器只在网格点求解网络方程，但开关触发、二极管关断、电流过零和接口采样通常发生在网格点之间。插值用于：

- 估计开关时刻 $t_s$，避免把事件强行提前或推迟到网格点。
- 为 [[multirate-method]] 中快慢子系统提供同步边界条件。
- 为线路延时、控制采样和实时硬件通信补偿构造中间值。
- 在事件定位后重算历史源，使 [[numerical-integration]] 与新拓扑一致。

## 核心机制

线性插值的基本形式为

$$
x(t_s)=x(t_n)+\alpha\left(x(t_{n+1})-x(t_n)\right),
$$

其中

$$
\alpha=\frac{t_s-t_n}{h},\quad 0\leq \alpha\leq 1.
$$

在开关事件中，$t_s$ 常由电压、电流或控制信号的阈值交叉给出。若插值结果被用作新的事件状态，后续还需要根据开关后的拓扑重建历史源或执行阻尼步骤。否则，即使事件时刻定位较好，电感电流、电容电压或伴随电路历史项也可能与新拓扑不一致。

在多速率接口中，慢变量 $x_s(t_m)$ 和 $x_s(t_{m+1})$ 可被插值到快步长时刻；快变量反馈到慢系统时常需要平均、滤波或采样，而不是简单取某个瞬时值。

## 分类与变体

| 方法 | 用途 | 边界 |
|------|------|------|
| 零阶保持 | 实时或采样保持接口 | 引入延迟，可能放大接口误差 |
| 线性插值 | 过零定位、慢到快同步 | 仅利用端点；不保证导数连续 |
| 多项式或 Hermite 插值 | 需要导数或步内点的高阶重构 | 对噪声、非连续点和外推更敏感 |
| 密集输出插值 | 利用积分器内部阶段或矩阵指数中间点 | 需要积分方法本身提供可信步内状态 |
| 外推预测 | 通信延迟补偿或预测校正 | 在开关、故障和强耦合接口处需严格稳定性检查 |

## 适用边界与失败模式

- 插值不能修复错误的物理模型或过大的仿真步长；它只在已有离散数据可信时构造中间值。
- 对不连续事件，跨越事件前后直接做高阶插值可能产生伪振荡。
- 外推不应被当作插值的无风险替代；在强耦合接口中可能引入能量或相位误差。
- 开关事件定位后若不重算历史源，可能出现电流截断、虚拟损耗或非特征谐波。
- 插值阶数越高不必然越好；导数信息、步内阶段值和事件光滑性必须与算法假设匹配。

## 代表性来源

| 来源 | 支撑内容 | 证据边界 |
|------|----------|----------|
| [[interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo]] | 矩阵指数和密集输出可为开关事件插值提供步内状态，强调积分器与插值公式匹配 | 当前证据不支持固定误差百分比、速度提升或实时能力断言 |
| [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da]] | 线性插值和 CDA 可等效为扩展切换状态，并在严格无源条件下得到稳定性充分条件 | 充分条件不等同于任意开关系统都稳定，也不评价效率 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations]] | 多速率接口的上采样、下采样、插值和外推会影响整体离散稳定性 | 理论边界主要是 LTI、整数步长比和特定接口规则 |
| [[a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems]] | 多速率 MMC 与大电网仿真需要接口同步和边界变量处理 | 结论应限定在原文分区和测试系统 |
| [[a-parallel-multi-rate-electromagnetic-transient-simulation-algorithm-based-on-ne]] | 并行多速率 EMT 把插值作为子网络接口协调的一部分 | 不等同于所有并行分区都稳定 |

## 与相关页面的关系

- [[multirate-method]] 使用插值处理快慢步长之间的接口。
- [[numerical-integration]] 决定是否有可靠步内状态可供插值。
- [[stiff-system-handling]] 处理插值定位后可能仍存在的突变和数值振荡。
- [[fixed-admittance]] 常与插值配合，以减少开关矩阵重构同时控制状态误差。
- [[switch-modeling]] 说明开关模型本身如何定义触发、导通和关断状态。
- [[voltage-interpolation]] 是电压变量插值的更窄页面。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[耦合长线电磁暂态分析的扩展bergeron模型|耦合长线电磁暂态分析的扩展Bergeron模型]] | 1996 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[电力系统机电暂态和电磁暂态混合仿真程序设计和实现|电力系统机电暂态和电磁暂态混合仿真程序设计和实现]] | 2006 |
| [[第29-卷-第34-期-中-国-电-机-工-程-学-报-vol29-no34-dec-5-2009|考虑任意重事件发生的多步变步长电磁暂态仿真算法]] | 2009 |
| [[模块化多电平换流器戴维南等效整体建模方法|模块化多电平换流器戴维南等效整体建模方法]] | 2015 |
| [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da|Stability Evaluation of Interpolation, Extrapolation, and Nu]] | 2020 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn|Study of a numerical integration method using the compact sc]] | 2023 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[电力系统数字混合仿真技术综述及展望|电力系统数字混合仿真技术综述及展望]] | 2023 |
| [[新能源电力系统细粒度并行与多速率电磁暂态仿真|新能源电力系统细粒度并行与多速率电磁暂态仿真]] | 2024 |
| [[reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in|Reduced-order and simultaneous solution of power and control]] | 2025 |
| [[stability-assessment-of-multi-rate-electromagnetic-transient-simulations|Stability Assessment of Multi-Rate Electromagnetic Transient]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
