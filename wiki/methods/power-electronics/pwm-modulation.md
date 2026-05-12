---
title: "PWM 调制方法 (PWM Modulation)"
type: method
tags: [pwm-modulation, pwm, spwm, svpwm, cps-spwm, nlm, modulation, converter-control, switching]
created: "2026-05-04"
updated: "2026-05-12"
---

# PWM 调制方法 (PWM Modulation)

## 1. 物理背景与工程需求

脉宽调制（PWM）是将控制器输出的连续调制参考信号转换为功率开关器件通断时序的基本方法，是连接控制层与主电路层的桥梁。在 EMT 仿真中，PWM 的执行方式直接决定开关事件的位置、谐波分布和仿真步长约束。

PWM 调制在 EMT 中的工程需求包括：

1. **调制参考到开关信号的转换**：控制器的电压/电流参考经 dq→abc 变换后，需通过 PWM 生成具体的开关触发时序（Ebrahimi & Jatskevich 2023）
2. **多电平调制策略选择**：两电平 VSC 使用 SPWM/SVPWM，MMC 等多电平换流器使用 CPS-SPWM 或 NLM，不同调制策略在 EMTP 中步长约束差异大
3. **调制指数与 EMT 等效模型的接口**：调制指数 m 被直接用作 VSC 平均值模型的输入参数，决定 AC/DC 侧阻抗折算关系（Bahirat, Høidalen & Mork 2015）
4. **开关频率与仿真效率的权衡**：开关频率越高，EMT 步长越受限，平均值模型和 NLM 等效模型可在毫秒级步长下回避开关级细节（Zhao 2023）

## 2. 数学描述

### 2.1 基本占空比关系

PWM 的基本占空比定义为导通时间与开关周期的比值：

$$
d(t) = \frac{t_{\text{on}}}{T_s}
$$

对正弦 PWM（SPWM），调制波与载波比较生成占空比：

$$
d(t) = \frac{1}{2}\left[1 + m\cos(\omega_0 t)\right], \quad m = \frac{V_{\text{ref}}}{V_{\text{carrier}}}
$$

其中 $m$ 为调制指数，线性调制区 $0 \leq m \leq 1$，过调制区 $m > 1$（Bahirat, Høidalen & Mork 2015）。

### 2.2 调制指数与 EMT 等效模型的关系

在 dq 坐标系下的平均模型中，调制指数直接决定 AC/DC 侧的电压和电流变换关系（Bahirat, Høidalen & Mork 2015）：

$$
v_d = \frac{m_d}{2}V_{dc}, \quad v_q = \frac{m_q}{2}V_{dc}
$$

$$
i_{dc} = \frac{3}{4}(m_d i_d + m_q i_q)
$$

Ebrahimi & Jatskevich (2023) 使用调制比 $M$ 和功角 $\delta$ 表达相同关系：

$$
\bar{v}_{qd} = \frac{1}{2} M \begin{bmatrix} \cos(\delta) \\ \sin(\delta) \end{bmatrix} \bar{v}_{dc}
$$

### 2.3 空间矢量 PWM（SVPWM）的电压利用率

SVPWM 通过八个基本电压矢量的合成逼近目标旋转矢量，电压利用率比 SPWM 高约 15.5%：

$$
V_{\text{max,SVPWM}} = \frac{V_{dc}}{\sqrt{3}}, \quad V_{\text{max,SPWM}} = \frac{V_{dc}}{2}
$$

比例 $V_{\text{max,SVPWM}}/V_{\text{max,SPWM}} = 2/\sqrt{3} \approx 1.155$。

### 2.4 载波移相 PWM（CPS-SPWM）

对 MMC 等 N 子模块级联的换流器，各子模块载波相位依次偏移 $360^\circ/N$，等效开关频率提升至 $N \cdot f_{sw}$，在不增加每个子模块开关频率的条件下降低输出谐波。

### 2.5 最近电平调制（NLM）

对 MMC 等高电平数换流器，NLM 用量化电平数代替高频 PWM 载波：

$$
n_{\text{on}} = \text{round}\left(\frac{v_{\text{ref}}}{V_c}\right)
$$

Zhao (2023) 将 NLM 等效占空比分解为稳态分量和波动分量：

$$
d_{eq} = d_{\text{stable}} + d_{\text{fluctuation}}
$$

## 3. 计算模型与离散化

### 3.1 PWM 在 EMT 每时间步中的角色

EMT 仿真中，PWM 在每个时间步 $n$ 的执行位于控制链末端：

1. 测量电气量 → 2. 外环 PI 计算参考 → 3. 内环 PI 生成调制波 → 4. **PWM：调制波→开关信号** → 5. 更新开关状态 → 6. 求解网络方程

对于详细开关模型，PWM 需要在每个步长内比较调制波与载波，决定开关动作时刻。开关动作落在步长内部时，需插值处理以避免波形畸变。

