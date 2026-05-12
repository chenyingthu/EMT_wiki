---
title: "环流抑制控制 (Circulating Current Suppression Control)"
type: method
tags: [circulating-current, ccs, mmc, control, capacitor-voltage, ripple]
created: "2026-05-04"
updated: "2026-05-12"
---

# 环流抑制控制 (Circulating Current Suppression Control)



## 定义与边界

环流抑制控制（Circulating Current Suppression Control, CCS）是模块化多电平换流器（MMC）中用于抑制相间环流的控制策略。MMC的三相阀臂通过公共直流母线连接，二倍频负序环流会在相间流动，增加开关损耗和电流应力，CCS通过附加控制回路有效抑制该环流。

**边界限定**：本方法适用于三相MMC换流器，单相或两相结构不存在相间环流。

## EMT中的作用

环流抑制是MMC高性能运行的关键：

- **损耗降低**：减少不必要的环流损耗
- **电流应力**：降低器件电流峰值
- **电容电压平衡**：改善子模块电容电压波动
- **效率提升**：提高换流器整体效率

## 主要分支与机制

### 1. 环流机理

**环流成分**：
$$i_{circ,a} = \frac{i_{up,a} + i_{low,a}}{2} = I_{dc}/3 + I_{2f}\cos(2\omega t + \phi)$$

二倍频分量主要由子模块电容电压波动引起。

### 2. 基于比例谐振的控制

**二倍频负序旋转坐标系**：
将环流变换到二倍频旋转坐标系：
$$\begin{bmatrix} i_{2d} \\ i_{2q} \end{bmatrix} = T_{2f} \cdot \begin{bmatrix} i_{circ,a} \\ i_{circ,b} \\ i_{circ,c} \end{bmatrix}$$

**PR控制器**：
$$G_{PR}(s) = K_p + \frac{2K_r s}{s^2 + (2\omega)^2}$$

### 3. 电压注入法

**环流抑制电压**：
$$v_{diff,j} = v_{circ,j}^* - Z_{arm} \cdot i_{circ,j}$$

注入到上下桥臂的差模电压中。

## 形式化表达

### 环流模型

三相环流动态方程：
$$L_{arm}\frac{di_{circ}}{dt} + R_{arm}i_{circ} = v_{diff} - \frac{1}{2}v_{cap,diff}$$

### 抑制效果

抑制前环流幅值：
$$I_{2f} \approx \frac{V_{dc}}{12\omega L_{arm}}$$

抑制后：
$$I_{2f,suppressed} < 0.1 I_{2f,nominal}$$

## 适用边界与失败模式

### 适用条件

- MMC结构完整
- 传感器精度足够
- 控制器带宽足够

### 失效边界

- **测量误差**：零序分量干扰
- **控制饱和**：注入电压超限
- **不对称故障**：负序电流与环流耦合

## 量化性能边界

**Tu 2012 环流抑制对MMC-HVDC直流电压脉动的抑制效果**:
- 针对MMC-HVDC系统，提出基于二倍频负序旋转坐标系的环流抑制策略
- 通过PR控制器在同步旋转坐标系下对环流分量进行闭环调节
- 环流中二倍频分量幅值可被抑制至额定值的10%以下（I2f,suppressed < 0.1 × I2f,nominal）
- 抑制后子模块电容电压波动幅度显著降低，直流侧电压高频脉动被有效抑制
- 数据缺口：原文未报告不同功率等级（MW级 vs GW级）和不同桥臂电抗器参数下的抑制效果变化

**Li 2013 MMC内部环流抑制方法**:
- 提出基于比例谐振（PR）控制的MMC内部环流抑制方法，无需坐标变换
- PR控制器在固定频率（2ω）处提供高增益，实现对二倍频环流的零稳态误差跟踪
- 控制器设计为GPR(s) = Kp + 2Kr·s/(s² + (2ω)²)，其中Kr决定谐振增益
- 桥臂电流THD从抑制前的15%-25%降至抑制后的2%-5%
- 抑制算法对系统参数变化具有鲁棒性，在±10%桥臂电感偏差下仍保持有效
- 数据缺口：PR控制器在频率偏移（非额定50/60Hz）工况下的性能衰减特性未系统评估

**设计参数约束（据方法推断）**:
- 环流抑制效果与桥臂电抗器Larm取值强相关：Larm越大，固有环流幅值I2f越小
- CCS控制器带宽需远低于MMC电流内环带宽，避免控制交互
- 二倍频负序dq变换需要准确锁相，PLL相位误差会直接映射为环流抑制误差
- PR控制器在电网频率波动时谐振峰偏移，可能导致抑制效果下降

**数据缺口声明**：CCS的量化数据来自两篇独立论文（Tu 2012, Li 2013），各自使用不同的MMC测试系统和评估指标。不同CCS拓扑（PR vs dq解耦）在相同测试条件下的横向对比数据缺乏。CCS与MMC内部环流自然特性（桥臂电抗、子模块电容取值）之间的定量关系已被理论分析覆盖，但不同调制策略（NLM vs PWM）下CCS效果的差异未系统评估。高动态工况（如交流故障穿越期间）下CCS的暂态行为数据缺失。

## 与相关页面的关系

- [[mmc-model]] - MMC换流器模型
- [[harmonic-analysis-methods]] - 谐波分析方法
- [[state-space-method]] - 状态空间法
- [[coordinate-transformation]] - 坐标变换方法
- [[average-value-model]] - 平均值模型
- [[nearest-level-control]] - 最近电平控制
- [[vector-control]] - 矢量控制
- [[submodule-model]] - 子模块模型
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法

## 代表性来源

- Tu, Q., et al., "Suppressing DC Voltage Ripples of MMC-HVDC," *IEEE TPEL*, 2012.
- Li, Z., et al., "An Inner Current Suppressing Method for Modular Multilevel Converters," *IEEE TPEL*, 2013.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
