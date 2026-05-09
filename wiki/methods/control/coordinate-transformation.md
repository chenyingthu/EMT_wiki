---
title: "坐标变换 (Coordinate Transformation)"
type: method
tags: [transformation, park, clarke, dq, alpha-beta, reference-frame, vector-control]
created: "2026-05-02"
---

# 坐标变换 (Coordinate Transformation)


```mermaid
graph TD
    subgraph Ncmp[坐标变换 (Coordinate Transformat…]
        N0[Clarke / alpha-beta-zero: 三相…]
        N1[Park / dq0: 三相基波相量或瞬时量]
        N2[Fortescue 序分量: 基频复相量]
        N3[瞬时序分量: 采样波形或解析信号]
        N4[线路模态变换: 多导体线路变量]
    end
```


## 定义与边界

坐标变换是把同一组三相或多导体电气量从一个坐标基底映射到另一个坐标基底的方法。EMT 语境中常见对象包括三相瞬时量 $\mathbf{x}_{abc}$、静止正交坐标 $\mathbf{x}_{\alpha\beta0}$、同步旋转坐标 $\mathbf{x}_{dq0}$、复数序分量 $\mathbf{x}_{012}$，以及线路模态坐标。

本页讨论坐标变换的共同结构和使用边界，不替代专门页面：[[dq-transformation]] 负责 Park/dq0 旋转坐标，[[symmetrical-components]] 负责 Fortescue 序分量，[[sequence-network-model]] 负责序网建模，[[modal-domain-decoupling]] 负责线路传播模态。坐标变换本身不是模型精度、实时性或控制性能的保证；这些结论必须绑定具体模型、步长、控制器和验证来源。

## EMT 中的作用

EMT 仿真以瞬时电压、电流和状态变量推进。坐标变换主要承担接口和解释任务：

- 把网络侧 abc 相变量送入电机、变流器或控制器内部坐标。
- 把控制器输出从 dq 或 alpha-beta 坐标变回三相端口注入。
- 在后处理中分离正序、负序、零序、谐波或旋转分量，解释不平衡和控制耦合。
- 对线路和电缆的多导体方程做近似或严格解耦，降低传播模型的处理复杂度。

在 EMT 主网络中，端口连接通常仍以相域节点电压和支路电流闭合。若内部模型使用 dq 或序分量，需要明确每个时间步的变换角、归一化、零序处理和反变换方式，否则会把坐标约定误差带入网络求解。

## 核心机制

一般线性坐标变换可写为

$$
\mathbf{x}'=\mathbf{T}(t)\mathbf{x}, \qquad
\mathbf{x}=\mathbf{T}^{-1}(t)\mathbf{x}'.
$$

当 $\mathbf{T}$ 随时间变化，例如 Park 旋转坐标，微分方程中会出现额外速度耦合项：

$$
\frac{d\mathbf{x}'}{dt}
=\mathbf{T}\frac{d\mathbf{x}}{dt}
+\frac{d\mathbf{T}}{dt}\mathbf{x}.
$$

因此坐标变换不能只写代数矩阵，还要说明它如何作用于状态方程、历史项和离散化后的伴随电路。

### Clarke 变换

幅值不变的 abc 到 alpha-beta-zero 变换常写成

$$
\begin{bmatrix} x_\alpha \\ x_\beta \\ x_0 \end{bmatrix}
=\frac{2}{3}
\begin{bmatrix}
1 & -\frac{1}{2} & -\frac{1}{2} \\
0 & \frac{\sqrt{3}}{2} & -\frac{\sqrt{3}}{2} \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}
\begin{bmatrix} x_a \\ x_b \\ x_c \end{bmatrix}.
$$

对三相和为零的平衡量，$x_0=0$，alpha-beta 平面可表示瞬时空间矢量。若系统存在中性点、接地支路或共模分量，不能省略零序通道。

### Park 变换

Park 变换可理解为在 alpha-beta 平面上再旋转角度 $\theta$：

