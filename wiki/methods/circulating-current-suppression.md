---
title: "环流抑制控制 (Circulating Current Suppression Control)"
type: method
tags: [circulating-current, ccs, mmc, control, capacitor-voltage, ripple]
created: "2026-05-04"
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
