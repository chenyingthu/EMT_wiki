---
title: "电力电子变压器 (PET/SST)"
type: model
tags: [pet, sst, solid-state-transformer, power-electronics, high-frequency, isolation]
created: "2026-04-29"
updated: "2026-05-12"
---

# 电力电子变压器 (Power Electronic Transformer / Solid-State Transformer)




## 定义与概述

电力电子变压器（PET）也称固态变压器（SST），是基于电力电子技术的新型智能变压器，通过AC-DC-AC多级变换实现电压等级转换和电气隔离。相比传统变压器，PET具有体积重量小、功率双向流动、功率因数可控、谐波隔离和故障限流等优势。本模型涵盖DAB/CLLC隔离级拓扑、移相控制、整流级和逆变级控制，适用于配电系统、新能源接入和电动汽车充电应用。

## 1. 物理对象概述

### 1.1 功能与定义

电力电子变压器（PET）也称固态变压器（SST），是基于电力电子技术的新型智能变压器：

**核心功能**：
- **电压变换**：AC-DC-AC多级变换，实现电压等级转换
- **电气隔离**：高频隔离，体积重量大幅减小
- **功率双向流动**：支持能量双向传输
- **功率因数校正**：网侧单位功率因数
- **谐波隔离**：阻止谐波传播
- **故障限流**：限流保护功能

**与传统变压器对比**：
| 特性 | 传统变压器 | 电力电子变压器 |
|------|-----------|--------------|
| 频率 | 50/60Hz | 高频(10-100kHz) |
| 体积/重量 | 基准 | 1/5 - 1/10 |
| 效率 | 98-99% | 96-98% |
| 功率流向 | 单向 | 双向 |
| 功率因数 | 负载决定 | 可控(≈1) |
| 谐波 | 传递 | 隔离 |
| 保护功能 | 无 | 故障限流 |
| 成本 | 低 | 高(5-10倍) |

### 1.2 拓扑结构

#### 1.2.1 三级式PET (AC-DC-DC-AC)

```
AC Input → Rectifier → DC Link 1 → DAB → DC Link 2 → Inverter → AC Output
                           ↕
                    High Freq Transformer
```

**各级功能**：
1. **整流级**：AC/DC变换，功率因数校正
2. **隔离级**：DC/DC变换，高频隔离
3. **逆变级**：DC/AC变换，输出电压控制

#### 1.2.2 典型隔离级拓扑

**DAB (Dual Active Bridge)**：
- 双H桥+高频变压器
- 移相控制功率传输
- 软开关能力（ZVS）

**CLLC谐振变换器**：
- 谐振槽实现软开关
- 高效率（>98%）
- 适合宽电压范围

**双有源桥+串联谐振**：
- 变频控制
- 双向功率传输
- 变压器漏感利用

### 1.3 运行激励

**电压等级**：
- 输入：10kV/35kV中压
- 输出：380V/750V低压
- 中间直流：1000-4000V

**功率等级**：
- 分布式：10-100kW
- 配电级：100kW-1MW
- 牵引应用：1-5MW

**控制目标**：
- 网侧：单位功率因数、低THD
- 隔离级：软开关、高效率
- 负荷侧：电压稳定、快速响应

## 2. 物理模型与数学描述

### 2.1 DAB变换器模型

#### 2.1.1 基本工作原理

**H桥输出电压**：
$$v_{p} = V_{dc1} \cdot s_1(t), \quad s_1 \in \{-1, 0, 1\}$$
$$v_{s} = n \cdot V_{dc2} \cdot s_2(t), \quad s_2 \in \{-1, 0, 1\}$$

其中$n$为变压器变比，$s_1, s_2$为开关函数。

**变压器方程**：
$$v_{p} - v_{s} = L_{leak} \frac{di_L}{dt}$$

其中$L_{leak}$为折算到原边的漏感。

#### 2.1.2 移相控制

**单移相(SPS)控制**：

副边相对原边移相角$\phi$，传输功率：
$$P = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \phi (1 - \frac{|\phi|}{\pi})$$

其中$f_s$为开关频率，$\phi \in [-\pi/2, \pi/2]$。

**功率方向**：
- $\phi > 0$：正向传输（原边→副边）
- $\phi < 0$：反向传输（副边→原边）

**回流功率**：
$$Q = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \left[\phi(1-\frac{\phi}{\pi}) - \frac{d(1-d)^2\pi}{4}\right]$$

其中$d = V_{dc2}/(nV_{dc1})$为电压传输比。

#### 2.1.3 扩展移相(EPS)控制

内移相$\phi_1$（原边H桥）和外移相$\phi_2$（两桥间）：
$$P = \frac{n V_{dc1} V_{dc2}}{2 f_s L_{leak}} \phi_2 (1 - \phi_2 - \frac{\phi_1}{2})$$

