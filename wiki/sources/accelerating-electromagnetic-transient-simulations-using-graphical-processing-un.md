---
title: "Accelerating electromagnetic transient simulations using graphical processing units"
type: source
authors: ['Devin Aluthge']
year: 2025
journal: "Electric Power Systems Research, 252 (2026) 112314. doi:10.1016/j.epsr.2025.112314"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf"]
---

# Accelerating electromagnetic transient simulations using graphical processing units

**作者**: Devin Aluthge
**年份**: 2025
**来源**: `05/Aluthge 等 - 2026 - Accelerating electromagnetic transient simulations using graphical processing units.pdf`

## 摘要

Accelerating electromagnetic transient simulations using graphical b Manitoba Hydro International, Winnipeg, MB, Canada This paper explores and evaluates various approaches to accelerate Electromagnetic Transient (EMT) sim- ulations of power systems using Graphical Processing Units (GPUs). Existing EMT simulation methods face computational challenges in systems with extensive renewable energy sources due to the complexity

## 核心贡献


- 提出全GPU驻留的EMT网络求解架构，彻底消除主机与设备间通信开销。
- 系统评估KLU、Cholesky及Woodbury公式在GPU稀疏求解器上的适配性。
- 针对含高频开关的大规模电网，实现高效稀疏导纳矩阵并行求解算法。


## 使用的方法


