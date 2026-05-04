---
title: "负荷建模 (Load Modeling)"
type: topic
tags: [load-modeling, load, power-system, dynamic, static]
created: "2026-05-02"
---

# 负荷建模 (Load Modeling)

## 概述

负荷建模是电力系统分析的基础，用于描述电力负荷的电压特性和频率特性。准确的负荷模型对`power-flow-analysis`、[[transient-stability-analysis]]和[[small-signal-stability]]分析至关重要。负荷特性直接影响系统的电压稳定、频率稳定和小信号稳定。

电力系统负荷建模的核心目标是建立能够准确反映实际负荷动态行为的数学模型。由于实际电力系统负荷具有高度多样性和时变性，负荷建模一直是电力系统研究中的难点问题。现代电力系统中，负荷组成日益复杂，包含传统负荷（照明、加热、电动机）和新型负荷（电动汽车、数据中心、分布式能源等），这进一步增加了负荷建模的挑战。

## 静态负荷模型

### ZIP模型
静态负荷最常用的模型，将负荷功率表示为电压的二次函数：

$$P = P_0\left[a(V/V_0)^2 + b(V/V_0) + c\right]$$
$$Q = Q_0\left[\alpha(V/V_0)^2 + \beta(V/V_0) + \gamma\right]$$

其中：
- Z: 恒阻抗分量（$a, \alpha$），代表恒定阻抗负荷如照明、加热设备
- I: 恒电流分量（$b, \beta$），代表恒定电流负荷
- P: 恒功率分量（$c, \gamma$），代表恒定功率负荷如电子设备
- $a+b+c=1$, $\alpha+\beta+\gamma=1$
- $V_0$, $P_0$, $Q_0$为额定电压、额定有功功率和额定无功功率

#### ZIP模型参数辨识
ZIP模型参数可通过以下方法确定：

**1. 基于实测数据的参数辨识**
通过现场电压扰动试验获取不同电压下的功率响应数据，采用最小二乘法求解：

$$\min_{a,b,c} \sum_{i=1}^{N} \left[P_i - P_0(a(V_i/V_0)^2 + b(V_i/V_0) + c)\right]^2$$

**2. 基于负荷构成的加权法**
根据负荷组成调查统计，按各类负荷占比加权计算：
$$a = \sum_{j} w_j a_j, \quad b = \sum_{j} w_j b_j, \quad c = \sum_{j} w_j c_j$$

其中$w_j$为第$j$类负荷的功率占比。

#### 多类型负荷聚合
对于包含多种负荷类型的母线，采用分层聚合方法：

**第一层：同类负荷聚合**
对于同一类型的负荷，假设具有相似的电压特性：
$$P_{agg}^{(k)} = \sum_{i \in \Omega_k} P_i$$

**第二层：多类型负荷聚合**
考虑ZIP系数的加权聚合：
$$a_{eq} = \frac{\sum_{k} a_k P_{agg}^{(k)}}{\sum_{k} P_{agg}^{(k)}}$$

聚合后的等效ZIP模型应保持总功率守恒：
$$P_{eq}(V_0) = \sum_{k} P_{agg}^{(k)}$$

### 指数模型
$$P = P_0(V/V_0)^{n_p}$$
$$Q = Q_0(V/V_0)^{n_q}$$

- **恒阻抗**: n=2，代表电阻性加热、白炽灯照明
- **恒电流**: n=1，代表某些类型的电器负载
- **恒功率**: n=0，代表电子设备、[[modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati-27&28]] - 恒功率负荷
- **综合负荷**: n=0.5-1.5，实际测量得到的典型值

指数模型可视为ZIP模型的简化形式，当$n=0,1,2$时与ZIP模型对应。

### 频率相关模型
静态负荷的频率特性可表示为：
$$P = P_0(1 + k_{pf}\Delta f + k_{pf2}\Delta f^2)$$
$$Q = Q_0(1 + k_{qf}\Delta f + k_{qf2}\Delta f^2)$$

