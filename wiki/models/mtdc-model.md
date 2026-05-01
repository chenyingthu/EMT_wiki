---
title: "多端直流电网 (MTDC)"
type: model
tags: [mtdc, multi-terminal, dc-grid, vsc, mmc, droop-control]
created: "2026-04-29"
---

# 多端直流电网 (Multi-Terminal DC, MTDC)

## 定义与概述

多端直流电网（MTDC）是指具有三个及以上换流站互联的高压直流输电系统，支持多电源多负荷的功率交换和路径选择。与传统点对点HVDC相比，MTDC具有更高的灵活性和可靠性，是构建未来直流电网和汇集大规模新能源的关键技术。本模型涵盖并联型MTDC拓扑、直流潮流计算、下垂控制策略、直流故障分析，适用于柔性直流输电系统规划和运行分析。

## 1. 物理对象概述

### 1.1 功能与定义

多端直流电网是指具有**三个及以上换流站**互联的高压直流输电系统。与传统点对点HVDC相比，MTDC具有以下核心特征：

- **多电源多负荷**：支持多送端和多受端功率交换
- **功率路径选择**：直流潮流可在多端间动态分配
- **冗余与可靠性**：单端故障不影响其他端功率传输
- **新能源汇集**：适合分散式海上风电/光伏汇集

### 1.2 拓扑结构

#### 1.2.1 串联型MTDC

各换流站直流侧串联连接，电流相同，通过调节电压分配功率：

$$
V_{DC,total} = \sum_{i=1}^{n} V_{DC,i}, \quad I_{DC} = I_{DC,1} = I_{DC,2} = ... = I_{DC,n}
$$

**特点**：
- 绝缘要求高（需承受总电压）
- 扩展性差（新增站需停运）
- 现已很少采用

#### 1.2.2 并联型MTDC

各换流站直流侧并联连接，电压相同，电流分配功率：

$$
V_{DC,1} = V_{DC,2} = ... = V_{DC,n} = V_{DC,bus}
$$
$$
I_{DC,total} = \sum_{i=1}^{n} I_{DC,i}
$$

**主流拓扑**：
- 辐射状 (Radial)
- 环状 (Ring/Mesh)
- 网状 (Meshed)

#### 1.2.3 混合拓扑

**VSC-MMC混合**：
- 送端：LCC（大容量、远距离）
- 受端：VSC/MMC（弱网接入）
- 海上风电：二极管整流+MMC逆变

**AC-DC混合电网**：
- 直流网络作为交流电网的"主干"
- 交流配电网从直流母线取电

### 1.3 运行激励

**稳态激励**：
- 直流电压：±320kV / ±500kV / ±800kV
- 有功功率：数百MW至数千MW
- 无功功率：由换流站独立控制（VSC类型）

**暂态激励**：
- 直流故障：极间短路、极对地故障
- 交流故障：换相失败（LCC）、低电压穿越（VSC）
- 功率突变：新能源出力波动、负荷投切

**控制激励**：
- 主从控制（Master-Slave）
- 电压下垂控制（Voltage Droop）
- 功率/电压裕度控制（Margin Control）

## 2. 物理模型与数学描述

### 2.1 直流网络方程

#### 2.1.1 直流潮流方程

并联型MTDC的直流潮流由电阻网络决定：

$$\mathbf{P}_{DC} = \mathbf{V}_{DC} \odot \mathbf{Y}_{DC} \mathbf{V}_{DC}$$

其中：
- $\mathbf{P}_{DC} = [P_1, P_2, ..., P_n]^T$：各端注入功率
- $\mathbf{V}_{DC} = [V_1, V_2, ..., V_n]^T$：各端直流电压
- $\mathbf{Y}_{DC}$：直流网络导纳矩阵（由各支路电阻构成）

**展开形式**：
$$P_i = V_i \sum_{j=1}^{n} Y_{ij} (V_i - V_j) = V_i^2 \sum_{j \neq i} Y_{ij} - V_i \sum_{j \neq i} Y_{ij} V_j$$

#### 2.1.2 网络损耗

直流线路损耗：
$$P_{loss} = \sum_{i,j} R_{ij} I_{ij}^2 = \sum_{i,j} \frac{(V_i - V_j)^2}{R_{ij}}$$

总功率平衡：
$$\sum_{i=1}^{n} P_i = -P_{loss}$$

### 2.2 换流站模型

#### 2.2.1 VSC换流站模型

**功率方程**：
$$
P = \frac{3}{2} (v_d i_d + v_q i_q) = V_{DC} I_{DC}
$$
$$
Q = \frac{3}{2} (v_q i_d - v_d i_q)
$$

