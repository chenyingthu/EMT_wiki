---
title: "节点导纳矩阵 (Nodal Admittance Matrix)"
type: method
tags: [nodal-admittance, ybus, matrix-solution, power-flow, circuit-analysis]
created: "2026-05-02"
---

# 节点导纳矩阵 (Nodal Admittance Matrix)

## 概述

节点导纳矩阵(Ybus)是电力系统网络分析的核心数学工具，用于描述电网中各节点之间的电气连接关系。基于基尔霍夫电流定律(KCL)，节点导纳矩阵建立了节点电压与节点注入电流之间的关系，广泛应用于潮流计算、短路计算和电磁暂态仿真。

节点导纳矩阵方法由Ward和Hale于1956年首次系统提出，现已成为电力系统分析的标准方法。其优势在于矩阵的稀疏性、构建的直接性以及数值计算的稳定性。

## 基本定义

### 矩阵形式
节点方程的矩阵形式：
$$\mathbf{I} = \mathbf{Y}\mathbf{V}$$

其中：
- $\mathbf{I}$: 节点注入电流向量 ($n \times 1$)
- $\mathbf{Y}$: 节点导纳矩阵 ($n \times n$)
- $\mathbf{V}$: 节点电压向量 ($n \times 1$)
- $n$: 网络节点数

展开形式为：
$$\begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_n \end{bmatrix} = \begin{bmatrix} Y_{11} & Y_{12} & \cdots & Y_{1n} \\ Y_{21} & Y_{22} & \cdots & Y_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ Y_{n1} & Y_{n2} & \cdots & Y_{nn} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_n \end{bmatrix}$$

### 矩阵元素
- **对角元素** $Y_{ii}$: 节点i的自导纳
  $$Y_{ii} = \sum_{j \in i} y_{ij} + y_{i0}$$
  其中$y_{ij}$为支路导纳，$y_{i0}$为对地导纳

- **非对角元素** $Y_{ij}$: 节点i与j之间的互导纳
  $$Y_{ij} = -y_{ij}$$

自导纳的物理意义是：当所有其他节点接地时，流入节点$i$的电流与节点$i$电压之比。互导纳则表示节点$i$与节点$j$之间的耦合程度。

## 矩阵构建

### 支路贡献
每条支路对导纳矩阵的贡献遵循叠加原理：

**两节点支路** (i-j间导纳$y_{ij}$):
- $Y_{ii}$ += $y_{ij}$
- $Y_{jj}$ += $y_{ij}$
- $Y_{ij}$ = $Y_{ji}$ = $-y_{ij}$

矩阵修改操作可以表示为：
$$\mathbf{Y}_{new} = \mathbf{Y}_{old} + y_{ij} \cdot \mathbf{M}_{ij}$$

其中$\mathbf{M}_{ij}$是修改矩阵：
$$\mathbf{M}_{ij} = \begin{bmatrix} \mathbf{e}_i - \mathbf{e}_j \end{bmatrix} \begin{bmatrix} \mathbf{e}_i - \mathbf{e}_j \end{bmatrix}^T$$

**接地支路** (节点i对地导纳$y_{i0}$):
- $Y_{ii}$ += $y_{i0}$

### 传输线路的导纳贡献

#### 单相线路模型
对于连接节点i和j的传输线路，采用π型等效电路：

**串联导纳** $y_{series}$：
$$y_{series} = \frac{1}{R + jX} = \frac{R - jX}{R^2 + X^2}$$

**并联导纳** $y_{shunt}$（对地导纳的一半）：
$$y_{shunt} = \frac{jB}{2} = j\omega C_{shunt}$$

完整的线路贡献矩阵：
$$\mathbf{Y}_{line} = \begin{bmatrix} y_{series} + y_{shunt} & -y_{series} \\ -y_{series} & y_{series} + y_{shunt} \end{bmatrix}$$

#### 长线路模型
对于长度超过250km的线路，需使用分布参数模型或修正后的等效π型电路：

