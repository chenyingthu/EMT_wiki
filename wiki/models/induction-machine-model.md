---
title: "感应电机 (Induction Machine)"
type: model
tags: [induction-machine, asynchronous-machine, motor, load, dq0, slip]
created: "2026-04-29"
---

# 感应电机 (Induction Machine)

## 定义与概述

感应电机（异步电机）是电力系统中应用最广泛的旋转电机类型，通过定子绕组产生的旋转磁场与转子感应电流相互作用产生电磁转矩。作为电力系统的主要负荷和工业驱动设备，感应电机在EMT仿真中需要精确建模以准确分析启动暂态、电压跌落响应和系统稳定性。本模型涵盖相域模型、dq0坐标变换模型、 deep bar效应建模，适用于机电暂态和电磁暂态仿真。

## 1. 物理对象概述

### 1.1 功能与分类

感应电机（异步电机）是电力系统中**最广泛应用的旋转电机**，占总发电容量60%以上：

**按转子结构分类**：
| 类型 | 结构 | 特点 | 应用 |
|------|------|------|------|
| **鼠笼式** | 铸铝/铜条转子 | 结构简单、坚固、成本低 | 通用电动机、风机、泵 |
| **绕线式** | 三相绕组转子 | 可调速、高启动转矩 | 起重机、卷扬机、大型风机 |

**按功率等级**：
- 小型：< 1 kW（家用电器）
- 中型：1 kW - 100 kW（工业驱动）
- 大型：100 kW - 10 MW（泵、压缩机）
- 特大型：> 10 MW（球磨机、矿井提升）

### 1.2 工作原理

**基本电磁原理**：
- 定子三相绕组产生旋转磁场（同步转速 $n_s = 60f/p$）
- 旋转磁场切割转子导条，感应转子电流
- 转子电流与气隙磁场相互作用产生转矩
- 转子转速 $n_r$ 始终低于同步转速（异步运行）

**转差率定义**：
$$s = \frac{n_s - n_r}{n_s} = \frac{\omega_s - \omega_r}{\omega_s}$$

典型运行范围：$s = 0.005 \sim 0.05$（额定负载）

### 1.3 运行激励

**电压激励**：
- 额定电压：380V / 6kV / 10kV（三相）
- 频率：50Hz / 60Hz
- 电压不平衡度：< 2%（正常运行）

**机械激励**：
- 负载转矩：恒转矩、平方转矩、恒功率
- 惯量：机械时间常数 $T_m = J\omega^2/P_{rated}$ 通常为0.5-5s

**暂态激励**：
- 直接启动：启动电流5-7倍额定
- 电压暂降：电机失速、接触器脱扣
- 短路故障：电磁转矩脉动、轴系扭振

## 2. 物理模型与数学描述

### 2.1 相域电压方程

三相定子/转子绕组电压方程：

**定子侧**：
$$
\mathbf{v}_{abc,s} = R_s \mathbf{i}_{abc,s} + \frac{d}{dt} \mathbf{\lambda}_{abc,s}
$$

**转子侧**（以电角度表示）：
$$
\mathbf{v}_{abc,r} = R_r \mathbf{i}_{abc,r} + \frac{d}{dt} \mathbf{\lambda}_{abc,r}
$$

**磁链方程**：
$$
\begin{bmatrix} \mathbf{\lambda}_{abc,s} \\ \mathbf{\lambda}_{abc,r} \end{bmatrix} =
\begin{bmatrix} \mathbf{L}_{ss} & \mathbf{L}_{sr}(\theta) \\ \mathbf{L}_{rs}(\theta) & \mathbf{L}_{rr} \end{bmatrix}
\begin{bmatrix} \mathbf{i}_{abc,s} \\ \mathbf{i}_{abc,r} \end{bmatrix}
$$

**电感矩阵**（考虑时变互感）：
$$L_{sr,ij}(\theta) = M_{sr} \cos\left(\theta - \frac{2\pi}{3}(i-j)\right)$$

其中$\theta$为转子位置角。

### 2.2 dq0坐标变换模型

#### 2.2.1 Park变换

将三相变量变换到旋转dq0坐标系：

**变换矩阵**：
$$
\mathbf{T}_{dq0} = \frac{2}{3} \begin{bmatrix}
\cos\theta & \cos(\theta - \frac{2\pi}{3}) & \cos(\theta + \frac{2\pi}{3}) \\
-\sin\theta & -\sin(\theta - \frac{2\pi}{3}) & -\sin(\theta + \frac{2\pi}{3}) \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}$$

#### 2.2.2 dq轴电压方程

