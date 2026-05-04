---
title: "静止同步补偿器模型 (STATCOM Model)"
type: model
tags: [statcom, model, vsc, reactive-power, voltage-control, facts, pwm]
created: "2026-05-02"
---

# 静止同步补偿器模型 (STATCOM Model)

## 概述

STATCOM模型用于电磁暂态(EMT)仿真中描述静止同步补偿器的动态行为。根据仿真精度和计算效率要求，STATCOM模型可分为详细开关模型、平均值模型和等效模型三个层次。不同层次模型适用于不同的研究目的，从器件级分析到系统级研究各有侧重。

## 详细开关模型

### 拓扑结构
两电平电压源换流器：
```
        S1    S3    S5
         ┬     ┬     ┬
    DC+ ─┴─C1─┴─C2─┴─C3─┴─ DC-
         │     │     │
        D1    D3    D5
         │     │     │
         ├─La─┼─Lb─┼─Lc─┤  → 滤波电感 → 电网
         │     │     │
        D2    D4    D6
         │     │     │
    DC- ─┬─C4─┴─C5─┴─C6─┬─ DC+
         ┴     ┴     ┴
        S2    S4    S6
```

其中S1-S6为IGBT开关，D1-D6为反并联二极管。

### IGBT模型
开关函数：
$$S_k = \begin{cases} 1 & \text{导通} \\ 0 & \text{关断} \end{cases}$$

导通压降：
$$V_{ce} = V_{ce0} + R_{ce}I_c$$

关断特性：
- 关断延时 $t_{d(off)}$
- 下降时间 $t_f$
- 拖尾电流 $I_{tail}$

### 开关状态
三相桥臂开关状态：

| 状态 | Sa | Sb | Sc | 输出电压 |
|-----|----|----|----|---------|
| 1 | 1 | 0 | 0 | $+V_{dc}/2$ (a相) |
| 2 | 1 | 1 | 0 | 特定组合 |
| ... | ... | ... | ... | ... |
| 8 | 0 | 0 | 0 | 零矢量 |

共8种开关状态（6个有效矢量 + 2个零矢量）。

### 换流过程
导通损耗：
$$P_{cond} = V_{ce0}I_{avg} + R_{ce}I_{rms}^2$$

开关损耗：
$$P_{sw} = f_{sw}(E_{on} + E_{off})\frac{I}{I_{nom}}\frac{V_{dc}}{V_{dc,nom}}$$

总损耗：
$$P_{loss} = 6(P_{cond} + P_{sw})$$

### 数值仿真
固定步长仿真：
- 步长 $\Delta t < T_{sw}/10$
- 典型值：1-10 μs
- 插值处理开关时刻

## 平均值模型

### 基本思想
忽略开关过程，用占空比等效：
$$v_a = d_a \cdot \frac{V_{dc}}{2}$$

其中 $d_a$ 为a相占空比，$d_a \in [-1, 1]$。

### dq坐标系模型
Park变换后的电压方程：
$$v_d = d_d \cdot \frac{V_{dc}}{2}$$
$$v_q = d_q \cdot \frac{V_{dc}}{2}$$

约束条件：
$$d_d^2 + d_q^2 \leq 1$$

### 线性化模型
在平衡点 $(d_{d0}, d_{q0})$ 线性化：
$$\begin{bmatrix} \Delta v_d \\ \Delta v_q \end{bmatrix} = \frac{V_{dc0}}{2}\begin{bmatrix} \Delta d_d \\ \Delta d_q \end{bmatrix} + \frac{1}{2}\begin{bmatrix} d_{d0} \\ d_{q0} \end{bmatrix}\Delta V_{dc}$$

### 状态空间方程
$$
\begin{bmatrix} \dot{i}_d \\ \dot{i}_q \\ \dot{V}_{dc} \end{bmatrix} = 
\begin{bmatrix} 
-R/L & \omega & d_d/(2L) \\
-\omega & -R/L & d_q/(2L) \\
-3d_d/(2C) & -3d_q/(2C) & 0 
\end{bmatrix}
\begin{bmatrix} i_d \\ i_q \\ V_{dc} \end{bmatrix}
+
\begin{bmatrix} -v_{gd}/L \\ -v_{gq}/L \\ 0 \end{bmatrix}
$$

## 等效受控源模型

### 简化模型
STATCOM等效为受控电流源：
$$\tilde{I}_{STATCOM} = (I_d + jI_q)e^{j\theta}$$

或受控电纳：
$$B_{STATCOM} = \frac{Q_{ref}}{V^2}$$

### 电流源模型
电流参考值：
$$I_{q,ref} = K_p(V_{ref} - V) + K_i\int(V_{ref} - V)dt$$

响应特性：
- 一阶惯性环节
- 时间常数 $T_{response}$
- 幅值限制

### 导纳模型
节点导纳矩阵修正：
$$Y_{bus,new} = Y_{bus} + jB_{STATCOM}$$

适用于潮流计算。

## 控制系统模型

### 电压外环
PI控制器：
$$I_q^* = K_{pv}\Delta V + K_{iv}\int\Delta V dt$$

