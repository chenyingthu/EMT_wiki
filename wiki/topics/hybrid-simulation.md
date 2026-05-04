---
title: "混合仿真 (Hybrid Simulation)"
type: topic
tags: [hybrid-simulation, emt-ts, co-simulation, multi-time-scale, interface]
created: "2026-05-02"
---

# 混合仿真 (Hybrid Simulation)

## 概述

混合仿真是指将电磁暂态(EMT)仿真和机电暂态(TS)仿真结合起来，利用两种方法的优势进行电力系统分析。EMT提供详细的电磁过程建模，TS提供大规模的机电动态分析，混合仿真能够兼顾精度和效率。

混合仿真的核心思想是将电力系统划分为两个区域：需要详细电磁暂态分析的区域采用EMT仿真，而其余大规模系统采用TS仿真。通过合理的[[interface-technique]]实现两个仿真环境之间的数据交换和协调求解。

## 理论基础

### 多时间尺度分析

电力系统中存在显著不同的时间尺度现象，这是混合仿真的物理基础：

#### 电磁暂态时间尺度
电磁暂态过程由网络元件的电磁特性决定，典型时间常数包括：
- **RL电路时间常数**：$\tau_{RL} = L/R$
- **RC电路时间常数**：$\tau_{RC} = RC$
- **行波传播时间**：$\tau_{wave} = l/v$，其中$v \approx 3 \times 10^8$ m/s（光速）

对于50Hz或60Hz工频系统，电磁暂态过程通常在毫秒级完成。为了准确捕捉这些快速动态，EMT仿真需要微秒级的时间步长：
$$\Delta t_{EMT} \leq \frac{1}{10f_{max}}$$
其中$f_{max}$是关注现象的最高频率分量。

#### 机电暂态时间尺度
机电暂态过程由发电机转子的机械惯性决定，典型时间尺度为：
- **摇摆周期**：$T_{swing} = 2\pi\sqrt{\frac{H}{\pi f_0 \frac{dP}{d\delta}}}$
- **转子时间常数**：$\tau_{mech} = 2H/S_B$

机电振荡频率通常在0.1-2Hz范围内，因此TS仿真可以采用毫秒到秒级的时间步长：
$$\Delta t_{TS} \approx 1-10 \text{ ms}$$

#### 时间尺度分离原理
时间尺度分离条件可以量化为：
$$\frac{\Delta t_{TS}}{\Delta t_{EMT}} \geq 100$$

这种显著的时间尺度差异使得混合仿真成为可能，也为计算效率的提升提供了理论基础。

### 模型简化原理

混合仿真中的模型简化遵循以下数学原理：

#### 准稳态近似
在机电暂态时间尺度下，电磁过程可以视为准稳态。对于三相系统：
$$v_{abc}(t) \approx \sqrt{2}V_{rms}\cos(\omega_0 t + \theta)$$

此时，电磁微分方程可以简化为代数方程。以电感为例：
- **EMT详细模型**：$v_L(t) = L\frac{di(t)}{dt}$
- **TS简化模型**：$\bar{V}_L = j\omega_0 L \bar{I}$

#### 相量变换
EMT仿真在时域进行，TS仿真在相量域进行。两者之间的转换关系为：
$$\bar{V}(t) = v_d(t) + jv_q(t) = \frac{2}{3}(v_a + v_b e^{j2\pi/3} + v_c e^{j4\pi/3})e^{-j\theta_{ref}}$$

逆变换为：
$$\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix} = \begin{bmatrix} \cos\theta_{ref} & -\sin\theta_{ref} \\ \cos(\theta_{ref}-2\pi/3) & -\sin(\theta_{ref}-2\pi/3) \\ \cos(\theta_{ref}+2\pi/3) & -\sin(\theta_{ref}+2\pi/3) \end{bmatrix} \begin{bmatrix} v_d \\ v_q \end{bmatrix}$$

## EMT与TS详细对比

### 仿真特性对比

