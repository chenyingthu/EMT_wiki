---
title: "接口技术 (Interface Technique)"
type: method
tags: [interface, coupling, subnetwork, connection, partitioning, co-simulation, hybrid-simulation]
created: "2026-05-02"
updated: "2026-05-16"
---

# 接口技术 (Interface Technique)

## 定义

接口技术是 EMT 仿真中连接两个或多个子系统（subnetwork）的核心方法集合。在电磁暂态仿真中，复杂电力系统通常按电气距离、研究频带和建模精度需求划分为多个区域——局部高密度电力电子装置、近区故障和开关过程需要微秒级步长 EMT 详细建模，而远端交流网络或慢动态过程可用大步长相量域或暂态稳定模型。接口技术定义边界变量形式、等值电路拓扑、数据交换时序和稳定性处理规则，使分属于不同求解器的子系统能够协调运行并保持物理一致性。

从变量域角度，接口技术处理的是**瞬时量**（EMT 三相 $a$-$b$-$c$ 电压电流）、**相量**（基频或扩展频率动态相量 $\dot{X}_h(t)$）和**标量**（功率、电流幅值）之间的双向转换。从耦合时序角度，接口分为**强耦合同步**（同一时刻联立求解边界方程）、**串行松耦合**（一侧先推进再传边界量）和**并行松耦合**（多侧独立推进用预测或迭代修正边界量）。

## EMT 中的角色

EMT 网络通常按节点电压法或改写后的微分-代数方程（DAE）推进。接口技术把边界一侧的行为转换为另一侧可接受的输入，核心功能包括：

1. **电压连续与电流守恒**：接口两侧的边界电压相等、边界电流之和为零（$\sum i_{\text{interface}} = 0$）
2. **频率响应保留**：外部网络在研究频带内的阻抗特性在接口等值中被正确传递
3. **数值能量注入控制**：多速率或通信延迟不引入虚假能量导致数值发散
4. **事件与控制限幅同步**：故障、保护动作和控制限幅在两侧时间轴上有一致的触发顺序

接口质量直接影响混合仿真的波形精度、计算效率和数值稳定性。差的接口设计会在边界引入额外阻抗、一步延迟或相位误差，导致近区故障响应失真或慢子系统接收到虚假暂态。

## 接口变量与等值形式

### 电压型接口

电压型接口向另一侧施加边界电压，常用 Thevenin 等效形式：

$$
v_p(t) = v_{\text{th}}(t) - Z_{\text{th}} \, i_p(t) \tag{1}
$$

其中 $v_{\text{th}}(t)$ 为等效电压源，$Z_{\text{th}}$ 为等效阻抗，$i_p(t)$ 为接口电流。它适合把外部网络表现为电压源加源阻抗。若忽略 $Z_{\text{th}}$（理想电压源），强电压源对强电压源连接可能形成代数冲突或数值振荡。若 $Z_{\text{th}}$ 过小，还会把外部系统强加到 EMT 侧节点方程，使本应被等值的弱网表现为强网。

### 电流型接口

电流型接口向节点注入边界电流，常用 Norton 等效形式：

$$
i_p(t) = i_n(t) - Y_n \, v_p(t) \tag{2}
$$

其中 $i_n(t)$ 为等效电流源，$Y_n$ 为等效导纳。它与 EMT 节点电压法匹配较好，因为 $Y_n$ 可直接并入节点导纳矩阵，等效电流源进入右端项。若接口侧近似为理想电流源（$Y_n \to 0$）而缺少并联阻尼，开路或弱网条件下可能产生不合理电压尖峰。

### 功率型接口

功率型接口交换有功、无功或瞬时功率：

$$
p(t) = v^{\mathsf{T}}(t) \, i(t), \quad q(t) = v^{\mathsf{T}}(t) \, \mathbf{J} \, i(t) \tag{3}
$$

其中 $\mathbf{J} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ 为正交变换矩阵。在相量域，接口通常使用 $P + jQ$ 与基频电压相量计算等效电流 $I = (P - jQ)/V^*$；在 EMT 域，瞬时三相电压电流需要滤波、相量提取或功率平均。功率型接口物理含义清晰，但受测量窗、相角参考和不平衡分量影响。