其中：
- $k_{pf}$, $k_{qf}$: 一阶频率调节系数
- $k_{pf2}$, $k_{qf2}$: 二阶频率调节系数
- $\Delta f = f - f_0$: 频率偏差
- 有功功率典型值: 0-3 %/Hz
- 无功功率典型值: -1 至 2 %/Hz

频率特性主要来源于：
1. 感应电动机滑差随频率变化
2. 恒阻抗负荷的电流与频率相关
3. 部分电子设备的频率敏感性

## 动态负荷模型

### 感应电动机模型

感应电动机是电力系统中最重要的动态负荷，占总负荷的40-70%。根据建模精度需求，可分为不同阶次的模型：

#### 一阶滑差模型（简化模型）
仅考虑转子运动方程：

$$\frac{d\omega_r}{dt} = \frac{1}{2H_m}(T_e - T_m)$$

其中：
- $\omega_r$: 转子转速（标幺值）
- $H_m$: 电动机惯性时间常数（秒）
- $T_e$: 电磁转矩
- $T_m$: 机械负载转矩

电磁转矩计算：
$$T_e = \frac{V^2 R_r' / s}{(R_s + R_r'/s)^2 + (X_s + X_r')^2}$$

其中$s = 1 - \omega_r$为滑差。

#### 三阶模型（详细模型）
考虑定子、转子电磁暂态和转子机械动态：

**转子运动方程**：
$$\frac{d\omega_r}{dt} = \frac{1}{2H_m}(T_e - T_m)$$

**转子磁链方程**：
$$\frac{d\psi_{qr}'}{dt} = -\frac{1}{T_r'}\psi_{qr}' + \frac{X_m}{X_r'}e_d' - (\omega_s - \omega_r)\psi_{dr}'$$
$$\frac{d\psi_{dr}'}{dt} = -\frac{1}{T_r'}\psi_{dr}' + \frac{X_m}{X_r'}e_q' + (\omega_s - \omega_r)\psi_{qr}'$$

其中：
- $\psi_{qr}'$, $\psi_{dr}'$: 转子q轴、d轴磁链（暂态）
- $T_r' = X_r'/R_r'$: 转子开路时间常数
- $X_m$: 互抗
- $X_r' = X_r + X_m$: 转子总电抗
- $\omega_s$: 同步转速

#### 五阶模型（全阶模型）
包含定子绕组暂态、转子绕组暂态和机械动态：

**定子电压方程**：
$$v_{ds} = R_s i_{ds} + \frac{d\psi_{ds}}{dt} - \omega_s \psi_{qs}$$
$$v_{qs} = R_s i_{qs} + \frac{d\psi_{qs}}{dt} + \omega_s \psi_{ds}$$

**转子电压方程**：
$$v_{dr} = R_r i_{dr} + \frac{d\psi_{dr}}{dt} - (\omega_s - \omega_r)\psi_{qr} = 0$$
$$v_{qr} = R_r i_{qr} + \frac{d\psi_{qr}}{dt} + (\omega_s - \omega_r)\psi_{dr} = 0$$

磁链方程：
$$\begin{bmatrix} \psi_{ds} \\ \psi_{qs} \\ \psi_{dr} \\ \psi_{qr} \end{bmatrix} = \begin{bmatrix} X_s & 0 & X_m & 0 \\ 0 & X_s & 0 & X_m \\ X_m & 0 & X_r & 0 \\ 0 & X_m & 0 & X_r \end{bmatrix} \begin{bmatrix} i_{ds} \\ i_{qs} \\ i_{dr} \\ i_{qr} \end{bmatrix}$$

#### 等值电动机参数计算
对于由多台电动机组成的负荷群，采用等值电动机方法：

**容量加权法**：
$$H_{eq} = \frac{\sum_{i} H_i S_i}{\sum_{i} S_i}$$
$$R_{s,eq} = \frac{\sum_{i} R_{s,i} S_i}{\sum_{i} S_i}$$

**保持暂态特性法**（更精确）：
考虑等值前后暂态电抗和开路时间常数的一致性：
$$X_{eq}' = \frac{1}{\sum_{i} S_i / X_i'}$$

### 综合负荷模型

