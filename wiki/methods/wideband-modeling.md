# 宽频建模方法 (Wideband Modeling)

## 定义与边界

宽频建模方法是在选定频率范围内表征设备、线路、接地系统或外部网络端口响应，并把该响应转换为可用于 EMT 时域仿真的模型族。输入通常包括几何和材料参数、频域测量或数值扫描数据、目标频带、端口定义、采样频点和误差指标；输出可以是频率相关参数、极点-留数有理模型、状态空间模型、递归卷积项、RLC 等效网络或 [[fdne-model]]。

本页关注建模流程和方法边界，不替代 [[frequency-dependent-modeling]] 的主题综述，也不替代 [[vector-fitting]]、[[universal-line-model]]、[[frequency-dependent-line-model]]、[[earth-return-impedance]] 或 [[passivity-enforcement]] 的具体算法页。宽频模型不是“全频精确模型”；它只在已定义频带、端口和工况下有意义。

## EMT 中的作用

EMT 中许多现象由工频以外的网络特性决定，包括开关暂态、雷电过电压、行波反射、谐波传播、超谐波、接地暂态和外部网络频率相关等值。宽频建模的作用是让这些频率相关效应以可计算形式进入 EMT 节点方程或伴随电路。

典型用途包括：

- 为架空线、电缆和混合线路建立频率相关传播和端口导纳。
- 把测量或有限元得到的变压器、接地网、设备端口频响转换为时域模型。
- 构建混合仿真边界和外部网络 [[fdne-model]]。
- 支撑 [[harmonic-analysis-methods]]、[[lightning-transient-analysis]] 和故障行波分析中的端口频响解释。

## 核心机制

宽频模型通常先得到频域函数，例如端口导纳、阻抗或传播函数：

$$Y(j\omega), \quad Z(j\omega), \quad H(j\omega)$$

随后用有理函数近似转成 EMT 可离散实现的形式：

$$Y(s)\approx \sum_{k=1}^{n}\frac{R_k}{s-p_k}+D+sE$$

其中 $p_k$ 是极点，$R_k$ 是留数矩阵，$D$ 和 $E$ 表示直接项和高频项。该形式可进一步转为状态空间、递归卷积或等效 RLC 支路。进入时域前，应检查稳定极点、DC 值、高频渐近、拟合误差、因果性和 [[passivity-enforcement]]。

对线路和电缆，宽频参数还来自物理机制：集肤效应、邻近效应、介质损耗、护套和铠装接地方式、大地回流路径以及频变土壤参数。对设备端口，频响可能来自测量、有限元、电磁场求解或白盒等效电路。

## 分类与变体

| 路线 | 输入 | 输出 | 适用场景 |
|------|------|------|----------|
| 物理参数模型 | 几何、材料、土壤和结构参数 | 频变 $R,L,G,C$ 或传播函数 | 线路、电缆、接地和部分变压器 |
| 测量/扫描黑箱模型 | FRA、端口注入或仿真扫频数据 | 端口阻抗/导纳有理模型 | 设备端口、外部网络和厂商模型 |
| 矢量拟合/有理逼近 | 频域采样点 | 极点-留数、状态空间 | EMT 时域实现和 FDNE |
| 等效电路综合 | 频响或有理模型 | RLC/RLCM 网络 | 需要物理可解释或无源网络时 |
| 模型降阶 | 高阶状态空间或多端口频响 | 低阶近似模型 | 实时仿真和大规模网络 |

## 适用边界与失败模式

- 目标频带必须由研究问题决定；雷电、谐波、次同步振荡和 HIL 接口需要的频带不同。
- 拟合误差小不代表接入 EMT 后稳定；非无源、非因果或 DC 值错误的模型仍可能发散或产生人工偏置。
- 频域测量噪声、端口校准、接地参考和激励幅值会影响模型可信度。
- 用线性宽频模型描述铁芯饱和、电弧、避雷器动作或控制限幅时，应明确它只覆盖线性化或局部工作点。
- 宽频模型阶数越高，实时仿真计算量越大；降阶后必须重新验证频响和时域响应。

## 代表性来源

| 来源 | 可支撑的内容 | 使用边界 |
|------|--------------|----------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] | 矢量拟合把频域响应转为有理函数的基础入口 | 不自动保证无源性或 EMT 稳定 |
| [[advanced-wideband-linecable-modeling-for-transient-studies]] | 线路/电缆宽频建模的代表性来源 | 具体频带和模型结构需回到原文 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat]] | 频率相关线路模型的改进实现 | 结论限于原文线路和算例 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti]] | 常变换矩阵和有理 Krylov 拟合路线 | 需检查变换矩阵和无源性边界 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb]] | 分区拟合和 DC 校正对宽频线路/电缆模型的作用 | 不应外推到所有频带和拓扑 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag]] | HVDC 变压器测量型频率相关模型 | 测量端口、频带和工况限定结论 |

## 与相关页面的关系

- [[frequency-dependent-modeling]] 是总主题页；本页说明方法工作流。
- [[vector-fitting]] 和 [[partial-fraction-expansion]] 处理有理近似和时域实现。
- [[passivity-enforcement]] 是宽频模型接入 EMT 前的关键后处理。
- [[frequency-dependent-line-model]]、[[universal-line-model]]、[[cable-model]] 和 [[transmission-line-model]] 是线路/电缆下游模型页。
- [[earth-return-impedance]]、[[frequency-dependent-soil]] 和 [[frequency-dependent-soil-model]] 说明大地回流和土壤参数如何进入宽频模型。
- [[fdne-model]] 和 [[network-equivalent]] 把宽频建模用于外部网络压缩和混合仿真边界。