| 特性 | EMT仿真 | TS仿真 |
|------|---------|--------|
| **时间步长** | 10-100 $\mu$s | 1-10 ms |
| **仿真时长** | 毫秒-秒级 | 秒-分钟级 |
| **系统规模** | 通常<100节点 | 可达10,000+节点 |
| **模型细节** | 三相详细模型 | 正序/序网简化 |
| **线路模型** | 分布参数/行波 | 集中参数/等值 |
| **元件模型** | 非线性详细模型 | 准稳态线性化 |
| **求解方法** | 时域数值积分 | 代数微分方程 |
| **计算成本** | 高 | 低 |

### 数学模型对比

#### 元件建模差异

**输电线路**：
- **EMT模型**： Bergeron模型、频率相关模型(FD-line)
  $$i_k(t) = \frac{1}{Z_c}v_k(t) + I_{hist,k}(t-\tau)$$
- **TS模型**： 等值阻抗
  $$\bar{I} = \frac{\bar{V}_m - \bar{V}_n}{Z_{eq}}$$

**发电机**：
- **EMT模型**： 详细的Park方程，考虑阻尼绕组
  $$\begin{aligned}
  v_d &= -R_a i_d + \frac{d\psi_d}{dt} - \omega_r\psi_q \\
  v_q &= -R_a i_q + \frac{d\psi_q}{dt} + \omega_r\psi_d
  \end{aligned}$$
- **TS模型**： 摇摆方程+经典模型
  $$\begin{aligned}
  \frac{d\delta}{dt} &= \omega - \omega_0 \\
  M\frac{d\omega}{dt} &= P_m - P_e - D(\omega - \omega_0)
  \end{aligned}$$

**变压器**：
- **EMT模型**： 磁化曲线、饱和特性、绕组电容
- **TS模型**： 理想变压器+漏抗

### 适用范围

**EMT仿真适用场景**：
- [[vsc-hvdc]]系统控制研究
- [[facts]]装置详细控制策略验证
- [[ferroresonance]]分析
- 绝缘配合与过电压研究
- 电力电子开关过程分析

**TS仿真适用场景**：
- 大电网暂态稳定性分析
- 低频振荡分析
- 电压稳定性研究
- 负荷 shedding 策略评估

**混合仿真适用场景**：
- 含HVDC的大规模电网稳定性
- 远端故障分析
- 新型电力电子设备对电网影响
- [[co-simulation]]验证

## 接口变量的数学描述

### 接口位置选择

混合仿真接口位置的选择需要满足以下条件：
1. 接口两侧具有明显的时间尺度分离
2. 接口变量能够充分表征子系统动态
3. 接口数量最少化以减少数据交换开销

### 电压接口

#### 三相电压
EMT侧向TS侧传输的三相电压可以表示为：
$$\begin{bmatrix} v_a(t) \\ v_b(t) \\ v_c(t) \end{bmatrix} = \begin{bmatrix} V_m\cos(\omega t + \phi) \\ V_m\cos(\omega t + \phi - 2\pi/3) \\ V_m\cos(\omega t + \phi + 2\pi/3) \end{bmatrix} + \begin{bmatrix} \Delta v_a(t) \\ \Delta v_b(t) \\ \Delta v_c(t) \end{bmatrix}$$

其中$\Delta v$代表谐波和暂态分量。

在TS侧，通过基波提取算法得到相量：
$$\bar{V}_{TS} = \frac{1}{T}\int_{t-T}^{t} v_{abc}(\tau)e^{-j\omega\tau}d\tau$$

#### dq坐标系表示
在同步旋转坐标系下：
$$\begin{bmatrix} v_d \\ v_q \end{bmatrix} = \frac{2}{3}\begin{bmatrix} \cos\theta & \cos(\theta-2\pi/3) & \cos(\theta+2\pi/3) \\ -\sin\theta & -\sin(\theta-2\pi/3) & -\sin(\theta+2\pi/3) \end{bmatrix}\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

### 电流接口

