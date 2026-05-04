---
title: "交直流混合系统 (Hybrid AC/DC System)"
type: topic
tags: [hybrid-acdc, vsc-hvdc, lcc-hvdc, power-system, mtdc]
created: "2026-05-04"
---

# 交直流混合系统 (Hybrid AC/DC System)

## 定义与边界

交直流混合系统是指由交流电网与高压直流输电系统互联构成的电力系统，通过换流站实现交流电与直流电的相互转换。在EMT仿真中，这类系统需要准确建模交流侧和直流侧的相互作用，以及换流器的动态响应。

**边界限定**：本页面聚焦于高压直流输电与交流电网互联的系统级建模，不包括纯交流或纯直流系统。

## EMT中的作用

- **研究交流故障对直流系统的影响**：如换相失败、直流功率波动
- **分析直流功率调制对交流系统的稳定性贡献**：直流功率紧急支援
- **仿真换相失败等复杂暂态过程**：LCC-HVDC特有的暂态现象
- **多馈入系统分析**：多个直流馈入同一交流电网的相互作用
- **交直流并列运行**：交流线路与直流线路并联时的功率分配

## 主要类型

### 1. LCC-HVDC + 交流电网

- 电流源型换流器
- 依赖交流电压换相
- 易发生换相失败

### 2. VSC-HVDC + 交流电网

- 电压源型换流器
- 可独立控制有功和无功
- 具备黑启动能力

### 3. 混合多馈入系统

- 多个直流系统接入同一交流电网
- 交互作用复杂
- 需协调控制

## 形式化表达

### 直流功率传输

$$P_{dc} = V_{dc} \cdot I_{dc}$$

### 交流侧功率

$$P_{ac} = \frac{3\sqrt{2}}{\pi} V_{LL} I_{dc} \cos\alpha$$

$\alpha$为触发角。

## 适用边界与失败模式

### 适用条件

- 交流系统强度足够（SCR>2）
- 换流器参数已知
- 控制策略明确
- 故障工况可定义

### 失效边界

- **交流故障引发换相失败**：LCC-HVDC的固有限制
- **多馈入交互**：多个直流系统相互影响
- **电压稳定性**：交流电压崩溃导致直流闭锁
- **谐波不稳定**：交流滤波器与系统谐振

## 与相关页面的关系

- [[vsc-hvdc]] - VSC-HVDC系统
- [[lcc-model]] - LCC换流器模型
- [[electromechanical-electromagnetic-hybrid-simulation]] - 机电电磁混合仿真
- [[co-simulation]] - 协同仿真技术
- [[hybrid-acdc-network]] - 交直流混合电网
- [[electromagnetic-transient]] - 电磁暂态
- [[power-system-network]] - 电力系统网络
- [[emt-simulation]]
- [[real-time-simulation]]
- [[facts]]
## 代表性来源

- Arrillaga, J. and Liu, Y.H., "Flexible Power Transmission: The HVDC Options," *Wiley*, 2007.
- Bahrman, M.P. and Johnson, B.K., "The ABCs of HVDC Transmission Technologies," *IEEE Power and Energy Magazine*, 2007.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
