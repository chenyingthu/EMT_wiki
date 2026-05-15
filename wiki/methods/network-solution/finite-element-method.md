---
title: "有限元法 (Finite Element Method, FEM)"
type: method
tags: [finite-element, fem, electromagnetic, field, numerical, network-solution]
created: "2026-05-02"
updated: "2026-05-16"
---

# 有限元法 (Finite Element Method, FEM)

## 定义

有限元法（Finite Element Method, FEM）是把连续电磁场问题划分为有限个单元、在每个单元上用形函数（trial function）近似未知量，并通过**弱形式（weak form）**组装代数方程组的数值方法。电磁 FEM 可用于静电场、静磁场、涡流场、频域全波和时域瞬态场问题。与 [[fdtd]] 的显式时域步进不同，FEM 通常形成大型稀疏线性系统并通过迭代或直接法求解。

在 EMT 知识体系中，FEM 属于**场级建模工具**，为电网元件提供高精度的本地参数（电感、电容、电阻、磁化曲线），而不直接替换整个电网的节点方程求解器。

## EMT 中的角色

FEM 在 EMT 仿真体系中的定位是**参数提取器**和**场路耦合接口**，主要作用包括：

- **参数提取**：计算变压器、电机、电抗器、电缆、接地电极和母线结构的集总参数或频率响应
- **材料非线性建模**：处理铁芯饱和（B-H 曲线）、涡流、集肤效应、邻近效应和磁滞
- **精细场分布**：获取绕组磁通密度空间分布、端部绕组电场应力、局部电磁力
- **生成可嵌入 EMT 的等效模型**：查表模型、状态空间模型、等效阻抗或受控源
- **验证基准**：为 [[emt-simulation-verification]] 提供参考解，评估 EMT 等效模型的精度边界

FEM 典型不直接参与 EMT 步进循环（实时仿真除外），而是在预处理阶段提取参数或在场路联合仿真中作为子求解器使用。

## 核心弱形式与离散化

### 标量二阶椭圆型方程

以标量泊松方程为例，说明 FEM 的标准弱形式推导：

$$\nabla \cdot (k \nabla u) + qu = f$$

其中 $k$ 为扩散系数，$q$ 为质量项系数，$f$ 为源项。乘以测试函数 $v \in H_0^1(\Omega)$（满足齐次 Dirichlet 边界）并在域 $\Omega$ 上积分，利用**高斯散度定理**分部积分：

$$\int_{\Omega} k \nabla u \cdot \nabla v \, d\Omega + \int_{\Omega} quv \, d\Omega = \int_{\Omega} fv \, d\Omega + \int_{\Gamma_N} gv \, d\Gamma$$

其中 $\Gamma_N$ 为 Neumann 边界，$g$ 为给定通量。这便是弱形式——未知函数 $u$ 的二阶导数被降为一阶导数与测试函数梯度的乘积，从而允许不连续或低正则解。

### Galerkin 离散

设近似解和测试函数均用同一组形函数 $\phi_j$ 展开：

$$u_h(\mathbf{x}) = \sum_{j=1}^{N} u_j \phi_j(\mathbf{x}), \quad v_h(\mathbf{x}) = \phi_i(\mathbf{x})$$

代入弱形式，得到线性系统：

$$\mathbf{K} \mathbf{u} = \mathbf{f}$$

其中刚度矩阵元和质量矩阵元分别为：

$$K_{ij} = \int_{\Omega} k \nabla \phi_j \cdot \nabla \phi_i \, d\Omega + \int_{\Omega} q \phi_j \phi_i \, d\Omega, \quad F_i = \int_{\Omega} f \phi_i \, d\Omega + \int_{\Gamma_N} g \phi_i \, d\Gamma$$

刚度矩阵是**稀疏、对称、正定**的（当 $k > 0, q \geq 0$ 时），这是 FEM 可以使用稀疏矩阵求解器的数学基础。

### 电磁场控制方程（涡流问题）

在 EMT 建模中最常用的是以磁矢势 $\mathbf{A}$ 为未知量的**涡流方程**：