### 多端口导纳接口

多端口接口保留端口间耦合，频域形式为：

$$
\mathbf{i}_p(s) = \mathbf{Y}_p(s) \, \mathbf{v}_p(s) + \mathbf{i}_{\text{hist}}(s) \tag{4}
$$

其中 $\mathbf{Y}_p(s)$ 为多端口导纳矩阵，$\mathbf{i}_{\text{hist}}(s)$ 为历史等效电流源。若外部网络频率相关性重要，$\mathbf{Y}_p(s)$ 可由 [[fdne-model]] 或 [[network-equivalent]] 构建有理函数拟合。若只保留对角单端口项（忽略 $\mathbf{Y}_p(s)$ 的非对角元素），会丢失并行线路、多馈入直流或接地回路的互耦。

## 接口分类体系

接口技术可按**三维度**进行类型学分类：

### 维度一：耦合强度

| 类型 | 耦合特性 | 典型接口形式 | 稳定性风险 |
|------|---------|------------|-----------|
| 强耦合 | 边界方程联立求解（Schur 补） | 戴维南/诺顿等效 + 全局边界方程 | 低，但计算代价高 |
| 串行松耦合 | 一侧先推进传边界量 | 单侧 Thevenin + 历史电流 | 一步延迟引入误差 |
| 并行松耦合 | 多侧独立推进 + 迭代修正 | 预测/保持/插值 + 子迭代 | 迭代不收敛风险 |

### 维度二：变量域

| 域 | 变量形式 | 步长范围 | 典型应用 |
|----|---------|---------|---------|
| EMT 瞬时域 | 三相瞬时值 $a$-$b$-$c$ | 1–100 μs | 换流器、MMC、近区故障 |
| 动态相量域 | 时变傅里叶系数 $\dot{X}_h(t)$ | 0.1–1 ms | DPIM、SFA、谐波分析 |
| 基频相量域 | 正序相量 $\dot{U}_1$ | 1–10 ms | EMT-TS 接口 |
| 暂态稳定域 | 等效功率/电流 | 10–50 ms | 大系统稳定分析 |

### 维度三：等值形式

| 等值形式 | 接口量 | 适用场景 |
|---------|-------|---------|
| Thevenin 等效 | $v_{\text{th}}, Z_{\text{th}}$ | 外部网络为电压源型 |
| Norton 等效 | $i_n, Y_n$ | 外部网络为电流源型或与节点方程自然匹配 |
| 功率/相量等效 | $P, Q, \dot{U}$ | EMT-TS 混合仿真、机电暂态接口 |
| 多端口导纳 | $\mathbf{Y}_p(s), \mathbf{i}_{\text{hist}}$ | 多馈入系统、含频率相关阻抗的等值 |

## 关键接口机制

### MATE：多区域戴维南等效框架

MATE（Multi-Area Thevenin Equivalent）将系统分为多个子系统，各子系统在边界端口用戴维南等效表示，通过边界联立方程同步求解接口量。设子系统 $\alpha$ 的端口戴维南电压为 $e_\alpha$，等效阻抗为 $Z_\alpha$，端口电流为 $I_\alpha$，则接口方程为：

$$
I_\alpha = Z_\alpha^{-1} \left( e_\alpha - \sum_{\beta \neq \alpha} V_{\text{boundary}} \right) \tag{5}
$$

MATE 的核心优势是各子系统可并行求解局部方程，仅在边界量处同步交换信息。根据 Huang & Vittal 2018，在 IEEE 9 节点系统中，MATE 接口在 10 μs:5 ms 步长比下可在工频周期内完成边界收敛，无额外一步延迟。

### DPIM：动态相量接口模型

DPIM（Dynamic Phasor Interface Model）将接口线路本身建模为动态相量域状态空间方程，替代依赖多周期采样的参数提取。接口 PI 支路的电压电流用滑动时间窗内的动态相量表示：

$$
\dot{x}_h(t) = \frac{1}{T} \int_{t-T}^{t} x(\tau) e^{-jh\omega\tau} d\tau, \quad h = 0, 1, 2, \ldots \tag{6}
$$

