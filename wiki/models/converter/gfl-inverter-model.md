---
title: "跟网型变流器 (Grid-Following Inverter, GFL)"
type: model
tags: [grid-following, gfl, current-control, pll, renewable-energy, inverter, ibr]
created: "2026-04-30"
updated: "2026-05-16"
---

# 跟网型变流器 (Grid-Following Inverter, GFL)

## 定义

跟网型变流器（Grid-Following Inverter, GFL）是当前新能源并网的主流技术路线，通过锁相环（PLL）跟踪电网相位，以电流源模式向电网注入有功/无功功率。GFL变流器不尝试维持电压和频率支撑，而是被动跟随电网相位——这使它在强电网下稳定可靠，但在弱电网下因PLL与电网阻抗的交互可能引发次同步振荡（SSO）和动态不稳定。

GFL的核心特征是**电流控制+PLL同步**：控制器给出dq坐标系下的电流指令 $(i_d^*, i_q^*)$，PWM将dq电压指令 $(v_d^*, v_q^*)$ 转换为变流器端口电压。PLL从电网电压提取相位角 $\theta_{pll}$，用于坐标变换和同步。

## EMT中的角色

GFL在EMT仿真中的核心角色是**新能源并网接口模型**。随着光伏、风电、储能渗透率提升，GFL变流器已成为电网中占比最高的电力电子接口类型（约60-80%的新能源装机容量）。EMT仿真的任务包括：

- **故障电流特性**：GFL故障电流受PLL和电流环支配，与同步机的短路电流特性完全不同（同步机短路电流峰值可达10倍额定，GFL受电流限幅限制约1.5-2倍）
- **次同步振荡分析**：PLL带宽与弱电网阻抗交互，在2-10Hz范围产生振荡模式（次同步控制振荡，SSCO）
- **故障穿越（FRT）**：低电压穿越期间GFL需维持注入无功支撑电网，PWM饱和、PLL失锁、电流限幅共同决定故障响应
- **谐波相互作用**：PWM谐波与电网背景谐波的交互，以及多GFL并联时的谐波聚合

### 关键挑战

GFL的EMT建模面临多时间尺度耦合的挑战：PLL同步（10-100ms量级）、电流环控制（1-10ms）、PWM开关（0.1-1ms）、以及功率器件的开通关断（μs级）。如何在保持物理可解释性的前提下合理简化，是EMT建模的核心问题。

## 形式化表达

### 同步旋转坐标系电压方程

在PLL估计的dq坐标系下，GFL端口电压方程为：

$$\frac{di_d}{dt} = \frac{1}{L}\left(v_d - Ri_d + \omega L i_q - v_{dc}s_d\right)$$

$$\frac{di_q}{dt} = \frac{1}{L}\left(v_q - Ri_q - \omega L i_d - v_{dc}s_q\right)$$

其中 $v_d, v_q$ 为电网电压分量，$i_d, i_q$ 为变流器输出电流，$R, L$ 为滤波器阻抗，$v_{dc}$ 为直流电压，$s_d, s_q$ 为dq坐标系下的等效开关函数。

### 锁相环（PLL）模型

SRF-PLL（同步参考帧锁相环）的动态方程为：

$$\frac{d\theta_{pll}}{dt} = \omega_{pll} = \omega_{ff} + K_p^{pll} v_q + K_i^{pll} \int v_q dt$$

其中 $K_p^{pll}, K_i^{pll}$ 为PI参数，$\omega_{ff}$ 为前馈频率。DSOGI-PLL在q轴引入二阶广义积分器（Second-Order Generalized Integrator, SOGI）构造正交信号，可抑制电网电压不平衡和谐波影响。

### 功率环与电流环

GFL采用双环级联控制：

**功率外环（慢动态）**：

$$i_d^* = \left(K_p^p + \frac{K_i^p}{s}\right)(P_{ref} - P), \quad i_q^* = \left(K_p^q + \frac{K_i^q}{s}\right)(Q_{ref} - Q)$$

**电流内环（快动态）**：

$$v_d^* = \left(K_p^c + \frac{K_i^c}{s}\right)(i_d^* - i_d) - \omega L i_q + v_d$$

$$v_q^* = \left(K_p^c + \frac{K_i^c}{s}\right)(i_q^* - i_q) + \omega L i_d + v_q$$

### 五模型精度-效率映射

GFL变流器在EMT仿真中有五种典型建模粒度，按精度从高到低排列如下：

| 模型类型 | 精度 | 计算效率 | 步长范围 | 适用场景 | 失效场景 |
|---------|------|---------|---------|---------|---------|
| **SW**（详细开关模型） | 最高 | 最低 | 1-10 μs | 谐波分析、开关纹波、死区效应 | 大系统、实时HIL |
| **VI**（电压插值模型） | 高 | 中 | 10-50 μs | 含PWM调制的详细控制 | 极高次谐波 |
| **AV**（平均值模型） | 中高 | 高 | 50-100 μs | 故障穿越、控制交互 | 开关纹波、谐波精度 |
| **CCI**（受控电流注入模型） | 中 | 很高 | 100-500 μs | 机电暂态接口、网络等值 | 详细开关事件 |
| **SCI**（简化电流注入模型） | 中低 | 极高 | 500 μs-1 ms | 大系统批量扫描 | 非线性控制、故障暂态 |