$$\nabla \times (\nu \nabla \times \mathbf{A}) + \sigma \frac{\partial \mathbf{A}}{\partial t} = \mathbf{J}_s$$

其中：
- $\nu = 1/\mu$ 为磁阻率（$\mu$ 为磁导率）
- $\sigma$ 为电导率
- $\mathbf{J}_s$ 为源电流密度

该方程兼容非线性材料（$\nu$ 随磁感应强度 $\mathbf{B} = \nabla \times \mathbf{A}$ 变化）和各向异性媒体。对二维问题可简化为标量势问题，对轴对称问题需引入环路坐标。

### 弱形式的矩阵表达

将场域 $\Omega$ 离散为 $N_e$ 个单元，单元 $e$ 上的近似解为：

$$\mathbf{A}^e(\mathbf{x}) = \sum_{j=1}^{n_{\mathrm{dof}}} A_j^e \mathbf{N}_j^e(\mathbf{x})$$

其中 $\mathbf{N}_j^e$ 为矢量形函数（常用 Whitney 边元 / 棱边元）。组装全域矩阵：

$$\mathbf{S}_{ij} = \int_{\Omega^e} \nu^e \nabla \times \mathbf{N}_j^e \cdot \nabla \times \mathbf{N}_i^e \, d\Omega^e, \quad \mathbf{T}_{ij} = \int_{\Omega^e} \sigma^e \mathbf{N}_j^e \cdot \mathbf{N}_i^e \, d\Omega^e$$

离散后的矩阵形式为：

$$(\mathbf{S} + \frac{\mathbf{T}}{\Delta t}) \mathbf{A}^{n+1} = \mathbf{J}_s^{n+1} + \frac{\mathbf{T}}{\Delta t} \mathbf{A}^n$$

时间离散通常采用**后向欧拉法**（无条件稳定）或 **Crank-Nicolson 法**（二阶精度）。

## EMT 耦合方式

FEM 与 EMT 仿真器的耦合有五种主要模式，各有其适用场景和精度特征：

### 1. 离线参数提取

用 FEM 在宽频带上计算端口阻抗或导纳矩阵，再写入 EMT 等效支路。这是最简单、最常用的模式——FEM 完全离线运行，结果以查表或解析拟合形式嵌入 EMT。

**典型流程**：几何建模 → 材料赋值 → 网格剖分 → 频域扫频 → 端口参数提取 → 生成 EMT 元件参数文件

**代表工作**：Dennetière 2009 用 FLUX3D 计算变压器铁芯 B-H 曲线，提取后在 EMTP 中建模为非线性磁化支路；Shafieipour 2018 用 FEM 计算任意截面电缆的电容、电感和阻抗参数。

### 2. 查表耦合（Look-up Table）

以电流、温度、频率或机械位置为输入变量，将 FEM 计算得到的磁链、损耗或力存储为多维查表，在 EMT 步进中实时查表注入。

查表耦合避免了 FEM 在线求解的开销，但需要预先在参数空间内进行密集采样，且插值精度受采样密度约束。典型应用：电机[[synchronous-machine-model]]的饱和磁化曲线、变压器绕组温升-损耗映射。

### 3. 场路联合仿真（Co-simulation）

EMT 侧作为主控程序驱动场求解器 FEM 侧，每步或每隔若干步交换端口电压/电流数据。两者通过接口条件（端口匹配条件）保持物理一致性。

**代表工作**（Dennetière 2009）：EMTP-RV 在时刻 $t$ 求解网络方程得到绕组端电压 $V_{\mathrm{EMTP}}(t)$，通过 DLL 发送至 FLUX3D；FLUX3D 求解非线性瞬态磁场方程，得到绕组电流 $I_{\mathrm{FEM}}(t)$，返回 EMTP 用于 $t+\Delta t$ 步的受控电流源更新。采用单步延迟耦合（$I_{\mathrm{EMTP}}(t+\Delta t) = I_{\mathrm{FEM}}(t)$）保证数值稳定性。

