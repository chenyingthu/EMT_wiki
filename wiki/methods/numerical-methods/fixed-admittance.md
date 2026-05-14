
---
title: "恒导纳模型 (Fixed Admittance / ADC Model)"
type: method
tags: [fixed-admittance, adc, real-time, companion-circuit]
created: "2026-04-13"
updated: "2026-05-10"
---

# 恒导纳模型 (Fixed Admittance / ADC Model)

## 1. 物理背景与工程需求

### 为什么需要恒导纳模型？

在 EMT 仿真中，每步需要求解节点方程 $\mathbf{Y}_n \mathbf{v} = \mathbf{i}$。若开关动作改变 $\mathbf{Y}_n$，就需要重新进行 LU 分解——计算量与 $N^3$ 成正比。在含大量电力电子开关的系统中（如 MMC 有数百个子模块），频繁重分解会使仿真速度骤降。

恒导纳模型的核心思想是将开关状态变化从左侧矩阵转移到右侧历史项：

$$
\mathbf{Y}_{\mathrm{fix}} \mathbf{v} = \mathbf{i}(s_k, x_{k-1}, u_k)
$$

矩阵 $\mathbf{Y}_{\mathrm{fix}}$ 固定不变，开关状态 $s_k$ 只影响右侧注入电流。这样 LU 分解只需做一次，每步只做前代回代 $O(nnz)$。

### 三个层级

恒导纳建模可以在三个层级实现，复杂度依次增加但精度也更高：

1. **单开关 ADC**：每个开关独立建模为固定导纳 + 历史源
2. **桥臂模块级 ADC（BAM-ADC）**：将上下开关、桥臂电感、电容整合为统一模块
3. **MMC 聚合恒导纳**：对子模块或桥臂做 Thevenin/Norton 聚合

---

## 2. 数学描述

### 统一形式

恒导纳模型的统一诺顿等效形式：

$$
i_k = G_{\mathrm{eq}} v_k + I_{\mathrm{hist}}(s_k, x_{k-1}, u_k)
$$

$G_{\mathrm{eq}}$ 在开关状态 $s_k$ 改变时保持不变，所有状态变化通过历史项 $I_{\mathrm{hist}}$ 体现。

### 参数化 ADC 模型（Bonjour et al., 2025）

对单个开关单元，参数化 ADC 模型写为：

$$
i_{sw}^n = G_{\mathrm{eq},sw} u_{sw}^n + \alpha G_{\mathrm{eq},sw} u_{sw}^{n-1} + \beta i_{sw}^{n-1}
$$

其中 $\alpha$、$\beta$ 是可调参数。通过 Z 变换终值定理推导理想稳态条件：

- 导通态：$\alpha \neq -1$，$\beta = 1$
- 关断态：$\alpha = -1$，$\beta \neq 1$

---

## 3. 计算模型与离散化

### 单开关 ADC

对理想开关，传统 $R_{\mathrm{on}}/R_{\mathrm{off}}$ 模型在切换时改变导纳矩阵。ADC 方法用固定导纳 $G_{\mathrm{eq}}$ 配合历史源：

- 导通：$I_{\mathrm{hist}}$ 使支路表现为小电阻
- 关断：$I_{\mathrm{hist}}$ 使支路表现为大电阻

矩阵不变，仅右端项变化。

### BAM-ADC（桥臂模块级）

Bonjour et al. (2025) 将桥臂模块整体建模。离散状态空间方程：

$$
x_1^n = A_1 x_1^{n-1} + b_1^n
$$

以状态转移矩阵谱半径 $\rho(A_1)$ 为核心指标进行参数寻优。最优参数下 $\rho(A_1) = 0$，暂态误差单步零收敛。

### MMC 聚合恒导纳

对 MMC 等含有大量重复子模块的拓扑，可在桥臂或模块级聚合：
- 消去内部节点，保留端口行为
- 外部导纳矩阵恒定
- 内部动态信息由历史源携带

---

## 4. 实现方法与算法细节

### CRI（交叉重初始化）

Bonjour et al. (2025) 提出的 CRI 是关键实现技术。开关状态切换时，不重新组网求解，而是用切换前后的交叉状态量重置历史注入源：

```text
检测到状态切换：
1. 记录切换前各支路电压、电流
2. 根据新拓扑计算应有的历史源初值
3. 用交叉状态量（旧状态 x 新配置）重置 I_hist
4. 继续用原有 Y_fix 求解
```

CRI 消除了切换瞬间的虚假初值误差，而不破坏固定导纳结构。

### 矩阵复用的收益

| 方法 | 每步矩阵操作 | 开关动作时的操作 | 适用场景 |
|------|-------------|-----------------|----------|
| $R_{\mathrm{on}}/R_{\mathrm{off}}$ | 前代回代 | 完全重分解 $O(N^3)$ | 开关少 |
| 单开关 ADC | 前代回代 | 历史项更新 $O(1)$ | 单开关 |
| BAM-ADC | 前代回代 | CRI + 历史项更新 $O(K)$ | 桥臂模块 |
| MMC 聚合 | 前代回代 | 聚合参数更新 $O(K)$ | 大量子模块 |

### 非互补导通降级

当进入非互补导通状态（如双管关断），BAM-ADC 自动降级切换回传统 L/C-ADC 模型，以确保仿真继续。

---

## 5. 适用边界与失效模式

### 什么条件下好用？

