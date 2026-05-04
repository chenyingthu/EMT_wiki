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

**大步长仿真突破**

传统模型要求 $\Delta t < \tau$，折叠线模型允许 $\Delta t > \tau$：

$$
Y_{eq}(s) = Y_{oc}(s) + Y_{sc}(s)
$$

其中短路分量吸收传播时延效应，实现大步长仿真时的数值稳定性。

**适用场景**：机电暂态、混合仿真

---

## 适用边界

- Bergeron模型仅适用于短线路、低频暂态，长线路高频误差可达15%
- 模态变换模型在对称/换位线路精度高，非对称线路需用相域模型
- 频变模型计算量大，实时仿真需采用简化或FPGA加速
- 电缆模型必须考虑大地回路频变特性，Carson公式在>100kHz误差增大
- 电晕效应模型需要ns级步长，不适合大规模系统仿真

---

## 代表性来源

| 论文 | 年份 | 关联要点 |
|------|------|----------|
| [[耦合长线电磁暂态分析的扩展bergeron模型]] | 1996 | 多相耦合线路Bergeron扩展 |
| [[new-multiphase-mode-domain-transmission-line-model]] | 1999 | 实数模态变换矩阵 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms]] | 1999 | 变步长线路模型 |
| Frequency-dependent transmission line modeling | 2001 | 换位条件利用 |
| [[transmission-line-modeling-with-explicit-grounding-representation]] | 2002 | 显式接地建模 |
| [[passivity-enforcement-for-transmission-line-models]] | 2008 | ULM无源性强制 |
| Development of phase domain FD line model on FPGA | 2021 | FPGA实时实现 |
| Using the Exact Equivalent π-Circuit | 2022 | 精确π电路时域实现 |
| Transient Analysis Combining VF and Nakagawa | 2022 | 矢量拟合+Nakagawa |
| Algorithms for Fast Calculation of Energization Overvoltage | 2023 | 混合线路快速计算 |

## 技术演进脉络

### 1960s-1980s：基础模型建立
- **Bergeron模型** (1960s)
  - 无损线行波等效
  - EMTP标准模型
- **模态变换理论** (1970s)
  - 多相线路解耦方法
  - Clarke/特征向量变换

### 1980s-2000s：频变建模突破
- **J. Marti模型** (1980s)
  - 频变特征阻抗/传播常数
  - 矢量拟合算法应用
- **ULM通用线路模型** (1990s)
  - 相域直接实现
  - 非对称线路精确建模

### 2000s-2010s：无源性校正与扩展
- **无源性强制算法** (2000s)
  - 解决ULM数值发散问题
  - 摄动法与RLC滤波器法
- **宽频建模** (2010s)
  - 雷电/VFTO仿真
  - 地下电缆精确模型

### 2010s-2026：实时与高效仿真
- **FPGA硬件实现** (2010s-2020s)
  - 2.4μs步长实时仿真
  - 自定义48位浮点
- **大步长/折叠线模型** (2020s)
  - 机电暂态联合仿真
  - 变步长自适应算法

## 关键发现汇总

### 模型性能对比
- **[1996]** 扩展Bergeron模型：多相耦合暂态精度显著提升
- **[1999]** 实数模态变换：恒定矩阵降低计算复杂度，误差<2%（对称线路）
- **[2001]** 混合换位模型：计算速度提升3-4倍，精度与全相域一致
- **[2021]** FPGA相域模型：2.4μs步长，48位浮点消除累积误差
- **[2022]** 精确π电路：避免卷积计算，矢量拟合+RLC综合

### 特殊现象建模
- **[2002]** 显式接地模型：雷击暂态地电位升预测，宽频带高精度
- **[2020]** 电晕-频变耦合模型：过电压预测误差降低27-49%
- **[2021]** 残余电荷模型：传统频变模型放电仿真不一致问题
- **[2023]** 混合线路模型：架空+电缆，误差<0.3%，耗时减少40-70%

