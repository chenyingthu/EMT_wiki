---
title: "磁饱和建模 (Magnetic Saturation Modeling)"
type: method
tags: [magnetic-saturation, transformer, nonlinear, iron-core, saturation]
created: "2026-05-02"
---

# 磁饱和建模 (Magnetic Saturation Modeling)


```mermaid
graph TD
    subgraph Ncmp[磁饱和建模 (Magnetic Saturation M…]
        N0[分段线性磁化曲线: 分段点、增量电感、初始磁链]
        N1[解析饱和函数: Frohlich、tanh、指数或多项式参数]
        N2[磁滞模型: 历史反转点、Preisach 或 J-A 参数]
        N3[磁等效电路: 铁芯磁阻、MMF 源、漏磁路径]
        N4[对偶电路模型: 磁路拓扑到电路拓扑映射]
    end
```


## 定义与边界

磁饱和建模是在 EMT 中描述铁磁元件磁链、磁通密度、励磁电流和磁滞历史之间非线性关系的方法。它的输入通常包括磁化曲线、剩磁或初始磁链、铁芯几何、绕组连接、漏磁路径、损耗参数和数值积分设置；输出是可接入电路网络的非线性电感、励磁支路、磁等效电路或变压器拓扑模型。

本页关注磁饱和作为方法如何进入 EMT，不替代 [[transformer-model]]、[[multi-winding-transformer]] 或 [[ferroresonance]] 的设备/现象页。它也不覆盖完整三维有限元建模；若研究局部漏磁、绕组热点或结构件涡流，应把 EMT 模型与有限元或测量证据分开说明。

## EMT 中的作用

磁饱和会影响励磁涌流、铁磁谐振、地磁感应电流、变压器投切过电压、二次谐波制动、直流偏磁和铁芯电抗器暂态。EMT 需要在每个时间步把非线性磁化支路转换为节点方程可求解的等效导纳和历史项，或通过迭代直接求解非线性方程。

该方法的关键不是只给一条 $B-H$ 曲线，而是说明该曲线放在什么磁路拓扑位置、使用什么状态变量、如何初始化剩磁、如何处理段间切换和如何验证波形。错误的励磁支路位置可能产生看似数值问题的物理拓扑错误；相关边界可与 [[duality-based-transformer-modeling-for-low-frequency-transients]] 的变压器对偶建模证据互相参照。

## 核心机制

EMT 中常用磁链-电流关系表示饱和：

$$\lambda=f(i_m), \quad v=\frac{d\lambda}{dt}$$

其中 $\lambda$ 是励磁支路磁链，$i_m$ 是磁化电流，$v$ 是对应绕组或支路电压。若采用磁通密度和磁场强度，则材料层面写为：

$$B=f(H)$$

但 EMT 电路求解通常需要把它转换为端口电压、电流和磁链关系。分段线性模型在当前工作点使用增量电感 $L_k=d\lambda/di$；解析模型可用 Frohlich、双曲正切、指数或多项式形式拟合磁化曲线；磁滞模型则还需历史变量，例如反转点栈或 Preisach/Jiles-Atherton 状态。

梯形积分下，非线性电感常被写成伴随形式：

$$i_{n+1}=G_{\mathrm{eq}}(\lambda,i)\,v_{n+1}+I_{\mathrm{hist}}$$

其中 $G_{\mathrm{eq}}$ 和历史项随工作点更新。若工作点跨越膝点或分段边界，应通过插值、子步长或牛顿迭代避免人工跳变。

## 分类与变体

| 模型路线 | 状态/参数 | 优点 | 边界 |
|----------|-----------|------|------|
| 分段线性磁化曲线 | 分段点、增量电感、初始磁链 | EMT 实现直接，便于实时仿真 | 膝点附近可能产生切换误差 |
| 解析饱和函数 | Frohlich、tanh、指数或多项式参数 | 连续可微，便于牛顿迭代 | 参数物理含义可能较弱 |
| 磁滞模型 | 历史反转点、Preisach 或 J-A 参数 | 可描述主回线和小回线 | 参数辨识和实时实现更复杂 |
| 磁等效电路 | 铁芯磁阻、MMF 源、漏磁路径 | 能保留铁芯拓扑和多绕组耦合 | 需要几何和磁路信息 |
| 对偶电路模型 | 磁路拓扑到电路拓扑映射 | 有助于放置励磁支路和漏磁支路 | 低频拓扑原则不等同于高频绕组模型 |

## 适用边界与失败模式

- 磁化曲线来源不明时，不应声明涌流、谐波或铁磁谐振结果具有定量精度。
- 忽略剩磁会显著改变投切涌流和铁磁谐振起始条件；初始磁链应作为工况输入报告。
- 把励磁支路随意放在端口等值中心可能得到正确短路阻抗但错误内部磁通路径。
- 只用单值磁化曲线不能描述磁滞小回线、剩磁路径和频率相关铁损。
- 饱和支路与梯形积分、开关切换和保护逻辑耦合时可能出现数值振荡；应区分数值离散问题和物理拓扑问题。
- 单个变压器、Sen transformer 或电抗器算例只能支撑对应结构和参数，不能外推为所有铁芯设备。

## 代表性来源

| 来源 | 可支撑的内容 | 使用边界 |
|------|--------------|----------|
| [[saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror]] | 基于 Jiles-Atherton 的饱和电抗器/铁磁谐振建模入口 | 参数和验证结论需绑定原文装置 |
| [[determination-of-the-saturation-curve-of-power-transformers-by-processing-transi]] | 从暂态波形处理获得变压器饱和曲线的来源入口 | 曲线适用性取决于测量和处理条件 |
| [[duality-based-transformer-modeling-for-low-frequency-transients]] | 对偶变压器模型、励磁支路位置和漏磁拓扑原则 | 主要支撑低频暂态拓扑，不等同于高频绕组模型 |
| [[nonlinear-magnetic-equivalent-circuit-based-real-time-sen-transformer-electromag]] | 非线性磁等效电路、磁滞和实时 FPGA 实现案例 | 限定在 Sen transformer、平台和原文验证工况 |
| [[including-magnetic-saturation-in-voltage-behind-reactance-induction-machine-mode]] | 感应机 VBR 模型中加入磁饱和的代表入口 | 不应外推到所有旋转机器和控制场景 |
| [[modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el]] | 同步机交叉磁化和饱和效应建模入口 | 需核查原文机器参数和 EMT 实现 |

## 与相关页面的关系

- [[transformer-model]] 和 [[multi-winding-transformer]] 是磁饱和最常见的设备承载页；本页说明非线性支路和磁路方法。
- [[ferroresonance]] 是饱和电感与电容网络相互作用的现象页，依赖本页的非线性建模边界。
- [[steady-state-initialization]] 决定剩磁、初始磁链和故障前状态是否一致。
- [[companion-circuit]]、[[discretization-methods]] 和 [[numerical-integration-methods]] 说明非线性电感如何进入 EMT 步进求解。
- [[harmonic-analysis-methods]] 可用于分析饱和导致的波形畸变，但谐波结果必须绑定窗口和工况。
- [[frequency-dependent-modeling]] 与 [[wideband-modeling]] 处理频率相关端口模型；磁饱和模型处理非线性磁化，两者不能互相替代。