动态相量的微分关系转写为状态空间方程后，接口线路在 TS 基频量与 EMT 瞬时量之间承担物理过渡，而非先采样再滞后传输。根据 Shu 等 2017，DPIM 保留了接口线路动态，避免了换流器近区故障时 FFT/DFT 采样延迟导致的相位误差。

### CM：补偿法无延迟并行

补偿法（Compensation Method，CM）通过在 MANA（改进节点分析）框架中构造边界补偿电流，使网络可在任意支路处解耦并行。设子网 A 和 B 在边界支路 $k$ 处断开，补偿电流 $i_{\text{comp}}$ 满足：

$$
v_A^{(k)} - v_B^{(k)} = Z_{\text{line},k} \, i_{\text{comp}} \tag{7}
$$

主进程组装小规模边界方程 $A_{\text{comp}} \, i_{\text{comp}} = b_{\text{comp}}$，求解后各子网用 $i_{\text{comp}}$ 修正内部节点电压。根据 Bruned 等 2026，CM 在 3619 节点风电场算例中实现约 6.02× 加速比（10 μs:10 μs 步长），误差约 0.040%；在 473 节点改进 IEEE-34 算例中实现约 3.30× 加速比，误差约 7.2×10⁻³%。

### SFA-EMT：移频分析接口

SFA（Shifted Frequency Analysis）在复数时间相关相量（TDP）域处理基频附近慢变动态，与 EMT 的瞬时实值量通过 MATE 框架直接耦合。设解析信号 $z(t) = u(t) + j\mathcal{H}[u(t)]$，移频后：

$$
\ddot{u}(t) = \text{Re}\{ z(t) e^{-j\omega_0 t} \} \tag{8}
$$

SFA 步长不受传输线传播延迟限制，允许 Δt_SFA 与 Δt_EMT 成非整数倍关系，实现异步多速率接口。根据 Tarazona 2026，在改进 CIGRE HVDC 算例中，SFA-EMT MATE 接口使交流网络用 SFA 大步长、HVDC 换流器用 EMT 小步长，两者波形吻合且无额外延迟。

### ID-DP-ME：接口位移与动态相量映射等效

接口位移（Interface Displacement）将接口从换流器交流母线移到控制回路和 EMT 子网内部，利用控制/电路惯性弱化耦合。动态相量映射等效（DP-ME）直接计算 EMT 侧向 TS 侧注入功率：

$$
P_{\text{inj}}(t) = \text{Re}\{ \dot{U}(t) \dot{I}^*(t) \} \tag{9}
$$

接口延迟 $\tau$ 引入 $e^{-\tau s}$ 项使特征方程变为超越型，可用 Lambert W 函数分析稳定性边界。根据 Gao 等 2025，当 $\tau > 0$ 时，延迟使特征根右移，可能导致混合仿真发散。

### ESPRIT：短窗信号参数辨识接口

ESPRIT（Estimation of Signal Parameters via Rotational Invariance Techniques）将接口问题转化为短窗信号参数估计：给定接口处 $N$ 点采样序列，构造 Hankel 矩阵，通过低秩结构分离主导振荡分量，求得特征值换算各频率分量，再重构只含正频率成分的解析信号：

$$
\hat{x}(t) = \sum_{m=1}^{M} A_m \cos(\omega_m t + \phi_m) \tag{10}
$$

该方法从源头减少负频分量进入移频 EMT（SFEMT）模型，适合处理接口处含基波、谐波或间谐波的瞬时波形。根据 Gao 等 2025，ESPRIT 在短数据窗内可准确估计多分量信号频率、幅值和相位，但分量数选择和采样窗长度需谨慎设定。

## 稳定性与一致性要求

接口不是单纯的数据格式转换。最低限度的检查包括：

1. **电压电流方向和基准值一致**：两侧使用相同的相序、相角参考和标幺基准
2. **功率守恒**：接口注入功率在两侧符号约定下闭合（$\sum P_{\text{interface}} = 0$）
3. **无源性检查**：等效导纳或阻抗在目标频带内不引入非无源行为（尤其重要于 FDNE 频变等值）
4. **延迟与插值不掩盖快速动态**：处理方式应与研究对象频带匹配
5. **事件对齐**：故障、开关和控制限幅在两侧时间轴上有明确触发顺序

