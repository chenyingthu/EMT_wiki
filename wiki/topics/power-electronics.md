---
title: "电力电子 (Power Electronics)"
type: topic
tags: [power-electronics, converter, inverter, rectifier, switching]
created: "2026-05-02"
---

# 电力电子 (Power Electronics)

## 概述

电力电子是研究利用电力电子器件进行电能变换和控制的学科，是连接弱电控制与强电系统的桥梁。电力电子技术广泛应用于新能源并网、电机驱动、直流输电、电能质量控制等领域，是现代电力系统的核心技术之一。

## 基本器件

### 半控型器件
- **晶闸管(SCR)**: 可控导通，不可控关断
- [[thyristor-control]] - 晶闸管
- **门极可关断晶闸管(GTO)**: 可关断
- `gto` - GTO

### 全控型器件
- **绝缘栅双极晶体管(IGBT)**: 主流器件
- [[igbt-model]] - IGBT
- **电力MOSFET**: 高频应用
- `power-mosfet` - 电力MOSFET
- **集成门极换流晶闸管(IGCT)**: 大功率
- `igct` - IGCT

### 宽禁带器件
- **碳化硅(SiC)**: 高温、高频
- `sic-device` - SiC器件
- **氮化镓(GaN)**: 超高速
- `gan-device` - GaN器件

## 基本变换器

### AC-DC变换
- **整流器**: 交流变直流
- [[dynamic-average-modeling-of-front-end-diode-rectifier-loads-considering-13&14]] - 整流器
- **可控整流**: 晶闸管整流
- `controlled-rectifier` - 可控整流
- **PWM整流**: 四象限运行
- `pwm-rectifier` - PWM整流

### DC-AC变换
- **逆变器**: 直流变交流
- [[inverter-model]] - 逆变器
- **电压源型**: VSI
- `vsi` - 电压源逆变器
- **电流源型**: CSI
- `csi` - 电流源逆变器

### DC-DC变换
- **斩波器**: 直流变压
- [[dc-dc-converter]] - DC-DC变换器
- **Buck**: 降压
- `buck-converter` - Buck变换器
- **Boost**: 升压
- `boost-converter` - Boost变换器
- **双向**: 能量双向
- `bidirectional-converter` - 双向变换器

### AC-AC变换
- **交流调压**: 相位控制
- `ac-voltage-controller` - 交流调压
- **周波变流**: 降频
- `cycloconverter` - 周波变换器
- **矩阵变换**: 直接变换
- `matrix-converter` - 矩阵变换器

## 多电平变换器

### 二极管箝位型
- **NPC**: 中性点箝位
- `npc-converter` - NPC变换器
- **三电平**: 最常用

### 飞跨电容型
- **FC**: 电容箝位
- `flying-capacitor` - 飞跨电容

### 级联型
- **CHB**: 级联H桥
- `cascaded-h-bridge` - 级联H桥
- **MMC**: 模块化多电平
- [[mmc-model]] - MMC换流器

## 控制技术

### PWM技术
- **SPWM**: 正弦脉宽调制
- `spwm` - SPWM
- **SVPWM**: 空间矢量调制
- `svpwm` - SVPWM
- **特定谐波消除**: SHEPWM
- `shepwm` - SHEPWM

### 矢量控制
- **FOC**: 磁场定向控制
- `field-oriented-control` - 磁场定向控制
- **DTC**: 直接转矩控制
- `direct-torque-control` - 直接转矩控制

### 先进控制
- **模型预测控制**: MPC
- `model-predictive-control` - 模型预测控制
- **自适应控制**: 参数自适应
- `adaptive-control` - 自适应控制

## 应用领域

### 新能源
- **光伏**: 光伏逆变器
- [[pv-inverter-test-system]] - 光伏逆变器
- **风电**: 风电变流器
- `wind-converter` - 风电变流器
- **储能**: 储能变流器
- [[energy-storage-converter-model]] - 储能变流器

### 直流输电
- **HVDC**: 高压直流
- [[cigre-hvdc-benchmark]] - 高压直流
- **柔性直流**: VSC-HVDC
- [[vsc-hvdc]] - 柔性直流
- [[mtdc-model]] - 多端直流

### 电机驱动
- **变频调速**: 交流调速
- `variable-frequency-drive` - 变频驱动
- **伺服驱动**: 精密控制
- `servo-drive` - 伺服驱动

### 电能质量
- **有源滤波**: APF
- `active-power-filter` - 有源滤波
- **无功补偿**: STATCOM/SVC
- [[statcom]] - STATCOM
- [[svc-model]] - SVC模型

## EMT仿真建模

### 开关模型
- **理想开关**: 简化模型
- [[ideal-switch-model]] - 理想开关
- **详细开关**: 含导通电阻
- [[detailed-switch-model]] - 详细开关
- **平均值**: 连续模型
- [[average-value-model]] - 平均值模型

### 换流器模型
- [[current-source-modular-multilevel-converter-modeling-and-control]] - 换流器建模
- **详细模型**: 开关级
- **平均值模型**: 占空比
- **等效模型**: 线性化

### 损耗计算
- **导通损耗**: I²R
- **开关损耗**: 开关过程
- `loss-calculation` - 损耗计算

## 设计考虑

### 热设计
- **散热**: 散热器设计
- `thermal-design` - 热设计
- **结温**: 最高允许温度

### EMC设计
- **电磁兼容**: 干扰抑制
- `emc-design` - EMC设计
- **滤波器**: EMI滤波
- [[emi-filter-model]] - EMI滤波器

### 保护设计
- **过流保护**: 快速保护
- **过压保护**: 浪涌保护
- `converter-protection` - 换流器保护

## 发展趋势
- **高频化**: 提高开关频率
- **高效率**: 降低损耗
- **高功率密度**: 体积小型化
- **智能化**: AI控制

## 相关主题
- [[power-electronics]] - 电力电子换流器建模
- [[switching-function-method]] - 开关函数法
- [[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-]] - 调制技术
- `semiconductor-device` - 半导体器件

## 来源论文

参见 [[index]] 获取更多电力电子相关文献。