**下垂控制特性**（电压源模式）：
$$V_{DC} = V_{DC,ref} - k_d (P - P_{ref})$$

其中$k_d$为下垂系数（V/MW）。

#### 2.2.2 MMC换流站模型

**电容能量方程**：
$$\frac{d}{dt} \left( \frac{1}{2} C_{eq} V_{DC}^2 \right) = P_{AC} - P_{DC}$$

**桥臂动态**：
$$\frac{V_{DC}}{2} = v_{arm,u} + v_{arm,l} + L_{arm} \frac{d}{dt} i_{arm} + R_{arm} i_{arm}$$

### 2.3 控制策略模型

#### 2.3.1 主从控制 (Master-Slave)

**主站（电压控制）**：
$$V_{DC} = V_{DC,ref}, \quad P_m = -\sum_{i \neq m} P_i - P_{loss}$$

**从站（功率控制）**：
$$P_i = P_{i,ref}$$

**缺点**：主站故障导致全网失压

#### 2.3.2 电压下垂控制 (Voltage Droop)

各站共同参与电压调节：

$$V_{DC,i} = V_{DC}^* - k_{d,i} (P_i - P_i^*)$$

矩阵形式：
$$\begin{bmatrix} \Delta V_{DC,1} \\ \vdots \\ \Delta V_{DC,n} \end{bmatrix} = -\begin{bmatrix} k_{d,1} & & \\ & \ddots & \\ & & k_{d,n} \end{bmatrix} \begin{bmatrix} \Delta P_1 \\ \vdots \\ \Delta P_n \end{bmatrix}$$

**下垂系数设计**：
$$k_{d,i} = \frac{\Delta V_{DC,max}}{P_{i,rated}} \cdot \alpha_i$$

其中$\sum \alpha_i = 1$。

#### 2.3.3 电压裕度控制 (Voltage Margin)

结合主从与下垂优点：
- 正常运行：主站定电压，从站定功率
- 主站满载：从站切换为下垂模式接管电压控制

**切换逻辑**：
$$
\text{Mode} = \begin{cases}
\text{定电压}, & |P_m| < P_{m,max} \\
\text{下垂}, & |P_m| \geq P_{m,max}
\end{cases}$$

## 3. EMT仿真模型

### 3.1 详细电磁暂态模型

#### 3.1.1 换流站详细模型

**VSC详细模型**：
- IGBT/MOSFET开关器件
- PWM调制（载波频率1-2kHz）
- LCL滤波器
- 直流电容动态

**MMC详细模型**：
- 子模块电容（200-400个/桥臂）
- 开关函数控制
- 环流抑制控制
- 电容电压平衡

#### 3.1.2 直流线路模型

**分布参数模型**（长线路）：
$$\frac{\partial V}{\partial x} = -L \frac{\partial I}{\partial t} - RI$$
$$\frac{\partial I}{\partial x} = -C \frac{\partial V}{\partial t} - GV$$

**Bergeron模型**（中等距离）：
$$I_k(t) = Y_c V_k(t) + I_{hist,k}(t-\tau)$$

**π型等效**（短线路）：
$$Y_{eq} = \frac{1}{R + j\omega L} + j\omega C/2$$

#### 3.1.3 直流断路器模型

**机械式直流断路器**：
- 开断时间：20-30ms
- 需配合限流电抗器

**混合式直流断路器**：
- 主支路：机械开关（低损耗）
- 转移支路：电力电子开关（快速）
- 开断时间：2-5ms

**开断过程建模**：
$$I_{br}(t) = I_0 e^{-t/\tau} - \frac{V_{arc}}{R_{eq}} (1 - e^{-t/\tau})$$

### 3.2 平均值模型

#### 3.2.1 VSC平均值模型

**受控电压源形式**：
$$\mathbf{v}_{abc} = \frac{1}{2} m_{abc} \cdot V_{DC}$$

**直流侧电流**：
$$I_{DC} = \frac{3}{4} \sum_{k=a,b,c} m_k i_k$$

**适用于**：
- 系统级研究
- 控制策略验证
- 步长可达100-500μs

#### 3.2.2 MMC平均值模型

**桥臂电压**：
$$v_{arm} = n_{on} \cdot v_{C,arm}^{avg}$$

**等效电容**：
$$C_{eq} = \frac{C_{SM}}{N}$$

**状态空间表示**：
$$\dot{x} = A x + B u$$
$$y = C x + D u$$

其中状态变量包括桥臂电流、等效电容电压。

