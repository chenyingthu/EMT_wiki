---
title: "时域有限差分法 (FDTD)"
type: method
tags: [fdtd, finite-difference, electromagnetic, full-wave, yee-grid, numerical-method]
created: "2026-05-02"
updated: "2026-05-15"
---

# 时域有限差分法 (FDTD)

## 定义

时域有限差分法（Finite-Difference Time-Domain, FDTD）是由 Kane Yee 于 1966 年提出的数值计算方法，通过在空间立方体网格和时间轴上交替离散 Maxwell 旋度方程，直接推进电磁场的时域演化。与其他 EMT 数值方法不同，FDTD 以**全波电磁场求解**为核心，不依赖预先定义的传输线等值电路或模态解耦，因而能够捕捉完整的三维辐射、耦合和散射效应。

FDTD 在 EMT 体系中的定位是**高频场求解器**：当电磁波频率高到使集总参数模型失效（如 GIS 超快暂态 VFT 达 100+ MHz、雷电波前 < 1 μs、电缆局部放电 ns 级暂态），或研究对象的几何结构复杂到无法简化为一维传输线时，FDTD 提供可直接求解 Maxwell 方程的路径。同时，FDTD 的计算结果可降维提取为端口阻抗或等效源，作为 EMT 集总电路模型的输入。

FDTD 与 [[finite-element-method]] 的核心区别在于：FDTD 在规则/分段规则笛卡尔网格上显式推进，无需组装大型稀疏矩阵，内存需求与网格点数近似线性相关；FEM 从弱变分形式出发，在任意非结构化四面体网格上离散，适合复杂曲面和材料非线性，但每次时间步需求解线性代数方程组。两者在 EMT 场景下互补：FDTD 适合规则结构的高频传播问题（母线、接地极、雷电通道），FEM 适合变压器铁芯、绝缘子几何精细化等复杂几何问题。

## EMT 中的角色

FDTD 在 EMT 知识体系中的核心价值在于**填补集总参数模型与全波电磁场模型之间的空白**，具体应用场景包括：

**雷电暂态分析**：当雷电流波前时间 ≤ 1 μs 或雷击点距离线路 < 100 m 时，雷电波的垂直电场分量和水平磁场分量对输电线路上感应电压的影响无法用简单的感应系数模型描述。FDTD 在二维/三维网格中直接计算雷电电磁场对多导体线路的耦合，提供从电磁场到线路电压的完整物理图像（De Conti 2020）。

**GIS/VFT 超快暂态**：气体绝缘变电站中隔离开关操作产生的超快暂态（VFT/VFTO）频率范围为 1–140 MHz（Ametani 2018）。在如此高频下，主回路导体与金属外壳之间的波传播模式介于传输线与辐射场之间；EMTP 的传输线模型需要"适当建模"（理想大地假设 + 同轴模参数 + 分支等效电容）才能与 FDTD 结果一致。FDTD 可用于校验 EMTP 建模假设的有效边界。

**杆塔接地系统冲击阻抗**：传统接地分析将接地极视为集中参数，但雷击瞬间接地极周围土壤电离形成扩展的等离子体通道，等效半径随电流峰值变化。FDTD 在时域中直接模拟接地极的冲击电离过程，与传输线理论（TL）结合形成 FDTD-TL 混合方法，可考察接地极有效长度、冲击阻抗和地电位升（GPR）的频变特性（Duarte 2025）。

**传输线理论适用范围验证**：传输线理论（Telegraph Equation）在何频率下仍然有效是 EMT 建模的基本问题。FDTD 作为"第一性原理"全波求解器，其计算结果可作为基准，用于评估 [[quasi-tem-approximation]] 在给定频率和几何条件下的误差上界（见 Noda 2004 关于阶梯近似的误差分析）。

## 核心机制

### Maxwell 旋度方程的时域形式

在各向同性线性介质中，FDTD 求解以下时域 Maxwell 旋度方程：

$$\nabla \times \mathbf{E} = -\mu \frac{\partial \mathbf{H}}{\partial t} \tag{1}$$