#### WECC模型
美国西部电力协调委员会（WECC）推荐的综合负荷模型（CLM）：
$$P_{load} = P_{static} + P_{motor}$$
$$Q_{load} = Q_{static} + Q_{motor}$$

其中：
- 静态部分采用ZIP模型
- 动态部分采用三阶感应电动机模型

典型参数配置：
- 电动机占比：30-70%（按负荷类型）
- 恒阻抗占比：20-40%
- 恒电流占比：5-15%
- 恒功率占比：10-30%

#### 中国电网负荷模型
中国国家电网公司采用的综合负荷模型：

**传统负荷区域模型**：
$$P = P_{ZIP} + k_m P_{motor} + P_{electronic}$$

**现代城市负荷模型**（考虑电子设备）：
增加电子设备负荷分量，采用恒功率或电流受限模型：
$$P_{electronic} = \min(P_{rated}, V \cdot I_{max})$$

### 电动机负荷特性
- **低电压特性**: 电压下降时，电动机吸收电流增大，导致无功需求增加
- **失速特性**: 电压过低时（通常<0.7 pu），电动机失去同步，滑差剧增
- **再启动特性**: 电压恢复后，成组电动机的自启动电流可达额定电流的5-7倍
- `induction-motor` - 感应电动机详细模型
- `single-phase-induction-machine` - 单相感应电机模型

## 负荷模型的电压特性和频率特性

### 电压特性分析

#### 静态电压特性
负荷功率随电压变化的敏感度：
$$\frac{dP/P_0}{dV/V_0} = 2a(V/V_0) + b$$

在额定电压点（V=V_0）：
$$\left.\frac{dP/P_0}{dV/V_0}\right|_{V_0} = 2a + b$$

典型负荷的电压敏感度：
| 负荷类型 | dP/dV | dQ/dV |
|----------|-------|-------|
| 电阻加热 | 2.0 | 0 |
| 白炽灯 | 1.6 | 0 |
| 感应电动机 | 0.1-0.8 | 2.0-4.0 |
| 电子设备 | 0 | 0 |
| 综合负荷 | 0.5-1.2 | 1.0-2.5 |

#### 动态电压特性
考虑电动机暂态过程：
$$P(t) = \frac{V^2(t) R_r'/s(t)}{(R_s + R_r'/s(t))^2 + X'^2}$$

关键动态过程：
1. **电压跌落**: 电磁转矩瞬时下降，机械转矩大于电磁转矩，转速下降
2. **电流峰值**: 电压恢复瞬间，大滑差导致大电流冲击
3. **恢复过程**: 电动机逐渐加速回到正常运行点

### 频率特性分析

#### 负荷频率响应
系统频率变化时，负荷功率的自动调节作用：
$$\Delta P_L = D_L \Delta f$$

其中$D_L$为负荷阻尼系数（MW/Hz或%/Hz）。

典型负荷频率特性：
| 负荷类型 | 频率系数(%/Hz) | 物理原因 |
|----------|----------------|----------|
| 感应电动机 | 0.5-2.0 | 滑差变化 |
| 电阻负荷 | 0 | 功率与频率无关 |
| 压缩机 | 2.0-3.0 | 转矩与转速平方成正比 |
| 照明 | 0 | 功率与频率无关 |

#### 频率相关负荷模型
综合模型：
$$P = P_0(V/V_0)^{n_p}(1 + k_{pf}\Delta f)$$
$$Q = Q_0(V/V_0)^{n_q}(1 + k_{qf}\Delta f)$$

## 负荷模型对稳定性的影响分析

### 电压稳定影响

#### 恒功率负荷的不稳定效应
恒功率负荷（$n=0$）是电压失稳的主要驱动力：

**静态分析**：
在P-V曲线分析中，恒功率负荷对应于：
$$P = \text{const} \Rightarrow I = P/V$$

当电压下降时，电流增加，导致线路压降进一步增大，形成正反馈：
$$V \downarrow \Rightarrow I \uparrow \Rightarrow \Delta V_{line} \uparrow \Rightarrow V \downarrow$$

**临界条件**：
$$\frac{\partial P_{load}}{\partial V} > \frac{\partial P_{supply}}{\partial V}$$

