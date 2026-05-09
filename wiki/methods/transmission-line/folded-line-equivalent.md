---
title: "折叠线等效 (Folded Line Equivalent)"
type: method
tags: [folded-line, equivalent, bergeron, transmission-line, delay, travel-time]
created: "2026-05-02"
---

# 折叠线等效 (Folded Line Equivalent)


```mermaid
graph TD
    subgraph Ncmp[折叠线等效 (Folded Line Equivalent)]
        N0[频域导纳 FLE: 对 $\mathbf{Y}_n(s)…]
        N1[电路化 FLE: 把导纳有理函数综合为 RLC 或 No…]
        N2[FLE + 延迟利用: 区分快慢极点，降低慢动态更新频度]
        N3[模态 FLE: 先相域到模态域，再对每个模态折叠]
    end
```


## 定义与边界

折叠线等效是把传输线两端口节点导纳重新分解为开路贡献和短路贡献的一类线路实现方法。它通常从频域线路节点导纳矩阵出发，通过线性变换把原本耦合的两端口问题拆成较小的导纳子问题，再把这些子问题拟合或综合成 EMT 可用的时域等效。

本页讨论方法机制和边界。它不是“把线路几何折弯”的物理模型，也不是对 [[bergeron-line-model]] 的简单改名。FLE 可与 [[vector-fitting]]、[[passivity-enforcement]] 和 [[frequency-dependent-line-model]] 结合，但拟合质量和时域稳定性必须单独验证。

## EMT 中的作用

FLE 在 EMT 中常用于处理两类问题：

- 频变线路节点导纳矩阵阶数较高、特征值跨度较大时，把完整两端口矩阵拆成开路/短路子矩阵再拟合。
- 短线路传播时延小于常规时间步时，避免主要依赖特征线延时队列，从而减轻步长约束。

其外部接口仍是线路两端端口电压和注入电流；内部实现则可能是有理导纳、RLC 综合电路、Norton 历史源或多伴随网络。

## 核心机制

以单模态或单相两端口为例，频域端口关系可写为：

$$
\begin{bmatrix} I_k \\ I_m \end{bmatrix}
=
\mathbf{Y}_n(s)
\begin{bmatrix} V_k \\ V_m \end{bmatrix}
$$

FLE 的关键是用变换矩阵把端口变量映射到“同相”和“反相”组合。常见解释是：

$$
\begin{bmatrix} V_{oc} \\ V_{sc} \end{bmatrix}
=
\mathbf{L}
\begin{bmatrix} V_k \\ V_m \end{bmatrix},\quad
\mathbf{L}=
\frac{1}{\sqrt{2}}
\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

理想条件下，变换后的导纳矩阵可分解为：

$$
\mathbf{Y}_{fle}(s)=\mathbf{L}\mathbf{Y}_n(s)\mathbf{L}^{-1}
=
\begin{bmatrix}
Y_{oc}(s) & 0 \\
0 & Y_{sc}(s)
\end{bmatrix}
$$

$Y_{oc}$ 表示开路型贡献，$Y_{sc}$ 表示短路型贡献。实际多相线路通常先经 [[modal-transformation]] 或相域矩阵处理，然后对每个模态或矩阵块执行类似分解。

## 实现路线

| 路线 | 机制 | 适合用途 | 风险点 |
|------|------|----------|--------|
| 频域导纳 FLE | 对 $\mathbf{Y}_n(s)$ 分解后拟合 $Y_{oc}$、$Y_{sc}$ | 频变线路和短线路等效 | 拟合阶数、无源性、频带选择 |
| 电路化 FLE | 把导纳有理函数综合为 RLC 或 Norton 支路 | ATP/EMTP 类节点求解器 | 电路元件数量和数值条件 |
| FLE + 延迟利用 | 区分快慢极点，降低慢动态更新频度 | 多时间尺度频变线路 | 快慢阈值和强耦合线路响应需验证 |
| 模态 FLE | 先相域到模态域，再对每个模态折叠 | 三相近似可解耦线路 | 频率相关变换矩阵会影响准确性 |

## 适用边界与失败模式

- FLE 改变的是实现和拟合对象，不改变线路端口物理本身。若原始线路参数或土壤模型不可靠，FLE 不会修复物理输入。
- 开路/短路块是否易于拟合取决于线路结构、频带和矩阵条件数。不能把单篇算例中的拟合阶数或加速比写成一般规律。
- 电路化实现需要检查有理函数极点、留数和导纳矩阵无源性；否则时域求解可能出现能量生成。
- 对非换位线路、多回强耦合线路、地下电缆和含接地护套系统，模态解耦假设应谨慎使用。
- 大步长可行性必须绑定模型实现、时间步、线路长度和对比基线，不能写成 FLE 固有能力。

## 代表性证据

- [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-]]：说明改进 FLE 可通过正交变换和电路元件在 ATP 中实现，并与 ULM/JMarti 在所给工况下比较；页面使用时应保留其三相线路、ATP 实现和算例边界。
- [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat]]：说明 FLE 可与延迟利用、多伴随网络和有理拟合结合，用于频变线路时域实现；其效率结论必须绑定原文测试线路和阈值设置。
- [[passivity-enforcement-for-transmission-line-models]] 和 [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res]]：可支撑频变有理线路模型需要无源性处理的边界性表述。

## 与相关页面的关系

- [[bergeron-line-model]] 以延时历史源表示特征线传播；FLE 更偏向节点导纳分解和有理导纳实现。
- [[universal-line-model]] 直接拟合相域特征导纳和传播矩阵，常作为频变线路对比对象。
- [[vector-fitting]] 是把 $Y_{oc}$、$Y_{sc}$ 转为有理函数的常见工具。
- [[passivity-enforcement]] 用于检查和修正有理导纳模型的能量一致性。
- [[large-timestep-simulation]] 讨论时间步限制与模型实现之间的关系。

## 修订与证据使用注意事项

后续扩展本页时，优先说明 FLE 的端口变量、变换矩阵、拟合对象和验证基线。不要保留未核验的“步长扩大倍数”“误差百分比”“计算加速比”或软件功能断言，除非同时给出来源论文、线路算例和频带。
