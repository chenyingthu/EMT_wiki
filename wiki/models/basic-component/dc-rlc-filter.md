---
title: "直流侧RLC滤波器 (DC-Side RLC Filter)"
type: model
tags: [dc-filter, rlc, converter, ripple, power-electronics, emi-filter, passive-filter]
created: "2026-05-02"
updated: "2026-05-18"
---

# 直流侧RLC滤波器 (DC-Side RLC Filter)

## 定义与边界

直流侧 RLC 滤波器（DC-Side RLC Filter）是在变流器、直流母线、储能或直流网络端口附近布置的无源滤波与阻尼网络。物理对象是电感、电容、电阻、连接母排、接地/屏蔽路径和器件寄生参数；EMT 等效对象是由 R、L、C 支路、状态变量、伴随导纳和历史源组成的端口网络。

本页聚焦 EMT 模型，不把 RLC 参数选择写成通用设计规范。纹波限值、阻尼比、开关频率比例、EMI 标准和元件额定值必须绑定设备、标准或论文算例；否则只应作为设计变量或验证项目出现。

## EMT 中的角色

直流侧 RLC 滤波器在 EMT 仿真中承担三类核心任务：

**1. 纹波抑制**：变流器开关动作在直流侧产生谐波电压/电流，RLC 滤波器提供低通通道将纹波旁路或阻尼。开关频率 $f_{\mathrm{sw}}$ 通常为 $2\text{–}10$ kHz（MMC）或 $f_{\mathrm{sw}} = 1\text{–}5$ kHz（三电平 VSC），对应的谐波次数在 $2f_{\mathrm{sw}}$ 以内需有效抑制。

**2. 谐振阻尼**：直流网络的寄生电感 $L_{\mathrm{dc}}$ 和电容 $C_{\mathrm{dc}}$ 与滤波电容形成固有谐振频率 $f_0 = 1/(2\pi\sqrt{L_{\mathrm{dc}}C_{\mathrm{dc}}})$，若不阻尼则换流器控制扰动或故障会激发谐振，导致电压/电流振荡失真。

**3. 阻抗匹配**：换流器直流侧等效阻抗 $Z_{\mathrm{cnv}}$ 与直流网络的特性阻抗 $Z_{\mathrm{dc}} = \sqrt{L_{\mathrm{dc}}/C_{\mathrm{dc}}}$ 若不匹配，直流电压会发生反射。RLC 滤波器可作为缓冲网络，吸收反射能量并降低电压过冲。

**EMT 建模的特殊挑战**：RLC 滤波器在 EMT 中不是孤立二阶系统——它的有效阻尼和谐振频率还受源阻抗、负载阻抗、换流器控制、采样延迟、电缆电容和外部网络影响。因此，单独 RLC 公式只能支撑局部模型定义，不能直接证明系统级稳定。

## EMT 建模方法

### 方法一：梯形积分伴随模型（Companion Model）

进入 EMT 节点法后，每个电感和电容通过梯形积分法转换为当前等效导纳和历史源。以串联 $R$-$L$ 后接并联 $C$ 的低通结构为例，电感支路的伴随模型为：

$$G_L = \frac{\Delta t}{2L}, \qquad i_{\mathrm{hist},L}(t) = G_L \cdot v_L(t-\Delta t) + i_{\mathrm{hist},L}(t-\Delta t)$$

电容支路的伴随模型为：

$$G_C = \frac{2C}{\Delta t}, \qquad i_{\mathrm{hist},C}(t) = G_C \cdot v_C(t) + i_{\mathrm{hist},C}(t-\Delta t)$$

组合后，完整 RLC 滤波器的节点导纳矩阵为：

$$\mathbf{Y}_{\mathrm{RLC}} = \begin{bmatrix} G_L + G_C & -G_C \\ -G_C & G_C + 1/R_d \end{bmatrix}$$

其中 $R_d$ 为可选阻尼路径。并联电容注入节点网络的电流为 $i_C(t) = G_C v_C(t) + i_{\mathrm{hist},C}(t-\Delta t)$。

