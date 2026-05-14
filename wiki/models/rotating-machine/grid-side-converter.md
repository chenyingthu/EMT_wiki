---
title: "网侧变流器 (Grid-side Converter)"
type: model
tags: [grid-side-converter, gsc, wind-turbine, dfig, inverter, grid-connection]
updated: "2026-05-12"
created: "2026-05-02"
---

# 网侧变流器 (Grid-side Converter)



## 定义与边界

网侧变流器（Grid-Side Converter, GSC）是连接直流环节与交流电网的电压源换流器，负责控制与电网交换的有功和无功功率，维持直流母线电压稳定。GSC广泛应用于双馈感应发电机（DFIG）风电系统、全功率变换风电机组、储能系统和光伏逆变器等场景。

**边界限定**：本页面聚焦于GSC的EMT建模与控制策略，不包括发电机侧变流器或直流-直流变换器。

## EMT中的作用

GSC是新能源并网系统的关键接口：

- **功率双向流动**：实现发电机与电网之间的有功、无功功率交换
- **直流电压稳定**：维持直流母线电压恒定，平衡两侧功率
- **电网支撑**：提供无功功率支撑，参与电压调节
- **电能质量控制**：抑制谐波电流，满足并网标准
- **故障穿越**：在电网故障时维持并网运行，提供无功支撑

## 基本结构

### 拓扑形式
- **两电平**: 基础三相全桥
- **三电平**: NPC/T型结构
- **多电平**: MMC、CHB等
- [[vsc-model]] - 电压源换流器

### 主电路元件
| 元件 | 功能 | 典型参数 |
|------|------|----------|
| IGBT | 功率开关 | 1.7kV/600A |
| 反并联二极管 | 续流 | 同规格 |
| 直流电容 | 稳压 | 数千μF |
| 滤波电感 | 电流滤波 | 0.1-0.3 pu |

### 连接方式
- **L滤波**: 简单电感
- **LCL滤波**: 降低电感量
- **变压器**: 电压匹配+隔离

## 数学模型

### 三相坐标系
电压方程：
$$v_{abc} = Ri_{abc} + L\frac{di_{abc}}{dt} + e_{abc}$$

其中：
- $v_{abc}$: 电网三相电压
- $i_{abc}$: 变流器三相电流
- $e_{abc}$: 变流器输出电压
- $R, L$: 滤波器电阻、电感

### 旋转坐标系(dq)
通过Park变换到同步旋转坐标系：
$$v_d = Ri_d + L\frac{di_d}{dt} - \omega Li_q + e_d$$
$$v_q = Ri_q + L\frac{di_q}{dt} + \omega Li_d + e_q$$

特点：
- 交流量变为直流量
- d轴、q轴解耦控制
- [[dq-transformation]] - dq变换

### 功率关系
有功、无功功率：
$$P = \frac{3}{2}(v_d i_d + v_q i_q)$$
$$Q = \frac{3}{2}(v_q i_d - v_d i_q)$$

电网电压定向控制时($v_q=0$):
$$P = \frac{3}{2}v_d i_d$$
$$Q = -\frac{3}{2}v_d i_q$$

## 控制策略

### 电压定向控制(VOC)
- **锁相环**: 同步电网相位
- [[pll-model]] - 锁相环
- **外环**: 直流电压/无功功率
- **内环**: d、q轴电流

### 直接功率控制(DPC)
- **开关表**: 基于功率滞环
- **查表法**: 无需电流内环
- **动态响应**: 更快

### 模型预测控制(MPC)
- **模型预测控制**: 基于系统模型的优化控制
- **目标函数**: 多目标优化
- **约束处理**: 显式处理约束

## 控制环路设计

### 电流内环
- **带宽**: 通常为开关频率的1/10
- **PI参数**: 基于模型设计
- **解耦项**: 消除d-q耦合
- **前馈**: 电网电压前馈

