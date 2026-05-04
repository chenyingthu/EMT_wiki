---
title: "部分分式展开 (Partial Fraction Expansion)"
type: method
tags: [partial-fraction, residue, laplace-transform, transfer-function, rational-function]
created: "2026-05-02"
---

# 部分分式展开 (Partial Fraction Expansion)

## 概述

部分分式展开是将复杂的有理函数分解为简单分式之和的方法，在电力系统EMT仿真中广泛应用于传递函数分析、时域响应计算、极点-留数建模和频域分析。通过部分分式展开，可以方便地分析系统的极点分布、计算时域响应和进行模型降阶。

## 数学原理

### 基本形式
有理函数 $F(s)$ 的部分分式展开：

$$F(s) = \frac{N(s)}{D(s)} = \sum_{i=1}^{n} \frac{k_i}{s-p_i} + R(s)$$

其中：
- $p_i$: 极点
- $k_i$: 留数（residue）
- $R(s)$: 多项式余项（当分子阶数≥分母时）

### 单极点情况
对于不同的单极点 $p_i$:
$$k_i = \lim_{s \to p_i} (s-p_i)F(s)$$

### 重极点情况
对于 $m$ 阶重极点 $p$:
$$F(s) = \sum_{j=1}^{m} \frac{k_j}{(s-p)^j}$$

其中：
$$k_j = \frac{1}{(m-j)!} \frac{d^{m-j}}{ds^{m-j}}[(s-p)^m F(s)]_{s=p}$$

## 计算方法

### 留数定理法
基于复变函数理论：
$$k_i = \frac{N(p_i)}{D'(p_i)}$$

其中 $D'(s)$ 为分母的导数。

### 待定系数法
假设展开形式，通过比较系数求解：
$$\frac{N(s)}{D(s)} = \frac{k_1}{s-p_1} + \frac{k_2}{s-p_2} + ...$$

通分后比较分子系数。

### Heaviside方法
对于单极点，直接代入：
$$k_i = [(s-p_i)F(s)]_{s=p_i}$$

## 时域响应

### 逆拉普拉斯变换
部分分式与时域响应的关系：
$$\mathcal{L}^{-1}\left\{\frac{1}{s-p}\right\} = e^{pt}$$

### 响应类型
| 极点位置 | 时域响应 |
|----------|----------|
| $p < 0$ (实轴) | 指数衰减 |
| $p > 0$ (实轴) | 指数增长 |
| $p = 0$ | 阶跃 |
| $p = \sigma \pm j\omega$ ($\sigma < 0$) | 衰减振荡 |
| $p = \pm j\omega$ | 等幅振荡 |

## 电力系统应用

### 传递函数分析
- `transfer-function` - 传递函数
- **频域响应**: Bode图、Nyquist图
- `frequency-response` - 频率响应
- **稳定性**: 极点位置判断
- [[transient-stability-analysis]] - 稳定性分析

### 矢量拟合
- [[vector-fitting]] - 矢量拟合
- **极点-留数**: 频率相关模型
- [[frequency-dependent-modeling]] - 频率相关建模
- **无源性**: 无源性验证和强制
- [[passivity-enforcement]] - 无源性强制

### 网络等值
- [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]] - 频变网络等值
- **FDNE**: 频率相关网络等值
- [[fdne-model]] - FDNE模型
- **有理逼近**: 传递函数拟合

### 暂态分析
- **时域响应**: 故障响应计算
- [[coupling-model-for-time-domain-analysis-of-nonparallel-overhead-wires-and-buried]] - 时域分析
- **卷积**: 任意激励响应
- [[zfunction-convolution-in-ehv]] - 卷积

## 数值计算

### MATLAB实现
```matlab
[r, p, k] = residue(num, den)
% r: 留数
% p: 极点
% k: 直接项
```

### Python实现
```python
from scipy.signal import residue
r, p, k = residue(num, den)
```

### 数值稳定性
- **病态极点**: 相近极点数值问题
- **尺度**: 参数量级差异
- **精度**: 高阶多项式精度损失

## 复数极点处理

### 共轭复数极点
对于 $p = \sigma \pm j\omega$:
$$\frac{k}{s-(\sigma+j\omega)} + \frac{k^*}{s-(\sigma-j\omega)} = \frac{A(s-\sigma)+B\omega}{(s-\sigma)^2+\omega^2}$$

时域响应：
$$2|k|e^{\sigma t}\cos(\omega t + \angle k)$$

### 振荡模式识别
- **频率**: $\omega$ (rad/s)
- **阻尼比**: $\xi = -\sigma/|p|$
- `oscillation-mode` - 振荡模式

## 高阶展开

### 级数展开
对于复杂函数：
- **Taylor级数**: 解析点附近
- **Laurent级数**: 含奇点
- `series-expansion` - 级数展开

### 渐近展开
大参数或小参数近似：
- **Pade逼近**: 有理函数逼近
- `pade-approximation` - Pade逼近
- **渐近分析**: 极限行为

## 与EMT仿真的关系

### 模型实现
- **有理函数**: 频变参数
- **状态空间**: 部分分式转状态空间
- `state-space-conversion` - 状态空间转换

### 伴随模型
- **离散化**: 梯形法等效
- [[companion-model]] - 伴随模型
- **递归卷积**: 高效时域计算
- `recursive-convolution` - 递归卷积

## 典型应用

### 传输线模型
- [[transmission-line-model]] - 输电线路模型
- **Bergeron模型**: 无损线
- **频率相关**: 考虑集肤效应
- [[frequency-dependent-line-model]] - 频变线路模型

### 变压器模型
- [[transformer-model]] - 变压器模型
- **饱和**: 非线性特性
- **涡流**: 频率相关损耗

### 电缆模型
- [[cable-model]] - 电缆模型
- **层间绝缘**: 复杂结构
- [[underground-cable-modeling]] - 地下电缆建模

## 相关方法
- `pole-zero-analysis` - 零极点分析
- `residue-calculation` - 留数计算
- [[numerical-laplace-transform]] - 拉普拉斯变换
- `rational-function` - 有理函数

## 扩展阅读
- 数值分析教材
- 线性系统理论
- 复变函数与应用

## 来源论文

参见 [[index.md]] 获取更多部分分式展开相关文献。