$$\nabla \times \mathbf{H} = \sigma \mathbf{E} + \varepsilon \frac{\partial \mathbf{E}}{\partial t} + \mathbf{J}_{\text{ext}} \tag{2}$$

其中 $\mathbf{E}$ 为电场强度（V/m），$\mathbf{H}$ 为磁场强度（A/m），$\mu$ 为磁导率（H/m），$\varepsilon$ 为介电常数（F/m），$\sigma$ 为电导率（S/m），$\mathbf{J}_{\text{ext}}$ 为外部激励电流密度（A/m²）。

对于非磁性土壤介质，$\mu = \mu_0 = 4\pi \times 10^{-7}$ H/m；电导率 $\sigma$ 和介电常数 $\varepsilon$ 可以是频率相关的（频变土壤模型），通过递归卷积或辅助微分方程（ADE）方法在时域中处理。

### Yee 网格与蛙跳格式

Yee 网格的核心思想是将电场分量和磁场分量在空间和时间上交替放置，利用它们之间的旋度关系实现显式时间推进：

- 电场分量 $\mathbf{E}$ 放置在网格棱边（edge）上，时间步为 $n$
- 磁场分量 $\mathbf{H}$ 放置在网格面心（face）上，时间步为 $n + 1/2$
- 电场和磁场在时间上交错半步（$\Delta t / 2$），在空间上交错 $\Delta x / 2$、$\Delta y / 2$、$\Delta z / 2$

以三维直角网格中 $E_x$ 分量为例，将旋度方程的 $x$ 分量展开：

$$\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} - \sigma E_x - J_{\text{ext},x}\right) \tag{3}$$

在交错时空网格中，离散化为（蛙跳格式，leapfrog scheme）：

$$E_x^{n+1}(i,j,k) = C_a E_x^n(i,j,k) + C_b \frac{H_z^{n+1/2}(i,j+1,k) - H_z^{n+1/2}(i,j-1,k)}{2\Delta y} - C_b \frac{H_y^{n+1/2}(i,j,k+1) - H_y^{n+1/2}(i,j,k-1)}{2\Delta z} - C_j J_{\text{ext},x}^{n+1/2}(i,j,k) \tag{4}$$

其中更新系数为：

$$C_a = \frac{2\varepsilon - \sigma\Delta t}{2\varepsilon + \sigma\Delta t}, \quad C_b = \frac{2\Delta t}{2\varepsilon + \sigma\Delta t}, \quad C_j = \frac{2\Delta t}{2\varepsilon + \sigma\Delta t} \tag{5}$$

磁场分量 $H_y$ 和 $H_z$ 用类似的中心差分格式更新，旋度方程中的空间导数自然地在交错网格上实现。"蛙跳"名称来源于：先利用 $n$ 时刻的 $\mathbf{E}$ 和 $n-1/2$ 时刻的 $\mathbf{H}$ 更新 $n+1/2$ 时刻的 $\mathbf{H}$，再利用 $n+1/2$ 时刻的 $\mathbf{H}$ 和 $n$ 时刻的 $\mathbf{E}$ 更新 $n+1$ 时刻的 $\mathbf{E}$——电场和磁场像两只青蛙交替跳跃。

### Courant-Friedrichs-Lewy（CFL）稳定性条件

FDTD 作为显式格式，时间步长 $\Delta t$ 必须小于某个临界值以防止数值不稳定。对于三维均匀网格，临界时间步由 Courant 条件决定：

$$\Delta t \leq \Delta t_{\max} = \frac{1}{c\sqrt{(\Delta x)^{-2} + (\Delta y)^{-2} + (\Delta z)^{-2}}} \tag{6}$$

其中 $c = 1/\sqrt{\mu\varepsilon}$ 为介质中的光速。若不满足 (6)，数值解将以指数方式发散（即使物理系统本身是稳定的）。工程中通常取 $\Delta t = 0.9 \Delta t_{\max}$ 以留出安全裕度。

** CFL 条件的物理含义**：时间步必须小于电磁波跨过最小网格单元所需的物理飞行时间（flight time）。因此，最小网格尺寸 $\min(\Delta x, \Delta y, \Delta z)$ 直接决定了全局时间步上限——局部细小结构（如土壤电离通道半径 ~ mm 级、电缆绝缘层厚度 ~ μm 级）会显著增加全局计算量。

