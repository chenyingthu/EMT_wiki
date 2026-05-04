---
title: "有限元法 (Finite Element Method, FEM)"
type: method
tags: [finite-element, fem, electromagnetic, field, numerical]
created: "2026-05-02"
---

# 有限元法 (Finite Element Method, FEM)

## 概述

有限元法（Finite Element Method, FEM）是求解偏微分方程边值问题的数值方法，通过将连续域离散化为有限个子域（单元），在每个单元上用简单函数近似未知解，从而将微分方程转化为代数方程组求解。在电力系统电磁暂态仿真领域，FEM广泛用于电磁场分析、设备参数提取、涡流损耗计算以及与电路仿真器的协同分析。

与[[fdtd]]和`bem`相比，FEM在处理复杂几何形状、非线性材料和各向异性介质方面具有独特优势，特别适合电力变压器、电机、接地系统和电缆的精细化建模。

## 数学基础

### 变分原理

变分原理是有限元法的理论基础，它将微分方程的边值问题转化为泛函极值问题。对于一般的二阶椭圆型偏微分方程：

$$-\nabla \cdot (k(\mathbf{r})\nabla u) + q(\mathbf{r})u = f(\mathbf{r}), \quad \mathbf{r} \in \Omega$$

边界条件为：
$$u = u_0, \quad \mathbf{r} \in \Gamma_D \quad \text{(Dirichlet边界)}$$
$$k\frac{\partial u}{\partial n} + \beta u = g, \quad \mathbf{r} \in \Gamma_N \quad \text{(Robin边界)}$$

对应的能量泛函为：

$$J(u) = \int_\Omega \left[\frac{1}{2}k|\nabla u|^2 + \frac{1}{2}qu^2 - fu\right] d\Omega + \int_{\Gamma_N} \left[\frac{1}{2}\beta u^2 - gu\right] d\Gamma$$

原边值问题的解等价于使泛函$J(u)$取极值的函数$u^*$：

$$J(u^*) = \min_{u \in H^1(\Omega)} J(u)$$

其中$H^1(\Omega)$是Sobolev空间，要求函数本身及其一阶导数在区域$\Omega$上平方可积。

### 弱形式（Weak Formulation）

弱形式通过分部积分降低了对解的光滑性要求，是有限元离散化的关键步骤。将微分方程乘以测试函数$v$并在区域$\Omega$上积分：

$$\int_\Omega \left[-\nabla \cdot (k\nabla u) + qu - f\right] v \, d\Omega = 0$$

应用Green恒等式进行分部积分：

$$\int_\Omega k\nabla u \cdot \nabla v \, d\Omega - \int_{\partial\Omega} k\frac{\partial u}{\partial n}v \, d\Gamma + \int_\Omega quv \, d\Omega = \int_\Omega fv \, d\Omega$$

考虑边界条件后，弱形式表述为：寻找$u \in V$，使得对所有$v \in V_0$：

$$a(u,v) = L(v)$$

其中双线性形式$a(\cdot,\cdot)$和线性泛函$L(\cdot)$分别为：

$$a(u,v) = \int_\Omega \left(k\nabla u \cdot \nabla v + quv\right) d\Omega + \int_{\Gamma_N} \beta uv \, d\Gamma$$

$$L(v) = \int_\Omega fv \, d\Omega + \int_{\Gamma_N} gv \, d\Gamma$$

函数空间定义为：
$$V = \{v \in H^1(\Omega) : v = u_0 \text{ on } \Gamma_D\}$$
$$V_0 = \{v \in H^1(\Omega) : v = 0 \text{ on } \Gamma_D\}$$

### Galerkin方法

Galerkin方法是加权残差法的一种特殊形式，其核心思想是用近似函数空间的基函数作为权函数。设有限维子空间$V_h \subset V$，$V_{0h} \subset V_0$，Galerkin近似问题表述为：

寻找$u_h \in V_h$，使得对所有$v_h \in V_{0h}$：

$$a(u_h, v_h) = L(v_h)$$

将近似解展开为基函数的线性组合：

$$u_h(\mathbf{r}) = \sum_{j=1}^{N} u_j \phi_j(\mathbf{r})$$

其中$\{\phi_j\}_{j=1}^N$是节点基函数，$u_j$是待求的节点未知量。取$v_h = \phi_i$，代入弱形式得到线性代数方程组：