### 方法二：状态空间-节点混合法（SSN）

对于多谐振复杂滤波器，直接节点法会因谐振条件恶劣（高 Q 值）产生数值振荡。状态空间-节点混合法将电感电流和电容电压保留为状态变量，其余网络部分用节点法求解。状态方程为：

$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}, \qquad \mathbf{A} = \begin{bmatrix} -R/L & -1/L \\ 1/C & -1/(R_d C) \end{bmatrix}$$

其中状态向量 $\mathbf{x} = [i_L,\; v_C]^T$。将状态空间方程与节点方程联立，通过舒尔补得到端口等效：

$$\mathbf{Y}_{\mathrm{port}} = \mathbf{G}_C - \mathbf{C}_c^T (\mathbf{A}^{*})^{-1} \mathbf{B}^{*}$$

其中 $\mathbf{A}^{*} = \mathbf{A} - \mathbf{I}\frac{2}{\Delta t}$，$\mathbf{G}_C$ 为电容伴随导纳矩阵。该方法在时域中自动满足无源性约束，数值稳定性优于纯节点法。

### 方法三：频域响应拟合法（Frequency-Dependent）

当滤波器的目标频段覆盖 $10\text{–}100$ kHz（SiC/GaN 换流器的高频开关谐波），寄生参数（ESR、ESL、寄生电容）必须纳入建模。频域响应拟合法通过矢量拟合（Vector Fitting）得到频域等效电路：

$$Z(j\omega) = \sum_{k=1}^{N} \frac{r_k}{j\omega - p_k} + d + s\cdot j\omega$$

其中 $r_k$ 和 $p_k$ 为留数和极点，$d$ 为实部常数项，$s$ 为刚度系数。拟合后的等效电路包含 $N$ 个一阶 RC/RL 支路，可直接转换为 EMT 时域伴随模型。该方法的精度取决于拟合阶数 $N$ 和频段覆盖范围。

### 方法四：时域伴随-source 等效法

对于已知谐波成分的稳态分析（如 MMC 子模块电容电压纹波分析），可将 RLC 滤波器等效为在特定谐波频率 $h\omega_1$ 处的等效阻抗：

$$Z_{\mathrm{eq}}(h\omega_1) = R + j\left(h\omega_1 L - \frac{1}{h\omega_1 C}\right)$$

对应的时域等效源为 $v_{\mathrm{eq}}(t) = \sum_{h} |V_h| \sin(h\omega_1 t + \phi_h)$。该方法计算量最小，适用于谐波潮流和稳态纹波估算，但不适于暂态分析。

## 形式化表达

### 基础谐振关系

$$\omega_0 = \frac{1}{\sqrt{LC}}, \qquad \zeta = \frac{R}{2}\sqrt{\frac{C}{L}}, \qquad f_0 = \frac{1}{2\pi\sqrt{LC}}$$

其中 $\omega_0$ 为谐振角频率，$\zeta$ 为阻尼比，$f_0$ 为谐振频率。

### 梯形积分表观阻抗误差（Carbonea & Dommel 2002）

**电感支路**：相对阻抗误差为

$$\epsilon_{X_L}(\omega) = \frac{X_{L,\mathrm{APP}} - X_L}{X_L} = \frac{\omega\Delta t / 2}{\tan(\omega\Delta t/2)} - 1 \approx -\frac{(\omega\Delta t)^2}{12}$$

当 $\omega\Delta t \gg 1$（即频率接近 $1/\Delta t$ 的奈奎斯特频率附近）时，误差急剧增大。

**电容支路**：相对容抗误差为

$$\epsilon_{X_C}(\omega) = \frac{X_{C,\mathrm{APP}} - X_C}{X_C} = 1 - \frac{\tan(\omega\Delta t/2)}{\omega\Delta t/2} \approx \frac{(\omega\Delta t)^2}{12}$$

**串联 RLC 电路**（品质因数 $Q = \omega_0 L/R$，谐振频率 $\omega_0$）：