**定子电压方程**（以同步速旋转）：
$$
v_{ds} = R_s i_{ds} + \frac{d\lambda_{ds}}{dt} - \omega_s \lambda_{qs}
$$
$$
v_{qs} = R_s i_{qs} + \frac{d\lambda_{qs}}{dt} + \omega_s \lambda_{ds}
$$

**转子电压方程**（以转子速旋转）：
$$
v_{dr} = R_r i_{dr} + \frac{d\lambda_{dr}}{dt} - (\omega_s - \omega_r) \lambda_{qr} = 0 \quad \text{(鼠笼式)}
$$
$$
v_{qr} = R_r i_{qr} + \frac{d\lambda_{qr}}{dt} + (\omega_s - \omega_r) \lambda_{dr} = 0
$$

#### 2.2.3 磁链方程

$$\lambda_{ds} = L_{ls} i_{ds} + L_m (i_{ds} + i_{dr})$$
$$\lambda_{qs} = L_{ls} i_{qs} + L_m (i_{qs} + i_{qr})$$
$$\lambda_{dr} = L_{lr} i_{dr} + L_m (i_{ds} + i_{dr})$$
$$\lambda_{qr} = L_{lr} i_{qr} + L_m (i_{qs} + i_{qr})$$

**等效电路电感**：
- $L_s = L_{ls} + L_m$：定子等效自感
- $L_r = L_{lr} + L_m$：转子等效自感
- $L_m$：互感（励磁电感）

### 2.3 状态空间形式

#### 2.3.1 状态变量选择

选择定子电流和转子磁链作为状态变量：
$$\mathbf{x} = [i_{ds}, i_{qs}, \lambda_{dr}, \lambda_{qr}, \omega_r]^T$$

#### 2.3.2 状态方程

$$\frac{d}{dt} \begin{bmatrix} i_{ds} \\ i_{qs} \\ \lambda_{dr} \\ \lambda_{qr} \\ \omega_r \end{bmatrix} =
\mathbf{A}(\omega_r) \begin{bmatrix} i_{ds} \\ i_{qs} \\ \lambda_{dr} \\ \lambda_{qr} \\ \omega_r \end{bmatrix} +
\mathbf{B} \begin{bmatrix} v_{ds} \\ v_{qs} \\ T_m \end{bmatrix}$$

**系数矩阵**（以定子磁链-转子电流形式）：

$$\sigma = 1 - \frac{L_m^2}{L_s L_r}$$（漏磁系数）

$$\tau_s' = \frac{L_s}{R_s}, \quad \tau_r' = \frac{L_r}{R_r}$$（瞬态时间常数）

$$\frac{di_{ds}}{dt} = -\frac{1}{\tau_{sd}} i_{ds} + \omega_s i_{qs} + \frac{k_r}{\tau_{sd} L_s} \lambda_{dr} + \frac{k_r \omega_r}{L_s} \lambda_{qr} + \frac{v_{ds}}{\sigma L_s}$$

### 2.4 机械运动方程

**电磁转矩**：

基于磁链和电流：
$$T_e = \frac{3}{2} \frac{p}{2} (\lambda_{ds} i_{qs} - \lambda_{qs} i_{ds}) = \frac{3}{2} \frac{p}{2} \frac{L_m}{L_r} (\lambda_{dr} i_{qs} - \lambda_{qr} i_{ds})$$

基于电流：
$$T_e = \frac{3}{2} \frac{p}{2} L_m (i_{qs} i_{dr} - i_{ds} i_{qr})$$

**转子运动方程**：
$$J \frac{d\omega_m}{dt} = T_e - T_L - D \omega_m$$

$$\frac{d\theta}{dt} = \omega_m$$

其中：
- $J$：转动惯量 (kg·m²)
- $D$：阻尼系数
- $T_L$：负载转矩

**标幺化形式**：
$$2H \frac{d\omega_r}{dt} = T_e - T_L - D \omega_r$$

$H$为惯性时间常数（秒）。

### 2.5 稳态等效电路

#### 2.5.1 单相等效电路

额定频率下的稳态等效电路（每相）：

```
Vs ─R1─ Lls─┬─Lm─┬─ Llr ─R2/s─ 滑差阻抗
            │    │
           ─┴────┴─
```

**阻抗表达式**：
$$Z_{eq} = R_s + jX_{ls} + \frac{jX_m (R_r/s + jX_{lr})}{R_r/s + j(X_m + X_{lr})}$$

#### 2.5.2 转矩-转速特性