$$\sum_{j=1}^{N} a(\phi_j, \phi_i) u_j = L(\phi_i), \quad i = 1, 2, \ldots, N$$

矩阵形式为：

$$\mathbf{K}\mathbf{u} = \mathbf{f}$$

其中刚度矩阵$\mathbf{K}$和载荷向量$\mathbf{f}$的元素为：

$$K_{ij} = a(\phi_j, \phi_i) = \int_\Omega \left(k\nabla\phi_j \cdot \nabla\phi_i + q\phi_j\phi_i\right) d\Omega + \int_{\Gamma_N} \beta\phi_j\phi_i \, d\Gamma$$

$$f_i = L(\phi_i) = \int_\Omega f\phi_i \, d\Omega + \int_{\Gamma_N} g\phi_i \, d\Gamma$$

## 详细求解流程

### 1. 前处理阶段

#### 几何建模
- **CAD导入**：从STEP、IGES等格式导入几何模型
- **参数化建模**：使用脚本语言（如Python）创建参数化几何
- **特征简化**：去除对电磁分析无关的小特征（圆角、小孔）

#### 网格划分（Mesh Generation）
网格质量直接影响计算精度和收敛性。关键指标包括：

**单元质量指标**：
- 长宽比（Aspect Ratio）：建议小于20
- 内角范围：避免极端锐角或钝角
- Jacobian行列式：应大于0（保证单元不退化）

**自适应网格细化**：
$$h_{\text{new}} = h_{\text{old}} \left(\frac{\epsilon}{\eta}\right)^{1/p}$$

其中$\eta$是局部误差估计，$\epsilon$是目标误差，$p$是形函数阶数。

**网格类型**：
- 结构化网格：适用于规则几何，计算效率高
- 非结构化网格：适用于复杂几何，灵活性高
- 混合网格：结合两者优点

### 2. 离散化阶段

#### 形函数（Shape Functions）

形函数定义了单元内场变量的插值方式。

**一维线性单元（两节点）**：
$$\phi_1(\xi) = \frac{1-\xi}{2}, \quad \phi_2(\xi) = \frac{1+\xi}{2}, \quad \xi \in [-1, 1]$$

**一维二次单元（三节点）**：
$$\phi_1(\xi) = \frac{\xi(\xi-1)}{2}, \quad \phi_2(\xi) = 1-\xi^2, \quad \phi_3(\xi) = \frac{\xi(\xi+1)}{2}$$

**三角形线性单元**：
$$\phi_i = a_i + b_i x + c_i y, \quad i = 1, 2, 3$$

其中系数由节点坐标确定，满足$\phi_i(x_j, y_j) = \delta_{ij}$。

**四边形双线性单元**：
$$\phi_i(\xi, \eta) = \frac{1}{4}(1+\xi_i\xi)(1+\eta_i\eta)$$

**六面体单元（8节点）**：
$$\phi_i(\xi, \eta, \zeta) = \frac{1}{8}(1+\xi_i\xi)(1+\eta_i\eta)(1+\zeta_i\zeta)$$

### 3. 刚度矩阵组装

#### 数值积分

单元积分通过Gauss数值积分实现：

$$\int_{\Omega_e} f(\mathbf{r}) d\Omega \approx \sum_{q=1}^{N_q} w_q f(\mathbf{r}_q) |J(\mathbf{r}_q)|$$

其中$w_q$是积分权重，$\mathbf{r}_q$是积分点坐标，$J$是Jacobian行列式。

**一维Gauss积分点**（2点）：
$$\xi_1 = -\frac{1}{\sqrt{3}}, \quad \xi_2 = \frac{1}{\sqrt{3}}, \quad w_1 = w_2 = 1$$

**二维三角形**（3点）：
$$\xi_1 = \frac{2}{3}, \eta_1 = \frac{1}{6}, \quad \xi_2 = \frac{1}{6}, \eta_2 = \frac{2}{3}, \quad \xi_3 = \frac{1}{6}, \eta_3 = \frac{1}{6}$$

$$w_1 = w_2 = w_3 = \frac{1}{6}$$

#### 单元刚度矩阵计算

$$\mathbf{K}_e = \int_{\Omega_e} \left(k \nabla\mathbf{N}_e^T \cdot \nabla\mathbf{N}_e + q\mathbf{N}_e^T\mathbf{N}_e\right) d\Omega$$

其中$\mathbf{N}_e = [\phi_1, \phi_2, \ldots, \phi_{n_e}]$是单元形函数向量。