#### 注入电流
TS侧计算得到的电流注入EMT侧的表达式：
$$i_{inj}(t) = I_m\cos(\omega t + \phi_{TS})$$

考虑接口动态，实际注入电流为：
$$i_{EMT}(t) = i_{inj}(t) + \Delta i(t)$$

其中$\Delta i(t)$补偿由于EMT侧详细模型引起的差异。

### 功率接口

#### 有功和无功功率
功率接口基于瞬时功率理论：
$$\begin{aligned}
p(t) &= v_a i_a + v_b i_b + v_c i_c \\
q(t) &= \frac{1}{\sqrt{3}}[(v_b - v_c)i_a + (v_c - v_a)i_b + (v_a - v_b)i_c]
\end{aligned}$$

平均功率（TS侧使用）：
$$\begin{aligned}
P &= \frac{3}{2}(v_d i_d + v_q i_q) \\
Q &= \frac{3}{2}(v_q i_d - v_d i_q)
\end{aligned}$$

### 阻抗接口

#### 等值阻抗矩阵
TS侧向EMT侧提供的等值阻抗表示为：
$$Z_{eq}(s) = R_{eq} + sL_{eq} + \frac{1}{sC_{eq}}$$

在频域中，通过[[vector-fitting]]得到有理函数近似：
$$Z_{eq}(s) \approx \sum_{k=1}^{N}\frac{r_k}{s-p_k} + d + se$$

## 串行混合仿真

### 主从式架构

#### EMT主控模式
在EMT主控模式下，时间推进由EMT仿真主导：

1. **EMT仿真步进**：
   $$t_{n+1} = t_n + \Delta t_{EMT}$$

2. **数据累积**：累积$N = \Delta t_{TS}/\Delta t_{EMT}$个EMT步的接口数据

3. **TS触发**：当达到TS时间步长时，触发TS仿真
   $$t_{TS,m+1} = t_{TS,m} + \Delta t_{TS}$$

4. **数据交换**：
   - EMT $\rightarrow$ TS：平均电压/电流、功率
   - TS $\rightarrow$ EMT：等值电路参数

数学表达式：
$$\bar{V}_{TS}^{(m)} = \frac{1}{N}\sum_{k=0}^{N-1} V_{EMT}(t_m + k\Delta t_{EMT})$$

#### TS主控模式
在TS主控模式下：

1. **TS仿真步进**：以较大步长推进系统状态
2. **EMT插值**：在TS步内，通过插值获得EMT边界条件
   $$v_{EMT}(t) = f(\bar{V}_{TS}^{(m)}, \bar{V}_{TS}^{(m+1)}, t)$$

### 交替求解算法

#### 迭代过程
设第$m$个TS时间步，第$k$次迭代：

$$\begin{aligned}
\text{Step 1:} \quad \bar{V}_{boundary}^{(k)} &\rightarrow \text{EMT求解} \rightarrow \bar{I}_{injection}^{(k)} \\
\text{Step 2:} \quad \bar{I}_{injection}^{(k)} &\rightarrow \text{TS求解} \rightarrow \bar{V}_{boundary}^{(k+1)} \\
\text{Step 3:} \quad \text{收敛检查:} &\|\bar{V}^{(k+1)} - \bar{V}^{(k)}\| < \epsilon
\end{aligned}$$

#### 收敛性分析
迭代过程的收敛条件取决于子系统间的耦合强度。设雅可比矩阵为$J$，则收敛要求：
$$\rho(J) < 1$$

其中$\rho(\cdot)$表示谱半径。

### 串行实现流程

```
初始化:
  设定 t = 0, 初始状态 x(0)

主循环 (while t < t_end):
  ├─ EMT子系统求解 (N个小步)
  │   ├─ 使用TS提供的边界条件
  │   ├─ 更新EMT状态: x_EMT(t + Δt_EMT)
  │   └─ 累积接口数据
  │
  ├─ 数据准备
  │   ├─ 计算平均功率
  │   ├─ 提取基波相量
  │   └─ 更新等值参数
  │
  ├─ TS子系统求解
  │   ├─ 使用EMT提供的注入量
  │   ├─ 更新TS状态: x_TS(t + Δt_TS)
  │   └─ 计算新边界条件
  │
  └─ t = t + Δt_TS
```

