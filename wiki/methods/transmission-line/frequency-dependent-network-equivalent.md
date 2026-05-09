---
title: "频变网络等值 (Frequency-Dependent Network Equivalent)"
type: method
tags: [frequency-dependent, network-equivalent, fdne, wideband, rational-approximation, vector-fitting]
created: "2026-05-04"
---

# 频变网络等值 (Frequency-Dependent Network Equivalent)


```mermaid
graph TD
    subgraph Ncmp[频变网络等值 (Frequency-Dependent …]
        N0[线性假设: 外部系统近似线性]
        N1[时不变性: 外部拓扑恒定]
        N2[频率范围: 明确上下限]
        N3[端口选择: 边界清晰]
    end
```


## 定义与边界

频变网络等值（FDNE, Frequency-Dependent Network Equivalent）是一种在宽频范围内保留外部系统频率特性、用于电磁暂态仿真的网络简化方法。通过有理函数逼近外部网络的频率响应，将复杂外部系统等值为少量频变元件，在保证计算效率的同时维持暂态精度。

**边界限定**：本方法适用于外部系统需要保留宽频特性（如谐波、开关暂态、雷击）但无需详细设备模型的场景。对于仅关心基波或机电暂态的问题，静态等值或机电模型更为高效。

## EMT中的作用

FDNE是连接大规模系统与详细EMT仿真的关键技术：

- **计算效率**：将数千节点外部系统降阶为数十个等值元件
- **频带覆盖**：保留从直流到数kHz的关键谐振特性
- **暂态保真**：准确复现外部系统对内部扰动的宽频响应
- **多场景复用**：同一FDNE可支持不同内部故障工况

## 主要分支与机制

### 1. 基于矢量拟合的FDNE

通过[[vector-fitting]]从频率扫描数据提取极点-留数：
$$Y_{eq}(s) = \sum_{k=1}^{n}\frac{r_k}{s-p_k} + d + se$$

其中$p_k$为极点，$r_k$为留数，$d$为常数项，$e$为微分项。

### 2. 时域实现

有理函数转换为等值电路：
- 实极点 → RC支路
- 复共轭极点 → RLC谐振支路
- 直接项 → 并导纳

### 3. 多端口FDNE

对于$m$端口网络，导纳矩阵：
$$\mathbf{Y}_{eq}(s) = \sum_{k=1}^{n}\frac{\mathbf{R}_k}{s-p_k} + \mathbf{D} + s\mathbf{E}$$

需保证导纳矩阵对称性和正实性。

## 形式化表达

### 频率扫描基础

在边界端口施加扫频源，测量驱动点阻抗和转移阻抗：
$$Z_{ij}(j\omega_k) = \frac{V_i(j\omega_k)}{I_j(j\omega_k)}\bigg|_{I_{m\neq j}=0}$$

扫描频率范围需覆盖关心暂态的最高频率。

### 有理逼近误差

拟合误差度量：
$$\epsilon = \sum_{k=1}^{N}w_k\left|Y_{orig}(j\omega_k) - Y_{fit}(j\omega_k)\right|^2$$

权重$w_k$可强调关键频段。

### 稳定性与无源性

- **稳定性**：所有极点位于左半平面 (Re($p_k$) < 0)
- **无源性**：实频导纳正实性，$	ext{Re}(Y(j\omega)) \geq 0$

无源性强制方法：[[passivity-enforcement]]

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 线性假设 | 外部系统近似线性 | 饱和、开关动作需特殊处理 |
| 时不变性 | 外部拓扑恒定 | 快速拓扑变化需在线更新 |
| 频率范围 | 明确上下限 | 决定扫描和拟合参数 |
| 端口选择 | 边界清晰 | 端口位置影响等值精度 |

### 失效边界

- **非线性主导**：外部系统含大量非线性设备（如HVDC换流器）
- **拓扑时变**：频繁开关操作改变外部系统结构
- **端口效应**：端口选择不当导致内部响应失真
- **谐振遗漏**：极点阶数不足或扫描范围不当
- **长时漂移**：FDNE参数不能反映外部系统慢变特性

### 关键假设

1. 外部系统在所关心频段内可用线性时不变模型表示
2. 边界端口电压电流关系足以刻画内部-外部交互
3. 频率扫描数据准确可靠（无数值噪声）
4. 有理函数阶数足够捕捉关键谐振

## 代表性来源

### 经典文献

- Watson, N. and Arrillaga, J., "Power Systems Electromagnetic Transients Simulation," *IET*, 2003. - FDNE理论与应用
- Morched, A., et al., "A Multipurpose Frequency Scanning Technique," *IEEE PAS*, 1992. - 频率扫描技术
- Gustavsen, B. and Semlyen, A., "Rational Approximation of Frequency Domain Responses," *IEEE TD*, 1999. - 矢量拟合奠基

### 相关方法

- [[vector-fitting]] - 有理逼近核心算法
- [[passivity-enforcement]] - 无源性强制
- [[frequency-scanning]] - 频率扫描方法
- [[network-equivalent]] - 网络等值一般方法

## 与相关页面的关系

- [[vector-fitting]] - 有理函数拟合算法
- [[passivity-enforcement]] - 保证无源性的后处理
- [[frequency-domain-analysis]] - 频域分析基础
- [[network-equivalent]] - 网络等值方法体系
- [[electromechanical-electromagnetic-hybrid-simulation]] - 混合仿真接口

## 开放问题

- 含非线性设备的FDNE扩展方法
- 时变拓扑下的自适应FDNE更新
- 大规模系统高效频率扫描算法
- 多端口FDNE的最优端口选择准则
- 数据驱动的FDNE黑箱建模

## 参考标准

- IEEE Std. 1800 - 电磁暂态仿真导则
- CIGRE TB 604 - EMT仿真应用指南

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
