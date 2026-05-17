---
title: "动态相量法"
type: topic
tags: [动态相量, 移频仿真, 混合仿真, 多速率, 相量接口]
created: "2026-04-13"
updated: "2026-05-17"
---

# 动态相量法

## 定义

动态相量法（Dynamic Phasors，DP）是一种将时域信号表示为滑动时窗内时变傅里叶系数的建模与仿真方法。任意时域信号 $x(t)$ 可表示为：

$$x(t) = \mathbf{X}_k(t)\,e^{jk\omega_0 t} \quad (k = 0, \pm 1, \pm 2, \dots)$$

其中 $\mathbf{X}_k(t)$ 是第 $k$ 阶动态相量（时变傅里叶系数），$\omega_0$ 是基频（移频频率）。动态相量法既可作为设备建模方法（保留指定阶次谐波的慢变包络），也可作为 [[co-simulation|混合仿真]] 接口和 [[harmonic-analysis|谐波相量域]] 仿真的数学基础。

在 EMT 仿真体系中，动态相量法位于传统 EMT 详细时域仿真与传统相量/机电暂态模型之间——它保留目标频率分量的动态，同时避免逐周期求解全部开关波形，从而在精度与效率之间取得平衡。

## EMT 中的角色

### 与 EMT 和 TS 的比较

| 特性 | 电磁暂态 (EMT) | 动态相量 (DP) | 机电暂态 (TS) |
|------|---------------|--------------|--------------|
| 时间步长 | 1–50 µs | 50–500 µs | 5–20 ms |
| 开关细节 | 完整 | 包络近似 | 忽略 |
| 频率范围 | 宽频 | 基频+低阶谐波 | 工频 |
| 计算效率 | 低 | 中等 | 高 |
| 适用场景 | 换相暂态、故障分析 | 电力电子设备接口 | 机电振荡 |

动态相量法的核心价值在于**填补 EMT 与 TS 之间的精度-效率鸿沟**：当系统含高密度电力电子设备时，纯 EMT 仿真步长受开关频率限制（通常需 < 10 µs），而 TS 仿真无法捕捉开关暂态细节。动态相量通过保留 $k = 0, \pm 1$ 等关键阶次，使步长可扩展至 200–500 µs，同时保留基频动态特性。

### 应用定位

动态相量法在 EMT 体系中的典型应用包括：
- **设备动态相量建模**：对 MMC、VSC、SST、DAB 等换流器设备建立保留基波、直流及低阶谐波的等效模型
- **混合仿真接口**：作为 EMT 与 TS 之间的桥接协议（DPIM、Thevenin/Norton 等效），实现双向数据交换
- **宽频等值建模**：通过移频相量（SFA/SFEMT）将高频开关动态折叠到低频等效电路，突破 CFL 稳定性约束

## 数学基础

### 时变傅里叶表示

对于周期 $T$ 窗口内 $(t - T, t)$ 的信号 $x(t)$，其第 $k$ 阶动态相量定义为：

$$\mathbf{X}_k(t) = \frac{1}{T}\int_{t-T}^{t}x(\tau)\,e^{-jk\omega_0 \tau}\,d\tau$$

对应的时域重建公式为：

$$x(t) = \sum_{k=-\infty}^{+\infty} \mathbf{X}_k(t)\,e^{jk\omega_0 t}$$

工程中通常截断到有限阶次 $k = -K, \dots, +K$。

### 广义积分因子理论（Parvari 2026）

设 $x(t) = \mu(t)\mathbf{X}(t)$，其中 $\mu(t)$ 为任意无量纲信号。Parvari 等证明了变换不变量条件（KVL/KCL 在变换后仍成立），并导出广义的导数性质：

$$\frac{dx(t)}{dt} \longleftrightarrow \frac{d\mathbf{X}(t)}{dt} + s(t)\mathbf{X}(t)$$

