---
title: "矢量拟合"
type: method
tags: []
created: "2026-04-13"
---

# 矢量拟合

## 定义与边界

矢量拟合（Vector Fitting, VF）是一种频域有理函数逼近方法，用迭代极点重定位把离散频率响应拟合为极点-留数模型。常见目标形式为 $H(s)\approx\sum_{m=1}^{M}\frac{R_m}{s-p_m}+D+sE$；多端口导纳可写为 $\mathbf{Y}(s)\approx\sum_m\frac{\mathbf{R}_m}{s-p_m}+\mathbf{D}+s\mathbf{E}$。

VF 解决的是“由频域采样得到可时域实现的有理模型”。它不直接保证模型接入 EMT 后无源、稳定或实时可运行；这些需要 [[passivity-enforcement]]、[[state-space-method]]、离散化和时域验证。它也不负责给出物理材料参数，除非拟合模型与物理参数之间有额外映射。

## EMT 中的作用

VF 是 [[frequency-dependent-modeling]] 和 [[fdne-model]] 的关键工具。线路、电缆、变压器、外部网络和黑箱设备的阻抗/导纳频率响应经过 VF 后，可转为递推卷积、状态空间模型或等效 RLC 网络，从而进入 EMT 时间步进。

VF 的价值在于把宽频响应压缩为有限阶模型。模型阶数、频率范围、采样密度、权重和初始极点决定拟合结果；离开这些条件谈“高精度”“最优”或“实时”都不够严谨。

## 核心机制

标准 VF 通过辅助函数 $\sigma(s)$ 把同时优化极点和留数的非线性问题拆成线性最小二乘问题。给定起始极点 $\bar{p}_m$，先拟合 $\sigma(s)H(s)$ 与 $\sigma(s)$，再把 $\sigma(s)$ 的零点作为更新极点。极点收敛后，固定极点重新求留数、直接项和高频项。

对多端口系统，常采用公共极点策略：所有矩阵元素共享同一组极点，但留数为矩阵。这样有利于统一状态空间实现，却可能增加阶数。若导纳矩阵小特征值很重要，普通元素级误差可能不足以控制高阻抗端接下的响应误差，需要模态加权或模态 VF。

## 分类与变体

| 变体 | 机制 | EMT 用途 | 边界 |
|------|------|----------|------|
| 标准 VF | 两阶段极点重定位和留数识别 | 单端口或矩阵元素频响拟合 | 对初始极点、权重和频段敏感 |
| 复数 VF | 允许独立复极点或复数域响应 | 基带、非对称或变换域模型 | 实值时域实现需额外处理 |
| 模态 VF | 在模态分量上加权拟合 | 多端口 FDNE、小特征值保护 | 依赖模态变换和矩阵对称性 |
| 快速/并行 VF | 利用稀疏结构、QR 和底层线性代数 | 大规模端口或高采样数拟合 | 加速量绑定实现平台 |
| VF + 降阶 | 拟合后截断弱状态或做 MOR | 实时仿真和 HIL | 降阶后需重新检查误差和无源性 |

## 适用边界与失败模式

- 采样边界：采样点应覆盖 DC 或最低关注频率至最高关注频率；谐振峰附近需要更密集采样。
- 初始极点边界：起始极点不足或分布不当会导致局部拟合差、冗余阶数或不稳定极点。
- 权重边界：幅值很小的通道、小特征值和高阻抗端接需要相对误差控制，不能只看绝对 RMS。
- 无源性边界：拟合曲线匹配不代表 $\mathbf{Y}(j\omega)$ 正实；非无源模型可能在 EMT 中发散。
- 非线性边界：VF 拟合线性频响；饱和、开关限幅和控制模式切换只能通过分段或多工作点处理。
- 证据边界：原页面中的“首次”“最优”“机器精度”“20-25 倍”等强结论只在对应论文和算例中成立，本页改为论文级证据，不写成领域共识。

## 代表性来源

| 来源 | 支撑内容 | 使用边界 |
|------|----------|----------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] | 复数起始极点扩展 VF，用于含谐振峰的频域响应有理逼近 | 原始抽取中未完整给出所有算例表图；数值精度需回原文核对 |
| [[fast-realization-of-the-modal-vector-fitting]] | 快速模态 VF 面向多端口导纳矩阵和小特征值模态 | 加速和误差结论依赖原文 FDNE 算例与实现 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin]] | 比较 VF、矩阵束、Loewner 等曲线拟合/降阶方法 | 选型结论应限于其测试算例 |
| [[transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-]] | VF 用于多相线路和频变土壤参数相关暂态建模 | 证据限于原文线路、土壤和频率设置 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend]] | 并行/底层实现可改善 FDNE 有理逼近计算性能 | 不能外推为所有端口规模和硬件平台 |

## 与相关页面的关系

- [[parameter-identification]]：VF 是频域参数辨识的一种特化形式。
- [[prony-analysis]]：Prony 从时域响应拟合指数模态；VF 从频域响应拟合有理函数。
- [[passivity-enforcement]]：VF 后处理常需要无源性检测和修正，尤其是多端口导纳。
- [[state-space-method]]：极点-留数结果常转换为状态空间参与 EMT 步进。
- [[model-order-reduction]]：VF 模型阶数偏高时，可进一步降阶，但需重新验证频域和时域误差。
- [[wideband-modeling]]：VF 是宽频模型的常用实现路径，但不是唯一选择。
