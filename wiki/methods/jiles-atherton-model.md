---
title: "Jiles-Atherton 磁滞模型"
type: method
tags: [jiles-atherton, hysteresis, transformer, magnetic-saturation, ferromagnetic, emtp]
created: "2026-05-10"
---

# Jiles-Atherton 磁滞模型

## 定义与边界

Jiles-Atherton（JA）磁滞模型是一种基于磁畴物理的铁磁材料磁滞回线解析模型，在 EMT 仿真中用于表示变压器、电抗器等铁芯设备的磁滞特性。与分段线性或单值励磁曲线不同，JA 模型能够描述磁化历史依赖、主/次磁滞回线以及动态铁损变化，对铁磁谐振等磁滞敏感暂态问题至关重要。

本页关注 JA 模型在 EMT 程序中的实现接口（\(\psi-i\) 形式）、动态损耗耦合方法及其与电路求解的集成。相关变压器建模基础见 [[transformer-model]]；铁磁谐振见 [[ferroresonance]]；基本磁化特性见 [[magnetic-saturation-modeling]]。

## EMT 中的作用

常规 EMT 变压器/电抗器模型通常使用单值饱和曲线，无法反映磁化历史。JA 模型在 EMT 中的价值在于：

- **磁滞记忆**：保留铁芯的磁化历史，区分增磁和退磁路径，生成主回线和次回线。
- **铁损动态**：将铁损（涡流损耗 + 剩余损耗）与电压激励耦合，而非仅并联固定电阻。
- **铁磁谐振**：磁滞回线和动态损耗共同决定可能的谐振运行点，单值曲线可能丢失关键暂态路径。
- **直流偏磁**：可模拟变压器因地磁感应电流或 HVDC 单极运行导致的偏磁饱和。

## 核心机制

### 磁学到电路变量的转换

JA 模型以磁学量表述，需转换为 EMT 电路接口量：

$$
\psi = NAB = NA\mu_0(H + M), \quad i = \frac{H l}{N}, \quad v = \frac{d\psi}{dt}
$$

其中 \(\psi\) 为磁链，\(i\) 为电流，\(N\) 为匝数，\(A\) 为铁芯截面积，\(l\) 为磁路长度。这样 JA 模型对外表现为一个具有历史相关 \(\psi-i\) 特性的非线性支路。

### JA 微分方程

有效磁场：

$$
H_e = H + \alpha M
$$

无磁滞磁化（采用 Langevin 函数或修正形式）：

$$
M_{\text{an}} = M_s \left[ \coth\left(\frac{H_e}{a}\right) - \frac{a}{H_e} \right]
$$

磁化率微分方程：

$$
\frac{dM}{dH} = \frac{M_{\text{an}} - M}{\delta k - \alpha(M_{\text{an}} - M)} + c \frac{dM_{\text{an}}}{dH}
$$

其中 \(\delta = \text{sign}(dH/dt)\) 决定增磁/退磁方向，\(k\) 为磁畴钉扎参数，\(c\) 为可逆磁化系数，\(\alpha\) 为畴间耦合系数。该方程决定了每个时间步磁链随电流变化的轨迹，使模型能区分增磁与退磁路径。

### 动态损耗耦合

静态 JA 模型给出 \(\psi-i\) 磁滞关系后，还需加入电压驱动的动态损耗（涡流和剩余损耗）：

$$
i_{\text{total}} = i_{\text{hysteresis}} + i_{\text{eddy}} + i_{\text{excess}}
$$

涡流损耗分量正比于磁链变化率：

$$
i_{\text{eddy}} = \frac{1}{R_e} \frac{d\psi}{dt}
$$

其中 \(R_e\) 为等效涡流电阻。动态损耗的引入使模型可反映铁损随激励电压变化的物理特性。

### EMTP 实现接口

在 EMTP-ATP 中，JA 模型通过 Type-94 控制元件实现：静态 \(\psi-i\) 磁滞关系用自定义模型描述，动态损耗由端电压驱动加入。每个时间步的执行顺序为：

1. 从当前端电压更新 \(d\psi/dt\)
2. 计算动态损耗电流分量
3. 根据当前电流方向确定 \(\delta\)
4. 更新 JA 微分方程求 \(dM/dH\)
5. 迭代求解 \(\psi-i\) 工作点

## 相关方法

- [[magnetic-saturation-modeling]] — 磁饱和基本概念
- [[companion-circuit]] — 非线性支路的 EMT 离散化
- [[numerical-integration]] — 含磁滞的刚性系统积分

## 相关模型

- [[transformer-model]] — 变压器 EMT 模型
- [[induction-machine-model]] — 感应电机模型（含铁芯饱和）

## 相关主题

- [[ferroresonance]]
- [[transformer-modeling]]
- [[power-electronic-device-modeling]]

## 代表性来源

- Sima 等 — Saturable reactor hysteresis model based on Jiles–Atherton formulation for ferroresonance studies (2018)
- Velásquez — On-site measurement of the hysteresis curve for improved modelling of transformers (2023)
- 多篇变压器铁磁谐振与 J-A 参数辨识相关论文