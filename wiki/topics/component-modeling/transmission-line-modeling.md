---
title: "输电线路与电缆建模 (Transmission Line and Cable Modeling)"
type: topic
tags: [transmission-line, cable, bergeron, frequency-dependent, traveling-wave, wideband-modeling]
created: "2026-05-01"
book-chapter: "4"
---

# 输电线路与电缆建模 (Transmission Line and Cable Modeling)

## 概述

输电线路与电缆是电力系统中分布范围最广、总长度最大的元件，其准确的电磁暂态建模对于系统仿真精度至关重要。与变压器、发电机等集中参数元件不同，线路具有显著的分布参数特性——电磁波的传播时延、反射与折射现象在线路暂态过程中扮演核心角色。

在EMT语境下，线路建模面临独特挑战：需要同时处理架空线与电缆的不同特性、频率相关参数（集肤效应、大地回路）、多相耦合、以及从工频到MHz级雷电暂态的宽频建模需求。从Bergeron行波模型到现代频变相域模型，线路建模技术经历了近60年的发展演进。

## 作用机制

### 4.1 基础电报方程与分布参数特性

**电报方程**

输电线路的电磁行为由时域电报方程描述：

$$
\begin{aligned}
-\frac{\partial v(x,t)}{\partial x} &= R i(x,t) + L \frac{\partial i(x,t)}{\partial t} \\
-\frac{\partial i(x,t)}{\partial x} &= G v(x,t) + C \frac{\partial v(x,t)}{\partial t}
\end{aligned}
$$

频域形式为：

$$
\begin{aligned}
-\frac{dV(x,s)}{dx} &= Z(s)I(x,s) \\
-\frac{dI(x,s)}{dx} &= Y(s)V(x,s)
\end{aligned}
$$

其中阻抗和导纳矩阵具有频率相关性：$Z(s) = R(s) + sL(s)$，$Y(s) = G + sC$

**分布参数特性**

| 参数 | 物理意义 | 频率特性 |
|------|---------|---------|
| $R$ | 单位长度电阻 | 集肤效应导致随频率增加 |
| $L$ | 单位长度电感 | 内电感随频率减小 |
| $C$ | 单位长度电容 | 基本恒定 |
| $G$ | 单位长度电导 | 介质损耗，随频率增加 |

### 4.2 Bergeron行波模型

**基本假设**
- 无损或低损线路
- 恒定参数（忽略频率相关性）
- 单一传播速度

**时域等效电路**

基于特征线法，节点$k$和$m$间的等效关系为：

$$
i_k(t) = \frac{1}{Z_c}v_k(t) + I_k(t-\tau), \quad i_m(t) = \frac{1}{Z_c}v_m(t) + I_m(t-\tau)
$$

其中特征阻抗 $Z_c = \sqrt{L/C}$，传播时延 $\tau = \ell\sqrt{LC} = \ell/c$

**历史电流源项**：

$$
I_k(t-\tau) = -\frac{1}{Z_c}v_m(t-\tau) - i_m(t-\tau)
$$

**Bergeron模型的诺顿等效**：

$$
i_k(t) = \frac{v_k(t)}{Z_c} - I_{hist,k}(t)
$$

**适用范围**：
- 工频潮流与机电暂态
- 短距离线路（<100km）
- 对精度要求不高的快速仿真

### 4.3 频变线路模型（J. Marti模型与ULM）

**频域特征参数**

考虑集肤效应和大地回路导致的频变参数：

$$
Z_c(s) = \sqrt{\frac{R(s) + sL(s)}{G(s) + sC(s)}}, \quad \gamma(s) = \sqrt{(R(s)+sL(s))(G(s)+sC(s))}
$$

**传播函数与特征导纳**：

$$
H(s) = e^{-\ell\gamma(s)}, \quad Y_c(s) = \frac{1}{Z_c(s)}
$$

**矢量拟合有理逼近**（Vector Fitting）：