### 3.3 混合模型

**详细-平均值混合**：
- 故障点附近：详细模型
- 远端网络：平均值模型

**接口条件**：
$$V_{interface}^{detailed} = V_{interface}^{average}$$
$$I_{interface}^{detailed} = I_{interface}^{average}$$

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**组件配置**：
```
MTDC_NETWORK
├── VSC_1 (Master, Vdc control)
├── VSC_2 (Slave, P control)
├── VSC_3 (Slave, P control)
├── VSC_4 (Droop, Vdc-P droop)
├── DC_Cable_1-2 (R=0.01Ω/km, L=0.5mH/km)
├── DC_Cable_2-3 (...)
├── DC_Cable_3-4 (...)
└── DC_Cable_4-1 (...)
```

**控制实现**：
```fortran
! 下垂控制
Vdc_ref = Vdc_nom - K_droop * (P_meas - P_ref)

! 限幅
if (Vdc_ref > Vdc_max) Vdc_ref = Vdc_max
if (Vdc_ref < Vdc_min) Vdc_ref = Vdc_min
```

### 4.2 MATLAB/Simulink实现

**Simscape模型**：
```matlab
% MTDC网络初始化
net = dcmicrogrid;
net.addConverter('VSC1', 'Master', Vdc_nom, P_rating);
net.addConverter('VSC2', 'Droop', Vdc_nom, P_rating, K_droop);
net.addCable('Cable12', R12, L12, C12);
net.build();
```

**下垂控制器**：
```matlab
function Vdc_ref = droop_controller(P_meas, P_ref, Vdc_nom, K_d)
    Vdc_ref = Vdc_nom - K_d * (P_meas - P_ref);
end
```

### 4.3 实时仿真实现

**RTDS配置**：
- 每换流站分配1个GPC卡
- 直流网络采用分布参数线模型
- 步长：20-50μs

**FPGA加速**：
- 换流阀详细模型在FPGA实现
- 步长可达1-2μs
- 适合硬件在环测试

## 5. 典型参数参考

### 5.1 张北柔性直流电网（示范工程）

| 参数 | 数值 | 说明 |
|------|------|------|
| 额定电压 | ±500 kV | 双极运行 |
| 输送容量 | 4500 MW | 4端总容量 |
| 送端1 | 3000 MW | 新能源汇集 |
| 送端2 | 1500 MW | 调相机支撑 |
| 受端1 | 3000 MW | 北京负荷中心 |
| 受端2 | 1500 MW | 备用 |

**换流站参数**：
| 参数 | 数值 |
|------|------|
| 换流阀 | MMC |
| 子模块数 | 400/桥臂 |
| 子模块电容 | 12 mF |
| 桥臂电抗 | 100 mH |
| 控制策略 | 主从+下垂混合 |

### 5.2 欧洲超级电网（规划）

| 参数 | 数值 |
|------|------|
| 直流电压 | ±800 kV |
| 网络拓扑 | 网状（Meshed） |
| 换流站数 | 20+ |
| 总容量 | 100+ GW |

**电压等级规划**：
- 400 kV：近海风电汇集
- 800 kV：跨国主干输电
- 1500 kV：远距离大容量输电

### 5.3 仿真参数设置

**步长选择**：
| 研究类型 | 推荐步长 | 理由 |
|---------|---------|------|
| 直流故障分析 | 10-20 μs | 捕捉快速暂态 |
| 交流故障响应 | 20-50 μs | 中等频率 |
| 功率振荡 | 100-500 μs | 机电时间常数 |
| 能量管理 | 1-10 ms | 慢速控制 |

**线路模型选择**：
| 线路长度 | 推荐模型 | 说明 |
|---------|---------|------|
| < 50 km | π型等效 | 集总参数 |
| 50-300 km | Bergeron | 行波效应 |
| > 300 km | 频变模型 | 色散效应 |

## 6. 典型应用案例

### 6.1 海上风电汇集

**场景**：北海海上风电场（总容量10GW，分散在50个风电场）

**方案**：
- 风电场内部：33kV交流集电
- 升压：33kV→220kV交流
- 海上平台：AC/DC换流站
- 直流网络：±525kV，网状拓扑
- 陆上落点：3-4个受端换流站

**仿真重点**：
- 风电出力波动对直流电压的影响
- 下垂控制参数优化
- 直流故障隔离策略

### 6.2 城市直流配电网

**场景**：未来城市配电网，大量光伏+储能+电动车充电

**拓扑**：
```
AC Grid ←→ AC/DC ↔ DC Bus ↔ DC/DC ↔ EV Charging
                         ↕
                    DC/DC ↔ PV + Battery
```