**关键挑战**：主控步长与场求解器收敛速度的匹配、非线性材料迭代与网络方程迭代的双向耦合、边界条件的物理一致性。

### 4. 模型降阶（Model Order Reduction, MOR）

将 FEM 得到的宽频响应或状态空间方程压缩为低阶模型，使其能在 EMT 步长约束内实时运行。降阶方法包括：

- **模态截断**：保留主要特征模态（特征值/特征向量）
- **平衡截断**：基于可控性/可观测性 Grammian 的系统性降阶
- **数据驱动的 Vector Fitting**：将 FEM 频域阻抗拟合成有理函数（极点-留数形式），再综合为 RLC 等效电路
- 详见 [[model-order-reduction]]

**代表工作**（electromagnetic-transient-modeling-of-grounding-electrodes 2020）：用快速松弛矢量拟合（FRVF）将 FEM 提取的接地极宽频阻抗（1 kHz–5 MHz）拟合成 6 阶有理函数，综合为 EMT 可嵌入的 RLC 网络，时域雷电流注入后 GPR 波形无虚假振荡。

### 5. 频率相关等值（FDNE）

直接用 FEM 计算端口的频率相关阻抗或导纳矩阵，通过 [[vector-fitting]] 拟合为 [[fdne-model]] 或 Norton 等效电路，供 EMT 在暂态仿真中使用。

该模式特别适用于**大型接地系统**（接地栅网、接地极群）和**电缆接头处**的高频响应建模，避免建立完整三维场模型。

## 形式化表达

### 单元矩阵装配

$$\mathbf{K}^{(e)} = \int_{\Omega^{(e)}} \nu^{(e)} \nabla \mathbf{N}^{(e)} \cdot \nabla \mathbf{N}^{(e)\top} \, d\Omega^{(e)}, \quad \mathbf{M}^{(e)} = \int_{\Omega^{(e)}} \sigma^{(e)} \mathbf{N}^{(e)} \cdot \mathbf{N}^{(e)\top} \, d\Omega^{(e)}$$

$$\mathbf{K} = \bigoplus_{e=1}^{N_e} \mathbf{K}^{(e)}, \quad \mathbf{M} = \bigoplus_{e=1}^{N_e} \mathbf{M}^{(e)}$$

（$\bigoplus$ 表示直接刚度装配，$N_e$ 为单元总数）

### 时间离散（后向欧拉）

$$\left(\frac{\mathbf{M}}{\Delta t} + \mathbf{K}\right) \mathbf{A}^{n+1} = \frac{\mathbf{M}}{\Delta t} \mathbf{A}^n + \mathbf{J}^{n+1}$$

### 场路接口条件（端口电压约束）

$$V_{\mathrm{port}}^n = \frac{1}{l}\int_{\mathrm{port}} \mathbf{E}^n \cdot d\mathbf{l} = \frac{1}{l} \sum_i A_i^n \cdot \Delta \mathbf{x}_i$$

（$l$ 为端口长度，$\mathbf{E}$ 为电场，$\Delta \mathbf{x}_i$ 为单元边长）

### 接地极频域阻抗（大地为均匀有损半空间）

$$Z_{\mathrm{ground}}(\omega) = \frac{1}{2\pi a\sigma_{\mathrm{soil}}} \left(1 + \frac{j\omega\mu_0\sigma_{\mathrm{soil}} a^2}{4}\right), \quad a \gg \delta$$

当频率升高或大地电导率较高时，需使用完整的 Sommerfeld 积分或复镜像理论处理趋肤效应（$\delta = \sqrt{2/(\omega\mu_0\sigma_{\mathrm{soil})}}$）。

## 关键技术挑战

### 网格质量与收敛性

- **网格细化策略**：气隙、尖端、导体边缘、集肤深度层和材料界面处需局部细化，自适应 FEM 通过误差估计指示器自动调整
- **集肤效应处理**：导体内部网格在集肤深度 $\delta$ 内需加密（建议至少 3-5 层单元），否则涡流损耗被低估
- **各向异性材料**：矽钢片叠片的磁导率张量、主变压器的油-纸绝缘结构，需要非一致网格或专用形函数