$$Z' = Z_c \sinh(\gamma l), \quad Y'/2 = \frac{\tanh(\gamma l/2)}{Z_c}$$

其中$\gamma = \sqrt{zy}$为传播常数，$Z_c = \sqrt{z/y}$为特性阻抗。

### 变压器的导纳矩阵

#### 理想变压器模型
变比为$a$:1的理想变压器（$a = V_i/V_j$）：

导纳矩阵元素为：
- $Y_{ii}$ += $\frac{y}{a^2}$
- $Y_{jj}$ += $y$
- $Y_{ij}$ = $Y_{ji}$ = $-\frac{y}{a}$

其中$y$为变压器等效导纳（漏抗的倒数）。

#### 非理想变压器模型
考虑励磁支路和损耗：

$$\mathbf{Y}_{transformer} = \begin{bmatrix} \frac{y_T}{a^2} + \frac{y_{exc}}{a^2} & -\frac{y_T}{a} \\ -\frac{y_T}{a} & y_T \end{bmatrix}$$

其中：
- $y_T = \frac{1}{R_T + jX_T}$：串联等效导纳
- $y_{exc} = \frac{1}{R_{exc}} + \frac{1}{jX_{exc}}$：励磁支路导纳

#### 三相变压器连接方式
不同连接组别（Y/Δ/Yn）对应不同的导纳矩阵结构，需考虑零序网络：

**Y-Δ连接**：
$$\mathbf{Y}_{3\phi} = \begin{bmatrix} \mathbf{Y}_{pos} & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{Y}_{pos} & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & \mathbf{0} \end{bmatrix}$$

零序分量在Δ侧形成环流，对外部网络无贡献。

### 并联元件的导纳贡献

**并联电容器**（节点i）：
$$Y_{ii} \mathrel{+}= j\omega C$$

**并联电抗器**：
$$Y_{ii} \mathrel{+}= \frac{-j}{\omega L}$$

**负荷导纳**：
$$Y_{ii} \mathrel{+}= \frac{P - jQ}{|V_i|^2}$$

**FACTS装置**（SVC、STATCOM）：
$$Y_{ii} \mathrel{+}= Y_{FACTS}(V_i, \alpha)$$

其中控制角$\alpha$决定等效导纳值。

## 稀疏矩阵存储与算法

### 稀疏矩阵特性
大型电力系统的节点导纳矩阵具有显著的稀疏性：

- **稀疏度**：对于$n$节点系统，非零元素约$3n$个，稀疏度达$\frac{3}{n}$
- **对称性**：无移相变压器时为对称矩阵，仅需存储上三角或下三角
- **对角优势**：$|Y_{ii}| \geq \sum_{j \neq i}|Y_{ij}|$

### 压缩存储格式

#### CSR (Compressed Sparse Row) 格式
$$\begin{aligned}
\text{values}[k] &: \text{第}k\text{个非零元素的值} \\
\text{col\_index}[k] &: \text{第}k\text{个非零元素的列号} \\
\text{row\_ptr}[i] &: \text{第}i\text{行第一个非零元素在values中的索引}
\end{aligned}$$

存储需求：$3 \times nnz + n + 1$个整数/浮点数，其中$nnz$为非零元素数。

#### CSC (Compressed Sparse Column) 格式
类似CSR，但按列压缩存储，更适合列运算。

#### 坐标格式 (COO)
直接存储三元组$(i, j, value)$，适合矩阵构建阶段，之后可转换为CSR/CSC。

### 稀疏矩阵算法

#### 稀疏矩阵-向量乘法 (SpMV)
$$\mathbf{y} = \mathbf{Y}\mathbf{x}$$

算法复杂度：$O(nnz)$，而非$O(n^2)$。

```
for i = 1 to n:
    y[i] = 0
    for k = row_ptr[i] to row_ptr[i+1]-1:
        j = col_index[k]
        y[i] += values[k] * x[j]
```

#### 稀疏三角求解
前代法求解$\mathbf{L}\mathbf{z} = \mathbf{b}$：

