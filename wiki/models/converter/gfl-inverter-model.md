---
title: "跟网型变流器 (Grid-Following Inverter, GFL)"
type: model
tags: [grid-following, gfl, current-control, pll, renewable-energy, inverter, ibr]
created: "2026-04-30"
updated: "2026-05-18"
---

# 跟网型变流器 (Grid-Following Inverter, GFL)

## 定义

跟网型变流器（Grid-Following Inverter, GFL）是当前新能源并网的主流技术路线，其核心特征是**电流控制+PLL同步**：控制器给出dq坐标系下的电流指令 $(i_d^*, i_q^*)$，PWM将dq电压指令 $(v_d^*, v_q^*)$ 转换为变流器端口电压。PLL从电网电压提取相位角 $\theta_{pll}$，用于坐标变换和同步。GFL变流器不尝试维持电压和频率支撑，而是被动跟随电网相位——这使它在强电网（SCR>5）下稳定可靠，但在弱电网（SCR<3）下因PLL与电网阻抗的交互可能引发次同步振荡（SSO）和动态不稳定。

从控制结构上，GFL与构网型变流器（GFM）的本质区别在于：GFM采用**电压控制内环**（内部建立电压参考），而GFL采用**电流控制内环**（跟踪电网相位注入电流）。当电网强度降低时，PLL的锁相误差增大，GFL的电流注入与电网电压之间的相位偏差会导致负阻尼效应。

## EMT中的角色

GFL在EMT仿真中的核心角色是**新能源并网接口模型**。随着光伏、风电、储能渗透率提升，GFL变流器已成为电网中占比最高的电力电子接口类型（约60-80%的新能源装机容量）。EMT仿真的任务包括：

- **故障电流特性**：GFL故障电流受PLL和电流环支配，与同步机的短路电流特性完全不同。同步机短路电流峰值可达10倍额定（由磁链守恒决定），而GFL受电流限幅限制约1.5-2倍额定（由功率半导体器件的IGBT电流承受能力决定）。这一差异对保护定值整定和短路计算有根本性影响。
- **次同步振荡分析**：PLL带宽与弱电网阻抗交互，在2-10Hz范围产生振荡模式（次同步控制振荡，SSCO/SSO）。振荡频率由PLL控制环带宽、电网电抗和直流侧电容共同决定。
- **故障穿越（FRT）**：低电压穿越期间GFL需维持注入无功支撑电网，PWM饱和、PLL失锁、电流限幅共同决定故障响应。GFL在故障期间可向电网注入1.1-1.5 pu的恒定电流（受半导体器件限制），而非同步机的反电动势驱动短路电流。
- **谐波相互作用**：PWM开关产生特征谐波（次谐波簇 $n\omega_1 \pm k\omega_{pll}$）和非特征谐波（直流偏置、间谐波）。多GFL并联时谐波聚合效应在电网谐波阻抗上产生电压畸变，反过来影响各GFL的PLL同步精度。

### 关键挑战

GFL的EMT建模面临多时间尺度耦合的挑战：PLL同步（10-100ms量级）、电流环控制（1-10ms）、PWM开关（0.1-1ms）、以及功率器件的开通关断（μs级）。如何在保持物理可解释性的前提下合理简化，是EMT建模的核心问题。

另一个核心挑战是**电磁暂态与机电暂态的交互建模**：在新能源渗透率高的系统中，GFL的快速电流控制与同步机的机电暂态在相近频段（0.1-10Hz）发生动态交互，需要在EMT环境中以适当步长捕捉这种耦合效应。

## EMT建模方法

GFL变流器在EMT仿真中有五种典型建模粒度，按精度从高到低排列如下：

| 模型类型 | 精度 | 计算效率 | 步长范围 | 适用场景 | 失效场景 |
|---------|------|---------|---------|---------|---------|
| **SW**（详细开关模型） | 最高 | 最低 | 1-10 μs | 谐波分析、开关纹波、死区效应 | 大系统、实时HIL |
| **VI**（电压插值模型） | 高 | 中 | 10-50 μs | 含PWM调制的详细控制 | 极高次谐波 |
| **AV**（平均值模型） | 中高 | 高 | 50-100 μs | 故障穿越、控制交互 | 开关纹波、谐波精度 |
| **CCI**（受控电流注入模型） | 中 | 很高 | 100-500 μs | 机电暂态接口、网络等值 | 详细开关事件 |
| **SCI**（简化电流注入模型） | 中低 | 极高 | 500 μs-1 ms | 大系统批量扫描 | 非线性控制、故障暂态 |

