---
title: "固态变压器 (Solid State Transformer, SST)"
type: model
tags: [solid-state-transformer, sst, power-electronic-transformer, pet, ac-dc-ac, isolation]
created: "2026-05-04"
---

# 固态变压器 (Solid State Transformer, SST)

## 定义与边界

固态变压器（SST）是基于电力电子变换器实现的智能变压器，通过AC-DC-AC或AC-AC变换实现电压变换和电气隔离。与传统工频变压器相比，SST具有体积小、重量轻、可控性强、功能集成度高等优点，可实现电压调节、谐波隔离、故障限流等高级功能。

**边界限定**：本页面聚焦于SST的拓扑结构和EMT建模，不包括磁性元件设计细节。

## EMT中的作用

SST是智能电网的关键设备：

- **电压调节**：动态无功补偿和电压支撑
- **故障隔离**：快速限制故障电流
- **谐波隔离**：阻止谐波传播
- **直流接口**：天然兼容交直流混合电网
- **能量路由**：智能能量管理和分配

## 主要分支与机制

### 1. 三级式SST

**结构**：
- 输入级：AC-DC整流（NPC或MMC）
- 隔离级：DC-DC高频变换（DAB或CLLC）
- 输出级：DC-AC逆变

**双有源桥（DAB）**：
$$P = \frac{nV_1V_2}{f_sL}\phi(1 - \frac{\phi}{\pi})$$

$\phi$为移相角。

### 2. 单级式SST

直接AC-AC变换：
- 矩阵变换器
- 无直流环节
- 效率更高，控制更复杂

### 3. 控制策略

**电压控制**：
- 输入级：功率因数校正
- 隔离级：直流母线电压控制
- 输出级：电压幅值/频率控制

**协调控制**：
- 三级间功率平衡
- 故障穿越

## 形式化表达

### DAB变换器

功率传输：
$$P = \frac{nV_1V_2}{2f_sL}\phi(1 - \frac{|\phi|}{\pi})$$

软开关条件：
$$I_{peak} > \frac{V_1 - nV_2}{2f_sL} \cdot D$$

### 电压变比

总变比：
$$\frac{V_{out}}{V_{in}} = m_1 \cdot n \cdot m_2$$

$m_1$、$m_2$为PWM调制比，$n$为高频变压器变比。

## 适用边界与失败模式

### 适用条件

- 功率等级在可接受范围
- 效率要求可接受
- 控制带宽足够
- 散热条件满足

### 失效边界

- **过流保护**：器件过流能力有限
- **效率限制**：高于传统变压器损耗
- **成本限制**：初期投资较高
- **可靠性**：大量电力电子器件

## 与相关页面的关系

- [[power-electronic-transformer]] - 电力电子变压器
- [[dual-active-bridge]] - 双有源桥变换器
- [[mmc-model]] - MMC换流器（输入级）
- [[vsc-model]] - VSC换流器（输出级）
- [[transformer-model]] - 传统变压器模型

## 代表性来源

- McMurray, W., "The Thyristor Electronic Transformer," *IEEE IGA*, 1968.
- She, X., et al., "Solid State Transformer in the Future Smart Grid," *CISS*, 2012.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