$$
\begin{bmatrix} x_d \\ x_q \end{bmatrix}
=
\begin{bmatrix}
\cos\theta & \sin\theta \\
-\sin\theta & \cos\theta
\end{bmatrix}
\begin{bmatrix} x_\alpha \\ x_\beta \end{bmatrix}.
$$

当 $\theta$ 跟随基波正序相角时，理想平衡正弦基波在 dq 坐标中可表现为近似常值。这个性质只对匹配的频率和序分量成立；负序、不平衡、谐波和 PLL 动态会在 dq 坐标中表现为振荡项。

### 对称分量变换

相量序分量使用复数算子 $a=e^{j120^\circ}$：

$$
\begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix}
=\frac{1}{3}
\begin{bmatrix}
1 & 1 & 1 \\
1 & a & a^2 \\
1 & a^2 & a
\end{bmatrix}
\begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix}.
$$

该变换主要用于基频相量和序网分析。若直接作用于 EMT 瞬时波形，需要说明滤波、窗口、频率跟踪或瞬时对称分量定义，不能把工频相量公式无条件当作宽频暂态分解。

## 分类与变体

| 变换 | 主要对象 | EMT 用途 | 边界 |
|---|---|---|---|
| Clarke / alpha-beta-zero | 三相瞬时量 | 空间矢量、控制输入、零序分离 | 零序和归一化不能省略 |
| Park / dq0 | 三相基波相量或瞬时量 | 电机方程、VSC 电流控制、PLL 后处理 | 依赖相角和符号约定 |
| Fortescue 序分量 | 基频复相量 | 不平衡故障、保护量、序网 | 线性和频率假设需标注 |
| 瞬时序分量 | 采样波形或解析信号 | 不平衡 EMT 后处理、动态相量接口 | 滤波和窗口会影响结果 |
| 线路模态变换 | 多导体线路变量 | 传播通道解耦、频变线路模型 | 非换位和频变耦合可能破坏常数变换 |

## 适用边界与失败模式

- 不说明幅值不变、功率不变或软件内部约定，导致功率、阻抗和控制增益解释不一致。
- 只对电压做变换，漏掉电流、功率、磁链、历史源或反变换的配套约定。
- 在不平衡或含谐波工况中，把单一同步 dq 坐标下的常值假设外推到所有分量。
- 在接地故障、三角形环流或共模电压问题中忽略零序通道。
- 用固定模态矩阵处理非换位线路、电缆和平行线路强频变耦合，而未验证误差。
- 把某个控制论文中的坐标选择写成所有 EMT 工具或所有设备模型的默认标准。

## 代表性证据

[[a-voltage-behind-reactance-synchronous-machine-model-for-the-emtp-type-solution]] 和 [[modeling-of-ac-machines-using-a-voltage-behind-reactance-formulation-for-simulat]] 可支撑“同步机 EMT 模型常在内部使用 dq/转子坐标、对外保持 abc 端口接口”的方法定位。其量化效率和步长结论只绑定原文机器、网络和算例，不能外推为所有坐标变换都更稳定。

[[dynamic-performance-of-embedded-hvdc-with-13&14]] 和 [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]] 可支撑 VSC/MMC 控制中使用 dq 坐标、PLL、内外环和延时共同影响 EMT 结果的认识。页面使用这些来源时应保留其拓扑和控制场景边界。

[[modal-domain-decoupling]] 所列线路来源说明模态变换在多导体线路中能简化传播通道，但非换位、频变和互耦场景需要额外验证。

## 与相关页面的关系

- [[dq-transformation]]：Park/dq0 坐标、参考角和控制方程边界。
- [[symmetrical-components]]：Fortescue 序分量的数学定义。
- [[sequence-component-method]]：把序分量用于不平衡交流分析的流程。
- [[sequence-network-model]]：把序分量阻抗组织成故障计算网络。
- [[phase-domain-modeling]]：说明何时直接保留 abc 相域更合适。
- [[modal-domain-decoupling]]：线路相域到模态域的专门边界页。

## 修订与证据使用注意事项

后续扩展本页时，不应新增未绑定来源的“典型步长”“提速倍数”“误差百分比”或“通用最优坐标系”。涉及公式符号时，应同时说明坐标方向、归一化和功率定义。
