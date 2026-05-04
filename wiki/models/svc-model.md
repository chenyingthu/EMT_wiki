---
title: "静止无功补偿器模型 (SVC Model)"
type: model
tags: [svc, model, facts, reactive-power, thyristor, tcr, tsc, voltage-control]
created: "2026-05-02"
---

# 静止无功补偿器模型 (SVC Model)

## 概述

SVC(Static Var Compensator)模型用于电磁暂态(EMT)仿真中描述静止无功补偿器的动态行为。SVC通过晶闸管控制电抗器(TCR)和晶闸管投切电容器(TSC)的组合实现无功功率的快速连续调节，是柔性交流输电系统(FACTS)的重要组成部分。根据仿真精度要求，SVC模型可分为详细开关模型、平均值模型和等效导纳模型三个层次。

## 基本结构与组成

### TCR(晶闸管控制电抗器)
```
        T1
   ─────┤├─────┐
              L
        T2    │
   ─────┤├─────┘
```

- 两个反并联晶闸管
- 串联电抗器L
- 连续调节电抗器电流

### TSC(晶闸管投切电容器)
```
        T1
   ─────┤├─────┬───C───┬────
              │       │
        T2    │     阻尼R
   ─────┤├─────┘       │
                      ─┴─
```

- 反并联晶闸管
- 串联电容C
- 阻尼电阻抑制涌流
- 阶梯式投切

### 组合结构
```
                  ┌─TCR─┐
   母线 ─────┬────┤     ├────┬─── 母线
            │    └─────┘    │
            │               │
           TSC1    TSC2    TSC3
            │       │       │
            └───────┴───────┘
```

## TCR详细开关模型

### 导通特性
触发角定义：
- $\alpha$: 电压过零点到触发时刻的电角度
- $\alpha = 0°$: 全导通
- $\alpha = 90°$: 不导通
- 调节范围：90°-180°

### 电流方程
导通期间电感电流：
$$L\frac{di_L}{dt} = v_s = \sqrt{2}V_s\sin(\omega t)$$

积分得：
$$i_L(t) = \frac{\sqrt{2}V_s}{\omega L}[\cos\alpha - \cos(\omega t)]$$

电流持续时间：
$$\sigma = 2(\pi - \alpha)$$

### 基波电流
傅里叶分析得基波分量：
$$I_1 = \frac{V_s}{\omega L}\left(1 - \frac{2\alpha}{\pi} - \frac{\sin 2\alpha}{\pi}\right)$$

等效电纳：
$$B_{TCR}(\alpha) = \frac{1}{\omega L}\left(1 - \frac{2\alpha}{\pi} - \frac{\sin 2\alpha}{\pi}\right)$$

### 谐波电流
特征谐波：
$$I_h = \frac{4V_s}{\pi\omega L}\left[\frac{\sin\alpha\cos(h\alpha) - h\cos\alpha\sin(h\alpha)}{h(h^2-1)}\right]$$

主要谐波：
- 5次：约5%
- 7次：约2.5%
- 11次：约1.5%
- 13次：约1%

### 触发控制
触发时刻计算：
$$t_{fire} = \frac{\alpha + 2n\pi}{\omega}$$

其中n为半波序号。

门极脉冲：
- 脉宽：100-200 μs
- 幅值：2-5 A
- 上升时间：< 1 μs

## TSC详细开关模型

### 投切时刻选择
零电压投切：
$$t_{switch} = \frac{n\pi}{\omega}$$

避免投切涌流。

### 暂态过程
投切时电容电压：
$$v_C(t) = V_s\sin(\omega t) + (V_{C0} - V_s\sin\phi)e^{-t/\tau}$$

其中：
- $V_{C0}$: 初始电容电压
- $\tau = RC$: 阻尼时间常数
- 阻尼电阻限制涌流

### 涌流限制
最大涌流：
$$I_{inrush,max} = \frac{\sqrt{2}V_s - V_{C0}}{\sqrt{R^2 + (\omega L)^2}}$$

典型值：< 3倍额定电流

阻尼电阻选择：
$$R = \sqrt{\frac{L}{C}}$$

或：
$$R = \frac{1}{n}\sqrt{\frac{L}{C}}$$

其中n为允许的过电压倍数。

## 平均值模型

### TCR等效电纳
$$B_{TCR}(\alpha) = B_L \cdot g(\alpha)$$

控制函数：
$$g(\alpha) = 1 - \frac{2\alpha}{\pi} - \frac{\sin 2\alpha}{\pi}$$

归一化特性：

| 触发角 | 导通角 | g(α) | 电纳 |
|-------|-------|------|------|
| 90° | 180° | 0 | 0 |
| 120° | 120° | 0.39 | 0.39$B_L$ |
| 150° | 60° | 0.84 | 0.84$B_L$ |
| 180° | 0° | 1.0 | $B_L$ |

### TSC等效电纳
离散电纳值：
$$B_{TSC,k} = k \cdot \omega C$$

其中k为投入组数(0, 1, 2, ..., N)。

### SVC总电纳
$$B_{SVC} = B_{TCR}(\alpha) + \sum_{k=1}^{N}B_{TSC,k}$$

总无功输出：
$$Q_{SVC} = -B_{SVC}V^2$$

容性为正，感性为负。

