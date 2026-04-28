---
title: "A.M. Gole"
type: entity
tags: [person, researcher, university-of-manitoba, psacard, hvdc, emt]
created: "2026-04-14"
---

# A.M. (Aniruddha M.) Gole

## 概述

A.M. Gole 是曼尼托巴大学（University of Manitoba）电气与计算机工程系教授，电力系统电磁暂态仿真领域的国际知名学者。他是PSCAD/EMTDC仿真软件的核心开发者之一。

## 核心原理详解

Gole 相关工作在本 wiki 中主要连接三类主题：[[pscad-emtdc|PSCAD/EMTDC]] 工具生态、[[vector-fitting|矢量拟合]] 与 [[passivity-enforcement|无源性强制]]、以及 HVDC/FACTS 的 EMT 建模。其技术共同点是把工程设备的宽频端口特性转化为可稳定用于时域仿真的模型。

宽频模型通常先用有理函数拟合端口响应：

$$
H(s)\approx d+\sum_{m=1}^{M}\frac{r_m}{s-p_m}
$$

然后转换为状态空间或等效电路接入 EMT 程序。若拟合模型不满足无源性，连接到外部网络后可能表现为“负阻尼”并导致时域发散，因此无源性检测和修正是这条研究线的关键。

## 主要贡献

- PSCAD/EMTDC软件的核心开发
- HVDC系统EMT建模研究
- 矢量拟合（Vector Fitting）在电力系统中的应用
- 频率相关网络等值（FDNE）建模
- 无源性强制（Passivity Enforcement）算法
- 大规模电力系统暂态仿真

## 研究方向

- 电磁暂态仿真
- HVDC和FACTS建模
- 矢量拟合算法
- 频变网络等值
- 实时仿真

## 关键技术详解

- **宽频端口建模**：用于线路、电缆、变压器和外部网络的频域响应拟合。
- **无源性强制**：修正宽频模型中的非物理能量产生，保证 EMT 时域稳定。
- **PSCAD/EMTDC 工程模型**：为 HVDC、FACTS 和电力电子设备提供详细时域验证环境。
- **网络等值与模型降阶**：在保留端口行为的同时降低大系统 EMT 计算成本。

## 适用边界与注意事项

- Gole 相关方法多用于线性或线性化端口特性；对饱和、死区、控制限幅等强非线性，需要结合工作点、分段模型或时域非线性元件。
- 频域拟合精度和时域稳定性是两件事：曲线拟合得好不代表接入 EMT 网络后一定稳定。
- 论文引用 Gole 或 PSCAD 背景时，应看其具体贡献是工具、算法、模型验证还是工程应用。

## 开放问题

- 多端口宽频模型在大规模系统中如何兼顾拟合阶数、无源性和实时计算成本。
- 数据驱动模型与传统矢量拟合/无源性强制如何结合，处理含控制器的非线性电力电子设备。

## 所属机构
- [[university-manitoba]]
- [[manitoba-hydro]]

## 相关工具
- [[pscad-emtdc]]

## 相关方法
- [[vector-fitting]]
- [[passivity-enforcement]]

## 相关模型
- [[fdne-model]]
- [[transmission-line-model]]

## 相关论文

| 论文 | 年份 |
|------|------|
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 1999 |
| [[passivity-enforcement-for-transmission-line-models|Passivity enforcement for transmission line models]] | 2009 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2024 |
| [[reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in|Partitioning and optimizing the accuracy equation solving pr]] | 2026 |

## 代表性来源与内部链接

代表性来源包括 [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vector fitting]]、[[passivity-enforcement-for-transmission-line-models|Passivity enforcement for transmission line models]]、[[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and full perturbation form]] 和 [[reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in|Reduced-order and simultaneous solution of power and control system equations]]。阅读路径可从 [[pscad-emtdc]] 和 [[university-manitoba]] 进入，再连接 [[vector-fitting]]、[[passivity-enforcement]]、[[fdne-model]]、[[transmission-line-model]]、[[network-equivalent]] 和 [[real-time-simulation]]。
