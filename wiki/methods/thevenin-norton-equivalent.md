---
title: "戴维南-诺顿等效 (Thevenin-Norton Equivalent)"
type: method
tags: [equivalent-circuit, thevenin, norton, port-model, network-reduction]
created: "2026-04-30"
---

# 戴维南-诺顿等效 (Thevenin-Norton Equivalent)

## 定义与边界

戴维南-诺顿等效（Thevenin-Norton Equivalent）是同一线性端口关系的两种表示：戴维南形式使用电压源串联阻抗，诺顿形式使用电流源并联导纳。对 EMT 来说，这组方法的价值不在于电路定理本身，而在于把网络、设备子系统或离散动态元件统一成“端口源 + 端口阻抗/导纳”的可求解接口。

本页关注两种端口形式的转换、EMT 离散实现和失败边界。更具体的单页见 [[thevenin-equivalent]] 与 [[norton-equivalent]]；更宽泛的端口等效见 [[equivalent-circuit-method]]。

## EMT 中的作用

戴维南-诺顿等效在 EMT 中常用于：

- 把电感、电容和状态空间子系统离散为当前导纳或阻抗加历史源。
- 把外部网络、交流区域或设备集群压缩成端口模型。
- 在多速率、分区和实时仿真中交换边界电压、电流和历史项。
- 对非线性端口使用补偿法，把线性网络部分预先等效为端口源和阻抗。
- 对 MMC 子模块、变压器端口和频变网络等值进行矩阵降维。

节点导纳方程通常偏向诺顿形式；电压边界、补偿法和接口解释常使用戴维南形式。两者应由同一个端口定义和同一组模型状态转换而来。

## 核心机制

### 单端口转换

若端口电流 $i$ 按流出戴维南电压源方向定义，可写成：

$$
v=V_{\mathrm{th}}-Z_{\mathrm{th}}i
$$

当 $Z_{\mathrm{th}}\neq 0$ 时，等价诺顿形式为：

$$
i=I_{\mathrm{N}}-Y_{\mathrm{N}}v
$$

其中：

$$
Y_{\mathrm{N}}=Z_{\mathrm{th}}^{-1},\quad I_{\mathrm{N}}=Y_{\mathrm{N}}V_{\mathrm{th}}
$$

如果采用“注入节点为正”的电流方向，右端符号会改变。文档和程序必须显式固定方向约定。

### 多端口转换

多端口戴维南形式为：

$$
\mathbf{v}=\mathbf{V}_{\mathrm{th}}-\mathbf{Z}_{\mathrm{th}}\mathbf{i}
$$

若 $\mathbf{Z}_{\mathrm{th}}$ 可逆，则诺顿形式为：

$$
\mathbf{i}=\mathbf{I}_{\mathrm{N}}-\mathbf{Y}_{\mathrm{N}}\mathbf{v}
$$

$$
\mathbf{Y}_{\mathrm{N}}=\mathbf{Z}_{\mathrm{th}}^{-1},\quad
\mathbf{I}_{\mathrm{N}}=\mathbf{Y}_{\mathrm{N}}\mathbf{V}_{\mathrm{th}}
$$

矩阵的非对角项代表端口耦合。把多端口模型拆成多个单端口必须有耦合可忽略的证据。

### EMT 离散时域形式

对动态元件或状态空间集群，积分离散后常得到：

$$
\mathbf{i}_{n+1}
=\mathbf{G}_{\mathrm{eq}}\mathbf{v}_{n+1}
+\mathbf{i}_{hist}^{n}
$$

这是诺顿伴随形式。若 $\mathbf{G}_{\mathrm{eq}}$ 可逆，也可写成戴维南伴随形式：

$$
\mathbf{v}_{n+1}
=\mathbf{R}_{\mathrm{eq}}\mathbf{i}_{n+1}
+\mathbf{v}_{hist}^{n}
$$

其中 $\mathbf{R}_{\mathrm{eq}}=\mathbf{G}_{\mathrm{eq}}^{-1}$。在实现上，诺顿形式通常直接装配到 [[nodal-admittance-matrix]]；戴维南形式可能需要增广节点分析、源变换或接口方程。

## 变体

| 变体 | 戴维南形式 | 诺顿形式 | 适合用途 |
|------|------------|----------|----------|
| 静态线性端口 | 开路电压 + 输入阻抗 | 短路电流 + 输入导纳 | 工频网络等值、短路计算 |
| 伴随支路 | 历史电压源 + 等效电阻 | 历史电流源 + 等效电导 | EMT 时间步求解 |
| 多端口网络 | 电压源向量 + 阻抗矩阵 | 电流源向量 + 导纳矩阵 | 分区、外部网络、FDNE |
| 线性化非线性端口 | 增量电压源 + 增量阻抗 | 增量电流源 + 增量导纳 | Newton 或分段线性迭代 |
| 频变等效 | $Z(s)$ 状态/卷积 | $Y(s)$ 状态/卷积 | 宽频网络等值 |

## 适用边界与失败模式

常见问题包括：

- 端口方向不一致，导致源变换后符号错误。
- $\mathbf{Z}_{\mathrm{th}}$ 或 $\mathbf{Y}_{\mathrm{N}}$ 奇异、病态或频率点不一致，却强行互换。
- 用固定线性等效表示含限幅、饱和、保护动作或开关逻辑的设备。
- 只保留多端口自阻抗或自导纳，删除互耦项。
- 历史源没有在开关或拓扑变化后重初始化，产生非物理暂态。
- 把某个算例中的加速或误差结果外推为方法的普遍性能。

## 代表性证据

[[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 支撑“状态空间集群经梯形积分后可形成 V 型、I 型或混合型端口等效，并映射到全局节点导纳矩阵”的机制。该来源适合作为戴维南/诺顿互换在 SSN 求解框架中的证据，但页面中具体实时和误差数字需要回原文核验。

[[high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us]] 支撑多端口诺顿等效与 Schur 补节点消去在 MMC 桥臂降维中的作用。该来源明确说明了外部端口等效与内部状态回代的机制；摘要中的加速声称应限定为原文报告，不应补写未核验的运行平台或误差数字。

[[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi]] 支撑多区域戴维南等效在多速率 LCC-HVDC 协同仿真接口中的用法。其结论应绑定实际系统、步长比和故障工况。

[[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga]] 支撑补偿法中线性网络对非线性端口形成多端口戴维南等效，并与非线性函数迭代联立的机制。

## 与相关页面的关系

- [[thevenin-equivalent]]：强调电压源串联阻抗和开路电压解释。
- [[norton-equivalent]]：强调电流源并联导纳和节点矩阵装配。
- [[companion-circuit]]：电感、电容等动态元件在每个时间步形成戴维南或诺顿伴随支路。
- [[fixed-admittance]]：特殊目标是保持导纳矩阵不随开关状态变化，不等同于一般诺顿等效。
- [[network-equivalent]]：系统级等值主题，包含静态、动态和频变端口等效。
- [[co-simulation]]：跨子系统边界常使用戴维南/诺顿接口。

## 开放问题

- 多端口等效的互耦保留、矩阵条件数和无源性检查仍是宽频 EMT 接口的关键问题。
- 对含控制器和保护动作的设备，需要事件状态、运行点和线性化策略共同定义端口等效。
- 不同仿真器对电流方向、历史源和源变换的约定不完全一致，页面和代码应显式记录。

## 来源论文

参见 [[index]] 获取更多戴维南-诺顿等效相关文献。
