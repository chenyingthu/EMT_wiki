---
title: "电力电子变压器方法入口 (PET)"
type: method
tags: [pet, power-electronic-transformer, sst, chb-dab, multirate, switching-function]
created: "2026-05-04"
updated: "2026-05-11"
---

# 电力电子变压器方法入口 (PET)

## 定义与边界

PET（Power Electronic Transformer）指通过多级电力电子变换和高频隔离链实现电压变换、功率调节和多端口能量路由的设备与建模方法入口，常与固态变压器（SST）、能源路由器、柔性变电场景相关。在EMT仿真语境中，PET建模面临的核心矛盾是：多级变换器（AC-DC、DC-DC、DC-AC）包含大量开关器件和高频隔离变压器，若全系统采用统一小步长详细模型，计算代价随模块数超线性增长。当前EMT方法学围绕三个方向解决此矛盾：**端口等效消元**（将内部开关网络压缩为多端口等效电路）、**多速率分区**（按固有频率差异分配不同步长）、**开关函数解耦**（用受控源替代显式开关网络以保持恒定导纳矩阵）。

本页定位为PET系统级EMT建模的方法入口，收集已核验的建模策略和量化性能边界，不写无来源的效率、容量或拓扑优势结论。

## EMT中的作用

在EMT仿真中，PET建模方法主要服务于三类场景：

1. **系统级加速仿真**：通过节点消去（Gao 2022）、恒定G矩阵（Li 2025, Li 2026）或多速率分区（Wang 2025）降低计算规模，使含数十至上百子模块的PET能在合理时间内完成EMT仿真。

2. **实时仿真（HIL）**：开关函数等效模型（Li 2026）在OPAL-RT上实现60子模块SST实时仿真，171倍加速比使微秒级实时步长可行；恒定导纳特性消除了实时环境中反复LU分解的开销瓶颈。

3. **控制原型验证**：SFB-DEM保留子模块级动态（Li 2025），可准确复现电容电压平衡、DAB功率传输等控制响应，作为详细模型与平均值模型之间的精度-速度折中方案。

## 常见分支

### 1. 端口等效消元型（Gao 2022 为代表）

针对DAB高频链路（HFL），建立完整节点导纳方程后利用Kron消去递归消除内部节点。关键机制是利用IGBT非阻塞互补导通特性（G_ON+G_OFF=G_x为常数），将内部节点逆矩阵C⁻¹预计算为常数矩阵Q，使单步矩阵求逆量降为0。短路导纳参数（y11, y12, y22）作为中间统一量，可根据ISOP/ISOS/IPOP/IPOS配置转换为对应端口参数直接代数叠加。

- **验证**：PSCAD/EMTDC，MMC型SST + DAB HFL，10-100倍加速，硬件实验确认
- **局限**：仅覆盖DAB型HFL，MAB/SAB和故障穿越工况未验证

### 2. 多速率分区型（Wang 2025 为代表）

利用PET多级变换电路的固有频率差异，将系统划分为慢子系统（CHB整流级，实际开关频率~500Hz）和快子系统（DAB隔离级，开关频率kHz级）。在互联节点处采用多端口诺顿等效与电流源等效相结合的数据传输方法，并通过交错等效交互算法消除接口延迟。DAB部分采用MNA将变压器两侧电流作为状态变量，接受高精度触发信号以扩大步长而不丢失开关瞬态。

- **步长比例**：CHB步长50-100μs，DAB步长1-10μs，比例约10:1至20:1
- **验证**：CHB-DAB型PET，ISOP结构，与单速率EMT对比验证
- **局限**：具体加速倍数和误差百分比未在可核验摘要范围内报告

### 3. 开关函数解耦型（Li 2025, Li 2026 为代表）

通过开关函数统一描述变换器行为，将功率电路简化为受控源与等效阻抗的组合。Li 2025用前向欧拉离散电容（G_eq=C/h）实现恒定G矩阵，通过直流链路解耦将三阶段（AC-DC、DAB DC-DC、DC-AC）分解为独立子系统，使G矩阵呈分块对角形式。Li 2026用显式Gear法离散电容实现两级解耦，隐式Gear法离散L/R网络维持高阶精度与L稳定性。两者均集成步内开关插值以支持大步长（20-50μs）仿真。

- **Li 2025 SFB-DEM**：节点从6N+1降至2N+3（N为子模块数）；SFB-AVM降至3-5节点；20-50μs步长偏差<0.5%；THD差异<0.3%
- **Li 2026 ImEx-G3O**（60 SM SST）：171倍加速（vs DM）、7.5倍（vs VG-DEM）；稳态误差<0.5%；节点求解维度降低60%
- **局限**：Li 2025未报告具体加速倍数；两者均未验证保护逻辑、磁件非线性或不同实时硬件平台

## 形式化表达

### 通用开关函数等效

$$$v_{eq} = S \cdot v_C, \quad i_{eq} = S \cdot i_{out}$$$

其中开关函数 S ∈ {-1, 0, 1} 统一描述全桥、DAB和三电平变换器在投入、旁路和闭锁模式下的行为（Li 2025）。

