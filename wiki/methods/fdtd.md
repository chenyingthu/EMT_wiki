---
title: "时域有限差分法 (FDTD)"
type: method
tags: [fdtd, finite-difference, electromagnetic, full-wave, simulation]
created: "2026-05-02"
---

# 时域有限差分法 (FDTD)

## 概述

时域有限差分法(Finite-Difference Time-Domain, FDTD)是由Kane Yee于1966年提出的电磁场数值计算方法。FDTD直接在时域求解麦克斯韦方程组，通过将空间和时间离散化，计算电磁场在空间中的传播和分布，广泛应用于高频暂态、电磁兼容和天线设计等领域。

FDTD方法的核心优势在于其直接时域求解特性，能够一次计算获得宽频带响应，无需像频域方法那样逐点扫描频率。该方法在电力系统中的应用包括[[lightning-transient-analysis]]、`substation-design`、`giscorona`等。

## 理论基础

### 麦克斯韦方程组

FDTD的理论基础是麦克斯韦方程组，描述了电磁场的基本规律。在时域形式下，麦克斯韦旋度方程为：

$$\nabla \times \mathbf{E} = -\mu \frac{\partial \mathbf{H}}{\partial t}$$

$$\nabla \times \mathbf{H} = \varepsilon \frac{\partial \mathbf{E}}{\partial t} + \sigma \mathbf{E} + \mathbf{J}$$

其中：
- $\mathbf{E}$: 电场强度矢量 (V/m)
- $\mathbf{H}$: 磁场强度矢量 (A/m)
- $\varepsilon$: 介电常数 (F/m)
- $\mu$: 磁导率 (H/m)
- $\sigma$: 电导率 (S/m)
- $\mathbf{J}$: 外部电流源 (A/m²)

在直角坐标系中，旋度方程可展开为六个标量方程：

**电场更新方程：**
$$\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} - \sigma E_x - J_x\right)$$

$$\frac{\partial E_y}{\partial t} = \frac{1}{\varepsilon}\left(\frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x} - \sigma E_y - J_y\right)$$

$$\frac{\partial E_z}{\partial t} = \frac{1}{\varepsilon}\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y} - \sigma E_z - J_z\right)$$

**磁场更新方程：**
$$\frac{\partial H_x}{\partial t} = \frac{1}{\mu}\left(\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}\right)$$

$$\frac{\partial H_y}{\partial t} = \frac{1}{\mu}\left(\frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z}\right)$$

$$\frac{\partial H_z}{\partial t} = \frac{1}{\mu}\left(\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right)$$

### Yee网格结构

Yee提出的交错网格结构是FDTD方法的核心创新。在三维Yee网格中，电场和磁场分量在空间上交错排列：

**电场分量位置：**
- $E_x$: 位于 $(i+1/2, j, k)$，即x方向棱边中点
- $E_y$: 位于 $(i, j+1/2, k)$，即y方向棱边中点
- $E_z$: 位于 $(i, j, k+1/2)$，即z方向棱边中点

**磁场分量位置：**
- $H_x$: 位于 $(i, j+1/2, k+1/2)$，即yz平面上方中心
- $H_y$: 位于 $(i+1/2, j, k+1/2)$，即xz平面上方中心
- $H_z$: 位于 $(i+1/2, j+1/2, k)$，即xy平面上方中心

这种交错排列保证了：
1. 每个电场分量被四个磁场分量环绕（法拉第定律）
2. 每个磁场分量被四个电场分量环绕（安培定律）
3. 自然满足散度条件（无源区域）
4. 二阶精度中心差分

## 离散麦克斯韦方程推导

### 时间离散化

FDTD采用蛙跳(leap-frog)时间步进格式，电场和磁场在时间上交替更新：
- 电场在整数时间步 $t = n\Delta t$ 计算
- 磁场在半整数时间步 $t = (n+1/2)\Delta t$ 计算
- 时间步长 $\Delta t$ 需满足稳定性条件

### 空间离散化

使用中心差分近似空间导数，具有二阶精度：
$$\frac{\partial f}{\partial x}\bigg|_{x=x_i} \approx \frac{f(x_i+\Delta x/2) - f(x_i-\Delta x/2)}{\Delta x}$$

### 完整离散方程

**x方向电场更新：**
$$E_x^{n+1}(i+1/2,j,k) = C_a \cdot E_x^n(i+1/2,j,k) + C_b \cdot \left[\frac{H_z^{n+1/2}(i+1/2,j+1/2,k) - H_z^{n+1/2}(i+1/2,j-1/2,k)}{\Delta y} - \frac{H_y^{n+1/2}(i+1/2,j,k+1/2) - H_y^{n+1/2}(i+1/2,j,k-1/2)}{\Delta z}\right] - C_c \cdot J_x^{n+1/2}(i+1/2,j,k)$$

