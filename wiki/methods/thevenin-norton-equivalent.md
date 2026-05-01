---
title: "戴维南-诺顿等效 (Thevenin-Norton Equivalent)"
type: method
tags: [equivalent-circuit, thevenin, norton, port-model, network-reduction]
created: "2026-04-30"
---

# 戴维南-诺顿等效 (Thevenin-Norton Equivalent)

## 定义与概述

戴维南-诺顿等效是电磁暂态仿真中网络简化的核心技术，通过将复杂子网络等效为端口处的电压源串联电阻（戴维南）或电流源并联电导（诺顿），大幅降低系统方程维度。在EMT仿真中，该技术广泛应用于同步机接口、MMC桥臂建模、变压器端口等效和子系统解耦，是实现大规模电网高效仿真的基础方法。

## 1. 理论基础

### 1.1 戴维南等效

**单端口戴维南等效**:
$$v(t) = v_{th}(t) + R_{th} \cdot i(t)$$

其中：
- $v_{th}(t)$: 开路电压（历史项）
- $R_{th}$: 等效电阻
- $i(t)$: 端口电流

**多端口扩展**:
$$\mathbf{v}(t) = \mathbf{v}_{th}(t) + \mathbf{R}_{th} \cdot \mathbf{i}(t)$$

### 1.2 诺顿等效

**单端口诺顿等效**:
$$i(t) = i_{N}(t) + G_{N} \cdot v(t)$$

其中：
- $i_{N}(t)$: 短路电流（历史项）
- $G_{N}$: 等效电导

**与戴维南的转换关系**:
$$G_{N} = R_{th}^{-1}, \quad i_{N}(t) = -G_{N} \cdot v_{th}(t)$$

### 1.3 离散时域等效

**梯形积分法离散**:
$$v(t) = R_{eq} \cdot i(t) + e_{hist}(t-\Delta t)$$

其中等效电阻:
$$R_{eq} = \frac{2L}{\Delta t} \quad \text{(电感支路)}$$
$$R_{eq} = R + \frac{\Delta t}{2C} \quad \text{(阻容支路)}$$

历史项:
$$e_{hist}(t-\Delta t) = v(t-\Delta t) + R_{eq} \cdot i(t-\Delta t)$$

## 2. EMT仿真应用

### 2.1 同步机接口（MANA-T）

**相域(PD)模型等效**:
$$\mathbf{v}_{abc} = -\mathbf{R}_{abc}^{PD} \cdot \mathbf{i}_{abc} + \mathbf{e}_{abc}^{PD}$$

等效电阻矩阵:
$$\mathbf{R}_{abc}^{PD} = \mathbf{R}_{ss} + \frac{2}{\Delta t}\mathbf{L}_{ss}(\theta)$$

**电抗后电压(VBR)模型等效**:
$$\mathbf{v}_{abc} = -(\mathbf{R}_{s} + k\mathbf{L}_{abc}''(\theta))\mathbf{i}_{abc} + \mathbf{v}_{abc}'' + \mathbf{h}_{svbr}$$

其中 $k = 2/\Delta t$。

### 2.2 MMC桥臂等效

**单个子模块等效**:
$$i_{SM}(t) = \frac{1}{R_{SMeq}}v_{arm}(t) + I_{SMH}$$

**桥臂级合并等效**:
$$i_{SUM} = \frac{1}{R_{ARMeq}}v_{arm}(t) + I_{ARMH}$$

其中:
$$\frac{1}{R_{ARMeq}} = \sum_{i=1}^{N} \frac{1}{R_{SMeq,i}}$$
$$I_{ARMH} = \sum_{i=1}^{N} I_{SMH,i}$$

### 2.3 变压器端口等效

**高频变压器模型**:
$$\mathbf{v}(t) = \mathbf{R}_{eq}\mathbf{i}(t) + \mathbf{e}_{hist}(t-\Delta t)$$

等效电阻矩阵通过有理函数逼近获得:
$$\mathbf{Z}(s) = \mathbf{D} + s\mathbf{E} + \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s-p_k}$$

## 3. 实现技术

### 3.1 MANA框架集成

**改进增广节点分析法**:

将等效电路直接嵌入网络方程:
$$\begin{bmatrix} \mathbf{Y}_{nn} & \mathbf{Y}_{nm} \\ \mathbf{Y}_{mn} & \mathbf{Y}_{mm} \end{bmatrix} \begin{bmatrix} \mathbf{v}_n \\ \mathbf{v}_m \end{bmatrix} = \begin{bmatrix} \mathbf{i}_n \\ \mathbf{i}_m \end{bmatrix} + \begin{bmatrix} \mathbf{j}_n \\ \mathbf{j}_m \end{bmatrix}$$

其中设备方程作为附加行/列直接参与求解。

### 3.2 局部重分解优化

**矩阵分块策略**:
$$\begin{bmatrix} \mathbf{A}_{11} & \mathbf{A}_{12} \\ \mathbf{A}_{21} & \mathbf{A}_{22} \end{bmatrix} \begin{bmatrix} \mathbf{x}_1 \\ \mathbf{x}_2 \end{bmatrix} = \begin{bmatrix} \mathbf{b}_1 \\ \mathbf{b}_2 \end{bmatrix}$$

