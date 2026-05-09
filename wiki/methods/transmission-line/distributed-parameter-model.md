---
title: "分布参数模型 (Distributed Parameter Model)"
type: method
tags: [distributed-parameter, transmission-line, wave-propagation, traveling-wave]
created: "2026-05-02"
---

# 分布参数模型 (Distributed Parameter Model)


```mermaid
graph TD
    subgraph Ncmp[分布参数模型 (Distributed Paramete…]
        N0[架空线路: 单位长度阻抗/导纳、传播函数]
        N1[地下电缆: 芯线、护套、绝缘和大地参数]
        N2[接地系统: 土壤电阻率和电磁场分布]
        N3[多导体混合走廊: 自/互阻抗矩阵]
    end
```


## 定义与边界

分布参数模型是把电磁、热、机械或电路参数视为空间位置函数的建模方式。在 EMT Wiki 中，该术语主要用于线路、电缆、接地导体和多导体系统：状态变量不只随时间变化，也随空间坐标变化。

对线路类问题，分布参数模型通常表现为偏微分方程或频域传播矩阵；对 EMT 工具实现，最终需要转化为可接入节点方程的端口模型。它不是“高精度”的同义词，也不等同于 [[distributed-parameter-line]] 一页；本页负责说明通用思想，线路页负责具体线路模型。

## EMT 中的作用

EMT 仿真选择分布参数模型，通常是因为以下现象不能由单个集中阻抗可靠表示：

- 传播延迟和行波反射。
- 参数随频率变化，例如集肤效应、邻近效应和大地返回路径。
- 多导体耦合、护套/地线/回流路径对端口响应的影响。
- 短电缆、架空-地下混合线路、接地系统和宽频暂态中的空间分布效应。

因此，模型选择应从研究目标出发：若只关心低频稳态近似，集中参数可能足够；若研究雷电、快速开关、故障行波或高频振荡，则需要分布参数或频变模型。

## 核心机制

分布参数模型的基本结构是“单位长度参数 + 空间传播”。以线路为例：

$$-\frac{\partial v}{\partial x}=R'(x,\omega)i+L'(x,\omega)\frac{\partial i}{\partial t}$$

$$-\frac{\partial i}{\partial x}=G'(x,\omega)v+C'(x,\omega)\frac{\partial v}{\partial t}$$

在均匀频域模型中，端口关系可由传播常数 $\gamma$ 和特征导纳 $Y_c$ 构建。多导体系统中，$R',L',G',C'$ 是矩阵，需考虑 [[mutual-impedance]] 和并联电容耦合。若参数随频率变化，常通过有理函数近似转入时域：

$$F(s)\approx \sum_{k=1}^{N}\frac{r_k}{s-p_k}+d+se$$

该形式可用于 [[vector-fitting]] 后的递归卷积、状态空间或等效电路实现。

## 分类与变体

| 对象 | 分布量 | 常见 EMT 实现 | 适用边界 |
|------|--------|---------------|----------|
| 架空线路 | 单位长度阻抗/导纳、传播函数 | Bergeron、Marti、ULM | 需处理地线、换位和土壤路径 |
| 地下电缆 | 芯线、护套、绝缘和大地参数 | 多导体频变模型 | 护套接地和土壤参数关键 |
| 接地系统 | 土壤电阻率和电磁场分布 | 频域阻抗或等效网络 | 三维局部结构可能超出线路理论 |
| 多导体混合走廊 | 自/互阻抗矩阵 | 相域或模域模型 | 几何和回流路径决定耦合 |

## 适用边界与失败模式

- 空间分布模型仍依赖几何与材料假设。非均匀土壤、有限长端部、复杂接地体和电缆附件可能需要专门模型。
- 模态解耦对对称或换位线路较方便；非对称多回路和混合架空/电缆系统可能更适合相域模型。
- 频变模型从频域转到时域时，拟合阶数、频带和无源性直接影响数值稳定。
- 分布参数模型通常增加状态、历史量和数据准备成本，不应在问题不需要时机械套用。

## 代表性来源

- [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und]]：说明分布参数/传输线理论在短电缆快速暂态中可与全波 FDTD 对比验证，但结论限于原文算例。
- [[a-new-tool-for-calculation-of-line-and-cable-parameters]]：说明单位长度参数矩阵计算本身就是模型质量的关键环节。
- [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14]]：说明多层土壤会进入大地返回自/互阻抗计算。
- [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-]]：展示分布参数频变模型进入实时仿真的实现压力和边界。

## 与相关页面的关系

- [[distributed-parameter-line]] 是本页在线路对象上的具体化。
- [[transmission-line-model]] 和 [[frequency-dependent-line-model]] 是模型页面。
- [[earth-return-impedance]] 和 [[mutual-impedance]] 是形成单位长度阻抗矩阵的重要组成。
- [[modal-transformation]] 与 [[phase-domain-modeling]] 是处理多导体耦合的两类路径。
- [[lumped-parameter-model]] 是简化对照。

## 修订与证据使用注意事项

本页后续应保持“模型思想”定位，不宜扩写成完整线路教材。具体工具能力、参数范围和误差数字必须下沉到 source 页或对应模型页，并注明验证工况。
