---
title: "晶闸管可控串联电容模型 (TCSC Model)"
type: model
tags: [tcsc, model, facts, series-compensation, thyristor, impedance-control, ssr]
created: "2026-05-02"
---

# 晶闸管可控串联电容模型 (TCSC Model)

## 概述

TCSC(Thyristor Controlled Series Capacitor)模型用于电磁暂态仿真中描述晶闸管可控串联电容的动态特性。TCSC通过控制晶闸管的触发角来连续调节串联补偿度，具有响应速度快、控制灵活等特点。根据研究目的不同，TCSC模型可分为详细开关模型、可变阻抗模型和等效模型三个层次。

## 主电路结构

### 基本拓扑
```
线路电流  →  ───┬───C───┬───  →  线路电流
              │       │
             L        │
              │       │
             T1      T2
              │       │
              ┴───────┴
```

其中：
- **C**: 固定串联电容
- **L**: 晶闸管控制电抗器(TCR)
- **T1, T2**: 反并联晶闸管
- **旁路开关**: 故障保护

### 工作模式

| 模式 | 触发角 | 等效阻抗 | 应用 |
|-----|-------|---------|------|
| 旁路 | $\alpha = 0°$ | 感性小电抗 | 线路保护 |
| 容性调节 | 90°-180° | 可变电容 | 正常运行 |
| 感性调节 | 0°-90° | 可变电感 | 特殊工况 |
| 阻断 | 无触发 | $X_C$ | 固定补偿 |

## 详细开关模型

### 晶闸管模型
开关函数：
$$S_{thy} = \begin{cases} 1 & \text{导通} \\ 0 & \text{关断} \end{cases}$$

触发条件：
- 正向电压
- 门极触发脉冲

关断条件：
- 电流过零
- 反向电压建立

### 电路方程
导通期间：
$$L\frac{di_L}{dt} = v_C$$

电容电流：
$$i_C = C\frac{dv_C}{dt} = i_{line} - i_L$$

线路电压：
$$v_{TCSC} = v_C = \frac{1}{C}\int i_C dt$$

### 触发控制
触发角定义：
- $\alpha = 0°$: 电压过零点
- $\alpha = 90°$: 电压峰值点
- $\alpha = 180°$: 下一过零点

触发时刻：
$$t_{fire} = \frac{\alpha}{\omega} + \frac{n\pi}{\omega}$$

其中n为半波序号。

### 数值仿真
固定步长处理：
- 步长 $\Delta t < T/100$
- 典型值：10-100 μs
- 插值精确捕捉触发时刻

## 阻抗特性分析

### 稳态阻抗公式
TCSC基波等效阻抗：
$$X_{TCSC}(\alpha) = X_C - \frac{X_C X_L}{X_C - X_L} \cdot \frac{\sigma + \sin\sigma}{\pi}$$

其中：
- $\sigma = 2(\pi - \alpha)$: 导通角
- $X_C = -1/(\omega C)$: 容抗
- $X_L = \omega L$: 感抗

### 谐振点
当 $X_{TCSC} = 0$ 时发生谐振：
$$\frac{X_C X_L}{X_C - X_L} = X_C$$

解得：
$$X_C = \frac{X_L}{2}$$

或：
$$\omega_0 = \sqrt{\frac{2}{LC}}$$

谐振触发角：
$$\alpha_{res} = \arccos\left(-\frac{\pi}{2\omega_0^2LC - 2}\right)$$

### 阻抗-触发角曲线

| 触发角 | 阻抗特性 | 补偿度 |
|-------|---------|-------|
| 0° | 小感性 | 接近旁路 |
| 90° | 纯容性 | 最大电容 |
| 90°-180° | 容性减小 | 调节范围 |
| 谐振点 | 无穷大 | 不可用 |

### 感性工作区
当 $\alpha < 90°$：
$$X_{TCSC}(\alpha) = X_L \cdot \frac{\sigma - \sin\sigma}{\pi}$$

呈感性特性，用于特殊工况。

## 可变阻抗模型

### 一阶惯性模型
$$\tau\frac{dX_{TCSC}}{dt} + X_{TCSC} = X_{ref}$$

其中：
- $\tau$: 响应时间常数(20-100 ms)
- $X_{ref}$: 阻抗参考值

### 限幅环节
阻抗约束：
$$X_{min} \leq X_{TCSC} \leq X_{max}$$

典型值：
- $X_{min}$: 0.2-0.5 $X_C$
- $X_{max}$: 2.0-3.0 $X_C$

变化速率限制：
$$\left|\frac{dX_{TCSC}}{dt}\right| \leq \dot{X}_{max}$$

### 同步振荡
考虑TCSC内部振荡：
$$\frac{d^2X_{TCSC}}{dt^2} + 2\xi\omega_n\frac{dX_{TCSC}}{dt} + \omega_n^2X_{TCSC} = \omega_n^2X_{ref}$$