## 并行混合仿真

### 同时求解架构

#### 分区协调
并行混合仿真同时推进两个子系统：

$$\begin{aligned}
\dot{x}_{EMT} &= f_{EMT}(x_{EMT}, u_{EMT}(x_{TS})) \\
\dot{x}_{TS} &= f_{TS}(x_{TS}, u_{TS}(x_{EMT}))
\end{aligned}$$

#### 时间同步机制
为了保证数值稳定性，需要协调两个子系统的时间推进：

**全局时钟驱动**：
- 设定全局时间服务器
- 每个子系统向时间服务器注册
- 子系统完成当前步后等待同步信号

**预测-校正方法**：
1. **预测步**：使用外推预测接口变量
   $$\hat{u}(t+\Delta t) = u(t) + \Delta t \cdot \dot{u}(t)$$

2. **并行求解**：两个子系统独立求解

3. **校正步**：基于实际求解结果修正
   $$u_{corrected} = u_{predicted} + K(\hat{u} - u_{actual})$$

### 并行实现策略

#### 保守策略（Chandy-Misra-Bryant）
- 每个子系统维护本地时钟
- 仅当确保不会接收到更早消息时才推进
- 保证因果性，但可能降低并行度

#### 乐观策略（Time Warp）
- 允许子系统乐观推进
- 检测到错误时回滚
- 高并行度但需要状态保存机制

### 数据交换协议

#### 同步点设置
在时间$t_{sync}$处强制同步：

$$t_{sync} = k \cdot \Delta t_{sync}, \quad k = 0, 1, 2, ...$$

其中$\Delta t_{sync}$是同步间隔，通常取$\Delta t_{TS}$或更小。

#### 数据封装
交换数据包结构：
```
数据包 {
  timestamp: 时间戳
  sequence: 序列号
  type: 数据类型 (电压/电流/功率/阻抗)
  values: [v_d, v_q] 或 [i_d, i_q] 或 [...]
  validity: 有效性标志
}
```

## 接口技术详解

### 戴维南等值接口

#### 等值电路形式
TS侧向EMT侧提供的戴维南等值为：
$$\bar{V}_{Th} = \bar{V}_{open} - Z_{Th}\bar{I}$$

其中：
- $\bar{V}_{open}$：开路电压（TS计算）
- $Z_{Th}$：等值阻抗
- $\bar{I}$：接口电流

#### 时域实现
EMT仿真中，戴维南等值表示为：
$$v(t) = v_{Th}(t) - R_{Th}i(t) - L_{Th}\frac{di(t)}{dt}$$

使用梯形积分法离散化：
$$v^{n+1} = v_{Th}^{n+1} - R_{Th}i^{n+1} - \frac{2L_{Th}}{\Delta t}i^{n+1} + \frac{2L_{Th}}{\Delta t}i^n + L_{Th}\frac{di^n}{dt}$$

#### 阻抗计算
等值阻抗通过TS侧导纳矩阵计算：
$$Z_{Th} = (Y_{reduced})^{-1}$$

其中$Y_{reduced}$是TS侧网络在接口节点处的导纳矩阵。

### 诺顿等值接口

#### 等值电路形式
诺顿等值为戴维南等值的对偶形式：
$$\bar{I}_{N} = \bar{I}_{sc} - Y_{N}\bar{V}$$

#### 与EMT的接口
EMT侧接收诺顿等值表示为电流注入：
$$i_{inj}(t) = i_N(t) - G_N v(t)$$

#### 等值导纳计算
$$Y_N = Z_{Th}^{-1}$$

诺顿等值更适合于EMT侧的节点导纳矩阵求解。

### 直接接口技术

#### [[direct-interface-technique]]原理
直接接口不使用等值电路，而是直接交换状态变量：

