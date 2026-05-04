---
title: "雷击暂态分析 (Lightning Transient Analysis)"
type: topic
tags: [lightning, transient, overvoltage, backflashover, shielding-failure, emt]
created: "2026-05-04"
---

# 雷击暂态分析 (Lightning Transient Analysis)

## 定义与边界

雷击暂态分析是研究雷电放电对电力系统产生的电磁暂态过程的方法，包括直击雷（雷电直接击中线路或设备）和感应雷（雷云放电在附近线路感应过电压）两种主要形式。EMT仿真用于计算雷击引起的过电压波形、传播和绝缘闪络风险。

**边界限定**：本页面聚焦于雷击电磁暂态的建模与仿真方法，不包括雷电物理机理或防雷装置设计细节。

## EMT中的作用

雷击暂态分析是输电线路绝缘配合的核心：

- **过电压计算**：确定雷击引起的线路和变电站过电压水平
- **绝缘闪络评估**：判断雷击过电压是否导致绝缘子闪络
- **防雷设计优化**：避雷线屏蔽效果、接地电阻影响分析
- **保护配合**：避雷器配置与绝缘水平的协调

## 主要分支与机制

### 1. 直击雷过电压

雷电直接击中导线或杆塔：

**雷电流模型**（Heidler模型）：
$$i(t) = \frac{I_m}{\eta} \cdot \frac{(t/\tau_1)^{10}}{1 + (t/\tau_1)^{10}} \cdot e^{-t/\tau_2}$$

其中$I_m$为峰值电流，$\tau_1$为波前时间常数，$\tau_2$为波尾时间常数。

**击中杆塔时的过电压**：
$$U_t = R_g \cdot i(t) + L_t \cdot \frac{di}{dt}$$

$R_g$为接地电阻，$L_t$为杆塔等效电感。

### 2. 感应雷过电压

雷云放电在线路感应过电压：

**Rusck模型**：
$$U_i = \frac{Z_0 \cdot I \cdot h}{y} \cdot \frac{1}{\sqrt{1 + (v \cdot t / 2y)^2}}$$

其中$Z_0$为线路波阻抗，$h$为导线高度，$y$为雷击点水平距离，$v$为光速。

### 3. 反击与绕击

- **反击（Backflashover）**：雷击杆塔或避雷线，绝缘子承受过高电压而闪络
- **绕击（Shielding Failure）**：雷电绕过避雷线直接击中导线

## 形式化表达

### 雷击跳闸率计算

$$N = N_g \cdot L \cdot (\eta_{bf} \cdot P_{bf} + \eta_{sf} \cdot P_{sf})$$

其中：
- $N_g$：地闪密度（次/km²/年）
- $L$：线路长度
- $\eta_{bf}$：反击闪络率
- $P_{bf}$：反击建弧率
- $\eta_{sf}$：绕击闪络率
- $P_{sf}$：绕击建弧率

### 电气几何模型

绕击暴露距离：
$$r_c = 8 \cdot I^{0.65} \quad (\text{m, 对于平原地区})$$

$$r_g = 8 \cdot I^{0.65} \cdot k_g$$

其中$r_c$为导线暴露距离，$r_g$为避雷线保护距离，$k_g$为地形系数。

### 波阻抗与传播

线路波阻抗：
$$Z_c = \frac{1}{2\pi} \sqrt{\frac{\mu_0}{\varepsilon_0}} \ln\frac{2h}{r} \approx 60 \ln\frac{2h}{r}$$

雷击过电压波沿线传播，遇到阻抗不连续点产生折射和反射。

## 适用边界与失败模式

### 适用条件

- 雷电流参数（幅值、波头、极性）基于统计分布
- 土壤电阻率已知，用于接地计算
- 线路参数（波阻抗、衰减）准确
- 绝缘子伏秒特性可用

### 失效边界

- **土壤电离**：高幅值雷电流下接地极附近土壤电离，有效接地电阻降低
- **电晕效应**：高电压下导线电晕增加有效半径，改变波阻抗
- **多回线耦合**：同塔多回线路的相互影响
- **复杂地形**：山区地形改变暴露距离计算
- **绝缘子老化**：老化绝缘子闪络电压降低

### 关键假设

1. 雷电流波形采用双指数或Heidler模型近似
2. 线路为均匀传输线
3. 大地为理想导体或采用Carson公式修正
4. 绝缘子闪络基于伏秒特性

## 代表性来源

### 经典文献

- IEEE Std. 1243 - 输电线路雷电性能估算
- CIGRE TB 63 - 输电线路雷电防护
- Eriksson, A.J., "The Incidence of Lightning Strikes to Power Lines," *IEEE PAS*, 1987.
- Rusck, S., "Induced Lightning Over-voltages on Power-transmission Lines," *Proc. IEE*, 1958.

### 应用方法

- [[transmission-line-model]] - 线路暂态模型
- [[insulator-string-model]] - 绝缘子闪络模型
- [[grounding-system-model]] - 接地系统建模

## 与相关页面的关系

- [[transmission-line-model]] - 输电线路波过程建模
- [[insulator-string-model]] - 绝缘子闪络特性
- [[grounding-system-model]] - 杆塔接地与雷电流泄放
- [[surge-arrester-model]] - 避雷器保护配合
- [[emt-simulation]] - 电磁暂态仿真基础

## 开放问题

- 高比例新能源接入对雷击暂态的影响
- 特高压线路雷击特性与防护
- 城市配电网雷击风险评估
- 雷电定位系统与线路跳闸关联分析
- 气候变化对雷电活动的影响

## 参考标准

- IEEE Std. 1243-1997 - 输电线路雷电性能估算
- IEC 62305 - 雷电防护
- GB/T 50064 - 交流电气装置的过电压保护和绝缘配合

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