其中 $s(t) = \frac{\mu'(t)}{\mu(t)}$ 是时变频率函数。当 $s(t) = j\omega_0$（常数）时，上式退化为经典动态相量导数公式。

### 导数性质

动态相量的核心优势在于将微分运算转化为代数运算。第 $k$ 阶动态相量的导数满足：

$$\left\langle \frac{dx}{dt} \right\rangle_k = \frac{d\mathbf{X}_k}{dt} + jk\omega_0 \mathbf{X}_k$$

即：时域微分 = 相量微分 + $jk\omega_0$ 频移项。当 $\frac{d\mathbf{X}_k}{dt} \approx 0$（准稳态）时，导数性质退化为经典相量的 $j\omega_0 \mathbf{X}$ 关系。

### 乘法性质与dq序列分解

动态相量的乘法性质（Zhu 2025）使得对称分量与 Park 变换后的dq坐标系可以直接构建状态方程。对于三相不平衡系统，dq序列动态相量满足：

$$\mathbf{X}_{dqk} = \mathbf{A}^{-1}\mathbf{T}(\theta)^{-1}\mathbf{X}_{abck}$$

其中 $\mathbf{T}(\theta)$ 为 Park 变换矩阵，$\mathbf{A}$ 为对称分量变换矩阵。$k$ 阶正序分量在 dq 坐标系中对应 $(k+1)$ 阶谐波分量。

## 形式化表达

### 基本动态相量变换

时域信号与动态相量的对应关系：

$$x(t) = \mathbf{X}_k(t)\,e^{jk\omega_0 t} \longleftrightarrow \mathbf{X}_k(t) = \frac{1}{T}\int_{t-T}^{t}x(\tau)\,e^{-jk\omega_0 \tau}\,d\tau$$

### 元件伴随电路（Companion Circuit）

动态相量模型在 EMT 求解器中通过伴随电路实现。各类元件的伴随电路模型（Parvari 2026）如下：

**电阻**（阻值不变）：

$$v(t) = Ri(t) \longleftrightarrow \mathbf{V}(t) = R\mathbf{I}(t)$$

**电感**（引入时变串联电阻 $Ls(t)$）：

$$v(t) = L\frac{di}{dt} \longleftrightarrow \mathbf{V}(t) = L\frac{d\mathbf{I}}{dt} + Ls(t)\mathbf{I}(t)$$

**电容**（引入时变并联电导 $Cs(t)$）：

$$i(t) = C\frac{dv}{dt} \longleftrightarrow \mathbf{I}(t) = C\frac{d\mathbf{V}}{dt} + Cs(t)\mathbf{V}(t)$$

### 离散化伴随电路

采用梯形积分法（第 $n$ 个时间步）：

$$i_L^{n+1} = \frac{1}{Z_L}\left[v_L^{n+1} + \frac{L}{\Delta t}i_L^n + v_L^n\right],\quad Z_L = \frac{2L}{\Delta t} + j\omega_0 L$$

其中 $Z_L$ 是动态相量电感的等效阻抗，$\Delta t$ 是仿真步长。表1给出各元件的离散化伴随电路参数。

**表1：离散化伴随电路参数**

| 元件 | $g$ | $k_I$ | $k_V$ |
|------|-----|-------|-------|
| 电阻 $R$ | $\frac{\Delta t}{2L}$ | $0$ | $0$ |
| 电感 $L$ | $\frac{j\omega_0\Delta t}{2}$ | $\frac{1 - j\omega_0\Delta t/2}{1 + j\omega_0\Delta t/2}$ | $\frac{\Delta t}{2L}$ |
| 电容 $C$ | $\frac{2C}{\Delta t}$ | $1$ | $0$ |

### 同步电机动态相量模型

同步电机的 dq0 域动态方程（Hassani 2022）需转换为动态相量形式。d轴电压方程：

$$v_d = -\frac{X''_d}{\omega_s}\frac{di_d}{dt} + \frac{1}{\omega_s}\frac{dE''_q}{dt} + \frac{\omega_r}{\omega_s}(X''_q - X'_q)i_q + E''_d - R_a i_d$$

对应的动态相量形式需要将 $\frac{d}{dt}$ 替换为 $\frac{d}{dt} + j\omega_0$。Park 变换矩阵：

$$\mathbf{T}(\theta) = \begin{bmatrix} \cos\theta & \cos(\theta - \frac{2\pi}{3}) & \cos(\theta + \frac{2\pi}{3}) \\ -\sin\theta & -\sin(\theta - \frac{2\pi}{3}) & -\sin(\theta + \frac{2\pi}{3}) \\ \frac{1}{2} & \frac{1}{2} & \frac{1}{2} \end{bmatrix}$$

对称分量与 dq 坐标的变换关系（$k$ 阶正序产生 dq 轴 $(k+1)$ 阶谐波）：

$$\begin{bmatrix} \mathbf{X}_{dk} \\ \mathbf{X}_{qk} \end{bmatrix} = \begin{bmatrix} je^{-j\delta} & -je^{j\delta} & 0 \\ e^{-j\delta} & e^{j\delta} & 0 \end{bmatrix}\begin{bmatrix} \mathbf{X}_{pk+1} \\ \mathbf{X}_{nk-1} \\ \mathbf{X}_{zk} \end{bmatrix}$$

## 分类与机制

### 按应用领域分类

**A. 设备动态相量模型**

保留设备特定频段分量的等效电路模型：
- **基频动态相量**：仅保留 $k = \pm 1$（工频基波），适用于 HVDC、SVC 等工频主导设备
- **多频段动态相量**：保留 $k = 0, \pm 1, \pm 2, \dots$（直流+基波+谐波），适用于 MMC 等高频谐波丰富的设备
- **谐波相量域（HPD）**：通过移频将高频开关动态折叠到低阶谐波，同时输出瞬时波形与谐波相量

**B. 接口动态相量模型**

EMT 与 TS/PQ 域之间的桥接协议：
- **动态相量接口模型（DPIM）**：基于 Thevenin/Norton 等效的双向缓冲接口
- **松弛迭代接口**：通过多端口等效与边界变量预测加速迭代收敛
- **模式切换接口**：支持纯 EMT 与混合 EMT-TS 动态切换

**C. 移频/谐波相量扩展**

突破基频约束的宽频建模方法：
- **移频分析（SFA）**：将系统特征频率偏移至零频，解除 CFL 稳定性约束
- **谐波相量域协同仿真（HPD-EMT）**：直流侧用 HPD、交流侧用 EMT，通过 HPD-TLM 接口解耦
- **多域协同仿真**：直流用 SFP、交流用 EMT，通过 HMD-TLM 接口实现跨域交互

### 按接口机制分类

| 接口类型 | 耦合强度 | 变量域 | 等值形式 |
|---------|---------|--------|---------|
| DPIM | 强 | 瞬时↔相量 | Thevenin/Norton |
| 松弛迭代 | 可调 | 瞬时↔相量 | 多端口等效 |
| 缓冲接口 | 弱 | 相量↔相量 | 诺顿等效 |
| SFA-EMT | 强 | 复数↔实部 | 双并行 EMT |

## EMT 建模方法

### 方法1：基频动态相量（DPDP）

**原理**：仅保留 $k = \pm 1$ 两个分量，将系统表示为工频等效电路：

$$\mathbf{X}(t) = \mathbf{X}_{+1}(t)\,e^{j\omega_0 t} + \mathbf{X}_{-1}(t)\,e^{-j\omega_0 t}$$

**伴随电路**：电感变为 $L$ 与 $j\omega_0 L$ 串联，电容变为 $C$ 与 $j\omega_0 C$ 并联。

**步长约束**：满足 $\Delta t_{DP} \ll \frac{1}{(n+1)\omega_0}$（$n$ 为最高谐波阶次），60 Hz 系统 13 次谐波时 $\Delta t \ll 189\,\mu s$（Parvari 2026）。

**量化性能**：Hassani 2022 在 IEEE-118 基准上测得 DP 与 TD 在同一步长下的精度基本一致，但大步长下 DP 的特征根偏移会导致暂态精度衰减。

### 方法2：广义状态空间平均法（GSSA）

**原理**：对周期信号的多个傅里叶系数同步建模，适用于多谐波设备：

$$\mathbf{X}(t) = \begin{bmatrix} \mathbf{X}_0 \\ \mathbf{X}_{+1} \\ \mathbf{X}_{-1} \\ \vdots \end{bmatrix}$$

**状态方程**：

$$\frac{d\mathbf{X}_k}{dt} = \frac{d}{dt}\langle x(t) \rangle_k = -jk\omega_0 \mathbf{X}_k + \langle \frac{dx}{dt} \rangle_k$$

**量化性能**：Shu 2019 报告 DAB 变换器用 GSSA（$k = 0, \pm 1$）在 100 µs 步长下精度损失 < 2%，相比详细开关模型加速约 8 倍。

### 方法3：移频分析（SFA）

**原理**：将系统特征频率 $\omega_c$ 偏移至 DC 附近，解除 CFL 约束使大步长稳定：

$$x(t) = \tilde{x}(t)\,e^{j\omega_c t} \longleftrightarrow \tilde{x}(t) = x(t)\,e^{-j\omega_c t}$$

**大步长可行性**：SFA 在 $\Delta t = 1\,$ms 时仍保持稳定（Zhou & Dinavahi 2014），而标准 EMT 在 $\Delta t > 50\,$µs 即失稳。

**量化性能**：Zhang 2024 报告 SFA + GPU 并行在 IEEE-39 节点系统上实现超实时仿真（$10\times$ 实时）。

### 方法4：动态相量接口模型（DPIM）

**原理**：在 EMT-TS 边界处建立双向缓冲机制，EMT 侧以诺顿等效注入相量电流，TS 侧以戴维南等效接收：

**接口方程**：

$$\mathbf{I}_{DP} = \sum_{k \in K} \mathbf{I}_k\,e^{jk\omega_0 t} \longleftrightarrow \text{EMT 诺顿等效}$$

**收敛性**：Shu 等（2017）证明 DPIM 在强扰动下可将接口波形失真降低 85%，迭代次数减少 60%。

### 方法5：多速率动态相量（Multirate DP）

**原理**：快慢子系统分别用 EMT 和 DP 建模，通过插值/平均机制交换数据：

$$\mathbf{X}_{slow}^{n+1} = \frac{1}{M}\sum_{m=0}^{M-1}\mathbf{X}_{fast}^{nM+m},\quad M = \frac{\Delta t_{slow}}{\Delta t_{fast}}$$

**量化性能**：Multirate Method（2026）在 10000 节点系统上将计算时间缩短 85%，同时保留 0.05 pu 精度。

### 方法6：谐波相量域（HPD）协同仿真

**原理**：将开关函数展开为傅里叶级数，将高频动态折叠到低阶谐波：

$$s(t) = \sum_{h} \mathbf{S}_h\,e^{jh\omega_s t} \Longrightarrow \begin{cases} \text{直流侧：} \mathbf{V}_{dc} = \sum_h \mathbf{V}_h\,e^{jh\omega_s t} \\ \text{交流侧：} v(t) = \sum_h \mathbf{V}_h\,e^{jh\omega_s t} \end{cases}$$

**HPD-TLM 接口**：实现 EMT 交流侧与 HPD 直流侧的高效解耦，支持瞬时波形与谐波相量同步输出（Shu 2019）。

## 关键技术挑战

### 挑战1：步长约束与特征根偏移

动态相量法引入的步长约束来自两方面：

**(a) 谐波截断约束**：当 $\omega_{sh} = \omega_0$ 时，最高开关谐波频率 $n\omega_0$ 决定步长上限：

$$\Delta t_{DP} \ll \frac{1}{(n+1)\omega_0}$$

**(b) 特征根偏移**：DP 变换将系统固有特征根 $\lambda$ 偏移为 $\lambda - jk\omega_0$，这可能导致原本稳定的特征根移入右半平面。Parvari 2026 证明：当且仅当系统阻尼充分（关键自然频率的暂态在开关周期内衰减完毕）时，大步长 DP 仿真才可保证精度。

**判据**：$|\text{Re}(\lambda)| \gg \omega_0$（高阻尼）或 $\Delta t \cdot |\text{Im}(\lambda)| \ll 1$（步长远小于振荡周期）。

### 挑战2：截断阶数选择

动态相量需在计算效率与精度之间选择保留的谐波阶数 $K$：
- $K = 0$（直流）仅适用于准稳态
- $K = 1$（基波）在暂态起始时刻误差最大（因为 $d\mathbf{X}_k/dt \neq 0$）
- $K \geq 2$ 适用于 MMC 等谐波丰富的设备，但计算量随之增加

**工程经验**：对于 12 脉动 LCC，$K = 3$（保留 11、13 次特征谐波）可覆盖 95% 的换相暂态能量；对于 MMC，$K \geq 5$ 才能准确捕捉子模块电容电压波动。

### 挑战3：初始化与稳态初值

动态相量的初值问题比 EMT 复杂：
- EMT 可通过"开路/短路法"直接计算稳态初值
- DP 需在傅里叶积分窗口内等待信号完成一个基频周期才能获得精确相量

**解法**：Zanon 2021 提出基于移相子迭代的初始化预热技术，通过 3–5 个基频周期的预仿真建立相量初值。

### 挑战4：接口映射误差

EMT ↔ DP 接口处的瞬时值与相量值映射存在量化误差：
- **采样同步误差**：窗口滑动导致的相位延迟（$\leq T/2$）
- **谐波混叠**：高频分量折叠到低阶谐波产生的伪影
- **零序/负序处理**：不对称故障时零序分量需特殊处理

**缓解方法**：Rupasinghe 2021 比较了五种相量提取算法（FFT、滑动 DFT、正交滤波器、插值 DFT、线性中点插值），建议对含强暂态的场景采用插值 DFT 或线性中点插值以减少同步误差。

### 挑战5：电力电子开关暂态

对于换流器开关动作，DP 的"阶梯波"特性会产生非物理的伪纹波：
- **纹波频率**：$N f_0$（$N$ 为开关频率比）
- **纹波幅值**：与截断阶数 $K$ 成反比

**Parvari 2026 示例**：当 $N = 200, f_0 = 60\,$Hz 时，纹波周期为 $83\,\mu$s，要求 $\Delta t \ll 83\,\mu$s——这与 EMT 的约束已无显著差异，说明 DP 在高频开关场景下的优势会消失。

## 量化性能边界

### 效率对比

| 场景 | 方法 | 步长 | 加速比 | 精度 |
|------|------|------|--------|------|
| IEEE-118 基准（Hassani 2022） | TD (EMT) | 50 µs | 基准 | 基准 |
| IEEE-118 基准（Hassani 2022） | DP | 500 µs | ~10× | 略低（暂态） |
| 9 节点 + SVC（E Zhijun 2009） | DP-TSP 混合 | 500 µs | 17× vs EMT 50 µs | 一致 |
| MMC 400 SM/桥臂（未经同行评审） | DP | 同步 | 8× vs 详细 EMT | 可比 |
| IEEE-39 + SFA（Zhang 2024） | SFA + GPU | 1 ms | 10× 实时 | 可比 |

### 精度边界

| 场景 | 步长 | DP 误差 | EMT 误差 | 结论 |
|------|------|---------|----------|------|
| 稳态运行 | 任意 | ≈ 0 | ≈ 0 | DP 精确 |
| 暂态故障 | 500 µs | < 5% | < 1% | DP 可接受 |
| 开关换相 | 100 µs | < 2% | < 0.5% | DP 精确 |
| 大频偏 | 500 µs | > 15% | < 5% | DP 失效 |

**Parvari 2026 核心发现**：DP 的计算优势并非无条件成立——当系统阻尼不足或特征根偏移导致稳定性边界收缩时，DP 大步长仿真的精度会显著劣化。原文未报告可核验的精确数值，但给出了定性判据。

### 选择决策表

| 场景 | 推荐方法 | 步长建议 |
|------|---------|---------|
| 大规模电网机电振荡 | DP 或 3pPD | 500 µs – 1 ms |
| 含 MMC/HVDC 的暂态 | DP + 接口 | 100 – 200 µs |
| 故障分析（< 1 kHz） | EMT | 10 – 50 µs |
| 开关换相细节 | EMT | 1 – 10 µs |
| 谐波阻抗扫描 | DP (~$k = \pm 11, \pm 13$) | 100 µs |
| 实时仿真（超实时） | SFA | 200 µs – 1 ms |
| 宽频稳定性分析 | DP + 阻抗法 | 50 – 100 µs |

## 适用边界与选择指南

### DP 适用条件

1. **频谱可压缩**：目标动态集中在基频 ± 低阶谐波（$k \leq 5$）
2. **阻尼充分**：系统固有频率的衰减时间常数 $\tau \ll T$（$\leq 1$ 个基频周期）
3. **开关频率已知**：换流器载波比 $N$ 明确，可计算步长上界
4. **接口协议明确**：EMT-TS 接口处需预定义 DP 缓冲机制

### DP 失效场景

1. **频谱宽展**：故障导致系统频率大范围偏移（$|\Delta f| > 5\,$Hz）
2. **强非周期暂态**：直流偏置、故障电流衰减导致 $\mathbf{X}_k(t)$ 快速变化
3. **高频谐振**：$k \geq 20$ 的开关谐波主导（如SiC器件驱动的快速瞬态）
4. **多频段耦合**：风场、光伏的间谐波（$0.1\!-\!0.5\,$Hz）与基频动态强耦合

### 与其他方法的比较

- **vs [[state-space-method|状态空间法]]**：SSM 在相量域建模时与 DP 本质等价，但 SSM 更适合控制器设计而 DP 更适合接口协议
- **vs [[average-value-model|平均值模型]]**：AVM 是 DP 的特殊形式（仅 $k = 0$），不保留谐波动态
- **vs [[multirate-method|多速率方法]]**：多速率 DP 是 DP 的实现框架而非替代方法
- **vs [[frequency-dependent-modeling|频率相关建模]]**：FDM 面向阻抗频率扫描，DP 面向时域暂态

## 相关方法

- [[numerical-integration|数值积分]] - 动态相量频率匹配积分
- [[state-space-method|状态空间法]] - 相量域状态空间建模
- [[average-value-model|平均值模型]] - 开关周期平均化
- [[multirate-method|多速率方法]] - 相量-时域多速率接口
- [[co-simulation|混合仿真]] - 动态相量接口
- [[harmonic-analysis|谐波分析]] - 谐波相量域 (HPD) 建模
- [[frequency-dependent-modeling|频率相关建模]] - 宽频移频相量

## 相关模型

- [[mmc-model|MMC模型]] - MMC 动态相量建模
- [[vsc-model|VSC模型]] - VSC 动态相量简化
- [[lcc-model|LCC模型]] - LCC 动态相量换相失败分析
- [[transformer-model|变压器模型]] - 变压器相量域建模
- [[transmission-line-model|输电线路模型]] - 线路相量域接口

## 相关主题

- [[harmonic-analysis|谐波分析]] - 谐波相量域（HPD）建模
- [[frequency-dependent-modeling|频率相关建模]] - 宽频移频相量
- [[co-simulation|混合仿真]] - 动态相量接口
- [[real-time-simulation|实时仿真]] - 动态相量实时实现
- [[electromechanical-electromagnetic-hybrid-simulation|机电-电磁混合仿真]] - TS-EMT 相量接口

## 来源论文

- [[revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits|Parvari 等 2026]] - 动态相量理论基础与步长约束分析
- [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients|Hassani 等 2022]] - IEEE-118 基准 DP vs TD 系统对比
- [[assessment-of-dynamic-phasor-extraction-methods-for-power-system-co-simulation-a|Rupasinghe 等 2021]] - 五种相量提取算法比较
- [[a-multi-domain-co-simulation-method-for-comprehensive-shifted-frequency-phasor-d|Shu 等 2019]] - 多域协同仿真与 HMD-TLM 接口
- [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Dey 等 2021]] - TCSC 动态相量 vs 离散时间 vs 频率扫描对比
- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model|E Zhijun 等 2009]] - SVC 动态相量混合仿真接口
- [[shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste|Zhang 等 2024]] - SFA + GPU 超实时仿真
- [[multirate-method-for-dynamic-phasor-simulation-of-large-scale-power-systems|Multirate Method 2026]] - 大规模系统多速率 DP 仿真
- [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Mudunkotuwa 和 Filizadeh 2018]] - EMT-DP 协同仿真接口算法