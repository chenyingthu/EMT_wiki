---
title: "静止同步补偿器 (STATCOM)"
type: model
tags: [statcom, svg, reactive-power, voltage-control, vsc, facts]
created: "2026-05-02"
---

# 静止同步补偿器 (STATCOM)


```mermaid
graph TD
    subgraph Ncmp[静止同步补偿器 (STATCOM)]
        N0[额定容量: $S_N$]
        N1[直流电压: $V_{dc}$]
        N2[开关频率: $f_{sw}$]
        N3[响应时间: $t_r$]
        N4[滤波电感: $L_f$]
        N5[损耗: $P_{loss}$]
    end
```


## 定义与边界

静止同步补偿器（Static Synchronous Compensator, STATCOM）是基于电压源换流器（VSC）的并联型柔性交流输电系统（FACTS）装置。通过向电网注入可控的无功电流，STATCOM能够快速、连续地调节节点电压，提供动态无功支撑。与传统SVC相比，STATCOM在电压跌落时仍能输出额定电流，具有更好的低电压特性。

**边界限定**：本页面聚焦于STATCOM的EMT建模与控制，不包括SVC或其他并联补偿装置。

## EMT中的作用

STATCOM是电压稳定控制的关键设备：

- **动态无功补偿**：快速响应电压变化，维持节点电压
- **电能质量改善**：抑制电压闪变、谐波和三相不平衡
- **故障电压支撑**：电网故障期间提供无功电流支撑
- **新能源并网**：风电场、光伏电站的电压调节
- **工业负荷补偿**：电弧炉、大型电机启动的电压波动抑制

## 基本结构

### 主电路拓扑

#### 两电平VSC结构
```
   DC电容        全桥逆变器        滤波电感      电网
   +----||----+   +--+--+--+     +--@@--+     +--o
   |          |   |  |  |  |     |     |     |
   |          H1--A  |  |  C1----L1----+-----Va
   |          |   |  B1 |  |     |     |
   |          H2--+  |  |  C2----L2----+-----Vb
   |          |   |  |  B2 |     |     |
   |          H3----+  |  C3----L3----+-----Vc
   |          |   |  |  |  |     |     |
   -----------+   +--+--+--+     +-----+     o--
```

主要元件：
- **直流侧**: 电容器组，电压 $V_{dc}$
- **换流桥**: 6个全控开关(IGBT/IGCT)
- **交流侧**: 滤波电感 $L_f$，滤除谐波
- **变压器**: 连接电抗/升压变

#### 多电平拓扑
对于高压大容量应用：

**三电平NPC**: 
- 开关器件数: 12
- 输出电平: 3
- 谐波特性: 优于两电平

**模块化多电平(MMC)**:
- 子模块级联
- 输出电平数: $2N+1$
- 谐波含量: < 3%
- [[mmc-model]] - MMC模型

### 关键参数

| 参数 | 符号 | 典型值 | 说明 |
|-----|------|-------|------|
| 额定容量 | $S_N$ | ±10-300 Mvar | 容性/感性 |
| 直流电压 | $V_{dc}$ | 10-100 kV | 取决于电压等级 |
| 开关频率 | $f_{sw}$ | 1-5 kHz | IGBT器件 |
| 响应时间 | $t_r$ | < 50 ms | 阶跃响应 |
| 滤波电感 | $L_f$ | 0.1-0.3 pu | 限制谐波电流 |
| 损耗 | $P_{loss}$ | 0.5-1.5% | 额定工况 |

## 工作原理

### 等效电路
STATCOM单相等效电路：

```
   Ṽ_out     jXf        Ṽ_grid
     o----@@----o-----------o
          |    |
         [If] |
          |    |
         ---  ---
          -    -
```

电压关系：
$$\tilde{V}_{out} = \tilde{V}_{grid} + jX_f \tilde{I}_f$$

### 功率交换
向电网注入的无功功率：
$$Q = \frac{V_{grid}(V_{out}\cos\delta - V_{grid})}{X_f}$$

有功功率（用于维持直流电压）：
$$P = \frac{V_{grid}V_{out}\sin\delta}{X_f}$$

其中：
- $\delta$: STATCOM输出电压与电网电压的相角差
- $X_f = \omega L_f$: 滤波电抗

### 工作模式

| 工作模式 | 条件 | 输出电流 | 功能 |
|---------|------|---------|------|
| 容性运行 | $V_{out} > V_{grid}$ | 容性 | 发出无功，支撑电压 |
| 感性运行 | $V_{out} < V_{grid}$ | 感性 | 吸收无功，降低电压 |
| 待机 | $V_{out} = V_{grid}$ | 接近0 | 零无功交换 |