### 直流电压外环
- **控制目标**: 维持直流电压恒定
- **响应速度**: 慢于电流环
- **功率平衡**: $P_{in} = P_{out} + P_{loss}$

### 无功功率环
- **控制模式**: 恒无功/恒功率因数
- **电压支撑**: 电网电压跌落时
- **电网规范**: 满足并网要求

## DFIG中的应用

### 系统配置
- [[dfig-model]] - 双馈感应发电机
- **转子侧变流器**: RSC控制转矩
- **网侧变流器**: GSC控制直流电压
- **直流环节**: 连接两侧变流器

### GSC功能
- **功率双向**: 亚同步/超同步运行
- **直流稳压**: 维持直流母线
- **无功交换**: 与电网无功交换
- **谐波抑制**: 滤波器设计

### 协调控制
- **RSC-GSC协调**: 功率分配
- **暂态控制**: 故障穿越
- [[fault-ride-through]] - 低电压穿越

## 形式化表达

### 功率平衡方程

直流侧功率平衡：
$$C_{dc}\frac{dV_{dc}}{dt} = \frac{P_{in} - P_{out}}{V_{dc}}$$

其中$P_{in}$为输入功率（来自发电机或直流源），$P_{out}$为输出功率（送往电网）。

### 电流限制

变流器电流限幅：
$$I_{max} = \sqrt{i_d^2 + i_q^2} \leq I_{rated}$$

典型过载能力：1.1-1.5倍额定电流，持续10-60秒。

## 适用边界与失败模式

### 适用条件

- 电网电压在允许范围内（通常0.9-1.1 pu）
- 直流母线电压稳定
- 开关器件温度正常
- 滤波器参数与设计匹配

### 失效边界

- **过流故障**：超过器件安全工作区
- **直流电压崩溃**：功率不平衡导致
- **PLL失锁**：电网电压跌落或畸变严重时
- **谐振**：滤波器与电网阻抗谐振

### 故障穿越策略

**低电压穿越(LVRT)**：
- 电压跌落时维持并网
- 提供无功电流支撑（典型：1 pu无功/0.1 pu电压跌落）
- 必要时激活Crowbar保护

**高电压穿越(HVRT)**：
- 电压升高时吸收无功
- 限制有功输出防止过压

## 调制技术

### PWM调制
- **SPWM**: 正弦脉宽调制
- **SVPWM**: 空间矢量调制
- **DPWM**: 不连续调制

### 多电平调制
- **载波移相**: CPS-PWM
- **最近电平**: NLM
- [[nearest-level-control]] - 最近电平控制

## 滤波器设计

### L滤波器
- **电感值**: 电流纹波限制
- **损耗**: 铜损、铁损

### LCL滤波器
- **谐振**: 固有谐振频率
- **阻尼**: 无源/有源阻尼

### 滤波目标
- **电流THD**: <5% (IEEE 519)
- **开关频率**: 2-10 kHz
- **谐振抑制**: 避免谐振

## 与机侧变流器对比

| 特性 | 机侧变流器(MSC) | 网侧变流器(GSC) |
|------|-----------------|-----------------|
| 连接 | 发电机 | 电网 |
| 控制目标 | 转矩/转速 | 直流电压/无功 |
| 频率 | 可变 | 固定(电网频率) |
| 功率流向 | 单向(发电) | 双向 |
| 谐波标准 | 内部要求 | 并网规范严格 |

## 与相关页面的关系

- [[dfig-model]] - 双馈感应发电机
- [[inverter-model]] - 逆变器模型
- [[pll-model]] - 锁相环模型
- [[dq-transformation]] - dq坐标变换
- [[pwm-modulator-model]] - PWM调制器模型

## 商业产品

- **Siemens**: SWT系列变流器
- **ABB**: PCS系列
- **Woodward**: 风机控制器

## 量化性能边界