限幅：
$$|I_q^*| \leq I_{max}$$

带宽设计：
$$\omega_{bw,v} = \frac{K_{pv}}{K_{iv}} = 10-50 \text{ rad/s}$$

### 电流内环
d轴电流控制：
$$v_d^* = K_{pc}(I_d^* - I_d) + K_{ic}\int(I_d^* - I_d)dt - \omega Li_q + v_{gd}$$

q轴电流控制：
$$v_q^* = K_{pc}(I_q^* - I_q) + K_{ic}\int(I_q^* - I_q)dt + \omega Li_d + v_{gq}$$

解耦项消除dq轴耦合。

带宽设计：
$$\omega_{bw,c} = 5-10 \times \omega_{bw,v}$$

### 直流电压控制
有功电流参考：
$$I_d^* = K_{pdc}(V_{dc}^* - V_{dc}) + K_{idc}\int(V_{dc}^* - V_{dc})dt$$

功率平衡：
$$\frac{3}{2}v_d i_d = V_{dc}I_{dc}$$

## PWM调制模型

### SPWM模型
调制波与载波比较：
$$d(t) = \frac{v_{ref}(t)}{V_{tri,peak}}$$

输出电压：
$$v_{out}(t) = d(t) \cdot V_{dc}$$

谐波分析：
$$V_n = \frac{4V_{dc}}{n\pi}J_0\left(\frac{n\pi M}{2}\right)$$

### SVPWM模型
空间矢量调制：
- 确定参考矢量所在扇区
- 计算相邻矢量作用时间
- 插入零矢量

电压利用率：
$$\frac{V_{out,max}}{V_{dc}/2} = \frac{2}{\sqrt{3}} \approx 1.15$$

比SPWM提高15%。

### 谐波等效
等效开关函数：
$$S_{eq}(t) = d(t) + \sum_{n=1}^{\infty}h_n(t)$$

其中 $h_n(t)$ 为高频谐波分量，在平均值模型中忽略。

## 暂态模型

### 故障响应模型
电压跌落时电流响应：
$$\frac{di_q}{dt} = \frac{v_q - v_{gq} - Ri_q}{L}$$

限流控制：
$$I_{lim} = \begin{cases} 1.2I_N & \text{故障期间} \\ I_N & \text{正常} \end{cases}$$

### 低电压穿越
LVRT控制策略：
- 无功优先
- 有功降额
- 直流电压控制
- 故障穿越能力验证

## 多电平模型

### NPC三电平模型
输出电平：$+V_{dc}/2, 0, -V_{dc}/2$

开关状态：
- P状态：上两管导通
- O状态：中两管导通
- N状态：下两管导通

中点电位平衡：
$$\Delta V_{np} = V_{c1} - V_{c2}$$

控制目标：$\Delta V_{np} \approx 0$

### MMC模型
子模块电容电压：
$$C_{sm}\frac{dv_{sm}}{dt} = i_{arm} \cdot S$$

桥臂电压：
$$v_{arm} = \sum_{i=1}^{N}v_{smi} \cdot S_i$$

环流抑制：
- 二倍频负序控制
- 桥臂电抗设计

## 模型选择指南

| 模型层次 | 适用场景 | 计算量 | 精度 |
|---------|---------|-------|------|
| 详细开关 | 器件分析、损耗计算 | 大 | 高 |
| 平均值 | 控制设计、系统研究 | 中 | 中 |
| 等效模型 | 潮流计算、稳态分析 | 小 | 低 |

### 选择原则
- 器件级研究：详细开关模型
- 控制策略验证：平均值模型
- 大规模系统：等效模型
- 混合仿真：多速率模型

## 参数设置

### 关键参数

| 参数 | 符号 | 典型值 | 说明 |
|-----|------|-------|------|
| 直流电容 | $C_{dc}$ | 5-20 mF | 储能 |
| 滤波电感 | $L_f$ | 0.1-0.3 pu | 限流 |
| 滤波电阻 | $R_f$ | 0.01-0.05 pu | 阻尼 |
| 开关频率 | $f_{sw}$ | 1-5 kHz | IGBT |
| 控制周期 | $T_s$ | 0.1-1 ms | 采样周期 |

### 控制参数
电压环PI：
- $K_{pv}$: 0.5-2.0
- $K_{iv}$: 10-50

电流环PI：
- $K_{pc}$: 0.3-1.0
- $K_{ic}$: 100-500

## 验证与测试

### 稳态验证
- 无功输出能力
- 电压调节精度
- 损耗特性

### 动态测试
- 阶跃响应
- 频率响应
- 故障响应

### 现场测试
- 并网试验
- 扰动试验
- 保护配合

## 相关模型
- [[vsc-model]] - VSC模型
- [[facts]] - FACTS模型
- `pwm-modulation` - PWM调制
- [[average-value-model]] - 平均值模型
- [[detailed-switch-model]] - 详细开关模型

## 来源论文

参见 [[index.md]] 获取更多STATCOM模型相关文献。