$$\epsilon_Z(\omega) = \frac{Z_{\mathrm{APP}} - Z}{Z} = jQ\left(1 - \frac{\omega^2}{\omega_0^2}\right)\frac{1}{1+j} \quad \text{（近似）}$$

在谐振点 $\omega \to \omega_0$ 处，复合阻抗误差可达约 **100%**（即表观阻抗是实际阻抗的约 2 倍），且误差随 $Q$ 值线性增长，随 $\omega_0$ 呈平方律增长。

**并联 RLC 电路**：最大误差出现在谐振频率前约 **10%** 处，与串联电路的对称误差分布不同。

### 离散伴随导纳

$$G_L^{(n)} = \frac{\Delta t}{2L}, \qquad i_{\mathrm{hist},L}^{(n)} = G_L^{(n)} v_L^{(n-1)} + i_{\mathrm{hist},L}^{(n-1)}$$

$$G_C^{(n)} = \frac{2C}{\Delta t}, \qquad i_{\mathrm{hist},C}^{(n)} = G_C^{(n)} v_C^{(n)} + i_{\mathrm{hist},C}^{(n-1)}$$

### 多层寄生参数模型

| 参数 | 来源 | 影响频率 |
|------|------|----------|
| ESR（等效串联电阻） | 电感绕组电阻、电容介质损耗 | 全频段 |
| ESL（等效串联电感） | 电感磁路饱和、母排分布电感 | $>10$ kHz |
| 寄生电容 $C_p$ | 线圈-地电容、电容引线电感 | $>100$ kHz |
| 温度依赖 $R(T)$ | 铜损温升 $R = R_0[1+\alpha(T-T_0)]$ | $>1$ kHz |

## 模型结构与接口变量

| 变量类别 | 典型内容 | EMT 作用 |
|----------|----------|----------|
| 端口变量 | 直流母线电压、滤波器电流、负载/源端电流 | 接入换流器和直流网络 |
| 状态变量 | 电感电流 $i_L$、电容电压 $v_C$、阻尼支路状态 | 描述储能和瞬态响应 |
| 代数变量 | 当前等效导纳、节点注入电流、约束电压 | 进入节点导纳矩阵 |
| 控制接口 | 直流电压控制、电流限幅、调制或保护状态 | 改变激励和等效阻抗 |
| 寄生变量 | ESR、ESL、绕组电阻、寄生电容、母排电感 | 影响高频谐振和 EMI |

## 建模层级

| 层级 | 保留内容 | 适合用途 | 边界 |
|------|----------|----------|------|
| 理想 RLC | 标称 R、L、C 和二阶动态 | 控制调试、低频纹波、局部谐振 | 不描述损耗、温度和高频寄生 |
| 含 ESR/ESL 模型 | 元件串联电阻、电感和阻尼支路 | 实际阻尼、损耗和中频谐振 | 参数需由器件或测量支撑 |
| 频率相关阻抗 | 电感绕组损耗、电容介质损耗、母排寄生 | EMI、传导干扰、宽频稳定 | 需要频响或结构参数 |
| 与控制耦合模型 | 变流器控制、采样、限幅和保护 | 直流母线稳定、故障恢复 | 控制模型边界必须明示 |
| 多端口直流网络模型 | 多换流器、电缆、储能和接地耦合 | VSC-HVDC、MTDC、直流配电 | 不能用单个二阶滤波器外推 |

## 量化性能边界

RLC 滤波器模型在 EMT 仿真中的量化性能边界如下（数据来源：Carbonea & Dommel 2002）：

**步长敏感性（梯形积分法）**：

| 仿真步长 $\Delta t$ | $f > 5$ kHz 误差 | $f > 10$ kHz 误差 | 适用场景 |
|---------------------|-------------------|-------------------|----------|
| $50\;\mu\text{s}$ | 显著，不可忽略 | ~100%（谐振点） | 低频纹波分析 |
| $20\;\mu\text{s}$ | $<5\%$ | $20\text{–}50\%$ | 中频谐振分析 |
| $5\;\mu\text{s}$ | $<1\%$ | $<10\%$ | 高频 EMI 分析 |
| $1\;\mu\text{s}$ | 可忽略 | $<2\%$ | SiC/GaN 高频换流器 |