**GSC控制性能**（基于VOC/DPC/MPC控制策略）：
- VOC电流内环带宽通常为开关频率的 1/5-1/10，闭环响应时间 1-5 ms
- 直流电压外环带宽通常为电流环的 1/5-1/10，响应时间 10-50 ms
- DPC动态响应比VOC快，但稳态纹波较大；MPC多目标优化可显式处理约束
- PLL带宽典型值 5-30 Hz，弱电网下需降至 < 15 Hz 以维持稳定
- 变流器过载能力：1.1-1.5 倍额定电流，持续 10-60 s

**滤波器性能与谐波抑制**（IEEE 519）：
- LCL滤波器谐振频率通常设计在开关频率的 1/3-1/2（Lins 2012）
- 有源阻尼可将LCL谐振峰抑制 10-20 dB，无源阻尼效率损失约 0.5-1%
- 电流THD要求：< 5%（IEEE 519），典型设计目标 < 3%
- 滤波器电感压降通常 < 0.1 pu

**DFIG-GSC功率效率**（2012 Type-4等效模型）：
- GSC容量约为DFIG额定功率的 30%（转差功率），全功率变换器中容量为 100%
- GSC效率通常为 97-99%，主要损耗来自IGBT开关损耗和滤波器铜损
- 直流母线电压波动在暂态过程中通常 < 5%（2025 风电场初始化）
- 全功率变换风电场初始化算法确保EMT仿真启动过程平稳过渡（2025）

**阻抗建模与稳定性**（2023 dq阻抗扫描、2023 序域频扫）：
- 高斯脉冲激励的dq导纳建模方法可高效提取GSC宽频阻抗特性（2023）
- 序域MIMO频扫方法可准确识别GSC在50 Hz-5 kHz范围内的阻抗耦合特性（2023）
- 弱电网下GSC与电网阻抗交互易引发次/超同步振荡，SCR < 2 时需附加阻尼控制

**数据缺口声明**：不同GSC拓扑（两电平/三电平/多电平）在相同工况下的效率-谐波对比缺乏系统性EMT仿真研究。LCL滤波器参数在不同功率等级（kW至MW级）下的优化设计准则缺乏统一标准。GSC在弱电网（SCR < 1.5）下的暂态稳定边界和PLL失锁阈值缺乏系统量化。

## 相关方法
- [[average-value-model|平均值模型]] - GSC系统级简化
- [[state-space-method|状态空间法]] - GSC控制分析
- [[dq-transformation|dq变换]] - 坐标变换
- [[vector-control|矢量控制]] - dq解耦控制
- [[pwm-modulation|PWM调制]] - 开关信号生成

## 相关模型
- [[dfig-model|DFIG模型]] - 双馈感应发电机
- [[inverter-model|逆变器模型]] - 通用逆变器
- [[pll-model|锁相环]] - 并网同步
- [[vsc-model|VSC模型]] - 电压源换流器
- [[pi-controller-model|PI控制器]] - 电流环/电压环
- [[lcl-filter-model|LCL滤波器]] - 并网滤波器

## 相关主题
- [[vsc-hvdc|VSC-HVDC]] - 电压源换流器直流输电
- 电能质量 - 谐波与闪变
- 弱电网 - 短路比限制
- 故障穿越 - LVRT/HVRT

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[a-new-sequence-domain-emt-level-multi-input-multi-output-frequency-scanning-meth|A new sequence domain EMT-level multi-input multi-output fre]] | 2023 |
| [[dq-admittance-model-extraction-for-ibrs-via-gaussian-pulse-excitation|DQ Admittance Model Extraction for IBRs via Gaussian Pulse E]] | 2023 |
| [[an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o|An enhanced K-means two-step clustering method for dynamic e]] | 2025 |
| [[comprehensive-full-scale-converter-wind-park-initialization-for-electromagnetic-|Comprehensive Full-Scale Converter Wind Park Initialization ]] | 2025 |