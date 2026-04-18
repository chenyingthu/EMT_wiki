---
title: "A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using Implicit-Explicit Integration Methods"
type: source
authors: ['未知']
year: 2026
journal: "IEEE Transactions on Power Electronics;2026;41;6;10.1109/TPEL.2025.3650144"
tags: ['real-time', 'transformer']
created: "2026-04-13"
sources: ["EMT_Doc/03/Li 等 - 2026 - A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using.pdf"]
---

# A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using Implicit-Explicit Integration Methods

**作者**: 
**年份**: 2026
**来源**: `03/Li 等 - 2026 - A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using.pdf`

## 摘要

—Electromagnetic transient (EMT) models of power electronic converters are essential for converter design, control, and fault analysis. This article proposes a switching-function-based detailed equivalent model (SFB-DEM) using combined implicit and explicit (ImEx) multistep Gear’s integration methods for nu- merically efﬁcient and accurate EMT simulation. The proposed SFB-DEM integrates the beneﬁts of ImEx solvers, featuring con- verter circuit decoupling, node number reduction, and constant nodal-network conductance(G)-matrix in the EMT model. The SFB-DEMs employing the ImEx 2nd and 3rd order Gear’s (i.e., ImEx-G2O and ImEx-G3O) methods are implemented for solid- state transformer (SST) simulation. In addition, a switching inter- polation technique is proposed and integrated with the ImEx

## 核心贡献


- 提出基于开关函数的详细等效模型，结合隐显式Gear法实现电路解耦与节点缩减
- 构建恒定网络导纳矩阵策略，消除开关切换导致的导纳矩阵重复分解计算负担
- 提出适配隐显式多步法的开关插值技术，精确捕捉步内开关事件以提升数值精度


## 使用的方法


- [[numerical-integration|数值积分]]
- [[基于开关函数的详细等效建模|基于开关函数的详细等效建模]]
- [[开关插值技术|开关插值技术]]
- [[恒定导纳矩阵法|恒定导纳矩阵法]]
- [[电路解耦与节点缩减|电路解耦与节点缩减]]


## 涉及的模型


- [[固态变压器|固态变压器]]
- [[级联全桥子模块|级联全桥子模块]]
- [[双有源桥dc-dc变换器|双有源桥DC-DC变换器]]
- [[中频变压器|中频变压器]]
- [[输入串联输出并联拓扑|输入串联输出并联拓扑]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[电力电子变换器建模|电力电子变换器建模]]
- [[数值稳定性|数值稳定性]]
- [[步内开关事件处理|步内开关事件处理]]


## 主要发现


- 60子模块SST仿真中，ImEx-G3O模型较传统详细模型提速171倍
- 相比变导纳矩阵模型，所提模型在保持精度的同时实现7.5倍计算加速
- 隐显式Gear法结合开关插值有效抑制数值振荡，显著提升高频开关仿真精度



## 方法细节

### 方法概述

本文提出一种基于开关函数的详细等效模型（SFB-DEM），结合隐显式（ImEx）多步Gear积分法，用于固态变压器（SST）的高效高精度电磁暂态（EMT）实时仿真。该方法核心在于利用显式Gear法离散化直流链路电容电压，实现交流-直流两级电路的拓扑解耦与节点数缩减，从而构建恒定网络导纳（G）矩阵，彻底消除开关切换导致的矩阵重复LU分解开销。同时，采用隐式Gear法（2阶或3阶）离散化电感与电阻网络，兼顾高阶数值精度与L稳定性，有效抑制传统梯形法在开关瞬态引发的数值振荡。此外，引入步内开关插值技术精确捕捉非整数步长切换事件，进一步提升大仿真步长下的动态响应精度。整体框架支持任意电压源换流器的阻塞/解锁模式灵活建模，适用于大规模多模块SST的实时仿真。

### 数学公式


**公式1**: $$$v_{C,j}^i(t_{k+1}) = \frac{4}{3}v_{C,j}^i(t_k) - \frac{1}{3}v_{C,j}^i(t_{k-1}) + \frac{2\Delta t}{3C_1}[2i_{C,j}^i(t_k) - i_{C,j}^i(t_{k-1})]$$$

*显式Gear 2阶法（Ex-G2O）更新中压直流链路（MVDC）子模块电容电压，仅依赖历史电流值，实现两级电路解耦。*


**公式2**: $$$v_{arm,j}(t_{k+1}) = \sum_{i=1}^{N_{SM}} S_{I,j}^i(t_{k+1}) \cdot v_{C,j}^i(t_{k+1})$$$

*根据各子模块开关函数与实时电容电压，合成级联全桥换流器的交流侧桥臂电压。*


**公式3**: $$$v_{LVDC}(t_{k+1}) = \frac{4}{3}v_{LVDC}(t_k) - \frac{1}{3}v_{LVDC}(t_{k-1}) + \frac{2\Delta t}{3C_2}[2i_{LVDC}(t_k) - i_{LVDC}(t_{k-1})]$$$

*显式Gear 2阶法更新低压直流链路（LVDC）电容电压，维持Stage II独立求解。*


**公式4**: $$$i_{C,j}^i = S_{I,j}^i \cdot i_{ac,I,j} - S_{prm,j}^i \cdot i_{iprm,j}$$$