- 开关动作频繁（MMC、VSC、DAB 等变流器拓扑）
- 矩阵分解成本显著（大规模网络 $> 10^3$ 节点）
- 实时仿真需要确定性计算时间（FPGA 流水线）
- 外部只需要端口行为，不需要内部细节

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| 虚拟功率损耗 | 开关切换时有虚假能量耗散 | 历史源不匹配 | CRI 或参数优化 |
| 状态切换初值误差 | 切换后波形跳变 | 旧状态带入新拓扑 | CRI 重初始化 |
| 非互补导通 | 模型失效 | ADC 假设不成立 | 降级回 L/C-ADC |
| 步长过大 | 精度丧失 | 固定导纳的截断误差 $O(\max\{k_L, k_C\})$ | 减小步长 |
| 器件级研究 | 开关损耗、EMI、过电压无法获取 | 等效过于粗糙 | 使用详细模型 |

### 工程经验值

- Bonjour et al. (2025) 的 BAM-ADC：$\rho(A_1) = 0$ 实现单步误差收敛
- 矩阵求逆次数：从 $2mN$ 次（RON/ROFF）降至 1 次
- 等效导纳配置准则：$G_{\mathrm{eq},L} \ll G_{\mathrm{eq},1} + G_{\mathrm{eq},2} \ll G_{\mathrm{eq},C}$
- 误差 $< 1\%$ 要求：$2k_L/(1+\sqrt{k_1}) < 0.01$ 且 $2k_C(1+\sqrt{k_1}) < 0.01$

---

## 6. 应用案例

### 一个简单开关的 ADC 建模

考虑一个理想开关连接节点 1 和 2。传统 RON/ROFF 模型在两个状态间切换：
- 闭合：$Y_{11} += G_{\mathrm{on}}$，$Y_{22} += G_{\mathrm{on}}$，$Y_{12} -= G_{\mathrm{on}}$，$Y_{21} -= G_{\mathrm{on}}$
- 断开：$Y_{11} += G_{\mathrm{off}}$，$Y_{22} += G_{\mathrm{off}}$，$Y_{12}} -= G_{\mathrm{off}}$，$Y_{21} -= G_{\mathrm{off}}$

ADC 方法取固定导纳 $G_{\mathrm{eq}} = (G_{\mathrm{on}} + G_{\mathrm{off}})/2$：
- 闭合时历史源 $I_{\mathrm{hist}}$ 补偿 $G_{\mathrm{eq}}$ 与 $G_{\mathrm{on}}$ 的差异
- 断开时历史源补偿 $G_{\mathrm{eq}}$ 与 $G_{\mathrm{off}}$ 的差异

$\mathbf{Y}_n$ 始终不变，只有 $I_{\mathrm{hist}}$ 随状态变化。

### 验证步骤

如需验证固定导纳的精度：
1. 用 RON/ROFF 模型和恒导纳 ADC 分别仿真同一电路
2. 对比两种方法的波形差异（重点关注开关切换时刻）
3. 观察恒导纳模型是否产生虚拟功率损耗或谐波尖峰
4. 检查步长减小时误差是否收敛

---

## 7. 延伸阅读

### 核心参考文献

- [[a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul]] — Bonjour et al. (2025)：BAM-ADC 参数化模型，$\rho(A_1) = 0$
- [[a-state-variables-elimination-based-emtp-type-constant-admittance-equivalent-mod]] — 状态变量消元恒导纳等效
- [[unified-high-speed-emt-equivalent-and-implementation-method-of-mmcs-with-single-]] — MMC 高速恒导纳等效
- [[analytical-modeling-of-the-half-bridge-leg-using-an-associated-discrete-circuit-]] — 半桥腿 ADC 解析建模
- [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear]] — FPGA 实时固定导纳实现

### 相关页面

- [[nodal-analysis]] — 恒导纳复用矩阵的求解框架
- [[companion-circuit]] — 伴随电路与等效导纳
- [[compensation-method]] — 另一种避免重分解的方法
- [[sparse-matrix-solver]] — 固定矩阵的分解复用
- [[switch-modeling]] — 开关模型的 ADC 等效
- [[mmc-model]] — MMC 聚合恒导纳的应用对象
- [[interpolation-method]] — 开关时刻对齐与历史项修正

## 来源论文

| 论文 | 年份 |
|------|------|
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[适用于电磁暂态仿真的变阶变步长3s-dirk算法|适用于电磁暂态仿真的变阶变步长3S-DIRK算法]] | 2020 |
| [[一种用于电磁暂态仿真的两电平电压源型换流器解耦模型|一种用于电磁暂态仿真的两电平电压源型换流器解耦模型]] | 2022 |
| [[中-国-电-机-工-程-学-报-34|中  国  电  机  工  程  学  报]] | 2022 |
| [[中-国-电-机-工-程-学-报|中  国  电  机  工  程  学  报]] | 2022 |
| [[模块化多电平换流器电磁暂态模型研究综述|模块化多电平换流器电磁暂态模型研究综述]] | 2022 |
| [[计及电容过渡过程的双钳位型mmc电磁暂态高效仿真方法|计及电容过渡过程的双钳位型MMC电磁暂态高效仿真方法]] | 2022 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|一种级联H桥型电力电子变压器电磁暂态解耦与仿真模型]] | 2023 |
| [[基于cpu-fpga异构平台的虚拟同步并网逆变器实时仿真算法设计|基于CPU-FPGA异构平台的虚拟同步并网逆变器实时仿真算法设计]] | 2023 |
| [[su-等-a-fixed-admittance-algorithm-for-the-fpga-based-microsecond-level-nonlinear|Su 等 | A fixed-admittance algorithm for the FPGA-based micro]] | 2025 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal Decoupled Equivalent Circuit Models of Solid-State]] | 2025 |
| [[中-国-电-机-工-程-学-报-37|中  国  电  机  工  程  学  报]] | 2025 |
| [[rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability|RMS&#x002B;: Augmenting the Traditional Circuit Model to Cap]] | 2026 |
