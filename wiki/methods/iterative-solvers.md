# 迭代求解方法 (Iterative Solvers)

## 定义与概述

迭代求解方法（Iterative Solvers）是通过逐步逼近而非直接计算来求解非线性方程组和大型线性方程组的数值技术。在EMT仿真中，迭代方法主要应用于：非线性元件（开关、避雷器、饱和变压器）的牛顿-拉夫逊迭代、隐式积分方法的非线性方程求解、大型系统的高效线性求解（CG/GMRES/BiCGSTAB等），以及混合仿真接口的迭代协调。与直接法（LU分解）相比，迭代法具有内存需求低、适合并行、可扩展性好等优势，是大规模电力系统EMT仿真的关键技术。

## 1. 理论基础

### 1.1 迭代法基本原理

**核心思想**：从初始猜测出发，通过迭代格式逐步逼近精确解。

**一般形式**：
$$x^{(k+1)} = F(x^{(k)})$$

**收敛条件**：
$$\|x^{(k+1)} - x^{*}\| \leq \rho \|x^{(k)} - x^{*}\|, \quad \rho < 1$$

其中$\rho$为收敛因子，$\rho$越小收敛越快。

**迭代法分类**：
| 类型 | 适用问题 | 代表方法 | 收敛特性 |
|------|----------|----------|----------|
| **固定点迭代** | 非线性方程 | Picard迭代 | 线性收敛 |
| **牛顿法族** | 非线性方程组 | Newton-Raphson | 二次收敛 |
| **Krylov子空间** | 大型线性系统 | CG/GMRES/BiCGSTAB | 超线性收敛 |
| **多重网格** | 偏微分方程 | AMG/GMG | 网格无关收敛 |

### 1.2 牛顿-拉夫逊方法

