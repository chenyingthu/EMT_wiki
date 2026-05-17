---
title: "Bergeron 线路模型 (Bergeron Line Model)"
type: method
tags: [transmission-line, bergeron, traveling-wave, lossless-line, companion-circuit, emt, characteristic-method]
created: "2026-05-02"
updated: "2026-05-17"
---

# Bergeron 线路模型 (Bergeron Line Model)

## 定义与边界

Bergeron 模型是一种基于**特征线法（Method of Characteristics）**的输电线路端口等效模型。它将一段均匀传输线的分布参数传播关系表示为端口导纳、传播延时和历史电流源的组合，供 EMT 网络方程在每个时间步调用。完整常参数行波线路理论见 [[distributed-parameter-line]] 和 [[bergeron-line-model]]；本页聚焦于**端口接口形式、历史源表达式和频变扩展**，作为方法体系的入口。

**与宽频模型的边界**：当研究需要导体集肤效应、大地返回阻抗、频变土壤、非换位强耦合或电缆护套耦合时，应转向 [[frequency-dependent-line-model]]（FD-line）、[[universal-line-model]]（ULM）和 [[earth-return-impedance]]。

## EMT 中的作用

在 EMTP 程序中，Bergeron 模型的核心作用是将分布参数传播关系转化为**Norton 端口**并入节点导纳方程。它解决了"线路两端不能瞬时相互作用"的问题——通过历史电流源将远端信息延迟 $\tau$ 个时间步传递到本端，实现分布式参数线路与集总参数网络的联解。

**典型输入**：线路长度 $\ell$、单位长度电感 $L$、单位长度电容 $C$、时间步长 $\Delta t$、延时 $\tau$、历史队列。

**典型输出**：当前步节点导纳贡献 $Y_c = 1/Z_c$ 与历史电流源 $I_h(t)$。

**多相扩展**：通过 [[modal-transformation]] 将相域耦合转为模态通道，对每模态独立应用 Bergeron 端口形式。若变换矩阵随频率变化明显，需使用 [[frequency-dependent-line-model]] 而非常参数 Bergeron。

## EMT 建模方法

### 方法 1：经典无损 Bergeron（Dommel 1969）

对单相无损均匀线，电报方程为：

$$-\frac{\partial v}{\partial x}=L\frac{\partial i}{\partial t},\quad -\frac{\partial i}{\partial x}=C\frac{\partial v}{\partial t}$$

令传播速度 $u=1/\sqrt{LC}$，特性阻抗 $Z_c=\sqrt{L/C}$，线路延时 $\tau=\ell/u$。沿特征线 $dx/dt = \pm u$ 积分，得行波解：

$$i(x,t)=f_1(x-ut)+f_2(x+ut),\quad v(x,t)=Z_c f_1(x-ut)-Z_c f_2(x+ut)$$

对端口 $k$（发送端）和端口 $m$（接收端），设电流均以流入线路为正。利用 $x=\ell$ 处 $(v_k+i_k Z_c)$ 和 $x=0$ 处 $(v_m-i_m Z_c)$ 为常数，有：

$$v_k(t)+Z_c i_k(t)=v_m(t-\tau)+Z_c i_m(t-\tau) \quad \text{(行波关系)}$$

整理得端口 $k$ 的 Norton 形式：

$$i_k(t)=Y_c v_k(t)+I_{h,k}(t),\quad Y_c=\frac{1}{Z_c}$$

$$I_{h,k}(t)=-Y_c v_m(t-\tau)-i_m(t-\tau) \tag{1}$$

端口 $m$ 对称成立：

$$i_m(t)=Y_c v_m(t)+I_{h,m}(t),\quad I_{h,m}(t)=-Y_c v_k(t-\tau)-i_k(t-\tau) \tag{2}$$

式 (1)(2) 中的历史源 $I_{h,k}(t)$、$I_{h,m}(T)$ 不是新的物理电源，而是远端延时电压电流沿特征线传播到本端后的等效表达。**实现时必须先统一端口电流正方向**，否则同一公式会出现符号差异。

### 方法 2：集中损耗扩展（Snelson 1972）

经典 Bergeron 忽略电阻 $R$ 和电导 $G$。Snelson 将线路损耗集中到两端，用两个等效电阻 $R_s$（发送端）和 $R_r$（接收端）近似分布损耗。等效电路为在无损 Bergeron 端口两端各串联一个电阻：

