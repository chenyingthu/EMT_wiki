---
title: "最近电平调制 (Nearest Level Modulation)"
type: method
tags: [nearest-level-modulation, nlm, mmc, modulation, sorting]
created: "2026-05-05"
updated: "2026-05-06"
---

# 最近电平调制 (Nearest Level Modulation)


```mermaid
graph TD
    subgraph S0[最近电平调制 (Nearest Level Modula…]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见关注点]
        N3[关键公式]
        N4[与相关方法的关系]
        N5[适用边界与失败模式]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

最近电平调制（Nearest Level Modulation, NLM）是 MMC 和其他多电平换流器中常见的调制方法，其基本思想是根据参考电压选择最接近的可用离散电平，并据此确定每个桥臂或子模块的插入数量与顺序。

本页讨论的是 NLM 的调制与排序逻辑，不把动态相量、频移方法或一般多速率求解公式误写成 NLM 本身。

## EMT 中的作用

在 EMT 仿真中，NLM 主要用于：

- 把连续参考电压映射为子模块离散插入状态；
- 分析电平合成误差、低开关频率特性和子模块排序策略；
- 研究电容电压平衡与调制逻辑之间的耦合；
- 为 MMC 详细模型、平均值模型和等效模型提供调制背景。

## 常见关注点

- 参考电压到离散插入数的映射；
- 子模块排序与电容电压平衡；
- 低开关频率特性与电平近似误差；
- 在详细模型、等效模型和实时仿真中的不同实现粒度。

## 关键公式

若桥臂共有 $N_{sm}$ 个子模块，目标桥臂电压参考为 $v_{ref}$，则 NLM 常通过“目标插入数”确定等效输出电平：

$$
n_{ins} \approx \operatorname{round}\!\left(\frac{v_{ref}}{v_c^{eq}}\right)
$$

其中 $v_c^{eq}$ 为等效子模块电容电压。实际实现中还需要决定“哪些子模块被插入”，因此排序和平衡策略是 NLM 方法的一部分，而非后处理细节。

## 与相关方法的关系

- [[half-bridge-submodule]] 和 [[fbsm]]：说明子模块拓扑决定可用电平集合。
- [[mbsm]]：统一子模块表示中常需要把 NLM 组织成插入指数或等效电平。
- [[mmc-model]]：给出整机层背景。
- [[circulating-current-suppression]]：说明桥臂调制与内部控制之间的耦合。

## 适用边界与失败模式

- 适用于子模块数较多、需要低开关频率和清晰电平结构的多电平换流器。
- 若子模块电压散布显著，仅靠最近电平选择可能不足以保证长期平衡。
- 在故障、闭锁或极端暂态场景中，NLM 的简化等效可能不足以代表所有开关细节。
- 不同论文中“等效 NLM 模型”的近似范围可能差别很大，不能泛化。

## 代表性来源

- [[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-]]：可作为 NLM 等效建模的直接背景来源。
- [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso]]：说明多电平换流器快速仿真与调制背景。
- [[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters]]：说明 NLM 在 MMC 建模文献中的位置。

## 证据边界

本页不写无来源的最优排序策略、电平误差或实时步长结论。具体实现效果必须绑定调制对象、子模块数量和验证工况。

## 开放问题

- 当前页尚未继续拆分“原始 NLM 排序逻辑”和“基于 NLM 的快速等效模型”之间的边界。
- 不同子模块电压散布条件下的 NLM 适用性，后续应回到具体 source 页继续细化。