### 数值色散

即使满足 CFL 条件，FDTD 离散化仍会产生数值色散——不同频率和传播方向的波具有不同的数值相速度，与物理相速度 $c$ 存在偏差。以一维 FDTD 为例，数值色散关系为：

$$\frac{\tan(\omega \Delta t / 2)}{\omega \Delta t / 2} = \frac{\sin(k\Delta x / 2)}{k\Delta x / 2} \tag{7}$$

当 $\Delta x \to 0$ 时，左侧趋于 1，数值解趋于物理解；当 $\Delta x$ 相对波长 $\lambda$ 不可忽略时，数值相速度偏离 $c$。工程中通常要求每个波长至少包含 10–20 个网格点（$\Delta x \leq \lambda/20$），以将数值色散误差控制在可接受范围（< 1%）。

对于非均匀网格或各向异性介质，数值色散更加复杂。不同传播方向（相对网格轴线角度）具有不同的数值相速度，导致波形畸变——尤其是斜入射波和面波。

### 吸收边界条件与 PML

FDTD 计算域必须截断到有限大小。在开放问题（如雷电场对线路的耦合）中，截断边界代表无限空间，需要设计吸收入边界的数值边界以避免来自截断边界的反射。

**完美匹配层（PML）** 是最常用的方案，由 Berenger 于 1994 年提出。其核心思想是在截断边界处设置一层阻抗匹配但具有复阻抗的"有耗介质"，使进入 PML 层的电磁波以指数方式衰减，无论其入射角和频率如何。

PML 可通过将 Maxwell 方程在分裂域形式（split-field）中进行修改来实现，或等效地引入复频域拉伸（Complex Frequency Shifted, CFS）坐标变换。将 PML 层中的 $x$ 方向设置为有耗介质，其本构参数修改为：

$$\tilde{\varepsilon}_x = \varepsilon \cdot \frac{s_y s_z}{s_x}, \quad \tilde{\mu}_x = \mu \cdot \frac{s_y s_z}{s_x} \tag{8}$$

其中 $s_x = \kappa_x + \sigma_x / (\alpha_x + j\omega\varepsilon_0)$ 为复频率拉伸因子。在实际实现中，推荐使用 CFS-PML 变体，其对低频入射波和掠入射波具有更好的吸收效果。

## EMT 建模方法

FDTD 在 EMT 建模体系中的独特价值在于它能直接耦合外部电磁场激励源（如雷电电磁场）到多导体传输线系统，形成**相域 FDTD-传输线混合方法**（De Conti 2020）。

### 外部电磁场耦合方程

考虑外部电磁场（雷电电磁脉冲 EMP）照射下的多导体线路，耦合机制可通过以下耦合电报方程描述：

$$\frac{\partial \mathbf{V}_s(x,t)}{\partial x} + \mathbf{L}_e \frac{\partial \mathbf{I}(x,t)}{\partial t} + \boldsymbol{\zeta}(t) * \frac{\partial \mathbf{I}(x,t)}{\partial t} = \mathbf{E}_x^i(x,t) \tag{9}$$

$$\frac{\partial \mathbf{I}(x,t)}{\partial x} + \mathbf{G}\mathbf{V}_s(x,t) + \mathbf{C} \frac{\partial \mathbf{V}_s(x,t)}{\partial t} = 0 \tag{10}$$

其中 $\mathbf{V}_s$ 为散射电压向量，$\mathbf{I}$ 为电流向量，$\mathbf{L}_e$ 为外部电感矩阵，$\boldsymbol{\zeta}(t)$ 为导体内部阻抗的时域卷积核（通过矢量拟合从频域变换得到），$\mathbf{E}_x^i$ 为入射电场的水平分量作为分布电压源。总电压 $\mathbf{v}(x,t) = \mathbf{V}_s(x,t) + \mathbf{V}_i(x,t)$，其中入射电压 $\mathbf{V}_i(x,t)$ 由垂直电场分量积分得到：

$$\mathbf{V}_i(x,t) \approx -h \mathbf{E}_z^i(x, z=0, t) \tag{11}$$