### 3.2 平均值模型中调制指数的直接嵌入

Ebrahimi & Jatskevich (2023) 的 DI-AVM 将 PWM 的调制效果（$M, \delta$）直接嵌入节点导纳矩阵：

$$
G_{VSC}^{abc,dc} \begin{bmatrix} v_{abc}^1 \\ \bar{v}_{dc} \end{bmatrix} = \begin{bmatrix} i_{abc}^1 \\ \bar{i}_{dc} \end{bmatrix} + i_{h,VSC}^{abc,dc}
$$

调制指数 $M$ 和功角 $\delta$ 出现在导纳矩阵 $G_{VSC}$ 和历史项 $i_h$ 中，使 PWM 平均效果在非迭代求解中与网络方程同步。此模型在 SPWM 策略（$f_{sw}=1620$ Hz）下验证，步长可达 1000 $\mu$s，为传统间接接口模型的 10 倍（Ebrahimi & Jatskevich 2023）。

### 3.3 NLM 等效模型的离散化（Zhao 2023）

Zhao (2023) 的 NLM 等效模型将每步长的计算任务从"载波比较 + 排序选择"简化为：

1. 读取调制波 → 计算 $d_{\text{stable}}$（桥臂基波电压）
2. 每个子模块的闭环控制器根据电容电压偏差计算 $d_{\text{fluctuation}}$（均衡波动）
3. $d_{eq} = d_{\text{stable}} + d_{\text{fluctuation}}$ → 映射为受控电压源
4. 代入网络导纳方程求解

该模型步长可放宽至 1--5 ms，在 0--500 Hz 范围内误差 $< 0.5\%$（Zhao 2023）。

### 3.4 调制指数依赖的阻抗折算

Bahirat, Høidalen & Mork (2015) 将 PWM 调制指数作为 VSC 直流侧等效阻抗的决定因素：

$$
Z_{dc,eq} = \frac{8}{3(m_d^2 + m_q^2)}(R + j\omega L)
$$

此式说明调制指数不仅决定电压变换比，还影响直流侧呈现的等效阻抗。在 SPWM 线性调制范围内，$m \in [0,1]$ 导致等效阻抗随运行点变化。

## 4. 实现方法与算法细节

### 4.1 PWM 变体对比

| 调制策略 | 机制 | 适用场景 | EMT 代价 |
|----------|------|----------|----------|
| SPWM | 正弦波与三角载波比较 | 两电平 VSC、通用逆变器 | 开关频率决定步长上限 |
| SVPWM | 八矢量合成旋转矢 | 两电平静止补偿器、电机驱动 | 计算量略高于 SPWM，电压利用率高 15.5% |
| CPS-SPWM | $N$ 载波依次移相 $360^\circ/N$ | MMC、级联 H 桥 | 等效开关频率高，但各子模块开关频率不变 |
| NLM | 电平量化替代载波比较 | 高电平 MMC（$N \geq 50$） | 可配毫秒级步长（Zhao 2023），需 O(N) 排序 |
| NLM 等效模型 | $d_{\text{stable}} + d_{\text{fluctuation}}$ 连续等效 | 大规模 MMC 系统级研究 | 步长 1--5 ms，误差 $< 0.5\%$（Zhao 2023） |

### 4.2 调制指数观测器

调制指数 $m_d, m_q$ 在实际系统中不可直接测量。Bahirat, Høidalen & Mork (2015) 设计了状态观测器实时估算 $m_d$ 和 $m_q$ 用于等效电路参数更新，观测器在 2--3 个基频周期内收敛，稳态误差 $< 0.5\%$。

### 4.3 PWM 饱和与限幅

调制指数超过线性区时（$m > 1$ 或 SVPWM 六边形边界），PWM 进入过调制区或饱和区。此状态下：
- 输出电压基波幅值不再随调制指数线性增加
- 低次谐波显著增大
- 控制器的 dq 电流内环应设限幅，防止调制参考超出 PWM 饱和边界（Nurunnabi 2025 的 PWM 饱和约束）

### 4.4 多电平换流器的调制映射

MMC 的 PWM 执行需将调制参考映射到各子模块的导通/切除状态。CPS-SPWM 中每个子模块独立载波，NLM 中每个仿真步根据排序结果选择导通的子模块数。Zhao (2023) 的等效模型用电压闭环自动生成波动分量，避免逐级执行排序逻辑。

## 5. 适用边界与失效模式

### 适用条件

- 详细开关 EMT 仿真中，PWM 策略需与开关频率、步长和拓扑匹配
- 平均值模型中，调制指数 $m$（或 $M, \delta$）作为已知输入参数可用（Ebrahimi & Jatskevich 2023）
- NLM 等效模型适用于关注低频动态的大规模 MMC 仿真，步长 1--5 ms（Zhao 2023）
- 调制指数依赖的阻抗折算适用于两电平 VSC 直流故障研究（Bahirat, Høidalen & Mork 2015）