```
for i = 1 to n:
    z[i] = b[i]
    for k = row_ptr_L[i] to row_ptr_L[i+1]-1:
        if col_index_L[k] < i:
            z[i] -= L[k] * z[col_index_L[k]]
    z[i] /= L_diag[i]
```

### 填充元控制

在LU分解过程中，原本为零的元素可能变为非零（填充）：

**填充元**：$\mathbf{Y}_{ij} = 0$但$\mathbf{L}_{ij} \neq 0$或$\mathbf{U}_{ij} \neq 0$

**最小度排序 (Minimum Degree)**：
选择使填充元最少的消去顺序，NP-hard问题，采用启发式算法。

**嵌套剖分 (Nested Dissection)**：
将网络递归分割，减少分离面，控制填充元增长。

## 求解方法详细推导

### LU分解

对于线性方程组$\mathbf{Y}\mathbf{V} = \mathbf{I}$，LU分解将$\mathbf{Y}$分解为：

$$\mathbf{Y} = \mathbf{L}\mathbf{U}$$

其中：
- $\mathbf{L}$：下三角矩阵，对角线为1
- $\mathbf{U}$：上三角矩阵

#### Doolittle分解算法

对于$i = 1, 2, ..., n$:

**计算U的第i行**：
$$U_{ij} = Y_{ij} - \sum_{k=1}^{i-1} L_{ik} U_{kj}, \quad j = i, i+1, ..., n$$

**计算L的第i列**：
$$L_{ji} = \frac{1}{U_{ii}} \left( Y_{ji} - \sum_{k=1}^{i-1} L_{jk} U_{ki} \right), \quad j = i+1, ..., n$$

#### 稀疏LU分解优化

**Tinney-Walker最优排序**：
1. **Tinney-1**：静态最小度，基于原始矩阵结构
2. **Tinney-2**：动态最小度，消去过程中更新
3. **Tinney-3**：最小局部填充，考虑填充元传播

**符号分解 (Symbolic Factorization)**：
预先确定填充元位置，分配存储空间，避免动态内存分配。

### KLU算法

KLU (Clark Kent LU) 是专门为电路仿真优化的稀疏LU求解器：

**特点**：
- 针对电路矩阵结构优化
- 支持部分主元选择
- 高效处理开关引起的矩阵修改
- 适合EMT仿真中的时变网络

**算法流程**：
1. 对矩阵进行块三角分解 (BTF)
2. 对每个对角块应用稀疏LU
3. 使用AMD (Approximate Minimum Degree) 排序
4. 保留因子表以支持快速前代回代

### 迭代求解方法

#### 雅可比迭代法
$$V_i^{(k+1)} = \frac{1}{Y_{ii}} \left( I_i - \sum_{j \neq i} Y_{ij} V_j^{(k)} \right)$$

收敛条件：谱半径$\rho(\mathbf{D}^{-1}(\mathbf{L}+\mathbf{U})) < 1$，其中$\mathbf{D}$为对角矩阵。

#### 高斯-赛德尔迭代法
$$V_i^{(k+1)} = \frac{1}{Y_{ii}} \left( I_i - \sum_{j < i} Y_{ij} V_j^{(k+1)} - \sum_{j > i} Y_{ij} V_j^{(k)} \right)$$

利用最新计算值，收敛速度通常比雅可比快一倍。

#### 不完全LU预处理共轭梯度法 (ILU-PCG)

对于对称正定系统，预处理后的CG算法：

1. 计算预处理矩阵$\mathbf{M} \approx \mathbf{L}\mathbf{L}^T$（不完全Cholesky）
2. 迭代求解：
   $$\mathbf{r}_k = \mathbf{I} - \mathbf{Y}\mathbf{V}_k$$
   $$\mathbf{M}\mathbf{z}_k = \mathbf{r}_k$$
   $$\beta_k = \frac{\mathbf{r}_k^T \mathbf{z}_k}{\mathbf{r}_{k-1}^T \mathbf{z}_{k-1}}$$
   $$\mathbf{p}_k = \mathbf{z}_k + \beta_k \mathbf{p}_{k-1}$$
   $$\alpha_k = \frac{\mathbf{r}_k^T \mathbf{z}_k}{\mathbf{p}_k^T \mathbf{Y}\mathbf{p}_k}$$
   $$\mathbf{V}_{k+1} = \mathbf{V}_k + \alpha_k \mathbf{p}_k$$