### 动态响应
一阶惯性模型：
$$\tau_{TCR}\frac{dB_{TCR}}{dt} + B_{TCR} = B_{ref}$$

TCR响应时间：
- 半波响应：10 ms(50Hz)
- 全波平均：20 ms

TSC响应时间：
- 投入：半个周波
- 切除：电流过零

## 等效导纳模型

### 简化模型
SVC等效为受控电纳：
$$B_{eq} = \frac{Q_{ref}}{V^2}$$

或等效为受控电流源：
$$\tilde{I}_{SVC} = -jB_{eq}\tilde{V}$$

### 节点导纳矩阵
$$Y_{bus,new} = Y_{bus} + jB_{SVC}$$

适用于潮流计算和稳态分析。

### 斜率特性
SVC电压-电流特性斜率：
$$X_{slope} = -\frac{\Delta V}{\Delta Q}$$

典型值：1-5%

等效斜率电抗：
$$B_{eff} = \frac{B_{SVC}}{1 + X_{slope}B_{SVC}}$$

## 控制系统模型

### 电压调节器
PI控制器：
$$B_{ref} = K_p(V_{ref} - V) + K_i\int(V_{ref} - V)dt$$

限幅：
$$B_{min} \leq B_{ref} \leq B_{max}$$

典型参数：
- $K_p$: 0.5-2.0 pu/pu
- $K_i$: 10-50 pu/pu/s
- 响应时间: 50-150 ms

### 协调控制
TCR与TSC协调：
1. 粗调：TSC投切（离散）
2. 细调：TCR触发角（连续）

控制策略：
- 优先使用TCR
- TSC在边界投切
- 避免频繁投切

投切时序：
- 投入TSC前减小TCR感性
- 切除TSC前增大TCR感性
- 平滑过渡

### 阻尼控制
附加阻尼控制：
$$\Delta B_{SVC} = K_d\frac{sT_w}{1+sT_w}\frac{1+sT_1}{1+sT_2}\Delta P$$

用于抑制低频振荡。

### 增益调节
电压依赖增益：
$$K_p(V) = K_{p0}\left(\frac{V}{V_0}\right)^n$$

提高低电压时的响应速度。

## 暂态特性

### 故障响应
电压跌落时：
- 立即输出最大容性无功
- 触发角调至最小(90°)
- TSC保持投入

响应时间：< 100 ms

### 恢复过程
电压恢复后：
- 逐渐调节回稳态
- 防止超调
- 平滑过渡

### 低电压特性
电压下降时电流能力：
$$I_{SVC} = B_{SVC}V$$

电流随电压线性下降，这是SVC与STATCOM的关键区别。

## 谐波模型

### 谐波源模型
TCR谐波电流源：
$$I_h = I_1 \cdot h_{factor}(\alpha)$$

等效谐波阻抗：
$$Z_h = \frac{V_h}{I_h}$$

### 滤波器设计
特征谐波滤波：
- 5次单调谐滤波器
- 7次单调谐滤波器
- 高通滤波器(11次及以上)

滤波器参数：
$$C_n = \frac{1}{(2\pi f_n)^2 L_n}$$
$$Q = \frac{\omega_n L}{R}$$

## 保护模型

### 过压保护
MOV保护：
$$I_{MOV} = k(V/V_{ref})^\alpha$$

### 过流保护
TCR过流：
$$I_{TCR} > 1.5I_N \Rightarrow \text{触发角移至180°}$$

### 不平衡保护
三相不平衡度：
$$K_{unb} = \frac{I_{neg}}{I_{pos}} > 10\% \Rightarrow \text{告警或退出}$$

## 参数设置

### 主电路参数

| 参数 | 符号 | 典型值 | 说明 |
|-----|------|-------|------|
| TCR电抗 | $X_L$ | 0.2-0.5 pu | 额定感性 |
| TSC电容 | $X_C$ | 0.2-0.5 pu | 每组容抗 |
| 阻尼电阻 | $R_d$ | 0.01-0.1 pu | TSC阻尼 |
| 额定电压 | $V_N$ | 6-35 kV | 母线电压 |
| 额定容量 | $Q_N$ | ±10-300 Mvar | 容性/感性 |

### 控制参数

| 参数 | 符号 | 典型值 | 说明 |
|-----|------|-------|------|
| 响应时间 | $\tau$ | 50-150 ms | 闭环响应 |
| 控制周期 | $T_s$ | 1-5 ms | 采样周期 |
| 斜率电抗 | $X_s$ | 1-5% | 电压调节斜率 |
| 死区 | $\Delta V_{db}$ | 0.5-1% | 防止频繁调节 |

## EMT仿真实现

### 详细模型
- 晶闸管详细模型
- 触发脉冲生成
- 保护逻辑
- 谐波滤波器

### 平均值模型
- 受控电纳等效
- 一阶惯性
- 适用于系统级研究

### 稳态模型
- 等效导纳
- 潮流计算
- 电压调节

## 相关模型
- [[svc-tcr-model]] - TCR模型
- `tsc-model` - TSC模型
- [[statcom-model]] - STATCOM模型
- [[facts]] - FACTS模型
- [[thyristor-control]] - 晶闸管模型

## 来源论文

参见 [[index]] 获取更多SVC模型相关文献。