### V-I特性
STATCOM的电压-电流特性：

```
I_q
  |      /¯¯¯¯¯¯¯¯¯¯\      感性极限
I_max |     /          \
  |    /            \
  |___/              \\____  线性区
      |               |
      |_______________| V_grid
      \              /
       \            /
        \__________/     容性极限
       -I_max
```

在电压下降时仍能维持额定电流输出，这是优于SVC的关键特性。

## 数学模型

### dq坐标系模型
采用电网电压定向的同步旋转坐标系：

电压方程：
$$L_f \frac{di_d}{dt} = -Ri_d + \omega L_f i_q + v_d - v_{gd}$$
$$L_f \frac{di_q}{dt} = -Ri_q - \omega L_f i_d + v_q - v_{gq}$$

其中：
- $v_{gd} = V_{grid}$, $v_{gq} = 0$（电压定向）
- $i_d$: 有功电流分量
- $i_q$: 无功电流分量

### 直流侧动态
$$C_{dc} \frac{dV_{dc}}{dt} = \frac{P_{in} - P_{out}}{V_{dc}}$$

功率平衡：
$$P_{dc} = V_{dc}I_{dc} = \frac{3}{2}(v_d i_d + v_q i_q)$$

### 线性化模型
在平衡点线性化：
$$\begin{bmatrix} \Delta\dot{i}_d \\ \Delta\dot{i}_q \\ \Delta\dot{V}_{dc} \end{bmatrix} = A \begin{bmatrix} \Delta i_d \\ \Delta i_q \\ \Delta V_{dc} \end{bmatrix} + B \begin{bmatrix} \Delta v_d \\ \Delta v_q \end{bmatrix}$$

状态矩阵：
$$A = \begin{bmatrix} -R/L_f & \omega & 0 \\ -\omega & -R/L_f & 0 \\ 3v_d/(2C_{dc}V_{dc}) & 3v_q/(2C_{dc}V_{dc}) & 0 \end{bmatrix}$$

## 控制系统

### 分层控制结构

#### 系统级控制
- 电压调节
- 无功功率控制
- 阻尼控制

#### 装置级控制
- 直流电压控制
- 电流内环控制
- 锁相环(PLL)

#### 设备级控制
- PWM调制
- 开关控制
- 保护逻辑

### 电压控制环
外环电压控制：
$$i_q^* = K_{pv}(V_{ref} - V_{grid}) + K_{iv}\int(V_{ref} - V_{grid})dt$$

典型参数：
- $K_{pv}$: 0.5-2.0 p.u.
- $K_{iv}$: 10-50 p.u./s
- 带宽: 10-50 Hz

### 电流内环控制
内环电流PI控制器：
$$v_d^* = K_{pc}(i_d^* - i_d) + K_{ic}\int(i_d^* - i_d)dt - \omega L_f i_q + v_{gd}$$
$$v_q^* = K_{pc}(i_q^* - i_q) + K_{ic}\int(i_q^* - i_q)dt + \omega L_f i_d + v_{gq}$$

前馈解耦项消除dq轴耦合。

典型参数：
- $K_{pc}$: 0.3-1.0 p.u.
- $K_{ic}$: 100-500 p.u./s
- 带宽: 200-1000 Hz

### 直流电压控制
维持直流侧电压恒定：
$$i_d^* = K_{pdc}(V_{dc}^* - V_{dc}) + K_{idc}\int(V_{dc}^* - V_{dc})dt$$

通过调节有功电流平衡换流器损耗。

### 锁相环(PLL)
电网同步：
$$\omega = \omega_0 + K_{p\omega}v_q + K_{i\omega}\int v_q dt$$
$$\theta = \int \omega dt$$

典型带宽: 20-100 Hz

## PWM调制

### SPWM调制
正弦脉宽调制：
$$m(t) = M \sin(\omega t + \phi)$$

调制比：
$$M = \frac{V_{out,1}}{V_{dc}/2}$$

$M \in [0, 1]$: 线性调制区
$M > 1$: 过调制区

### 三次谐波注入
提高直流电压利用率：
$$m_a(t) = M[\sin(\omega t) + k_3\sin(3\omega t)]$$

最大调制比提升至：
$$M_{max} = \frac{2}{\sqrt{3}} \approx 1.15$$

