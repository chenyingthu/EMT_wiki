---
title: "换位三相线路 (Transposed Three-Phase Line)"
type: method
tags: [transposed, three-phase, line, balancing, sequence-impedance, transmission]
created: "2026-05-02"
---

# 换位三相线路 (Transposed Three-Phase Line)


```mermaid
graph TD
    subgraph Ncmp[换位三相线路 (Transposed Three-Pha…]
        N0[完全换位平均: 每相经历每个位置的长度相同]
        N1[分段换位模型: 每个区段保留实际相序，再串联]
        N2[部分换位/不完整换位: 只在部分区段交换位置]
        N3[双回协调换位: 同时考虑两回线路相对位置]
    end
```


## 定义与边界

换位三相线路是通过让 A、B、C 三相导线在不同空间位置上轮换运行，使每相在全线或一个换位周期内经历相同几何环境的线路建模对象。它关注的是“几何不对称如何被平均化”，不是保护整定、施工设计手册或通用电压等级参数表。

本页与 [[balanced-three-phase-line]] 的边界是：平衡三相线路讨论已经满足对称参数假设后的等值模型；本页讨论这种假设如何由换位或平均化获得，以及在 EMT 宽频仿真中何时不能只用平均参数。

## EMT 中的作用

换位假设在 EMT 中通常用于决定是否可以：

- 用序分量或固定模态变换近似解耦三相线路。
- 将相域参数矩阵平均为自阻抗相等、互阻抗相等的循环矩阵。
- 在常参数 Bergeron、频变模态模型或相域模型之间选择简化程度。

若目标暂态对高频、地模、非完整换位区段或端部不平衡敏感，换位平均只应作为近似，需与完整相域模型比较。

## 核心机制

未换位三相线路的单位长度阻抗矩阵可写为：

$$
\mathbf{Z}_{abc}=
\begin{bmatrix}
Z_{aa} & Z_{ab} & Z_{ac}\\
Z_{ba} & Z_{bb} & Z_{bc}\\
Z_{ca} & Z_{cb} & Z_{cc}
\end{bmatrix}
$$

完全换位的理想平均把每相在三个位置上经历相同长度。平均后可近似写成循环对称形式：

$$
\bar{\mathbf{Z}}_{abc}=
\begin{bmatrix}
Z_s & Z_m & Z_m\\
Z_m & Z_s & Z_m\\
Z_m & Z_m & Z_s
\end{bmatrix}
$$

实际建模时应由参数生成工具或手算平均矩阵确认自/互阻抗，而不是复制模板。对称化后的理想序阻抗关系为：

$$Z_0=Z_s+2Z_m,\quad Z_1=Z_2=Z_s-Z_m$$

该关系只说明对称矩阵的代数结果。零序阻抗仍依赖大地返回路径、接地线和土壤参数。

## 换位层级

| 层级 | 含义 | 建模影响 | 边界 |
|------|------|----------|------|
| 完全换位平均 | 每相经历每个位置的长度相同 | 可形成平均循环矩阵 | 忽略端部和分段边界 |
| 分段换位模型 | 每个区段保留实际相序，再串联 | 能保留换位点反射和局部不平衡 | 参数量和拓扑复杂 |
| 部分换位/不完整换位 | 只在部分区段交换位置 | 仍可能有残余负序或模态耦合 | 不能直接当成平衡线路 |
| 双回协调换位 | 同时考虑两回线路相对位置 | 影响跨回互耦和零序通道 | 需与 [[parallel-transmission-line]] 联合建模 |

## EMT 建模流程

1. 从实际塔型、相序、地线和区段长度生成相域参数。
2. 判断目标研究是否允许全线平均；工频稳态和部分低频故障分析通常更容易接受平均，雷电和陡波暂态需更谨慎。
3. 若使用平均模型，记录平均方法和换位周期，不把平均参数写成实测相域矩阵。
4. 若使用分段模型，在换位点连接不同相序的线路段，并检查端口相别映射。
5. 对频变线路，分别检查 $\mathbf{Z}(\omega)$ 与 $\mathbf{Y}(\omega)$ 的对称性；常数模态变换不一定覆盖所有频点。
6. 用关键工况比较平均模型与相域/分段模型的差异。

## 适用边界与失败模式

- 换位能降低几何不平衡，但不等于消除所有频率相关耦合。
- 端部未换位区、换位塔附近、并行线路和地线耦合可能保留局部不平衡。
- 对地下单芯电缆、交叉互联护套或混合架空-电缆线路，不能直接套用架空线换位平均。
- 若页面给出不平衡度改善百分比、换位距离、电压等级尺寸，必须绑定工程规范或来源；本页不保留无来源数字。
- 在宽频 EMT 中，频率相关变换矩阵和地模传播可能使“正负序完全解耦”只在部分频带近似成立。

## 代表性证据

- [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p]]：适合支撑“利用换位条件构造频变线路模型”的来源入口；具体算法和验证结果需回到 source。
- [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software]]：支撑完全换位三相线路可用 Clarke 类模态变换电路接入 Bergeron/JMarti 模型的实现思路；其量化结论限于原文测试条件。
- [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-]]：用于提醒不换位线路中频率相关变换矩阵会破坏简单换位/常数模态假设。

## 与相关页面的关系

- [[balanced-three-phase-line]]：已平均后得到的平衡三相模型。
- [[sequence-component-method]] 和 [[symmetrical-components]]：序分量代数基础。
- [[modal-domain-decoupling]]：线路模态解耦条件与失败模式。
- [[parallel-transmission-line]]：双回或多回线路中换位与跨回耦合的组合问题。
- [[frequency-dependent-line-model]]：宽频参数下平均和模态变换的实现边界。

## 修订与证据使用注意事项

后续补充本页时，应优先区分“几何换位事实”“参数平均算法”和“EMT 算例结果”。不要加入未来源绑定的换位距离、工程尺寸、不平衡改善百分比或强制设计结论。