#### 全局组装

使用散度组装（Assembly）将单元矩阵叠加到全局矩阵：

$$K_{IJ} = \sum_e K_{ij}^{(e)}$$

其中$I = \text{DOF}(e, i)$，$J = \text{DOF}(e, j)$是自由度映射函数。

### 4. 求解阶段

#### 边界条件处理

**Dirichlet边界条件**：
- 直接消去法：移除对应行和列
- 罚函数法：将对角元置为极大值$K_{ii} = 10^{20}$
- 拉格朗日乘子法：引入额外未知量

**周期边界条件**（用于旋转电机）：
$$\mathbf{u}_A = e^{j\theta} \mathbf{u}_B$$

通过约束方程耦合边界上的自由度。

#### 线性方程组求解

**直接法**：
- LU分解：适用于中小规模问题（$N < 10^5$）
- Cholesky分解：适用于对称正定矩阵
- 稀疏矩阵技术：使用CSR/CSC格式存储

**迭代法**：
- 共轭梯度法（CG）：适用于对称正定系统
- GMRES：适用于非对称系统
- 多重网格法：收敛速度最优，适合大规模问题

预条件技术：
$$\mathbf{M}^{-1}\mathbf{K}\mathbf{u} = \mathbf{M}^{-1}\mathbf{f}$$

常用预条件子包括ILU（不完全LU）、Jacobi、SSOR等。

### 5. 后处理阶段

#### 场量计算

**梯度计算**：
$$\nabla u_h = \sum_{j=1}^N u_j \nabla\phi_j$$

**通量计算**：
$$\mathbf{J} = -k\nabla u_h$$

**能量计算**：
$$W = \frac{1}{2}\mathbf{u}^T\mathbf{K}\mathbf{u}$$

#### 误差估计

**先验误差估计**：
$$\|u - u_h\|_{H^1} \leq Ch^p|u|_{H^{p+1}}$$

其中$h$是网格尺寸，$p$是多项式阶数，$C$是与网格无关的常数。

**后验误差估计**（基于残差）：
$$\eta_K^2 = h_K^2\|R_K\|_{L^2(K)}^2 + \frac{1}{2}\sum_{e \subset \partial K} h_e\|R_e\|_{L^2(e)}^2$$

## 电磁场方程

### 静电场（Poisson方程）

对于电位$\varphi$：

$$-\nabla \cdot (\varepsilon \nabla \varphi) = \rho$$

其中$\varepsilon$是介电常数，$\rho$是电荷密度。电场强度：

$$\mathbf{E} = -\nabla \varphi$$

有限元弱形式：
$$\int_\Omega \varepsilon \nabla\varphi \cdot \nabla v \, d\Omega = \int_\Omega \rho v \, d\Omega$$

**应用**：高压绝缘设计、电缆电容计算、SF6断路器电场分析。

### 静磁场（磁标势/矢势）

#### 无电流区域（磁标势$\psi$）

$$\nabla \cdot (\mu \nabla \psi) = 0$$

$$\mathbf{H} = -\nabla \psi, \quad \mathbf{B} = \mu\mathbf{H}$$

#### 有电流区域（磁矢势$\mathbf{A}$）

$$\nabla \times (\nu \nabla \times \mathbf{A}) = \mathbf{J}_s$$

其中$\nu = 1/\mu$是磁阻率，$\mathbf{J}_s$是源电流密度。

**库仑规范**：
$$\nabla \cdot \mathbf{A} = 0$$

### 涡流场（Eddy Current）

考虑电磁感应的准静态近似：

$$\nabla \times (\nu \nabla \times \mathbf{A}) + \sigma\frac{\partial \mathbf{A}}{\partial t} = \mathbf{J}_s$$

其中$\sigma$是电导率。

**复数相量形式**（正弦稳态）：
$$\nabla \times (\nu \nabla \times \dot{\mathbf{A}}) + j\omega\sigma\dot{\mathbf{A}} = \dot{\mathbf{J}}_s$$

涡流损耗功率：
$$P_{eddy} = \frac{1}{2}\omega^2\sigma\int_\Omega |\dot{\mathbf{A}}|^2 d\Omega$$

**应用**：变压器铁心损耗计算、感应加热、电磁屏蔽设计。

### 全波电磁场（波动方程）

时域Maxwell方程组：

