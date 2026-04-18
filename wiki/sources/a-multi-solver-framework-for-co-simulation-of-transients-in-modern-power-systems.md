---
title: "A multi-solver framework for co-simulation of transients in modern power systems"
type: source
authors: ['Janesh Rupasinghe']
year: 2023
journal: "Electric Power Systems Research, 223 (2023) 109659. doi:10.1016/j.epsr.2023.109659"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf"]
---

# A multi-solver framework for co-simulation of transients in modern power systems

**作者**: Janesh Rupasinghe
**年份**: 2023
**来源**: `02/Rupasinghe 等 - 2023 - A multi-solver framework for co-simulation of transients in modern power systems.pdf`

## 摘要

0378-7796/© 2023 Elsevier B.V. All rights reserved. A multi-solver framework for co-simulation of transients in modern Janesh Rupasinghe a, Shaahin Filizadeh b,*, Dharshana Muthumuni c, Ramin Parvari b b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada c Manitoba Hydro International, Winnipeg, MB R3P 1A3, Canada

## 核心贡献


- 提出融合EMT、BFAST、动态相量与暂态稳定求解器的多速率协同仿真框架
- 建立基于电气距离与动态特性的子系统划分准则及多接口交互算法
- 实现频率自适应的多速率仿真架构，兼顾大规模电网仿真精度与效率


## 使用的方法


- [[多速率仿真|多速率仿真]]
- [[动态相量法|动态相量法]]
- [[频率自适应暂态仿真|频率自适应暂态仿真]]
- [[暂态稳定求解|暂态稳定求解]]
- [[协同仿真接口技术|协同仿真接口技术]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[电力电子变换器|电力电子变换器]]
- [[平均值模型|平均值模型]]
- [[118节点测试系统|118节点测试系统]]


## 相关主题