$$
Y_c(s) \approx \sum_{k=1}^{N}\frac{r_k}{s-p_k} + d + se
$$

$$
H(s) \approx \sum_{k=1}^{N_g}\sum_{j=1}^{N_h(k)}\frac{r_{h,kj}}{s-p_{h,kj}}e^{-s\tau_k}
$$

**时域递归卷积**（Recursive Convolution）：

历史电流源通过指数函数递推更新，避免全卷积计算：

$$
I_{hist}(t) = \sum_{k} h_k(t) * i(t) \approx \sum_{k} \alpha_k i(t-\Delta t) + \beta_k I_{hist,k}(t-\Delta t)
$$

**通用线路模型（ULM）——相域实现**

直接在相域建立模型，避免模态变换误差：

$$
I_{ph}(s) = Y_c(s)V_{ph}(s) - H(s)[Y_c(s)V_{ph}(s) + I_{ph}(s)]
$$

状态空间实现：

$$
\dot{x}(t) = Ax(t) + Bu(t), \quad y(t) = Cx(t) + Du(t)
$$

### 4.4 模态变换与多相耦合

**相模变换**

多相线路通过变换矩阵$T$解耦为独立模态：

$$
V_{mode} = T^{-1}V_{phase}, \quad I_{mode} = T^{T}I_{phase}
$$

**常用变换矩阵**：

| 矩阵类型 | 特点 | 适用条件 |
|---------|------|---------|
| 特征向量矩阵 | 精确解耦 | 频变，需逐点计算 |
| Clarke矩阵 | 实常数矩阵 | 对称/换位线路 |
| 修正Clarke | 近似解耦 | 非对称线路，误差<2% |

**模态参数的频率依赖性**：

$$
T(s) = T_0 + \Delta T(s)
$$

恒定矩阵近似会引入误差，长线路需考虑频变变换矩阵。

### 4.5 电缆模型特殊考虑

**电缆结构参数**

| 层次 | 材料 | 电磁特性 |
|------|------|---------|
| 导体 | 铜/铝 | 频变电阻（集肤效应） |
| 绝缘层 | XLPE/油纸 | 频变介电损耗 |
| 金属护套 | 铅/铝 | 接地方式影响 |
| 铠装层 | 钢丝 | 机械保护与电气连接 |

**地下/海底电缆特殊问题**：

- 大地回路阻抗（Carson/Nakagawa公式）
- 交叉互联段建模
- 电缆-架空线混合线路

**Nakagawa模型**（频变大地回路）：

$$
Z_{earth}(s) = \frac{\mu_0}{2\pi}\ln\frac{s + \sqrt{s^2 + \omega_0^2}}{s + \sqrt{s^2 + \omega_0^2\varepsilon_r}}, \quad \omega_0 = \sqrt{\frac{1}{\mu_0\varepsilon_0\rho}}
$$

### 4.6 宽频建模与特殊暂态

**宽频建模要求**

| 暂态类型 | 频率范围 | 建模重点 |
|---------|---------|---------|
| 雷电过电压 | 100 kHz - 10 MHz | 波阻抗、杆塔接地 |
| 开关操作 | 1 kHz - 100 kHz | 行波传播、反射 |
| 谐波传播 | 50 Hz - 2 kHz | 集肤效应、介质损耗 |
| VFTO | 1 MHz - 100 MHz | GIS波过程、陡波头 |

**电晕效应建模**

考虑电晕导致的非线性并联电容：

$$
C(v) = C_0 + \Delta C(v)
$$

空间离散化满足：$\Delta x \leq c/(10f_{max})$（通常≤50m对应1MHz）

**残余电荷分析**

线路断开后的电荷释放过程需要宽带频变模型：

$$
v_{trapped}(t) = v_{pre}(t) - v_{discharge}(t)
$$

### 4.7 折叠线等效模型

**大步长仿真贡献**