**仿真关注点**：
- 功率双向流动控制
- 多层级下垂控制协调
- 直流故障定位与隔离

### 6.3 异步电网互联

**场景**：将不同步的三个交流电网（如华北、华中、华东）通过MTDC互联

**优势**：
- 避免交流联网的稳定性问题
- 紧急功率支援
- 频率支撑

**仿真内容**：
- 频率下垂控制设计
- 暂态稳定性分析
- 功率调制能力

## 7. 前沿研究方向

### 7.1 直流故障处理

**故障清除难题**：
- 直流故障电流无自然过零点
- 需快速隔离（<10ms）
- 混合式直流断路器成本高

**研究方向**：
- 限流电抗器优化
- 故障限流器（FCL）
- 低电压穿越策略
- 故障自愈技术

### 7.2 高比例新能源接入

**挑战**：
- 新能源出力波动→直流电压波动
- 弱惯性系统稳定性
- 功率预测误差

**解决方案**：
- 储能平滑控制
- 虚拟同步机控制（VSM）
- 多时间尺度优化

### 7.3 直流电网保护

**保护难点**：
- 故障电流大、上升快
- 线路阻抗小，故障定位困难
- 需要选择性保护

**研究进展**：
- 行波保护
- 差动保护
- 通信辅助保护
- 人工智能故障诊断

## 8. 相关主题与链接

### 8.1 相关模型
- [[vsc-model|VSC模型]] - 电压源换流器详细模型
- [[mmc-model|MMC模型]] - 模块化多电平换流器
- [[lcc-model|LCC模型]] - 线路换相换流器
- [[transmission-line-model|输电线路模型]] - 直流线路建模

### 8.2 相关方法
- 下垂控制 - 直流电网电压控制策略
- 潮流计算 - 直流电网稳态分析
- 故障分析 - 直流故障特性与保护

### 8.3 相关主题
- [[vsc-hvdc|VSC-HVDC]] - 柔性直流输电技术
- 海上风电 - 海上风电汇集与输送
- 直流保护 - 直流电网保护技术
- 交直流混合电网 - 未来电网架构

### 7.4 适用边界与限制

#### 7.4.1 适用条件
- **电压等级**：±320kV至±800kV（柔性直流）
- **功率范围**：100MW至10GW
- **换流站数**：3-20个（多端定义）
- **控制模式**：主从控制、下垂控制、裕度控制

#### 7.4.2 模型限制
- **直流故障**：故障电流上升极快，模型需极小时步
- **换流器非线性**：线性化模型仅适用于小扰动
- **电缆模型**：长电缆行波效应复杂
- **保护配合**：直流保护选择性难以保证

#### 7.4.3 精度边界
| 模型类型 | 直流电压 | 功率分配 | 故障电流 | 适用场景 |
|---------|---------|---------|---------|---------|
| 详细MMC | ±1% | ±2% | 精确 | 设备级 |
| 平均值 | ±3% | ±5% | ±10% | 系统级 |
| 直流潮流 | ±5% | ±3% | - | 稳态分析 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| A unified droop control strategy for VSC-MTDC | 2018 | 基于电压裕度的统一下垂控制策略 |
| Multi-terminal DC grids: Modeling, analysis and control | 2020 | MTDC建模、分析与控制的综合综述 |
| A review on protection of meshed multi-terminal HVDC systems | 2021 | 网状MTDC系统保护技术综述 |
| Impedance-based stability analysis of multi-terminal cascaded hybrid HVDC | 2025 | 多端口级联混合HVDC的阻抗稳定性分析 |

## 相关方法
- [[average-value-model|平均值模型]] - MTDC平均值简化
- [[state-space-method|状态空间法]] - MTDC状态空间建模
- [[droop-control-model|下垂控制]] - 直流电压下垂控制
- [[multirate-method|多速率方法]] - 多换流站多速率仿真

## 相关模型
- [[mmc-model|MMC模型]] - MMC-MTDC核心设备
- [[vsc-model|VSC模型]] - VSC-MTDC两电平换流器
- [[lcc-model|LCC模型]] - LCC-MTDC传统HVDC
- [[cable-model|电缆模型]] - 直流电缆建模

## 相关主题
- [[vsc-hvdc]] - 柔性直流输电
- [[co-simulation]] - MTDC多域混合仿真
- [[real-time-simulation]] - MTDC实时仿真
- [[network-equivalent]] - MTDC网络等值
- [[parallel-computing]] - MTDC并行计算

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