**电磁转矩表达式**：
$$T_e = \frac{3 V_s^2 R_r/s}{\omega_s \left[(R_s + R_r/s)^2 + (X_{ls} + X_{lr})^2\right]}$$

**最大转矩**：
$$T_{max} = \frac{3 V_s^2}{2\omega_s (R_s + \sqrt{R_s^2 + (X_{ls} + X_{lr})^2})}$$

**临界转差率**：
$$s_{max} = \frac{R_r}{\sqrt{R_s^2 + (X_{ls} + X_{lr})^2}} \approx \frac{R_r}{X_{eq}}$$

## 3. EMT仿真模型

### 3.1 详细相域模型

#### 3.1.1 时变电感模型

直接使用相域时变电感矩阵：
$$\mathbf{v} = \mathbf{R} \mathbf{i} + \frac{d}{dt}(\mathbf{L}(\theta) \mathbf{i})$$

**实现难点**：
- 时变电感导致变拓扑（每步需重算导纳矩阵）
- 计算效率低
- 适用于详细分析，不适合大规模系统

#### 3.1.2 相坐标饱和模型

考虑铁芯饱和的非线性电感：
$$L_m = f(i_m), \quad i_m = \sqrt{i_{ds}^2 + i_{qs}^2}$$

### 3.2 dq0坐标模型（主流）

#### 3.2.1 电压源型模型

**定子侧**：
$$
v_{ds} = R_s i_{ds} + L_s' \frac{di_{ds}}{dt} - \omega_s L_s' i_{qs} + e_d'
$$
$$
v_{qs} = R_s i_{qs} + L_s' \frac{di_{qs}}{dt} + \omega_s L_s' i_{ds} + e_q'
$$

**暂态电动势**：
$$
e_d' = \frac{L_m}{L_r} \lambda_{qr}, \quad e_q' = -\frac{L_m}{L_r} \lambda_{dr}
$$

**转子磁链动态**：
$$\frac{de_d'}{dt} = -\frac{1}{\tau_r'} e_d' + (\omega_s - \omega_r) e_q' - \frac{L_m^2}{\tau_r' L_r} i_{qs}$$

#### 3.2.2 电流源型模型

适用于恒导纳求解器：

$$\begin{bmatrix} i_{ds} \\ i_{qs} \end{bmatrix} =
\mathbf{Y}_{eq} \begin{bmatrix} v_{ds} \\ v_{qs} \end{bmatrix} +
\mathbf{i}_{hist}$$

**等效导纳**：
$$Y_{eq} = \frac{\Delta t}{2\sigma L_s}$$

#### 3.2.3 三阶机电暂态模型

保留转子磁链和转速动态，忽略定子电磁暂态：

$$0 = v_{ds} - R_s i_{ds} + X' i_{qs} + e_d'$$
$$0 = v_{qs} - R_s i_{qs} - X' i_{ds} + e_q'$$

$$T_d' \frac{de_d'}{dt} = -e_d' - (X - X') i_{qs} - s T_d' e_q'$$
$$T_d' \frac{de_q'}{dt} = -e_q' + (X - X') i_{ds} + s T_d' e_d'$$

$$2H \frac{ds}{dt} = T_m - T_e$$

**简化条件**：$T_e << T_{mech}$，适用于机电暂态仿真（步长10ms）

### 3.3 深槽/双笼模型

#### 3.3.1 深槽效应

高频（启动时）转子导条集肤效应导致等效电阻增加：

$$R_r(s) = R_{r0} \cdot k_{skin}(s), \quad k_{skin} = f(s \cdot f_{slip})$$

**简化实现**：
使用双笼等效：
- 上笼（启动笼）：电阻大、漏抗小
- 下笼（运行笼）：电阻小、漏抗大

#### 3.3.2 双笼模型方程

$$\begin{bmatrix} v_{ds} \\ v_{qs} \\ 0 \\ 0 \end{bmatrix} =
\begin{bmatrix}
R_s + L_s p & -\omega_s L_s & L_m p & -\omega_s L_m \\
\omega_s L_s & R_s + L_s p & \omega_s L_m & L_m p \\
L_m p & -(\omega_s-\omega_r)L_m & R_{r1}+L_{r1}p & -(\omega_s-\omega_r)L_{r1} \\
(\omega_s-\omega_r)L_m & L_m p & (\omega_s-\omega_r)L_{r1} & R_{r1}+L_{r1}p
\end{bmatrix}
\begin{bmatrix} i_{ds} \\ i_{qs} \\ i_{dr1} \\ i_{qr1} \end{bmatrix}$$

### 3.4 饱和与铁损模型