传统模型要求 $\Delta t < \tau$，折叠线模型允许 $\Delta t > \tau$：

$$
Y_{eq}(s) = Y_{oc}(s) + Y_{sc}(s)
$$

其中短路分量吸收传播时延效应，实现大步长仿真时的数值稳定性。

**FLE+MCNR组合加速**（Camara 2018）：

FLE将$2n\times 2n$节点导纳矩阵$Y_n$解耦为两个$n\times n$的开路导纳$Y_{oc}$与短路导纳$Y_{sc}$，降低拟合维度并压缩特征值跨度；MCNR快慢极点分离更新实现10%~35%仿真加速（慢极点判定阈值$\alpha \geq 0.99$，强耦合线路收紧至$\alpha \geq 0.9999$）：

$$
h_s(t) = h_s(t-\Delta t) + c v(t-\Delta t)
$$

松弛更新公式在时间步长比$k$高达500时仍保持数值稳定。

**适用场景**：机电暂态、混合仿真

### 4.8 并行线路互感耦合建模

**问题本质**：传统FD线路模型的恒定模态变换矩阵在多回平行线路中对跨线路互耦的表征失效，导致邻线扰动计算误差>18%（Gustavsen 2012）。

**解耦策略**：将平行线路系统拆分独立FD模型，线路间互感与互容耦合通过相域宽频有理函数状态空间模型独立表征：

$$
\tilde{\mathbf{Y}}_{12}(s) \approx \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}
$$

**模态揭示变换**：消除零序/共模分量对运行模态的掩盖，使运行模态分量幅值提升约6-12倍，低频段（0.1-10 Hz）互阻抗拟合误差从>12%降至<0.4%。

**容性/感性耦合分离**：低频段感性耦合被容性主导掩盖，设置对端开路计算容性耦合贡献、对端接地计算感性耦合贡献：

$$
\mathbf{Y}_{12} = \mathbf{Y}_{12}^{(V)} + \mathbf{Y}_{12}^{(I)}
$$

## EMT建模方法体系

输电线路与电缆的EMT建模按三个维度组织：**参数特性**（恒定参数 vs 频变参数）、**坐标域**（模态域 vs 相域）、**时间延迟处理**（直接卷积 vs 递归卷积 vs 延迟利用）。各建模方法的核心公式与适用场景如下：

| 建模方法 | 参数特性 | 坐标域 | 时间延迟 | 核心公式 | 典型误差 |
|---------|---------|--------|---------|---------|---------|
| Bergeron模型 | 恒定 | 模态域 | 直接$\tau$ | $i_k = v_k/Z_c - I_{hist,k}$ | 15%（长线路高频） |
| J.Marti模型 | 频变 | 模态域 | 递归卷积 | $Y_c$, $H$矢量拟合 | <2%（换位线路） |
| ULM相域模型 | 频变 | 相域 | 递归卷积 | $I_{ph} = Y_c V_{ph} - H[\cdots]$ | <0.5%（任意线路） |
| FLE+MCNR | 频变 | 相域 | 延迟利用 | $Y_n = K diag(Y_{oc},Y_{sc})K^{-1}$ | <0.5%（10-35%加速） |
| FDPD-FPGA | 频变 | 相域 | 递归卷积 | $i_k = G*v_k - i_{histk}$ | 2.4µs步长（实时） |
| 平行线路互耦 | 频变 | 相域 | 递归卷积 | $\tilde{Y}_{12} = T_1^{-1}Y_{12}T_2$ | <1.5%（互耦精度） |

## 形式化表达

### 诺顿等效方程（通用形式）

频域端口关系式（ULM频域等效电路基础）：

$$
I_k(s) - Y_c(s) V_k(s) = -H(s)[I_m(s) + Y_c(s) V_m(s)]
$$

时域诺顿等效：

$$
i_k(t) = G \cdot v_k(t) - i_{hist,k}(t)
$$

### 递归卷积状态更新