$$i_k(t)=\frac{1}{Z_c+R_s}v_k(t)+\frac{R_s}{Z_c+R_s}I_{h,k}(t)$$

$$i_m(t)=\frac{1}{Z_c+R_r}v_m(t)+\frac{R_r}{Z_c+R_r}I_{h,m}(t)$$

该扩展对低损耗线路（架空线）近似效果好，但对高频衰减显著或电缆线路误差较大。

### 方法 3：级联 Bergeron

将长线路分为 $N$ 个短段串联，每段保留独立历史源：

$$i_{k}^{(j)}(t)=Y_c v_{k}^{(j)}(t)+I_{h,k}^{(j)}(t),\quad j=1,2,\dots,N$$

段数增加可更精确地嵌入局部损耗或状态模块，但计算量相应增加。需验证段数、步长和拟合参数的协调性。

### 方法 4：频变 Bergeron 扩展（Torres Caballero 2014）

Torres Caballero 等提出将频变纵向阻抗 $Z(\omega)=R(\omega)+j\omega L(\omega)$ 用 [[vector-fitting]] 拟合成有理函数：

$$Z_{\text{fit}}(\omega)=\sum_{i=1}^{n}\frac{r_i}{j\omega-p_i}$$

每个 RL 电路对应一个伴随电路，通过级联多个短 Bergeron 段表示频变效应。该方法保留了 Bergeron 端口结构的简洁性，同时将频变损耗纳入时域仿真。

### 方法 5：插值历史源（变步长接口）

当延时 $\tau$ 不是时间步长 $\Delta t$ 的整数倍时，需对历史量插值。设 $\tau=q\Delta t+\delta\Delta t$，$0\le\delta<1$，线性插值：

$$x(t-\tau)\approx(1-\delta)x(t-q\Delta t)+\delta x(t-(q+1)\Delta t)$$

插值阶次影响高频相位与幅值精度。可变步长或多速率仿真还需明确历史队列重采样策略（见 [[transmission-line-model-for-variable-step-size-simulation-algorithms]]）。

## 形式化表达

**端口 Norton 等效**（任意端口 $k$）：

$$i_k(t)=Y_c v_k(t)+I_{h,k}(t),\quad Y_c=\frac{1}{Z_c}=\sqrt{\frac{C}{L}}$$

**历史电流源**（发送端 $k$）：

$$I_{h,k}(t)=-Y_c v_m(t-\tau)-i_m(t-\tau)$$

**历史电流源**（接收端 $m$）：

$$I_{h,m}(t)=-Y_c v_k(t-\tau)-i_k(t-\tau)$$

**延时关系**：

$$\tau=\ell\sqrt{LC}=\frac{\ell}{u},\quad u=\frac{1}{\sqrt{LC}}$$

**集中损耗扩展**：

$$i_k(t)=\frac{1}{Z_c+R_s}v_k(t)+\frac{R_s}{Z_c+R_s}I_{h,k}(t)$$

**频变扩展（向量拟合参数）**：

$$Z_{\text{fit}}(s)=\sum_{i=1}^{n}\frac{r_i}{s-p_i}\quad\Longrightarrow\quad \text{RL 伴随电路}$$

**插值近似**：

$$x(t-\tau)=(1-\delta)x(t-q\Delta t)+\delta x(t-(q+1)\Delta t)$$

## 关键技术挑战

**挑战 1：频变损耗的时域嵌入**
频变纵向阻抗 $R(\omega)$、$L(\omega)$ 无法直接在时域使用。Torres Caballero 2014 指出，通过 vector fitting 将 $Z(\omega)$ 拟合为有理函数后，每个 RL 电路可转化为时域伴随电路，但拟合阶数与计算效率之间存在权衡。拟合阶数过低会损失高频精度，过高则增加伴随电路数量。

**挑战 2：多相线路的解耦与模态变换**
对多导体线路，相域耦合矩阵 $\mathbf{Z}$、$\mathbf{Y}$ 通常不是对角矩阵。Dommel 的相模变换方法要求变换矩阵使 $\mathbf{R}$ 解耦为对角阵或近似对角阵。对非换位线路，该条件难以满足，需要使用 [[modal-domain-decoupling]] 或直接采用 [[frequency-dependent-line-model]]。

**挑战 3：插值误差与数值色散**
当 $\tau/\Delta t$ 不是整数时，线性插值引入数值色散。插值误差在高频分量（接近 Nyquist 频率）中尤为显著，可能导致波前畸变。更高阶插值（如 Lagrange）可缓解但增加计算量。