**电压驱动的直接接口**：
$$v_{EMT}(t) = \text{Interp}(\bar{V}_{TS}(t_k), \bar{V}_{TS}(t_{k+1}), t)$$

**电流驱动的直接接口**：
$$\bar{I}_{TS} = \text{Transform}(i_{EMT}(t))$$

#### 节点撕裂方法
`node-tearing`将接口节点从两个子系统中分离：

原始网络方程：
$$YV = I$$

撕裂后：
$$\begin{bmatrix} Y_{EE} & Y_{ET} & Y_{E\Gamma} \\ Y_{TE} & Y_{TT} & Y_{T\Gamma} \\ Y_{\Gamma E} & Y_{\Gamma T} & Y_{\Gamma\Gamma} \end{bmatrix}\begin{bmatrix} V_E \\ V_T \\ V_\Gamma \end{bmatrix} = \begin{bmatrix} I_E \\ I_T \\ I_\Gamma \end{bmatrix}$$

其中$\Gamma$表示接口节点集合。

### 等值方法对比

| 等值方法 | 优点 | 缺点 | 适用场景 |
|----------|------|------|----------|
| **戴维南** | 物理意义明确 | 需要阻抗逆运算 | 高阻抗网络 |
| **诺顿** | 易于节点分析 | 可能奇异 | 低阻抗网络 |
| **直接接口** | 无等值误差 | 稳定性要求高 | 紧密耦合 |
| **WARD** | 计算简单 | 精度有限 | 远程等值 |
| **REI** | 保留物理特性 | 计算复杂 | 需要物理等值 |

## 稳定性分析

### 接口时延影响

#### 时延模型
设接口传输时延为$\tau$，则接口方程变为：
$$u_{EMT}(t) = u_{TS}(t - \tau)$$

#### 稳定性判据
对于简单RL电路接口，稳定性条件为：
$$\tau < \frac{L}{R}$$

更一般的，使用奈奎斯特判据分析：
$$1 + G(j\omega)H(j\omega)e^{-j\omega\tau} = 0$$

其中$G(s)$是EMT子系统传递函数，$H(s)$是TS子系统传递函数。

#### 时延补偿
预测补偿方法：
$$\hat{u}(t) = u(t-\tau) + \tau\dot{u}(t-\tau) + \frac{\tau^2}{2}\ddot{u}(t-\tau)$$

### 数据插值方法

#### 线性插值
[[interpolation-method]]最简单，在两个数据点间线性过渡：
$$u(t) = u_k + \frac{t-t_k}{t_{k+1}-t_k}(u_{k+1}-u_k), \quad t_k \leq t \leq t_{k+1}$$

#### 三次样条插值
提供更平滑的过渡：
$$u(t) = a_k + b_k(t-t_k) + c_k(t-t_k)^2 + d_k(t-t_k)^3$$

系数通过连续性条件确定。

#### 插值误差分析
线性插值误差：
$$\epsilon_{linear} \approx \frac{\Delta t^2}{8}\ddot{u}_{max}$$

三次样条插值误差：
$$\epsilon_{spline} \approx \frac{\Delta t^4}{384}u^{(4)}_{max}$$

### 稳定性增强技术

#### 阻尼注入
在接口处添加虚拟阻尼：
$$R_{virtual} = \alpha\sqrt{\frac{L_{eq}}{C_{eq}}}$$

其中$\alpha$是阻尼系数。

#### 预测-校正迭代
在每个时间步进行多轮迭代提高精度：
$$u^{(k+1)} = u^{(k)} + \omega(f(u^{(k)}) - u^{(k)})$$

其中$\omega$是松弛因子。

## EMT-TS接口详细实现

### 正序接口

#### 对称系统假设
`positive-sequence`假设系统三相对称，仅传输正序分量：
$$\bar{V}_+ = \frac{1}{3}(\bar{V}_a + \bar{V}_b e^{j2\pi/3} + \bar{V}_c e^{j4\pi/3})$$