其中更新系数：
$$C_a = \frac{1 - \sigma\Delta t/(2\varepsilon)}{1 + \sigma\Delta t/(2\varepsilon)}$$
$$C_b = \frac{\Delta t/\varepsilon}{1 + \sigma\Delta t/(2\varepsilon)}$$
$$C_c = \frac{\Delta t/\varepsilon}{1 + \sigma\Delta t/(2\varepsilon)}$$

**x方向磁场更新：**
$$H_x^{n+1/2}(i,j+1/2,k+1/2) = D_a \cdot H_x^{n-1/2}(i,j+1/2,k+1/2) + D_b \cdot \left[\frac{E_y^n(i,j+1/2,k+1) - E_y^n(i,j+1/2,k)}{\Delta z} - \frac{E_z^n(i,j+1,k+1/2) - E_z^n(i,j,k+1/2)}{\Delta y}\right]$$

其中更新系数：
$$D_a = \frac{1 - \sigma_m\Delta t/(2\mu)}{1 + \sigma_m\Delta t/(2\mu)}$$
$$D_b = \frac{\Delta t/\mu}{1 + \sigma_m\Delta t/(2\mu)}$$

y和z方向的更新方程可通过对称性推导得到。

## 稳定性条件

### Courant稳定性条件

FDTD显式时间步进要求时间步长满足Courant-Friedrichs-Lewy (CFL)条件：

$$\Delta t \leq \frac{1}{c\sqrt{\frac{1}{(\Delta x)^2} + \frac{1}{(\Delta y)^2} + \frac{1}{(\Delta z)^2}}}$$

对于均匀立方网格 ($\Delta x = \Delta y = \Delta z = \Delta$)：
$$\Delta t \leq \frac{\Delta}{c\sqrt{3}}$$

其中：
- $c = 1/\sqrt{\mu\varepsilon}$: 介质中的光速
- $\Delta x, \Delta y, \Delta z$: 空间网格步长

**物理意义：** CFL条件要求在一个时间步内，波传播距离不超过一个网格单元。违反此条件会导致数值解指数增长而发散。

### 数值色散

离散化引入的数值色散误差可用数值波数描述。对于平面波 $e^{j(\omega t - k_x x - k_y y - k_z z)}$，数值色散关系为：

$$\left(\frac{1}{c\Delta t}\sin\frac{\omega\Delta t}{2}\right)^2 = \left(\frac{\sin(k_x\Delta x/2)}{\Delta x}\right)^2 + \left(\frac{\sin(k_y\Delta y/2)}{\Delta y}\right)^2 + \left(\frac{\sin(k_z\Delta z/2)}{\Delta z}\right)^2$$

**减小色散的措施：**
1. 增加每波长网格数（至少10-20个网格/波长）
2. 使用更精细的时间步长
3. 采用高阶差分格式
4. 使用均匀网格（减少各向异性色散）

### 数值稳定性分析

使用von Neumann稳定性分析，设解的形式为：
$$E^n = E_0 \cdot g^n \cdot e^{j\mathbf{k}\cdot\mathbf{r}}$$

放大因子 $g$ 必须满足 $|g| \leq 1$ 以保证稳定。对于无损介质：
$$g = 1 - 2s^2 \pm 2s\sqrt{s^2 - 1}$$

其中 $s = c\Delta t \sqrt{\sum (\sin^2(k_i\Delta_i/2)/\Delta_i^2)}$。当CFL条件满足时，$s \leq 1$，保证 $|g| = 1$（无耗散稳定）。

## 三维Yee网格详细结构

### 基本Yee单元

三维Yee单元是一个包含12个场分量的结构体：

```
         Hz(i+1/2,j+1/2,k)
              |
              v
    Ey(i,j+1/2,k) -- Ez(i,j,k+1/2)
         |              |
         v              v
    Ex(i+1/2,j,k) -- Hx(i,j+1/2,k+1/2)
              |
              v
         Hy(i+1/2,j,k+1/2)
```

### 网格索引约定

**整数网格点** $(i, j, k)$：对应空间位置 $(x_i, y_j, z_k)$

**电场存储位置：**
```
Ex[NX-1][NY][NZ]    // x方向棱边: (i+0.5, j, k)
Ey[NX][NY-1][NZ]    // y方向棱边: (i, j+0.5, k)
Ez[NX][NY][NZ-1]    // z方向棱边: (i, j, k+0.5)
```