其中 $h$ 为导体高度对角矩阵，$\mathbf{E}_z^i$ 为入射电场的垂直分量。

在 FDTD 数值实现中，(9) 和 (10) 直接在相域中求解，不需要模态变换（De Conti 2020 的 FDTD 相域解法作为基准），避免了模态参数拟合误差。

### 频变土壤模型的 FDTD 处理

雷电暂态分析中，土壤电阻率在宽频带内变化（从直流 ~ 1000 Ω·m 到高频 ~ 100 Ω·m），土壤导纳 $Y(\omega)$ 和导体内部阻抗 $Z_i(\omega)$ 均为频率相关函数。在 FDTD 时域求解中，这些频变特性通过以下流程处理（基于 Duarte 2025 的 FDTD-TL 方法）：

**步骤 1**：获取土壤复导纳 $\kappa(j\omega) = \sigma_{DC} + j\omega\varepsilon'_\infty + \sum_{j=1}^{N} \frac{r_j}{j\omega - p_j}$（Alipio-Visacro 频变土壤模型），通过矢量拟合（Vector Fitting）将 $N$ 阶极点-留数形式提取为 $(p_j, r_j)$。

**步骤 2**：对每个极点的复指数核进行逆拉普拉斯变换，得到时域卷积核 $\eta_g(t) = \sum_j r_j e^{p_j t}$。在 FDTD 时间推进中，卷积历史通过引入辅助变量 $\psi_{k,j}$ 进行递推更新，避免存储完整历史波形（递归卷积算法）。

**步骤 3**：将递归卷积项并入 FDTD 蛙跳格式，在每个时间步更新电压和电流时同步更新辅助变量。递归卷积的内存需求与时间步数无关（仅需存储 $N$ 个辅助变量），使大规模时域仿真成为可能。

### FDTD 与 EMTP 传输线模型的接口

FDTD 计算的端口电压/电流可按以下方式嵌入 EMTP 集总电路模型：

**端口等值法**：在 FDTD 端口平面处，将三维电磁场计算结果等效为诺顿/戴维南电路参数。给定端口参考阻抗 $Z_{c,ij}$，端口电压 $V_{ij}^{FDTD}$ 和端口电流 $I_{ij}^{FDTD}$ 直接作为 EMTP 节点方程的激励源。

**等效源注入法**：在 EMTP 的传输线支路两端注入 FDTD 计算得到的分布源项（9）中的水平电场积分项 $u_k(t) = -\int_0^\ell \mathbf{a}(x,t) * \mathbf{E}_x^i(x,t)dx$，使 EMTP 传输线模型能够考虑外部电磁场耦合而不需要改变 EMTP 本身的数值求解器。

**校验式接口**：FDTD 计算结果用于评估 EMTP 传输线模型的精度上限。例如，当 EMTP 传输线模型（Marti 模型）与 FDTD 的偏差 > 5% 时，说明在当前频率/几何条件下传输线近似失效，需要使用更精细的模型。

## 形式化表达

### FDTD 更新方程（笛卡尔网格，一阶蛙跳）

**磁场更新**（$n \to n+1/2$）：

$$H_x^{n+1/2}(i,j,k) = H_x^{n-1/2}(i,j,k) + \frac{\Delta t}{\mu}\left[\frac{E_y^{n}(i,j,k+1) - E_y^{n}(i,j,k-1)}{2\Delta z} - \frac{E_z^{n}(i,j+1,k) - E_z^{n}(i,j-1,k)}{2\Delta y}\right] \tag{12}$$

$$H_y^{n+1/2}(i,j,k) = H_y^{n-1/2}(i,j,k) + \frac{\Delta t}{\mu}\left[\frac{E_z^{n}(i+1,j,k) - E_z^{n}(i-1,j,k)}{2\Delta x} - \frac{E_x^{n}(i,j,k+1) - E_x^{n}(i,j,k-1)}{2\Delta z}\right] \tag{13}$$

