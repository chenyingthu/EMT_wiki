---
title: "灵敏度分析 (Sensitivity Analysis)"
type: method
tags: [sensitivity, analysis, parameter, stability, optimization, eigenvalue, participation-factor]
created: "2026-05-02"
updated: "2026-05-18"
---

# 灵敏度分析 (Sensitivity Analysis)

## 定义与边界

灵敏度分析研究模型输出、误差指标或稳定指标随参数变化的局部或全局响应。它回答"哪个参数更影响结果"和"沿哪个方向调整最可能改变指标"，但不能单独证明因果机制、参数可辨识性或控制方案有效。

本页聚焦 EMT 方法用途：参数筛选、模型校准、模态解释、控制整定和不确定性排序。与[[least-squares-method]]（可辨识性判断）、[[parameter-identification]]（参数反演）、[[small-perturbation-linearization]]（线性化模型）和[[modal-analysis]]（模态参与因子）紧密相关。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 380" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入层 -->
  <rect x="20" y="30" width="140" height="60" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">EMT模型参数</text>
  <text x="90" y="72" text-anchor="middle" font-size="10" fill="#3b82f6">线路频变参数</text>
  <text x="90" y="84" text-anchor="middle" font-size="10" fill="#3b82f6">换流器控制增益</text>

  <rect x="20" y="100" width="140" height="60" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">PLL/控制参数</text>
  <text x="90" y="142" text-anchor="middle" font-size="10" fill="#3b82f6">同步电机参数</text>
  <text x="90" y="154" text-anchor="middle" font-size="10" fill="#3b82f6">负荷/开关器件</text>

  <rect x="20" y="170" width="140" height="60" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="90" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e40af">初始化状态</text>
  <text x="90" y="212" text-anchor="middle" font-size="10" fill="#3b82f6">拓扑/故障事件</text>
  <text x="90" y="224" text-anchor="middle" font-size="10" fill="#3b82f6">饱和/限幅参数</text>

  <!-- 方法层：局部 -->
  <rect x="220" y="30" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="300" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">局部差分法</text>
  <text x="300" y="72" text-anchor="middle" font-size="10" fill="#b45309">单参数小扰动复算</text>

  <rect x="220" y="90" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="300" y="115" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">解析/自动微分</text>
  <text x="300" y="132" text-anchor="middle" font-size="10" fill="#b45309">方程或代码求导</text>

  <rect x="220" y="150" width="160" height="50" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="300" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">伴随灵敏度</text>
  <text x="300" y="192" text-anchor="middle" font-size="10" fill="#b45309">一次反向求多参数梯度</text>

  <rect x="220" y="210" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="300" y="235" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Sobol全局灵敏度</text>
  <text x="300" y="252" text-anchor="middle" font-size="10" fill="#15803d">方差分解，全局采样</text>

  <rect x="220" y="270" width="160" height="50" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="300" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">Morris筛选法</text>
  <text x="300" y="312" text-anchor="middle" font-size="10" fill="#15803d">随机轨迹初筛大量候选</text>

  <!-- 指标输出层 -->
  <rect x="440" y="100" width="160" height="70" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="520" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">输出指标</text>
  <text x="520" y="142" text-anchor="middle" font-size="10" fill="#6d28d9">波形均方误差 RMSE</text>
  <text x="520" y="156" text-anchor="middle" font-size="10" fill="#6d28d9">阻尼趋势/频率响应幅值</text>
  <text x="520" y="168" text-anchor="middle" font-size="10" fill="#6d28d9">暂态峰值/稳态功率偏差</text>

  <rect x="660" y="100" width="160" height="70" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="740" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">EMT应用场景</text>
  <text x="740" y="142" text-anchor="middle" font-size="10" fill="#6d28d9">参数筛选/模型校准</text>
  <text x="740" y="156" text-anchor="middle" font-size="10" fill="#6d28d9">模态解释/控制整定</text>
  <text x="740" y="168" text-anchor="middle" font-size="10" fill="#6d28d9">不确定性排序/代理模型</text>

  <!-- 箭头 -->
  <line x1="160" y1="60" x2="210" y2="55" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="160" y1="130" x2="210" y2="115" stroke="#333" stroke-width="1.5"/>
  <line x1="160" y1="130" x2="210" y2="175" stroke="#333" stroke-width="1.5"/>
  <line x1="160" y1="200" x2="210" y2="235" stroke="#333" stroke-width="1.5"/>
  <line x1="160" y1="200" x2="210" y2="295" stroke="#333" stroke-width="1.5"/>
  <line x1="380" y1="55" x2="430" y2="135" stroke="#333" stroke-width="1.5"/>
  <line x1="380" y1="115" x2="430" y2="135" stroke="#333" stroke-width="1.5"/>
  <line x1="380" y1="175" x2="430" y2="135" stroke="#333" stroke-width="1.5"/>
  <line x1="380" y1="235" x2="430" y2="135" stroke="#333" stroke-width="1.5"/>
  <line x1="380" y1="295" x2="430" y2="135" stroke="#333" stroke-width="1.5"/>
  <line x1="600" y1="135" x2="650" y2="135" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- 图例 -->
  <rect x="20" y="340" width="14" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="40" y="352" font-size="10" fill="#333">输入参数</text>
  <rect x="140" y="340" width="14" height="14" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="160" y="352" font-size="10" fill="#333">局部方法</text>
  <rect x="250" y="340" width="14" height="14" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="270" y="352" font-size="10" fill="#333">全局方法</text>
  <rect x="370" y="340" width="14" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="390" y="352" font-size="10" fill="#333">指标/应用</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 灵敏度分析在EMT中的四层架构：输入参数 → 局部/全局方法 → 指标量化 → 应用场景</p>