### 谐波特性
两电平STATCOM输出电压谐波：
$$V_n = \frac{4V_{dc}}{n\pi} J_0\left(\frac{n\pi M}{2}\right)$$

主要谐波: 载波频率附近 $(nf_c \pm kf_0)$

THD要求: < 5%

## 暂态特性

### 阶跃响应
无功电流阶跃响应时间：
$$t_r \approx \frac{3}{\omega_{bw}}$$

其中 $\omega_{bw}$ 为电流环带宽。

典型响应时间: 20-100 ms

### 故障响应
电压跌落时STATCOM支撑能力：

| 电压跌落 | 输出电流 | 支撑能力 |
|---------|---------|---------|
| 10% | 额定 | 100% |
| 30% | 额定 | 100% |
| 50% | 额定 | 100% |
| >50% | 保护动作 | 退出 |

### 低电压穿越
LVRT要求（根据电网标准）：
- 电压跌至20%时维持至少150-625 ms
- 期间持续输出无功电流
- 电压恢复后快速恢复运行

## 损耗模型

### 导通损耗
IGBT导通损耗：
$$P_{cond} = V_{ce0}I_{avg} + R_{ce}I_{rms}^2$$

二极管导通损耗：
$$P_{cond,D} = V_{f0}I_{avg} + R_fI_{rms}^2$$

### 开关损耗
IGBT开关损耗：
$$P_{sw} = f_{sw}(E_{on} + E_{off})\frac{I_{avg}}{I_{nom}}$$

总损耗：
$$P_{loss} = 6(P_{cond} + P_{sw})$$

典型效率: 98.5-99.5%

## 应用场景

### 电压支撑
- `voltage-stability` - 电压稳定
- 重载区电压调节
- 长距离输电补偿

### 电能质量
- `power-quality` - 电能质量
- 闪变抑制
- 谐波补偿
- 三相不平衡治理

### 新能源并网
- [[pmsg-offshore-wind-farm]] - 风电场
- [[pv-power-plant]] - 光伏电站
- 无功功率调节
- 电压波动平抑

### 工业应用
- [[a-time-domain-ac-electric-arc-furnace-model-for-flicker-planning-studies]] - 电弧炉
- 大型电机启动
- 冲击负荷补偿

## 与SVC对比

| 特性 | STATCOM | SVC |
|-----|---------|-----|
| 技术 | VSC-based | 晶闸管控制 |
| 响应速度 | < 50 ms | 1-2周波 |
| 低电压特性 | 恒流输出 | 电流下降 |
| 谐波特性 | 较好(滤波) | 较差 |
| 占地面积 | 小 | 大(电容器组) |
| 损耗 | 0.5-1.5% | 0.5-1.0% |
| 成本 | 较高 | 较低 |
| 有功能力 | 可四象限 | 仅无功 |

## 保护系统

### 过流保护
瞬时过流：
$$I > 1.5I_N$$

延时过流：
$$I > 1.2I_N$$

### 过压保护
直流过压保护：
$$V_{dc} > 1.2V_{dc,rated}$$

交流过压保护：
$$V_{ac} > 1.1V_{ac,rated}$$

### 温度保护
IGBT结温限制：
$$T_j < 125°C$$

冷却系统故障时退出运行。

## 仿真模型

### 平均值模型
忽略开关过程，等效为受控电压源：
$$\tilde{V}_{out} = \frac{m}{2}V_{dc}e^{j\theta}$$

适用于：
- 系统级研究
- 控制设计
- 机电暂态仿真

### 详细开关模型
包含IGBT开关特性：
- 开关函数模型
- 导通/关断瞬态
- 死区效应

适用于：
- 电磁暂态仿真
- 谐波分析
- 损耗计算

## 与相关页面的关系

- [[vsc-model]] - VSC换流器模型
- [[svc-model]] - SVC静止无功补偿器
- [[facts]] - FACTS柔性交流输电系统
- [[mmc-model]] - MMC模块化多电平换流器
- [[pll-model]] - 锁相环模型
- [[power-quality]] - 电能质量

## 代表性来源

- Schauder, C. and Mehta, H., "Vector Analysis and Control of Advanced Static VAR Compensators," *IEE Proceedings C*, 1993.
- Gyugyi, L., "Dynamic Compensation of AC Transmission Lines by Solid-State Synchronous Voltage Sources," *IEEE TPWRD*, 1994.

## 来源论文

参见 [[index]] 获取更多STATCOM相关文献。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of|Modeling of MMC-based STATCOM with embedded energy storage f]] | 2023 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