$$\nabla \times \mathbf{E} = -\mu\frac{\partial \mathbf{H}}{\partial t}$$
$$\nabla \times \mathbf{H} = \varepsilon\frac{\partial \mathbf{E}}{partial t} + \sigma\mathbf{E}$$

消去磁场后得到电场波动方程：

$$\nabla \times (\mu^{-1}\nabla \times \mathbf{E}) + \varepsilon\frac{\partial^2 \mathbf{E}}{\partial t^2} + \sigma\frac{\partial \mathbf{E}}{\partial t} = -\frac{\partial \mathbf{J}_s}{\partial t}$$

**频域形式**（Helmholtz方程）：
$$\nabla \times (\mu^{-1}\nabla \times \dot{\mathbf{E}}) - k^2\varepsilon_r\dot{\mathbf{E}} = -j\omega\dot{\mathbf{J}}_s$$

其中$k = \omega\sqrt{\mu_0\varepsilon_0}$是波数。

## 单元类型详解

### 一维单元

**线性杆单元**（2节点）：
- 节点：$x_1, x_2$
- 长度：$L = x_2 - x_1$
- 形函数：线性插值
- 应用：细长导体、传输线简化模型

**Hermite梁单元**（2节点，每节点2自由度）：
- 自由度：$w, \theta$（挠度和转角）
- 形函数：三次Hermite多项式
- 特点：保证$C^1$连续性

### 二维单元

#### 三角形单元

**线性三角形**（3节点）：
- 面积坐标：$L_1, L_2, L_3$，满足$L_1 + L_2 + L_3 = 1$
- 形函数：$\phi_i = L_i$
- 特点：适应任意三角形，自动满足协调性

**二次三角形**（6节点）：
- 节点配置：3顶点 + 3边中点
- 形函数：完全二次多项式
- 精度：$O(h^3)$收敛

**高阶三角形**：
- 三次（10节点）：包含内部节点
- 四次（15节点）、五次（21节点）

#### 四边形单元

**双线性四边形**（4节点）：
- 等参映射：从标准正方形$[-1,1]^2$到任意四边形
- 形函数：双线性插值
- Jacobian：需保证处处不为零

**Serendipity单元**（8节点）：
- 节点配置：4顶点 + 4边中点
- 形函数：不完全二次，不含内部节点
- 优势：同等精度下自由度更少

**双二次Lagrange单元**（9节点）：
- 含内部中心节点
- 形函数：完全双二次

### 三维单元

#### 四面体单元

**线性四面体**（4节点）：
- 体积坐标：$L_1, L_2, L_3, L_4$
- 形函数：$\phi_i = L_i$
- 优势：自动剖分复杂几何

**二次四面体**（10节点）：
- 6边中点 + 4顶点
- 形函数：完全二次多项式

#### 六面体单元

**三线性六面体**（8节点）：
- 等参映射：从标准立方体$[-1,1]^3$
- 形函数：三线性插值
- 应用：规则区域剖分

**20节点六面体**（Serendipity）：
- 8顶点 + 12边中点
- 形函数：不完全三二次
- 精度与效率的平衡

**27节点六面体**（Lagrange）：
- 含面心和体心节点
- 形函数：完全三二次

#### 棱柱和金字塔单元

**楔形（棱柱）单元**：
- 6节点线性、15节点二次
- 用于薄层区域（如涂层、绝缘层）

**金字塔单元**：
- 5节点线性、13节点二次
- 用于过渡网格（四面体-六面体连接）

### 高阶单元与谱元法

**p-型有限元**：
- 固定网格，提高多项式阶数
- 指数收敛速度（对比h型的代数收敛）
- 适合光滑解问题

**谱元法**：
- 使用Legendre多项式作为基函数
- 结合谱方法的高精度和有限元的几何灵活性
- 伪谱方法实现，可用FFT加速

**hp-自适应**：
- 同时优化网格细化（h）和阶数提升（p）
- 最优收敛策略，但实现复杂

## 时间域有限元法

### 时域离散化方法

#### 向后Euler法（一阶精度）

$$\frac{\mathbf{u}^{n+1} - \mathbf{u}^n}{\Delta t} = \dot{\mathbf{u}}^{n+1}$$

稳定性：无条件稳定（A-稳定）

精度：$O(\Delta t)$

#### Crank-Nicolson法（二阶精度）

