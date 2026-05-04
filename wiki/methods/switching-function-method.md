---
title: "开关函数法 (Switching Function Method)"
type: method
tags: [switching-function, average-value, modulation, converter, power-electronics]
created: "2026-05-02"
---

# 开关函数法 (Switching Function Method)

## 概述

开关函数法(Switching Function Method)是电力电子变换器建模的重要方法，通过引入开关函数来描述开关器件的通断状态，将时变的开关电路转化为数学模型。该方法可以建立详细的开关模型，也可以通过平均化处理得到平均值模型。开关函数法直观、物理意义清晰，广泛应用于DC-DC变换器、DC-AC逆变器、AC-DC整流器和多电平变换器的分析与控制设计中。通过开关函数，可以方便地分析变换器的电压传输比、功率流动和谐波特性，是电力电子系统分析和控制设计的基础工具。

## 基本原理

### 开关函数定义

**单相开关函数**:
$$S(t) = \begin{cases} 1 & \text{上管导通，下管关断} \\ 0 & \text{上管关断，下管导通} \end{cases}$$

**三相开关函数**:
$$\mathbf{S}(t) = [S_a(t), S_b(t), S_c(t)]^T$$

**互补开关**:
对于半桥结构:
$$S_{lower} = 1 - S_{upper}$$

### 理想开关假设

**特性假设**:
- 导通时: 零电阻，零压降
- 关断时: 无穷大电阻，零漏电流
- 瞬时切换: 无开关时间

**实际修正**:
- 导通压降
- 开关时间
- 死区时间

## DC-DC变换器建模

### Buck变换器

**开关函数模型**:
$$v_o = S \cdot V_{in}$$

**状态方程**:
$$\begin{cases}
L\frac{di_L}{dt} = S \cdot V_{in} - v_o \\
C\frac{dv_o}{dt} = i_L - \frac{v_o}{R}
\end{cases}$$

**状态空间平均**:
$$\dot{\bar{x}} = (dA_1 + (1-d)A_2)\bar{x} + (dB_1 + (1-d)B_2)\bar{u}$$

其中 $d$ 为占空比。

**传输函数**:
$$\frac{V_o}{V_{in}} = d$$

### Boost变换器

**开关函数模型**:
$$v_{in} = (1-S)V_o$$

**状态方程**:
$$\begin{cases}
L\frac{di_L}{dt} = V_{in} - (1-S)v_o \\
C\frac{dv_o}{dt} = (1-S)i_L - \frac{v_o}{R}
\end{cases}$$

**传输函数**:
$$\frac{V_o}{V_{in}} = \frac{1}{1-d}$$

### Buck-Boost变换器

**开关函数模型**:
$$v_o = -\frac{S}{1-S}V_{in}$$

**传输函数**:
$$\frac{V_o}{V_{in}} = -\frac{d}{1-d}$$

## DC-AC逆变器建模

### 单相全桥逆变器

**开关函数**:
$$S = S_1 - S_4$$

取值: +1, 0, -1 (三电平)

**输出电压**:
$$v_o = S \cdot \frac{V_{dc}}{2}$$

**电流方程**:
$$L\frac{di}{dt} = v_o - v_{grid}$$

### 三相逆变器

**开关函数矩阵**:
$$\mathbf{S} = [S_a, S_b, S_c]^T$$

**相电压**:
$$\mathbf{v}_{abc} = \mathbf{S} \cdot \frac{V_{dc}}{2}$$

**线电压**:
$$\mathbf{v}_{ab} = (S_a - S_b)\frac{V_{dc}}{2}$$

**坐标变换**:
$$\mathbf{v}_{dq} = \mathbf{T}_{abc/dq} \cdot \mathbf{v}_{abc}$$

## AC-DC整流器建模

### 单相整流器

**开关函数**:
$$S = \begin{cases} 1 & \text{正半周上管导通} \\ -1 & \text{负半周下管导通} \end{cases}$$

**输出电压**:
$$v_{dc} = S \cdot v_{ac}$$

**功率流动**:
$$P_{ac} = v_{ac} \cdot i_{ac} = v_{dc} \cdot i_{dc}$$

### 三相PWM整流器

**开关函数**:
$$\mathbf{S} = [S_a, S_b, S_c]^T$$

**交流侧电压**:
$$\mathbf{v}_{abc} = \mathbf{S} \cdot \frac{V_{dc}}{2}$$

**直流侧电流**:
$$i_{dc} = \mathbf{S}^T \cdot \mathbf{i}_{abc}$$

**功率平衡**:
$$\frac{3}{2}(v_d i_d + v_q i_q) = V_{dc} i_{dc}$$

## 平均值模型

### 状态空间平均法

**基本思想**:
对开关周期内的状态方程取平均。

**平均开关函数**:
$$d = \frac{1}{T_s}\int_0^{T_s} S(t)dt$$