### 1. 详细开关模型（SW）

SW模型显式表示功率器件开关，直接由PWM门极信号决定电路拓扑。器件模型可以是理想开关、带阻尼电阻的开关或可变电阻（ON时为导通电阻，OFF时为大电阻）。SW模型能保留开关频率分量、死区影响和二极管续流路径，但最小步长必须小于开关周期的1/20-1/50以避免量化误差在电流中累积。

根据Sano等2022在相同系统、相同故障条件、相同XTAP求解框架下的对比测试，SW模型的计算时间基准为1.0（100%），步长约2 μs。由于需要小步长计算，大系统仿真（如含100+台GFL的新能源场站）计算时间可达数小时，不适合参数扫描和实时HIL测试。

### 2. 电压插值模型（VI）

VI模型由Sano等于2022年正式提出并系统比较，其核心思想是**不在固定步长网格上强制开关时刻**，而用插值占空比公式估计一个步长内参考电压与载波的交越位置。具体地，三角载波PWM中，精确开关时刻由参考电压 $v^*$ 与载波 $v_{carrier}$ 的交点决定：

$$t_{rise} = t_{n-1} + \frac{T_s}{2}\left(1 + \frac{v^* - v_{carrier}}{h}\right)$$

其中 $h$ 为载波斜率（由载波幅值和频率决定），$T_s$ 为仿真步长。插值电压 $\bar{s}$ 使区间 $[t_{rise}, t_{fall}]$ 内的电压面积与理论PWM脉冲面积相等：

$$\bar{s} = \frac{1}{2} + \frac{v^* - v_{carrier}}{2hT_s}$$

在梯形积分格式下，该插值电压直接作为受控电压源的输出。VI模型在交直流端口维持瞬时功率平衡：直流侧用受控电流源 $i_{dc}$ 表示功率平衡，直流电压动态 $\frac{dv_{dc}}{dt} = \frac{i_{dc} - i_{in}}{C}$ 由外部网络决定。

**量化数据**（Sano 2022）：VI模型计算时间约为SW的**19%**，步长可由SW的2 μs放大至10 μs（约5倍）。VI能保留开关相关谐波（5-50次）并正确反映电流内环的动态，是精度与效率的最佳折中。

### 3. 平均值模型（AV）

AV模型基于状态空间平均法，用调制占空比直接给出相电压平均值。例如，v_{sa} = d_a v_{dc}，其中d_a为a相占空比（一个步长内的平均值）。AV模型保留控制器与基波动态，消去了开关纹波和死区相关谐波。

AV模型的控制接口与SW模型相同（保留PLL、功率环、电流环），但功率器件级用连续时间模型等效。在dq坐标系下，GFL端口电压的连续时间动态方程为：

$$\frac{di_d}{dt} = \frac{1}{L}\left(v_d - Ri_d + \omega L i_q - v_{dc}s_d\right)$$

$$\frac{di_q}{dt} = \frac{1}{L}\left(v_q - Ri_q - \omega L i_d - v_{dc}s_q\right)$$

其中 $s_d, s_q$ 为dq坐标系下的等效开关函数（由PWM占空比决定），不再是离散的0/1值，而是连续变量 $d \in [0,1]$。

**量化数据**（Sano 2022）：AV模型计算时间约为SW的**1.5%**，步长可放大至100 μs（约50倍）。但AV模型在某些故障场景下会乐观估计电流控制的稳定裕度——因为它忽略了PWM的离散采样效应和有限更新率下的延时。

### 4. 受控电流注入模型（CCI）

CCI模型把逆变器交流侧等效为受控电流源，输入主要是有功/无功或电流参考。其dq电流指令由功率外环直接给出（而非PLL锁相角度+功率反解），直流侧通过功率平衡计算电流。

CCI模型在接口上表现为诺顿等效：电流源 $i_{abc} = f(P_{ref}, Q_{ref})$ 并联电导 $G = 1/R_{th}$（可选）。CCI保留功率外环动态，但缺少电流内环和PWM调制环节——因此在电网电压相位突变（如低电压穿越）时，电流参考无法正确跟踪电压相位变化。

**量化数据**（Sano 2022）：CCI模型计算时间约为SW的**0.20%**，步长可放大至600 μs（约300倍）。但CCI缺少PLL相关能力，在电压相位变化和暂降逻辑下会偏离SW结果。

### 5. 简化电流注入模型（SCI）

SCI进一步简化，去除所有控制环节，直接用恒定电流注入（由稳态功率指令决定）。适用于快速潮流计算、大系统静态安全评估和蒙特卡洛批量扫描。