$$\frac{\mathbf{u}^{n+1} - \mathbf{u}^n}{\Delta t} = \frac{1}{2}(\dot{\mathbf{u}}^{n+1} + \dot{\mathbf{u}}^n)$$

稳定性：无条件稳定

精度：$O(\Delta t^2)$

时间离散后的方程系统：
$$(\mathbf{M} + \frac{\Delta t}{2}\mathbf{K})\mathbf{u}^{n+1} = (\mathbf{M} - \frac{\Delta t}{2}\mathbf{K})\mathbf{u}^n + \frac{\Delta t}{2}(\mathbf{f}^{n+1} + \mathbf{f}^n)$$

#### Newmark-β法

用于结构动力学和电磁-机械耦合：
$$\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta t \dot{\mathbf{u}}^n + \frac{(\Delta t)^2}{2}\left[(1-2\beta)\ddot{\mathbf{u}}^n + 2\beta\ddot{\mathbf{u}}^{n+1}\right]$$

$$\dot{\mathbf{u}}^{n+1} = \dot{\mathbf{u}}^n + \Delta t\left[(1-\gamma)\ddot{\mathbf{u}}^n + \gamma\ddot{\mathbf{u}}^{n+1}\right]$$

参数选择：
- $\beta = 1/4, \gamma = 1/2$：平均加速度法（无条件稳定）
- $\beta = 1/6, \gamma = 1/2$：线性加速度法（条件稳定）

### 与EMT仿真的接口

#### 场路耦合策略

**直接耦合**（Monolithic）：
- 场和路的方程同时求解
- 精度高，但计算量大
- 适用于强耦合问题

**迭代耦合**（Partitioned）：
- 交替求解场方程和路方程
- 通过传输条件交换信息
- 实现简单，但可能收敛慢

**降阶耦合**（ROM-based）：
- 提取场模型的等效电路
- 在电路仿真器中运行
- 效率高，适合系统级仿真

#### 参数提取

**电感矩阵提取**：
$$L_{ij} = \frac{\Psi_i}{I_j}\bigg|_{I_k=0, k\neq j} = \frac{1}{I_j}\int_{\Omega_i} \mathbf{A} \cdot \mathbf{J}_i \, d\Omega$$

**电容矩阵提取**：
$$C_{ij} = \frac{Q_i}{V_j}\bigg|_{V_k=0, k\neq j} = \frac{1}{V_j}\oint_{\Gamma_i} \varepsilon\frac{\partial \varphi}{\partial n} d\Gamma$$

**电阻矩阵提取**：
$$R_{ij} = \frac{V_i}{I_j}\bigg|_{I_k=0, k\neq j} = \frac{1}{I_j}\int_{\Omega_i} \frac{\mathbf{J}_i \cdot \mathbf{J}_j}{\sigma} d\Omega$$

### 瞬态涡流分析

考虑铁心饱和的非线性时域方程：

$$\nabla \times (\nu(|\mathbf{B}|) \nabla \times \mathbf{A}) + \sigma\frac{\partial \mathbf{A}}{\partial t} = \mathbf{J}_s(t)$$

非线性迭代（Newton-Raphson）：
$$\mathbf{J}^{(k)}\delta\mathbf{A}^{(k)} = -\mathbf{R}^{(k)}$$

其中$\mathbf{J}$是Jacobian矩阵：
$$J_{ij} = \frac{\partial R_i}{\partial A_j} = \int_\Omega \left[\nu \nabla\phi_i \cdot \nabla\phi_j + \frac{\partial \nu}{\partial B^2}(\nabla\phi_i \cdot \mathbf{B})(\nabla\phi_j \cdot \mathbf{B})\right] d\Omega$$

## 电力系统应用

### 变压器建模

[[transformer-model]]中有限元法的应用包括：

#### 漏磁场分析

三维磁场计算确定绕组间漏磁通分布：
$$\nabla \times (\nu \nabla \times \mathbf{A}) = \mathbf{J}_w$$

其中$\mathbf{J}_w$是绕组电流密度。

短路阻抗计算：
$$Z_k = \frac{2W_{mag}}{I_N^2} = \frac{1}{I_N^2}\int_\Omega \nu |\nabla \times \mathbf{A}|^2 d\Omega$$

#### 损耗计算

**铁心损耗**（考虑旋转磁化）：
$$P_{Fe} = P_h + P_e + P_a = k_h f B_m^\alpha + k_e (fB_m)^2 + k_a (fB_m)^{1.5}$$

