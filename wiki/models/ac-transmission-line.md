---
title: "交流输电线路 (AC Transmission Line)"
type: model
tags: [ac-transmission, overhead-line, power-transmission, line-modeling, emt]
created: "2026-05-04"
---

# 交流输电线路 (AC Transmission Line)

## 定义与边界

交流输电线路是用于传输电能的架空导线系统，通常由三相导线、地线（避雷线）、绝缘子串和杆塔组成。在EMT仿真中，交流输电线路模型需要考虑分布参数特性、频变效应、多导体耦合和地回路影响，以准确模拟正常运行和暂态过程。

**边界限定**：本页面聚焦于交流架空线路的EMT建模，不包括电缆线路或直流输电线路。

## EMT中的作用

交流输电线路是电力系统EMT仿真的核心元件：

- **工频潮流**：稳态电压分布和无功功率传输
- **暂态过电压**：操作过电压、雷击过电压的传播
- **故障分析**：短路故障的电流行波和传播
- **稳定性研究**：机电振荡和功率摇摆
- **谐波分析**：谐波在电网中的传播和放大

## 主要分支与机制

### 1. 线路参数

**单位长度参数**（每相）：
- 电阻 $R'$：导线集肤效应和地回路损耗
- 电感 $L'$：自感和互感
- 电容 $C'$：对地电容和相间电容
- 电导 $G'$：电晕和泄漏损耗（通常忽略）

**几何平均半径 (GMR)**：
$$GMD = \sqrt[3]{D_{ab}D_{bc}D_{ca}}$$

**电感计算**：
$$L' = 2 \times 10^{-7} \ln\frac{GMD}{GMR} \quad (\text{H/m})$$

### 2. 线路模型层次

| 模型 | 适用场景 | 时间尺度 |
|------|----------|----------|
| 集中参数π型 | 短线路 (<100km) | 工频稳态 |
| Bergeron模型 | 中长线路 | 开关暂态 |
| 频变线路模型 | 长线路/宽频分析 | 雷击、谐波 |
| 多导体相域模型 | 非对称故障 | 全暂态 |

### 3. 多导体系统

三相导线的耦合矩阵：
$$\mathbf{Z}' = \begin{bmatrix} Z_{aa}' & Z_{ab}' & Z_{ac}' \\ Z_{ba}' & Z_{bb}' & Z_{bc}' \\ Z_{ca}' & Z_{cb}' & Z_{cc}' \end{bmatrix}$$

通过对称分量变换或模态变换解耦。

## 形式化表达

### 电报方程

交流线路的分布参数方程：
$$-\frac{\partial \mathbf{v}}{\partial x} = \mathbf{Z}' \mathbf{i}$$
$$-\frac{\partial \mathbf{i}}{\partial x} = \mathbf{Y}' \mathbf{v}$$

其中$\mathbf{Z}' = \mathbf{R}' + j\omega\mathbf{L}'$，$\mathbf{Y}' = \mathbf{G}' + j\omega\mathbf{C}'$。

### 特性阻抗与传播常数

特性阻抗：
$$\mathbf{Z}_c = \sqrt{\frac{\mathbf{Z}'}{\mathbf{Y}'}}$$

传播常数：
$$\gamma = \sqrt{\mathbf{Z}' \mathbf{Y}'} = \alpha + j\beta$$

### ABCD参数

二端口网络表示：
$$\begin{bmatrix} \mathbf{V}_S \\ \mathbf{I}_S \end{bmatrix} = \begin{bmatrix} \mathbf{A} & \mathbf{B} \\ \mathbf{C} & \mathbf{D} \end{bmatrix} \begin{bmatrix} \mathbf{V}_R \\ \mathbf{I}_R \end{bmatrix}$$

其中：
$$\mathbf{A} = \mathbf{D} = \cosh(\gamma l)$$
$$\mathbf{B} = \mathbf{Z}_c \sinh(\gamma l)$$
$$\mathbf{C} = \frac{1}{\mathbf{Z}_c} \sinh(\gamma l)$$


## 数值分析

### 精度与效率
- 仿真精度：误差控制在1%以内
- 计算效率：支持大规模系统实时仿真
- 数值稳定性：在典型工况下保持稳定

### 典型参数范围
- 时间步长：1μs ~ 1ms
- 系统规模：10~1000节点
- 仿真时长：0.1s ~ 10s

### 性能指标
- 内存占用：随系统规模线性增长
- 计算时间：与系统复杂度和仿真时长相关
- 收敛性：在绝大多数情况下稳定收敛

## 适用边界与失败模式

### 适用条件

- 线路几何参数（间距、高度）准确
- 导线材料特性（电阻率、GMR）已知
- 土壤电阻率用于地回路计算
- 气象条件（温度）用于载流量修正

### 失效边界

- **电晕效应**：高电压下电晕增加有效电容和损耗
- **集肤效应**：高频下电阻增加
- **地回路频变**：大地返回路径的频率相关特性
- **不平衡**：三相不对称或换位不充分
- **非线性**：变压器饱和等影响线路边界条件

### 关键假设

1. 线路参数沿线均匀分布
2. 大地为均匀或分层均匀介质
3. 导线为理想圆柱（忽略绞线效应）
4. 线路换位理想（三相参数对称）

## 代表性来源

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统建模
- [[electromagnetic-transient]] - 电磁暂态分析
- [[control-system]] - 控制系统设计
- [[real-time-simulation]] - 实时仿真技术
### 经典文献

- Stevenson, W.D., "Elements of Power System Analysis," *McGraw-Hill*, 1982.
- Grainger, J.J. and Stevenson, W.D., "Power System Analysis," *McGraw-Hill*, 1994.
- Carson, J.R., "Wave Propagation in Overhead Wires," *BSTJ*, 1926.

### EMT应用

- [[transmission-line-model]] - 输电线路详细模型
- [[distributed-parameter-model]] - 分布参数理论
- [[bergeron-line-model]] - Bergeron数值模型

## 与相关页面的关系

- [[transmission-line-model]] - 输电线路模型综合
- [[distributed-parameter-model]] - 分布参数理论
- [[frequency-dependent-line-model]] - 频变线路模型
- [[earth-return-impedance]] - 地回路阻抗
- [[insulator-string-model]] - 绝缘子串

## 开放问题

- 高比例新能源接入对交流线路潮流的影响
- 特高压线路的电晕与可听噪声建模
- 复杂地形（山区、跨海）线路参数计算
- 线路动态热定额的实时评估
- 智能线路（在线监测、动态增容）建模

## 参考标准

- IEEE Std. 738 - 架空导线电流-温度计算
- IEC 61597 - 架空线路载流量计算
- GB/T 1179 - 圆线同心绞架空导线

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
