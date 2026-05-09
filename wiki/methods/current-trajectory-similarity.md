---
title: "电流轨迹相似性方法 (Current Trajectory Similarity)"
type: method
tags: [current-trajectory-similarity, pattern-recognition, protection, waveform]
created: "2026-05-05"
updated: "2026-05-06"
---

# 电流轨迹相似性方法 (Current Trajectory Similarity)


```mermaid
graph TD
    N0[电流轨迹相似性方法 (Curre…]
    N1[定义与边界]
    N0 --> N1
    N2[EMT 中的作用]
    N0 --> N2
    N3[关键公式]
    N0 --> N3
    N4[常见路线]
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

电流轨迹相似性方法是通过比较故障或运行过程中的电流波形轨迹、形状或特征序列来进行识别、分类或判据构造的技术路线。它常出现在保护判据、事件识别和波形模式匹配场景中。

本页讨论的是“轨迹相似性”这一判据思路，不把限流熔断器经验模型或 EMTP/TACS 电弧等效方法误写成该方法本身。

## EMT 中的作用

在 EMT 研究中，电流轨迹相似性方法可用于：

- 根据故障初期波形特征识别故障类型或区段；
- 比较不同事件、不同位置或不同模型产生的电流轨迹；
- 构造保护、监测或诊断算法中的相似度指标；
- 辅助验证模型是否保留了关键波形形状特征。

## 关键公式

最简单的相似性度量可写为：

$$
S(\mathbf{i}_1,\mathbf{i}_2)=\frac{\mathbf{i}_1^\top \mathbf{i}_2}{\|\mathbf{i}_1\|\,\|\mathbf{i}_2\|}
$$

也可用动态时间规整、距离度量或特征嵌入。关键是比较对象必须来自可对齐的波形窗口和一致的采样条件。

## 常见路线

- 直接波形相似度：比较归一化后的原始电流轨迹。
- 特征相似度：比较波头、峰值、能量或变换域特征。
- 模板匹配或分类路线：把参考轨迹库作为故障识别或事件分类依据。

## 与相关方法的关系

- [[dc-protection]]：波形相似性可用于故障判据设计。
- [[digital-distance-protection]]：电流/电压轨迹特征也可服务保护算法。
- [[filtering]]：轨迹特征提取前常需预处理。
- [[fault-analysis]]：故障工况是轨迹相似性方法的典型激励背景。
- [[protection-system]]：保护算法与判据设计的上位背景。

## 适用边界与失败模式

- 适用于有足够采样率且波形特征具有区分度的场景。
- 对噪声、采样对齐误差和工况变化通常较敏感。
- 若训练/参考轨迹覆盖不足，可能出现误判或泛化失败。

## 代表性来源

- [[empirical-model-of-a-current-limiting-fuse-using-emtp]]：可作为电流波形特征和故障过程背景的相关来源。
- [[a-new-topology-for-current-limiting-hvdc-circuit-breaker]]：可作为直流故障电流轨迹相关背景来源。
- [[neutral-conductor-current-in-three-phase-networks-with-compact-fluorescent-lamps]]：说明不同工况下电流轨迹差异的相关背景。

## 证据边界

本页不写某种相似度指标优于所有其他指标，也不写无来源识别率结论。

## 开放问题

- 当前页尚未区分保护判据、诊断分类和模型验证三类使用场景。
- 轨迹相似度对采样同步和噪声的敏感性仍需结合具体算法展开。