`voltage-stability` - 电压稳定详细分析
`voltage-collapse` - 电压崩溃机理

#### 电动机负荷的失稳效应
电动机负荷失速导致的电压失稳：

**失速判据**：
当端电压低于临界电压时，电磁转矩小于机械转矩：
$$T_e(V_{critical}, s_{nominal}) = T_m$$

**成组失速**：
多个电动机同时失速时，恢复电流叠加，可能导致电压无法恢复。

### 频率稳定影响

#### 负荷阻尼效应
`frequency-response` - 频率响应分析
`load-damping` - 负荷阻尼特性

频率相关负荷提供天然的频率调节：
$$\Delta P_L = D_L \Delta f$$

系统频率动态方程：
$$2H_{sys}\frac{d\Delta f}{dt} = \Delta P_m - \Delta P_L = \Delta P_m - D_L \Delta f$$

负荷阻尼的作用：
1. **减少频率偏差**：$\Delta f_{ss} = \frac{\Delta P_m}{D_L + 1/R}$（R为调速器调差系数）
2. **增加稳定性**：阻尼系数增大，振荡衰减加快
3. **减少UFLS动作**：较小的频率偏差可能避免低频减载

#### 低频减载协调
`under-frequency-load-shedding` - 低频减载系统

UFLS整定需考虑负荷频率特性：
- 负荷阻尼大时，UFLS动作频率可适当降低
- 恒功率负荷比例高时，需增加UFLS轮次

### 小信号稳定影响

负荷模型影响系统振荡模式：
- **恒阻抗负荷**：增加系统等效阻尼
- **恒功率负荷**：可能引入负阻尼
- **感应电动机**：增加机电振荡模式的复杂性

## 负荷预测方法

### 短期负荷预测（1小时-1周）

#### 时序分析方法
`time-series-analysis` - 时序分析技术

**ARIMA模型**：
$$\phi(B)(1-B)^d y_t = \theta(B)\epsilon_t$$

其中：
- $\phi(B)$: 自回归多项式
- $\theta(B)$: 移动平均多项式
- $(1-B)^d$: 差分算子
- $\epsilon_t$: 白噪声

**季节性分解**：
$$Y_t = T_t + S_t + C_t + \epsilon_t$$
- $T_t$: 趋势分量
- $S_t$: 季节分量
- $C_t$: 循环分量
- $\epsilon_t$: 随机分量

#### 机器学习方法
`neural-network` - 神经网络预测

**多层感知机（MLP）**：
$$\hat{L}_{t+h} = f(W_3 \cdot g(W_2 \cdot g(W_1 \cdot X + b_1) + b_2) + b_3)$$

输入特征：
- 历史负荷：$L_{t-1}, L_{t-2}, ..., L_{t-n}$
- 气象因素：温度、湿度
- 时间特征：小时、星期、节假日

**LSTM网络**：
$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
$$\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$$
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$

### 中期负荷预测（1月-1年）

**经济增长关联法**：
$$L_t = L_0(1 + \alpha \cdot g_{GDP})^t$$

其中：
- $\alpha$: 电力弹性系数
- $g_{GDP}$: GDP增长率

典型电力弹性系数：
- 工业化初期：1.2-1.5
- 工业化中期：0.8-1.0
- 后工业化：0.5-0.8

### 长期负荷预测（1-20年）

**部门分析法**：
$$L_{total} = \sum_{sector} L_{sector} = \sum_{sector} (N_{sector} \cdot S_{sector} \cdot LF_{sector})$$

其中：
- $N$: 用户数
- $S$: 单户容量
- $LF$: 负荷率

`load-forecasting` - 负荷预测综合方法

## 需求响应建模

### 价格型需求响应
`demand-response` - 需求响应系统

**价格弹性模型**：
$$\frac{\Delta L}{L_0} = \varepsilon_p \frac{\Delta \pi}{\pi_0}$$

其中$\varepsilon_p$为价格弹性系数（通常为负值）。

**分时电价响应**：
$$L_t^{DR} = L_t^{base} \cdot \left(1 + \sum_{k} \varepsilon_{tk} \frac{\pi_k - \pi_k^{base}}{\pi_k^{base}}\right)$$