$$H_z^{n+1/2}(i,j,k) = H_z^{n-1/2}(i,j,k) + \frac{\Delta t}{\mu}\left[\frac{E_x^{n}(i,j+1,k) - E_x^{n}(i,j-1,k)}{2\Delta y} - \frac{E_y^{n}(i+1,j,k) - E_y^{n}(i-1,j,k)}{2\Delta x}\right] \tag{14}$$

**电场更新**（$n+1/2 \to n+1$）：

$$E_x^{n+1}(i,j,k) = C_a E_x^{n}(i,j,k) + \frac{C_b}{\varepsilon}\left[\frac{H_z^{n+1/2}(i,j+1,k) - H_z^{n+1/2}(i,j-1,k)}{2\Delta y} - \frac{H_y^{n+1/2}(i,j,k+1) - H_y^{n+1/2}(i,j,k-1)}{2\Delta z} - J_{\text{ext},x}^{n+1/2}\right] \tag{15}$$

其余分量 $E_y, E_z$ 类似。

### CFL 稳定性条件

$$\Delta t \leq \frac{1}{c\sqrt{(\Delta x)^{-2} + (\Delta y)^{-2} + (\Delta z)^{-2}}} \tag{16}$$

### PML 复频率拉伸因子

$$s_x = \kappa_x + \frac{\sigma_x}{\alpha_x + j\omega\varepsilon_0}, \quad s_y = \kappa_y + \frac{\sigma_y}{\alpha_y + j\omega\varepsilon_0}, \quad s_z = \kappa_z + \frac{\sigma_z}{\alpha_z + j\omega\varepsilon_0} \tag{17}$$

### 频变土壤递归卷积核

$$\kappa(s) = \sigma_{DC} + s\varepsilon'_\infty + s\sum_{j=1}^{N}\frac{r_j}{s - p_j} \implies \eta_g(t) = \sum_{j=1}^{N} r_j e^{p_j t} \tag{18}$$

### 外部场耦合电压源

$$u_k(t) = -\int_0^\ell \mathbf{a}(x,t) * \mathbf{E}_x^i(x,t)dx - h\mathbf{E}_{z,k}^i(t) + \mathbf{a}(t) * h\mathbf{E}_{z,m}^i(t) \tag{19}$$

## 关键技术挑战

### 几何近似误差（阶梯效应）

三维复杂几何结构在笛卡尔网格上只能以阶梯（staircase）方式近似。对于倾斜导体、弯曲导体或曲面结构，阶梯近似引入等效的额外电容和电感，导致数值相速度偏差（Noda 2004 给出倾斜导线阶梯近似的误差量化：误差与倾斜角度和网格密度相关，当倾斜角 < 15° 且 $\Delta x \leq \lambda/40$ 时误差 < 2%）。

**应对策略**：对于可以解析参数化的几何结构（如圆柱导体、球形接地极），可使用亚网格技术（subgridding）在局部加密网格，同时保持全局 CFL 稳定性。对于复杂不可简化几何，建议使用非均匀网格过渡到细密区域，并在过渡区使用插值保形网格。

### 局部细小结构导致的全局时间步瓶颈

CFL 条件 (16) 由最小网格尺寸 $\min(\Delta x, \Delta y, \Delta z)$ 决定。在包含细导线的模型中（如电缆绝缘层厚度 ~ mm 级、地电位升分析中土壤电离通道半径 ~ mm 级），即使感兴趣的现象频率不高，局部细结构也会迫使全局使用极小 $\Delta t$，增加计算时间数十倍。

**应对策略**：使用亚网格技术（subgridding）在局部细小结构区域使用更细的空间步长，同时保持粗网格区域的大 $\Delta t$；或使用时间同步子网格（time synchronized subgridding）在局部时间步内完成细结构求解，再与主网格同步。

### PML 参数选取不当导致的残余反射和数值增长

PML 的吸收效果对参数选取（$\sigma(x)$ 分布、$\kappa(x)$ 分布、层数）敏感。参数选取不当会导致：
- **残余反射**：PML 层未能完全吸收高频/掠入射波，部分能量被反射回计算域
- **数值增长**：PML 层内部数值不稳定，导致解在时间上发散
- **低频锁定**：CFS-PML 对低频入射波（< 10 MHz）的吸收效率显著降低