### 非线性材料迭代

- 铁芯饱和（B-H 曲线）需在每个时间步或每个非线性迭代中更新 $\nu(\mathbf{B})$
- **牛顿-拉夫逊法（Newton-Raphson）** 是处理非线性磁化的标准方法，每次迭代需重新装配刚度矩阵（计算成本高）
- **Picard 迭代（固定点法）**：收敛较慢但每次迭代不需要重新装配刚度矩阵，适合弱非线性问题
- **自适应时间步长**：在饱和突变区域（涌流峰值、铁磁谐振）临时缩小步长，避免迭代发散

### 场路耦合的数值稳定性

- **单步延迟耦合**（$I_{\mathrm{EMTP}}^{n+1} = I_{\mathrm{FEM}}^n$）是保证耦合系统稳定的最小延迟量；无延迟全联立耦合要求 FEM 子步长 ≤ EMT 步长 1/10
- **端口插值误差**：FEM 计算的端口电流是单元内积分值，与 EMT 网络方程中定义的端口电流（节点电压差/等效阻抗）可能存在定义不一致
- **能量守恒**：场路耦合系统应满足功率平衡 $\sum V_{\mathrm{port}} I_{\mathrm{port}} = \int_{\Omega} \mathbf{J} \cdot \mathbf{E} \, d\Omega$，偏差过大说明接口条件有问题

### 多物理耦合

- **磁-热耦合**：涡流损耗转换为热，热影响材料电导率和磁导率，需双向迭代
- **磁-机械耦合**：麦克斯韦力引起铁芯和绕组振动，振动又改变气隙长度（变压器啸声问题），需结构力学 FEM 子步
- **电-化学耦合**：接地电极腐蚀、电化学极化效应，主要出现在长期直流接地极设计中

## 量化性能边界

| 参数 | 典型范围 | 数据来源 |
|------|---------|---------|
| 网格节点数（变压器铁芯 3D 模型） | 5,000–500,000 | Dennetière 2009：12,000 节点（600 MVA 五柱变压器） |
| FEM-EMTP 单步延迟误差 | < 3%（励磁涌流） | Dennetière 2009：Δt=0.5 ms 时误差 3% |
| 允许的 FEM/EMTP 步长比 | 1:10（无延迟）至 1:1（单步延迟） | Dennetière 2009 |
| 接地极峰值 GPR 降幅（频变土壤） | 13.7%–37.3% | 2020 paper（相对于恒定参数模型） |
| 土壤含水率 1.32%→8.74% 时 GPR 下降 | ~17 倍 | 2020 paper |
| FRVF 拟合接地极阻抗（10 m 垂直接地极） | 6 阶极点，无振荡 | 2020 paper |
| 铜导体集肤深度（60 Hz） | ~8.5 mm | 铜 $\sigma = 5.8\times10^7$ S/m |
| 钢导体集肤深度（60 Hz） | ~0.5–2 mm | 钢 $\sigma \approx 10^6$–$10^7$ S/m |

## 适用边界与选择指南

| 场景 | 推荐 FEM 模式 | 不推荐场景 |
|------|------------|-----------|
| 变压器参数提取（离线） | 离线参数提取 + 查表 | 不需要 FEM，直接查厂家曲线 |
| 变压器合闸涌流（在线） | 场路联合仿真（EMTP-FLUX3D） | 纯 EMT 单相等值（无法捕捉相间耦合） |
| 接地系统宽频阻抗 | FDNE + Vector Fitting | 二维轴对称模型（高估端部效应） |
| 电缆参数提取 | 离线参数提取（任意截面） | FDTD（不适合复杂截面） |
| 电机饱和转矩 | 查表耦合（B-H 曲线） | 全 FEM 在线求解（实时性不足） |
| 雷电冲击电场分布 | 频域 FEM + 参数扫描 | 静磁场近似（高频瞬态需全波） |
| 铁磁谐振分析 | 场路联合仿真（非线性） | 线性 EMT 模型（铁芯饱和是核心） |

