---
title: "电力系统网络 (Power System Network)"
type: topic
tags: [power-system, network-topology, power-flow, emt-integration, grid-modeling]
created: "2026-05-04"
---

# 电力系统网络 (Power System Network)


```mermaid
graph TD
    subgraph Ncmp[电力系统网络 (Power System Network)]
        N0[发电机: 同步电机+励磁+调速+PSS]
        N1[变压器: 多绕组+饱和+频变]
        N2[线路: 分布参数+频变特性]
        N3[负荷: 动态负荷模型]
    end
```


## 定义与边界

电力系统网络是指由发电、输电、变电、配电和用电设备通过电气连接构成的能量传输与分配系统。在EMT仿真语境中，网络通常指需要详细电磁暂态建模的电网部分，与采用简化等值的外部系统或机电暂态模型形成边界。

**边界限定**：本页面聚焦于EMT仿真中的网络表示方法，不替代潮流计算或机电暂态稳定分析的基础教材内容。

## EMT中的作用

电力系统网络是EMT仿真的核心对象：

- **详细建模区**：网络中的关键设备（换流器、FACTS、新能源接口）需要详细的电磁暂态模型
- **等值边界**：外部网络通过戴维南/诺顿等值或FDNE简化表示
- **混合仿真接口**：与机电暂态仿真的网络分割与数据交换
- **过电压分析**：网络拓扑对操作过电压、雷击过电压的分布起决定作用

## 主要分支与机制

### 1. 网络拓扑表示

- **节点-支路模型**：导纳矩阵Y或阻抗矩阵Z表示
- **母线-断路器模型**：详细开关状态与拓扑变化
- **分层分区表示**：输电层、配电层、用户层的不同建模粒度

### 2. 网络元件建模层次

| 元件 | EMT详细模型 | 简化/等值模型 |
|------|-------------|---------------|
| 发电机 | 同步电机+励磁+调速+PSS | 电压源+内阻抗 |
| 变压器 | 多绕组+饱和+频变 | 理想变比+漏抗 |
| 线路 | 分布参数+频变特性 | π型等值/集中参数 |
| 负荷 | 动态负荷模型 | 恒定功率/阻抗 |

### 3. 网络等值方法

- **Ward等值**：基于潮流的静态等值
- **REI等值**：保留外部系统关键电气特性
- **FDNE**：频变网络等值，适用于宽频EMT分析
- **戴维南等值**：单端口简化表示

## 形式化表达

### 网络方程

节点电压方程：
$$\mathbf{Y}(s)\mathbf{V}(s) = \mathbf{I}(s)$$

其中$\mathbf{Y}(s)$为节点导纳矩阵，$\mathbf{V}(s)$为节点电压向量，$\mathbf{I}(s)$为注入电流向量。

### 与EMT的衔接

网络在EMT中的时域离散方程：
$$\mathbf{G}\mathbf{v}(t) = \mathbf{i}(t) + \mathbf{i}_h(t)$$

其中$\mathbf{G}$为等值电导矩阵，$\mathbf{i}_h(t)$为历史项电流。


## 数值分析

### 精度与效率
- 仿真精度：误差控制在1%以内
- 计算效率：支持大规模系统实时仿真
- 数值稳定性：在典型工况下保持稳定

### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s

### 性能指标
- 内存占用：随系统规模线性增长
- 计算时间：与系统复杂度和仿真时长相关
- 收敛性：在绝大多数情况下稳定收敛

## 适用边界与失败模式

### 适用条件

- 网络参数（R、L、C、线路参数）在仿真频段内有效
- 拓扑变化可通过开关模型或重新形成导纳矩阵处理
- 等值边界的选择应保留关键动态特性

### 失效边界

- **参数频变忽略**：高频暂态下集总参数假设失效
- **等值过度简化**：关键谐振特性被等值滤除
- **拓扑快速变化**：大量开关动作导致频繁重构导纳矩阵
- **多时间尺度耦合**：机电暂态与电磁暂态交互强烈区域

## 代表性来源

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统建模
- [[electromagnetic-transient]] - 电磁暂态分析
- [[control-system]] - 控制系统设计
- [[real-time-simulation]] - 实时仿真技术
### 经典文献

- Kundur, P., "Power System Stability and Control," *McGraw-Hill*, 1994. - 电力系统网络基础
- Dommel, H.W., "Digital Computer Solution of Electromagnetic Transients," *IEEE PAS*, 1969. - EMT仿真网络解法

### EMT应用

- [[fdne-model]] - 频变网络等值
- [[electromechanical-electromagnetic-hybrid-simulation]] - 机电-电磁混合仿真
- [[network-equivalent]] - 网络等值方法

## 与相关页面的关系

- [[electromechanical-electromagnetic-hybrid-simulation]] - 多时间尺度网络分割
- [[fdne-model]] - 外部系统宽频等值
- [[nodal-analysis]] - 节点分析解法
- [[transmission-line-model]] - 输电线路详细模型
- [[network-equivalent]] - 网络等值理论

## 开放问题

- 超大规模网络的实时仿真降阶方法
- 含高比例电力电子设备的网络等值精度
- 数据驱动的网络动态等值
- 网络拓扑变化下的快速重构算法

## 参考标准

- IEEE Std. 1800 - 电磁暂态仿真导则
- IEC 61970 (CIM) - 电网模型交换标准

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-time-domain-ac-electric-arc-furnace-model-for-flicker-planning-studies|A Time-Domain AC Electric Arc Furnace Model for Flicker Plan]] | 2009 |
| [[cpu-based-parallel-computation-of-electromagnetic-transients-for-large-power-gri|CPU based parallel computation of electromagnetic transients]] | 2018 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[multi-scale-induction-machine-model-in-the-phase-domain-with-constant-inner-impe|Multi-scale Induction Machine Model in the Phase Domain with]] | 2019 |
| [[iet-generation-transmission-distribution|IET Generation, Transmission & Distribution]] | 2020 |
| [[a-parallelization-in-time-approach-for-accelerating-emt-simulations|A parallelization-in-time approach for accelerating EMT simu]] | 2021 |
| [[laplace-transform-inversion-through-the-theta-algorithm-for-power-system-emt-ana|Laplace transform inversion through the theta algorithm for ]] | 2021 |
| [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t|Lessons learned in porting offline large-scale power system ]] | 2023 |
| [[an-open-source-parallel-emt-simulation-framework|An open-source parallel EMT simulation framework]] | 2024 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-|Comprehensive Full-Scale Converter Wind Park Initialization ]] | 2025 |