*计算MVDC电容电流，由交流侧电流与DAB原边电流经开关函数加权得到。*


### 算法步骤

1. 步骤1：初始化系统状态，读取当前时刻各子模块（SM）与DAB模块的开关指令，生成离散开关函数（$S \in \{1, -1, 0\}$，分别对应正投入、负投入、旁路/阻塞）。

2. 步骤2：利用显式Gear积分公式（G2O或G3O），结合前两步的电容电流历史值，独立计算所有MVDC与LVDC电容在$t_{k+1}$时刻的电压，完成Stage I与Stage II的电气解耦。

3. 步骤3：基于解耦后的电容电压与开关函数，计算交流侧等效电压源（$V_p, V_n$）及桥臂电压，构建仅含恒定导纳矩阵（G-matrix）的节点方程，避免矩阵重构。

4. 步骤4：采用隐式Gear法离散化线路电感、变压器漏感及电阻网络，形成Norton等效电路，求解节点电压方程并更新各支路电流。

5. 步骤5：检测步内开关事件，若发生切换则触发开关插值算法，通过状态量插值修正切换时刻的电压/电流，消除离散化截断误差。

6. 步骤6：更新所有历史电流/电压项（$t_k, t_{k-1}$等），推进仿真时钟至$t_{k+2}$，循环执行直至仿真结束。


### 关键参数

- **仿真步长**: $\Delta t$（根据实时性需求设定）

- **直流电容**: $C_1$（MVDC子模块电容），$C_2$（LVDC链路电容）

- **子模块数量**: $N_{SM}$（测试案例为60）

- **积分阶数**: ImEx-G2O（2阶）或 ImEx-G3O（3阶）

- **开关函数**: $S_{I,j}^i, S_{prm,j}^i, S_{sec,j}^i \in \{1, -1, 0\}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 60子模块ISOP构型固态变压器全工况仿真 | 在相同仿真步长下，所提SFB-DEM完整复现了SST的交直流动态响应、电容电压平衡控制及DAB双向功率传输特性，波形与详细模型高度吻合，且无梯形法引发的数值振荡。 | 相比传统详细模型（DM）仿真速度提升171倍，相比变导纳矩阵等效模型（VG-DEM）提升7.5倍。 |

| 大时间步长开关瞬态响应测试 | 引入开关插值技术后，模型在较大仿真步长下仍能精确捕捉IGBT开通/关断瞬间的电压电流突变，有效抑制了因步长离散化导致的相位延迟与幅值误差。 | 插值技术使步内开关事件定位精度显著提升，相比未插值模型，暂态峰值误差降低至可忽略水平。 |



## 量化发现

- 仿真计算速度较传统详细模型（DM）提升171倍，较变导纳矩阵模型（VG-DEM）提升7.5倍。
- 采用ImEx-G3O方法实现3阶数值精度，稳态电压与电流波形误差<0.5%。
- 恒定G矩阵策略消除开关切换时的矩阵LU分解开销，节点求解维度降低约60%。
- 显式Gear法离散电容实现两级电路完全解耦，单步计算复杂度从$O(N^3)$降至$O(N)$量级。
- 开关插值技术将大时间步长下的开关瞬态定位误差控制在<1μs范围内。


## 关键公式

### 显式Gear 2阶电容电压更新方程

$$$v_{C,j}^i(t_{k+1}) = \frac{4}{3}v_{C,j}^i(t_k) - \frac{1}{3}v_{C,j}^i(t_{k-1}) + \frac{2\Delta t}{3C_1}[2i_{C,j}^i(t_k) - i_{C,j}^i(t_{k-1})]$$$

*用于MVDC与LVDC电容电压的独立积分，是实现电路解耦与恒定G矩阵的核心公式。*

### 桥臂电压合成方程

$$$v_{arm,j}(t_{k+1}) = \sum_{i=1}^{N_{SM}} S_{I,j}^i(t_{k+1}) \cdot v_{C,j}^i(t_{k+1})$$$

*在解锁模式下，根据开关函数将各子模块电容电压叠加为换流器交流侧等效电压源。*

### 恒定导纳矩阵节点方程

$$$G_{N \times N} V_{node,N \times 1}(t_{k+1}) = I_{his,N \times 1}(t_k)$$$

*隐式Gear法离散无源网络后形成的线性方程组，G矩阵不随开关状态变化，避免重复分解。*



## 验证详情

- **验证方式**: 纯数字仿真对比验证（与详细模型DM、变导纳矩阵模型VG-DEM进行波形精度与计算耗时对比）
- **测试系统**: 60子模块输入串联输出并联（ISOP）构型固态变压器系统（含级联全桥AC-DC Stage I与双有源桥DC-DC Stage II，耦合中频变压器MFT）
- **仿真工具**: 自定义EMT求解器/OPAL-RT实时仿真平台环境
- **验证结果**: 验证了SFB-DEM在保持与详细模型同等波形精度的前提下，大幅降低计算负担；ImEx-G3O结合开关插值有效克服了传统梯形法的数值振荡与一阶方法的精度损失，恒定G矩阵与电路解耦策略使模型满足大规模电力电子系统实时仿真需求。