### 失效模式

| 失效场景 | 原因 | 后果 |
|----------|------|------|
| 过调制区 PWM 失真 | $m > 1$ 后基波非线性 | 低次谐波增大，控制性能下降 |
| 平均值模型掩盖开关细节 | AVM 不解析开关事件位置 | 开关纹波、EMI 和器件应力被忽略 |
| 调制指数未更新的接口延迟 | 间接接口 AVM 用上一拍调制量 | Ebrahimi & Jatskevich (2023) 证明大步长下误差发散 |
| NLM 等效模型高频失效 | $d_{\text{fluctuation}}$ 闭环在高频段精度下降 | Zhao (2023) 确认误差 $< 0.5\%$ 限于 0--500 Hz |
| PG 故障下调制指数等效偏差 | 零序分量处理简化 | 故障电流低估 5--10%（Bahirat, Høidalen & Mork 2015） |

### 关键约束

- SPWM 线性调制区 $m \leq 1$，过调制区需额外谐波建模；SVPWM 线性区扩大约 15.5% 但仍有物理上限
- 平均值模型和 NLM 等效模型需要验证针对的开关策略和频率范围——SPWM 验证不保证适用 SVPWM 或 CPS-SPWM
- Bahirat, Høidalen & Mork (2015) 的调制指数等效阻抗结论基于 SPWM，且只在所报告测试系统（±150 kV, 300 MW 两电平 VSC）内验证
- Zhao (2023) 的 NLM 等效模型结论限于 0--500 Hz 和毫秒级步长，高频或详细开关场景需回到原始 NLM 开关模型

## 6. 量化性能边界

**Bahirat, Høidalen & Mork (2015) 调制指数依赖VSC戴维南等效模型**：
- 方法：SPWM调制指数m通过状态观测器实时估算，m∈[0,1]线性调制区
- dq帧平均方程：v_d=m_d·Vdc/2, v_q=m_q·Vdc/2; Z_dc_eq=8(R+jωL)/(3(m_d²+m_q²))
- PP故障等效模型误差<1%，PG故障误差5~10%
- 750 μs步长下126倍加速（vs 5 μs详细模型）
- 验证：ATP-EMTP，±150 kV/300 MW两电平VSC
- 数据缺口：PG故障误差5~10%的物理根源和分析未深入；仅在两电平VSC验证，MMC多电平未覆盖

**Ebrahimi & Jatskevich (2023) DI-AVM直接接口VSC平均值模型**：
- 方法：调制比M和功角δ直接嵌入节点导纳矩阵，SPWM验证(f_sw=1620 Hz)
- 平均qd电压：v̄_qd=½·M·[cos(δ); sin(δ)]·v̄_dc
- DI-AVM步长可达1000 μs（vs间接接口~100 μs），交流侧2-范数误差在1000 μs下保持极低
- 直接接口模型在大步长下不发散，间接接口模型在同等大步长下发散
- 验证：两电平VSC EMTP仿真
- 数据缺口：仅在SPWM策略下验证，SVPWM和CPS-SPWM下的适用性未报告

**Zhao et al. (2023) NLM等效模型（MMC）**：
- 方法：占空比分解为d_stable（调制波）+d_fluctuation（电容电压闭环均衡）
- 步长1~5 ms（vs详细NLM μs级），0~500 Hz误差<0.5%
- 电容电压偏差<±2%，计算复杂度O(N)
- 验证：N≥200子模块MMC-HVDC系统EMT仿真
- 数据缺口：等效模型在500 Hz以上频段的精度未验证；在非对称故障和直流故障场景下的适用性未系统评估

**数据缺口声明**：三种PWM建模方法（调制指数等效、DI-AVM、NLM等效）针对不同换流器拓扑（两电平VSC vs MMC）和调制策略（SPWM vs NLM），直接横向对比不可行。三者均在各自假设的开关策略和拓扑下验证，方法的通用性边界尚未系统建立。PWM在故障暂态（过调制区、非对称故障）下的建模误差缺乏统一量化框架。

- [[switch-modeling]]：开关建模的不同层级，PWM 生成的开关信号驱动开关模型
- [[average-value-model]]：PWM 的周期平均效果，调制指数 $M$ 作为 AVM 的输入参数
- [[switching-function-method]]：用开关函数表达调制逻辑的另一种方法
- [[vector-control]]：dq 电流内环的输出经 dq→abc 变换后作为 PWM 的调制参考
- [[grid-forming-inverter]]：GFM 逆变器中下垂→电压环→电流环→PWM 的完整控制链
- [[nearest-level-modulation]]：NLM 的专门页面，与 PWM 同属调制方法
- [[companion-circuit]]：PWM 开关事件在伴随模型中的历史项重置
- [[fpga-real-time-simulation]]：FPGA 上 PWM 生成的并行流水线实现
