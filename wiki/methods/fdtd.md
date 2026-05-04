---
title: "时域有限差分法 (FDTD)"
type: method
tags: [fdtd, finite-difference, electromagnetic, full-wave, simulation]
created: "2026-05-02"
---

# 时域有限差分法 (FDTD)

## 定义与边界

时域有限差分法（Finite-Difference Time-Domain, FDTD）是在空间网格和时间步上直接离散 Maxwell 旋度方程的全波电磁场方法。它使用交错的 Yee 网格和显式蛙跳时间推进，直接得到电磁波在时域中的传播、反射、耦合和衰减。

FDTD 与 [[finite-element-method]] 的主要区别在于：FDTD 通常在规则或分块规则网格上显式推进时域场量，适合宽带传播问题；FEM 通常从弱形式和网格单元组装矩阵，适合复杂几何、材料非线性和频域/准静态场问题。两者都可以为 EMT 提供场求解证据或等值参数，但不能替代常规电路 EMT 的系统级求解。

## EMT 中的作用

FDTD 在 EMT wiki 中主要用于场求解和高频暂态边界，而不是常规电网节点方程的默认求解器。典型用途包括：

- 雷电、电磁干扰、GIS/VFT 和接地暂态中的波传播分析，见 [[lightning-transient-analysis]] 和 [[high-frequency-transient-analysis]]。
- 验证传输线理论、接地等值或电缆模型在快速暂态中的适用范围。
- 从场解提取端口阻抗、耦合电压、电流分布或等效源，再嵌入 EMT 电路。
- 与 [[transmission-line-model]]、[[grounding-system-modeling]] 和 [[underground-cable-modeling]] 的参数边界互相校验。

## 核心方程

在均匀各向同性介质中，FDTD 离散 Maxwell 旋度方程：

$$
\nabla \times \mathbf{E} = -\mu \frac{\partial \mathbf{H}}{\partial t}
$$

$$
\nabla \times \mathbf{H} = \sigma \mathbf{E} + \varepsilon \frac{\partial \mathbf{E}}{\partial t} + \mathbf{J}
$$

Yee 网格把电场分量放在网格边上，把磁场分量放在网格面上，并在时间上交错半步。以一个电场分量为例：

$$
E_x^{n+1} = C_a E_x^n + C_b
\left(
\frac{H_z^{n+1/2}|_{y+} - H_z^{n+1/2}|_{y-}}{\Delta y}
-
\frac{H_y^{n+1/2}|_{z+} - H_y^{n+1/2}|_{z-}}{\Delta z}
\right)
-
C_j J_x^{n+1/2}
$$

其中 $C_a$、$C_b$ 和 $C_j$ 由介电常数、电导率和时间步长确定。磁场分量用相邻电场旋度类似更新。

## 工作流程

1. 定义计算域、材料参数、源和观测量。
2. 生成 Yee 网格，并在材料交界、导体边界和细小结构处检查空间分辨率。
3. 选择时间步，使其满足 CFL 稳定条件。
4. 设置边界条件，例如 PEC、PMC、吸收边界或 PML。
5. 按半步交错更新磁场和电场，并注入源项。
6. 记录端口电压电流、场量或时域波形。
7. 用网格细化、能量平衡、解析解或测量数据验证结果。

## 稳定性与色散

显式 FDTD 需要满足 Courant 条件。三维直角网格中的常见形式为：

$$
\Delta t \le
\frac{1}{c\sqrt{(\Delta x)^{-2}+(\Delta y)^{-2}+(\Delta z)^{-2}}}
$$

其中 $c$ 是介质中的波速。即使满足稳定性条件，离散网格仍会产生数值色散：不同传播方向和不同频率的数值相速度可能不同。因此，FDTD 的可信频带取决于网格尺寸、材料模型和源频谱，不能只由时间步长判断。

## 主要变体

- 一维、二维和三维 FDTD：按几何简化程度选择。
- 非均匀或局部细化网格：降低局部小结构对全域网格的成本，但需要处理网格过渡误差。
- 分散材料 FDTD：用 Debye、Drude、Lorentz 或递归卷积模型描述频变介质。
- PML/CPML 吸收边界：减少截断边界反射，但参数选择不当会产生残余反射或数值增长。
- 改进 FDTD/MFDTD：在特定传输线或有损介质问题中调整离散形式；其结论应绑定原问题。

## 适用边界与失败模式

- 复杂曲面和细小几何在阶梯网格上可能产生几何误差。
- 最小网格尺寸决定全局显式时间步，局部细节会显著增加计算量。
- PML 对低频、掠入射、强非均匀介质或不当参数可能吸收不足。
- 材料色散、土壤频变和导体集肤效应需要专门模型，不能用常数参数无条件代替。
- FDTD 输出场量转成 EMT 端口等值时，需要说明积分路径、参考方向和端口定义。

## 证据边界

FDTD 证据通常适合支撑“某一几何、材料、源谱和观测点下的场传播或耦合结果”。它不能直接证明一个集总 EMT 模型在所有频带有效，也不能把单个全波对比外推为所有线路、电缆或接地模型的通用精度。

可作为入口的来源包括 [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und]]、[[parametric-study-of-transient-electromagnetic-fields]]、[[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi]] 和 [[electromagnetic-disturbances-in-gas-insulated-substations-and-vft-calculations]]。

## 与相关页面的关系

- [[finite-element-method]]：更适合复杂几何、非线性材料和弱形式场问题。
- [[high-frequency-transient-analysis]]：FDTD 常作为高频暂态的场求解证据。
- [[lightning-transient-analysis]]：雷电波传播和耦合分析的应用入口。
- [[transmission-line-model]]：系统级 EMT 中常用的线路近似，需要用全波结果界定适用范围。
- [[grounding-system-modeling]]：接地电极和土壤频变问题可能需要场求解校验。
- [[interface-technique]]：说明场解与 EMT 电路之间如何交换端口变量。