其中 $d$ 为占空比，$T_s$ 为开关周期。

**状态平均方程**:
$$\dot{\bar{x}} = A(d)\bar{x} + B(d)\bar{u}$$

其中:
$$A(d) = dA_1 + (1-d)A_2$$
$$B(d) = dB_1 + (1-d)B_2$$

### 小信号模型

**扰动分析**:
$$d = D + \tilde{d}$$
$$\bar{x} = X + \tilde{x}$$

**线性化**:
$$\dot{\tilde{x}} = A(D)\tilde{x} + B(D)\tilde{u} + E\tilde{d}$$

其中 $E = \frac{\partial(A\bar{x}+B\bar{u})}{\partial d}$

**传递函数**:
$$G_{vd}(s) = \frac{\tilde{v}_o(s)}{\tilde{d}(s)}$$

## 调制策略

### PWM调制

**SPWM (正弦脉宽调制)**:
$$d(t) = M\sin(\omega t) + 0.5$$

调制比:
$$M = \frac{V_{ref}}{V_{tri}}$$

**线电压输出**:
$$V_{LL} = \frac{\sqrt{3}}{2}MV_{dc}$$

**SVPWM (空间矢量调制)**:

基本电压矢量:
$$\mathbf{V}_k = \frac{2}{3}V_{dc}e^{j(k-1)\frac{\pi}{3}}, \quad k = 1,2,...,6$$

参考矢量合成:
$$\mathbf{V}_{ref}T_s = \mathbf{V}_iT_i + \mathbf{V}_{i+1}T_{i+1} + \mathbf{V}_0T_0$$

### 多电平调制

**NLM (最近电平调制)**:
选择最接近的整数电平:
$$n = \text{round}\left(\frac{V_{ref}}{V_{dc}/N}\right)$$

**PD-PWM (载波层叠)**:
多个三角载波层叠，与调制波比较。

**PS-PWM (载波移相)**:
多模块载波相位差:
$$\phi_k = \frac{2\pi(k-1)}{N}$$

## MMC建模

### 子模块开关函数

**子模块状态**:
$$S_{SM} = \begin{cases} 1 & \text{投入} \\ 0 & \text{旁路} \end{cases}$$

**子模块输出电压**:
$$v_{SM} = S_{SM} \cdot v_c$$

**桥臂电压**:
$$v_{arm} = \sum_{i=1}^{N} S_i \cdot v_{c,i}$$

### 平均值模型

**桥臂等效电压**:
$$\bar{v}_{arm} = n \cdot \bar{v}_c$$

其中 $n$ 为投入子模块数，$\bar{v}_c$ 为平均电容电压。

**电容电压平衡**:
$$\dot{\bar{v}}_c = \frac{n \cdot i_{arm}}{C}$$

## 应用实例

### 两电平VSC

**开关函数模型**:
$$\mathbf{v}_{abc} = \frac{V_{dc}}{2}\mathbf{S}$$

**功率计算**:
$$P = \frac{3}{2}(v_d i_d + v_q i_q)$$
$$Q = \frac{3}{2}(v_q i_d - v_d i_q)$$

**控制设计**:
- d轴: 有功功率/直流电压
- q轴: 无功功率/交流电压

### 三电平NPC

**开关函数**:
$$S \in \{-1, 0, 1\}$$

**输出电压**:
$$v_o = S \cdot \frac{V_{dc}}{2}$$

**中点电位平衡**:
控制正负直流母线电压均衡。

## 谐波分析

### 谐波产生机理

**开关谐波**:
- 载波频率及其倍频
- 边带谐波
- 与调制比相关

**谐波幅值**:
Bessel函数描述:
$$I_n = I_0 J_n(m\frac{\pi}{2})$$

### 谐波抑制

**载波频率选择**:
$$f_c \gg f_{fundamental}$$

**多电平技术**:
- 等效开关频率提高
- 谐波分布优化
- 滤波器体积减小

## 优缺点分析

### 优点

**物理直观**:
- 开关状态清晰
- 物理意义明确
- 易于理解

**建模灵活**:
- 适用各种拓扑
- 可详细可简化
- 便于扩展

**分析方便**:
- 功率流动清晰
- 控制设计直观
- 谐波分析容易

### 缺点

**开关细节**:
- 理想化假设
- 忽略开关动态
- 损耗难计算

**高频特性**:
- 谐波近似
- EMI难分析
- 寄生参数忽略

**数值问题**:
- 开关时刻插值
- 数值振荡
- 刚性问题

## 相关方法
- [[average-value-model]] - 平均值模型
- [[state-space-average-method]] - 状态空间平均法
- `modulation-method` - 调制方法
- `power-electronics-modeling` - 电力电子建模

## 来源论文

参见 [[index.md]] 获取更多开关函数法相关文献。
