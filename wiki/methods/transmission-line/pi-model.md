---
title: "PI 控制器模型 (PI Controller in EMT)"
type: method
tags: [pi-model, pi-controller, discretization, anti-windup, feedback-control]
created: "2026-05-06"
updated: "2026-05-11"
---

# PI 控制模型 (PI Controller in EMT)

## 物理背景与工程需求

比例-积分（PI）控制器是电力电子变流器控制中最基本的反馈调节结构。在电磁暂态（EMT）仿真中，PI 控制器广泛用于电流内环、电压外环、功率环、锁相环（PLL）和速度环等环节。其核心作用是消除稳态跟踪误差并调节动态响应速度，但其离散化方式、积分饱和处理、采样延迟和限幅逻辑会直接影响 EMT 波形的真实性和稳定性。

在 EMT 仿真中显式建模 PI 控制器而非使用理想传递函数的原因是：控制器的离散实现（尤其积分方法）、抗饱和策略和限幅行为会与主电路暂态相互作用，产生仅有连续域小信号分析无法预测的现象。例如，[[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]] 在 MMC-HVDC 系统中展示了 PI 电流内环比例系数过高会显著降低时滞稳定裕度，Zhang 等（2022）报告当 $k_p$ 从 5.0 增至 7.5 时，时滞稳定裕度从 347.90 μs 单调下降至 240.25 μs，降幅达 30.9%。

## 数学描述

### 连续域形式

标准 PI 控制器在连续时域的表达式为：

$$
u(t) = K_p e(t) + K_i \int_0^t e(\tau)\,d\tau
$$

其中 $e(t) = r(t) - y(t)$ 为误差信号，$K_p$ 为比例增益，$K_i$ 为积分增益。写成传递函数形式为：

$$G_c(s) = K_p + \frac{K_i}{s}$$

### 增量式与位置式

位置式 PI 直接计算控制量 $u(t)$，增量式只计算控制量的变化量 $\Delta u[k]$：

$$\Delta u[k] = K_p (e[k] - e[k-1]) + K_i T_s e[k]$$

增量式的优势在于限幅实现简单——只需累积 $\Delta u$ 到 $u[k]$ 后截断，积分状态不会在限幅期间错误累积。

## 计算模型与离散化

PI 控制器的 EMT 实现需要将连续积分方程离散化。三种常见的离散化方法各有特性：

### 前向欧拉法（Forward Euler）

$$x_i[k] = x_i[k-1] + K_i T_s e[k-1], \quad u[k] = K_p e[k] + x_i[k]$$

前向欧拉最为简单，但在 $K_i T_s$ 较大时可能引入数值不稳定的开环零点（据方法推断）。

### 后向欧拉法（Backward Euler）

$$x_i[k] = x_i[k-1] + K_i T_s e[k], \quad u[k] = K_p e[k] + x_i[k]$$

后向欧拉无条件稳定，是 EMT 程序中最常用的离散积分方法之一。

### 梯形法（Tustin/Bilinear）

$$x_i[k] = x_i[k-1] + \frac{K_i T_s}{2} (e[k] + e[k-1]), \quad u[k] = K_p e[k] + x_i[k]$$

梯形法的幅值和相位精度优于欧拉法，但在快速暂态中可能引入数值振荡（据方法推断）。

## 实现方法与算法细节

### 抗饱和策略

当 PI 输出达到执行器限幅时，若积分项继续累积，会导致控制量在退出饱和时产生严重过冲。常用的抗饱和策略有：
- **条件积分法**：输出限幅时冻结积分更新。
- **反算法**：将限幅前后的差值反馈衰减积分状态。
- **积分清零法**：饱和期间清零积分项。

[[dual-loop-pi-controller]] 中明确强调，如果控制输出达到调制或电流限制，积分项继续累积可能导致恢复时过冲，因此 EMT 模型中应显式表示条件积分、反算抗饱和或其他抗饱和策略。

### 与 dq 变换的配合

在 VSC 和 MMC 的 EMT 模型中，PI 控制器通常工作在 dq 同步旋转坐标系下。电流内环的典型实现包括：

$$v_d^* = K_p (i_d^* - i_d) + x_{i_d} - \omega L i_q + v_{gd}$$
$$v_q^* = K_p (i_q^* - i_q) + x_{i_q} + \omega L i_d + v_{gq}$$

