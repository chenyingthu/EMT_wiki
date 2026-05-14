---
title: "M3C 建模方法 (Modular Multilevel Matrix Converter)"
type: method
tags: [m3c, modular-multilevel-matrix-converter, lfac, converter-modeling, ac-ac]
created: "2026-05-05"
updated: "2026-05-10"
---

# M3C 建模方法 (Modular Multilevel Matrix Converter)


```mermaid
graph TD
    subgraph S0[M3C 建模方法 (M3C)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[常见建模方法]
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

M3C (Modular Multilevel Matrix Converter) 是一种九桥臂 AC/AC 直接变换结构，每个桥臂由子模块(半桥或全桥)串联构成，可在两侧不同频率的交流系统之间实现功率变换。M3C 常见于低频交流(LFAC)输电、异步交流系统互联和背靠背频率变换场景。

M3C 与普通 MMC 的核心区别:
- MMC 是 AC/DC 变换，直流侧为单极性; M3C 是 AC/AC 变换，两侧均为交流
- M3C 桥臂能量需在输入/输出两侧间同时平衡，控制复杂度更高
- M3C 需要处理两侧不同频率下的坐标变换和功率耦合

本页作为 M3C 建模方法入口，承接缩写型链接并说明其与普通 MMC、VSC 的建模边界。

## EMT 中的作用

M3C 建模通常用于分析:

- 模块化多电平矩阵换流器的桥臂动态和端口等效电路
- 不同频率交流系统之间的功率变换与能量平衡
- 低频交流(LFAC)系统中的控制策略和稳定性问题
- M3C 与常规 MMC/VSC 在拓扑、控制和等效模型上的差异
- LFAC 输电系统的潮流初始化与机电暂态仿真

## 常见建模方法

### 详细电磁暂态模型

完整保留每条桥臂的子模块开关状态、电容电压和桥臂电流。状态量规模为 9 桥臂 × N 子模块/桥臂，计算量随 N 线性增长。适用于开关谐波、子模块均压和内部环流分析。

### 平均值模型 (AVM)

将子模块电容电压等效为集中电容 $C_{eq} = 9N C_{SM}$，忽略子模块开关细节，保留桥臂级动态。适用于系统级 EMT 仿真和稳定性分析。

### 双 $\alpha\beta 0$ 变换解耦模型 [Yu 2023]

通过双重 $\alpha\beta 0$ 变换将 M3C 九桥臂变量解耦为输入侧和输出侧独立的等效电路: 输入侧 $\alpha\beta 0$ 变换将输出电压和电流映射至输入频率参考系; 输出侧变换映射至输出频率参考系。解耦后的桥臂微分方程为:

$$
L_0 \frac{d}{dt} \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + R_0 \begin{bmatrix} i_{V\alpha} \\ i_{V\beta} \end{bmatrix} + \frac{\sqrt{3}}{3} \begin{bmatrix} u_{0\alpha} \\ u_{0\beta} \end{bmatrix} = \frac{\sqrt{3}}{3} \begin{bmatrix} u_{V\alpha} \\ u_{V\beta} \end{bmatrix}
$$

### 正序基波相量模型 [Yu 2023]

结合准稳态假设和频率缩放，将 M3C 表示为正序基波相量域的等效电路。适用于 PSS/E 等机电暂态平台的大系统稳定性仿真。

## 关键公式

### 等效电容

$$
C_{eq} = 9N C_{SM}
$$

九桥臂子模块电容集中等效为单一电容，$N$ 为单桥臂子模块数，$C_{SM}$ 为单个子模块电容值。

### 能量守恒方程

$$
P_{sOut} = P_{sIn} - P_{loss}
$$

M3C 输入侧与输出侧有功功率通过桥臂损耗耦合，是迭代潮流计算的核心约束。

### VSG 构网控制同步环

$$
J \frac{d\omega_s}{dt} = \frac{1}{\omega_0}(P_{sref} - P_s) - D_d \omega_s
$$

虚拟同步机控制下 M3C 的功率同步环微分方程，$J$ 为虚拟惯量，$D_d$ 为阻尼系数。

### 多 VSG 去中心化功率分配

$$
P_{dis\_VSGi} = \frac{D_i}{\sum_{i=1}^k D_i} P_{mis}
$$

$$
f = f_{ref} - \frac{1}{\sum_{i=1}^k D_i} P_{mis}
$$

多个构网型 M3C 按阻尼系数比例分担不平衡功率，共同确定系统频率。

## 与相关方法的关系

- [[mmc-model]]: MMC 是 AC/DC 变换,M3C 是 AC/AC 变换; 两者共享多电平桥臂思想但端口拓扑和控制目标不同
- [[mbsm]]: 若页面使用多桥臂统一表示思路,可与 MBSM 框架关联
- [[vector-control]]: M3C 控制常需要多坐标系(输入/输出侧不同频率)或多频率控制组织
- [[virtual-synchronous-generator]]: M3C 可采用 VSG 控制实现去中心化构网运行
- [[electromechanical-transient]]: M3C 可在机电暂态尺度下等效为端口模型用于大系统研究
- [[multi-terminal-dc]]: M3C 虽然连接交流系统,但其多端功率交换特性可与 MTDC 系统对比
- [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular]]: M3C-LFAC 系统机电暂态建模的直接来源

## 适用边界与失败模式

### 适用条件

- LFAC 输电系统的 M3C 换流站建模与仿真
- 异步交流电网互联(如 50/60 Hz 与 16.7 Hz 或 20 Hz 系统)
- 背靠背 AC/AC 频率变换场景
- 含 M3C 的多机电力系统机电暂态稳定性分析

### 失效边界

- 若将 M3C 简化为普通 MMC 或 VSC,将丢失输入/输出侧频率耦合的核心特性
- EMT 尺度与机电暂态尺度的模型层级不同(Yu 2023 的 10ms 步长模型不适用于开关级谐波),不能跨层级外推结论
- 平均值模型和等效电容简化丢失了子模块电压纹波和内部环流信息,不适用于保护闭锁和均压分析
- Yu 2023 的验证约束于正序基波和机电暂态场景,未覆盖不平衡故障和电磁暂态细节

### 关键假设

- 双重 $\alpha\beta 0$ 变换解耦假设桥臂参数对称
- 准稳态近似假设输入/输出侧频率偏差在可接受范围内
- 机电暂态模型假设 M3C 内部动态可以等效为集中电容和端口阻抗

## 代表性来源

- [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular]]: 提出 M3C-LFAC 系统机电暂态建模完整框架,包含双重 $\alpha\beta 0$ 变换解耦、迭代潮流算法和 PSS/E 实现

## 数值证据汇总

| 参数 | 值 | 来源 |
|------|-----|------|
| 等效电容 | Ceq = 9N*Csm | Yu 2023 |
| 机电暂态步长 | 10 ms | Yu 2023 |
| 加速倍数(机/电磁) | ~200 倍 | Yu 2023 |
| 稳态误差 | < 1.5% | Yu 2023 |
| 暂态恢复时间误差 | < 3% | Yu 2023 |
| VSG阻尼系数分配 | Di/sum(Di) | Yu 2023 |
| 验证系统 | 双异步/39节点 | Yu 2023 |

## 开放问题

- M3C 在 EMT 尺度下的详细开关模型及其与机电暂态模型的接口
- 多 M3C 并联或 M3C 与 MMC 混合系统的协调控制
- M3C 内部环流和子模块电容电压平衡对系统级稳定性的影响

## 来源论文

| 论文 | 年份 |
|------|------|
| [[electromechanical-transient-modeling-of-the-low-frequency-ac-system-with-modular|Electromechanical Transient Modeling of the Low-Frequency AC]] | 2023 |
