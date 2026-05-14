---
title: "固态变压器 (Solid State Transformer, SST)"
type: model
tags: [solid-state-transformer, sst, power-electronic-transformer, pet, ac-dc-ac, isolation]
created: "2026-05-04"
updated: "2026-05-12"
---

# 固态变压器 (Solid State Transformer, SST)


## 定义与边界

固态变压器（SST）是基于电力电子变换器实现的智能变压器，通过AC-DC-AC或AC-AC变换实现电压变换和电气隔离。与传统工频变压器相比，SST具有体积小、重量轻、可控性强、功能集成度高等优点，可实现电压调节、谐波隔离、故障限流等高级功能。

**边界限定**：本页面聚焦于SST的拓扑结构和EMT建模，不包括磁性元件设计细节。

## EMT中的作用

SST是智能电网的关键设备：

- **电压调节**：动态无功补偿和电压支撑
- **故障隔离**：快速限制故障电流
- **谐波隔离**：阻止谐波传播
- **直流接口**：天然兼容交直流混合电网
- **能量路由**：智能能量管理和分配

## 主要分支与机制

### 1. 三级式SST

**结构**：
- 输入级：AC-DC整流（NPC或MMC）
- 隔离级：DC-DC高频变换（DAB或CLLC）
- 输出级：DC-AC逆变

**双有源桥（DAB）**：
$$P = \frac{nV_1V_2}{f_sL}\phi(1 - \frac{\phi}{\pi})$$

$\phi$为移相角。

### 2. 单级式SST

直接AC-AC变换：
- 矩阵变换器
- 无直流环节
- 效率更高，控制更复杂

### 3. 控制策略

**电压控制**：
- 输入级：功率因数校正
- 隔离级：直流母线电压控制
- 输出级：电压幅值/频率控制

**协调控制**：
- 三级间功率平衡
- 故障穿越

## 形式化表达

### DAB变换器

功率传输：
$$P = \frac{nV_1V_2}{2f_sL}\phi(1 - \frac{|\phi|}{\pi})$$

软开关条件：
$$I_{peak} > \frac{V_1 - nV_2}{2f_sL} \cdot D$$

### 电压变比

总变比：
$$\frac{V_{out}}{V_{in}} = m_1 \cdot n \cdot m_2$$

$m_1$、$m_2$为PWM调制比，$n$为高频变压器变比。


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

## 适用边界与失败模式

### 适用条件

- 功率等级在可接受范围
- 效率要求可接受
- 控制带宽足够
- 散热条件满足

### 失效边界

- **过流保护**：器件过流能力有限
- **效率限制**：高于传统变压器损耗
- **成本限制**：初期投资较高
- **可靠性**：大量电力电子器件

## 与相关页面的关系

- [[pet-sst-model]] - 电力电子变压器模型
- [[dc-dc-converter]] - DC-DC变换器
- [[mmc-model]] - MMC换流器（输入级）
- [[vsc-model]] - VSC换流器（输出级）
- [[transformer-model]] - 传统变压器模型
- [[ieee-14-bus-system]] - IEEE 14节点测试系统
- [[emt-simulation]] - EMT仿真基础
- [[transformer-model]] - 传统变压器模型

## 相关方法
- [[average-value-model|平均值模型]] - DAB/CLLC平均值建模
- [[fixed-admittance|恒导纳模型]] - 高频变换器恒导纳实现

## 来源论文

| 论文 | 年份 |
|------|------|
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio|EMTP model of a bidirectional multilevel solid state transfo]] | 2014 |
| [[emtp-model-of-a-bidirectional-multilevel-solid-state-transformer-for-distributio|EMTP model of a bidirectional multilevel solid state transfo]] | 2014 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[accelerated-electromagnetic-transient-emt-equivalent-model-of-solid-state-transf|Accelerated Electromagnetic Transient (EMT) Equivalent Model]] | 2022 |
| [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour|Fast Electromagnetic Transient Modeling Method for Half-brid]] | 2023 |
| [[a-component-level-modeling-and-fine-grained-simulation-method-for-renewable-ener|适用于级联型电力电子拓扑电磁暂态仿真的N端口网络通用等效建模方法]] | 2024 |
| [[a-numerically-efficient-and-accurate-model-for-real-time-simulation-of-solid-sta|A Numerically Efficient and Accurate Model for Real-Time Sim]] | 2026 |