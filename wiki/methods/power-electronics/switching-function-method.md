---
title: "开关函数法 (Switching Function Method)"
type: method
tags: [switching-function, average-value, modulation, converter, power-electronics, state-space-average]
created: "2026-05-02"
updated: "2026-05-10"
---

# 开关函数法 (Switching Function Method)

## 1. 物理背景与工程需求

开关函数法用离散或连续函数表示功率电子开关网络的连接状态，是将调制、拓扑和方程联系起来的数学表达方式。它不是一种独立的仿真模型，而是一种表达框架——不同的建模层级使用不同粒度的开关函数表示，其精度和计算成本差异显著。

开关函数法在 EMT 中的工程需求包括：

1. **详细开关级建模**：二值开关函数 $s(t) \in \{0,1\}$ 精确描述每个开关器件的通断状态，直接决定网络拓扑变化（Meng 2020）
2. **平均值模型（AVM）**：周期平均开关函数 $d(t) \in [0,1]$ 替代二进制开关信号，使仿真步长从微秒级放宽至百微秒级（Cao 2026）
3. **多电平换流器统一建模**：插入指数 $s_n$ 将开关函数概念推广至 MMC 等子模块级联拓扑的桥臂等效（Meng 2020）
4. **谐波保留仿真**：在平均值模型骨架中同步计算开关函数对应的谐波分量，突破传统 AVM 丢失谐波的限制（Cao 2026）

## 2. 数学描述

### 2.1 二值开关函数

对半桥桥臂，开关函数定义上下开关的互补状态：

$$
s(t)=
\begin{cases}
1, & \text{上桥臂导通}\\
0, & \text{下桥臂导通}
\end{cases}
$$

极点电压由开关函数和直流电压决定：

$$
v_{xO}=\left(s_x-\frac{1}{2}\right)V_{\mathrm{dc}},\qquad x\in\{a,b,c\}.
$$

直流侧电流由交流侧电流和开关函数耦合：

$$
i_{\mathrm{dc}}=\mathbf{s}^{T}\mathbf{i}_{abc},
$$

### 2.2 平均开关函数（占空比）

对开关周期平均：

$$
d_x(t)=\frac{1}{T_s}\int_{t}^{t+T_s}s_x(\tau)\,d\tau,
$$

得到平均电压关系：

$$
\bar{\mathbf{v}}_{abc}=
\left(\mathbf{I}-\frac{1}{3}\mathbf{1}\mathbf{1}^{T}\right)
\left(\mathbf{d}-\frac{1}{2}\mathbf{1}\right)V_{\mathrm{dc}}.
$$

Cao (2026) 在 HP-AVM 中将此平均化推广到状态空间矩阵：

$$
\dot{\bar{x}} = \bar{A} \bar{x} + \bar{b},\quad
\bar{A} = A_0 + \sum_{k=1}^N (D_{\text{up},k} A_{\text{up},k} + D_{\text{low},k} A_{\text{low},k})
$$

其中二进制 $S \in \{0,1\}$ 被连续占空比 $D \in [0,1]$ 替代。

### 2.3 MMC 的统一开关函数表示

Meng (2020) 的广义开关函数 AVM（GSFB-AVM）使用插入指数作为桥臂级开关函数：

$$
s_n = \frac{1}{N} \sum_{i=1}^N s_i
$$

桥臂等效电容：

$$
C_{\text{eq}}^{\text{arm}} = \frac{C_{\text{SM}}}{N}
$$

广义电容电压更新方程统一不同子模块拓扑和运行模式：

$$
v_{\text{cavg}}(t+\Delta t) = v_{\text{cavg}}(t) + (\bar{b}s_n + b)(i_{D1}(t) - m i_{D2}(t)) \frac{\Delta t}{C_{\text{eq}}^{\text{arm}}}
$$

### 2.4 闭锁模式下的开关函数

Meng (2019) 将开关函数概念嵌入通用阻塞模块：当 MMC 进入闭锁模式后，开关函数不再由控制信号决定，而是由子模块类型（HB/FB/MB）和电流方向共同确定二极管的导通路径。桥臂等效通态电阻：

$$
R_{\text{arm}} = N R_{\text{on}} (2 - \rho)
$$

其中 $\rho$ 为 HB 子模块比例。

## 3. 计算模型与离散化

### 3.1 开关函数法在各建模层级中的角色