若接口基于频域等值，还应检查有理拟合的稳定极点（无右半平面极点）、无源性条件（$\text{Re}(Y(j\omega)) \geq 0$）和时域实现方式。相关背景见 [[vector-fitting]]（有理函数拟合）、[[fdne-model]]（频变网络等值）和 [[frequency-scan]]（阻抗扫描）。

## 关键技术挑战

### 挑战一：弱网条件下的数值振荡

当接口两侧等值为理想电压源（$Z_{\text{th}} = 0$）或理想电流源（$Y_n = 0$）时，强-强连接可能引起代数环或数值振荡。解决思路是在接口增加阻尼阻抗 $R_{\text{damping}}$，使等值在高频段呈现阻性。

### 挑战二：多速率接口的混叠与插值误差

当 Δt_fast = 10 μs、Δt_slow = 1 ms（100:1 步长比）时，从慢侧到快侧需要插值或零阶保持（ZOH），从快侧到慢侧需要抗混叠滤波后抽取。插值引入相位延迟，抽取引入高频折叠噪声。根据 Rupasinghe 2023，在 IEEE 118 + MMC-HVDC 算例中，25:1 步长比下计算时间从 694 s 降至 132 s（约 12.8×），但若插值阶次或滤波参数不当，波形误差会随仿真时长累积。

### 挑战三：故障期间的状态突变与切换

换相失败、阀组闭锁等离散事件在 EMT 侧产生状态突变，相量侧若无对应状态变化，切换时会出现电压电流跳变。Huang & Vittal 2018 提出的切换判据包含两步：先等待故障后延迟，再检查边界电压变化率是否低于阈值，确保快暂态已衰减；随后要求详细系统相量模型与外部系统边界电压偏差持续若干工频周期满足容差。

### 挑战四：多端耦合系统的接口耦合保留

当系统被划分为多个 EMT 子系统（各自独立求解）经由 TS 网络交互时，简单并行会把子系统间耦合忽略或错误简化。根据 Xiao 等 2017，两级 Schur 补可从全局分块导纳方程中消去各子系统内部节点，保留接口节点之间的等效耦合，使多 EMT 区域仍感知其余区域的动态影响。

### 挑战五：谐波与间谐波的接口量表示

传统基频相量接口不能直接解释高频谐波、非周期暂态或强不平衡瞬时量，除非提取算法和误差边界已说明。扩展频率动态相量（EDP）可保留 $h = 0, 1, 2, \ldots, H$ 次谐波，但接口数据量和通信开销随之增加。

## 量化性能边界

| 接口类型 | 步长配置 | 加速比 | 误差量级 | 验证场景 | 来源 |
|---------|---------|-------|---------|---------|------|
| EMT-DP 多求解器（BFAST） | 10 μs : 0.5 ms | ~12.8× | 波形基本一致 | IEEE 118 + MMC-HVDC (300 MW) | Rupasinghe 2023 |
| EMT-DP 补偿法 CM5 | 10 μs : 10 μs | ~3.30× | ~7.2×10⁻³% | 473 节点 IEEE-34 风电配电网 | Bruned 2026 |
| EMT-DP 补偿法 CM8 | 10 μs : 10 μs | ~6.02× | ~0.040% | 3619 节点风电场（45 台风机） | Bruned 2026 |
| EMT-TS MATE | 10 μs : 5 ms | 未报告 | 工频周期内收敛 | IEEE 9 节点 | Huang & Vittal 2018 |
| SFA-EMT MATE | 非整数倍步长 | 未报告 | 波形吻合 | 改进 CIGRE HVDC | Tarazona 2026 |
| DPIM | 10 μs : 5 ms | 未报告 | 相位误差优于 FFT/DFT 采样 | LCC-HVDC 实际工程 | Shu 等 2017 |
| ESPRIT 接口 | 步长比依赖采样窗 | 未报告 | 短窗参数估计有效 | SFEMT/EMT 联合仿真 | Gao 等 2025 |
| ID-DP-ME | 10 μs : 5 ms | 未报告 | Lambert W 延迟稳定性边界 | HVAC/DC 实际系统 | Gao 等 2025 |