收敛速度取决于条件数$\kappa(\mathbf{M}^{-1}\mathbf{Y})$。

## 在EMT仿真中的应用

### 伴随模型方法

EMT仿真将动态元件离散化为诺顿等效电路：

**梯形法离散**（积分步长$\Delta t$）：
$$i(t) = G_{eq} v(t) + I_{hist}$$

其中：
- $G_{eq} = \frac{2C}{\Delta t}$（电容）或$\frac{\Delta t}{2L}$（电感）
- $I_{hist}$：历史电流源，由上一时刻状态确定

**节点导纳矩阵构建**：
$$\mathbf{Y}_{EMT} = \mathbf{Y}_{static} + \mathbf{G}_{eq,dynamic}$$

动态元件贡献等效导纳到对角元素，历史电流作为注入电流。

### 时变网络处理

#### 开关操作建模
电力电子开关导通/关断改变网络拓扑：

**开关导通**（闭合）：
- 添加支路导纳$y_{sw}$
- 修改$Y_{ii}$, $Y_{jj}$, $Y_{ij}$

**开关关断**（断开）：
- 移除支路导纳
- 或设置$y_{sw} \approx 0$

#### 快速重因子化算法
利用矩阵求逆引理避免完全重新分解：

**Woodbury公式**：
$$(\mathbf{Y} + \mathbf{U}\mathbf{C}\mathbf{V}^T)^{-1} = \mathbf{Y}^{-1} - \mathbf{Y}^{-1}\mathbf{U}(\mathbf{C}^{-1} + \mathbf{V}^T\mathbf{Y}^{-1}\mathbf{U})^{-1}\mathbf{V}^T\mathbf{Y}^{-1}$$

对于单条支路修改，只需更新少量元素。

#### 多开关状态处理
**稀疏LU更新**：仅重新分解受影响的块
**补偿法**：使用部分网络等效减少计算量
**预计算**：离线计算所有可能的开关组合

### 大规模EMT系统求解

#### 网络分块技术
$$\mathbf{Y} = \begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} & \cdots \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} & \cdots \\ \vdots & \vdots & \ddots \end{bmatrix}$$

块对角结构允许并行求解。

#### GPU加速求解
- **SpMV加速**：利用GPU的并行计算能力
- **批量LU分解**：对多个小矩阵并行分解
- **迭代求解器**：Jacobi/Gauss-Seidel适合GPU并行

## 矩阵修改与更新方法

### 支路追加算法

新增支路$(i,j,y_{new})$的修改：

```
Y[i,i] += y_new
Y[j,j] += y_new
Y[i,j] = Y[j,i] -= y_new
```

对于稀疏存储，需要：
1. 查找或插入(i,j)位置
2. 更新对角元素
3. 维护row_ptr和col_index

### 支路移除与修改

**支路移除**（导纳变为$y_{new} - y_{old}$）：
```
Y[i,i] -= y_old
Y[j,j] -= y_old
Y[i,j] = Y[j,i] += y_old
```

**导纳修改**：先移除旧值，再添加新值。

### 节点消去与添加

#### Kron消去
消去节点$k$，更新其余节点：
$$Y_{ij}^{new} = Y_{ij} - \frac{Y_{ik} Y_{kj}}{Y_{kk}}$$

**应用场景**：
- 消去零注入节点
- 网络等值简化
- 生成FDNE（频率相关网络等值）

#### 节点恢复
当需要重新添加节点时，需要保留原始连接信息或使用补偿法。

### 补偿法详细推导