固有频率：
$$\omega_n = \sqrt{\frac{1}{LC}}$$

## 控制系统模型

### 阻抗控制
PI控制器：
$$\alpha = K_p(X_{ref} - X_{TCSC}) + K_i\int(X_{ref} - X_{TCSC})dt$$

逆查表法：
- 预存 $\alpha$-$X_{TCSC}$ 关系
- 根据 $X_{ref}$ 查表得 $\alpha_{ref}$
- 线性插值提高精度

### 潮流控制
功率反馈：
$$X_{ref} = K_p(P_{ref} - P_{line}) + K_i\int(P_{ref} - P_{line})dt$$

线路功率：
$$P = \frac{V_1 V_2}{X_{line} - X_{TCSC}}\sin\delta$$

### 阻尼控制
功率振荡阻尼：
$$\Delta X_{TCSC} = K_d \frac{sT_w}{1+sT_w} \frac{1+sT_1}{1+sT_2} P_{line}$$

调节TCSC阻抗提供振荡阻尼。

### 同步信号
电压过零检测：
- 锁相环(PLL)同步
- 线路电流过零
- 电容电压过零

## 次同步振荡(SSR)模型

### SSR机理
TCSC与汽轮发电机组轴系相互作用：
$$f_{sub} + f_e = f_m$$

其中：
- $f_{sub}$: 次同步频率(10-50 Hz)
- $f_e$: 电网频率(50/60 Hz)
- $f_m$: 轴系扭振频率

### 电气阻尼
次同步频段阻抗：
$$Z_{sub}(f_{sub}) = R_{sub}(f_{sub}) + jX_{sub}(f_{sub})$$

负阻尼判据：
$$R_{sub}(f_{sub}) < 0$$

TCSC可能提供负阻尼。

### SSR抑制模型
主动阻尼控制：
$$X_{TCSC} = X_0 + \Delta X_d$$

阻尼调制：
$$\Delta X_d = K_{SSR}\Delta\omega_{shaft}$$

通过轴系转速反馈提供正阻尼。

### 保护逻辑
SSR检测与保护：
- 次同步电流监测
- 轴系扭振监测
- 阻抗快速调节
- 旁路保护

## 保护模型

### 过压保护
MOV(金属氧化物避雷器)模型：
$$I_{MOV} = k\left(\frac{V}{V_{ref}}\right)^\alpha$$

动作条件：
$$V_C > V_{MOV,ref}$$

### 旁路保护
旁路开关动作：
- 过流保护
- 过压保护
- 保护动作延时
- 重合闸逻辑

### 晶闸管保护
- 过流保护
- du/dt保护
- di/dt保护
- 温度保护

## 参数设置

### 主电路参数

| 参数 | 符号 | 典型值 | 说明 |
|-----|------|-------|------|
| 电容 | C | 50-500 μF | 基波容抗 |
| 电感 | L | 5-50 mH | TCR电抗 |
| 额定电流 | $I_N$ | 1-5 kA | 线路电流 |
| 额定电压 | $V_N$ | 10-100 kV | 电容电压 |

### 控制参数

| 参数 | 符号 | 典型值 | 说明 |
|-----|------|-------|------|
| 响应时间 | $\tau$ | 20-100 ms | 一阶惯性 |
| 控制周期 | $T_s$ | 0.5-2 ms | 采样周期 |
| 最小阻抗 | $X_{min}$ | 0.3 $X_C$ | 下限 |
| 最大阻抗 | $X_{max}$ | 2.5 $X_C$ | 上限 |
| 变化速率 | $\dot{X}_{max}$ | 10-50 $X_C$/s | 速率限制 |

## EMT仿真实现

### 伴随模型
梯形法离散化：
$$G_{eq} = \frac{\Delta t}{2L}$$
$$I_{hist} = -i_L(t-\Delta t) - G_{eq}v_L(t-\Delta t)$$

开关处理：
- 导通: 小电阻等效(0.01 Ω)
- 关断: 大电阻等效(1 MΩ)

### 多速率仿真
TCSC与系统多速率：
- 系统步长：50-100 μs
- TCSC步长：1-10 μs
- 接口插值

## 模型验证

### 稳态验证
- 阻抗-触发角特性
- 谐波含量
- 损耗特性

### 动态验证
- 阶跃响应
- 频率响应
- SSR特性

### 现场验证
- 阻抗测量
- 控制响应
- 保护配合

## 相关模型
- [[svc-model]] - SVC模型
- [[facts]] - FACTS模型
- [[thyristor-control]] - 晶闸管模型
- `series-compensation` - 串联补偿
- `ssr-analysis` - SSR分析

## 来源论文

参见 [[index.md]] 获取更多TCSC模型相关文献。
