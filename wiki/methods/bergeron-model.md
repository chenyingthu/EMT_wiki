---
title: "Bergeron 线路模型 (Bergeron Line Model)"
type: method
tags: [transmission-line, bergeron, traveling-wave, lossless-line, companion-circuit, emt]
created: "2026-05-02"
---

# Bergeron 线路模型 (Bergeron Line Model)

## 定义与边界

本页把 Bergeron 模型作为一种“线路端口等效结构”来说明：它把一段均匀传输线写成端口特性导纳、传播延时和历史电流源的组合，供 EMT 网络方程在每个时间步调用。更完整的常参数行波线路页已经由 [[bergeron-line-model]] 保护；本页只补充其模型接口、符号约定和扩展边界，避免重复讲完整线路模型史。

Bergeron 模型不是宽频线路模型的同义词。若研究对象需要导体集肤效应、大地返回阻抗、频变土壤、非换位强耦合或电缆护套耦合，应转向 [[frequency-dependent-line-model]]、[[universal-line-model]]、[[earth-return-impedance]] 和 [[frequency-dependent-soil]]。

## EMT 中的作用

在 EMT 程序中，Bergeron 模型的主要作用是把分布参数传播关系变成可并入节点导纳方程的 Norton 端口。它解决的是“线路两端不能瞬时相互作用”的问题，而不是替代所有线路参数计算。

典型输入包括线路长度 $\ell$、单位长度电感 $L$、单位长度电容 $C$、端口电压电流方向约定、时间步长 $\Delta t$ 和延时历史队列。典型输出是当前步节点导纳贡献 $Y_c$ 与历史电流源 $I_h(t)$。对多相线路，输入还包括相域参数矩阵或模态变换矩阵。

## 核心机制

无损单相均匀线满足：

$$-\frac{\partial v}{\partial x}=L\frac{\partial i}{\partial t},\quad
-\frac{\partial i}{\partial x}=C\frac{\partial v}{\partial t}$$

令传播速度 $u=1/\sqrt{LC}$，特性阻抗 $Z_c=\sqrt{L/C}$，线路延时 $\tau=\ell/u$。若端口电流均按流入线路为正，端口 $k$ 的 Norton 形式可写成：

$$i_k(t)=Y_c v_k(t)+I_{h,k}(t),\quad Y_c=\frac{1}{Z_c}$$

$$I_{h,k}(t)=-Y_c v_m(t-\tau)-i_m(t-\tau)$$

端口 $m$ 对称成立。这里的历史源不是新的物理电源，而是远端延时电压、电流沿特征线传播到本端后的等效表达。实现时必须先统一端口电流正方向，否则同一公式会出现符号差异。

## 模型变体

| 变体 | 机制 | 可支撑的问题 | 主要边界 |
|------|------|--------------|----------|
| 常参数 Bergeron | 固定 $Z_c$ 与 $\tau$，历史源延时更新 | 架空线常参数行波、接口解耦、教学模型 | 不能表达频变衰减 |
| 集中损耗扩展 | 在线路端部或分段中加入集中电阻/电导 | 低损耗线路的近似损耗 | 高频损耗分布不可靠 |
| 级联 Bergeron | 多个短段串联，每段保留历史源 | 把局部损耗或状态模块嵌入线路段 | 段数、步长和拟合需验证 |
| 频变 Bergeron 扩展 | 将频变纵向参数拟合为状态空间或有理函数 | 宽频纵向损耗与时域非线性网络耦合 | 需要拟合、稳定性和无源性检查 |

## 数值实现要点

若 $\tau$ 不是 $\Delta t$ 的整数倍，历史量通常需要插值。设 $\tau=q\Delta t+\delta\Delta t$，$0\leq\delta<1$，可用线性插值近似：

$$x(t-\tau)\approx (1-\delta)x(t-q\Delta t)+\delta x(t-(q+1)\Delta t)$$

插值阶次会影响高频相位与幅值。可变步长或多速率仿真还需要明确历史队列重采样策略；这也是 [[transmission-line-model-for-variable-step-size-simulation-algorithms]] 等来源适合支撑的边界。

对多相线路，常见路线是先用 [[modal-transformation]] 或 [[modal-domain-decoupling]] 把相域耦合近似转为若干模态通道，再对每个模态使用 Bergeron 端口形式。若变换矩阵随频率变化明显，固定模态 Bergeron 表示可能不足。

## 适用边界与失败模式

- 不应写成“无条件适用于所有线路暂态”。频变损耗、地模、护套和土壤参数会改变传播函数。
- 不应加入未绑定来源的典型线路长度、波速、阻抗范围或误差百分比。
- 短线路或小步长接口中，延时可能小于或接近时间步，需检查数值接口是否退化为强耦合问题。
- 频变扩展若使用有理函数，应检查稳定极点、低频极限、拟合误差和 [[passivity-enforcement]]。
- 多导体线路中，互耦是否可由常数模态矩阵充分解耦，需要结合线路几何和频带验证。

## 代表性证据

- [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp]]：支撑“频变纵向参数可嵌入 Bergeron 线路段并级联”的方法方向；该 source 的 deep-review 同时提醒不要直接引用未核验的误差、频带和速度数字。
- [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-]]：支撑“特征线/历史源模型的瓶颈可来自状态方程组织和历史源访问”的实现层证据，结论主要限于作者架空线算例。
- [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method]] 与 [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model]] 可作为频变多导体 Bergeron 扩展的入口。
- [[耦合长线电磁暂态分析的扩展bergeron模型]] 可支撑多相耦合线路中扩展 Bergeron 表示的历史来源，但不应外推为所有耦合线路的统一精度保证。

## 与相关页面的关系

- [[bergeron-line-model]]：保护页，给出常参数线路模型的主说明。
- [[characteristic-method]]：说明特征线法本身，本页只讨论其线路端口模型化结果。
- [[distributed-parameter-line]]：给出电报方程和分布参数线路总框架。
- [[universal-line-model]]：处理相域频变线路，与常参数 Bergeron 边界不同。
- [[folded-line-equivalent]]：另一路线路导纳组织方式，可用于短线路和频变实现比较。

## 修订与证据使用注意事项

后续补充本页时，应把“模型结构说明”和“论文算例结果”分开。凡涉及误差、速度、频带、段数、步长、软件模块或工程参数，必须绑定具体来源、算例、指标和对比基线。
