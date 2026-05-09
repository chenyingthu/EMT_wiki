---
title: "电磁暂态 (Electromagnetic Transient)"
type: topic
tags: [electromagnetic-transient, emt, fast-transient, switching, overvoltage]
created: "2026-05-02"
---

# 电磁暂态 (Electromagnetic Transient)

## 技术背景

### 发展历史
该技术源于电力系统仿真领域的长期研究积累，随着电力电子设备在电网中的广泛应用而日益重要。

### 研究现状
当前学术界和工业界对该技术的研究主要集中在提升仿真效率、计算效率和模型通用性方面。

### 技术挑战
- 大规模系统的计算复杂度问题
- 多时间尺度混合仿真的协调问题
- 实时仿真的时效性要求
- 模型验证和不确定性量化

## 定义与边界

电磁暂态（Electromagnetic Transient）指电力系统中电压、电流、磁链、电荷和电磁场在扰动后发生的快速时域变化。它覆盖开关动作、雷电冲击、短路故障、铁磁饱和、电力电子开关和行波传播等波形级现象，通常需要在相域或多导体坐标中保留瞬时量。

本页讨论“物理现象与研究对象”。它不同于 [[emt-simulation]]，后者讨论如何用数值程序求解这些现象；也不同于 [[electromechanical-transient]]，后者以机电能量交换、转子角和慢速控制为主。若研究问题只依赖工频正序相量、潮流或秒级频率恢复，直接使用 EMT 语言会夸大模型需求。

## EMT 中的作用

电磁暂态是 EMT 建模和验证的核心对象。仿真模型需要回答的不是“系统是否正常运行”，而是扰动后某个端口、设备或保护判据看到的瞬时波形是否可信。典型用途包括：

- 在 [[switching-transient]] 中评估合闸、分闸、重燃、截流和暂态恢复电压。
- 在 [[lightning-overvoltage]] 中评估行波、反射、接地响应、避雷器应力和绝缘配合。
- 在 [[unbalanced-fault-analysis]] 中保留相别、零序、负序、直流偏置和保护测量链。
- 在 [[power-electronics]]、[[vsc-hvdc]] 和 [[mmc-model]] 中观察阀级开关、限流、控制采样和非线性保护动作。

## 主要分支与机制

电磁暂态可按扰动源和传播机制分为若干相互重叠的分支：

- 开关暂态：拓扑状态 $s(t)$ 改变，使网络方程 $\mathbf{Y}(s)\mathbf{v}=\mathbf{i}$ 在事件点发生重组或等值切换。
- 雷电暂态：雷电流、外部电磁场和接地系统共同产生入射波、反射波和侵入波，需要与 [[transmission-line-theory]]、[[frequency-dependent-soil]] 和 [[surge-arrester-model]] 衔接。
- 故障暂态：故障阻抗、接地路径、保护动作和电机次暂态响应共同决定电流波形，不能只用稳态短路电流替代。
- 频变传播：导体集肤效应、大地回流和电缆护层使 $\mathbf{Z}(\omega)$ 与 $\mathbf{Y}(\omega)$ 随频率变化，常由 [[wideband-modeling]]、[[vector-fitting]] 或 [[universal-line-model]] 表示。
- 非线性暂态：磁饱和、电弧、避雷器、开关器件和控制限幅使局部关系从线性导纳变为 $i=f(v,x,t)$。

一个保守的时域表达可写为

$$
\mathbf{Y}_{s,n}\mathbf{v}_n =
\mathbf{i}^{\mathrm{src}}_n+\mathbf{i}^{\mathrm{hist}}_n+\mathbf{i}^{\mathrm{nl}}(\mathbf{v}_n,\mathbf{x}_n),
\qquad
\mathbf{x}_{n+1}=F_{\Delta t}(\mathbf{x}_n,\mathbf{v}_n,\mathbf{u}_n,s_n).
$$

其中 $\mathbf{v}_n$ 为节点电压向量，$\mathbf{x}_n$ 为元件或控制状态，$\mathbf{i}^{\mathrm{hist}}_n$ 为伴随电路历史源，$s_n$ 为拓扑或开关状态。该式只说明 EMT 型问题的接口，不等同于任何单一软件实现。

## 适用边界与失败模式

- 时间尺度和频带必须由研究对象决定。雷电波头、开关事件、控制采样和故障保护需要不同步长和模型细节。
- 无来源的“典型过电压倍数”“典型波阻抗”“典型采样率”不应作为结论；这些数字只有在绑定线路类型、接地、端接、工具和来源时才有意义。
- 梯形积分、后向欧拉、Gear 类方法和插值策略会改变高频阻尼与事件点能量误差，应在 [[numerical-integration]] 和 [[interpolation-method]] 的边界内解释。
- 详细 EMT 结果依赖参数质量。若线路频变参数、变压器饱和、避雷器伏安曲线、电弧参数或控制限幅缺失，结论只能作为场景探索。
- 大系统 EMT 可能因矩阵重构、非线性迭代、事件密集和初始化不一致而失败；加速或等值方法需要报告基准波形和误差定义。


### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s
- 电压等级：10kV ~ 500kV
- 功率范围：1MW ~ 1000MW
- 频率范围：50Hz / 60Hz

## 代表性来源

- [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on]] 可作为 EMTP 型时域建模传统的来源入口，适合追踪节点方程、伴随电路和暂态程序结构。
- [[a-combined-state-space-nodal-method-for-the-simulation-of-power-system-transient]] 支撑状态空间与节点分析组合的机制讨论。
- [[a-comparative-study-of-electromagnetic-transient-simulations-using-companion-cir]] 提醒伴随电路实现之间可能存在数值差异，不能只用“EMT”标签替代算法说明。
- [[accuracy-evaluation-of-electromagnetic-transients-simulation-algorithms]] 支撑“精度需要绑定测试系统、指标和参考解”的证据纪律。
- [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an]] 可作为线路与电缆暂态中数值稳定性问题的来源入口。

## 与相关页面的关系

- [[emt-simulation]] 是仿真范式页；本页是现象边界页。
- [[switching-transient]]、[[lightning-overvoltage]] 和 [[unbalanced-fault-analysis]] 是本主题下的高频、过电压和故障分支。
- [[phase-domain-model]] 说明在相域保留不对称和耦合的建模路线，是许多电磁暂态问题的底层表达。
- [[frequency-domain-analysis]] 和 [[harmonic-analysis]] 提供频域诊断，但不能替代事件驱动的瞬时波形验证。
- [[real-time-simulation]] 与 [[hil-simulation]] 是执行约束；实时通过不等于物理模型自动更可信。

## 开放问题

- 如何在可审计文档中同时记录模型层级、参数来源、步长、事件处理和验证基线。
- 如何为黑盒电力电子设备和保护控制器建立既可共享又不泄露商业细节的 EMT 模型证据。
- 如何把频域阻抗、机电暂态、现场录波和 EMT 波形组织成一致的验证链。
- 如何判断模型降阶、平均值模型和频变等值在目标暂态下的失效边界。