FEM **不擅长** 的场景：
- 全规模电网的系统级暂态（节点数 > $10^5$ 时 3D FEM 计算成本不可接受）
- 实时仿真（除非使用极致降阶模型，如磁路等效电路）
- 长输电线路传播效应（应使用 [[transmission-line-model]] 的分布参数模型）



<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- Background -->
  <rect width="900" height="520" fill="#ffffff"/>

  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" font-weight="bold" fill="#333">图1 · FEM 在 EMT 中的工作流程与耦合模式</text>

  <!-- ====== Layer 1: 离线参数提取路径 ====== -->
  <!-- 输入框: 几何+材料 -->
  <rect x="20" y="50" width="130" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="85" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e40af">几何建模</text>
  <text x="85" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">材料参数</text>
  <text x="85" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">边界条件</text>

  <!-- 网格剖分 -->
  <rect x="190" y="50" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="250" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#166534">网格剖分</text>
  <text x="250" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">局部细化</text>
  <text x="250" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">自适应加密</text>

  <!-- FEM 求解器 -->
  <rect x="350" y="50" width="120" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="410" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#92400e">FEM 求解</text>
  <text x="410" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">弱形式装配</text>
  <text x="410" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">稀疏矩阵求解</text>

  <!-- 参数提取 -->
  <rect x="510" y="50" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="570" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#166534">参数提取</text>
  <text x="570" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">L/C/R 矩阵</text>
  <text x="570" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">频响曲线</text>

  <!-- EMT 嵌入 -->
  <rect x="670" y="50" width="130" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="735" y="70" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#5b21b6">EMT 嵌入</text>
  <text x="735" y="86" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">查表模型</text>
  <text x="735" y="98" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">等效阻抗</text>

  <!-- Arrows Layer 1 -->
  <line x1="150" y1="75" x2="188" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="310" y1="75" x2="348" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="470" y1="75" x2="508" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="630" y1="75" x2="668" y2="75" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ====== Layer 2: 场路联合仿真路径 ====== -->
  <rect x="20" y="140" width="130" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="85" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e40af">EMTP</text>
  <text x="85" y="176" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">网络方程</text>
  <text x="85" y="188" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">求解器</text>

  <rect x="190" y="140" width="120" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="250" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#5b21b6">接口条件</text>
  <text x="250" y="176" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">V/I 交换</text>
  <text x="250" y="188" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">单步延迟</text>

  <rect x="350" y="140" width="120" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="410" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#92400e">FEM 场求解</text>
  <text x="410" y="176" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">Newton-Raphson</text>
  <text x="410" y="188" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">非线性迭代</text>

  <rect x="510" y="140" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="570" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#166534">数据回传</text>
  <text x="570" y="176" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">磁链/电流</text>
  <text x="570" y="188" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">返回 EMT</text>

  <rect x="670" y="140" width="130" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="735" y="160" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#5b21b6">EMTP</text>
  <text x="735" y="176" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">下一步更新</text>
  <text x="735" y="188" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">受控源注入</text>

  <!-- Arrows Layer 2 -->
  <line x1="150" y1="165" x2="188" y2="165" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="310" y1="165" x2="348" y2="165" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="470" y1="165" x2="508" y2="165" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="630" y1="165" x2="668" y2="165" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ====== Layer 3: 模型降阶路径 ====== -->
  <rect x="20" y="230" width="130" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="85" y="250" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#1e40af">FEM 频域</text>
  <text x="85" y="266" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">宽频响应</text>
  <text x="85" y="278" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#1e40af">1 kHz–5 MHz</text>

  <rect x="190" y="230" width="120" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="250" y="250" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#92400e">Vector Fitting</text>
  <text x="250" y="266" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">有理函数拟合</text>
  <text x="250" y="278" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#92400e">FRVF 6阶极点</text>

  <rect x="350" y="230" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="410" y="250" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#166534">RLC 综合</text>
  <text x="410" y="266" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">等效电路</text>
  <text x="410" y="278" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">无源性验证</text>

  <rect x="510" y="230" width="120" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="570" y="250" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#166534">EMT 嵌入</text>
  <text x="570" y="266" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">FDNE 模型</text>
  <text x="570" y="278" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#166534">时域仿真</text>

  <rect x="670" y="230" width="130" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="735" y="250" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" font-weight="bold" fill="#5b21b6">实时仿真</text>
  <text x="735" y="266" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">实时步长</text>
  <text x="735" y="278" text-anchor="middle" font-family="Arial,sans-serif" font-size="10" fill="#5b21b6">在线求解</text>

  <!-- Arrows Layer 3 -->
  <line x1="150" y1="255" x2="188" y2="255" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="310" y1="255" x2="348" y2="255" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="470" y1="255" x2="508" y2="255" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="630" y1="255" x2="668" y2="255" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- ====== 关键技术挑战 Box ====== -->
  <rect x="20" y="310" width="860" height="130" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="40" y="330" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#92400e">关键技术挑战</text>

  <text x="40" y="350" font-family="Arial,sans-serif" font-size="10" fill="#78350f">① 网格质量：气隙/尖端/集肤深度层需局部细化，自适应 FEM 通过误差估计指示器自动调整</text>
  <text x="40" y="366" font-family="Arial,sans-serif" font-size="10" fill="#78350f">② 非线性迭代：铁芯饱和需 Newton-Raphson 迭代，每次重新装配刚度矩阵，计算成本高</text>
  <text x="40" y="382" font-family="Arial,sans-serif" font-size="10" fill="#78350f">③ 场路耦合稳定性：单步延迟耦合（I_EMTP(n+1)=I_FEM(n)）保证数值稳定，允许 FEM/EMTP 步长比≤10:1</text>
  <text x="40" y="398" font-family="Arial,sans-serif" font-size="10" fill="#78350f">④ 端口插值误差：FEM 积分电流与 EMT 节点电压定义的端口电流可能存在定义不一致</text>
  <text x="40" y="414" font-family="Arial,sans-serif" font-size="10" fill="#78350f">⑤ 多物理耦合：磁-热耦合、磁-机械耦合需双向迭代，实时仿真中难以完全收敛</text>
  <text x="40" y="430" font-family="Arial,sans-serif" font-size="10" fill="#78350f">⑥ 能量守恒：场路耦合系统应满足功率平衡，偏差过大说明接口条件有问题</text>

  <!-- ====== 量化性能边界 Box ====== -->
  <rect x="20" y="455" width="860" height="55" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="40" y="475" font-family="Arial,sans-serif" font-size="12" font-weight="bold" fill="#166534">量化性能边界</text>
  <text x="40" y="493" font-family="Arial,sans-serif" font-size="10" fill="#14532d">Dennetière 2009: 12,000节点网格 @ Δt=0.5ms → 励磁涌流误差 3% | FRVF 6阶极点拟合接地极（2020）→ 时域无振荡 | 铜/钢集肤深度 60Hz: 8.5mm/0.5–2mm</text>

  <!-- Arrowhead definition -->
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>

  <!-- Legend -->
  <rect x="20" y="490" width="12" height="12" rx="2" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="36" y="500" font-family="Arial,sans-serif" font-size="9" fill="#333">输入</text>
  <rect x="70" y="490" width="12" height="12" rx="2" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="86" y="500" font-family="Arial,sans-serif" font-size="9" fill="#333">处理</text>
  <rect x="130" y="490" width="12" height="12" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="146" y="500" font-family="Arial,sans-serif" font-size="9" fill="#333">算法</text>
  <rect x="190" y="490" width="12" height="12" rx="2" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="206" y="500" font-family="Arial,sans-serif" font-size="9" fill="#333">输出</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · FEM 在 EMT 中的工作流程与耦合模式</p>