## 定义与边界

灵敏度分析研究模型输出、误差指标或稳定指标随参数变化的局部或全局响应。它可以回答"哪个参数更影响结果"和"沿哪个方向调整最可能改变指标"，但不能单独证明因果机制、参数可辨识性或控制方案有效。

本页聚焦 EMT 方法用途：参数筛选、模型校准、模态解释、控制整定和不确定性排序。与[[least-squares-method]]（可辨识性判断）、[[parameter-identification]]（参数反演流程）、[[small-perturbation-linearization]]（局部线性化模型）和[[modal-analysis]]（特征值/参与因子）紧密相关。

## EMT 中的作用

EMT 模型的参数可能包括线路频变参数、换流器控制增益、PLL 参数、机器参数、负荷参数、开关器件等效参数和初始化状态。灵敏度分析可用于：

- **参数筛选**：在黑盒 EMT 校准前，用 Sobol 全局灵敏度识别主导参数，有效降低优化维度（Wang 2024）
- **模态解释**：解释某个小信号模态为何随控制参数移动；特征值灵敏度 $\partial\lambda_i/\partial p$ 可追踪关键参数对振荡模式的影响（[[modal-analysis]]）
- **初始化误差分析**：评估稳态初始化误差对启动暂态的影响（[[steady-state-initialization]]）
- **不确定性传播**：为参数扫描、代理模型和不确定性传播提供变量排序
- **控制整定**：结合阻抗稳定性分析，用灵敏度结果指导参数重整（Xu 2025）

输出必须绑定指标，例如波形均方误差（RMSE）、阻尼趋势、频率响应幅值、暂态峰值或稳态功率偏差。

## 局部灵敏度

对指标 $y = f(\mathbf{p})$，参数 $p_i$ 的局部灵敏度定义为

$$
S_i = \frac{\partial y}{\partial p_i}.
$$

常用无量纲归一化形式为

$$
\tilde{S}_i = \frac{p_i}{y} \frac{\partial y}{\partial p_i},
$$

但当 $p_i$ 或 $y$ 接近零时，该归一化可能失去解释性。有限差分近似为

