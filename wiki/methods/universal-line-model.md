---
title: "通用线路模型 (Universal Line Model, ULM)"
type: method
tags: [universal-line, frequency-dependent, marti, transmission-line, vector-fitting]
created: "2026-05-02"
---

# 通用线路模型 (Universal Line Model, ULM)


```mermaid
graph TD
    subgraph Ncmp[通用线路模型 (Universal Line Model…]
        N0[相域 ULM: 直接拟合 $\mathbf{Y}_c$ …]
        N1[JMarti 类模型: 使用近似常数模态变换和频变传播函数]
        N2[Noda 相域模型: 相域处理频变线路响应]
        N3[FLE 频变实现: 分解节点导纳为开路/短路块]
    end
```


## 定义与边界

通用线路模型（Universal Line Model, ULM）是 EMT 中用于相域频率相关线路建模的一类方法名称。这里的“通用”是模型名，不表示它对所有线路、所有频带或所有软件实现都无条件适用。

ULM 的核心边界是：直接在相域中处理多导体线路的特征导纳矩阵和传播矩阵，并把它们拟合成时域可递推的历史项。它区别于固定模态变换的 JMarti 类模型，也区别于常参数 [[bergeron-line-model]]。其可信度取决于线路参数、频率采样、拟合质量、延迟提取、无源性和时域接口实现。

## EMT 中的作用

ULM 面向以下 EMT 场景：

- 非换位或强不对称线路中，常数模态变换可能不足以描述频率相关耦合。
- 地下电缆、架空-电缆混合段、频率相关土壤参数和大地返回路径对暂态结果有影响。
- 需要把宽频线路频域响应转成节点导纳方程中的固定导纳和历史电流源。
- 需要与不同 EMT 工具中的线路模型进行方法级对比，但不能把软件实现差异混同为理论差异。

## 核心机制

频域多导体线路方程可写为：

$$-\frac{d\mathbf{V}}{dx}=\mathbf{Z}(\omega)\mathbf{I},\quad
-\frac{d\mathbf{I}}{dx}=\mathbf{Y}(\omega)\mathbf{V}$$

其中 $\mathbf{Z}(\omega)$ 和 $\mathbf{Y}(\omega)$ 是单位长度串联阻抗和并联导纳矩阵。ULM 通常围绕两个频率相关矩阵构造端口关系：

$$\mathbf{Y}_c(\omega)=\mathbf{Y}(\omega)^{-1}\sqrt{\mathbf{Y}(\omega)\mathbf{Z}(\omega)}$$

$$\mathbf{H}(\omega)=e^{-\ell\sqrt{\mathbf{Z}(\omega)\mathbf{Y}(\omega)}}$$

$\mathbf{Y}_c$ 决定端口特征导纳，$\mathbf{H}$ 描述跨端传播、衰减和相间耦合。时域实现通常把这些频域函数写成延时项与有理函数的组合：

$$\hat{F}(s)=D+\sum_{r=1}^{N}\frac{R_r}{s-p_r}$$

每个极点-留数项可离散为递归卷积历史变量，最后形成 Norton 等效：

$$\mathbf{i}(t)=\mathbf{G}\mathbf{v}(t)+\mathbf{i}_h(t)$$

## 建模流程

1. 计算线路几何、导体、护套、土壤和介质参数对应的 $\mathbf{Z}(\omega)$、$\mathbf{Y}(\omega)$。
2. 形成相域 $\mathbf{Y}_c(\omega)$ 和 $\mathbf{H}(\omega)$，并确定每个传播通道的延时处理方式。
3. 使用 [[vector-fitting]] 或相关有理逼近方法拟合频率响应。
4. 检查稳定极点、实系数、一致的低频/高频极限和 [[passivity-enforcement]]。
5. 把拟合结果离散为 EMT 步进中的导纳矩阵、历史电流源和延时队列。
6. 用频域拟合误差、时域波形对比和关键工况复核模型。

## 变体与相邻模型

| 方法 | 核心处理 | 适合用途 | 边界 |
|------|----------|----------|------|
| 相域 ULM | 直接拟合 $\mathbf{Y}_c$ 和 $\mathbf{H}$ | 非对称线路、地下电缆、宽频暂态 | 矩阵拟合和实现复杂 |
| JMarti 类模型 | 使用近似常数模态变换和频变传播函数 | 常见架空线暂态 | 频率相关特征向量强变化时需复核 |
| Noda 相域模型 | 相域处理频变线路响应 | 避免固定模态假设 | 对时间步和拟合设置敏感性需验证 |
| FLE 频变实现 | 分解节点导纳为开路/短路块 | 短线路和导纳拟合问题 | 依赖分解、拟合和无源性处理 |

## 适用边界与失败模式

- ULM 的频率响应拟合不应只看幅值；相位、延时提取和低频极限同样影响 EMT 波形。
- 频率相关土壤、护套和接地返回导纳的不确定性会进入线路参数，不能靠 ULM 结构本身消除。
- 有理模型若非无源，连接到其他网络元件后可能产生非物理振荡。
- 外部模型接口可能引入单步延迟、插值或数据交换误差；这属于实现边界，不是线路理论本身。
- 论文或工具中的“参考模型”地位只在其验证范围内成立，不应写成所有线路建模问题的最终答案。

## 代表性证据

- [[implementation-of-the-universal-line-model-in-the-alternative-transients-program]]：支撑 ULM 在 ATP 中通过预处理、相域拟合和外部模型接口实现的说明；该来源的验证主要是软件间对比，不能外推为现场实测确认。
- [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-]]：说明相域频变线路模型可被用于 FPGA 实时 EMT 研究；具体步长和精度结论应绑定原文硬件平台。
- [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-]]：适合支撑非换位线路中频率相关变换矩阵会影响模态模型的边界性表述。
- [[validation-of-frequency-dependent]]：可作为频变线路模型验证入口；具体结论需回到该 source 的证据边界。

## 与相关页面的关系

- [[distributed-parameter-line]] 提供线路方程总框架。
- [[bergeron-line-model]] 是常参数行波时域实现入口。
- [[folded-line-equivalent]] 是频变线路节点导纳分解的相邻实现路线。
- [[frequency-dependent-soil]]、[[earth-return-impedance]] 和 [[mutual-impedance]] 决定 ULM 输入参数的物理边界。
- [[frequency-dependent-modeling]] 讨论宽频参数转时域的共性问题。

## 修订与证据使用注意事项

本页后续补充应避免无来源的频带、误差、阶数、运行时间和软件功能描述。若要比较 ULM、JMarti、Noda、Bergeron 或 FLE，应说明对比对象是理论结构、软件实现还是某个论文算例。