- [[协同仿真|协同仿真]]
- [[多速率仿真|多速率仿真]]
- [[频率自适应仿真|频率自适应仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[暂态稳定|暂态稳定]]
- [[网络分区|网络分区]]


## 主要发现


- 在含MMC-HVDC的118节点系统中验证了框架的精度与计算效率优势
- 动态相量缓冲区有效隔离了EMT与暂态稳定求解器，提升了数值稳定性
- BFAST求解器能根据暂态频率自动切换步长，显著降低稳态计算耗时



## 方法细节

### 方法概述

提出一种多求解器、多速率协同仿真框架，将现代电网按设备类型、精度需求、扰动电气距离及研究目的划分为五类子系统：EMT1（高频暂态，微秒级步长）、EMT2（中频暂态，数十微秒步长）、BFAST（自适应切换EMT/动态相量）、DP（动态相量缓冲，大固定步长）和TS（暂态稳定，毫秒级正序步长）。框架以工业级PSCAD/EMTDC为核心，外部C++程序实现BFAST、DP和TS求解器。通过电气网络接口(ENI)、无损Bergeron传输线模型（显式耦合与延迟补偿）以及多区域戴维南等效(MATE)方法实现跨域接口交互。BFAST求解器基于基频动态相量(BFDP)理论，通过调节频移参数和步长在EMT与DP模式间自动切换，兼顾全频段精度与计算效率。

### 数学公式


**公式1**: $$$x(t - T + s) = \text{Re}\left( \langle X \rangle_B(t) e^{j\omega_s(t-T+s)} \right)$$$

*基频动态相量(BFDP)信号重构公式，将全谐波频谱压缩为单一频移相量，用于BFAST求解器的数学基础*


**公式2**: $$$Y = f(\Delta t, \omega_s)$$$

*网络节点导纳矩阵依赖关系式，表明导纳矩阵随仿真步长和频移参数动态变化，是模式切换的核心依据*


**公式3**: $$$h_M(t) = \frac{2v_K(t-\tau)}{Z_C} - h_K(t-\tau)$$$

*Bergeron传输线接口电流公式，用于EMT侧边界数据注入，利用波传播时间实现无延迟显式耦合*


**公式4**: $$$I_\alpha(i) = Z_\alpha^{-1} e_\alpha(i)$$$

*MATE方法联络支路电流计算公式，用于DP与TS子系统间的解耦并行求解，消除大时间步限制*


### 算法步骤

1. 在$t=t_k$时刻，独立求解TS子系统在$t_k$的局部解（不含联络支路）与DP子系统在中间时刻$t_i$的局部解。

2. 将TS子系统的局部解线性插值至$t_i$，并将正序相量转换为三相形式以匹配DP子系统的三相接口需求。

3. 基于DP与插值后的TS局部解，分别计算两子系统的戴维南等效电压，进而求解联络支路电流向量$I_\alpha(i) = Z_\alpha^{-1} e_\alpha(i)$。

4. 将计算得到的$I_\alpha(i)$注入DP子系统接口节点并独立求解完整状态，该过程在DP子系统的每个中间时刻$t_i$重复执行。

5. 到达$t=t_k$时，重新计算接口电流并同步注入DP与TS子系统，并行求解两子系统的完整网络状态，实现无时间步延迟的精确耦合。


### 关键参数

- **Δt_EMT1**: 10 μs

- **Δt_EMT2**: 50 μs

- **Δt_T (BFAST EMT模式)**: 50 μs

- **Δt_DP1 (BFAST DP模式)**: 200 μs

- **Δt_DP2**: 250 μs

- **Δt_TS**: 5 ms

- **MMC额定参数**: 230 kV, 300 MW, 直流母线400 kV, 每桥臂20个子模块, 子模块电容5 mF, 桥臂电感/电阻0.001 H/0.025 Ω



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 改进型IEEE 118节点系统（含MMC-HVDC）母线47处0.2秒单相接地故障 | 多求解器框架输出的EMT1、EMT2及BFAST子系统电压/电流波形与PSCAD/EMTDC全EMT基准仿真完全一致。BFAST在故障发生前自动由DP模式切换至EMT模式，故障清除后切回DP模式，暂态细节完整保留。切换后因波形含微小直流分量出现轻微振荡，但不影响整体精度。 | 10秒仿真耗时从基准全EMT的1126秒降至88秒（提速约12.8倍）；相比多速率全EMT仿真（358秒）提速约4.07倍。TS子系统步长(5 ms)为基准EMT步长(10 μs)的500倍。 |



## 量化发现

- 10秒仿真计算时间由1126 s大幅缩减至88 s，整体加速比达12.8倍。
- 相较于多速率纯EMT仿真（358 s），计算效率提升约4.07倍。
- TS求解器采用5 ms步长，为传统EMT步长(10 μs)的500倍，显著降低稳态计算负荷。
- 跨域接口波形误差基本不可察觉(essentially identical)，在Bergeron传输线接口下实现零时间步延迟补偿。
- BFAST求解器在暂态期间自动切换至50 μs步长，稳态期间切换至200 μs步长，模式切换响应无额外数值延迟。


## 关键公式

### BFDP频移变换公式

$$$\langle X \rangle_B(t) = \langle x \rangle_0(t) e^{-j\omega_s(t-T+s)} + 2 \sum_{k=1}^{+\infty} \langle x \rangle_k(t) e^{j(k-1)\omega_s(t-T+s)}$$$

*用于BFAST求解器在EMT与DP模式间切换的核心数学基础，通过设置$\omega_s=0$或$\omega_s=\omega_0$实现求解域转换*

### BFAST/DP侧Bergeron边界电流注入公式

$$$\langle h_K \rangle_B(t) = \left( \frac{2\langle v_M \rangle_B(t-\tau)}{Z_C} - \left( \frac{2\langle v_K \rangle_B(t-2\tau)}{Z_C} - \langle h_K \rangle_B(t-2\tau) \right) e^{-j\omega_s \tau} \right) e^{-j\omega_s \tau}$$$

*用于EMT与BFAST/DP求解器间的显式无延迟数据交互，补偿跨求解器通信与分区带来的时间步差异*

### MATE联络电流计算式

$$$I_\alpha(i) = Z_\alpha^{-1} e_\alpha(i)$$$

*用于DP与TS子系统解耦并行计算，消除传输线接口对大时间步的限制，支持毫秒级暂态稳定求解*



## 验证详情

- **验证方式**: 协同仿真对比验证（与PSCAD/EMTDC独立全EMT基准仿真进行波形与耗时对比）
- **测试系统**: 改进型IEEE 118节点测试系统（母线62发电机替换为300 MW MMC-HVDC系统）
- **仿真工具**: PSCAD/EMTDC（核心EMT求解器）、Microsoft Visual Studio C++（外部BFAST/DP/TS求解器）、内置协同仿真组件与MATE算法
- **验证结果**: 框架在含电力电子设备的复杂电网中实现了高精度暂态波形复现，跨求解器接口无显著数值误差或延迟；通过多速率分区与自适应求解策略，计算效率较传统全EMT提升超12倍，验证了多求解器架构在兼顾精度与大规模电网仿真效率方面的优越性。
