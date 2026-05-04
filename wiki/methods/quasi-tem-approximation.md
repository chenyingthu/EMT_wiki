---
title: "准TEM近似 (Quasi-TEM Approximation)"
type: method
tags: [quasi-tem, transmission-line, high-frequency, wave-propagation, dispersive-media]
created: "2026-05-04"
---

# 准TEM近似 (Quasi-TEM Approximation)

## 定义与边界

准TEM（准横电磁波）近似是分析非理想传输线（如有损地层、频变介质中的线路）电磁传播的一种近似方法。当介质的损耗或频变特性导致纯TEM模式无法存在时，准TEM近似假设电场和磁场仍近似横向分布，但允许存在小的纵向分量，从而简化分析。

**边界限定**：本方法适用于有损线路和低频至中频范围（<1MHz），高频需用全波分析。

## EMT中的作用

准TEM近似是线路暂态分析的理论基础：

- **地回路分析**：考虑大地损耗的线路参数计算
- **频变特性**：频率相关线路参数的建模
- **宽频仿真**：从工频到谐波频段的统一处理
- **电缆建模**：绝缘介质损耗的影响

## 主要分支与机制

### 1. TEM与准TEM对比

**理想TEM**：
- $E_z = 0$, $H_z = 0$
- 无截止频率
- 无色散

**准TEM**：
- $|E_z| \ll |E_t|$, $|H_z| \ll |H_t|$
- 低频近似有效
- 弱色散

### 2. 有损地层影响

**Carson公式**：
大地返回路径的阻抗修正：
$$Z_g = j\omega\frac{\mu_0}{2\pi}\ln\frac{1.85}{h\sqrt{\frac{\omega\mu_0}{\rho}}}$$

**Pollaczek公式**：
更精确的地回路阻抗计算。

### 3. 频变参数

**Skin效应**：
$$R(f) = R_{dc}\sqrt{\frac{f}{f_0}}$$

**Dielectric损耗**：
$$G(f) = \omega C \tan\delta$$

## 形式化表达

### 传播常数

准TEM近似下的传播常数：
$$\gamma = \sqrt{(R + j\omega L)(G + j\omega C)}$$

低频近似：
$$\gamma \approx \frac{R}{2}\sqrt{\frac{C}{L}} + j\omega\sqrt{LC}$$

### 特性阻抗

$$Z_c = \sqrt{\frac{R + j\omega L}{G + j\omega C}}$$

## 适用边界与失败模式

### 适用条件

- 频率较低（$f < 1$ MHz）
- 损耗适中
- 截面尺寸远小于波长

### 失效边界

- **高频**：出现高次模式
- **大损耗**：TEM假设失效
- **不均匀介质**：混合模式

## 与相关页面的关系

- [[transmission-line-model]] - 输电线路模型
- [[cable-model]] - 电缆模型
- [[wideband-modeling]] - 宽频建模
- [[frequency-dependent-modeling]] - 频率相关建模
- [[earth-return-impedance]] - 地回路阻抗
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法

## 代表性来源

- Carson, J.R., "Wave Propagation in Overhead Wires," *BSTJ*, 1926.
- Wedepohl, L.M., "Applications of Matrix Methods," *Proc. IEE*, 1963.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