**量化数据**：Luchini (2023) 在ATP/ATPDraw中实现的GFL等效时域模型（含DSOGI-PLL和电流环），与全开关模型相比，故障电流平均误差约2.33%，仿真时间减少约70%。Carreño (2026) 的RMS+模型在单换流器场景下与EMT偏差小于0.5%，而传统RMS模型在跨临界分岔边界完全失效。DAVM (2012) 在5 μs步长下CPU减少50-54%，≥40 μs步长下减少60-70%。

## 关键技术挑战

### PLL与弱电网交互失稳

当电网强度 SCR < 3（弱电网）时，PLL与电网阻抗的交互可能导致小信号失稳。PLL的闭环传递函数在dq坐标系下等效为一个与电网电抗串联的负电阻，在特定频段（通常2-10Hz）提供负阻尼。Ranasinghe (2024) 的改进型DSOGI-PLL将SCR稳定下限从2.3扩展至1.0。

**量化边界**：SCR < 2时Hopf分岔临界功率下降约40%（从0.9 pu降至0.55 pu），时间尺度比 $\tau_L/\tau_{PLL} < 0.1$ 时误差小于2%。

### 电流限幅与故障穿越

GFL在电网故障时受直流侧电压支撑能力和电流限幅器的约束，输出电流被钳位在1.1-1.5倍额定值。与同步机的短路电流特性形成鲜明对比：同步机峰值可达10倍额定，而GFL受功率半导体器件的IGBT电流承受能力限制。故障期间PLL输入电压可能跌落至正常值的20-30%，PLL失锁是GFL脱网的主要原因之一。

### 谐波与间谐波注入

PWM开关产生特征谐波（次谐波簇 $n\omega_1 \pm k\omega_{pll}$）和非特征谐波（直流偏置、间谐波），多GFL并联时谐波聚合效应在电网谐波阻抗上产生电压畸变，反过来影响各GFL的PLL同步精度。

## 适用边界与选择指南

### 按电网强度选择

| 电网强度 | SCR范围 | 推荐模型 | 关键考虑 |
|---------|--------|---------|---------|
| 强电网 | SCR > 5 | SW/VI/AV/CCI均适用 | 精度主要取决于开关细节是否影响研究目标 |
| 弱电网 | 2 < SCR < 5 | VI/AV（需含PLL模型） | 必须保留PLL动态，否则无法捕捉SSCO |
| 极弱电网 | SCR < 2 | SW/VI（需详细PLL） | 推荐SRF-PLL带宽自适应降频，否则失稳 |

### 按仿真目标选择

| 研究目标 | 推荐模型 | 步长 | 原因 |
|---------|---------|------|------|
| 谐波分析 | SW/VI | 1-20 μs | 需保留PWM开关细节 |
| 次同步振荡 | VI/AV（含PLL） | 10-50 μs | 需PLL带宽和电网阻抗交互 |
| 故障穿越/短路电流 | AV/CCI | 50-200 μs | 电流限幅和FRT逻辑 |
| 大系统参数扫描 | CCI/SCI | 200-1000 μs | 计算效率优先 |

### 模型选择决策表

**问题一**：是否需要保留开关纹波？
- **否**（只看控制响应）→ 跳到问题二
- **是**（谐波、电磁兼容）→ SW或VI模型

**问题二**：是否涉及弱电网（SCR < 3）或次同步振荡？
- **是** → 必须选含完整PLL的VI或AV模型，不能用CCI/SCI
- **否** → 跳到问题三

**问题三**：系统规模是否超过100节点或需要实时仿真？
- **是** → CCI或SCI，牺牲精度换取速度
- **否** → AV模型作为默认选择

## 相关方法

- [[pll-model]] - 锁相环动态建模与参数整定
- [[pi-controller-model]] - PI控制器参数设计
- [[coordinate-transformation-model]] - dq坐标系等效电路
- [[average-value-model]] - 平均值模型的GFL变体
- [[state-space-method]] - 状态空间表示与小信号分析
- [[harmonic-analysis]] - 并网谐波与间谐波分析

## 相关模型

- [[gfm-inverter-model]] - 构网型变流器（GFM与GFL对比）
- [[vsc-model]] - 两电平/三电平换流器通用模型
- [[pv-system-model]] - 光伏并网系统聚合模型
- [[dfig-model]] - 双馈风机（本质是GFL加励磁控制）
- [[ibr]] - 跟网型资源（IBR）聚合等值模型

## 相关主题

- [[real-time-simulation]] - GFL实时HIL测试
- [[harmonic-analysis]] - 并网谐波分析
- [[harmonic-analysis]] - 次同步振荡与SSCO
- [[weak-grid-vsc]] - 弱电网稳定性分析
- [[fault-ride-through]] - 低电压穿越与故障穿越

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]] | 2023 | ATP/ATPDraw中GFL等效模型，故障电流误差2.33%，70%加速（Luchini） |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]] | 2026 | RMS+模型捕捉PLL失稳，SCR<2时Hopf分岔，临界功率降40%（Carreño） |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient]] | 2021 | 五模型精度-效率映射框架（SW/VI/AV/CCI/SCI）量化对比 |
| [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]] | 2024 | DSOGI-PLL带宽自适应，SCR稳定下限扩展至1.0（Ranasinghe） |
| [[dynamic-average-value-modeling-of-13&14|Dynamic Average-Value Modeling of VSC-HVDC]] | 2012 | DAVM，5μs步长CPU减少50-54%，≥40μs步长减少60-70% |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo]] | 2020 | 低计算负担的谐波逆变器模型 |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based]] | 2025 | 保状态变量的IBR高效建模方法 |
| [[discretized-impedance-based-modeling-of-converter-interfaced-energy-resources-fo]] | 2025 | 离散阻抗IBR建模 |