#### 实现简化
正序接口大大简化了数据交换：
- 仅需2个实数量（d-q分量）
- 无需考虑负序和零序
- 计算效率最高

#### 适用条件
正序接口适用于：
- 三相平衡系统
- 对称故障分析
- 稳态和准稳态研究

### 三相接口

#### [[three-phase-bridge-inverter]]实现
完整的三相接口传输全部相量信息：
$$\begin{bmatrix} \bar{V}_a \\ \bar{V}_b \\ \bar{V}_c \end{bmatrix} = \begin{bmatrix} V_a\angle\theta_a \\ V_b\angle\theta_b \\ V_c\angle\theta_c \end{bmatrix}$$

#### 序分量分解
三相量可以分解为：
$$\begin{bmatrix} \bar{V}_0 \\ \bar{V}_+ \\ \bar{V}_- \end{bmatrix} = \frac{1}{3}\begin{bmatrix} 1 & 1 & 1 \\ 1 & a & a^2 \\ 1 & a^2 & a \end{bmatrix}\begin{bmatrix} \bar{V}_a \\ \bar{V}_b \\ \bar{V}_c \end{bmatrix}$$

其中$a = e^{j2\pi/3}$。

#### 不对称处理能力
三相接口可以处理：
- 不对称故障
- 不平衡负荷
- 负序和零序分量

### 等值方法实现

#### `ward-equivalent`
WARD等值通过高斯消去简化网络：
$$Y_{eq} = Y_{II} - Y_{IE}Y_{EE}^{-1}Y_{EI}$$

其中下标$I$表示保留节点，$E$表示消去节点。

#### `rei-equivalent`
REI(Radial Equivalent Independent)等值保持物理特性：
1. 构建等值发电机
2. 保持功率平衡
3. 阻抗匹配

## 应用场景

### 远端故障分析

#### 场景描述
当故障发生在距离关注区域较远处：
- **详细区域**：故障点附近，使用EMT
- **等值区域**：远端系统，使用TS

#### 实现要点
1. 在关注区域边界设置接口
2. EMT侧详细建模故障过程
3. TS侧提供远端系统等值
4. 分析故障对关注区域的影响

#### 案例
HVDC换流站附近远端交流故障：
- 换流站及附近网络：EMT详细模型
- 远端交流电网：TS等值模型
- 研究故障对直流系统的影响

### FACTS控制研究

#### 场景描述
[[facts]]装置的控制策略验证：
- FACTS装置：详细的EMT模型
- 外部电网：TS简化模型

#### 控制接口
FACTS控制器信号交换：
$$\begin{aligned}
\text{测量信号} &: V, I, P, Q \rightarrow \text{控制器} \\
\text{控制信号} &: \alpha, V_{ref}, Q_{ref} \rightarrow \text{FACTS}
\end{aligned}$$

#### 典型应用
- SVC电压控制
- STATCOM无功补偿
- TCSC阻抗调节

### HVDC故障分析

#### [[vsc-hvdc]]混合仿真
柔性直流输电系统的故障响应分析：

**AC侧故障**：
- 换流站：EMT详细模型
- 交流电网：TS等值模型

**DC侧故障**：
- 直流线路：EMT行波模型
- 控制系统：详细模型

#### 故障类型
1. **单相接地故障**
2. **相间短路故障**
3. **三相短路故障**
4. **直流极间短路**

### 新能源并网

#### 风电场建模
大型风电场的[[wind-farm-modeling]]：
- 风电机组：详细EMT模型
- 集电网络：等值或详细模型
- 外送通道：TS模型

#### 光伏电站
光伏并网逆变器的控制研究：
- 逆变器：EMT详细模型
- 光伏阵列：简化或详细模型
- 电网：TS等值

## 验证与精度分析

### 精度验证方法

#### 与纯EMT对比
`accuracy-verification`的金标准：
$$\epsilon = \frac{\|x_{hybrid} - x_{EMT}\|}{\|x_{EMT}\|} \times 100\%$$