**问题**：支路$(p,q)$从$y$修改为$y'$，避免完全重新分解。

**步骤**：
1. 计算等效修改：$\Delta y = y' - y$
2. 求解原系统的两个辅助问题：
   $$\mathbf{Y}\mathbf{V}^{(p)} = \mathbf{e}_p, \quad \mathbf{Y}\mathbf{V}^{(q)} = \mathbf{e}_q$$
3. 计算补偿电流：
   $$\begin{bmatrix} I_p \\ I_q \end{bmatrix} = -\left( \begin{bmatrix} \Delta y & -\Delta y \\ -\Delta y & \Delta y \end{bmatrix}^{-1} + \begin{bmatrix} Z_{pp} & Z_{pq} \\ Z_{qp} & Z_{qq} \end{bmatrix} \right)^{-1} \begin{bmatrix} V_p - V_q \\ V_q - V_p \end{bmatrix}$$
4. 更新节点电压：
   $$\mathbf{V}^{new} = \mathbf{V}^{old} + I_p \mathbf{V}^{(p)} + I_q \mathbf{V}^{(q)}$$

## 三相系统的块矩阵形式

### 三相节点导纳矩阵

对于$n$节点三相系统，导纳矩阵为$3n \times 3n$：

$$\mathbf{Y}_{3\phi} = \begin{bmatrix} \mathbf{Y}_{11} & \mathbf{Y}_{12} & \cdots & \mathbf{Y}_{1n} \\ \mathbf{Y}_{21} & \mathbf{Y}_{22} & \cdots & \mathbf{Y}_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \mathbf{Y}_{n1} & \mathbf{Y}_{n2} & \cdots & \mathbf{Y}_{nn} \end{bmatrix}$$

其中每个$\mathbf{Y}_{ij}$为$3 \times 3$子矩阵：
$$\mathbf{Y}_{ij} = \begin{bmatrix} Y_{ij}^{aa} & Y_{ij}^{ab} & Y_{ij}^{ac} \\ Y_{ij}^{ba} & Y_{ij}^{bb} & Y_{ij}^{bc} \\ Y_{ij}^{ca} & Y_{ij}^{cb} & Y_{ij}^{cc} \end{bmatrix}$$

### 对称分量变换

通过变换矩阵$\mathbf{T}$转换为序分量：
$$\mathbf{T} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & a^2 & a \\ 1 & a & a^2 \end{bmatrix}, \quad a = e^{j2\pi/3}$$

序分量导纳矩阵：
$$\mathbf{Y}_{012} = \mathbf{T}^{-1} \mathbf{Y}_{abc} \mathbf{T}$$

对于对称网络，序分量矩阵解耦：
$$\mathbf{Y}_{012} = \begin{bmatrix} \mathbf{Y}_0 & 0 & 0 \\ 0 & \mathbf{Y}_1 & 0 \\ 0 & 0 & \mathbf{Y}_2 \end{bmatrix}$$

可以独立求解正序、负序、零序网络。

### 不平衡系统处理

**直接三相法**：直接求解$3n \times 3n$系统
**序分量法**：先分解再求解（仅限线性对称元件）
**混合法**：对称部分用序分量，不对称部分用相分量

### 相序混合求解
对于含不对称负荷的系统：
1. 构建三相导纳矩阵
2. 使用块稀疏求解器
3. 或采用补偿法处理不对称部分

## 数值问题和病态处理

### 矩阵条件数

条件数衡量矩阵求逆的数值稳定性：
$$\kappa(\mathbf{Y}) = \|\mathbf{Y}\| \cdot \|\mathbf{Y}^{-1}\|$$

- $\kappa \approx 1$：良态
- $\kappa \gg 1$：病态
- 条件数大 → 舍入误差放大严重

### 病态来源

#### 大R/X比问题
长距离输电线路$R/X < 0.001$：
- 导纳矩阵接近奇异
- 潮流计算收敛困难
- EMT仿真步长受限