**磁场存储位置：**
```
Hx[NX][NY-1][NZ-1]  // yz平面中心: (i, j+0.5, k+0.5)
Hy[NX-1][NY][NZ-1]  // xz平面中心: (i+0.5, j, k+0.5)
Hz[NX-1][NY-1][NZ]  // xy平面中心: (i+0.5, j+0.5, k)
```

### 材料参数配置

在Yee网格中，材料参数位于不同位置：
- $\varepsilon, \sigma$: 与电场共位（棱边中点）
- $\mu, \sigma_m$: 与磁场共位（面中心）

对于非均匀材料，需要进行体积平均：
$$\varepsilon_{eff} = \frac{\sum \varepsilon_i V_i}{\sum V_i}$$

其中 $V_i$ 是材料 $i$ 在Yee单元中的体积份额。

## 边界条件处理

### 理想电导体边界 (PEC)

PEC边界条件要求切向电场为零：
$$\mathbf{n} \times \mathbf{E} = 0$$

**实现方法：**
```
边界外一层设置:
E_tangential = 0
H_normal = 0
```

对于 $x=0$ 处的PEC边界：
$$E_y(0, j+1/2, k) = 0$$
$$E_z(0, j, k+1/2) = 0$$

磁场更新时使用镜像理论：
$$H_y^{n+1/2}(0, j, k+1/2) = H_y^{n-1/2}(0, j, k+1/2) + \frac{\Delta t}{\mu\Delta x}E_z^n(1, j, k+1/2)$$

### 理想磁导体边界 (PMC)

PMC边界条件要求切向磁场为零：
$$\mathbf{n} \times \mathbf{H} = 0$$

用于模拟对称面，可减少计算域。在PMC边界处，法向电场分量为零。

### 完全匹配层 (PML)

PML是吸收边界的标准实现，由Berenger于1994年提出。其核心思想是在边界区域引入人工损耗，使入射波无反射地衰减。

**分裂场PML：**
将场分量分裂为两个子分量，例如 $E_x = E_{xy} + E_{xz}$，并引入电导率剖面：

$$\sigma_x(x) = \sigma_{max}\left(\frac{x}{d}\right)^m$$

其中：
- $d$: PML厚度
- $m$: 剖面阶数（通常2-4）
- $\sigma_{max}$: 最大电导率

**更新方程（分裂场）：**
$$E_{xy}^{n+1} = e^{-\sigma_y\Delta t/\varepsilon}E_{xy}^n + \frac{1 - e^{-\sigma_y\Delta t/\varepsilon}}{\sigma_y\Delta y}\left(H_z^{n+1/2}|_{y+} - H_z^{n+1/2}|_{y-}\right)$$

**性能参数：**
- 典型反射系数：-40dB ~ -80dB
- 推荐PML厚度：8-16层网格
- 最优 $\sigma_{max} = (m+1)/(150\pi\Delta)$

**CPML (卷积PML)：**
使用递归卷积代替场分裂，保持麦克斯韦方程完整性：
$$\psi_{E_x} = b\psi_{E_x} + a(E_z^{n}|_{y+} - E_z^{n}|_{y-})$$
$$E_x^{n+1} = E_x^n + \frac{\Delta t}{\varepsilon\Delta y}\left[(H_z^{n+1/2}|_{y+} - H_z^{n+1/2}|_{y-}) + \psi_{E_x}\right]$$

## 激励源设置

### 电压源激励

在指定位置注入电压信号：
$$E_z(i, j, k+1/2) = \frac{V_{source}(t)}{\Delta z}$$

**硬源 vs 软源：**
- **硬源**：直接设置场值（会反射回波）
- **软源**：叠加到场值上（$E = E_{FDTD} + E_{source}$）

**总场/散射场技术：**
将计算域分为总场区和散射场区，在连接边界注入平面波：
$$E_{total} = E_{incident} + E_{scattered}$$

### 电流源激励

在指定棱边注入电流密度：
$$J_x^{n+1/2}(i+1/2, j, k) = I_{source}(t)/A$$

其中 $A$ 是棱边截面积。

### 平面波激励

用于散射问题分析：
$$\mathbf{E}_{inc} = \mathbf{E}_0 e^{j(\omega t - \mathbf{k}\cdot\mathbf{r})}$$

入射方向由波矢量 $\mathbf{k}$ 确定：
$$k_x = k_0\sin\theta\cos\phi$$
$$k_y = k_0\sin\theta\sin\phi$$
$$k_z = k_0\cos\theta$$

## 材料模型

### 色散材料

实际介质介电常数随频率变化，常用Drude模型或Lorentz模型描述。