- $\mathbf{A}_{11}$: 恒定网络部分（一次分解，重复使用）
- $\mathbf{A}_{22}$: 时变设备部分（每步局部重分解）

**性能提升**:
- PD/VBR模型计算速度提升 **2.5~3倍**
- 30机系统仿真时间增加仅 **20%**（传统方法>200%）

### 3.3 稀疏矩阵求解

**KLU求解器集成**:
- 近似最小度(AMD)排序
- 块三角形式(BTF)分解
- Gilbert-Peierls左视算法

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

```fortran
! 戴维南等效接口
! 计算等效电阻
REQ = 2.0 * L / DT

! 计算历史电压源
EHIST = V_OLD + REQ * I_OLD

! 注入节点方程
V_NODE = (I_INJ + EHIST/REQ) / (G_NODE + 1.0/REQ)

! 更新支路电流
I_BRANCH = (V_NODE - EHIST) / REQ
```

### 4.2 MATLAB实现

```matlab
function [v_port, i_update] = thevenin_equivalent(i_port, params)
    % 戴维南等效计算
    Req = params.Req;
    v_hist = params.v_hist;
    
    % 端口电压
    v_port = v_hist + Req * i_port;
    
    % 更新历史项（梯形积分）
    i_update = i_port;
    v_hist_new = v_port + Req * i_port;
    params.v_hist = v_hist_new;
end

function [i_port, v_update] = norton_equivalent(v_port, params)
    % 诺顿等效计算
    Geq = params.Geq;
    i_hist = params.i_hist;
    
    % 端口电流
    i_port = i_hist + Geq * v_port;
    
    % 更新历史项
    v_update = v_port;
    i_hist_new = i_port + Geq * v_port;
    params.i_hist = i_hist_new;
end
```

## 5. 典型参数参考

| 应用场景 | 等效电阻范围 | 历史项更新频率 | 性能提升 |
|----------|-------------|---------------|----------|
| 同步机PD模型 | 0.1-10 Ω | 每步 | 2.5-3倍 |
| MMC桥臂(400SM) | 0.001-0.1 Ω | 每步 | 10-15倍 |
| 变压器高频模型 | 1-1000 Ω | 每步 | 5-10倍 |
| 线路分布参数 | 10-500 Ω | 每步 | 2-3倍 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[synchronous-machine-model|同步电机模型]] - MANA-T接口应用
- [[mmc-model|MMC模型]] - 桥臂等效建模
- [[transformer-model|变压器模型]] - 高频端口等效
- [[fdne-model|FDNE模型]] - 频变网络等值

### 6.2 相关方法
- [[nodal-analysis|节点分析]] - 网络方程基础
- [[numerical-integration|数值积分]] - 梯形法离散
- [[state-space-method|状态空间法]] - 设备方程建模
- [[fixed-admittance|恒导纳模型]] - 等效导纳实现

### 6.3 相关主题
- [[real-time-simulation|实时仿真]] - 计算效率优化
- [[parallel-computing|并行计算]] - 矩阵求解加速
- [[network-equivalent|网络等值]] - 系统级简化

## 7. 适用边界与限制

### 7.1 适用条件
- **线性网络**: 等效前网络应为线性时不变或分段线性
- **端口定义**: 明确等效端口位置
- **时间步长**: 等效参数与仿真步长相关

### 7.2 失效边界
- **强非线性**: 饱和、电弧等非线性难以精确等效
- **宽频暂态**: 极高频率下分布参数效应显著
- **多物理耦合**: 热-电-磁耦合需保留内部细节

### 7.3 精度边界
| 应用场景 | 稳态误差 | 暂态误差 | 适用频段 |
|----------|---------|---------|----------|
| 同步机接口 | <0.1% | <1% | DC-1kHz |
| MMC等效 | <0.5% | <1.5% | DC-5kHz |
| 变压器高频 | <3% | <5% | DC-1MHz |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Partial refactorization based machine modeling for EMT | 2016 | MANA-T局部重分解，PD/VBR模型加速 |
| Efficient modeling of modular multilevel HVDC | 2010 | MMC桥臂诺顿等效，10-15倍加速 |
| Average-Value Models for MMC in VSC-HVDC grids | 2014 | AVM等效建模，直流故障精度改进 |
| A transformer model for winding fault studies | 2004 | 变压器故障等效建模 |

## 相关模型

- [[synchronous-machine-model|同步电机模型]] - MANA-T接口应用
- [[mmc-model|MMC模型]] - 桥臂等效建模
- [[transformer-model|变压器模型]] - 高频端口等效
- [[fdne-model|FDNE模型]] - 频变网络等值
- [[vsc-model|VSC模型]] - 变流器等效电路

## 相关主题

- [[real-time-simulation|实时仿真]] - 计算效率优化
- [[parallel-computing|并行计算]] - 矩阵求解加速
- [[network-equivalent|网络等值]] - 系统级简化
- [[co-simulation|混合仿真]] - 接口等值应用

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*