**解决方法**：
- 阻抗矩阵法（短路计算）
- 改进潮流算法
- 使用扩展精度计算

#### 孤立节点
节点仅通过小导纳连接：
- 对角优势弱
- 高斯消去产生大填充元

#### 零注入节点集中
多个零注入节点相邻：
- 消去后产生稠密块
- 求解复杂度增加

### 数值稳定性改进

#### 主元选择
**部分主元**：每列选择最大元素
$$|Y_{ii}^{(k)}| = \max_{j \geq k} |Y_{ji}^{(k)}|$$

**完全主元**：全局最大元素，计算代价高

#### 标度技术
行/列标度改善矩阵条件：
$$\mathbf{D}_r \mathbf{Y} \mathbf{D}_c \tilde{\mathbf{V}} = \mathbf{D}_r \mathbf{I}$$

其中$\mathbf{D}_r$, $\mathbf{D}_c$为对角标度矩阵。

#### 迭代精化
$$\mathbf{r} = \mathbf{I} - \mathbf{Y}\mathbf{V}$$
$$\mathbf{Y}\Delta\mathbf{V} = \mathbf{r}$$
$$\mathbf{V}_{new} = \mathbf{V} + \Delta\mathbf{V}$$

### 零注入节点处理

#### 高斯消去
消去节点$k$后，$i,j$元素更新：
$$Y_{ij} = Y_{ij} - \frac{Y_{ik} Y_{kj}}{Y_{kk}}$$

#### 保留策略
- 稀疏性考虑：消去增加填充元
- 网络可视化：保留原始拓扑
- 并行性：消去减少并行度

## 与阻抗矩阵的详细对比

### 定义与关系

**导纳矩阵** $Y$：$\mathbf{I} = \mathbf{Y}\mathbf{V}$
**阻抗矩阵** $Z$：$\mathbf{V} = \mathbf{Z}\mathbf{I}$

关系：
$$\mathbf{Z} = \mathbf{Y}^{-1}$$

### 构建复杂度

| 操作 | 导纳矩阵 | 阻抗矩阵 |
|------|----------|----------|
| 构建 | $O(nnz)$，直接求和 | $O(n^3)$，需矩阵求逆 |
| 存储 | $O(n)$，稀疏 | $O(n^2)$，稠密 |
| 修改 | $O(1)$，直接修改 | $O(n^2)$，需重新计算 |
| 求解 | $O(n^{1.2})$~$O(n^{1.5})$ | $O(n^2)$，矩阵-向量乘法 |

### 应用场景对比

**导纳矩阵优势**：
- 潮流计算（迭代求解）
- EMT仿真（时变网络）
- 大规模系统（稀疏性）
- 网络修改（快速更新）

**阻抗矩阵优势**：
- 短路计算（端口电流-电压关系）
- 灵敏度分析（$\partial V / \partial I$）
- 小干扰稳定（特征值分析）
- 等值网络（端口等效）

### 混合方法

**部分求逆**：只计算需要的阻抗元素
$$Z_{ij} = \mathbf{e}_i^T \mathbf{Y}^{-1} \mathbf{e}_j$$
使用稀疏求解计算特定列。

## 实际应用案例

### 案例1：IEEE 39节点系统潮流计算

**系统规模**：39节点，46条支路

**导纳矩阵特性**：
- 非零元素：117个
- 稀疏度：92.3%
- 条件数：$\approx 10^4$

**求解过程**：
1. 构建Ybus，采用极坐标形式
2. 牛顿-拉夫逊法迭代
3. 每次迭代求解修正方程：
   $$\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \begin{bmatrix} \mathbf{H} & \mathbf{N} \\ \mathbf{J} & \mathbf{L} \end{bmatrix} \begin{bmatrix} \Delta\theta \\ \Delta V/V \end{bmatrix}$$
4. 稀疏LU分解，Tinney-2排序
5. 3-4次迭代收敛

### 案例2：MMC-HVDC系统EMT仿真

**系统描述**：401电平MMC换流器，连接交流电网