## FEM 变体分类

### 按物理类型分类

| 类型 | 控制方程 | 典型应用 |
|------|---------|---------|
| 静电场 | $-\nabla \cdot (\varepsilon \nabla \phi) = \rho$ | GIS 绝缘子电场、导线表面电场 |
| 静磁场 | $\nabla \times (\nu \nabla \times \mathbf{A}) = \mathbf{J}_s$ | 永磁电机磁场、大型变压器漏磁 |
| 涡流场 | $\nabla \times (\nu \nabla \times \mathbf{A}) + \sigma \partial \mathbf{A}/\partial t = \mathbf{J}_s$ | 变压器铁芯损耗、导体涡流损耗 |
| 频域全波 | $\nabla \times (\nu \nabla \times \mathbf{E}) - k_0^2 \mathbf{E} = 0$ | 雷电电磁脉冲辐射、接地系统宽频响应 |
| 时域全波 | 后向欧拉离散涡流方程 | 暂态电磁兼容、开关电弧辐射 |

### 按几何维度分类

| 维度 | 适用场景 | 局限 |
|------|---------|------|
| 一维 | 传输线单位长参数、导体内部电流分布 | 无法处理端部效应 |
| 二维平面 | 无限长设备横截面电场/磁场 | 无法处理长度方向变化 |
| 二维轴对称 | 旋转对称设备（电缆、绝缘子） | 无法处理不对称结构 |
| 三维 | 任意复杂几何结构 | 计算成本高，网格生成困难 |