**优势**：减小回流功率，提高效率

### 2.2 CLLC谐振变换器模型

#### 2.2.1 谐振槽参数

谐振频率：
$$f_r = \frac{1}{2\pi \sqrt{L_r C_r}}$$

归一化频率：
$$F = \frac{f_s}{f_r}$$

**电压增益**：
$$M_g = \frac{V_{out}}{n V_{in}} = \frac{1}{\sqrt{(1 + k - \frac{k}{F^2})^2 + Q^2 (F - \frac{1}{F})^2}}$$

其中：
- $k = L_m/L_r$：电感比
- $Q = \sqrt{L_r/C_r}/R_{eq}$：品质因数

#### 2.2.2 软开关条件

**原边ZVS条件**：
$$f_s \geq f_r \quad \text{或} \quad I_{mag} > \frac{2 C_{oss} V_{dc}}{t_{dead}}$$

**副边ZCS条件**（同步整流）：
$$f_s \leq f_r$$

### 2.3 整流级模型

#### 2.3.1 两电平整流器

**电压方程**：
$$v_{abc} = R_f i_{abc} + L_f \frac{di_{abc}}{dt} + v_{conv,abc}$$

**调制电压**：
$$v_{conv} = m \cdot \frac{V_{dc}}{2}$$

**功率平衡**：
$$P_{ac} = \frac{3}{2} V_{sd} I_{sd} = V_{dc} I_{dc} = P_{dc}$$

#### 2.3.2 级联H桥整流器

用于中压输入（10kV+），每相多模块串联：
$$V_{phase} = \sum_{i=1}^{N} V_{H,i} = N \cdot m_i \cdot V_{dc,mod}$$

模块数：$N \approx V_{LL}/(V_{IGBT,rated})$，典型为10-20级

## 3. EMT仿真模型

### 3.1 详细开关模型

**整流级**：
- IGBT/MOSFET开关器件
- PWM调制（载波频率2-20kHz）
- LCL滤波器

**隔离级**：
- 高频变压器（铁氧体磁芯）
- DAB/CLLC拓扑
- 开关频率10-100kHz

**逆变级**：
- 两电平/三电平拓扑
- 输出LC滤波
- 电压/电流双环控制

### 3.2 平均值模型

**整流级等效**：
- 受控电流源：$i_d = k_p(v_{dc}^* - v_{dc}) + k_i \int (v_{dc}^* - v_{dc})dt$
- 功率因数≈1

**隔离级等效**：
- 理想变压器+等效阻抗
- 效率损失：$P_{loss} = (1-\eta) P_{rated} (P/P_{rated})^2$

**逆变级等效**：
- 受控电压源：$v_{out} = v_{ref}$
- 响应延时：1-2个开关周期

### 3.3 恒导纳模型

适用于大规模系统仿真：

**整流级**：
$$G_{eq} = \frac{3}{2} \frac{m^2}{R_{eq}}$$

**隔离级**：
$$G_{eq,DAB} = \frac{P}{V_{dc1}^2 - V_{dc2}^2/n^2}$$

## 4. 典型参数

### 4.1 10kV/400V配电级PET

| 参数 | 数值 | 单位 |
|------|------|------|
| 额定功率 | 100 | kW |
| 输入电压 | 10 | kV |
| 输出电压 | 380/400 | V |
| 中间直流 | 1500 | V |
| 开关频率(整流) | 10 | kHz |
| 开关频率(DAB) | 20 | kHz |
| 变压器频率 | 20 | kHz |
| 效率 | 96-97 | % |
| 功率密度 | 3-5 | kW/kg |

**模块配置**：
- 整流级：级联H桥，每相12模块
- 隔离级：12个DAB并联
- 逆变级：三相两电平逆变器

### 4.2 模型选择指南

| 应用场景 | 推荐模型 | 步长 |
|---------|---------|------|
| 软开关分析 | 详细开关 | 100ns-1μs |
| 控制验证 | 平均值 | 10-100μs |
| 系统级研究 | 等效功率源 | 100-500μs |
| 电能质量 | 谐波源模型 | 10μs |

### 4.3 损耗构成

| 损耗类型 | 占比 | 说明 |
|---------|------|------|
| IGBT导通 | 30-40% | $I^2 R_{on}$ |
| IGBT开关 | 25-35% | 开关瞬态 |
| 变压器 | 15-25% | 铁损+铜损 |
| 电感/电容 | 5-10% | 寄生电阻 |
| 其他 | 5% | 辅助电源等 |

## 5. 适用边界与限制