**建模挑战**：
- 每个子模块含2个IGBT开关
- 开关状态组合：$2^{N_{SM}}$种可能
- 实时性要求：步长$\Delta t = 10\mu s$

**导纳矩阵策略**：
1. **恒导纳建模**：开关用可变电阻表示，$R_{on} = 0.01\Omega$, $R_{off} = 1M\Omega$
2. **伴随模型**：电容离散化为$G_{eq} + I_{hist}$
3. **稀疏结构优化**：预处理阶段分析所有可能拓扑
4. **KLU求解器**：针对电路结构优化，填充元最少

**性能指标**：
- 矩阵规模：1200×1200
- 非零元素：~4800
- 单次求解时间：<5μs（CPU）
- 实时因子：0.3（比实时快3倍）

### 案例3：大规模风电场等值

**问题**：200台风机风电场，需简化用于系统级仿真

**FDNE方法**：
1. 保留边界节点（并网点）
2. 消去内部节点（风机、集电线路）
3. 构建频率相关等值导纳：
   $$\mathbf{Y}_{eq}(s) = \mathbf{Y}_{bb} - \mathbf{Y}_{bi}(\mathbf{Y}_{ii} + s\mathbf{C})^{-1}\mathbf{Y}_{ib}$$

**矢量拟合**：
$$\mathbf{Y}_{eq}(s) \approx \sum_{m=1}^{N} \frac{\mathbf{R}_m}{s - p_m} + \mathbf{D} + s\mathbf{E}$$

转换为RLC等效电路用于EMT仿真。

### 案例4：电磁暂态-机电暂态混合仿真

**接口问题**：EMT侧（详细模型）与TS侧（相量模型）耦合

**导纳矩阵处理**：
1. **诺顿等效**：TS侧向EMT侧提供等效导纳和电流源
2. **戴维南等效**：EMT侧向TS侧提供等效电压源
3. **接口稳定性**：$Y_{eq} = Y_{TS} + Y_{interface}$

**数值稳定性**：
- 接口导纳选择影响稳定性
- 采用阻尼电阻抑制数值振荡
- 多速率方法处理不同时间尺度

## 相关方法
- `power-flow-analysis` - 潮流分析
- `short-circuit-calculation` - 短路计算
- [[sparse-matrix-techniques]] - 稀疏矩阵技术
- `circuit-analysis` - 电路分析
- `lu-factorization` - LU分解
- `iterative-method` - 迭代法
- [[compensation-method]] - 补偿法
- [[transformer-model]] - 变压器模型
- `three-phase-power-flow` - 三相潮流
- [[network-partitioning]] - 网络分区
- [[gpu-parallel-acceleration]] - GPU并行
- [[companion-model]] - 伴随模型
- [[harmonic-analysis]] - 谐波分析
- [[frequency-dependent-modeling]] - 频率相关建模
- [[state-space-method]] - 状态空间法
- [[symmetrical-components]] - 对称分量
- `ill-conditioned-matrix` - 病态矩阵
- `node-elimination` - 节点消去
- [[fdne-model]] - FDNE模型
- [[mmc-model]] - MMC模型

## 参考文献与延伸阅读

1. Tinney, W.F. and Walker, J.W., "Direct solutions of sparse network equations by optimally ordered triangular factorization", Proceedings of the IEEE, 1967.

2. Kundur, P., "Power System Stability and Control", McGraw-Hill, 1994.

3. Dommel, H.W., "Digital Computer Solution of Electromagnetic Transients in Single-and Multiphase Networks", IEEE Trans. PAS, 1969.

4. Davis, T.A. and Natarajan, E.P., "Algorithm 907: KLU, A Direct Sparse Solver for Circuit Simulation Problems", ACM TOMS, 2010.

5. Glover, J.D. et al., "Power System Analysis and Design", Cengage Learning, 2016.

6. Milano, F., "Power System Modelling and Scripting", Springer, 2010.

## 来源论文

参见 [[index]] 获取更多节点导纳矩阵相关文献。