### 激励型需求响应

**直接负荷控制（DLC）模型**：
$$L_t^{DLC} = L_t^{base} - \sum_{i \in \Omega_{on}} u_{i,t} \cdot L_i$$

其中$u_{i,t} \in \{0,1\}$为控制信号。

**可中断负荷**：
$$L_t^{IL} = L_t^{base} \cdot (1 - \alpha_t \cdot I_t)$$

$\alpha_t$为中断比例，$I_t$为中断指示变量。

## 特殊负荷建模

### 电弧炉负荷
[[a-time-domain-ac-electric-arc-furnace-model-for-flicker-planning-studies]] - 电弧炉详细模型

电弧炉是典型的冲击性、非线性负荷：

**时变电阻模型**：
$$R_{arc}(t) = R_{base} + \Delta R(t) + R_{flicker}(t)$$

其中：
- $R_{base}$: 基础电弧电阻
- $\Delta R(t)$: 炉料熔化过程变化
- $R_{flicker}(t)$: 电压闪变分量

**闪变发射特性**：
$$P_{st} = k \cdot \frac{S_{EAF}}{S_{sc}}$$

$P_{st}$为短期闪变严重度，$S_{sc}$为短路容量。

### 电气化铁路负荷
`electric-railway` - 电气化铁路系统

**牵引负荷模型**：
$$P_{train}(t) = \sum_{i} P_{loco,i}(v_i(t), a_i(t), G_i(t))$$

其中：
- $v_i$: 第i列车的速度
- $a_i$: 加速度
- $G_i$: 线路坡度

**移动负荷特性**：
负荷随列车位置移动而变化，需考虑：
- 列车运行图
- 线路阻抗
- 多车牵引的重载时刻

### HVDC换流站负荷
`hvdc-converter-load` - HVDC换流器负荷模型

**直流功率模型**：
$$P_{dc} = V_d \cdot I_d$$
$$Q_{ac} = P_{dc} \cdot \tan\phi(V_d, \alpha, \mu)$$

其中：
- $\alpha$: 触发角
- $\mu$: 换相重叠角
- $\tan\phi$: 功率因数角正切

直流功率-电压特性：
$$P_{dc} = \begin{cases} P_{ordered} & V_{ac} > V_{min} \\ P_{max}(V_{ac}) & V_{ac} \leq V_{min} \end{cases}$$

## 负荷模型的参数辨识方法

### 统计综合法
- **用户分类**: 按类型统计（居民、商业、工业）
- **典型曲线**: 各类负荷的典型日负荷曲线
- **加权求和**: 根据各类负荷占比综合

综合公式：
$$\theta_{eq} = \sum_{j=1}^{M} w_j \theta_j, \quad \sum_{j=1}^{M} w_j = 1$$

### 总体测辨法
`system-identification` - 系统辨识方法
[[least-squares-method]] - 最小二乘法

**现场测试方法**：
1. **电压扰动试验**：通过变压器分接头或电容器投切产生电压阶跃
2. **伪随机信号注入**：注入PRBS信号分析频响特性

**参数估计方法**：

**最小二乘法**：
$$\min_{\theta} J = \sum_{k=1}^{N} [y_k - \hat{y}_k(\theta)]^2$$

**极大似然法**：
$$\max_{\theta} L = \prod_{k=1}^{N} p(y_k|\theta)$$

**递推最小二乘（在线辨识）**：
$$\hat{\theta}_k = \hat{\theta}_{k-1} + K_k(y_k - \phi_k^T\hat{\theta}_{k-1})$$
$$K_k = P_{k-1}\phi_k(\lambda + \phi_k^T P_{k-1}\phi_k)^{-1}$$
$$P_k = \frac{1}{\lambda}(P_{k-1} - K_k\phi_k^T P_{k-1})$$

其中$\lambda$为遗忘因子（通常0.95-0.99）。

### 混合法
`load-aggregation` - 负荷聚合技术

**聚合-辨识结合**：
1. 先按负荷类型分类聚合
2. 对各类型进行独立辨识
3. 按容量加权得到等值参数