### 5.1 适用条件
- **功率等级**：10kW-10MW（配电级，高压输电需级联）
- **电压等级**：输入≤35kV，输出≤1kV（低压配电）
- **开关频率**：整流级2-20kHz，隔离级10-100kHz
- **控制模式**：正常双向运行，支持孤岛和并网模式

### 5.2 模型限制
- **开关细节**：平均值模型不捕捉开关瞬态
- **磁芯非线性**：简化磁芯模型，饱和特性需单独考虑
- **热效应**：损耗-热耦合简化处理
- **故障保护**：内部故障模型需额外开发

## 量化性能边界

**Gao 2022 SST高频链路加速等效模型**（DAB功率模块，MMC型SST）:
- 基于节点导纳方程预处理与Kron消去法，消除DAB模块内部节点，构建多端口等效电路
- 仿真速度较详细模型提升 **1~2个数量级**（10~100倍），特定工况可达2~3个数量级
- 利用IGBT互补导通特性（$G_{ON}+G_{OFF}=G_x$为常数），实现单步矩阵求逆运算量为0
- 支持ISOP/ISOS/IPOP/IPOS等多种串并联连接配置的参数统一转换
- 验证平台：PSCAD/EMTDC + 硬件实验验证，端口波形与详细模型高度一致
- 数据缺口：速度提升范围（1~2个数量级）来自摘要概述，原文未在不同SST功率等级下给出精确加速比

**Li 2026 SFB-DEM + ImEx-Gear实时仿真模型**（60模块ISOP SST, OPAL-RT）:
- 采用隐显多步Gear法，实现 **171x** 加速比（vs 详细模型）， **7.5x**（vs VG-DEM传统戴维南等效）
- **3阶ImEx-G3O**格式，稳态误差 **<0.5%**，开关定位精度<1μs
- 恒定导纳矩阵 + 节点缩减约 **60%**，单步计算复杂度从 $O(N^3)$ 降至 $O(N)$
- 数据缺口：验证仅基于60 SM ISOP SST，故障工况和非线性磁芯尚未验证

**Li 2025 通用解耦等效电路模型**（SFB-DEM / SFB-AVM, ISOP SST）:
- SFB-DEM节点数从 **6N+1降至2N+3**，SFB-AVM进一步降至 **3-5节点**
- 恒定等效导纳 $G_{eq}=C/h$，导纳矩阵呈块对角（三级独立）
- 步长20-50μs时波形偏差 **<0.5%**（vs 1μs详细模型），相关系数>0.99
- 验证平台：PSCAD/EMTDC，10相FBSM + 30 DAB + NPC三电平
- 数据缺口：保护继电器配合、其他硬件平台（RTDS/FPGA）未覆盖

**Wang 2025 多速率PET仿真**（CHB-DAB拓扑）:
- 基于频率的子网划分：CHB慢速子系统（~500Hz）与DAB快速子系统（kHz级）
- 步长比例 **10:1~20:1**（CHB 50-100μs, DAB 1-10μs）
- 数据缺口：具体加速比数值在原文摘要中未量化报告

**数据缺口声明**：PET/SST建模的加速比高度依赖于具体拓扑（ISOP/ISOS/CHB-DAB）、子模块数量和仿真平台。不同模型间的横向对比缺乏统一基准（详细模型步长、硬件配置不同）。大多数验证在离线EMT环境完成，实时硬件平台（FPGA/RTDS）下的数据仅Li 2026在OPAL-RT上报告。

## 相关方法
- [[average-value-model|平均值模型]] - DAB/CLLC平均值建模
- [[state-space-method|状态空间法]] - SST状态空间建模
- [[fixed-admittance|恒导纳模型]] - 高频变换器恒导纳实现
- [[dynamic-phasor|动态相量法]] - SST动态相量简化

## 相关模型
- [[vsc-model|VSC模型]] - 整流/逆变级建模
- [[mmc-model|MMC模型]] - MMC型SST对比
- [[transformer-model|变压器模型]] - 高频变压器建模
- [[emi-filter-model|EMI滤波器]] - 高频噪声滤波

## 相关主题
- [[vsc-hvdc]] - 柔性直流输电
- [[real-time-simulation]] - SST实时仿真
- [[co-simulation]] - SST多域混合仿真
- [[frequency-dependent-modeling]] - 宽频变压器建模

---

## 来源论文

| 论文 | 年份 |
|------|------|
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Accelerated EMT Equivalent Model of Solid-State Transformer]] | 2022 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A numerically efficient and accurate model for real-time simulation of solid-state transformer]] | 2026 |
| [[universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc|Universal decoupled equivalent circuit models of solid-state transformer]] | 2025 |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Multirate EMT Simulation of Power Electronic Transformers]] | 2025 |

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