| 建模层级 | 开关函数形式 | EMT 实现方式 | 步长约束 |
|----------|-------------|-------------|----------|
| 详细开关模型 | $s(t) \in \{0,1\}$ | 直接决定拓扑/导纳 | 受开关频率限制（$< 10$ $\mu$s） |
| 等效平均模型 | $d(t) \in [0,1]$ | 受控源/节点导纳矩阵 | $\sim 50$ $\mu$s（Meng 2019） |
| 广义开关函数 AVM | 插入指数 $s_n$ | 桥臂等效电容 + 受控源 | $\sim 20$ $\mu$s（Meng 2020） |
| HP-AVM | $D$ 替代 $S$ | 平均矩阵 + 同步谐波计算 | $\sim 10-50$ $\mu$s（Cao 2026） |

### 3.2 插入指数的离散更新

在 GSFB-AVM 中，开关函数（插入指数）的离散更新与 MMC 控制器的输出同步（Meng 2020）：

1. 从控制器获取调制波 → 计算 $s_n$
2. 检测桥臂电流方向 → 确定 $i_{D1}$ 或 $i_{D2}$
3. 根据子模块拓扑确定模式系数 $b, \bar{b}, m$
4. 更新平均电容电压 $v_{\text{cavg}}$
5. 计算桥臂等效受控电压源

GSFB-AVM 在 4800 子模块下单步仅需 9.45 $\mu$s，计算复杂度与 $N$ 解耦（Meng 2020）。

### 3.3 HP-AVM 的半载波周期占空比预测

Cao (2026) 的 HP-AVM 引入半载波周期（HCP）占空比预测策略：在每个 HCP 起始时刻预测未来半个载波周期内的平均占空比 $D$，矩阵求逆频率从每开关周期一次降至每 HCP 一次，速度较开关函数模型（SFM）提升 5--6 倍。

### 3.4 模型切换时的开关函数映射

当 GSFB-AVM 与详细等效模型（DEM）切换时，开关函数状态需通过能量等价映射（Meng 2020）：
- AVM → DEM：$v_{ci}(t) = v_{\text{cavg}}(t)/N$（平均电压均分）
- DEM → AVM：$v_{\text{cavg}}(t) = \sum v_{ci}(t)$（个体电压累加）

## 4. 实现方法与算法细节

### 4.1 开关函数变体对比

| 变体 | 表示方式 | 适用问题 | 限制 |
|------|----------|----------|------|
| 二值开关函数 | $s(t) \in \{0,1\}$ 或 $\{-1,1\}$ | 详细开关级 EMT、调制逻辑验证 | 步长受限，计算量大 |
| 平均开关函数 | $d(t) \in [0,1]$ | 低频控制和系统级暂态 | 丢失载波边带和开关纹波 |
| 插入指数 | $s_n = \frac{1}{N}\sum s_i$（Meng 2020） | MMC 桥臂级平均等效 | 需闭锁模式修正 |
| 谐波保留开关函数 | $D$ + 谐波分量（Cao 2026） | 保留谐波的系统级仿真 | 计算量高于传统 AVM |
| 阻塞模块开关函数 | 拓扑相关导通路径（Meng 2019） | MMC 闭锁/故障场景 | 仅适用于 MMC 类拓扑 |

### 4.2 死区与互锁的处理

理想互补关系 $s_{\text{lower}} = 1 - s_{\text{upper}}$ 在死区时间内不成立。开关函数法需在详细模型中显式包含死区状态，否则会低估畸变和桥臂短路风险。

### 4.3 闭锁/解锁模式切换

Meng (2019) 在 UBM-AVM 中展示：闭锁模式下开关函数由电流方向自动决定，而非由控制信号决定。解锁模式下 UBM 被强制反偏隔离，闭锁模式下动态反映电容充电过程。

### 4.4 开关函数的谐波恢复

Cao (2026) 的 HP-AVM 在平均值计算框架内同步计算开关谐波分量：在每个仿真步长内，基于当前开关状态与占空比偏差，通过时域谐波模型直接计算各次开关谐波分量（5次、7次、11次等）。谐波幅值误差 $< 1.5\%$（相对 SFM）。

## 5. 适用边界与失效模式

### 适用条件

- 二值开关函数适用于需要精确开关时序和波形的详细 EMT 仿真
- 平均开关函数适用于低频动态为主、开关纹波不重要的系统级研究
- 插入指数法适用于 MMC 等多电平换流器的桥臂级平均等效（Meng 2020）
- 谐波保留开关函数适用于需要谐波信息的系统级仿真（Cao 2026）
- 阻塞模块开关函数适用于 MMC 闭锁/故障场景（Meng 2019）

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| 死区忽略 | 互补关系 $s_{\text{lower}} = 1 - s_{\text{upper}}$ 不成立 | 低估电压畸变，忽略桥臂短路风险 |
| 平均化丢失谐波 | $s(t) \to d(t)$ 抹去载波边带 | 丢失开关纹波、电磁干扰和谐振信息 |
| 闭锁时继续使用解锁开关函数 | 闭锁后导通路径由二极管而非控制信号决定 | Meng (2019) 指出充电和故障仿真失准 |
| AVM 切换后状态不连续 | 缺乏能量等价映射 | 虚假电压阶跃（Meng 2020 用均分/累加消除） |
| 开关函数未含器件非理想性 | 导通压降、反向恢复、寄生电容不在 $s(t)$ 中 | 器件应力和损耗不可得 |