- [[klu分解|KLU分解]]
- [[cholesky分解|Cholesky分解]]
- [[woodbury公式|Woodbury公式]]
- [[补偿法|补偿法]]
- [[gpu稀疏求解|GPU稀疏求解]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[ieee-39节点系统|IEEE 39节点系统]]
- [[变压器|变压器]]
- [[同步发电机|同步发电机]]
- [[π型输电线路|π型输电线路]]
- [[逆变器接口电源|逆变器接口电源]]
- [[电力电子换流器|电力电子换流器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[gpu并行加速|GPU并行加速]]
- [[大规模电网仿真|大规模电网仿真]]
- [[高频开关动态|高频开关动态]]
- [[稀疏矩阵求解|稀疏矩阵求解]]
- [[新能源并网|新能源并网]]


## 主要发现


- cuDSS求解器在中小规模及万阶导纳矩阵测试中，计算耗时均显著低于CPU基准算法。
- GPU全驻留架构有效克服了频繁网络拓扑变化导致的矩阵重复分解瓶颈。
- 针对含大量电力电子设备的大规模系统，GPU方案可实现数量级的仿真提速。



## 方法细节

### 方法概述

本文提出了一种全GPU驻留的电磁暂态(EMT)仿真架构，旨在彻底消除CPU与GPU之间的数据传输与通信开销。该方法基于伴随电路理论将电网元件等效为电流源与电阻，构建实数导纳矩阵。通过系统评估KLU、Cholesky分解、Woodbury公式及补偿法，最终选定NVIDIA cuDSS稀疏求解器结合Cholesky分解作为核心网络求解引擎。算法利用CUDA内核并行处理同步发电机、无源元件及电流源的动态更新，并在每个时间步内完成右端向量组装。针对网络拓扑变化（如故障或高频开关动作），仅执行数值重分解而复用符号分解结构，从而在保证精度的前提下实现大规模、高开关频率电网的高效并行求解。

### 数学公式


**公式1**: $$$\mathbf{Y}(t)\mathbf{v}(t) = \mathbf{i}(t)$$$

*EMT网络节点电压求解基本方程，其中$\mathbf{Y}$为导纳矩阵，$\mathbf{v}$为节点电压向量，$\mathbf{i}$为注入电流向量。*


**公式2**: $$$(\mathbf{Y} + \mathbf{U}\mathbf{V}^T)^{-1} = \mathbf{Y}^{-1} - \mathbf{Y}^{-1}\mathbf{U}(\mathbf{I} + \mathbf{V}^T\mathbf{Y}^{-1}\mathbf{U})^{-1}\mathbf{V}^T\mathbf{Y}^{-1}$$$

*Woodbury矩阵求逆公式，用于在不重新分解整个矩阵的情况下，高效处理导纳矩阵中$k$个元素的局部变化。*


**公式3**: $$$\mathbf{Y} = \mathbf{L}\mathbf{L}^T$$$

*Cholesky分解公式，适用于对称正定(SPD)导纳矩阵，可将计算时间和内存需求降低约一半。*


### 算法步骤

1. 初始化仿真参数，在GPU上分配系统数据、导纳矩阵、电流和电压的内存空间，并将主机(CPU)数据拷贝至设备(GPU)。

2. 对导纳矩阵$\mathbf{Y}$执行符号分解以确定稀疏填充结构，随后在GPU上完成数值分解。

3. 进入时间步进循环，根据当前时间$t$判断同步发电机是否解锁转子动力学（$t<t_1$时锁定，$t \ge t_1$时启用）。

4. 调用并行CUDA内核：更新非动态电流源；基于上一时刻电压求解发电机模型方程；更新电感、电容等无源元件的历史电流项。

5. 组装网络方程的右端向量(RHS)，准备进行线性系统求解。

6. 检测故障或开关事件：若拓扑发生变化，更新导纳矩阵$\mathbf{Y}$并执行数值重分解（符号分解保持不变）；若无变化则跳过分解。

7. 利用前代回代法在GPU上求解节点电压向量。

8. 计算当前时间步无源元件的注入电流，时间步长递增($t \leftarrow t + dt$)，循环直至达到最大仿真时间。


### 关键参数

- **仿真步长**: 50 μs

- **测试矩阵规模**: 81×81, 10000×10000, 15618×15618

- **GPU硬件**: NVIDIA Tesla V100-PCIE-16GB

- **CPU硬件**: 14核 Intel Core i7 2.1 GHz, 32GB RAM

- **Woodbury变化量k**: 400 (对应100个网络开关变化)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 39节点系统 | 仿真时长101秒，步长50μs。GPU求解器耗时220秒，PSCAD/EMTDC耗时260秒。GPU代码在每个时间步均强制执行数值分解以模拟最恶劣的开关场景。 | GPU方案比PSCAD快约1.18倍（在最坏情况下仍具优势） |

| Texas 2000节点合成电网 | 仿真时长5秒，步长50μs，导纳矩阵规模15618×15618。GPU求解器总耗时51秒（单步510μs），PSCAD/EMTDC耗时2016秒（单步20.16ms）。 | GPU方案实现39.5倍的仿真加速 |

| 10000×10000稀疏矩阵求解基准测试 | cuDSS求解器（不含符号分解）耗时0.030 ms，MATLAB反斜杠算子耗时1302 ms，PARDISO耗时9000-18000 ms。 | cuDSS数值求解阶段比MATLAB快约43400倍，比PARDISO快30万至60万倍 |



## 量化发现

- 全GPU驻留架构彻底消除了主机与设备间的通信开销，使大规模网络求解延迟降至微秒级。
- cuDSS结合Cholesky分解在万阶及以上导纳矩阵求解中表现最优，数值求解耗时仅0.030 ms。
- Woodbury公式实现中，显式存储逆矩阵比存储分解因子快10倍，但当变化量k=400时，O(k^3)的稠密矩阵求逆成为性能瓶颈，整体效率不及cuDSS。
- 补偿法因需串行求解两个子网络互联方程且单时间步内需两次矩阵求解，其加速比未能超越cuDSS直接求解方案。
- 在Texas 2000节点系统中，GPU方案实现39.5倍加速，单步计算时间从20.16 ms降至510 μs。


## 关键公式

### EMT网络节点方程

$$$\mathbf{Y}(t)\mathbf{v}(t) = \mathbf{i}(t)$$$

*每个时间步求解电网节点电压的核心线性方程组*

### Woodbury矩阵恒等式

$$$(\mathbf{Y} + \mathbf{U}\mathbf{V}^T)^{-1} = \mathbf{Y}^{-1} - \mathbf{Y}^{-1}\mathbf{U}(\mathbf{I} + \mathbf{V}^T\mathbf{Y}^{-1}\mathbf{U})^{-1}\mathbf{V}^T\mathbf{Y}^{-1}$$$

*用于处理网络拓扑局部变化（如开关动作）时的导纳矩阵快速更新，避免全局重分解*

### Cholesky分解

$$$\mathbf{Y} = \mathbf{L}\mathbf{L}^T$$$

*针对对称正定导纳矩阵的分解方法，用于cuDSS求解器以降低计算复杂度和内存占用*



## 验证详情

- **验证方式**: 商业软件对比仿真验证
- **测试系统**: 双电源简单系统、IEEE 39节点系统、Texas 2000节点合成电网
- **仿真工具**: 自研GPU-EMT求解器（基于CUDA/cuDSS） vs PSCAD/EMTDC
- **验证结果**: 在双电源系统故障投切测试中，GPU求解器计算的节点3电压波形与PSCAD/EMTDC结果完全吻合（误差可忽略），验证了算法精度；在IEEE 39节点和2000节点系统中，GPU方案在保持精度的同时实现了显著的计算加速，尤其在最坏情况（每步重分解）下仍优于传统串行求解器。