**Drude模型（金属、等离子体）：**
$$\varepsilon(\omega) = \varepsilon_\infty - \frac{\omega_p^2}{\omega^2 - j\omega\gamma}$$

**辅助微分方程(ADE)实现：**
引入极化电流 $J_p$，求解：
$$\frac{dJ_p}{dt} + \gamma J_p = \varepsilon_0\omega_p^2 E$$

与麦克斯韦方程耦合求解。

**Lorentz模型（谐振介质）：**
$$\varepsilon(\omega) = \varepsilon_\infty + \frac{(\varepsilon_s - \varepsilon_\infty)\omega_0^2}{\omega_0^2 + 2j\omega\delta - \omega^2}$$

### 非线性材料

**Kerr非线性：**
$$\varepsilon = \varepsilon_0\left(\varepsilon_r + \chi^{(3)}|E|^2\right)$$

需要迭代求解或使用预测-校正方法。

**非线性更新：**
$$E^{n+1} = \frac{C_a E^n + C_b (\nabla \times H)^{n+1/2}}{1 + C_b \chi^{(3)}|E^n|^2}$$

### 各向异性材料

张量介电常数：
$$\overline{\varepsilon} = \begin{bmatrix} \varepsilon_{xx} & \varepsilon_{xy} & \varepsilon_{xz} \\ \varepsilon_{yx} & \varepsilon_{yy} & \varepsilon_{yz} \\ \varepsilon_{zx} & \varepsilon_{zy} & \varepsilon_{zz} \end{bmatrix}$$

需要求解3×3方程组更新电场分量。

## 在电力系统中的应用

### 变电站电磁场分析

**应用场景：**
- 母线、设备周围的工频电场分布
- 变压器、电抗器周围的磁场分布
- 工作人员电磁暴露评估
- 电磁兼容设计验证

**建模要点：**
1. 精确几何建模（考虑导体半径、间距）
2. 大地建模（有限电导率影响）
3. 设备简化等效
4. 频率范围：50Hz-数MHz（谐波）

**结果输出：**
- 电场强度云图
- 磁场强度分布
- 指定路径的场强曲线
- 与IEEE/ICNIRP标准对比

### 雷电暂态分析

[[lightning-transient-analysis]]是FDTD在电力系统中最重要的应用之一。

**雷击通道建模：**
- 采用传输线模型或电阻率模型
- 考虑先导发展过程
- 回击电流波形：双指数或Heidler模型

$$i(t) = \frac{I_m}{\eta} \cdot \frac{(t/\tau_1)^{10}}{1 + (t/\tau_1)^{10}} \cdot e^{-t/\tau_2}$$

**雷电电磁脉冲(LEMP)计算：**
- 空间电场分布
- 感应电压计算
- 屏蔽效能评估
- 二次感应过电压

**接地系统分析：**
- 接地网电流分布
- 地电位升高(GPR)
- 接触电压、跨步电压
- 土壤电离效应（非线性）

### GIS快速暂态过电压(VFTO)分析

`very-fast-transient`过电压是GIS中的特殊问题。

**VFTO特性：**
- 上升时间：ns级
- 幅值：2-3 p.u.
- 频率成分：数百MHz

**FDTD建模：**
1. GIS腔体几何精确建模
2. 隔离开关操作建模（时变阻抗）
3. 盆式绝缘子介电特性
4. 波阻抗不连续点处理

**关键分析内容：**
- 波在GIS管道内的传播
- 绝缘子上的电压分布
- 盆式绝缘子三结合点电场
- 对外壳的暂态感应电压

### 电缆系统电磁分析

[[underground-cable-modeling]]与[[cable-modeling]]相关内容。

**分析内容：**
- 电缆周围电场分布
- 金属护层感应电压
- 护层环流计算
- 电磁干扰评估

**交叉互联系统建模：**
- 护层接地方式
- 交叉互联箱建模
- 护层电压不平衡

**暂态分析：**
- 开关操作过电压
- 短路故障暂态
- 谐波电流分布

### 输电线电磁环境

**工频电磁场：**
- 走廊电场分布
- 磁场强度计算
- 居民暴露评估

**电晕分析：**
- 电晕电流脉冲
- 无线电干扰预测
- 可听噪声计算

## 场路耦合与混合仿真

### FDTD与电路仿真耦合

`field-circuit-coupling`是电力系统仿真的重要技术。

**耦合方式：**
1. **端口耦合**：在FDTD域中定义集总端口
2. **子域耦合**：将电路方程嵌入FDTD网格
3. **外部耦合**：通过接口文件交换数据