### Kron端口消去（Gao 2022）

$$$Y_{EX} = A - B \cdot C^{-1} \cdot B^T, \quad j_S = B \cdot C^{-1} \cdot j_{IN} - j_{EX}$$$

内部节点消去后的多端口诺顿等效方程：

$$$\begin{bmatrix} i_{\text{IN}} \\ i_{\text{OUT}} \end{bmatrix} = \begin{bmatrix} y_{11} & y_{12} \\ y_{21} & y_{22} \end{bmatrix} \begin{bmatrix} v_{\text{IN}} \\ v_{\text{OUT}} \end{bmatrix} + \begin{bmatrix} j_{S1} \\ j_{S2} \end{bmatrix}$$

### ImEx-Gear解耦策略（Li 2026）

显式Gear 2阶更新MVDC电容电压实现Stage I与Stage II解耦：

$$$v_{C,j}^i(t_{k+1}) = \frac{4}{3}v_{C,j}^i(t_k) - \frac{1}{3}v_{C,j}^i(t_{k-1}) + \frac{2\Delta t}{3C_1}[2i_{C,j}^i(t_k) - i_{C,j}^i(t_{k-1})]$$

### 分块对角导纳矩阵（Li 2025）

$$$G_{system} = \begin{bmatrix} G_{StageI} & 0 & 0 \\ 0 & G_{StageII} & 0 \\ 0 & 0 & G_{StageIII} \end{bmatrix}$$

直流链路解耦后，三阶段独立求解，矩阵规模从O((6N+1)²)降至O((2N+3)²) + O(N²) + O(25)。

## 与相关页面的关系

- [[dual-active-bridge]]：DAB是PET最常见的中间级隔离DC-DC模块，Gao 2022的端口消去法和Li 2025的开关函数法均以DAB为核心建模对象。
- [[multirate-method]]：Wang 2025是将多速率方法应用于PET的典型案例，利用CHB与DAB的频率差异实现分区求解。
- [[fixed-admittance]]：Li 2025通过前向欧拉离散电容（G_eq=C/h）和Li 2026通过显式Gear解耦实现恒定G矩阵，是恒导纳法的直接应用。
- [[interpolation-method]]：Li 2025和Li 2026均集成步内开关插值，使大步长（20-50μs）仿真保持<0.5%偏差。
- [[average-value-model]]：Li 2025的SFB-AVM是开关函数法在平均值建模方向的延伸，节点数降至3-5个。
- [[real-time-simulation]]：Li 2026在OPAL-RT上验证60 SM SST实时仿真，171倍加速是PET实时化的量化参考。
- [[n-port-network]]：PET的多端口等效模型（Gao 2022的短路导纳参数、Li 2025的受控源等效）是多端口网络理论在电力电子中的典型应用。

## 代表性来源

| 来源 | 年份 | 核心贡献 | 加速比 | 精度 |
|------|------|----------|--------|------|
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Gao 2022]] | 2022 | Kron消去+短路导纳参数转换，DAB HFL端口等效 | 10-100x | 波形一致（未报告误差%） |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Wang 2025]] | 2025 | 多速率分区+交错等效交互，CHB-DAB频率差异利用 | 未量化 | 等同TSR精度 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Li 2025]] | 2025 | 开关函数统一建模+DC-link解耦，两层次等效（DEM/AVM） | 50-100x(AVM) | <0.5%(大步长) |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|Li 2026]] | 2026 | ImEx-Gear解耦+开关插值，60 SM SST实时验证 | 171x | <0.5%稳态误差 |

## 证据边界

- **已验证拓扑**：MMC型SST + DAB HFL（Gao 2022）、CHB-DAB ISOP型PET（Wang 2025, Li 2025, Li 2026）
- **已验证工具**：PSCAD/EMTDC（Gao 2022, Li 2025）、OPAL-RT（Li 2026）
- **已验证规模**：60子模块（Li 2026）、每相10 FBSM + 30 DAB（Li 2025）
- **未经验证**：MAB/SAB拓扑、故障穿越工况、器件寄生/死区效应、磁件非线性、保护逻辑、不同实时硬件平台
- **量化谨慎**：Li 2025的具体加速倍数（50-100x）和Li 2026的精度指标（<0.5%）来自原文可核验部分；Wang 2025的加速比和误差百分比未经量化报告

## 开放问题

1. 三种方法分支（端口消元、多速率、开关函数解耦）间是否存在统一数学框架？当前各自独立发展。
2. Li 2025和Gao 2022均用C⁻¹预处理实现恒定G矩阵，但方法适用范围（DAB HFL vs 全三阶段）不同，融合可能性待评估。
3. PET页面后续是否应提升为topic级页面，取决于相邻方法页（[[dual-active-bridge]], [[m3c]], [[n-port-network]]）和场景页的收敛情况。
4. 当前所有方法的验证基线均为详细开关模型，缺乏与硬件实测在故障暂态下的定量误差对比。
</｜DSML｜parameter>

## 来源论文

| 论文 | 年份 |
|------|------|
| [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix|Analysis and Prospect of Development of China]] | 2022 |