#### 3.4.1 磁化曲线模型

**经验公式**：
$$i_m = a \lambda_m + b \lambda_m^n$$

或分段线性：
$$L_m = \begin{cases}
L_{m0}, & |\lambda_m| < \lambda_{knee} \\
L_{m0} \cdot \frac{\lambda_{knee}}{|\lambda_m|}, & |\lambda_m| \geq \lambda_{knee}
\end{cases}$$

#### 3.4.2 铁损等效电阻

在等效电路中并联铁损电阻：
$$R_{fe} = \frac{V_s^2}{P_{core}}$$

铁损功率：
$$P_{core} = P_{hysteresis} + P_{eddy} = k_h f B_m^2 + k_e f^2 B_m^2$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**Universal Machine模型**：
```
UNIVERSAL_MACHINE
- Type: Induction Machine
- Rating: 10 MVA, 6.6 kV, 50 Hz
- Stator: Rs=0.01pu, Xls=0.15pu
- Rotor: Rr=0.01pu, Xlr=0.15pu
- Magnetizing: Xm=3.5pu
- Inertia: H=1.0s
```

**负载转矩设定**：
```fortran
! 平方转矩负载（风机、泵）
T_load = T_rated * (speed / speed_rated)**2

! 恒转矩负载（传送带）
T_load = T_rated

! 恒功率负载（卷取机）
T_load = P_rated / speed
```

### 4.2 MATLAB/Simulink实现

**Simulink模型**：
```matlab
% 感应电机参数
params.Rs = 0.014;      % 定子电阻
params.Rr = 0.009;      % 转子电阻
params.Lls = 0.065;     % 定子漏感
params.Llr = 0.065;     % 转子漏感
params.Lm = 2.31;       % 互感
params.J = 10.8;        % 转动惯量

% 创建Simscape模型
motor = ee_lib/Asynchronous Machine SI Units;
set_param(motor, 'Rs', num2str(params.Rs));
set_param(motor, 'Lls', num2str(params.Lls));
```

**自定义dq0实现**：
```matlab
function dxdt = induction_machine(t, x, v_dq, T_load, params)
    % 状态变量解包
    ids = x(1); iqs = x(2);
    idr = x(3); iqr = x(4);
    omega = x(5);
    
    % 参数
    Rs = params.Rs; Rr = params.Rr;
    Ls = params.Lls + params.Lm;
    Lr = params.Llr + params.Lm;
    Lm = params.Lm;
    p = params.poles;
    J = params.J;
    
    % 磁链
    lambda_ds = Ls*ids + Lm*idr;
    lambda_qs = Ls*iqs + Lm*iqr;
    lambda_dr = Lr*idr + Lm*ids;
    lambda_qr = Lr*iqr + Lm*iqs;
    
    % 电压方程
    vds = v_dq(1); vqs = v_dq(2);
    dids = (vds - Rs*ids + omega*lambda_qs - Lm*Rr/Lr*idr + omega*Lm/Lr*lambda_qr) / (Ls - Lm^2/Lr);
    diqs = (vqs - Rs*iqs - omega*lambda_ds - Lm*Rr/Lr*iqr - omega*Lm/Lr*lambda_dr) / (Ls - Lm^2/Lr);
    
    % 转子方程（短路）
    didr = (-Rr*idr + (omega-omega_r)*lambda_qr - Lm*dids) / Lr;
    diqr = (-Rr*iqr - (omega-omega_r)*lambda_dr - Lm*diqs) / Lr;
    
    % 电磁转矩
    Te = (3/2)*(p/2)*Lm*(iqs*idr - ids*iqr);
    
    % 机械方程
    domega = (Te - T_load - params.D*omega) / (J*(2/p));
    
    dxdt = [dids; diqs; didr; diqr; domega];
end
```

### 4.3 EMTP/ATP实现

**Type-59模型**：
```
INDUCTION_MACHINE
- Model: 3-phase, squirrel cage
- Rated power: 1000 HP
- Rated voltage: 4160 V
- Frequency: 60 Hz
- Stator resistance: 0.029 pu
- Rotor resistance: 0.022 pu
- Stator leakage: 0.099 pu
- Rotor leakage: 0.099 pu
- Magnetizing reactance: 3.2 pu
- Inertia: 1.5 s
```

### 4.4 实时仿真实现

**步长选择**：
- 详细模型（考虑PWM）：10-20 μs
- 平均值模型（VSC供电）：50-100 μs
- 系统级仿真：100-500 μs

**硬件配置**：
- 大规模电机群：恒导纳等效
- 单电机详细分析：详细dq0模型

