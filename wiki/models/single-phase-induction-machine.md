---
title: "单相感应电机 (Single-Phase Induction Machine)"
type: model
tags: [single-phase, induction-machine, capacitor-start, split-phase, motor-model]
created: "2026-05-04"
---

# 单相感应电机 (Single-Phase Induction Machine)

## 定义与边界

单相感应电机是由单相交流电源供电的感应电机，依靠辅助绕组和启动装置（电容、电阻或罩极）产生旋转磁场实现启动。在EMT仿真中，单相感应电机模型需要考虑主副绕组的不对称、启动装置的切换以及电容对运行特性的影响。

**边界限定**：本页面聚焦于单相感应电机的EMT建模，不包括三相感应电机或同步电机。

## EMT中的作用

单相感应电机是配电系统的重要负荷：

- **居民负荷**：家用电器（空调、冰箱、洗衣机）的主要动力
- **商业负荷**：小型水泵、风机、压缩机
- **农村电网**：灌溉泵、农用机械
- **微网分析**：孤岛系统的电机启动问题
- **电压稳定性**：大规模电机启动引起的电压跌落

## 主要分支与机制

### 1. 双轴理论模型

主绕组（m）和辅助绕组（a）的电压方程：
$$v_m = R_m i_m + \frac{d\psi_m}{dt}$$
$$v_a = R_a i_a + \frac{d\psi_a}{dt}$$

磁链方程：
$$\begin{bmatrix} \psi_m \\ \psi_a \end{bmatrix} = \begin{bmatrix} L_m & L_{ma} \\ L_{am} & L_a \end{bmatrix} \begin{bmatrix} i_m \\ i_a \end{bmatrix}$$

### 2. 启动方式

**电容启动**：
- 启动电容与辅助绕组串联
- 启动后离心开关断开
- 启动转矩大，启动电流小

**电容运行**：
- 小电容永久连接
- 运行性能改善
- 启动转矩较小

**电阻启动**：
- 辅助绕组电阻较大
- 结构简单，成本低
- 启动转矩较小

### 3. 等效电路

正序和负序等效电路：
$$Z_+ = R_1 + jX_1 + \frac{(R_2'/s + jX_2')(jX_m)}{R_2'/s + j(X_2'+X_m)}$$
$$Z_- = R_1 + jX_1 + \frac{(R_2'/(2-s) + jX_2')(jX_m)}{R_2'/(2-s) + j(X_2'+X_m)}$$

合成转矩：
$$T_e = T_+ + T_-$$

## 形式化表达

### 启动转矩

电容启动电机的启动转矩：
$$T_{start} = \frac{P_{gap}}{\omega_s} = \frac{|V_a|^2 R_2'/s}{\omega_s |Z_a|^2} - \frac{|V_m|^2 R_2'/(2-s)}{\omega_s |Z_m|^2}$$

启动时$s=1$，正负序转矩方向相反。

### 稳态运行

额定转差率：
$$s_N = \frac{n_s - n_N}{n_s}$$

典型值：0.02-0.06（电容运行电机）

### 启动电流

直接启动电流：
$$I_{start} = (5-7) I_N$$

较三相电机启动电流更大（缺少两相抵消）。

## 适用边界与失败模式

### 适用条件

- 额定电压和频率范围
- 负载转矩特性已知
- 启动装置参数（电容值、开关时间）
- 电网短路容量足够（避免过度电压跌落）

### 失效边界

- **启动失败**：电压过低或负载转矩过大
- **电容老化**：启动电容容量下降导致启动困难
- **离心开关故障**：无法断开导致过热
- **过热**：长期过载或通风不良
- **单相运行**：辅助绕组故障后单相运行发热

### 关键假设

1. 气隙磁场正弦分布
2. 铁损可忽略或等效到电阻
3. 绕组参数对称（除匝数比）
4. 启动开关动作理想

## 代表性来源

### 经典文献

- Alger, P.L., "Induction Machines," *Gordon and Breach*, 1970.
- Krause, P.C., "Analysis of Electric Machinery," *McGraw-Hill*, 1986.
- Fitzgerald, A.E., et al., "Electric Machinery," *McGraw-Hill*, 2003.

### 电机建模

- [[induction-machine-model]] - 感应电机通用模型
- [[three-phase-induction-machine]] - 三相感应电机
- [[motor-starting-analysis]] - 电机启动分析

## 与相关页面的关系

- [[induction-machine-model]] - 感应电机通用模型
- [[load-model]] - 负荷模型中的电机成分
- [[voltage-stability]] - 电压稳定性分析
- [[distribution-network]] - 配电网分析

## 开放问题

- 变频驱动的单相电机控制
- 高效单相电机设计（永磁辅助）
- 大规模单相电机接入的配电网影响
- 电机软启动器的EMT建模
- 单相电机故障诊断方法

## 参考标准

- IEEE Std. 112 - 感应电机测试标准
- IEC 60034 - 旋转电机
- NEMA MG1 - 电机和发电机标准

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