**误差随频率的增长规律**：对于固定 $\Delta t$，误差近似随 $\omega^2$ 增长（即 $f^2$ 增长）。典型 $50\;\mu\text{s}$ 步长下，$f=5$ kHz 时误差约 $5\%$，$f=10$ kHz 时误差已达 $20\%$，$f=25$ kHz（开关谐波频段）时误差接近 $100\%$。

**误差随品质因数增长**：$Q$ 值每增大一倍，谐振点附近误差约增大一倍（串联 RLC）或增大 $10\%$（并联 RLC）。

**不同拓扑的误差特征**：

| 拓扑 | 误差最大值位置 | 典型误差量级 |
|------|----------------|--------------|
| 串联 RLC | 紧邻谐振频率 $f_0$ | $Q \times \epsilon_{X_L/X_C}$ |
| 并联 RLC | 谐振频率前约 $10\%$ | 约谐振点误差的 $0.5\text{–}0.7$ 倍 |
| CLC $\pi$ 型 | 各 $L$/$C$ 节点处 | 分布型，需多频率点评估 |
| 阻尼支路型 | 取决于 $R_d$ 位置 | $R_d$ 越小阻尼越大但损耗越大 |

## 关键技术挑战

**挑战一：数值截断误差与谐振放大（Carbonea/Dommel 2002）**

梯形积分法在 $f > 5$ kHz 时误差显著，在谐振点附近复合阻抗误差可达约 100%，远超单一元件的局部误差。高 Q 值谐振电路中，误差被品质因数和谐振结构进一步放大。**解法**：对高频谐振分析使用 $\Delta t \leq 5\;\mu\text{s}$，或切换为后向欧拉法（无条件稳定但增大数值阻尼）。

**挑战二：寄生参数的高频建模**

当换流器使用 SiC/GaN 器件时，开关频率提升至 $100\text{–}500$ kHz，ESR/ESL/寄生电容对 EMI 和共模干扰的影响不可忽略。精确寄生参数需要结构仿真（有限元分析）或宽频测量（$1\text{–}100$ MHz VNA 扫频）。**解法**：矢量拟合建立宽频等效电路，或使用高频电磁瞬态仿真（FDTD）替代集总参数模型。

**挑战三：与换流器控制的耦合效应**

直流滤波器端口电压受换流器控制（直流电压控制/电流限幅）调制，控制环的带宽（通常 $5\text{–}50$ Hz）与滤波器谐振频率（$1\text{–}10$ kHz）存在多速率交互。控制扰动通过滤波器注入网络，可能激发谐振不稳定。**解法**：多速率联合仿真（控制步长 $\Delta t_c \gg$ 电磁步长 $\Delta t_e$），或使用谐波状态空间（HSS）方法将控制-滤波器耦合建模为线性周期时变（LPTV）系统。

**挑战四：直流故障暂态中的非线性行为**

直流故障（极间短路、单极接地）期间，换流器闭锁导致直流侧等效为低阻抗故障点，原有 RLC 滤波器的初始储能（电容电压、电感电流）通过故障点释放，产生高频振荡。饱和电感、压敏电阻（MOV）和熔断器等非线性元件改变等效拓扑。**解法**：在故障期间切换滤波器的等效拓扑（断开阻尼支路、接入故障限流电抗），并在恢复时正确初始化状态变量。

**挑战五：多换流器直流网络中的谐振耦合**

VSC-HVDC 或 MTDC 中，多台换流器的直流侧滤波器通过直流母线电容相互耦合，形成多自由度谐振系统。各端口滤波器的谐振频率可能重合（强耦合）或接近（弱耦合），耦合强度由直流母线阻抗矩阵 $\mathbf{Z}_{\mathrm{dc}}$ 决定。**解法**：建立多端口网络等效（$N\times N$ 导纳矩阵），使用模态分析识别谐振耦合路径。