**应对策略**：对于典型 EMT 问题（雷击、开关暂态），推荐使用 8–12 层 PML，$\sigma_{\max}$ 按 $0.8 \times (\varepsilon_0 / \mu_0) \times \text{CFL}$ 选取，具体参数见 Gedney 的 PML 实现建议。

### 土壤频变与非线性电离

土壤电阻率在雷电暂态宽频带（0.1 Hz–10 MHz）内显著变化：直流电阻率 $\rho_{DC}$ 与高频电阻率 $\rho_{HF}$ 差异可达 10 倍（Alipio-Visacro 测量数据）。当接地极周围土壤电场超过土壤击穿场强 $E_c \approx 300$ kV/m 时，土壤发生电离，等效电阻率随电流密度非线性变化。

**应对策略**：对于线性频变问题，使用 (18) 的递归卷积核结合矢量拟合处理土壤频变（Duarte 2025）；对于土壤电离非线性问题，需要在 FDTD 迭代中实时更新土壤电导率场（$\sigma(\mathbf{r}, t) = f(|\mathbf{E}(\mathbf{r}, t)|)$），计算量显著增加，但可在时域中捕捉土壤击穿与恢复动态过程。

### 场-路接口的积分路径与参考方向

FDTD 计算域输出的端口电压/电流注入 EMTP 电路时，需要明确：
- 积分路径：端口电压 $V = \int \mathbf{E} \cdot d\mathbf{l}$ 的路径必须与 EMTP 端口参考方向一致
- 参考方向：电场从节点 A 到节点 B 的线积分对应 EMTP 中节点 A 的正电位
- 端口定义：FDTD 三维端口面与 EMTP 支路端点的映射关系

**应对策略**：在 FDTD 模型建立初期即确定场-路接口的位置和方向，使用统一的几何参考框架；接口处设置标志性格点（flag cells）记录端口变量，用于与 EMTP 数据交换。

## 量化性能边界

基于来源论文的量化数据汇总：

| 应用场景 | 频率范围 | 网格要求 | 计算效率 | 精度/偏差 | 来源 |
|---------|---------|---------|---------|---------|------|
| GIS VFT 分析 | 1–140 MHz | 12m GIB 模型，$\Delta x$ = 2–5 mm | EMTP/FDTD = 1:50（耗时比） | 主频偏差 < 5%，幅值偏差 < 15% | Ametani 2018 |
| 紧凑线路雷击感应电压 | 0.1 Hz–1 MHz | 15kV 三相线路，$\Delta x$ = 0.5 m | 矢量拟合误差 < 0.1% | 与火箭引雷实测偏差待核验 | De Conti 2020 |
| 接地极 FDTD-TL 冲击阻抗 | DC–1 MHz | 双平行导线，$\Delta x$ = 0.1 m | FDTD-TL vs HEM 偏差 < 5% | GPR 偏差 < 5%，高阻率下误差趋近 0 | Duarte 2025 |
| 倾斜导线阶梯近似误差 | 0.5–5 MHz | $\Delta x$ = λ/20 | — | 倾斜角 15° 时误差 < 2% | Noda 2004 |

**FDTD 计算效率的主要限制因素**：
- 网格总量 $N_x \times N_y \times N_z$（三维模型）
- 时间步数（由仿真时长 $T$ 和 $\Delta t$ 决定）
- CFL 稳定性条件 $\Delta t \leq \Delta t_{\max}$（由 $\min(\Delta x, \Delta y, \Delta z)$ 决定）

典型雷电暂态仿真（$T$ = 100 μs，$\Delta t$ = 0.1 ns）：需迭代 $10^6$ 步，三维模型网格量 $10^6$–$10^8$ 量级。

## 适用边界与选择指南

### FDTD 优先于 EMTP 传输线模型的场景

- **超高频暂态**：频率 > 10 MHz，波长与导线截面尺寸可比拟，集总参数模型失效
- **复杂三维几何**：非平面布线、非圆柱导体、复杂接地网结构，传输线近似不适用
- **外部场耦合**：雷电电磁场对线路的宽频耦合、EMI/EMC 分析，耦合机制无法简化为集总源
- **土壤非线性击穿**：接地极周围土壤电离动态过程，需要局部更新介电参数场
- **辐射场研究**：电磁脉冲（EMP）对电力系统的作用，天线效应和电磁兼容问题

