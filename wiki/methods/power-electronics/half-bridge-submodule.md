---
title: "半桥子模块方法 (Half-Bridge Submodule)"
type: method
tags: [half-bridge-submodule, hbsm, mmc, submodule, converter]
created: "2026-05-05"
updated: "2026-05-06"
---

# 半桥子模块方法 (Half-Bridge Submodule)


```mermaid
graph TD
    N0[半桥子模块方法 (Half-Br…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[常见关注点]
    N0 --> N3
    N4[关键公式]
    N0 --> N4
    N5[与相关方法的关系]
    N0 --> N5
    N6[适用边界与失败模式]
    N0 --> N6
    N7[代表性来源]
    N0 --> N7
    N8[证据边界]
    N0 --> N8
```


## 定义与边界

半桥子模块（Half-Bridge Submodule, HBSM）是 MMC 中最常见的子模块单元，由两个主开关器件和一个子模块电容构成。对应的方法问题不是“这个硬件存在”，而是如何在 EMT 中表示其插入/旁路状态、电容电压动态、桥臂电流路径以及与调制、排序和平衡控制的耦合。

本页讨论的是半桥子模块的 EMT 建模与表示边界，不把钳位二极管自平衡拓扑、全桥模型或并行求解框架混写成通用半桥子模块方法。

## EMT 中的作用

在 EMT 仿真中，半桥子模块方法主要用于：

- 表达 MMC 桥臂电压由多个子模块离散叠加形成的过程；
- 跟踪子模块电容电压、插入状态和桥臂电流方向；
- 评估调制、排序和电压平衡对桥臂动态的影响；
- 为平均值模型、详细等效模型或混合模型提供子模块层接口。

## 常见关注点

- 插入/旁路状态与桥臂电流方向的关系；
- 子模块电容电压平衡与排序逻辑；
- 详细开关、等效和平均值模型之间的切换；
- 在直流故障下与全桥或混合拓扑的能力差异。

## 关键公式

若以开关函数 $s \in \{0,1\}$ 表示子模块插入状态，则子模块输出电压常写为：

$$
v_{sm} = s \, v_c
$$

电容电压动态可写为：

$$
C_{sm}\frac{dv_c}{dt} = i_c
$$

其中 $C_{sm}$ 为子模块电容，$i_c$ 为流经电容的电流。半桥结构通常只能输出正电压或零电压，因此其故障阻断和负电平能力与 [[fbsm]] 明显不同。

## 与相关方法的关系

- [[hbsm]]：可作为半桥子模块的简称入口和拓扑别名。
- [[fbsm]]：对比全桥子模块的负电压与故障阻断能力。
- [[nearest-level-modulation]]：说明子模块插入排序与等效输出电平的关系。
- [[mbsm]]：说明多桥臂/混合子模块框架下的统一表示思路。

## 适用边界与失败模式

- 适用于标准半桥 MMC 子模块的 EMT 建模。
- 不适用于直接表达全桥、钳位双桥或混合桥子模块的完整能力。
- 仅用平均值表示时，难以保留单个子模块电压散布和开关事件细节。
- 若不显式建模排序和平衡逻辑，可能低估子模块电压不均衡风险。

## 代表性来源

- [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour]]：说明半桥型 VSC/MMC 相关的快速 EMT 表示背景。
- [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]]：说明半桥 MMC 模型在 EMT 加速场景中的典型处理思路。
- [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-]]：说明半桥子模块拓扑扩展与电容平衡问题的特定场景。

## 证据边界

本页只说明半桥子模块的建模边界和接口关系，不写无来源电容纹波范围、最优平衡算法或统一故障性能结论。

## 开放问题

- 当前页尚未继续拆分“标准 HBSM”与带附加钳位/平衡结构的半桥扩展拓扑。
- 排序和平衡控制的建模深度，仍需结合系统级还是器件级目标判断。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
