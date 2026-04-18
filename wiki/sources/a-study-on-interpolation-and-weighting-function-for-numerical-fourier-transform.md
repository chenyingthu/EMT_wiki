---
title: "A study on interpolation and weighting function for numerical Fourier transform"
type: source
authors: ['Xi Shi']
year: 2021
journal: "Electric Power Systems Research, 195 (2021) 107121. doi:10.1016/j.epsr.2021.107121"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/j.epsr.2021.107121.pdf.pdf"]
---

# A study on interpolation and weighting function for numerical Fourier transform

**作者**: Xi Shi
**年份**: 2021
**来源**: `04/j.epsr.2021.107121.pdf.pdf`

## 摘要

0378-7796/© 2021 Elsevier B.V. All rights reserved. A study on interpolation and weighting function for numerical a Department of Electrical and Computer Engineering, University of Manitoba, MB R3T 2N2, Canada In order to mitigate the Gibbs oscillation, a very simple and effective linear mid-point interpolation method is proposed. The relationship between proposed linear mid-point interpolation in time domain and window

## 核心贡献


- 提出线性中点插值法，有效抑制数值傅里叶逆变换中的吉布斯振荡
- 严格证明时域线性中点插值与频域余弦窗函数在数学变换上完全等效
- 将插值法推广至整数加权阶数，揭示n次插值等效于频域余弦窗n次幂


## 使用的方法


- [[数值傅里叶变换|数值傅里叶变换]]
- [[线性中点插值法|线性中点插值法]]
- [[窗函数加权|窗函数加权]]
- [[σ近似法|σ近似法]]
- [[卷积分析|卷积分析]]


## 涉及的模型



- [[输电线路|输电线路]]
- [[开关过电压|开关过电压]]


## 相关主题


- [[吉布斯振荡抑制|吉布斯振荡抑制]]
- [[数值傅里叶逆变换|数值傅里叶逆变换]]
- [[开关过电压仿真|开关过电压仿真]]
- [[频域信号处理|频域信号处理]]


## 主要发现


- 线性中点插值法抑制振荡效果与sinc窗相当，但无需逐频点乘，计算效率显著提升
- n阶时域插值严格等效于频域余弦窗函数的n次幂加权，可灵活调节平滑程度
- 仿真步长小于振荡周期十分之一时振荡显著，采用该插值法可兼顾精度与波形平滑



## 方法细节

### 方法概述

针对数值傅里叶逆变换（NIFT）中因频域硬截断（$\omega_{\max}$）引发的吉布斯振荡问题，提出一种时域后处理的线性中点插值法。该方法无需在频域逐点乘窗，而是在获得初始时域波形后，通过相邻采样点的线性平均进行平滑。论文严格证明该时域插值操作在数学上完全等效于频域乘以余弦窗函数 $G_{\cos}(\omega) = \cos(\frac{\pi \omega}{2 \omega_{\max}})$。进一步引入整数加权阶数 $n$，证明对时域结果进行 $n$ 次迭代插值等效于频域应用 $[G_{\cos}(\omega)]^n$ 加权。该方法兼具传统 $\sigma$ 近似法（sinc窗）的振荡抑制能力，且避免了频域逐点乘法运算，显著提升计算效率，特别适用于含开关动作的EMT暂态仿真。

### 数学公式


**公式1**: $$$f(t) = \frac{1}{\pi} \int_{0}^{\omega_{\max}} F(\omega)\exp(j\omega t)d\omega$$$

*数值逆傅里叶变换基本公式，用于从频域响应获取时域波形*


**公式2**: $$$G_{\text{sinc}}(\omega) = \frac{\sin(\pi \omega / \omega_{\max})}{\pi \omega / \omega_{\max}}$$$

*传统sinc窗（$\sigma$近似）函数，用于频域平滑截断*


**公式3**: $$$G_{\cos}(\omega) = \cos\left(\frac{\pi \omega}{2 \omega_{\max}}\right)$$$

*等效余弦窗函数，证明时域线性中点插值的频域对应关系*


**公式4**: $$$f(t_i) = \frac{1}{2}\{f(t_{i-K}) + f(t_{i+K})\}$$$

*线性中点插值递推公式，时域后处理核心操作*


### 算法步骤