一阶递归状态变量（用于将频域卷积转化为时域差分）：

$$
x_{Yc}(t) = \alpha_{Yc} x_{Yc}(t-\Delta t) + v_k(t-\Delta t)
$$

历史电流卷积输出：

$$
Y_c * v_k(t) = c_{Yc} x_{Yc}(t)
$$

### 有理函数拟合（矢量拟合核心）

特征导纳有理逼近（公共极点集与加权最小二乘）：

$$
\tilde{Y}_C(s) \approx k_0 + \sum_{n=1}^{N_{pY}} \frac{k_n}{s - a_n}
$$

传播函数模态分解与拟合（引入优化时间延迟$\tau_j$）：

$$
\tilde{H}(s) \approx \sum_{j=1}^{N_{mod}} \sum_{i=1}^{N_{pH}} \frac{c_{ij}}{s - a_i} e^{-s\tau_j}
$$

### 折叠线等效（FLE）变换

$$
Y_n = K \begin{bmatrix} Y_{oc} & 0 \\ 0 & Y_{sc} \end{bmatrix} K^{-1}
$$

将$2n\times 2n$的节点导纳矩阵解耦为两个$n\times n$子矩阵，降低拟合维度。

## 关键技术挑战

### 挑战1：低频特征值失真

直接对频变节点导纳矩阵$Y_n$进行有理拟合时，低频小特征值与高频大特征值跨度可达数个量级，导致矢量拟合精度严重下降。FLE通过将$Y_n$分解为两个$n\times n$子矩阵，将最大/最小特征值比值显著降低，矢量拟合阶数减少约20%~30%。

### 挑战2：数值发散与长递归误差

32位单精度浮点在长递归卷积（>10000步）中因舍入误差累积导致数值发散。Camara 2018实测32位单精度FPGA模型电流无法恢复稳态值。解法：采用48位自定义浮点格式彻底消除发散（LUT占用率48.39%，DSP48占用率47.08%）。

### 挑战3：实时仿真步长约束

FDPD相域模型计算量约为常参数模型的10倍，全流水线FPGA实现可将步长压缩至2.4µs~3.27µs（较传统50µs提升15~20倍），但需全流水并行架构与双端口RAM列优先存储设计。

### 挑战4：非对称/未换位线路的模态变换误差

恒定模态变换矩阵在强不对称平行线路中引入跨线互耦误差（>18%）。相域ULM直接避免模态变换，但计算成本高；模态揭示变换+宽频有理互耦模型作为折中方案，可将误差控制在1.5%以内。

### 挑战5：大地回路频变特性

Carson公式在>100kHz误差可达200%，需采用Nakagawa频变大地回路模型（高阻土壤雷电感应电压降低10-30%）；Carson在>100kHz误差增大是电缆和长线路建模的主要失效场景。

## 量化性能边界

### 模型精度对比

| 模型 | 精度 | 计算效率 | 步长约束 |
|------|------|---------|---------|
| Bergeron | 低（误差~15%） | 最高 | $\Delta t < \tau$ |
| J.Marti | 中（误差<2%） | 高 | $\Delta t < \tau$ |
| ULM | 高（误差<0.5%） | 中 | $\Delta t < \tau$ |
| FLE+MCNR | 高（误差<0.5%） | 高（+10~35%加速） | $\Delta t > \tau$（允许） |
| FDPD-FPGA | 高（误差≈0） | 实时（2.4µs步长） | 微秒级 |
| 平行线路互耦 | 高（误差<1.5%） | 中（-42%耗时） | $\Delta t < \tau$ |

### 实时仿真性能数据

- **FPGA FDPD步长**：2.4µs（8导体）/ 2.8µs（12导体），较传统处理器提升15~20倍
- **FLE+MCNR加速比**：10%~35%（取决于慢极点占比，强耦合线路稍低）
- **慢极点松弛更新稳定步长比**：$k$高达500时仍数值稳定
- **48位浮点精度**：彻底消除32位长递归卷积发散
- **Bergeron接口 vs 嵌入式**：接口模式2.4µs步长但高频段轻微偏差；嵌入式5.0µs步长但全频段零偏差