### EMTP 传输线模型优先于 FDTD 的场景

- **工频/低频暂态**：频率 < 1 MHz，传输线近似精度足够
- **大系统整体响应**：系统级 EMT 仿真（数百节点），FDTD 的计算量无法承受
- **实时仿真约束**：时间步长要求 < 50 μs（如继电保护测试），FDTD 步长时间不支持
- **已知简化模型适用**：大量工程经验已验证传输线模型在给定场景下足够精确

### FDTD 与 FEM 的选择

| 特征 | FDTD | FEM |
|------|------|-----|
| 几何适应性 | 阶梯近似复杂曲面 | 任意非结构化网格 |
| 计算效率 | 显式，无需线性方程求解 | 隐式，需组装和求解稀疏矩阵 |
| 宽带分析 | 直接时域，宽频一次获取 | 通常需多频点逐点求解 |
| 材料非线性 | 通过场局部更新参数 | 通过 Newton-Raphson 迭代 |
| 典型 EMT 应用 | 雷电、VFT、接地冲击、线路耦合 | 变压器铁芯、绝缘子、电场集中区域 |

### FDTD 网格设计决策表

| 问题特征 | 网格策略 | 注意事项 |
|---------|---------|---------|
| 均匀介质，规则几何 | 均匀网格，$\Delta x$ = λ/20 | 避免 CFL 瓶颈 |
| 含细导线/薄层 | 局部加密 + 亚网格 | 确保亚网格界面数值稳定 |
| 开放边界（雷电场耦合） | PML（8–12 层） | CFS-PML 对低频效果更好 |
| 频率相关材料 | ADE 或递归卷积 | 矢量拟合阶数需覆盖频段 |
| 大长宽比结构（如电缆） | 非均匀渐变网格 | 渐变率 < 1.1–1.2 避免反射 |

## 相关方法

- [[finite-element-method]]：更适合复杂几何、非线性材料和弱形式场问题；与 FDTD 在几何适应性和计算效率上互补
- [[high-frequency-transient-analysis]]：FDTD 常作为高频暂态的场求解证据，提供三维电磁场分布
- [[lightning-transient-analysis]]：雷电波传播和耦合分析的应用入口；FDTD 是验证雷电感应电压模型的基准求解器
- [[transmission-line-model]]：系统级 EMT 中常用的线路近似，需要用 FDTD 全波结果界定适用范围
- [[grounding-system-modeling]]：接地电极和土壤频变问题需要场求解校验；FDTD-TL 混合方法是接地冲击分析的有效工具
- [[interface-technique]]：说明场解与 EMT 电路之间如何交换端口变量
- [[vector-fitting]]：频变土壤和导体内部阻抗在 FDTD 时域卷积中的有理函数逼近技术
- [[characteristic-method]]：与 FDTD 不同的另一类时域全波方法，基于特征线法和 Riemann 解

## 来源论文

| 论文 | 年份 | 主要贡献 |
|------|------|---------|
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi]] | 2025 | FDTD-TL 混合方法计算接地极冲击阻抗；递归卷积处理频变土壤；偏差 < 5% |
| [[electromagnetic-disturbances-in-gas-insulated-substations-and-vft-calculations]] | 2018 | GIS VFT 1–140 MHz 实测数据；EMTP 与 FDTD 交叉验证；主频偏差 < 5% |
| [[lightning-induced-voltage-analysis-on-a-three-phase-compact-distribution-line-co]] | 2020 | 相域 FDTD 基准；扩展 Marti 模型用于雷电感应电压；矢量拟合优于 Bode 渐近法 |
| [[equivalent-circuit-model-of-a-transmission-tower-considering-a-lightning-struck-]] | 2021 | 杆塔雷击 FDTD 等值电路；冲击阻抗建模 |
| [[error-in-propagation-velocity-due-to-staircase-approximation-of-an-inclined-thin]] | 2004 | 倾斜导线 FDTD 阶梯近似误差分析；倾斜角 15° 时误差 < 2% |