**注**：量化数据来源于对应论文原文表格，未报告具体数值的项目标注"未报告"。

## 适用边界与选择指南

| 场景 | 推荐接口类型 | 主要理由 |
|------|------------|---------|
| 换流器近区故障（需保留高频动态） | DPIM 或 SFA-EMT MATE | 动态相量避免采样延迟，保留接口线路物理过渡 |
| 大规模交直流系统并行仿真 | CM（补偿法） | 不依赖物理延迟，短线路网络适用，嵌入 MANA 非线性迭代 |
| EMT-TS 长期稳定分析 | MATE + 模式切换 | 工频周期内收敛，离散事件状态同步 |
| 含谐波/间谐波的多频率动态 | ESPRIT + 扩展相量 | 短窗多分量估计，正频率解析信号重构 |
| 实时硬件在环（HIL） | 接口位移 ID-DP-ME | 控制惯性弱化耦合，减少延迟敏感性 |
| 电力电子化配电网（IBR 高渗透） | CM + 多核并行 | 无虚假延迟，避免数值振荡，6+ 倍加速 |

| 失效场景 | 不推荐类型 | 原因 |
|--------|----------|------|
| 强不平衡故障（三相不对称） | 基频相量接口 | 基频假设失效，负序/零序不可忽略 |
| 宽频暂态（直流侧高频） | 纯 DPIM（单谐波阶次） | 需扩展到多谐波阶次否则丢失高频动态 |
| 极高步长比（>1000:1） | 串行松耦合 | 插值误差累积，可能发散 |
| 弱交流系统（短路比 < 2） | 理想电压源 Thevenin | 接口畸变放大，换相失败风险高 |

## 相关方法与模型

- [[direct-interface-technique]]：强耦合分区接口，直接 Schur 补求解边界方程
- [[hybrid-modeling]]：模型层级和物理域组合，与接口技术互补但不等同
- [[electromechanical-electromagnetic-hybrid-simulation]]：机电相量域与 EMT 瞬时域混合仿真
- [[model-compatibility-layer]]：工具间模型语义和参数映射
- [[offline-to-realtime-porting]]：离线模型迁移到实时平台时的接口约束
- [[emt-simulation-verification]]：接口误差的验证和证据边界
- [[fdne-model]]：频变网络等值，常作为接口的外部网络模型
- [[vector-fitting]]：有理函数拟合，用于 FDNE 的参数化
- [[real-time-simulation]]：实时仿真平台对接口延迟和步长的约束

## 来源论文

- [[co-simulation-of-electrical-networks-by-interfacing-emt-and-dynamic-phasor-simul|Rupasinghe 2023]] — EMT-DP 样本映射算法，多速率接口设计，12.8× 加速比（IEEE 118 + MMC-HVDC）
- [[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu|Shu 等 2017]] — DPIM 动态相量接口模型，将接口线路作为状态空间方程求解
- [[interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd-24|Gao 等 2025]] — 接口位移 ID 与 DP-ME，Lambert W 延迟稳定性分析
- [[a-multi-solver-framework-for-co-simulation-of-transients-in-modern-power-systems|Rupasinghe 2023]] — 多求解器框架，BFAST 自适应切换，多接口耦合
- [[co-simulation-and-compensation-method-for-parallel-simulation-of-electromagnetic|Bruned 等 2026]] — 补偿法 CM 并行 EMT，MANA 框架，6.02× 加速比（3619 节点）
- [[advanced-emt-and-phasor-domain-hybrid-simulation-with-simulation-mode-switching-|Huang & Vittal 2018]] — MATE + 模式切换，离散状态一致性检查
- [[sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems|Tarazona 2026]] — SFA-EMT MATE 异步多速率，CIGRE HVDC 验证
- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Nelson River HIL]] — Manitoba Hydro Bipole I/II/III RTDS 实时 HIL 平台