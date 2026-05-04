---
title: "有限元法 (Finite Element Method, FEM)"
type: method
tags: [finite-element, fem, electromagnetic, field, numerical]
created: "2026-05-02"
---

# 有限元法 (Finite Element Method, FEM)

## 定义与边界

有限元法（Finite Element Method, FEM）把连续场问题划分为有限个单元，在每个单元上用形函数近似未知量，并通过弱形式组装代数方程。电磁 FEM 可用于静电、静磁、涡流、频域波动和时域场问题。

FEM 与 [[fdtd]] 都是电磁场数值方法，但侧重点不同。FEM 擅长复杂几何、非结构网格、材料非线性、各向异性和边界条件精细处理；FDTD 擅长规则网格上的显式宽带时域传播。对 EMT 来说，FEM 通常提供设备参数、场路耦合模型或验证基准，而不是替代整个电网 EMT 求解器。

## EMT 中的作用

FEM 在 EMT 知识体系中的主要角色包括：

- 提取变压器、电机、电抗器、电缆、接地电极和母线结构的等值参数。
- 计算饱和、涡流、集肤效应、邻近效应和局部电磁力。
- 生成可嵌入 EMT 的查表模型、状态空间模型、等效阻抗或受控源。
- 为 [[grounding-system-modeling]]、[[underground-cable-modeling]]、[[synchronous-machine-model]] 和 [[transmission-line-model]] 提供场级证据边界。

## 核心弱形式

以标量二阶问题为例：

$$
-\nabla \cdot (k\nabla u) + qu = f
$$

乘以测试函数 $v$ 并分部积分，得到弱形式：

$$
\int_{\Omega} k\nabla u \cdot \nabla v\,d\Omega
+ \int_{\Omega} quv\,d\Omega
=
\int_{\Omega} fv\,d\Omega
+ \int_{\Gamma_N} gv\,d\Gamma
$$

令近似解为：

$$
u_h = \sum_{j=1}^{N} u_j \phi_j
$$

取测试函数为形函数 $\phi_i$，组装线性系统：

$$
K u = f
$$

在电磁场中，未知量可为电位 $\varphi$、磁矢势 $\mathbf{A}$、磁标势或电场分量。涡流问题常见形式为：

$$
\nabla \times (\nu \nabla \times \mathbf{A})
+ \sigma \frac{\partial \mathbf{A}}{\partial t}
= \mathbf{J}_s
$$

其中 $\nu$ 是磁阻率，$\sigma$ 是电导率，$\mathbf{J}_s$ 是源电流密度。

## 工作流程

1. 建立几何、材料、边界条件和激励。
2. 选择物理方程：静电、静磁、涡流、频域或时域全波。
3. 生成网格，并在气隙、尖端、导体边缘、集肤深度和材料界面处细化。
4. 选择形函数阶数、单元类型和时间/频率离散方式。
5. 组装矩阵并求解线性或非线性方程；非线性磁化曲线通常需要迭代。
6. 后处理磁链、损耗、电场强度、端口阻抗、力或温升源项。
7. 将结果转换为 EMT 可用模型，并用测量、解析解或网格收敛检查验证。

## 与 EMT 的耦合方式

- 离线参数提取：用 FEM 计算电感、电容、电阻、磁化曲线或频率响应，再写入 EMT 元件。
- 查表耦合：以电流、位置、温度或频率为输入，查表得到磁链、损耗或力。
- 场路联合仿真：电路侧提供端口电压电流，FEM 侧返回磁链、反电势、阻抗或损耗。
- 模型降阶：把 FEM 频响或状态方程压缩为可在 EMT 步长内运行的模型，见 [[model-order-reduction]]。
- 频率相关等值：把 FEM 得到的端口响应拟合为 [[fdne-model]] 或等效电路。

## 主要变体

- 静态/准静态 FEM：适合低频电场、磁场和涡流问题。
- 频域 FEM：适合正弦稳态、阻抗扫描和谐波场问题。
- 时域 FEM：适合非线性材料和暂态场路耦合，但矩阵求解成本较高。
- 轴对称、二维和平面模型：用几何对称降低成本，但不适合三维端部效应或不对称结构。
- 高阶 FEM 和自适应 FEM：提高局部精度，但需要误差估计和网格质量控制。

## 适用边界与失败模式

- 网格不足会低估尖端电场、气隙磁场、集肤效应或局部损耗。
- 材料曲线、温度、频率和磁滞模型不准确时，场解精细也不能保证 EMT 参数可信。
- 二维或轴对称模型不能默认代表端部绕组、引线、接地引下线等三维效应。
- 场路耦合若步长过大或插值不当，可能产生能量不守恒或数值振荡。
- FEM 结果转换为集总参数时，会丢失空间分布信息；必须说明端口定义和适用频带。

## 证据边界

FEM 证据通常支撑具体几何、材料、边界和频率/时间范围内的场量或端口参数。若来源只使用 FEM 作为参数提取或对比基准，不能外推为某 EMT 模型在所有暂态下准确。若论文报告与 FEM 对比的误差，应保留其设备、频带、网格和测量/参考模型条件。

可作为入口的来源包括 [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu]]、[[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d]]、[[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t]] 和 [[electromagnetic-modeling-of-transformers-in-emt-type-software-by-a-circuit-based]]。

## 与相关页面的关系

- [[fdtd]]：规则网格显式时域全波方法，适合宽带传播问题。
- [[interface-technique]]：说明 FEM 场域与 EMT 电路之间的端口交换。
- [[hybrid-modeling]]：把 FEM 与电路、控制或系统模型组合的上层方法。
- [[frequency-scan]]：FEM 端口响应可作为频率扫描输入。
- [[vector-fitting]]：把 FEM 频响拟合为可嵌入 EMT 的有理模型。
- [[emt-simulation-verification]]：说明 FEM 作为参考模型时的验证边界。
