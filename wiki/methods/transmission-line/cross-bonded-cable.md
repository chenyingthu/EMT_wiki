---
title: "交叉互联电缆 (Cross-bonded Cable)"
type: method
tags: [cross-bonded, cable, sheathing, grounding, high-voltage]
created: "2026-05-02"
---

# 交叉互联电缆 (Cross-bonded Cable)


```mermaid
graph TD
    subgraph Ncmp[交叉互联电缆 (Cross-bonded Cable)]
        N0[护套显式多导体模型: 芯线、护套、接地线同列入线路矩阵]
        N1[小段线路加接头节点: 每个小段独立线路元件，接头箱处交换…]
        N2[等效护套回路模型: 用互感电压源和护套阻抗构造回路]
        N3[端口等效/降阶模型: 保留端部和接地箱端口响应]
    end
```


## 定义与边界

交叉互联电缆是单芯交流电缆中金属护套/屏蔽层的一种连接方法：把线路划分为若干小段，并在接头箱处交叉连接三相护套，使一个主段内不同相位的护套感应电压尽量相互抵消。其目标是在限制护套对地电压的同时降低闭合护套环流和相关损耗。

本页讨论交叉互联作为 EMT 电缆和接地方法。它不等同于电缆本体参数计算，也不等同于绝缘接头、护层保护器或接地网的产品设计；这些对象需要与 [[underground-cable-modeling]]、[[grounding-system-modeling]] 和 [[insulation-coordination]] 一起建模。

## EMT 中的作用

在 EMT 中，交叉互联影响：

- 正常运行和不平衡故障下的护套感应电压、护套电流和损耗。
- 雷电、开关和故障波沿电缆护套、接地线和接地箱传播时的反射与分流。
- 护层保护器、绝缘接头和接地箱的过电压应力。
- 零序/地模通道，以及电缆段与接地系统之间的耦合。

因此，交叉互联不应只用“护套电压抵消”一句描述。EMT 模型至少要保留小段长度、接头箱连接、接地点阻抗和护套/芯线互耦。

## 核心机制

单芯电缆芯线电流通过互感在护套中感应纵向电压。简化相量表达可写为：

$$\mathbf{e}_s=j\omega\mathbf{M}_{sc}\mathbf{i}_c$$

其中 $\mathbf{i}_c$ 是芯线电流向量，$\mathbf{M}_{sc}$ 是芯线-护套互感矩阵。长度为 $\ell_k$ 的第 $k$ 小段护套感应电压近似为：

$$\Delta\mathbf{v}_{s,k}=\ell_k\mathbf{e}_{s,k}$$

交叉互联箱可用排列矩阵 $\mathbf{P}_k$ 表示护套连接关系。一个主段内的累积护套电压为：

$$\mathbf{v}_{s,\text{major}}=\sum_{k=1}^{3}\mathbf{P}_k\Delta\mathbf{v}_{s,k}$$

在三相电流平衡、三小段长度和参数接近、接地连接理想的条件下，三段感应电压的相量和可以接近抵消。实际 EMT 中该抵消只是条件性近似，因为负荷不平衡、几何不对称、故障、护套保护器动作、接地阻抗和频率相关参数都会留下残余电压与电流。

## EMT 建模方式

| 表示方式 | 处理内容 | 适合用途 | 注意事项 |
|----------|----------|----------|----------|
| 护套显式多导体模型 | 芯线、护套、接地线同列入线路矩阵 | 雷电、故障、护套过电压 | 参数和连接矩阵必须一致 |
| 小段线路加接头节点 | 每个小段独立线路元件，接头箱处交换护套节点 | 详细 EMT 和保护器应力 | 节点数多，易出连接错误 |
| 等效护套回路模型 | 用互感电压源和护套阻抗构造回路 | 工频环流和设计筛选 | 高频传播和反射不足 |
| 端口等效/降阶模型 | 保留端部和接地箱端口响应 | 大系统扫参 | 需要用详细模型或测量校核 |

## 连接与方程接口

交叉互联可在节点方程中表示为理想连接约束、很小阻抗连接或受保护器非线性支路约束。若 $\mathbf{A}$ 是护套节点连接矩阵，则连接条件可写成：

$$\mathbf{A}\mathbf{v}_s=\mathbf{0}$$

或通过支路导纳并入网络：

$$\mathbf{i}_b=\mathbf{Y}_b\mathbf{A}\mathbf{v}_s$$

当护层保护器或间隙动作时，$\mathbf{Y}_b$ 变为非线性或开关状态相关。此时模型必须与 [[surge-arrester-model]]、开关事件插值和接地节点阻抗一致。

## 适用边界与失败模式

- 三段完全抵消依赖平衡电流、相似段长、相似几何和理想连接；故障、负荷不平衡或混合敷设会破坏这一条件。
- 护套绝缘接头、交叉互联箱和保护器的杂散电容/电感可影响陡波响应。
- 接地电阻或接地网频变阻抗不应被替换成理想地，除非该近似已通过目标频段验证。
- 护套保护器动作会改变边界条件，可能使线性频域模型和稳态环流计算失效。
- 工频环流模型不能直接证明雷电护套过电压安全；两者的频谱和边界条件不同。

## 代表性证据

- [[underground-cable-modeling]] 提供电缆多导体 EMT 表示的总框架，交叉互联应作为护套连接条件嵌入其中。
- [[time-domain-modeling-of-a-subsea-buried-cable]] 支撑电缆护套/铠装和外部介质会进入时域线路模型，但该 source 是海底电缆算例，不直接证明交叉互联设计规则。
- [[multi-scale-formulation-of-admittance-based-modeling-of-cables]] 支撑端口导纳型电缆模型可用于电缆 EMT 接口；交叉互联箱和护套连接仍需在网络拓扑中显式或等效表示。
- [[earth-return-impedance]] 与 [[frequency-dependent-soil]] 支撑接地返回路径和土壤频变会影响护套/地模暂态。

## 与相关页面的关系

- [[underground-cable-modeling]] 是电缆本体和参数建模入口。
- [[grounding-system-modeling]] 描述护套接地点、接地箱和接地网接口。
- [[high-frequency-transient-analysis]] 和 [[lightning-transient-analysis]] 处理陡波下的护套过电压。
- [[insulation-coordination]] 用护套和绝缘接头的过电压结果检查保护裕度。
- [[phase-domain-modeling]] 适合表达芯线-护套-接地线的非对称耦合。

## 开放问题

- 交叉互联箱、护层保护器和接地引下线的宽频参数常缺少公开可复核数据。
- 长电缆多主段模型在大系统 EMT 中可能需要降阶，但降阶后必须保留护套过电压和保护器能量指标。
- 工程资料中的接地方式、段长和保护器参数需要与仿真模型逐项核对，不能只按示意图连接。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[algorithm-for-fast-calculating-the-energization-overvoltages-along-a-power-cable|Algorithm for fast calculating the energization overvoltages]] | 2022 |
| [[multi-conductor-cable-modeling-with-inclusion-of-measured-coaxial-wave-propagati|Multi-Conductor Cable Modeling With Inclusion of Measured Co]] | 2023 |