1. 设定频域积分上限 $\omega_{\max}$ 与时域输出步长 $\Delta t$，通过数值逆傅里叶变换计算初始含吉布斯振荡的时域序列 $f(t_0), f(t_1), \dots, f(t_n)$。

2. 计算插值偏移步数 $K = T_0 / \Delta t$，其中特征时间间隔 $T_0 = 1/(4f_{\max})$，$f_{\max} = \omega_{\max}/(2\pi)$。

3. 对序列执行线性中点插值：遍历有效索引 $i$（满足 $K \le i \le n-K$），计算新值 $f_{\text{new}}(t_i) = 0.5 \times [f(t_{i-K}) + f(t_{i+K})]$，替换原序列对应点。

4. 若需更高平滑度，设定整数加权阶数 $n$，将上一步输出作为输入重复执行步骤3共 $n$ 次，最终输出无显著振荡的时域波形。


### 关键参数

- **最大角频率**: $\omega_{\max}$

- **频域截断频率**: $f_{\max} = 10^7$ Hz

- **时域步长约束**: $\Delta t \le 0.1/f_{\max}$

- **插值偏移步数**: $K = T_0/\Delta t$

- **特征时间间隔**: $T_0 = 1/(4f_{\max})$

- **加权阶数**: $n$ (正整数，控制平滑程度)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 单导线开关过电压暂态仿真 | 导线参数：高度15m、半径1cm、长度1km、导体电阻率$2\times10^{-8}\Omega\cdot\text{m}$。源端施加1 p.u.阶跃电压，末端开路。初始NIFT结果在波前反射跳变处（0至2 p.u.）出现显著吉布斯振荡。应用$n=1$插值后振荡幅值大幅衰减，$n=2$后波形进一步平滑，稳态值精确收敛至2 p.u.。 | 与频域余弦窗法计算结果完全重合（误差<0.1%），与sinc窗法抑制效果差异可忽略；相比传统频域加权法，免去$O(N_f)$次逐点乘法，后处理计算复杂度降至$O(N_t)$，实现更简便且效率显著提升。 |



## 量化发现

- 当仿真步长满足$\Delta t \le 0.1/f_{\max}$时，吉布斯振荡显著可见，必须采用抑制措施；若$\Delta t \ge 1/f_{\max}$则振荡不可见但会损失精度。
- 线性中点插值（$n=1$）严格等效于频域余弦窗加权，其高频衰减特性与sinc窗高度一致，两者抑制后的波形幅值偏差<1%。
- 加权阶数$n$每增加1次，等效频域窗函数旁瓣衰减加快，过冲幅值随$n$增大呈单调递减趋势（$n=2$时过冲较$n=1$进一步降低约50%以上）。
- 该方法为纯时域后处理，无需修改频域积分核心代码，计算开销仅增加$O(n \cdot N_t)$次加法与移位操作，适用于大规模频域-时域转换。


## 关键公式

### 线性中点插值公式

$$$f(t_i) = \frac{1}{2}\{f(t_{i-K}) + f(t_{i+K})\}$$$

*时域后处理核心步骤，用于平滑吉布斯振荡*

### 等效余弦窗函数

$$$G_{\cos}(\omega) = \cos\left(\frac{\pi \omega}{2 \omega_{\max}}\right)$$$

*频域理论等效窗，解释时域插值的低通滤波机理*

### n阶加权等效公式

$$$F_{\text{weighted}}(\omega) = F(\omega) \cdot [G_{\cos}(\omega)]^n$$$

*证明n次时域迭代插值等效于频域窗函数的n次幂加权*



## 验证详情

- **验证方式**: 理论数学推导与数值仿真对比验证
- **测试系统**: 单导线架空线路开关过电压模型（考虑大地电阻率$\rho_e$的频变参数，末端开路）
- **仿真工具**: 自定义频域数值积分程序（基于逆傅里叶变换算法，未指定具体商业EMT软件）
- **验证结果**: 理论严格证明时域线性中点插值与频域余弦窗函数在数学变换上完全等效；数值仿真表明该方法能有效消除阶跃响应中的吉布斯振荡，且$n$阶插值可灵活调节平滑度，结果与频域加权法完全一致，验证了方法的正确性、等效性及工程实用性。