**挑战 4：无源性保证**
频变参数的有理函数拟合可能产生非无源等效电路（部分极点位于右半平面），导致数值不稳定。需结合 [[passivity-enforcement]] 检查拟合结果的无源性。

**挑战 5：短线路的数值接口退化**
当 $\tau < \Delta t$（短线路或大步长仿真）时，历史源表达式中 $t-\tau$ 可能与当前时刻接近，延时关系退化为强耦合代数约束，导致数值条件数增大甚至求解发散。

## 量化性能边界

| 变体 | 步长约束 | 计算效率 | 精度范围 | 代表数据 |
|------|----------|----------|----------|----------|
| 常参数 Bergeron | $\Delta t \le \tau$ | 极低（无迭代） | 低频（<1 kHz） | Dommel 1969, EMTP经典 |
| 集中损耗扩展 | $\Delta t \le \tau$ | 极低 | 中频（<10 kHz） | Snelson 1972 |
| 级联 Bergeron（10段） | $\Delta t \le \tau/N$ | 低（增加$N$倍） | 宽频（<100 kHz） | Torres Caballero 2014 |
| 频变 Bergeron（vector fitting） | $\Delta t \le \tau$ | 中等（有拟合开销） | 宽频（<1 MHz） | Torres Caballero 2014: 100km架空线，阶数8，反射误差<2% |
| 插值历史源 | 任意（插值开销） | 中等 | 高频精度下降 | $\delta=0.3$时相位误差$<1\%$（$\Delta f/f_s<0.1$） |

**代表性验证数据**（Torres Caballero 2014）：
- 100 km 架空线，8阶 vector fitting，阶跃响应反射误差 **< 2%**（对比数值 Laplace 变换基准）
- 对比 cascade $\pi$-circuit：频变 Bergeron 计算效率提升约 **3-5 倍**（段数相同时）
- 对比 FD-line：频变 Bergeron 宽频精度相当，但节点数减少约 **40%**

## 适用边界与选择指南

| 场景 | 推荐变体 | 不适用 |
|------|----------|--------|
| 低频暂态（工频谐波、开关操作） | 常参数 Bergeron | — |
| 含分布损耗的长架空线 | 集中损耗扩展 | 高频行波（>10kHz） |
| 频变参数宽频仿真 | 频变 Bergeron（VF拟合） | 实时仿真（拟合开销大） |
| 可变步长或多速率仿真 | 插值历史源 | 短线路（$\tau<\Delta t$） |
| 多导体非换位线路 | 级联 Bergeron + 模态变换 | 常参数 Bergeron（解耦失效） |
| 实时仿真硬件实现 | 常参数 Bergeron（结构简单） | 频变扩展（需在线拟合） |

## 相关模型 / 相关方法

- [[distributed-parameter-line]] — 分布参数线路总框架（电报方程推导）
- [[bergeron-line-model]] — 常参数 Bergeron 模型完整说明页（保护页）
- [[characteristic-method]] — 特征线法本身
- [[universal-line-model]] — 相域频变线路，与常参数 Bergeron 边界不同
- [[frequency-dependent-line-model]] — 频变线路的另一类建模方法（FD-line）
- [[folded-line-equivalent]] — 折叠线路导纳组织方式，可与 Bergeron 比较
- [[modal-transformation]] — 多相解耦的变换方法
- [[modal-domain-decoupling]] — 频变模态变换处理
- [[passivity-enforcement]] — 频变参数拟合的无源性保证
- [[vector-fitting]] — 频变参数有理函数拟合的核心方法
- [[earth-return-impedance]] — 大地返回阻抗（影响纵向参数频变特性）
- [[transmission-line-model-for-variable-step-size-simulation-algorithms]] — 可变步长仿真接口

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model]] | 2014 | 频变参数向量拟合嵌入 Bergeron 端口；8阶拟合 vs cascade $\pi$-circuit 3-5×加速 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method]] | 2014 | 多导体频变 Bergeron 扩展；模态域频变参数处理 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-]] | 2020 | 加速特征线/历史源模型；状态方程组织和历史源访问优化 |
| [[耦合长线电磁暂态分析的扩展bergeron模型]] | 1996 | 扩展 Bergeron 用于任意结构多相耦合线路；不对称参数处理 |
| Dommel (1969) | 1969 | 经典无损 Bergeron + 梯形积分；EMTP 创始模型 |
| Snelson (1972) | 1972 | 集中损耗扩展；两端等效电阻近似分布损耗 |