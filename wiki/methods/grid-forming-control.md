---
title: "构网型控制 (Grid-Forming Control)"
type: method
tags: [grid-forming, gfm, virtual-synchronous-machine, vsm, inverter-control, power-electronics]
created: "2026-05-04"
---

# 构网型控制 (Grid-Forming Control)

## 定义与边界

构网型控制（Grid-Forming, GFM）是电力电子变换器模拟同步发电机外特性、自主建立和维持电网电压幅值与频率的控制策略。与跟网型控制（GFL）依赖电网电压定向不同，构网型逆变器能够主动塑造电网，适用于高比例新能源、弱电网或孤岛运行场景。

**边界限定**：本页面聚焦于构网型控制的原理与实现，不包括具体的硬件设计或详细调制策略。

## EMT中的作用

构网型控制是新型电力系统的关键技术：

- **高比例新能源**：替代同步机提供惯量和阻尼
- **弱电网运行**：在短路比(SCR)低的电网稳定运行
- **孤岛微网**：自主建立电压频率，无需外部参考
- **黑启动**：电网故障后自主恢复供电
- **系统强度**：提升电网抗扰动能力

## 主要分支与机制

### 1. 下垂控制 (Droop Control)

模拟同步机功频特性：
$$f = f_0 - k_p(P - P_0)$$
$$V = V_0 - k_q(Q - Q_0)$$

其中$k_p$、$k_q$为下垂系数，$f_0$、$V_0$为额定值。

### 2. 虚拟同步机 (VSM)

模拟同步机摇摆方程：
$$J\frac{d\omega}{dt} = P_{ref} - P - D(\omega - \omega_0)$$
$$\frac{d\delta}{dt} = \omega - \omega_0$$

其中$J$为虚拟惯量，$D$为阻尼系数。

输出功率：
$$P = \frac{EV}{X} \sin\delta$$
$$Q = \frac{EV\cos\delta - V^2}{X}$$

### 3. 虚拟振荡器控制 (VOC)

基于非线性振荡器理论：
$$\ddot{v} + \epsilon(1-v^2)\dot{v} + \omega_0^2 v = i_{inj}$$

自激振荡产生正弦电压。

## 形式化表达

### GFM与GFL对比

| 特性 | GFM | GFL |
|------|-----|-----|
| 电压建立 | 自主 | 依赖电网 |
| 惯量支撑 | 有 | 无 |
| SCR要求 | 可<1 | 通常>2 |
| 适用场景 | 孤岛/弱电网 | 强电网 |
| 控制复杂度 | 较高 | 较低 |

### 功频下垂小信号模型

线性化后：
$$\Delta f = -k_p \Delta P$$

多台并联：
$$\Delta f = -\frac{\sum k_{p,i} \Delta P_i}{\sum k_{p,i}}$$

实现无通信功率均分。

### 暂态稳定性

等面积法则：
$$\int_{\delta_0}^{\delta_{max}} (P_m - P_e) d\delta = 0$$

GFM需设计加速面积小于减速面积。

## 适用边界与失败模式

### 适用条件

- 需要电压频率支撑的场合
- 短路比低于2的弱电网
- 孤岛或微电网运行
- 高比例电力电子设备系统

### 失效边界

- **功率过载**：超过逆变器容量限制
- **直流电压崩溃**：功率不平衡导致直流母线失稳
- **环流问题**：多台GFM并联的环流
- **谐振风险**：与电网阻抗的谐振
- **保护协调**：故障期间控制与保护的协调

### 关键假设

1. 直流母线电压稳定（或有储能支撑）
2. 开关器件容量足够
3. 滤波器设计合理
4. 参数整定适当（惯量、阻尼）

## 代表性来源

### 经典文献

- Zhong, Q.C. and Weiss, G., "Synchronverters: Inverters that Mimic Synchronous Generators," *IEEE TIE*, 2011. - 虚拟同步机奠基
- Beck, H.P. and Hesse, R., "Virtual Synchronous Machine," *IET*, 2007. - VSM概念
- Schiffer, J., et al., "Synchronization of Droop-Controlled Microgrids," *IEEE TSP*, 2014. - 下垂控制同步

### GFM应用

- 构网型逆变器模型
- 下垂控制实现
- 微电网应用技术

## 与相关页面的关系

- [[gfm-inverter-model]] - 构网型逆变器详细模型
- [[gfl-inverter-model]] - 跟网型逆变器对比
- [[droop-control-model]] - 下垂控制模型
- [[microgrid-distribution-network]] - 微电网应用
- [[pll-model]] - 锁相环模型

## 开放问题

- 100%电力电子系统的稳定性理论
- GFM与GFL的最优混合比例
- 构网型设备的故障穿越策略
- 大规模GFM系统的协调控制
- 构网型储能的经济运行优化

## 参考标准

- IEEE Std. 1547-2018 - 分布式资源并网标准（含GFM要求）
- NREL GFM技术报告
- 中国《构网型变流器技术规范》

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