$$
\frac{\partial y}{\partial p_i} \approx \frac{f(p_i + \Delta p_i) - f(p_i - \Delta p_i)}{2 \Delta p_i}.
$$

差分步长应结合参数量纲、仿真噪声和事件时间误差选择，不能无条件套用固定比例。

**局部差分法**：单参数小扰动复算，适合快速筛查和白盒模型核对；仅代表当前运行点附近灵敏度。

**解析/自动微分法**：对模型方程或代码直接求导，适合可微模型和控制器线性化；**局限**：事件和限幅不可微。

**伴随灵敏度法**：一次反向求解多个参数梯度，适合高维参数空间、少数指标的优化场景；实现复杂且依赖模型方程。

## 模态和特征值灵敏度

对线性化矩阵 $\mathbf{A}(\mathbf{p})$，若特征值 $\lambda_i$ 简单且左右特征向量满足

$$
\mathbf{A}\mathbf{v}_i = \lambda_i \mathbf{v}_i, \quad \mathbf{w}_i^T \mathbf{A} = \lambda_i \mathbf{w}_i^T,
$$

则特征值灵敏度为

$$
\frac{\partial \lambda_i}{\partial p} = \frac{\mathbf{w}_i^T \frac{\partial \mathbf{A}}{\partial p} \mathbf{v}_i}{\mathbf{w}_i^T \mathbf{v}_i}.
$$

该公式只适用于局部线性模型和非重特征值。接近重根、非正规矩阵或强离散化影响时，特征值灵敏度可能非常不稳定，需要用扰动复算和 EMT 小扰动响应核对。

**参与因子**是特征值灵敏度的工程实现：$p_{ki} = u_{ik} w_{ki}$，把左右特征向量映射到具体状态量，用于回答"哪个状态在临界模态中占主导"（Trevisan 2020）。在 DFIG 串补系统中，定子/转子电流的参与因子总和超过 90%。

## 全局灵敏度

全局灵敏度把参数看作随机变量，评估输入不确定性对输出方差的贡献。Sobol 一阶指数的常见形式为

$$
S_i = \frac{\mathrm{Var}_{p_i}\left(\mathbb{E}_{\mathbf{p}_{-i}}[y \mid p_i]\right)}{\mathrm{Var}(y)}.
$$

总效应指数 $S_{Ti}$ 还包含 $p_i$ 与其他参数的交互贡献。全局灵敏度适合非线性黑盒 EMT，但需要明确采样范围、分布、样本规模和仿真失败处理。

**Sobol 全局灵敏度应用**（Wang 2024）：
1. 通过蒙特卡洛采样构造参数样本，计算一阶 $S_i$ 和总 $S_{Ti}$ 指数
2. 设定灵敏度阈值，筛选出指数较大的参数作为主导参数子集
3. 剔除冗余变量以降低 GMM 建模和 IPSO 优化维度
4. 仅需 4 个测试系统即可验证框架通用性

**Morris 筛选法**：随机轨迹初筛大量候选参数，适合参数候选极多时的快速初筛；结果较粗糙，需要复核。

## 特征值灵敏度与模态边界

Floquet 参与因子把灵敏度分析扩展到周期时变 EMT 系统（Sajjadi 2026）：

1. 将 EMT 模型在周期稳态轨迹附近线性化为线性时周期（LTP）系统：$\dot{\mathbf{x}}(t) = \mathbf{A}(t)\mathbf{x}(t)$
2. 计算单周期状态转移矩阵（单值矩阵）：$\mathbf{\Phi}(T) = \mathcal{T}\exp\left(\int_0^T \mathbf{A}(\tau)d\tau\right)$
3. 求 Floquet 乘子 $\mu_i$ 与左右特征向量，计算参与因子 $P_{ki}^{(h)}$
4. 谐波筛选准则剔除 >85% 冗余状态变量，同时保证目标 SSO 特征值误差 < 0.01（实部）