**单变量牛顿法**：
$$x^{(k+1)} = x^{(k)} - \frac{f(x^{(k)})}{f'(x^{(k)})}$$

**多变量牛顿法**：
$$x^{(k+1)} = x^{(k)} - J^{-1}(x^{(k)})F(x^{(k)})$$

其中$J$为雅可比矩阵：
$$J_{ij} = \frac{\partial F_i}{\partial x_j}$$

**简化牛顿法**：
固定雅可比矩阵（仅每步或数步更新）：
$$J_0 \Delta x^{(k)} = -F(x^{(k)})$$

减少LU分解次数，适用于弱非线性系统。

**阻尼牛顿法**：
$$x^{(k+1)} = x^{(k)} + \lambda_k \Delta x^{(k)}$$

通过线搜索确定阻尼因子$\lambda_k$，增强全局收敛性。

**收敛判据**：
$$\|F(x^{(k)})\| < \epsilon_{abs} \quad \text{或} \quad \frac{\|\Delta x^{(k)}\|}{\|x^{(k)}\|} < \epsilon_{rel}$$

### 1.3 雅可比矩阵与预处理

**雅可比矩阵结构**（EMT节点分析）：
$$J = I - h\beta \frac{\partial f}{\partial x} = I - h\beta Y_{NL}$$

其中$Y_{NL}$为非线性元件导纳。

**预处理技术**：
对于大型系统，直接求解$J \Delta x = -F$代价高昂。

**不完全LU预处理（ILU）**：
$$M = \tilde{L}\tilde{U} \approx J$$

预处理后的系统：
$$M^{-1}J \Delta x = -M^{-1}F$$

条件数改善，迭代收敛加速。

**块对角预处理**：
$$M = \text{diag}(J_{11}, J_{22}, ..., J_{nn})$$

适合分块对角占优系统。

**不完全Cholesky（IC）**：
对称正定系统的预处理选择。

### 1.4 Krylov子空间方法

**共轭梯度法（CG）**：
对称正定系统的最优方法。

收敛速率：
$$\|x^{(k)} - x^{*}\|_A \leq 2\left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^k \|x^{(0)} - x^{*}\|_A$$

其中$\kappa = \lambda_{max}/\lambda_{min}$为条件数。

**GMRES（广义最小残差）**：
非对称系统的标准方法。

**BiCGSTAB**：
双共轭梯度稳定化版本，适合非对称不定系统。

**预条件Krylov方法**（EMT常用）：
```
求解：Ax = b

预处理后：M^{-1}Ax = M^{-1}b

迭代格式：
  r_0 = b - Ax_0
  z_0 = M^{-1}r_0
  p_0 = z_0
  for k = 0, 1, 2, ...
    α_k = (r_k^T z_k) / (p_k^T A p_k)
    x_{k+1} = x_k + α_k p_k
    r_{k+1} = r_k - α_k A p_k
    if ||r_{k+1}|| < tol: break
    z_{k+1} = M^{-1}r_{k+1}
    β_k = (r_{k+1}^T z_{k+1}) / (r_k^T z_k)
    p_{k+1} = z_{k+1} + β_k p_k
```

## 2. EMT仿真应用

### 2.1 非线性元件牛顿迭代

**饱和变压器建模**：
非线性磁化特性：$\Phi = f(i_m)$

牛顿迭代：
$$i_m^{(k+1)} = i_m^{(k)} - \frac{\Phi(i_m^{(k)}) - \Phi_{target}}{d\Phi/di_m}$$

**避雷器非线性电阻**：
$$V = C I^\alpha$$

牛顿-拉夫逊求解：
$$I^{(k+1)} = I^{(k)} - \frac{C(I^{(k)})^\alpha - V}{\alpha C(I^{(k)})^{\alpha-1}}$$

**开关分段线性化**（2006 GENE方法）：
将非线性V-I特性分段线性近似，避免迭代：
- 导通区：$R = R_{on}$
- 关断区：$R = R_{off}$
- 过渡区：线性插值

**量化收敛**：
| 非线性程度 | 迭代次数 | 收敛策略 |
|------------|----------|----------|
| 弱非线性 | 2-3次 | 简化牛顿 |
| 中等非线性 | 3-5次 | 标准牛顿 |
| 强非线性 | 5-10次 | 阻尼牛顿 |

### 2.2 隐式积分非线性求解

**后向欧拉非线性方程**：
$$x_{n+1} = x_n + h f(x_{n+1})$$

改写为：
$$F(x_{n+1}) = x_{n+1} - x_n - h f(x_{n+1}) = 0$$

牛顿迭代：
$$J^{(k)} \Delta x^{(k)} = -F(x^{(k)})$$

其中雅可比：
$$J = I - h \frac{\partial f}{\partial x}$$

**预测-校正策略**：
```
预测（Predictor）：
  x^(0) = x_n + h f(x_n)  （显式欧拉）

校正（Corrector）：
  for k = 0, 1, ..., max_iter
    F = x^(k) - x_n - h f(x^(k))
    if ||F|| < tol: break
    J = I - h ∂f/∂x
    solve J Δx = -F
    x^(k+1) = x^(k) + Δx
```

**梯形法非线性求解**：
$$F(x_{n+1}) = x_{n+1} - x_n - \frac{h}{2}[f(x_n) + f(x_{n+1})] = 0$$

雅可比相同形式：$J = I - \frac{h}{2}\frac{\partial f}{\partial x}$

### 2.3 大型线性系统Krylov求解

**FDNE等值网络**：
大规模外部网络等值后，导纳矩阵维度$N$可达$10^4$-$10^5$。

**直接法vs迭代法**：
| 特性 | 直接法（LU） | 迭代法（GMRES） |
|------|--------------|-----------------|
| 内存需求 | $O(N^2)$（填充） | $O(N)$ |
| 计算复杂度 | $O(N^3)$ | $O(kN)$（$k$为迭代次数） |
| 并行性 | 差 | 好 |
| 预处理 | 可选 | 必需 |
| 适用规模 | $N < 10^5$ | $N > 10^4$ |

**ILU-GMRES实现**（EMT大规模系统）：
```
预计算阶段：
  ILU分解：M = LU ≈ A

每步迭代：
  1. 求解Mz = r（前代回代）
  2. Krylov子空间投影
  3. 收敛判断
```

**KLU+迭代混合策略**（10,000+节点）：
- 子网内部：KLU直接求解（稀疏优化）
- 边界网络：GMRES迭代求解（避免稠密化）

### 2.4 混合仿真接口迭代

**机电-电磁混合仿真迭代**（ADPSS实现）：

TSA侧（机电）：
$$\dot{\delta} = \omega - \omega_s$$

EMT侧（电磁）：
$$Y_{FDNE} V_{bus} = I_{inj}$$

**串行迭代时序**：
```
迭代1：
  TSA → 计算等值电压源 V^(0)
        传递给EMT
  EMT → 用V^(0)求解网络，得注入电流I^(0)
        传递给TSA

迭代2：
  TSA → 用I^(0)更新等值，得V^(1)
  EMT → 用V^(1)求解，得I^(1)

直到收敛：|I^(k) - I^(k-1)| < tol
```

**并行迭代时序**（Jacobi型）：
```
同时求解：
  TSA → 基于上一时步边界量求解
  EMT → 基于上一时步边界量求解

交换边界量：
  TSA ← EMT 电压/电流
  EMT ← TSA 电压/电流

收敛判断：边界量变化<阈值
```

**量化结果**（ADPSS）：
- 并行时序：3-5次迭代收敛
- 功率偏差：<0.1%
- 10,000+节点、1,000+发电机规模

### 2.5 移频仿真复数迭代

**复数方程求解**（2022 高仕林）：
复包络域节点方程：
$$(G + jB)V = I$$

**复数Krylov方法**：
将复数方程转换为实数形式：
$$\begin{bmatrix} G & -B \\ B & G \end{bmatrix} \begin{bmatrix} V_r \\ V_i \end{bmatrix} = \begin{bmatrix} I_r \\ I_i \end{bmatrix}$$

或直接用复数运算求解（更快）。

**IEEE 9241节点测试**：
- 复数形式：8.15s
- 矩阵形式：21.59s
- 加速比：2.65倍

## 3. 实现技术

### 3.1 收敛加速技术

**不完全LU分解（ILU）**：
```c
void ILU_factorize(A, L, U) {
    for i = 0 to n-1:
        for k = 0 to i-1 where A[i][k] != 0:
            L[i][k] = A[i][k] / U[k][k]
            for j = k+1 to n-1 where A[i][j] != 0:
                A[i][j] -= L[i][k] * U[k][j]
        for j = i to n-1 where A[i][j] != 0:
            U[i][j] = A[i][j]
}
```

**阈值控制（ILU(tol)）**：
丢弃小于tol的元素，控制填充。

**雅可比更新策略**：
| 策略 | 更新频率 | 适用场景 |
|------|----------|----------|
| 每迭代更新 | 每次 | 强非线性 |
| 每步更新 | 每时步 | 中等非线性 |
| 每多步更新 | 5-10步 | 弱非线性 |
| 固定雅可比 | 永不 | 线性系统 |

### 3.2 多重网格方法

**基本思想**：
- 细网格上光滑高频误差
- 粗网格上修正低频误差
- 递归形成网格层级

**V循环**：
```
细网格 → 前光滑（Jacobi/Gauss-Seidel）
       → 限制到粗网格
粗网格 → 求解（直接法或递归）
       → 延拓到细网格
细网格 → 后光滑
```

**EMT应用**：
- 变压器有限元建模
- 电缆电磁场分析
- 适合空间离散后的椭圆型方程

### 3.3 并行迭代策略

**Krylov子空间并行**：
- 矩阵-向量乘法并行（行划分）
- 内积运算全局通信
- 适合多核/GPU

**区域分解法**：
将系统分割为子域，子域边界迭代协调：
$$A_i x_i = b_i + \lambda_i$$

**异步迭代**：
各子系统独立迭代，周期同步边界量，适合分布式计算。

## 4. 仿真软件实现

### 4.1 EMTP-RV实现

**牛顿迭代核心**：
```fortran
! 非线性支路牛顿求解
SUBROUTINE NEWTON_SOLVE(V, I, TOL, MAX_ITER)
    REAL V, I, TOL
    INTEGER MAX_ITER
    
    DO K = 1, MAX_ITER
        ! 计算残差
        F = V - R_NONLIN(I) * I - V_SOURCE
        
        ! 检查收敛
        IF (ABS(F) < TOL) EXIT
        
        ! 计算雅可比（导数）
        J = 1.0 - R_NONLIN(I) - I * dR/dI
        
        ! 更新
        DI = -F / J
        I = I + DI
    END DO
END SUBROUTINE
```

**开关迭代处理**：
分段线性化避免迭代（2006 GENE方法）。

### 4.2 PETSc实现（开源）

**Krylov求解器配置**：
```c
// 创建KSP对象
KSPCreate(PETSC_COMM_WORLD, &ksp);

// 设置求解器类型
KSPSetType(ksp, KSPGMRES);  // GMRES

// 设置预处理器
KSPGetPC(ksp, &pc);
PCSetType(pc, PCILU);  // ILU预处理

// 求解
KSPSolve(ksp, b, x);
```

**并行Krylov**：
```c
// 矩阵并行分布
MatCreateMPIAIJ(comm, m, n, M, N, d_nz, d_nnz, o_nz, o_nnz, &A);

// 向量并行分布
VecCreateMPI(comm, n, N, &x);
```

### 4.3 MATLAB实现

**牛顿法自定义**：
```matlab
function x = newton_solve(F, J, x0, tol, max_iter)
    x = x0;
    for k = 1:max_iter
        F_val = F(x);
        if norm(F_val) < tol
            break;
        end
        J_val = J(x);
        dx = -J_val \ F_val;
        x = x + dx;
    end
end
```

**内置迭代求解器**：
```matlab
% GMRES求解
x = gmres(A, b, restart, tol, maxit, M);

% 预处理器
M = ilu(A, struct('type', 'ilutp', 'droptol', 1e-6));
```

## 5. 典型参数参考

### 5.1 迭代收敛参数

| 应用场景 | 最大迭代 | 绝对容差 | 相对容差 | 预处理器 |
|----------|----------|----------|----------|----------|
| 饱和变压器 | 5-10 | 1e-6 | 1e-4 | ILU(0) |
| 避雷器 | 3-5 | 1e-4 | 1e-3 | 对角 |
| 大型线性系统 | 100-1000 | 1e-10 | 1e-8 | ILU(tol) |
| 混合仿真接口 | 3-10 | 1e-3 | 1e-2 | 无需 |
| 实时仿真 | 1-3 | 1e-2 | 1e-2 | 固定雅可比 |

### 5.2 求解器选择指南

| 矩阵特性 | 推荐方法 | 预处理 | 理由 |
|----------|----------|--------|------|
| 对称正定 | CG | IC | 最优收敛 |
| 对称不定 | MINRES | 对角 | 稳定性好 |
| 非对称 | GMRES | ILU | 通用性强 |
| 非对称（短迭代） | BiCGSTAB | ILU | 存储低 |
| 大规模稀疏 | GMRES+AMG | 代数多重网格 | 可扩展性 |

## 6. 相关主题与链接

### 6.1 相关方法
- [[sparse-matrix-solver|稀疏矩阵求解]] - 直接法与迭代法对比
- [[discretization-methods|离散化方法]] - 隐式积分非线性求解
- [[numerical-integration|数值积分]] - 预测-校正迭代框架
- [[stiff-system-handling|刚性系统处理]] - 牛顿迭代在刚性系统中的应用
- [[electromechanical-electromagnetic-hybrid-simulation|机电-电磁混合仿真]] - 接口迭代协调

### 6.2 相关模型
- [[transformer-model|变压器模型]] - 饱和特性牛顿迭代
- [[surge-arrester-model|避雷器]] - 非线性电阻迭代求解
- [[igbt-model|IGBT模型]] - 详细模型中的非线性迭代

### 6.3 相关主题
- [[parallel-computing|并行计算]] - Krylov并行实现
- [[real-time-simulation|实时仿真]] - 实时约束下的迭代策略

## 7. 适用边界与限制

### 7.1 适用条件

**迭代法优势场景**：
- **大规模系统**：$N > 10^4$，矩阵稀疏
- **并行环境**：分布式/多核计算
- **内存受限**：直接法填充过多
- **弱非线性**：牛顿迭代收敛快
- **多物理场**：多域耦合迭代

**直接法优势场景**：
- **中小规模**：$N < 10^4$
- **多右端项**：单一矩阵多求解
- **强非线性**：雅可比频繁变化
- **实时仿真**：确定性计算时间

### 7.2 失效边界

**迭代法失效信号**：
- 迭代次数超过限制（不收敛）
- 残差振荡或发散
- 条件数过大（$\kappa > 10^{12}$）
- 预处理失效（M近似性差）

**应对策略**：
| 问题 | 解决方案 |
|------|----------|
| 不收敛 | 改进预处理、阻尼牛顿 |
| 收敛慢 | 更好的初始猜测、自适应步长 |
| 条件数大 | 标度化、改进预处理 |
| 预处理差 | ILU(tol)调参、块预处理 |

### 7.3 精度边界

| 方法 | 局部收敛 | 全局收敛 | 每步计算量 |
|------|----------|----------|-----------|
| Picard | 线性 | 弱 | 低 |
| 牛顿 | 二次 | 局部 | 中（需LU） |
| 简化牛顿 | 线性 | 局部 | 低 |
| 阻尼牛顿 | 二次 | 强 | 中（线搜索） |
| Krylov | 超线性 | 依赖预处理 | 依赖矩阵向量积 |

**误差控制**：
- 非线性求解：相对误差$< 10^{-6}$
- 线性求解：相对误差$< 10^{-10}$
- 混合接口：功率误差$< 0.1\%$

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Nested fast and simultaneous solution for time-domain simulation | 2006 | GENE方法，分段线性化避免非线性迭代，预计算开关状态，提速23% |
| The implementation and effectiveness of linear interpolation | 2003 | PSCAD插值算法，牛顿迭代框架内精确开关定位，消除数值振荡 |
| 电力系统移频电磁暂态仿真原理及应用综述 | 2022 | 复数方程Krylov求解，复数形式比矩阵形式快2.65倍 |
| KLU: A sparse high performance linear algebra solver | 2004 | 稀疏直接法+迭代混合策略，10,000+节点实时仿真 |
| 交直流电力系统分割并行电磁暂态仿真 | 2011 | 区域分解迭代，分网并行，Krylov子空间协调边界 |

## 相关模型

- [[transformer-model|变压器模型]] - 饱和特性非线性迭代求解
- [[surge-arrester-model|避雷器模型]] - 非线性电阻特性迭代处理
- [[igbt-model|IGBT模型]] - 详细模型中的非线性方程迭代
- [[mmc-model|MMC模型]] - 大规模系统Krylov子空间迭代求解
- [[fdne-model|FDNE模型]] - 大型等值网络迭代优化

## 相关主题

- [[parallel-computing|并行计算]] - Krylov子空间并行实现技术
- [[real-time-simulation|实时仿真]] - 实时约束下的迭代策略
- [[electromechanical-electromagnetic-hybrid-simulation|机电-电磁混合仿真]] - 接口迭代协调方法
- [[sparse-matrix-solver|稀疏矩阵求解]] - 直接法与迭代法对比

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*