## 适用边界与选择指南

### 建模方法选择决策表

| 线路条件 | 推荐模型 | 不适用模型 |
|---------|---------|-----------|
| 短线路（<50km），工频 | Bergeron | — |
| 中长换位线路，频变参数 | J.Marti | Bergeron |
| 非对称/未换位/电缆 | ULM相域 | J.Marti（模态误差大） |
| 机电暂态大步长混合仿真 | FLE+MCNR | ULM（步长限制） |
| 实时数字仿真器（RTDS） | FDPD-FPGA | 软件仅实现 |
| 多回平行线路互感耦合 | 模态揭示+互耦模型 | 恒定矩阵FD |
| 雷电/VFTO超宽带暂态 | ULM+Nakagawa | Bergeron（精度不足） |

### 宽频带仿真参数配置

| 应用场景 | 步长 | 拟合极点数 | 频率范围 |
|---------|------|-----------|---------|
| 雷电暂态 | 10-50ns | 15-30 | 0.1Hz-10MHz |
| 开关过电压 | 1-10µs | 8-15 | 1kHz-100kHz |
| 实时仿真（FPGA） | 2.4-5.8µs | 8-12 | 1Hz-1kHz |
| 机电暂态混合 | 40-60ms | 3-5 | DC-100Hz |
| 谐波分析 | 50-100µs | 5-8 | 50Hz-2kHz |

## 相关方法

- [[vector-fitting]] - 频变参数有理逼近
- [[passivity-enforcement]] - 确保模型数值稳定
- [[numerical-integration-methods]] - 梯形法/后向欧拉法
- [[state-space-method]] - 相模变换解耦
- [[nodal-analysis]] - 网络方程求解
- [[modal-decomposition]] - 线路解耦理论基础
- [[folded-line-equivalent]] - 大步长等效模型
- [[frequency-dependent-line-model]] - J.Marti/FD-line

## 相关模型

- [[cable-model]] - 地下/海底电缆专题
- [[transformer-model]] - 线路-变压器接口
- [[fdne-model]] - 线路等值端网
- [[grounding-system-model]] - 杆塔/变电站接地

## 相关主题

- [[frequency-dependent-modeling]] - 广义频变建模
- [[harmonic-analysis]] - 宽频应用之一
- [[lightning-overvoltage]] - 雷击暂态仿真
- [[real-time-simulation]] - 实时线路模型
- [[parallel-computing]] - 大规模线路并行
- [[switching-transient]] - 操作过电压仿真

## 来源论文

以下论文为页面核心知识来源，全部经过wiki来源页 deep-review 验证：

- Camara 2018 (a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat) — FLE+MCNR快慢极点分离，10-35%加速，$\alpha$阈值优选
- Zanon 2021 (implementation-of-the-universal-line-model-in-the-alternative-transients-program) — ATP中ULM两阶段混合架构，拟合精度RMSE<1e-4
- Gustavsen 2012 (modal-domain-based-modeling-of-parallel-transmission-lines) — 模态揭示变换，6-12倍运行模态提升，耦合误差<1.5%
- Liu 2021 (development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga) — FPGA全流水并行2.4µs步长，48位浮点消除发散
- 徐政 1996 (耦合长线电磁暂态分析的扩展bergeron模型) — 多相耦合Bergeron扩展，开路/短路导纳分解
- Gustavsen 2012 parallel lines — 平行线路FD模型互耦误差>18%，解耦策略量化
- De Conti 2016 (extension-of-a-modal-domain-transmission-line-model-for-including-frequency-depe) — 频变大地回路参数扩展
- Loaiza-Elejalde 2026 (time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models) — ULM延迟精确估计all-pass函数法