**量化数据**（Sano 2022）：SCI模型计算时间约为SW的**0.12%**，步长可达600 μs-1 ms。但缺少PLL动态，在故障和暂态场景下完全失效。

## 形式化表达

### 同步旋转坐标系电压方程

在PLL估计的dq坐标系下，GFL端口电压方程为dq耦合形式：

$$\frac{di_d}{dt} = \frac{1}{L}\left(v_d - Ri_d + \omega L i_q - v_{dc}s_d\right)$$

$$\frac{di_q}{dt} = \frac{1}{L}\left(v_q - Ri_q - \omega L i_d - v_{dc}s_q\right)$$

其中：$v_d, v_q$ 为电网电压在dq坐标系的分量；$i_d, i_q$ 为变流器输出电流的dq分量；$R, L$ 为滤波器阻抗（串联电阻和电感）；$v_{dc}$ 为直流电压；$s_d, s_q$ 为dq坐标系下的等效开关函数（由PWM占空比决定）。

### 锁相环（PLL）模型

**SRF-PLL（同步参考帧锁相环）**：最常用的PLL结构，从三相电网电压 $v_{abc}$ 经Clark变换得到 $\alpha\beta$ 坐标系，再用Park变换得到dq分量。q轴电压 $v_q$ 在稳态下为零，偏离同步时 $v_q \neq 0$。PI控制器检测 $v_q$ 并输出角频率：

$$\omega_{pll} = \omega_{ff} + K_p^{pll} v_q + K_i^{pll} \int v_q dt$$

其中 $K_p^{pll}, K_i^{pll}$ 为PI参数，$\omega_{ff}$ 为前馈频率（通常为额定电网频率 $\omega_0 = 2\pi \cdot 60$ rad/s或50 rad/s）。

**DSOGI-PLL（二阶广义积分器锁相环）**：在q轴引入二阶广义积分器（SOGI）构造正交信号，可抑制电网电压不平衡（负序分量）和谐波影响。DSOGI的传递函数为：

$$H_{SOGI}(s) = \frac{\omega_0 s}{s^2 + \omega_0 s + \omega_0^2}$$

DSOGI-PLL同时输出正交信号 $(v_\alpha, v_\beta)$ 和正序分量提取结果 $(v_\alpha^+, v_\beta^+)$，再经SRF-PLL得到同步角。**自适应带宽DSOGI-PLL**（Ranasinghe 2024）在暂态期间临时冻结PLL估计频率以避免频率估计污染DSOGI滤波，并在稳态恢复较低带宽以抑制噪声。

### 功率环与电流环

GFL采用双环级联控制：

**功率外环（慢动态，10-100 ms）**：

$$i_d^* = \left(K_p^p + \frac{K_i^p}{s}\right)(P_{ref} - P), \quad i_q^* = \left(K_p^q + \frac{K_i^q}{s}\right)(Q_{ref} - Q)$$

其中 $P = \frac{3}{2}(v_d i_d + v_q i_q)$、$Q = \frac{3}{2}(v_q i_d - v_d i_q)$ 为瞬时有功/无功功率（Park定向后通常令 $v_q = 0$，简化为 $P = \frac{3}{2}v_d i_d$，$Q = -\frac{3}{2}v_d i_q$）。

**电流内环（快动态，1-10 ms）**：

$$v_d^* = \left(K_p^c + \frac{K_i^c}{s}\right)(i_d^* - i_d) - \omega L i_q + v_d$$

$$v_q^* = \left(K_p^c + \frac{K_i^c}{s}\right)(i_q^* - i_q) + \omega L i_d + v_q$$

前馈项 $\omega L i_q$（d轴）和 $-\omega L i_d$（q轴）为dq解耦项，用于消除dq轴间的耦合，实现独立控制。

### PWM调制

电压指令 $v_{dq}^*$ 经反向Park变换得到三相电压参考 $v_{abc}^*$，再与三角载波比较生成PWM门极信号。双边沿调制（Triangle Carrier PWM）的开关时刻精确值由插值公式（VI模型核心）给出。

### 电流限幅与故障穿越逻辑

GFL通常在电流内环输出设置限幅器：

$$i_{dq}^{lim} = \begin{cases} i_{dq}^* & \text{if } |i_{dq}^*| \leq I_{max} \\ I_{max} \cdot \text{sign}(i_{dq}^*) & \text{if } |i_{dq}^*| > I_{max} \end{cases}$$