**集总端口模型：**
在FDTD网格中引入等效电路元件：
$$V_{port} = -L\frac{\partial I}{\partial t} - RI + V_{source}$$

转换为FDTD更新方程：
$$I^{n+1/2} = I^{n-1/2} + \frac{\Delta t}{L}(V^n - RI^{n-1/2} - V_{source}^n)$$

### 多尺度混合仿真

[[hybrid-simulation]]结合FDTD和电路仿真优势：

**分区策略：**
- FDTD域：需要详细场分布的区域
- 电路域：集总参数适用的区域

**接口技术：**
- [[interface-technique]]实现数据交换
- 阻抗匹配避免反射
- 时域同步（不同步长处理）

**应用示例：**
- 变电站FDTD + 输电线路EMTP
- 天线FDTD + 馈电网络电路仿真
- 设备FDTD + 系统级电路仿真

## 与其他数值方法对比

### FDTD vs FEM (有限元法)

[[finite-element-method]]是另一种常用的电磁场数值方法。

| 特性 | FDTD | FEM |
|------|------|-----|
| 求解域 | 时域 | 频域/时域 |
| 网格 | 结构网格(矩形) | 非结构网格(任意) |
| 几何适应性 | 差(阶梯近似) | 优(贴体网格) |
| 计算效率 | 高(稀疏矩阵) | 中(需解方程组) |
| 内存需求 | 低(仅存储场) | 高(存储矩阵) |
| 频域结果 | FFT获得 | 直接获得 |
| 色散材料 | 复杂(ADE) | 简单(直接代入) |
| 开放边界 | PML | 无限元/BEM耦合 |

**选择建议：**
- 复杂几何 → FEM
- 宽频响应 → FDTD
- 大规模开放域 → FDTD
- 精细谐振分析 → FEM

### FDTD vs MoM (矩量法)

`method-of-moments`基于积分方程，适合天线问题。

| 特性 | FDTD | MoM |
|------|------|-----|
| 方程类型 | 微分方程 | 积分方程 |
| 离散对象 | 整个空间 | 仅目标表面 |
| 计算复杂度 | O(N) | O(N²)-O(N³) |
| 辐射边界 | 自动满足 | 自动满足 |
| 金属处理 | 网格近似 | 精确边界条件 |
| 介质处理 | 直接 | 需要体积分 |
| 典型应用 | EMC/散射 | 天线/RCS |

### FDTD vs TLM (传输线矩阵法)

[[transmission-line-modeling]]与FDTD数学等价。

**主要区别：**
- FDTD：直接离散麦克斯韦方程
- TLM：基于Huygens原理的电路类比

**等价关系：**
$$\Delta t_{TLM} = \frac{\Delta}{2c} = \frac{\Delta t_{FDTD}}{2}$$

## 数值实现要点

### 并行计算

[[parallel-computing]]是FDTD处理大规模问题的必需技术。

**并行策略：**
1. **OpenMP并行**：共享内存，按网格分片
2. **MPI并行**：分布式内存，域分解
3. **GPU加速**：CUDA/OpenCL实现

**域分解：**
将计算域分割为子域，子域间通过边界交换数据：
```
[Subdomain 1] <-> [Subdomain 2] <-> [Subdomain 3]
```

**性能优化：**
- 减少通信边界数据
- 重叠计算与通信
- 负载均衡

### 后处理

**时频转换：**
使用FFT获得频域响应：
$$\hat{E}(f) = \int_{-\infty}^{\infty} E(t) e^{-j2\pi ft} dt$$

**S参数提取：**
$$S_{ij} = \frac{V_i^-}{V_j^+}$$

**场可视化：**
- 2D/3D场分布云图
- 时域波形
- 动画生成

## 软件工具

**开源工具：**
- **MEEP**: MIT开发的FDTD软件，支持Python/C++接口
- **OpenEMS**: 基于ECSS的开放源码FDTD求解器
- **gprMax**: 专用于探地雷达的FDTD实现

**商业软件：**
- **CST Studio Suite**: 包含FDTD模块的全波电磁仿真
- **XFdtd**: Remcom公司专业FDTD软件
- **EMPro**: Keysight的电磁仿真平台

## 相关方法

- [[finite-element-method]] - 基于变分原理的频域/时域方法
- `method-of-moments` - 基于积分方程的边界元方法
- [[transmission-line-modeling]] - 与FDTD等价的电路方法
- `electromagnetic-field-analysis` - 电磁场数值分析总览
- [[frequency-dependent-modeling]] - 宽频材料建模方法
- [[high-frequency-transient-analysis]] - FDTD主要应用领域

## 来源论文

参见 [[index.md]] 获取更多FDTD相关文献。