### 按离散格式分类

| 单元类型 | 形函数阶数 | 自由度 | 适用场景 |
|---------|-----------|--------|---------|
| 线性三角形/四面体 | 一阶 | 节点标量势 | 快速初步估算 |
| 二次三角形/四面体 | 二阶 | 节点标量势 | 弯曲边界精确求解 |
| 棱边元（Whitney） | 一阶 | 边矢量势 | 涡流场（$\mathbf{A}$-$\phi$ 格式） |
| 矢量有限元 | 高阶 | 边/面 | 全波高频问题 |

## 相关页面

- [[fdtd]]：规则网格显式时域全波方法，适合宽带传播问题（与 FEM 形成互补）
- [[vector-fitting]]：FEM 频域结果到 EMT 有理模型拟合的核心方法
- [[model-order-reduction]]：FEM 大规模模型压缩为实时可运行模型的技术
- [[grounding-system-modeling]]：FEM 在接地系统中的核心应用场景之一
- [[synchronous-machine-model]]：FEM 提供电机饱和磁化曲线
- [[transmission-line-model]]：FEM 参数提取结果的使用对象
- [[interface-technique]]：场路联合仿真的接口实现框架
- [[hybrid-modeling]]：FEM 与 EMT 组合的上层集成方法
- [[frequency-scan]]：FEM 端口响应作为频率扫描的输入
- [[emt-simulation-verification]]：FEM 作为 EMT 参考解进行验证的方法
- [[fdne-model]]：FEM 宽频结果等值为频率相关网络模型

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[a-link-between-emtp-rv-and-flux3d-for-transformer-energization-studies]] | 2009 | EMTP-RV 与 FLUX3D 场路联合仿真接口，单步延迟耦合，励磁涌流 3% 误差，Δt=0.5 ms |
| [[parametric-study-of-transient-electromagnetic-fields]] | 2011 | 有损大地上方多导体线路暂态电磁场混合方法，偶极子分解+MFDTD，复镜像理论有效频率 0–10 MHz |
| [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based]] | 2022 | 电路型 FEM 变压器模型，磁路等效电路与 EMT 接口 |
| [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d]] | 2020 | 频变土壤 FEM 接地极模型，FRVF 拟合 6 阶极点，GPR 降低 13.7%–37.3% |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an]] | 2023 | 基于传输线理论的塔脚接地模型，频变土壤对 EMT 程序的影响 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende]] | 2020 | 接地网格频变 FEM，频域到时域的接口 |
| [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu]] | 2019 | 变压器电场和温度分布 FEM 计算，接地电极瞬态温升 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme]] | 2019 | 简单布置接地极的 GPR 和接地阻抗计算，与 FEM 对比 |