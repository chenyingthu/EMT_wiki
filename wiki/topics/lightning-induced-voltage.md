---
title: "雷击感应电压 (Lightning Induced Voltage)"
type: topic
tags: [lightning, induced-voltage, electromagnetic-coupling, transmission-line, emt]
created: "2026-05-04"
---

# 雷击感应电压 (Lightning Induced Voltage)

## 定义与边界

雷击感应电压是雷云对地放电时，在附近架空线路或电气设备上由于电磁感应产生的过电压。与直击雷不同，感应雷不直接接触线路，但通过电磁耦合（电场耦合和磁场耦合）在导线上感应出幅值可观的过电压，是配电线路和中低压系统雷击故障的主要原因。

**边界限定**：本页面聚焦于雷击电磁感应的建模与计算方法，不包括直击雷或雷电物理过程。

## EMT中的作用

雷击感应电压是配电系统防雷设计的关键：

- **配电线路防雷**：评估10-35kV线路的感应雷击跳闸风险
- **绝缘配合**：确定线路绝缘水平与感应过电压的关系
- **防雷措施评估**：分析避雷器、屏蔽线对感应过电压的抑制效果
- **设备保护**：评估变电站和终端设备的感应过电压暴露

## 主要分支与机制

### 1. 电场耦合（容性耦合）

雷云电荷在线路上感应的电压：

**静电感应模型**：
$$V_e = \frac{C_{12}}{C_{12} + C_{20}} \cdot V_{cloud}$$

其中$C_{12}$为雷云与线路间电容，$C_{20}$为线路对地电容，$V_{cloud}$为雷云电位。

### 2. 磁场耦合（感性耦合）

雷电流产生的磁场在线路感应的电压：

**Agrawal模型**（传输线近似）：
$$\frac{\partial V}{\partial x} + L \frac{\partial I}{\partial t} = E_x^e$$
$$\frac{\partial I}{\partial x} + C \frac{\partial V}{\partial t} = 0$$

$E_x^e$为沿导线方向的激励电场。

**Rusck简化模型**：
对于距离雷击点$y$、高度$h$的导线：
$$V_{max} = \frac{Z_c \cdot I \cdot h}{y} \cdot k(y, t)$$

$k(y,t)$为时间相关函数，峰值约在$t = y/v$时达到。

### 3. 完整电磁耦合模型

基于麦克斯韦方程组的场线耦合：

**Taylor模型**：
$$\frac{\partial V}{\partial x} + L \frac{\partial I}{\partial t} = - \frac{\partial \phi}{\partial t}$$

**Rachidi模型**：
考虑大地有限电导率的影响，修正镜像位置。

## 形式化表达

### 感应电压峰值估算

**Rusck公式**（垂直雷击通道，距离$y$）：
$$V_{max} = 30 \cdot I \cdot \frac{h}{y} \quad (\text{kV})$$

其中$I$为雷电流峰值（kA），$h$为导线高度（m），$y$为水平距离（m）。

**Cooray修正**（考虑回击速度$v$）：
$$V_{max} = \frac{Z_c \cdot I \cdot h}{y} \cdot \frac{v}{c} \cdot \frac{1}{\sqrt{1 - (v/c)^2 \sin^2\theta}}$$

### 感应电压波形

典型感应电压波形特征：
- 波头时间：1-5 μs（快于直击雷）
- 波尾时间：50-100 μs
- 极性：通常与雷电流相反

### 多导线系统

三相线路的感应电压：
$$\mathbf{V}_{ind} = \mathbf{Z}_{mutual} \cdot \mathbf{I}_{lightning}$$

互阻抗矩阵考虑导线间的电磁耦合。

## 适用边界与失败模式

### 适用条件

- 雷击点距离线路一定距离（通常50-2000m）
- 线路高度和几何结构明确
- 雷电流波形参数（幅值、波头）统计分布已知
- 土壤电阻率用于地回路修正

### 失效边界

- **近场效应**：雷击点过近（<50m）时，场线耦合模型需修正
- **倾斜雷击通道**：非垂直雷击改变电磁场分布
- **复杂地形**：山地、山谷改变电场分布
- **多回击**：多次回击的叠加效应
- **屏蔽效应**：建筑物、树木对线路的屏蔽

### 关键假设

1. 雷击通道为垂直直线
2. 线路为均匀传输线
3. 大地为平面（复杂地形需修正）
4. 雷电流波形为双指数或Heidler模型
5. 回击速度恒定（通常为$c/3$至$c/2$）

## 代表性来源

### 经典文献

- Rusck, S., "Induced Lightning Over-voltages on Power-transmission Lines," *Proc. IEE*, 1958.
- Agrawal, A.K., et al., "Transient Response of Multiconductor Transmission Lines Excited by a Nonuniform Electromagnetic Field," *IEEE EMC*, 1980.
- Rachidi, F., et al., "Influence of a Lossy Ground on Lightning-induced Voltages," *IEEE PWRD*, 1996.
- Cooray, V., "Calculating Lightning-induced Overvoltages in Power Lines," *IEEE PWRD*, 1993.

### 应用方法

- 雷击暂态分析方法
- 线路场线耦合建模
- 电磁耦合理论

## 与相关页面的关系

- [[lightning-transient-analysis]] - 雷击暂态整体分析
- [[transmission-line-model]] - 输电线路建模
- [[distributed-parameter-line]] - 分布参数线路
- [[grounding-system-model]] - 接地系统模型
- [[insulator-string-model]] - 绝缘子串模型
- [[electromagnetic-transient]] - 电磁暂态
- [[power-system-network]] - 电力系统网络
- [[emt-simulation]]
- [[real-time-simulation]]
- [[co-simulation]]
## 开放问题

- 高比例分布式电源接入对感应过电压的影响
- 配电网智能化设备（传感器、通信）的感应过电压防护
- 城市配电网复杂环境下的感应过电压计算
- 气候变化对雷电活动及感应过电压的影响
- 新型绝缘导线（覆盖层）的感应过电压特性

## 参考标准

- IEEE Std. 1243 - 输电线路雷电性能估算
- IEC 62305-2 - 雷电防护风险评估
- GB/T 50064 - 交流电气装置的过电压保护和绝缘配合

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
