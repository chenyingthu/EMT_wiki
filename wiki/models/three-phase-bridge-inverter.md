---
title: "三相桥式逆变器 (Three-Phase Bridge Inverter)"
type: model
tags: [three-phase, bridge, inverter, vsc, pwm, igbt]
created: "2026-05-02"
---

# 三相桥式逆变器 (Three-Phase Bridge Inverter)

## 概述

三相桥式逆变器是电力电子变流器的标准拓扑结构，由六个开关器件组成三相全桥，实现直流到三相交流的电能转换。该拓扑广泛应用于电机驱动、新能源并网、UPS电源和电能质量治理等领域，是现代电力电子技术的核心组成部分。

## 基本拓扑

### 电路结构
```
        S1    S3    S5
         ┬     ┬     ┬
    DC+ ─┴─C─┴─C─┴─C┴─ DC-
         │     │     │
         ├──La─┼─Lb─┼─Lc─┤ → 三相输出
         │     │     │
        S4    S6    S2
         ┴     ┴     ┴
```

开关编号(典型)：
- 上桥臂：S1, S3, S5
- 下桥臂：S4, S6, S2

### 开关组合
三相桥臂开关状态：

| 状态 | S1 | S3 | S5 | 电压矢量 |
|-----|----|----|----|---------|
| V0(000) | 0 | 0 | 0 | 零矢量 |
| V1(100) | 1 | 0 | 0 | Ua = +Vdc |
| V2(110) | 1 | 1 | 0 | 有效矢量 |
| V3(010) | 0 | 1 | 0 | Ub = +Vdc |
| V4(011) | 0 | 1 | 1 | 有效矢量 |
| V5(001) | 0 | 0 | 1 | Uc = +Vdc |
| V6(101) | 1 | 0 | 1 | 有效矢量 |
| V7(111) | 1 | 1 | 1 | 零矢量 |

共8种开关状态。

### 电压矢量
空间电压矢量：
$$\vec{V} = \frac{2}{3}(v_{aN} + v_{bN}e^{j120°} + v_{cN}e^{j240°})$$

非零矢量(六边形顶点)：
$$\vec{V}_k = \frac{2}{3}V_{dc}e^{j(k-1)60°}, \quad k=1,2,...,6$$

幅值：
$$|V_k| = \frac{2}{3}V_{dc}$$

零矢量：
$$\vec{V}_0 = \vec{V}_7 = 0$$

## 工作原理

### 180°导通方式
每管导通180°：
- 三管同时导通
- 无死区
- 线电压六阶梯波

相电压波形：
- 五电平：+Vdc, +Vdc/2, 0, -Vdc/2, -Vdc
- 120°对称

### 120°导通方式
每管导通120°：
- 两管同时导通
- 有死区
- 线电压准方波

### PWM调制

#### SPWM调制
正弦波调制：
$$m_a = M\sin(\omega t)$$
$$m_b = M\sin(\omega t - 120°)$$
$$m_c = M\sin(\omega t - 240°)$$

调制比：
$$M = \frac{V_{ref}}{V_{tri}}$$

输出电压：
$$V_{LL,rms} = \frac{\sqrt{3}}{2\sqrt{2}}MV_{dc} = 0.612MV_{dc}$$

最大M=1时：
$$V_{LL,rms,max} = 0.612V_{dc}$$

#### SVPWM调制
空间矢量调制：
- 参考矢量分解
- 相邻矢量合成
- 零矢量调节

电压利用率：
$$V_{LL,rms,max} = \frac{V_{dc}}{\sqrt{2}} = 0.707V_{dc}$$

比SPWM高15.5%。

### 谐波分析
SPWM输出谐波：
$$V_n = \frac{2V_{dc}}{n\pi}J_0\left(\frac{n\pi M}{2}\right)$$

主要谐波：
- 载波频率附近
- 边带谐波
- 开关频率整数倍

## 数学模型

### 开关函数模型
相电压：
$$v_{aN} = (S_a - \frac{S_a+S_b+S_c}{3})V_{dc}$$

线电压：
$$v_{ab} = (S_a - S_b)V_{dc}$$

### 平均模型
开关周期平均：
$$\bar{v}_{aN} = d_aV_{dc}$$

占空比：
$$d_a = \frac{1}{T_{sw}}\int_0^{T_{sw}}S_a(t)dt$$

### dq坐标模型
Park变换：
$$\begin{bmatrix} v_d \\ v_q \\ v_0 \end{bmatrix} = \frac{2}{3}\begin{bmatrix}
\cos\theta & \cos(\theta-120°) & \cos(\theta+120°) \\
-\sin\theta & -\sin(\theta-120°) & -\sin(\theta+120°) \\
\frac{1}{2} & \frac{1}{2} & \frac{1}{2}
\end{bmatrix}\begin{bmatrix} v_a \\ v_b \\ v_c \end{bmatrix}$$

直流母线电压关系：
$$\sqrt{v_d^2 + v_q^2} \leq \frac{V_{dc}}{\sqrt{3}}$$

## 控制系统

### 电压控制环
PI控制器：
$$v_{d,q}^* = K_p(v_{d,q,ref} - v_{d,q}) + K_i\int(v_{d,q,ref} - v_{d,q})dt$$

### 电流内环
解耦控制：
$$v_d^* = v_{gd} - \omega Li_q + K_p(i_d^* - i_d)$$
$$v_q^* = v_{gq} + \omega Li_d + K_p(i_q^* - i_q)$$

### 直流电压控制
有功电流：
$$i_d^* = K_p(V_{dc,ref} - V_{dc}) + K_i\int(V_{dc,ref} - V_{dc})dt$$

## 应用领域

### 电机驱动
感应电机：
- V/f控制
- 矢量控制
- 直接转矩控制

同步电机：
- 永磁同步电机
- 电励磁同步电机

### 新能源并网
光伏逆变器：
- MPPT控制
- 并网同步
- 无功调节

风电变流器：
- 全功率变流
- 双馈变流器

### UPS电源
在线式UPS：
- 整流+逆变
- 电池管理
- 并机技术

### 电能质量
APF：
- 谐波补偿
- 无功补偿
- 不平衡补偿

## 参数设计

### 滤波器设计
L滤波器：
$$L = \frac{V_{dc}}{2\sqrt{3}I_{ripple}f_{sw}}$$

LC滤波器：
$$\omega_{res} = \frac{1}{\sqrt{LC}}$$

谐振频率：
$$10f_{grid} < f_{res} < \frac{f_{sw}}{2}$$

### 开关频率
选择考虑：
- 损耗：随频率增加
- 谐波：随频率减小
- 效率与性能平衡

典型值：
- IGBT：2-20 kHz
- MOSFET：20-100 kHz
- SiC：50-200 kHz

## 保护系统

### 过流保护
瞬时值限流：
$$|i| < I_{max}$$

有效值保护：
$$I_{rms} < I_{rated}$$

### 过压保护
直流过压：
$$V_{dc} < V_{dc,max}$$

交流过压：
$$V_{ac} < V_{ac,max}$$

### 过温保护
结温限制：
$$T_j < T_{j,max}$$

热管理：
- 散热器设计
- 风冷/水冷
- 温度监测

## 相关模型
- [[vsc-model]] - VSC模型
- `pwm-modulation` - PWM调制
- `svpwm` - SVPWM
- `inverter-control` - 逆变器控制

## 来源论文

参见 [[index]] 获取更多三相桥式逆变器相关文献。