#### 与纯TS对比
验证机电暂态一致性：
$$\epsilon_{TS} = \frac{\|x_{TS-hybrid} - x_{pure-TS}\|}{\|x_{pure-TS}\|}$$

#### 能量守恒检查
验证功率平衡：
$$\sum P_{in} - \sum P_{out} = \frac{dE}{dt}$$

### 误差来源分析

#### `hybrid-error`
网络等值引入的误差：
$$\epsilon_{eq} = \sum_{k=1}^{N_{removed}} |S_k|$$

其中$S_k$是消去节点的复功率。

#### 接口误差
数据交换引入的误差包括：
1. **采样误差**：时间离散化
2. **量化误差**：数值精度
3. **插值误差**：数据重构
4. **时延误差**：传输延迟

总接口误差：
$$\epsilon_{interface} = \sqrt{\epsilon_{sample}^2 + \epsilon_{quant}^2 + \epsilon_{interp}^2 + \epsilon_{delay}^2}$$

#### 模型简化误差
从详细模型到简化模型的误差：
$$\epsilon_{model} = \|f_{detailed}(x) - f_{simplified}(x)\|$$

### 误差控制策略

#### 接口位置优化
最小化等值误差：
$$\min_{\Gamma} \epsilon_{eq}(\Gamma)$$

约束条件：
- 接口两侧时间尺度分离
- 接口数量限制
- 物理合理性

#### 自适应步长
根据局部误差调整时间步长：
$$\Delta t_{new} = \Delta t_{old} \cdot \min\left(\sqrt{\frac{\epsilon_{tol}}{\epsilon_{actual}}}, 2\right)$$

#### 多步验证
定期进行全系统EMT验证：
- 关键工况完整EMT仿真
- 混合仿真结果对比
- 误差统计和趋势分析

## 软件实现

### 商业软件

#### PSCAD与PSSE互连
- **PSCAD/EMTDC**：电磁暂态仿真
- **PSS/E**：机电暂态仿真
- **接口方式**：通过API或文件交换

#### RT-LAB实时混合仿真
`rt-lab`支持：
- 实时混合仿真
- 硬件在环测试
- 分布式计算

### 自定义开发

#### API接口
通过`api-interface`实现软件互联：
- Socket通信
- 共享内存
- 消息队列

#### 联合仿真框架
[[co-simulation]]平台：
- FMI/FMU标准
- 自定义协议
- 分布式架构

## 发展趋势

### 自动分区技术

#### `automatic-partitioning`算法
基于图论的自动分区：
$$\min_{P} Cut(P) + \lambda \cdot Imbalance(P)$$

其中$Cut(P)$是分区间的连接权重，$Imbalance(P)$是子系统规模不平衡度。

#### 时标分离检测
自动识别时间尺度分离点：
$$\text{Separation Index} = \frac{\tau_{electromechanical}}{\tau_{electromagnetic}}$$

### 多物理场耦合

#### `multi-physics`混合仿真
扩展至其他物理域：
- 电力-热力耦合
- 电力-机械耦合
- 控制-电力耦合

### 人工智能辅助

#### 智能分区
利用机器学习优化分区：
- 神经网络预测最优分区
- 强化学习动态调整

#### 误差估计
基于深度学习的误差预测：
$$\hat{\epsilon} = f_{NN}(x_{system}, x_{partition}, t_{simulation})$$

## 相关方法

- [[hybrid-modeling]] - 混合仿真建模方法
- [[co-simulation]] - 多软件联合仿真技术
- [[electromechanical-electromagnetic-hybrid-simulation]] - 详细理论
- [[time-domain-modeling-of-a-subsea-buried-cable]] - 时域仿真基础
- [[interface-technique]] - 接口方法总览
- [[direct-interface-technique]] - 直接接口详细实现
- [[equivalent-circuit-method]] - 等值方法理论
- `emt-ts-hybrid` - 混合仿真专题

## 来源论文

见[[index]]中混合仿真相关文献。

---

*最后更新: 2026-05-03*
