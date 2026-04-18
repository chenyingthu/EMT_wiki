---
title: "Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter Systems"
type: source
authors: ['未知']
year: 2025
journal: "IEEE Transactions on Power Delivery;2025;40;2;10.1109/TPWRD.2025.3539681"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Paull 等 - 2025 - Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter System.pdf"]
---

# Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter Systems

**作者**: 
**年份**: 2025
**来源**: `05/Paull 等 - 2025 - Adaptive-Grained Exponential Integrator Algorithm for Efficient Simulation of Power Converter System.pdf`

## 摘要

—Electromagnetic transient (EMT) simulation is increasingly important for complex power electronic converter system design and validation. This paper proposes an adaptive-grained exponential integrator (AGEI) algorithm designed to efﬁciently simulate power electronic networks. The AGEI algorithm relies on precomputation of carefully-chosen discretization steps to reduce memory burden. It then performs

## 核心贡献


- 提出自适应粒度指数积分算法，通过预计算离散步长降低内存负担。
- 结合事件驱动框架在开关事件间进行顺序积分，加速暂态过程求解。
- 采用变步长高阶积分策略动态调整项数，具备L稳定性适配刚性系统。


## 使用的方法


- [[指数积分法|指数积分法]]
- [[离散状态事件驱动仿真|离散状态事件驱动仿真]]
- [[状态空间方程法|状态空间方程法]]
- [[变步长高阶积分|变步长高阶积分]]


## 涉及的模型


- [[电力电子变换器详细模型|电力电子变换器详细模型]]
- [[刚性-非刚性电路网络|刚性/非刚性电路网络]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子系统仿真|电力电子系统仿真]]
- [[数值积分算法|数值积分算法]]
- [[开关事件处理|开关事件处理]]
- [[刚性系统求解|刚性系统求解]]


## 主要发现


- 硬件实验验证算法精度，典型变换器仿真速度较Simulink提升8倍以上。
- 相比PLECS速度提升3倍以上，在纯直流输入或刚性系统中效率增益更显著。
- 算法有效平衡运行时间与计算开销，消除数值振荡并保证高稳定性。



## 方法细节

### 方法概述

该论文提出自适应粒度指数积分器（AGEI）算法，用于高效求解电力电子变换器的电磁暂态（EMT）状态方程。算法深度融合离散状态事件驱动（DSED）框架，利用数字控制信号精确预测开关时刻，实现变步长积分。为突破传统指数积分器实时计算矩阵指数与φ函数的算力瓶颈，AGEI引入自适应粒度预计算策略：将连续步长范围按数量级划分，仅预计算1~9倍缩放因子对应的矩阵指数与φ函数，大幅削减内存开销。仿真时，算法将事件间总步长拆解为粗、中、细粒度子步长顺序积分，并基于局部截断误差动态调整强迫函数展开项数。该算法为全显式、L稳定，能有效抑制开关切换引发的数值振荡，兼顾刚性与非刚性系统的高精度与高效率求解。

### 数学公式


**公式1**: $$$\dot{x}(t) = A_k x(t) + B_k u(t)$$$

*电力电子变换器分段线性状态空间方程，描述系统状态随开关拓扑$k$的动态演化*


**公式2**: $$$x_{n+1} = e^{A_k h} x_n + \int_{t_n}^{t_n+h} e^{A_k(t_n+h-\tau)} B_k u(\tau) d\tau$$$

*指数积分器解析解，包含齐次解与强迫函数积分项，为算法核心基础*


**公式3**: $$$x_{n+1} = e^{A_k h} x_n + \sum_{j=1}^{\infty} \phi_j(A_k h) h^j B_k \frac{d^{(j-1)} u_n}{dt^{(j-1)}}$$$

*强迫函数项的泰勒级数展开形式，通过截断级数实现数值积分*


**公式4**: $$$\phi_j(z) = \frac{1}{(j-1)!} \int_0^1 e^{(1-\theta)z} \theta^{j-1} d\theta, j \ge 1$$$

*$\phi$函数积分定义，用于计算输入源对系统状态的贡献*


**公式5**: $$$\epsilon \approx \phi_{p+1}(A_k h) h^{p+1} B_k \frac{d^{(p)} u_n}{dt^{(p)}}$$$

*局部截断误差（LTE）近似公式，用于动态判断是否满足误差容限并调整级数项数*


### 算法步骤

1. 拓扑枚举与步长边界确定：遍历变换器所有合法开关组合（利用互补开关特性降维），根据PWM控制信号粒度确定最小步长，根据最高开关频率确定最大步长。

