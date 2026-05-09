---
title: "摇摆方程 (Swing Equation)"
type: method
tags: [swing-equation, rotor-dynamics, transient-stability, synchronous-machine, equal-area]
created: "2026-05-02"
---

# 摇摆方程 (Swing Equation)


```mermaid
graph LR
    N0[定义与边界]
    N1[基本形式]
    N0 -->|Nf1| N1
    N2[电磁功率接口]
    N1 -->|Nf2| N2
    N3[分析用途]
    N2 -->|Nf3| N3
    N4[数值求解]
    N3 -->|Nf4| N4
    N5[适用边界与失败模式]
    N4 -->|Nf5| N5
```


## 定义与边界

摇摆方程（Swing Equation）描述同步机转子机械运动与电磁功率不平衡之间的关系，是机电暂态和转子角稳定分析中的基础方程。它关注转子功角和转速在扰动后的变化，主要对应机电时间尺度。

摇摆方程不是 EMT 网络求解方法。EMT 仿真可以包含同步机机械方程，但 EMT 的核心仍是三相瞬时电路、设备模型和数值积分。若研究对象是定子电磁暂态、绕组耦合、不平衡故障或开关暂态，摇摆方程必须与更详细的 [[synchronous-machine-model]] 和网络方程共同使用。

## 基本形式

转子机械运动可由转矩不平衡表示：

$$
J\frac{d^2\theta_m}{dt^2}=T_m-T_e-T_D
$$

在标幺功率和同步参考坐标下，常见形式为：

$$
\frac{2H}{\omega_0}\frac{d^2\delta}{dt^2}=P_m-P_e-D\frac{d\delta}{dt}
$$

其中 $H$ 为惯性常数，$\omega_0$ 为同步角速度，$\delta$ 为功角，$P_m$ 为机械输入功率，$P_e$ 为电磁输出功率，$D$ 为等效阻尼系数。

状态空间形式可写为：

$$
\dot{\delta}=\Delta\omega
$$

$$
\dot{\Delta\omega}=\frac{\omega_0}{2H}(P_m-P_e-D\Delta\omega)
$$

不同教材和软件可能采用不同符号、基准值和转速变量定义，比较模型时应先统一标幺基准和角速度定义。

## 电磁功率接口

在单机无穷大系统和经典模型中，电磁功率常近似为：

$$
P_e=\frac{EV}{X}\sin\delta
$$

该表达依赖简化网络、恒定内电势和正序相量假设。多机系统、详细同步机模型或 EMT 仿真中，$P_e$ 通常由网络方程、定子电流、磁链和控制系统共同决定，而不是固定的正弦函数。

因此，摇摆方程的关键接口是 $P_e$ 的来源：如果 $P_e$ 来自稳态相量网络，模型属于机电暂态近似；如果 $P_e$ 来自瞬时三相 EMT 模型，则摇摆方程只是同步机完整动态模型中的机械子方程。

## 分析用途

摇摆方程常用于：

- [[transient-stability-analysis]] 中的大扰动功角稳定评估；
- 小扰动线性化和阻尼分析；
- 单机无穷大系统的等面积法解释；
- 多机系统转子角相对运动和中心惯性坐标分析；
- EMT 或混合仿真中同步机机械子系统建模。

## 数值求解

摇摆方程可用常微分方程积分方法求解，例如显式积分、隐式积分或与网络代数方程联立的时域积分。方法选择取决于：

- 是否与电磁网络方程强耦合；
- 步长相对于机电振荡和电磁暂态的尺度；
- 阻尼、限幅、保护和控制器事件是否显式建模；
- 是否要求与 EMT 主求解器同步。

本页不给出无来源的固定步长建议。机电暂态步长和 EMT 步长通常处于不同数量级，混合仿真需要通过接口和多速率策略处理。

## 适用边界与失败模式

- 经典摇摆方程忽略定子暂态和详细绕组动态，不能单独分析电磁暂态波形。
- 单机等面积法依赖强简化假设，不应直接推广到复杂多机系统。
- 阻尼系数 $D$ 往往是等效参数，其来源可能包括阻尼绕组、负荷频率特性、调速器和励磁控制。
- 大扰动下的限幅、饱和和保护动作会改变线性化阻尼解释。

## 代表性来源

- [[evaluation-of-time-domain-and-phasor-domain-methods-for-power-system-transients]]：适合支撑“机电/相量域与 EMT 时间尺度不同”的边界说明。
- [[saturation-in-transient-and-stability-phenomena-for-cylindrical-13&14]]：可用于说明同步机机械方程与电磁饱和、励磁和稳定现象耦合，不能只看经典正弦功角公式。
- [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t]]：说明摇摆方程所在机电暂态模型可与 EMT 子系统耦合，但接口和分网边界需要单独验证。

## 与相关页面的关系

- [[synchronous-machine-model]] 给出同步机电磁和机械模型的完整上下文。
- [[excitation-system]] 通过改变电磁功率影响摇摆方程。
- [[power-system-stabilizer]] 通过励磁通道改善目标机电模态阻尼。
- [[transient-stability-analysis]] 以摇摆方程为核心工具之一。
- [[electromechanical-transient]] 说明摇摆方程所在的时间尺度。
- [[emt-simulation]] 说明瞬时值仿真的更宽建模范围。

## 证据边界

本页给出摇摆方程的通用定义、接口和适用边界。具体惯性常数、阻尼参数、临界切除时间、稳定裕度或算例结论必须绑定设备数据、系统模型和仿真证据后才能写入。