$I_{max}$ 通常设为1.1-1.5 pu额定电流。限幅后，内环输出电压指令可能饱和，PWM以最大占空比运行。故障穿越期间，GFL还需根据电网电压跌落程度注入无功电流（电网规范要求每1%电压跌落注入至少2%额定无功电流）。

### DQ导纳模型

DQ导纳模型将GFL在dq坐标系下线性化，得到小信号输入导纳矩阵：

$$\begin{bmatrix} \Delta i_d \\ \Delta i_q \end{bmatrix} = \mathbf{Y}_{dq} \begin{bmatrix} \Delta v_d \\ \Delta v_q \end{bmatrix}$$

其中 $\mathbf{Y}_{dq}$ 的元素由电流环PI参数、PLL带宽、滤波器参数和直流电压决定。DQ导纳模型广泛应用于阻抗稳定性分析（Gnanarathna 2011，Fan & Miao 2023）。通过Gaussian脉冲激励（Fan & Miao 2023）或PRBS扰动注入，可从EMT仿真环境直接提取DQ导纳参数。

## 关键技术挑战

### PLL与弱电网交互失稳

当电网强度 SCR < 3（弱电网）时，PLL与电网阻抗的交互可能导致小信号失稳。PLL的闭环传递函数在dq坐标系下等效为一个与电网电抗串联的负电阻，在特定频段（通常2-10Hz）提供负阻尼。

**物理机理**：PLL在锁相过程中将电网电压相位映射为dq旋转坐标系的定向基准。当电网阻抗 $Z_g = R_g + jX_g$ 与PLL控制环交互时，等效电阻在特定频率范围内变为负值（即GFL向电网注入有功时从电网吸收等效负阻尼功率），导致振荡发散。

**量化边界**（Carreño 2026）：SCR < 2时Hopf分岔临界功率下降约40%（从0.9 pu降至0.55 pu），时间尺度比 $\tau_L / \tau_{PLL} < 0.1$ 时误差小于2%。改进型DSOGI-PLL（Ranasinghe 2024）将SCR稳定下限从2.3扩展至1.0。

**RMS+模型**（Carreño 2026）可在保持较低计算成本的同时捕捉PLL与网络动态的相互作用，比传统RMS模型（恒定导纳）多保留影响PLL同步稳定性的网络动态成分，比完整EMT模型状态变量少，适合大规模模态分析。

### 电流限幅与故障穿越

GFL在电网故障时受直流侧电压支撑能力和电流限幅器的约束，输出电流被钳位在1.1-1.5倍额定值。这与同步机形成鲜明对比：同步机峰值短路电流可达10倍额定（由磁链守恒和励磁系统决定），而GFL受功率半导体器件的IGBT电流承受能力限制。

**Carreño 2026的关键发现**：在SCR<2的极弱电网中，传统RMS模型的恒定导纳接口无法捕捉PLL闭环与电网阻抗在故障暂态期间的相互作用，导致无法预测Hopf分岔边界。RMS+通过在故障后保留网络电感电流的di/dt动态，解决了这一建模失效问题。

故障期间PLL输入电压可能跌落至正常值的20-30%，PLL失锁是GFL脱网的主要原因之一。DSOGI-PLL通过二阶广义积分器提供更强的抗扰动能力，但仍需在电网电压严重畸变时配合自适应带宽机制。

### 谐波与间谐波注入

PWM开关产生特征谐波（次谐波簇 $n\omega_1 \pm k\omega_{pll}$）和非特征谐波（直流偏置、间谐波）。其中 $n$ 为载波比（奇数次载波谐波主要分布），$k$ 为边带系数。

**多GFL并联谐波聚合**：当多台GFL变流器并联于同一PCC（公共连接点）时，各变流器的PWM载波相位若未协调（如分散式光伏电站无统一PLL同步），载波谐波可能叠加，形成间谐波注入，严重时可在电网谐波阻抗上激发电压畸变（>5% THD），反过来影响各GFL的PLL同步精度，形成正反馈。

**Luchini 2023的谐波分析**：ATP/ATPDraw中实现的GFL等效模型，使用LPF-PLL和DSOGI-PLL两种同步方案，可有效研究谐波对GFL稳态和故障响应的影响。结果表明在2-50次谐波范围内，DSOGI-PLL比LPF-PLL对谐波电压的抗扰动能力更强。

###dq轴耦合与稳定性分析

GFL的dq电压方程在dq坐标系下通过滤波器电感实现耦合（$\omega L i_q$ 和 $-\omega L i_d$ 项）。当电网频率偏移（如 $\Delta f > 0.5$ Hz）或PLL锁相角误差增大时，dq耦合项的实际值偏离标称设计，内环控制的解耦效果下降，导致等效控制带宽收缩，在弱电网条件下更易引发振荡。