**临界短路比（CSCR）灵敏度**（Jiang 2025）：
- 通过 dq0 动态频率扫描，提取变流器端口阻抗 $Z_{\text{MMC}}(f)$
- 构建闭环传递函数 $Z_{\text{MMC}} Y_{\text{ac}}$，计算特征值伯德图
- 在特征值相位 $-180°$ 处，反推系统临界短路比：$\text{CSCR} = 2.5 / |Z_{\text{MMC}} Y_{\text{ac}}|$
- 电压源型 VSG 的 CSCR 约为 3.7，失稳振荡频率约为 1.15 Hz

## 阻抗稳定性中的灵敏度分析

在多端级联混合 HVDC 中，灵敏度分析用于指导阻抗重塑（Xu 2025）：

- 建立 LCC/MMC 及交直流网络的 MIMO 阻抗模型
- 计算各换流器端口阻抗对目标振荡模态的灵敏度
- 量化串补度升高时临界模态的阻尼迁移方向
- 在 DFIG 串补系统中，串补度升至约 10% 时出现临界失稳，振荡频率约 52 Hz；降低 RSC 电流控制 PI 增益可把临界模态移回稳定区域

## 工作流

1. **选定指标**：先定义输出、误差函数或稳定指标（如 RMSE、阻尼比、CSCR）
2. **确定参数空间**：列出范围、单位、相关性和不可调参数
3. **选择方法**：局部导数、有限差分、伴随法、Sobol、Morris 或采样回归
4. **运行仿真**：记录失败样本、事件触发和随机种子
5. **排序解释**：区分一阶贡献、交互贡献和数值噪声
6. **验证用途**：用筛选后的参数做独立校准、复算或控制整定检查

## EMT 建模方法汇总

| 方法 | 核心机制 | EMT 适用场景 | 精度/局限 |
|------|---------|-------------|-----------|
| 局部差分 | 单参数小扰动复算 | 快速筛查、白盒核对 | 仅当前运行点附近有效 |
| 解析/自动微分 | 对方程或代码求导 | 可微控制器线性化 | 事件/限幅不可微 |
| 伴随灵敏度 | 一次反向求多参数梯度 | 高维参数、少数指标 | 实现复杂，依赖模型方程 |
| Sobol 全局灵敏度 | 方差分解，蒙特卡洛采样 | 黑盒 EMT 参数筛选 | 采样成本高，依赖参数分布 |
| Morris 筛选 | 随机轨迹初筛 | 大量候选参数初筛 | 结果较粗，需复核 |
| Floquet 参与因子 | LTP 系统周期模态分析 | SSO/IBR 模态边界划分 | 仅周期稳态附近有效 |
| 阻抗灵敏度 | 端口阻抗对参数求导 | HVDC/VSG 稳定性分析 | 依赖频域阻抗模型精度 |

## 量化性能边界

| 方法 | 典型采样规模 | 计算成本 | 适用参数维度 |
|------|------------|---------|------------|
| 局部差分 | $O(2n)$ | 低 | 任意维度 |
| 伴随灵敏度 | $O(n + m)$ | 中 | 高维参数 |
| Sobol 全局 | $O(n \times 10^4)$ | 高 | 低中维（<20） |
| Morris 筛选 | $O(n \times r)$ | 中 | 高维（>100） |
| Floquet PF | 单周期数据 | 极低 | 任意维度（需线性化） |

**Sobol 方法降维效果**（Wang 2024）：从候选参数中识别 3-5 个主导参数，优化维度降低 60-80%，GMM + IPSO 校准误差收敛至 <5%。

**Floquet 边界划分效果**（Sajjadi 2026）：单周期（1/60 s）数据即可完成模态提取，时间窗口较传统长时仿真缩短 99% 以上；剔除 >85% 冗余状态变量，目标 SSO 特征值实部误差 <0.01、虚部误差 <0.5 rad/s。

**dq0 频率扫描精度**（Jiang 2025）：电压源型 VSG 临界短路比预测值 CSCR = 3.7，振荡频率 1.15 Hz；与根轨迹分析（3.7-3.8）和 EMT 时域仿真高度一致。

