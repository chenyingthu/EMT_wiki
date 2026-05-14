---
title: "绝缘子串 (Insulator String)"
type: model
tags: [insulator, string, flashover, contamination, overvoltage, transmission-line]
created: "2026-05-04"
updated: "2026-05-11"
---

# 绝缘子串 (Insulator String)


## 定义与边界

绝缘子串是由多个绝缘子单元串联组成的支撑和绝缘结构，用于悬挂输电导线并承受导线与杆塔之间的电气绝缘和机械载荷。在EMT仿真中，绝缘子串模型主要用于分析操作过电压、雷击过电压下的闪络特性，以及污染条件下的绝缘配合。

**边界限定**：本页面聚焦于绝缘子串的电气建模与闪络特性，不包括机械强度设计或绝缘子材料学。

## EMT中的作用

绝缘子串是过电压分析与绝缘配合的关键元件：

- **闪络建模**：预测过电压条件下绝缘子串的空气间隙击穿
- **雷击分析**：分析直击雷或感应雷引起的绝缘子闪络
- **污染闪络**：评估污秽条件下绝缘子表面放电风险
- **绝缘配合**：确定绝缘子串长度与过电压保护水平

## 主要分支与机制

### 1. 空气间隙闪络模型

基于流注理论或先导发展理论的间隙击穿：

**临界闪络电压**：
$$U_{50} = k \cdot d^n$$

其中$d$为间隙距离，$k$和$n$为经验系数（标准大气条件下$n \approx 0.6$）。

**伏秒特性**：
$$U(t) = U_{50} \cdot \left(1 + \frac{K}{t^{0.5}}\right)$$

描述冲击电压下闪络电压与波头时间的关系。

### 2. 污闪模型

污染条件下绝缘子表面放电：

**表面电导率**：
$$G_s = \frac{1}{R_s} = \frac{L}{\rho_s \cdot l}$$

其中$\rho_s$为表面电阻率，$L$为泄漏距离，$l$为沿面长度。

**局部电弧发展**：
$$U_{arc} = A \cdot I^{-n} \cdot x$$

$x$为电弧长度，$A$和$n$为电弧特性常数。

### 3. 绝缘子串等效电路

多单元串联的等效表示：
- 每个单元：电容$C_i$与表面电导$G_i$并联
- 串接电容：$C_{eq} = C_i/n$
- 电压分布：首端绝缘子承受最高电压（30-40%）

## 形式化表达

### 闪络判据

时变电压下闪络条件：
$$\int_0^{t_f} (U(t) - U_{crit})^m dt = K$$

积分超过阈值$K$时发生闪络，$m$为经验指数。

### 绝缘子串电压分布

$n$片绝缘子串联，对地电容$C_g$与片间电容$C_s$：
$$\frac{V_k}{V} = \frac{\sinh(\alpha k)}{\sinh(\alpha n)}$$

其中$\alpha = \text{arccosh}(1 + C_g/C_s)$。

### 50%闪络电压

标准波（1.2/50 μs）下：
$$U_{50} = 540 \cdot d \quad (\text{kV/m}, \text{正极性})$$
$$U_{50} = 600 \cdot d \quad (\text{kV/m}, \text{负极性})$$


## 量化性能边界

绝缘子串模型在 EMT 仿真中缺乏针对性的可核验量化结果。现有研究主要归属于输电线路雷击暂态和绝缘配合领域，不直接提供绝缘子串作为独立 EMT 模型的逐时步仿真性能指标。

- **雷击闪络响应**：基于流注发展或先导发展模型的绝缘子闪络判据通常在 EMTP/ATP 等软件中以 TACS 或 MODELS 控制块形式实现，其计算耗时受闪络判据积分步长和检测逻辑复杂度影响，但现有文献未单独报告绝缘子串闪络模型本身的仿真步长、加速比或精度百分比（Rizk 1978）。

- **污染闪络建模**：污闪模型（表面电导率+局部电弧发展）的 EMT 实现主要依赖经验参数 $A$ 和 $n$ 的离线标定，时域仿真中电弧动态的逐时步更新开销未见独立量化报告。

- **绝缘配合仿真**：绝缘子串的等效电容-电导网络在过电压分析中通常作为输电线路或变电站模型的附属元件参与节点求解，其单独的计算开销和精度贡献未被分解量化。

这些量化缺口不构成对绝缘子串建模方法的否定，只说明现有公开文献尚未将该元件的 EMT 计算性能作为独立研究对象进行可核验的量化报告。

## 适用边界与失败模式

### 适用条件

- 标准大气条件或已知修正系数
- 绝缘子表面状态已知（清洁/污秽）
- 过电压波形类型明确（操作/雷电）
- 海拔高度在修正范围内

### 失效边界

- **海拔影响**：高海拔地区空气密度降低，闪络电压下降
- **湿度影响**：绝对湿度影响流注发展
- **污染程度**：ESDD（等值盐密）和NSDD（非可溶沉积物密度）
- **老化退化**：瓷质劣化、玻璃自爆、复合绝缘子伞裙老化
- **雨闪**：大雨条件下表面水膜引起的闪络

### 关键假设

1. 闪络模型基于统计特性，存在分散性
2. 电压分布假设线性电容网络
3. 污闪模型假设均匀污染分布
4. 气象条件（温度、湿度、气压）可修正

## 代表性来源

- [[emt-simulation]] - EMT仿真基础
- [[power-system]] - 电力系统建模
- [[electromagnetic-transient]] - 电磁暂态分析
- [[control-system]] - 控制系统设计
- [[real-time-simulation]] - 实时仿真技术
### 标准与规范

- IEC 60060 - 高电压试验技术
- IEC 60507 - 人工污秽试验
- IEEE Std. 1313 - 绝缘配合标准
- GB/T 311 - 绝缘配合标准

### 研究文献

- Rizk, F.A.M., "Switching Surge Strength of Air Insulation," *IEEE PAS*, 1978.
- [[transmission-line-model]] - 线路绝缘配合
- [[lightning-overvoltage]] - 雷击过电压分析

## 与相关页面的关系

- [[transmission-line-model]] - 输电线路整体建模
- [[lightning-transient-analysis]] - 雷击暂态分析
- [[switching-transient]] - 操作过电压分析
- [[surge-arrester-model]] - 避雷器模型
- [[grounding-system-model]] - 接地系统模型
- [[ieee-14-bus-system]] - IEEE 14节点测试系统
- [[emt-simulation]] - EMT仿真基础

## 开放问题

- 复合绝缘子长期老化与闪络特性变化
- 特高压（UHV）长空气间隙闪络机理
- 复杂地形条件下绝缘子闪络预测
- 智能绝缘子在线监测技术
- 新型环境友好型绝缘材料

## 参考标准

- IEC 60060-1 - 高电压试验技术
- IEC 60507 - 交流系统用绝缘子人工污秽试验
- IEEE Std. 1313.1 - 绝缘配合应用指南
- GB/T 311.1-2012 - 绝缘配合

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[equivalent-circuit-model-of-a-transmission-tower-considering-a-lightning-struck-|Equivalent Circuit Model of a Transmission Tower Considering]] | 2021 |
| [[full-wave-black-box-transmission-line-tower-model-for-the-assessment-of-lightnin|Full-wave black-box transmission line tower model for the as]] | 2021 |
| [[influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio|Influence of a lossy ground on the lightning performance of ]] | 2022 |
