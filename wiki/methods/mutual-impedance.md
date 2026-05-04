---
title: "互阻抗 (Mutual Impedance)"
type: method
tags: [mutual-impedance, coupling, parallel-lines, transmission-line, zero-sequence]
created: "2026-05-02"
---

# 互阻抗 (Mutual Impedance)

## 定义与边界

互阻抗描述一个导体或回路中的电流在另一个导体或回路中引起电压响应的比例关系。在线路和电缆 EMT 建模中，它是单位长度串联阻抗矩阵的非对角元素，用来表达相间、多回路、地线、护套和大地返回路径之间的电磁耦合。

若 $n$ 根导体组成多导体系统，频域串联阻抗矩阵可写为：

$$V'(\omega)=Z'(\omega)I(\omega)$$

其中：

$$Z'(\omega)=
\begin{bmatrix}
Z_{11} & Z_{12} & \cdots & Z_{1n}\\
Z_{21} & Z_{22} & \cdots & Z_{2n}\\
\vdots & \vdots & \ddots & \vdots\\
Z_{n1} & Z_{n2} & \cdots & Z_{nn}
\end{bmatrix}$$

非对角项 $Z_{ij}$ 即互阻抗。它不只是工频故障分析参数，也影响 [[methods/distributed-parameter-line.md]]、[[methods/earth-return-impedance.md]] 和宽频 EMT 模型。

## EMT 中的作用

互阻抗在 EMT 中用于解释：

- 双回线、平行线路和混合走廊中的感应电压/电流。
- 不平衡故障、零序网络和接地保护计算。
- 电缆芯线、护套、铠装和邻近电缆之间的耦合。
- 多导体频变模型中的相域矩阵、模态解耦和相互影响。

如果忽略互阻抗，模型可能低估或错估平行回路耦合、地线去磁效应、护套环流和架空-地下混合线路感应。

## 核心机制

互阻抗来自导体间共享磁场和回流路径。对低频均匀近似，互阻抗常被表示为几何距离和大地返回项的函数；在宽频模型中，它应作为频率相关矩阵元素计算：

$$Z_{ij}'(\omega)=j\omega L_{ij}(\omega)+R_{ij}(\omega),\quad i\ne j$$

若包含大地返回：

$$Z_{ij}'(\omega)=Z_{\text{geom},ij}(\omega)+Z_{\text{earth},ij}(\omega)$$

在三相对称、完全换位且参数理想均匀时，序分量变换可把矩阵近似对角化；在非换位、平行多回路或电缆系统中，非对角耦合可能不能忽略，需要 [[methods/phase-domain-modeling.md]] 或频率相关 [[methods/modal-transformation.md]]。

## 分类与变体

| 场景 | 互阻抗来源 | 常见用途 | 主要边界 |
|------|------------|----------|----------|
| 三相架空线 | 相间几何耦合和地回路 | 序阻抗、故障计算 | 换位和地线影响很大 |
| 平行多回线路 | 回路间磁耦合 | 感应电压、保护整定 | 运行方式和零序电流相关 |
| 地下电缆 | 芯线-护套-铠装耦合 | 护套电压、暂态过电压 | 接地方式和土壤参数关键 |
| 架空-地下混合走廊 | 不同介质和回流路径耦合 | 混合线路感应分析 | 传统 LC/CC 工具可能不足 |

## 适用边界与失败模式

- 互阻抗不是固定常数；它随频率、几何布置、导体材料、土壤和回流路径变化。
- 序阻抗公式依赖对称和换位假设。把 $Z_0,Z_1,Z_2$ 的简单关系套到非对称线路可能误导。
- 对宽频暂态，使用工频互阻抗可能无法反映集肤、邻近和大地返回效应。
- 互阻抗导致的感应现象需要结合边界条件和负载/接地状态解释；仅有矩阵元素不能直接给出危险程度。

## 代表性来源

- [[sources/earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14.md]]：把自阻抗和互阻抗纳入多层大地统一公式，适合支撑“互阻抗依赖土壤结构”的表述。
- [[sources/a-new-tool-for-calculation-of-line-and-cable-parameters.md]]：说明复杂架空线/电缆参数计算需要统一处理邻近效应和混合导体耦合。
- [[sources/development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-.md]]：展示相域频变矩阵模型在实时仿真中的实现意义。
- [[sources/frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method.md]]：适合说明多导体线路可通过模态处理互耦，但其结论仍受验证范围限制。

## 与相关页面的关系

- [[methods/earth-return-impedance.md]] 是互阻抗的重要组成。
- [[methods/distributed-parameter-model.md]] 和 [[methods/distributed-parameter-line.md]] 使用互阻抗构造多导体方程。
- [[methods/single-phase-line-model.md]] 通常忽略或外部化互阻抗，适合简化场景。
- [[topics/frequency-dependent-modeling.md]] 讨论互阻抗随频率变化后的时域实现。
- [[methods/impedance-measurement.md]] 可用于识别或校核等效耦合参数。

## 修订与证据使用注意事项

后续扩展本页时，应优先补充“互阻抗如何进入矩阵、如何影响 EMT 结果”的证据。保护整定、故障测距或标准计算公式若没有来源，不应作为确定结论写入。