**绕组涡流损耗**：
- 轴向漏磁引起的环流损耗
- 辐向漏磁引起的涡流损耗

$$P_{w,e} = \int_{\Omega_w} \frac{|\mathbf{J}_{eddy}|^2}{\sigma} d\Omega$$

#### 局部过热分析

结合流体-热耦合计算：
$$\rho c_p \frac{\partial T}{\partial t} = \nabla \cdot (k\nabla T) + Q_{loss}(\mathbf{r}, t)$$

热点温度预测对绝缘寿命评估至关重要。

#### 直流偏磁

直流电流引起的半波饱和分析：
$$B(t) = B_{ac}\sin(\omega t) + B_{dc}$$

### 电机电磁设计

#### 同步电机

**空载特性计算**：
- 额定转速下的气隙磁场分布
- 每极磁通计算：$\Phi = \int_{S_{pole}} B_n dS$
- 感应电动势：$E = 4.44 f N k_w \Phi$

**负载分析**：
- 电枢反应磁场
- 阻尼绕组电流分布
- 转矩计算：$T = \frac{\partial W'}{\partial \theta}$

#### 感应电机

**滑差分析**：
转子涡流方程：
$$\nabla \times (\nu \nabla \times \mathbf{A}) - j\omega_s\sigma\mathbf{A} = 0$$

等效电路参数提取：
- 定子电阻$R_1$
- 转子等效电阻$R_2'$（与滑差相关）
- 漏感$L_1, L_2'$
- 励磁电感$L_m$

### 接地系统分析

[[grounding-system]]中的FEM应用：

#### 接地电阻计算

复杂地质结构中的接地网分析：
$$R_g = \frac{V_g}{I_g} = \frac{\rho}{2\pi C}$$

其中$C$是接地网等效电容，通过FEM求解电流场获得。

#### 跨步电压和接触电压

地表电位分布：
$$\varphi(\mathbf{r}) = \int_{\Omega_g} \frac{\rho}{4\pi|\mathbf{r} - \mathbf{r}'|} \nabla \cdot \mathbf{J} \, d\Omega$$

安全评估：
- 跨步电压：$V_{step} = \varphi(x) - \varphi(x+s)$，$s = 1\text{m}$
- 接触电压：$V_{touch} = \varphi(x) - \varphi_{hand}}$

#### 暂态接地分析

考虑土壤电离的非线性电阻：
$$\rho(E) = \rho_0 \left(1 + \frac{E}{E_c}\right)^{-1}$$

雷击电流注入时的地电位升高（GPR）计算。

### 电缆系统建模

[[cable-model]]中的详细场分析：

#### 电容参数计算

多层介质电缆的电位分布：
$$-\nabla \cdot (\varepsilon(r) \nabla \varphi) = 0$$

导体表面电荷：
$$Q = \oint_{\Gamma_c} \varepsilon \frac{\partial \varphi}{\partial n} d\Gamma$$

电缆电容：
$$C = \frac{Q}{V_{rated}}$$

#### 涡流损耗

金属护套和铠装中的涡流：
- 单芯电缆护套感应电压
- 三芯电缆不对称引起的环流
- 邻近效应损耗

$$P_{sheath} = \int_{\Omega_s} \frac{1}{\sigma}|\mathbf{J}_{ind}|^2 d\Omega$$

#### 热场分析

载流量计算（IEC 60287等效）：
$$I = \sqrt{\frac{\Delta T - W_d[0.5T_1 + n(T_2 + T_3 + T_4)]}{RT_1 + nR(1+\lambda_1)T_2 + nR(1+\lambda_1+\lambda_2)(T_3+T_4)}}$$

FEM提供详细的热阻$T_i$计算。

#### 电缆群热分析

多根电缆并列敷设时的相互加热：
$$T_{surface} = T_{ambient} + \sum_j R_{th,ij} P_{loss,j}$$

FEM可考虑土壤非均匀性、回填材料等复杂条件。

## 与电路仿真的协同

### 参数提取流程

#### 频域参数提取

在多个频率点求解场方程，拟合宽频模型：
$$Z(f) = R(f) + j\omega L(f)$$

[[vector-fitting]]用于有理函数逼近：
$$Z(s) = R_0 + sL_0 + \sum_{k=1}^N \frac{R_k}{s - p_k}$$

#### 耦合系数矩阵

多绕组系统的电感矩阵：
$$\mathbf{L} = \begin{bmatrix} L_{11} & M_{12} & \cdots & M_{1n} \\ M_{21} & L_{22} & \cdots & M_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ M_{n1} & M_{n2} & \cdots & L_{nn} \end{bmatrix}$$

FEM计算各绕组单位电流激励下的磁链分布。

### 场路耦合方法

#### 直接耦合（Monolithic）

场和路的自由度联立求解：
$$\begin{bmatrix} \mathbf{K}_{ff} & \mathbf{K}_{fc} \\ \mathbf{K}_{cf} & \mathbf{K}_{cc} \end{bmatrix} \begin{bmatrix} \mathbf{u}_f \\ \mathbf{u}_c \end{bmatrix} = \begin{bmatrix} \mathbf{f}_f \\ \mathbf{f}_c \end{bmatrix}$$

其中下标$f$表示场自由度，$c$表示路自由度。

耦合矩阵$\mathbf{K}_{fc}$反映场-路界面条件：
- 电流源条件：绕组电流$\rightarrow$场源项
- 电压源条件：$\frac{d\Psi}{dt} = V_{terminal}$

#### 迭代耦合（Co-simulation）

场求解器和电路求解器交替迭代：

**步骤1**：从电路获取边界电流$\mathbf{I}^{(k)}$

**步骤2**：求解场方程得磁链$\Psi^{(k)} = \mathbf{L}(I^{(k)})\mathbf{I}^{(k)}$

**步骤3**：更新等效电路参数传给电路求解器

**步骤4**：求解电路方程得新电流$\mathbf{I}^{(k+1)}$

收敛判据：
$$\|\mathbf{I}^{(k+1)} - \mathbf{I}^{(k)}\| < \varepsilon$$

松弛加速：
$$\mathbf{I}^{(k+1)} = \alpha\mathbf{I}_{new} + (1-\alpha)\mathbf{I}^{(k)}$$

### 降阶模型（ROM）

#### 本征正交分解（POD）

基于快照数据的模型降阶：
$$\mathbf{u}(t) \approx \sum_{i=1}^r a_i(t)\boldsymbol{\phi}_i$$

其中$\boldsymbol{\phi}_i$是从快照矩阵$\mathbf{S} = [\mathbf{u}(t_1), \ldots, \mathbf{u}(t_n)]$提取的主模态。

SVD分解：
$$\mathbf{S} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^T$$

取前$r$个左奇异向量作为POD基。

#### Krylov子空间方法

矩匹配降阶：
$$\text{span}\{\mathbf{V}\} = \mathcal{K}_r(\mathbf{A}^{-1}\mathbf{E}, \mathbf{A}^{-1}\mathbf{b})$$

保持系统在特定频率范围内的响应特性。

#### 等效电路综合

从FEM提取参数构造SPICE兼容模型：
- RL ladder网络拟合频变阻抗
- 耦合电感模型
- 受控源实现非线性特性

## 方法对比

### FEM vs FDTD

[[fdtd]]对比分析：

| 特性 | FEM | FDTD |
|------|-----|------|
| 几何适应性 | 优秀（非结构网格） | 一般（阶梯近似） |
| 计算效率 | 高（大时间步长） | 受CFL条件限制 |
| 色散特性 | 低（谱精度可选） | 存在数值色散 |
| 非线性处理 | 方便（每时间步迭代） | 直接更新 |
| 内存需求 | 中等（稀疏矩阵） | 高（需存储整个网格） |
| 开放边界 | 需特殊处理 | 吸收边界条件 |

**选择建议**：
- 复杂几何 + 低频问题 $\rightarrow$ FEM
- 均匀介质 + 宽带分析 $\rightarrow$ FDTD

### FEM vs BEM

`bem`对比分析：

| 特性 | FEM | BEM |
|------|-----|-----|
| 问题维度 | 3D体网格 | 2D面网格（降维） |
| 矩阵性质 | 稀疏对称 | 稠密非对称 |
| 无限域处理 | 截断/吸收边界 | 自动满足 |
| 非线性材料 | 直接处理 | 需迭代/域分解 |
| 计算复杂度 | $O(N)$~$O(N^{1.5})$ | $O(N^2)$~$O(N\log N)$（快速算法） |
| 多物理场 | 方便耦合 | 较复杂 |

**选择建议**：
- 非线性/多物理场 $\rightarrow$ FEM
- 无限域/开放边界 $\rightarrow$ BEM
- 混合FEM-BEM结合两者优点

### 计算效率对比

**典型计算规模**：
- FEM：$10^5$~$10^7$自由度
- FDTD：$10^6$~$10^9$网格单元
- BEM：$10^4$~$10^6$边界单元

**加速技术**：
- FEM：多重网格、区域分解、GPU加速
- FDTD：MPI并行、CUDA加速
- BEM：快速多极子（FMM）、$\mathcal{H}$矩阵

## 软件工具

### 商业软件

**ANSYS Maxwell**：
- 2D/3D低频电磁场
- 涡流、静磁、静电分析
- 与Simplorer电路协同仿真
- 参数化优化设计

**JMAG**：
- 日本JSOL公司开发
- 电机专用，旋转机械优化
- 快速求解器，GPU支持
- 与控制系统联合仿真

**Flux**（Altair）：
- 法国CEDRAT开发
- 多物理场耦合（电磁-热-机械）
- 高级材料建模（各向异性、磁滞）
- 与Simulink接口

**COMSOL Multiphysics**：
- 多物理场平台
- 自定义偏微分方程
- 应用构建器（App开发）
- 与MATLAB深度集成

### 开源软件

**FEniCS Project**：
- Python/C++接口
- 自动代码生成
- 支持高阶有限元
- 并行计算

**MFEM**：
- 美国LLNL开发
- 高性能计算优化
- GPU支持
- AMR（自适应网格细化）

**Elmer**：
- 芬兰CSC开发
- 多物理场耦合
- GUI前处理
- 丰富的求解器

**GetDP**：
- 比利时开发
- 基于弱形式定义
- 适合学术研究
- 与Gmsh集成

## 工程应用最佳实践

### 网格划分策略

**变压器**：
- 绕组区域：精细网格（< 2mm）
- 铁心：中等网格（5-10mm）
- 油箱：粗网格（> 20mm）
- 气隙加密处理边缘效应

**电机**：
- 气隙：1-2层网格
- 定转子齿：3-4层网格
- 端部绕组：非结构网格

**接地系统**：
- 接地极附近：加密（< 0.1m）
- 远处：逐渐稀疏（10-100m）
- 土壤分层界面：对齐网格

### 求解器选择

**直接求解器**：
- 问题规模 $< 10^5$ 自由度
- 多右端项（参数扫描）
- PARDISO、MUMPS推荐

**迭代求解器**：
- 问题规模 $> 10^5$ 自由度
- ICCG（对称正定）
- GMRES+ILU（一般矩阵）
- 代数多重网格（AMG）

### 结果验证

**收敛性检验**：
- 网格细化研究
- 理查森外推
- 计算不确定度估计

**实验验证**：
- 短路阻抗比对
- 温升试验对比
- 局放起始电压验证

## 前沿发展方向

### 等几何分析（IGA）

使用CAD的NURBS基函数替代传统有限元形函数：
- 精确几何表示
- 高阶连续性
- 设计-分析一体化

### 模型降阶与机器学习

**数据驱动ROM**：
- 神经网络代理模型
- 物理信息神经网络（PINN）
- 算子学习（DeepONet、FNO）

**不确定性量化**：
- 随机有限元
- 多项式混沌展开
- 贝叶斯推断

### 高性能计算

**异构计算**：
- CPU-GPU协同
- 矩阵组装并行化
- 预处理并行化

**云原生仿真**：
- 容器化部署
- 弹性资源调度
- SaaS化CAE服务

## 相关方法
- [[fdtd]] - 时域有限差分法，适合均匀介质宽带分析
- `bem` - 边界元法，适合无限域和开放边界问题
- [[functional-mock-up-interface-based-approach-for-parallel-and-multistep-simulatio]] - 矩量法，适合天线辐射问题
- [[vector-fitting]] - 频变参数拟合，用于FEM-电路接口
- [[model-order-reduction]] - 模型降阶技术
- [[co-simulation]] - 场路协同仿真方法

## 来源论文

FEM在电力系统EMT仿真中的应用研究参见 [[index.md]] 相关文献，主要涵盖：
- 变压器电磁场分析（[[transformer-model]]相关来源）
- 接地系统数值计算（[[grounding-system]]相关来源）
- 电缆参数提取（[[cable-model]]相关来源）
- 场路耦合仿真方法（[[co-simulation]]相关来源）