## EMT仿真中的负荷表示

### 静态负荷的EMT表示

#### 恒阻抗负荷
`time-varying-load` - 时变负荷模型

在EMT仿真中，恒阻抗负荷直接作为RLC元件：
$$R = \frac{V_0^2}{P_0}, \quad L = \frac{V_0^2}{2\pi f_0 Q_0}$$

导纳形式：
$$Y_{load} = G + jB = \frac{P_0 - jQ_0}{V_0^2}$$

#### 恒功率负荷
恒功率负荷在EMT中采用时变导纳或电流源表示：

**导纳法**：
$$Y_{eq}(t) = \frac{P_0 - jQ_0}{|V(t)|^2}$$

**电流源法**：
$$\dot{I}(t) = \left(\frac{P_0 + jQ_0}{\dot{V}(t)}\right)^*$$

#### 动态负荷
`dynamic-load-model` - 动态负荷模型

详细电动机模型直接接入EMT：
- 定子电压方程与网络联立求解
- 转子状态方程用数值积分求解

### EMT仿真中的负荷初始化

EMT仿真需要准确的初始条件：
$$\psi_{r0} = \frac{X_m}{X_r'}E_0, \quad \omega_{r0} = 1 - s_0$$

其中$s_0$为初始滑差，$E_0$为初始内电势。

### 负荷模型的频率响应表示
在EMT中，频率相关负荷可采用：
1. 锁相环测量频率，实时调整负荷功率
2. 频率作为状态变量，直接参与网络求解

## 负荷模型验证方法

### 现场数据验证

**测量指标**：
1. **功率误差**：
$$e_P = \frac{1}{N}\sum_{k=1}^{N} \left|\frac{P_{model,k} - P_{meas,k}}{P_{base}}\right| \times 100\%$$

2. **动态响应误差**：
$$RMSE = \sqrt{\frac{1}{N}\sum_{k=1}^{N} (y_{model,k} - y_{meas,k})^2}$$

3. **相关系数**：
$$R = \frac{\sum(y_{model} - \bar{y}_{model})(y_{meas} - \bar{y}_{meas})}{\sqrt{\sum(y_{model} - \bar{y}_{model})^2\sum(y_{meas} - \bar{y}_{meas})^2}}$$

### 仿真对比验证

**不同仿真软件对比**：
- [[pscad-emtdc]] - PSCAD/EMTDC仿真
- [[atp-emtp]] - ATP-EMTP仿真
- [[pscad-emtdc]] - PSCAD仿真结果

**对比指标**：
- 电压跌落深度
- 恢复时间
- 峰值电流
- 稳定运行点

### 模型适用性评估

**静态验证**：
- P-V曲线拟合精度
- Q-V曲线拟合精度

**动态验证**：
- 阶跃响应对比
- 故障恢复过程对比

**稳定性验证**：
- 临界电压计算误差
- 稳定裕度评估精度

## 负荷组成参考数据

| 负荷类型 | 占比 | 特性描述 |
|----------|------|----------|
| 恒阻抗 | 30-50% | 照明、加热、电阻炉 |
| 恒电流 | 10-20% | 某些类型电器、荧光灯 |
| 恒功率 | 20-40% | 电子设备、变频调速 |
| 感应电动机 | 40-70% | 工业电动机、空调、冰箱 |
| 同步电动机 | 5-15% | 大型工业驱动 |

典型综合负荷参数（WECC标准）：
- 电动机占比：50%
- 恒阻抗占比：30%
- 恒电流占比：10%
- 恒功率占比：10%

## 相关主题
- `power-system-load` - 电力系统负荷概述
- [[unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids]] - 负荷潮流计算
- `power-system-stability` - 电力系统稳定性
- `motor-load` - 电动机负荷特性
- `static-load-model` - 静态负荷模型
- `composite-load-model` - 综合负荷模型

## 来源论文

参见 [[index.md]] 获取更多负荷建模相关文献。

---

*本文档基于IEEE和CIGRE负荷建模标准，结合国内外电网实测数据编写。*