### 土壤与接地
- **[2016]** Nakagawa模型：高阻土壤(10000Ω·m)雷电感应电压降低10-30%
- **[2022]** 频变土壤模型：Carson在>100kHz误差可达200%

### 前沿研究方向
- **模型降阶**：平衡截断降阶，62阶→20阶，误差<0.5%
- **无源性保持**：全频段(10Hz-10MHz)严格无源，避免过补偿
- **量子计算应用**：线路特征值求解的量子加速
- **数字孪生集成**：高频模型与PMU数据实时融合

## 深度增强内容

### 1. 模型选择决策树

```
线路类型？
├── 架空输电线路
│   ├── 短线路(<50km) → Bergeron模型
│   ├── 中长线路 → 频变模态模型
│   └── 非换位/非对称 → 相域ULM模型
├── 地下/海底电缆
│   ├── 工频分析 → 恒定参数π型
│   └── 暂态分析 → Nakagawa频变模型
└── 混合线路
    └── 全频域参数模型 + 改进NILT

暂态类型？
├── 雷电/快速暂态(>100kHz) → 宽带模型+频变土壤
├── 开关操作(1-100kHz) → ULM/Marti模型
├── 谐波传播(<1kHz) → 恒定参数Bergeron
└── 机电暂态混合 → 折叠线等效模型
```

### 2. 仿真参数配置表

| 应用场景 | 步长 | 极点数 | 关键设置 |
|---------|------|--------|---------|
| 雷电暂态 | 10-50ns | 15-30 | 频带0.1Hz-10MHz |
| 开关过电压 | 1-10μs | 8-15 | 土壤频变模型 |
| 实时仿真 | 2.4-5.8μs | 8-12 | FPGA全流水线 |
| 机电暂态 | 40-60ms | 3-5 | 允许Δt>τ |
| 谐波分析 | 50-100μs | 5-8 | 实常数变换矩阵 |

### 3. 典型线路参数参考

| 线路类型 | 电压等级 | R(Ω/km) | L(mH/km) | C(μF/km) |
|---------|---------|---------|---------|---------|
| 单分裂架空线 | 500kV | 0.02 | 0.9 | 0.013 |
| 四分裂架空线 | 1000kV | 0.007 | 0.85 | 0.014 |
| XLPE电缆 | 220kV | 0.05 | 0.35 | 0.25 |
| 海底电缆 | ±320kV | 0.01 | 0.25 | 0.35 |

### 4. 宽频建模检查清单

- [ ] 频率范围覆盖暂态主频分量
- [ ] 集肤效应参数随频率更新
- [ ] 大地回路模型选择（Carson/Nakagawa）
- [ ] 土壤电阻率频变特性
- [ ] 无源性条件验证
- [ ] 极点数充足（谐振峰捕捉）
- [ ] 步长满足稳定性要求

## 相关方法
- [[vector-fitting]] - 频变参数有理逼近
- [[passivity-enforcement]] - 确保模型稳定性
- [[numerical-integration-methods]] - 梯形法/后向欧拉法
- [[state-space-method]] - 相模变换解耦
- [[transmission-line-modeling]] - 时域高效实现
- [[wideband-modeling]] - 宽带频变特性

## 相关模型
- [[cable-model]] - 地下/海底电缆专题
- [[transformer-model]] - 线路-变压器接口
- [[fdne-model]] - 外部网络等值
- [[grounding-system-model]] - 杆塔/变电站接地

## 相关主题
- [[frequency-dependent-modeling]] - 广义频变建模
- [[harmonic-analysis]] - 宽频应用之一
- [[lightning-overvoltage]] - 雷击暂态仿真
- [[real-time-simulation]] - 实时线路模型
- [[parallel-computing]] - 大规模线路并行

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
*支撑书籍第二篇第4章"输电线路与电缆建模"*