### 关键约束

- 开关函数法不是一种精度保证——相同符号在不同参考点、桥臂极性和平均窗口下对应不同物理量
- 二值开关函数 $s(t)$ 到平均开关函数 $d(t)$ 的转换丢失了开关频率和载波边带信息，除非使用 HP-AVM 显式保留（Cao 2026）
- GSFB-AVM 的复杂度与 $N$ 解耦结论基于 Meng (2020) 给出的 20 $\mu$s 步长和 OPAL-RT 平台，不保证适用其他硬件或步长
- 闭锁模式下的开关函数行为取决于子模块拓扑（HB/FB/MB），通用形式需要 Meng (2019) 的阻塞模块等效

## 6. 应用案例

### 案例 1：GSFB-AVM 的 MMC 统一仿真框架（Meng 2020）

场景：含 HBSM、FBSM、CDSM、MBSM 的 41 电平 MMC-HVDC 系统。插入指数 $s_n$ 作为桥臂级开关函数，输入为控制器调制信号，经广义电容更新方程生成桥臂受控电压源。GSFB-AVM 单步 9.45 $\mu$s（4800 SM），DEM 单步 51.59 $\mu$s（480 SM），功率阶跃相对误差 $< 0.4\%$，直流故障误差 $< 0.3\%$。

### 案例 2：HP-AVM 谐波保留仿真（Cao 2026）

场景：三相两电平逆变器并网系统。传统 AVM 将开关函数 $S$ 替换为占空比 $D$，丢失 5、7 次谐波；HP-AVM 在平均骨架中同步计算谐波分量。基波误差 $< 0.5\%$，谐波幅值误差 $< 1.5\%$，速度较 SFM 提升 5--6 倍。

### 案例 3：UBM-AVM 闭锁模式 MMC 仿真（Meng 2019）

场景：41 电平双端 MMC-HVDC 系统的交流充电启动和直流极间故障。闭锁模式下开关函数由二极管导通路径决定，UBM 动态反映电容充电过程。直流故障峰值误差 $< 1.5\%$，步长从 1--5 $\mu$s 放大至 50 $\mu$s，速度提升 15--20 倍。

## 7. 延伸阅读

- [[switch-modeling]]：开关建模的不同层级，开关函数法的底层实现
- [[average-value-model]]：用平均开关函数替代详细开关动作的建模方法
- [[state-space-average-method]]：将不同开关状态的状态方程按开关函数加权平均
- [[pwm-modulation]]：从调制参考到开关函数 $s(t)$ 的生成过程
- [[companion-circuit]]：开关函数变化时的伴随模型历史项重置
- [[power-electronics-control]]：开关函数法在电力电子控制中的角色
</｜DSML｜parameter>

## 来源论文

| 论文 | 年份 |
|------|------|
| [[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model-22|Hybrid Transient Stability Simulation Using Dynamic Phasor B]] | 2006 |
| [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-system-model|Hybrid-model transient stability simulation using dynamic ph]] | 2006 |
| [[modular-multilevel-converter-models|Modular Multilevel Converter Models]] | 2013 |
| [[a-universal-blocking-module-based-average-value-model-of-modular-multilevel-conv|A Universal Blocking-Module-Based Average Value Model of Mod]] | 2019 |
| [[combining-detailed-equivalent-model-with-switching-function-based-average-value-|Combining Detailed Equivalent Model With Switching-Function-]] | 2020 |
| [[2728模块化多电平换流器时间尺度变换建模和仿真|模块化多电平换流器时间尺度变换建模和仿真]] | 2022 |
| [[modeling-and-simulation-of-vsc-hvdc-with-dynamic-phasors|Modeling and simulation of VSC-HVDC with dynamic phasors]] | 2023 |
| [[多有源桥型电力电子变压器简化电磁暂态等效模型|多有源桥型电力电子变压器简化电磁暂态等效模型]] | 2023 |
| [[efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f|Efficient electromagnetic transient simulation for DFIG-base]] | 2024 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[harmonic-preserved-average-value-model-for-converters-in-electromagnetic-transie|Harmonic-Preserved Average-Value Model for Converters in Ele]] | 2026 |
| [[vsc-hvdc-系统的动态相量法建模仿真分析|VSC-HVDC 系统的动态相量法建模仿真分析]] | 2026 |
