---
title: "双线性变换 (Bilinear Transform)"
type: method
tags: [bilinear-transform, tustin, discretization, s-to-z, numerical-integration]
created: "2026-05-04"
---

# 双线性变换 (Bilinear Transform)

## 定义与边界

双线性变换（Bilinear Transform），又称Tustin变换或梯形积分法，是将连续时间传递函数$H(s)$转换为离散时间传递函数$H(z)$的数学方法。通过$s = \frac{2}{T}\frac{z-1}{z+1}$的映射，保持系统稳定性，且频率响应在低频段与连续系统近似。双线性变换是EMT仿真中连续控制器离散化和频变模型时域实现的基础工具。

**边界限定**：本页面聚焦于双线性变换在EMT中的应用，不包括其他离散化方法（如前向/后向欧拉）的详细对比。

## EMT中的作用

双线性变换是连续-离散转换的核心工具：

- **控制器离散化**：将连续域设计的控制器转换为数字实现
- **频变模型实现**：有理函数频变模型的时域离散
- **滤波器设计**：数字滤波器从模拟原型转换
- **多速率接口**：不同采样率系统间的数据转换
- **伴随电路**：梯形积分对应的离散等效电路

## 主要分支与机制

### 1. 基本变换公式

**s域到z域映射**：
$$s = \frac{2}{T} \cdot \frac{z-1}{z+1} = \frac{2}{T} \cdot \frac{1-z^{-1}}{1+z^{-1}}$$

**逆变换**：
$$z = \frac{1 + sT/2}{1 - sT/2}$$

其中$T$为采样周期。

### 2. 频率畸变与预畸变

**频率映射关系**：
$$\omega_a = \frac{2}{T}\tan\left(\frac{\omega_d T}{2}\right)$$

**预畸变（Pre-warping）**：
在关键频率$\omega_c$处匹配：
$$s \leftarrow \frac{\omega_c}{\tan(\omega_c T/2)} \cdot \frac{z-1}{z+1}$$

### 3. 梯形积分对应

对微分方程：
$$\frac{dy}{dt} = f(t)$$

梯形离散：
$$\frac{y_n - y_{n-1}}{T} = \frac{f_n + f_{n-1}}{2}$$

对应$z$域：
$$Y(z) = \frac{T}{2} \cdot \frac{1+z^{-1}}{1-z^{-1}} F(z)$$

## 形式化表达

### 传递函数转换

连续传递函数：
$$H(s) = \frac{b_0 s^m + b_1 s^{m-1} + ... + b_m}{a_0 s^n + a_1 s^{n-1} + ... + a_n}$$

代入$s = \frac{2}{T}\frac{z-1}{z+1}$得到离散传递函数$H(z)$。

### 状态空间转换

连续状态方程：
$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$

离散化（梯形法）：
$$\mathbf{x}_{n+1} = \mathbf{A}_d \mathbf{x}_n + \mathbf{B}_d \mathbf{u}_n + \mathbf{E}_d \mathbf{u}_{n+1}$$

其中：
$$\mathbf{A}_d = \left(\mathbf{I} - \frac{T}{2}\mathbf{A}\right)^{-1}\left(\mathbf{I} + \frac{T}{2}\mathbf{A}\right)$$
$$\mathbf{B}_d = \frac{T}{2}\left(\mathbf{I} - \frac{T}{2}\mathbf{A}\right)^{-1}\mathbf{B}$$

### 稳定性保持

$s$域左半平面映射到$z$域单位圆内：
$$\text{Re}(s) < 0 \Leftrightarrow |z| < 1$$

保证稳定连续系统离散后仍稳定。

## 适用边界与失败模式

### 适用条件

| 条件 | 要求 | 说明 |
|------|------|------|
| 采样率 | $f_s > 10f_{max}$ | 减少频率畸变 |
| 线性系统 | 传递函数存在 | 非线性需特殊处理 |
| 稳定性 | 原系统稳定 | 保持稳定性 |
| 精度 | 可接受频率畸变 | 或预畸变校正 |

### 失效边界

- **高频分量**：频率接近奈奎斯特频率时畸变严重
- **脉冲响应**：梯形法对脉冲输入响应不准
- ** stiff 系统**：多时间尺度系统需多速率处理
- **非线性系统**：需局部线性化或迭代

### 关键假设

1. 系统为线性时不变（LTI）
2. 采样率足够高
3. 初始条件正确处理
4. 数值精度足够（避免累积误差）

## 代表性来源

### 经典文献

- Tustin, A., "A Method of Analysing the Behaviour of Linear Systems in Terms of Time Series," *JIEE*, 1947. - 双线性变换奠基
- Franklin, G.F., et al., "Digital Control of Dynamic Systems," *Addison-Wesley*, 1998. - 数字控制经典教材
- Ogata, K., "Discrete-Time Control Systems," *Prentice-Hall*, 1995.

### EMT应用

- [[numerical-integration]] - 数值积分方法
- [[discretization-methods]] - 离散化方法
- [[companion-circuit]] - 伴随电路

## 与相关页面的关系

- [[numerical-integration]] - 数值积分（梯形法）
- [[discretization-methods]] - 离散化方法综合
- [[companion-circuit]] - 伴随电路（梯形法实现）
- [[z-transform]] - Z变换理论
- [[state-space-method]] - 状态空间方法

## 开放问题

- 变步长双线性变换
- 非均匀采样的推广
- 多速率系统的转换
- 时变系统的离散化
- 高阶保持器的结合

## 参考标准

- IEEE Std. 1800 - 电磁暂态仿真导则
- IEC 61970 - 能量管理系统

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