## 量化性能边界

| 研究目标 | 推荐模型 | 步长 | 加速比（vs SW） | 精度说明 |
|---------|---------|------|-------------|---------|
| 谐波分析（开关纹波、电磁兼容） | SW/VI | 1-20 μs | 1×（SW）/ 5×（VI） | VI保留5-50次谐波，误差<3% |
| 次同步振荡（SSCO/SSO） | VI/AV（含PLL） | 10-50 μs | 5-10× | 需保留PLL动态和电网阻抗 |
| 故障穿越/短路电流 | AV/CCI | 50-200 μs | 20-100× | 电流限幅和FRT逻辑 |
| 大系统参数扫描/蒙特卡洛 | CCI/SCI | 200-1000 μs | 100-500× | 精度有限，适合批量扫描 |
| 并网振荡分析（阻抗稳定性） | VI/AV（含dq导纳） | 10-100 μs | 10-50× | 需提取DQ导纳矩阵 |

**来源量化数据**：

- **Luchini 2023**（ATP/ATPDraw GFL等效模型）：故障条件下平均误差约2.33%，执行时间减少约70%（vs 详细光伏基准模型）。PI参数：$k_p = 0.8$，$k_i = 61.69$（SRF-PLL）。
- **Sano 2022**（五模型系统比较）：VI=SW的19%，AV=SW的1.5%，CCI=SW的0.20%，SCI=SW的0.12%。步长：SW=2 μs，VI=10 μs，AV=100 μs，CCI/SCI=600 μs。
- **Carreño 2026**（RMS+）：SCR<2时Hopf分岔临界功率下降约40%（0.9 pu→0.55 pu），时间尺度比 $\tau_L / \tau_{PLL} < 0.1$ 时误差<2%。
- **Ranasinghe 2024**（自适应DSOGI-PLL）：SCR稳定下限从2.3扩展至1.0（弱电网稳定性边界改善）。

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
| 阻抗稳定性分析 | VI/AV（含dq导纳） | 10-100 μs | 需提取DQ导纳矩阵 |

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
- [[dq-transformation]] - dq轴解耦控制的数学表达

## 相关模型

- [[gfm-inverter-model]] - 构网型变流器（GFM与GFL对比）
- [[vsc-model]] - 两电平/三电平换流器通用模型
- [[pv-system-model]] - 光伏并网系统聚合模型
- [[dfig-model]] - 双馈风机（本质是GFL加励磁控制）
- [[ibr]] - 跟网型资源（IBR）聚合等值模型
- [[bess-model]] - 储能变流器（BESS-PCS，本质是GFL加储能控制）

## 相关主题

- [[real-time-simulation]] - GFL实时HIL测试
- [[harmonic-analysis]] - 并网谐波分析
- [[wideband-oscillation-stability]] - 宽频振荡与SSCO
- [[weak-grid-vsc]] - 弱电网稳定性分析
- [[fault-ride-through]] - 低电压穿越与故障穿越
- [[power-electronics]] - 电力电子变流器综述

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]] | 2023 | ATP/ATPDraw中GFL等效模型，故障电流误差2.33%，70%加速（Luchini） |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability]] | 2026 | RMS+模型捕捉PLL失稳，SCR<2时Hopf分岔，临界功率降40%（Carreño） |
| [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient]] | 2022 | 五模型精度-效率映射框架（SW/VI/AV/CCI/SCI），VI=SW的19%，AV=SW的1.5%，CCI=SW的0.20%（Sano） |
| [[advanced-dsogi-pll-with-adaptive-bandwidth-for-improved-transient-performance-of]] | 2024 | DSOGI-PLL带宽自适应，SCR稳定下限扩展至1.0（Ranasinghe） |
| [[dynamic-average-value-modeling-of-13&14]] | 2012 | VSC-HVDC动态平均值模型，5μs步长CPU减少50-54%，≥40μs步长减少60-70%（DAVM） |
| [[an-inverter-model-simulating-accurate-harmonics-with-low-computational-burden-fo]] | 2020 | 低计算负担的谐波逆变器模型（Luchini） |
| [[a-state-variable-preserving-method-for-the-efficient-modelling-of-inverter-based]] | 2025 | 保状态变量的IBR高效并行建模方法（Wang） |
| [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation]] | 2023 | Gaussian脉冲激励提取IBR DQ导纳模型（Fan & Miao） |