**DFIG 串补参数灵敏度**（Trevisan 2020）：串补度约 10% 时临界失稳；振荡频率约 52 Hz；定子/转子电流（dq 轴）对临界模态总参与度超过 90%（Is_d: 0.2383, Is_q: 0.2014, Ir_d: 0.2087, Ir_q: 0.1766）。

## 适用边界与失败模式

- 灵敏度高不代表参数可被测量唯一识别；多个参数可能产生相似波形（参数可辨识性独立于灵敏度）
- 灵敏度低可能只是当前工况不激励该动态，不代表参数永远不重要
- 大扰动、保护切换、饱和和拓扑变化会让局部导数失去连续性
- 全局灵敏度结论依赖参数范围和分布；换范围后排序可能改变
- 把单篇校准算例的主导参数排序外推到所有 EMT 模型是不合规的强断言
- Sobol 采样在参数维度 >20 时计算代价急剧增加，需要结合 Morris 筛选做两阶段降维
- Floquet 方法仅在周期稳态附近有效；故障穿越、换相失败等强非线性场景需要回到时域仿真
- 阻抗灵敏度分析依赖小扰动线性化假设；多振荡源同时激励时，线性叠加假设可能失效

## 与相关页面的关系

- [[least-squares-method]]：最小二乘法用于判断拟合参数是否可辨识；灵敏度矩阵 $\mathbf{J}^T\mathbf{J}$ 的条件数是可辨识性的直接指标
- [[parameter-identification]]：把灵敏度排序用于参数反演流程；Sobol 筛主导参数 → GMM 建联合分布 → IPSO 误差优化
- [[modal-analysis]]：使用参与因子和留数解释模态参与；特征值灵敏度 $\partial\lambda_i/\partial p$ 量化参数对振荡模态的影响
- [[small-perturbation-linearization]]：提供局部灵敏度和特征值灵敏度的线性模型基础
- [[steady-state-initialization]]：可分析初值误差对启动暂态的影响；初始化灵敏度是 EMT 准确性的前导指标
- [[frequency-scan]]：提供频域响应对参数变化的观测方式；dq0 扫描是阻抗灵敏度的工程实现
- [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]]：用 Floquet 参与因子划定 EMT 详细建模区域边界，兼顾计算效率与动态保真度
- [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]]：自动化 dq0 频率扫描工具，提取变流器阻抗并计算 CSCR 临界值
- [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy]]：多端 HVDC 阻抗稳定性分层分析框架，结合灵敏度分析指导阻抗重塑或参数重整

## 来源论文

| 论文 | 年份 | 贡献 |
|------|------|------|
| [[a-parallel-multi-modal-optimization-algorithm-for-simulation-based-design-of-pow]] | 2015 | 并行多模态优化 + 三次样条代理模型；Sobol 筛参数后代理模型加速极值搜索；10.8× 并行加速比 |
| [[analysis-of-low-frequency-interactions-of-dfig-wind-turbine-systems-in-series-co]] | 2020 | DFIG 串补低频相互作用；参与因子定位 SSO 主导状态；RSC PI 增益调节可抑制 52 Hz 振荡 |
| [[data-driven-parameter-calibration-of-power-system-emt-model-based-on-sobol-sensi]] | 2024 | Sobol 全局灵敏度 + GMM 参数校准框架；4 系统泛化验证；降低优化维度 60-80% |
| [[impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy]] | 2025 | 多端 HVDC MIMO 阻抗建模 + 灵敏度指导阻抗重塑；5 换流器系统；等效 SISO 振荡传播路径 |
| [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] | 2026 | Floquet 参与因子自动划分 EMT 边界；单周期提取 99%+ 时间缩减；85%+ 冗余状态剔除 |
| [[an-emt-based-dynamic-frequency-scanning-tool-for-stability-analysis-of-inverter-]] | 2025 | dq0 动态频率扫描工具；CSCR ≈ 3.7 预测；电压源型 VSG 失稳频率 1.15 Hz |