## 5. 典型参数参考

### 5.1 典型感应电机参数（标幺值）

| 参数 | 小型电机(<10kW) | 中型电机(100kW) | 大型电机(>1MW) | 说明 |
|------|----------------|----------------|---------------|------|
| Rs | 0.03-0.05 | 0.01-0.03 | 0.005-0.01 | 定子电阻 |
| Rr | 0.02-0.04 | 0.01-0.02 | 0.005-0.01 | 转子电阻 |
| Xls | 0.10-0.15 | 0.12-0.18 | 0.15-0.25 | 定子漏抗 |
| Xlr | 0.10-0.15 | 0.12-0.18 | 0.15-0.25 | 转子漏抗 |
| Xm | 2.0-3.0 | 2.5-4.0 | 3.0-5.0 | 互抗 |
| H | 0.2-0.5 s | 0.5-1.5 s | 1.0-3.0 s | 惯性常数 |

### 5.2 有名值参数示例（100kW, 400V）

| 参数 | 数值 | 单位 |
|------|------|------|
| 额定功率 | 100 | kW |
| 额定电压 | 400 | V (线) |
| 额定电流 | 180 | A |
| 额定转速 | 1470 | rpm (4极) |
| 同步转速 | 1500 | rpm |
| 额定转差率 | 0.02 | - |
| 定子电阻 Rs | 0.03 | Ω |
| 转子电阻 Rr | 0.02 | Ω |
| 定子漏感 Lls | 0.4 | mH |
| 转子漏感 Llr | 0.4 | mH |
| 互感 Lm | 15 | mH |

### 5.3 启动特性

| 参数 | 直接启动 | 软启动 | 变频启动 |
|------|---------|--------|---------|
| 启动电流 | 5-7 I_n | 2-4 I_n | 0.5-1 I_n |
| 启动转矩 | 1.5-2.5 T_n | 0.5-1.5 T_n | 可调 |
| 启动时间 | 1-5 s | 5-30 s | 可调 |

### 5.4 模型选择指南

| 应用场景 | 推荐模型 | 步长 | 说明 |
|---------|---------|------|------|
| 直接启动分析 | 详细dq0模型 | 50-100 μs | 捕捉启动电流冲击 |
| 电压暂降研究 | 三阶机电暂态 | 1-10 ms | 慢速动态 |
| 负荷流计算 | 稳态等效电路 | - | 潮流分析 |
| 轴系扭振 | 详细模型+机械系统 | 10-100 μs | 机电耦合 |
| 大规模系统 | 恒功率/恒阻抗等效 | 100-500 μs | 负荷聚合 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[synchronous-machine-model|同步电机模型]] - 同步发电机/电动机
- [[dfig-model|DFIG模型]] - 双馈感应发电机（风机）
- [[pmsm-model|PMSM模型]] - 永磁同步电机
- [[load-model|负荷模型]] - 综合负荷建模

### 6.2 相关方法
- dq0变换 - 旋转坐标变换
- 矢量控制 - 感应电机矢量控制
- 变频驱动(VFD) - 变频调速技术

### 6.3 相关主题
- 电机启动 - 启动方式与冲击
- 电压暂降 - 电压跌落对电机影响
- 负荷建模 - 电力系统负荷模型

### 5.4 适用边界与限制

#### 5.4.1 适用条件
- **电压范围**：0.7-1.2 p.u.（电压过低可能失速）
- **频率范围**：45-55Hz（大范围需特殊模型）
- **转差率**：0-0.1（正常运行），启动时可达1.0
- **负荷类型**：恒转矩、平方转矩、恒功率

#### 5.4.2 模型限制
- **饱和效应**：磁路饱和简化处理
- **集肤效应**：深槽效应模型简化
- **机械系统**：单质块模型，复杂轴系需扩展
- **温度影响**：参数温升修正简化

#### 5.4.3 精度边界
| 模型类型 | 稳态电流 | 启动转矩 | 暂态响应 | 适用场景 |
|---------|---------|---------|---------|---------|
| 详细dq0 | ±1% | ±3% | 精确 | 设备级 |
| 简化三阶 | ±3% | ±5% | ±5% | 系统级 |
| 稳态等效 | ±5% | - | - | 潮流计算 |

## 6. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Improved induction machine model for real-time simulations | 2010 | 改进的实时仿真感应电机模型 |
| A detailed squirrel cage induction machine model for EMT | 2015 | 鼠笼式感应机详细EMT模型 |
| Modeling and simulation of induction motor during starting | 2018 | 感应电机启动过程建模 |

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