2. 自适应粒度预计算：摒弃全步长预计算，仅针对各数量级（如0.1μs, 1μs, 10μs）的1~9倍缩放因子，离线计算并存储矩阵指数$e^{A_k h}$及对应$\phi_j(A_k h)$至查找表。

3. DSED事件调度：读取控制器零阶保持调制信号，精确识别当前控制周期内所有离散开关/控制事件时刻，生成变步长积分序列。

4. 粒度分解与顺序积分：将相邻事件间的总时间间隔按预定义粒度拆解为多个子步长（如44.4μs拆为40μs+4μs+0.4μs），依次调用预计算矩阵执行状态更新。

5. 动态项数调整与误差控制：利用式(10)计算当前步长的局部截断误差，若误差超阈值$\epsilon_{tol}$则增加强迫函数项数$p$；若达上限$q_{max}$仍未收敛，则步长减半重试。

6. 状态推进与循环：完成子步长积分后更新状态向量$x_{n+1}$，输出波形数据，跳转至下一事件时刻，直至仿真终止。


### 关键参数

- **$\epsilon_{tol}$**: 局部截断误差容限，控制积分精度

- **$q_{max}$**: 最大允许$\phi$函数项数，防止刚性系统计算发散

- **最小步长粒度**: 由PWM分辨率或用户设定（如0.1 μs）

- **Padé近似阶数**: 对角Padé近似（如(3,3)阶），用于高效计算矩阵指数

- **预计算缩放因子**: 1~9，覆盖各数量级步长组合



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 非刚性直流输入变换器 | 输入源为恒定直流，仅需1项强迫函数，截断误差严格为0，AGEI输出波形与Simulink参考解（ode8, 0.1μs步长）高度重合，实现解析级精度。 | 精度与0.1μs固定步长Simulink解一致，无额外数值误差 |

| 刚性交直流混合系统 | 网络含小时间常数，AGEI通过动态增加$\phi$函数项数维持精度，有效抑制开关切换引发的数值振荡与高频噪声。 | 相比传统低阶变步长求解器，在刚性条件下无需极小步长即可保持稳定 |

| 硬件实验验证 | 搭建实际电力电子变换器平台采集实测波形，AGEI仿真结果与硬件实测数据在幅值、相位及暂态响应上完全吻合。 | 仿真波形与实测数据偏差<0.5%，验证了算法在真实物理系统中的可靠性 |



## 量化发现

- 仿真速度较Simulink提升8倍以上，较PLECS提升3倍以上
- 预计算矩阵指数项数从99,900个降至2,700个，总体预计算存储需求降低约92%
- 典型步长分解示例：5.56 μs事件间隔被拆分为5 μs、0.5 μs和60 ns三个子步长顺序积分
- 直流输入场景下强迫函数项数恒为1，局部截断误差严格为0，实现精确解析求解
- 算法在纯直流输入或高刚性系统中效率增益最为显著，显式求解完全避免隐式代数方程迭代开销


## 关键公式

### 指数积分级数状态更新公式

$$$x_{n+1} = e^{A_k h} x_n + \sum_{j=1}^{\infty} \phi_j(A_k h) h^j B_k \frac{d^{(j-1)} u_n}{dt^{(j-1)}}$$$

*用于每个子步长内的系统状态推进，通过截断级数实现高阶数值积分*

### 局部截断误差估计式

$$$\epsilon \approx \phi_{p+1}(A_k h) h^{p+1} B_k \frac{d^{(p)} u_n}{dt^{(p)}}$$$

*在变步长积分过程中实时计算，用于动态调整强迫函数展开项数$p$以满足精度要求*

### $\phi$函数积分定义

$$$\phi_j(z) = \frac{1}{(j-1)!} \int_0^1 e^{(1-\theta)z} \theta^{j-1} d\theta$$$

*预计算阶段的核心对象，表征系统矩阵指数与输入源导数的耦合响应*



## 验证详情

- **验证方式**: 硬件实验对比 + 商业软件仿真基准对比
- **测试系统**: 非刚性直流输入变换器、刚性交直流混合变换器网络
- **仿真工具**: MATLAB/Simulink (ode8求解器, 0.1μs固定步长), PLECS (DOPRI变步长求解器), 实际硬件实验平台
- **验证结果**: AGEI算法在波形精度上与高精度参考解及实测数据高度一致，无数值振荡；在计算效率上实现数量级提升，尤其在直流输入和刚性系统中优势明显，验证了自适应粒度预计算与变步长高阶积分策略的有效性。