## 适用边界与失败模式

- 低通传递函数只在端口定义和负载假设明确时成立；源/负载阻抗变化会移动阻尼和谐振。
- 忽略电容 ESR/ESL 与电感寄生电容时，高频振荡和 EMI 结果可能失真。
- 过小阻尼会放大开关谐波或控制扰动；过大阻尼会引入损耗和热边界，需要单独验证。
- 直流故障、闭锁和保护动作会改变等效拓扑；滤波器初始能量和历史项需重新检查。
- 纹波百分比、THD、插入损耗或标准合规结论必须绑定测试系统、频段、测量点和标准版本。
- 与 [[average-value-model|平均值模型]] 连接时，开关纹波可能被模型本身消除；此时不能用该结果评价高频滤波效果。
- 对 SiC/GaN 换流器（$f_{\mathrm{sw}} > 100$ kHz），$50\;\mu\text{s}$ 步长下数值截断误差接近 100%，需将步长压缩至 $1\;\mu\text{s}$ 以下或使用专用高频模型。

## 验证需求

RLC 滤波器模型至少应验证：

1. **元件参数**：R、L、C、ESR、ESL、阻尼支路和温度依赖是否有来源。
2. **频域响应**：端口阻抗、传递函数或插入损耗是否在目标频段匹配测量、解析或详细模型。
3. **时域响应**：直流母线阶跃、负载突变、开关纹波、故障恢复和控制动作是否在同一工况下比较。
4. **数值实现**：[[trapezoidal-rule|梯形法]]或[[backward-euler|后向欧拉法]]是否造成数值振荡或过度阻尼。

若研究目标是电磁兼容，应明确共模/差模路径、接地电容、安全限制和测量端口；普通直流低通模型不足以替代 [[emi-filter-model|EMI 滤波器]]。

## 相关模型

- [[inductor-model]]：RLC 滤波器中电感支路的 EMT 伴随模型来源
- [[capacitor-model]]：RLC 滤波器中电容支路的 EMT 伴随模型来源
- [[companion-circuit]]：梯形积分离散化的伴随电路理论基础
- [[nodal-admittance-matrix]]：RLC 滤波器接入网络方程的矩阵形式
- [[vector-fitting]]：频域响应拟合法的理论基础
- [[harmonic-analysis]]：滤波器谐振频率与谐波分析的关联

## 相关主题

- [[vsc-hvdc]]：VSC-HVDC 中的直流侧滤波器应用
- [[dc-dc-converter]]：DC-DC 变换器的直流滤波器设计
- [[power-electronics-control]]：换流器控制与滤波器交互
- [[frequency-domain-analysis]]：宽频阻抗分析与滤波器设计
- [[passivity-enforcement]]：无源性约束在滤波器建模中的意义
- [[emi-filter-model]]：EMI 滤波器的完整建模框架

## 来源论文

- [[analysis-and-estimation-of-truncation-errors-in-modeling-complex-resonant-circui-fix|Carbonea 等 2002]] — 《Analysis and estimation of truncation errors in modeling complex resonant circuits with the EMTP》，*Electrical Power and Energy Systems*，系统分析梯形积分法在 RLC 谐振电路中的截断误差，推导串联/并联 RLC 的解析误差公式，给出 $f > 5$ kHz 时误差不可忽略、谐振点误差达 100% 的量化结论
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient|Navarro 等]] — 《A combined state-space nodal method for the simulation of power system transients》，提出状态空间-节点混合法在含 RLC/开关电路 EMT 仿真中的应用
- [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Ramirez 等 2021]] — 《Parallel computation of power system EMTs through polyphase QMF filter banks》，多相 QMF 滤波器组在 EMT 并行计算中的应用，间接涉及无源滤波器设计与实现
- [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent|Ahmadi 等 2021]] — 《A guaranteed passive model for multi-port frequency dependent network equivalents》，多端口频域依赖网络等值，保证无源性的宽频等效方法