其中前馈项 $\omega L i_{q,d}$ 和电网电压 $v_{gd,gq}$ 用于解耦。[[dynamic-performance-of-embedded-hvdc-with-13&14]]（Mengjia 等，2015）明确报告在 PSCAD/EMTDC 中采用此结构，并通过在参考层叠加频率补偿实现了平均 CCT 提升 22.93%。

### 采样延迟与等效延时

数字控制器的采样保持、计算延迟和 PWM 更新延迟在 EMT 模型中不可忽略。对于载波频率 $f_{sw}$，总的控制延迟通常为 $1.5T_s$（含 0.5 周期采样延迟和 1 周期 PWM 更新延迟）。[[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]（Zhang 等，2022）将链路延时统一建模为状态空间中的时滞项，并证明其对高频稳定性的影响随 PI 增益增大而急剧恶化。

## 适用边界与失效模式

### valid_when
- 系统工作点相对稳定，主电路参数已知且不剧烈变化
- 控制带宽远低于采样频率（通常内环带宽 < 1/10 采样频率）
- 被控对象可以用线性化一阶或二阶模型近似
- dq 坐标系下的解耦前馈项参数与实际系统匹配

### invalid_when
- LCL 滤波器谐振频率接近电流内环带宽时，纯 PI 控制可能无法抑制谐振
- 弱电网条件下 PLL 动态与电流环形成强耦合时（据 Luchini 2023，其 DSOGI-PLL 模型在 SCR 约 1 时仍可工作，但标准 PI 加 SRF-PLL 在该条件下接近稳定边界）
- 限幅激活期间，积分饱和导致响应严重超调且未配置抗饱和逻辑
- 链路总延时超过 PI 参数所允许的时滞稳定裕度（Zhang 2022 显示 $k_p=7.5$ 时仅允许 240.25 μs）

### assumptions
- 假设被控对象在 PI 控制带宽内可用线性模型近似（据方法推断）
- dq 解耦假设电网阻抗参数准确（据方法推断）

### evidence_gaps
- 当前来源未系统比较三种离散化方法在 EMT 波形中的具体差异
- 各抗饱和策略在不同限幅深度和持续时间下的性能对比原文未报告可核验的数值结果

## 应用案例

### VSC-HVDC 双环 PI 控制

[[dynamic-performance-of-embedded-hvdc-with-13&14]]（Mengjia 等，2015）在 IEEE 4 机 6 节点系统中使用标准 dq 双环 PI 结构：外环 PI 根据直流电压或功率目标生成 $i_{d,q}^*$，内环 PI 跟踪电流并生成调制信号。该基线控制达到的 CCT 为 0.39-0.57 s（依故障位置不同），叠加频率补偿后平均提升 22.93%。

### MMC-HVDC 电流内环 PI 参数敏感性

[[high-frequency-oscillation-analysis-and-suppression-strategy-of-mmc-hvdc-system-]]（Zhang 等，2022）定量分析了电流内环比例系数对 MMC-HVDC 高频稳定性的影响：$k_p$ 从 5.0 增至 7.5 使时滞稳定裕度从 347.90 μs 降至 240.25 μs，临界振荡频率从 927.63 Hz 升至 1147.11 Hz。该发现直接指导了 PI 参数的上限选择。

### 跟网型逆变器 PI 等效模型

[[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]]（Luchini 等，2023）在 ATP/ATPDraw 中实现了包含 PI 内环电流控制和 LPF-PLL 的跟网型逆变器等效模型。在稳态与对称/不对称故障条件下，该模型与全开关基准模型的输出电流平均误差约 2.33%，仿真时间降低约 70%。

## 延伸阅读

- [[dual-loop-pi-controller]]：双闭环级联 PI 控制器的结构和设计步骤。
- [[pi-controller-model]]：面向实现的 PI/PID 模型离散化和抗饱和细节。
- [[control-system]]：EMT 中控制系统建模的总体框架。
- [[pll-model]]：PI 在同步环节（SRF-PLL）中的具体应用。
- [[fixed-admittance]]：PI 控制输出与 EMT 网络求解器的接口方法。
- [[vector-control]]：dq 坐标系下的 PI 控制典型场景。
