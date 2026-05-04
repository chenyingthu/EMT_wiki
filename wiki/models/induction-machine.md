---
title: "感应电机 (Induction Machine)"
type: model
tags: [induction-machine, asynchronous-motor, squirrel-cage, wound-rotor, emt-modeling]
created: "2026-05-04"
---

# 感应电机 (Induction Machine)

## 定义与边界

感应电机（又称异步电机）是转子转速低于定子旋转磁场转速的交流旋转电机，依靠电磁感应在转子绕组中产生电流和转矩。根据转子结构分为鼠笼式和绕线式两种。在EMT仿真中，感应电机模型需要考虑机电耦合、饱和特性和启动过程。

**边界限定**：本页面聚焦于三相感应电机的EMT建模，不包括单相感应电机或特殊结构电机。

## EMT中的作用

感应电机是电力系统的重要动态负荷：

- **负荷建模**：工业和民用负荷的主要成分
- **启动分析**：大电机启动的电压暂降
- **稳定性分析**：负荷特性对系统稳定的影响
- **故障分析**：不对称故障下的电机响应
- **保护整定**：电机保护的协调配合

## 主要分支与机制

### 1. 电机方程

**dq0坐标系电压方程**：
$$v_{ds} = R_s i_{ds} + \frac{d\psi_{ds}}{dt} - \omega_s\psi_{qs}$$
$$v_{qs} = R_s i_{qs} + \frac{d\psi_{qs}}{dt} + \omega_s\psi_{ds}$$

**磁链方程**：
$$\psi_{ds} = L_s i_{ds} + L_m i_{dr}$$
$$\psi_{qs} = L_s i_{qs} + L_m i_{qr}$$

### 2. 等效电路

**稳态等效电路**：
- 定子电阻$R_s$
- 定子漏抗$X_s$
- 励磁电抗$X_m$
- 转子电阻$R_r'/s$
- 转子漏抗$X_r'$

### 3. 转矩方程

**电磁转矩**：
$$T_e = \frac{3}{2}p\frac{L_m}{L_r}(\psi_{dr}i_{qs} - \psi_{qr}i_{ds})$$

或：
$$T_e = \frac{3V_{th}^2R_r'/s}{\omega_s((R_s + R_r'/s)^2 + (X_s + X_r')^2)}$$

## 形式化表达

### 运动方程

$$J\frac{d\omega_r}{dt} = T_e - T_L$$

转差率：
$$s = \frac{\omega_s - \omega_r}{\omega_s}$$

### 启动电流

直接启动电流：
$$I_{start} = (5-7)I_N$$

启动转矩：
$$T_{start} = (1.5-2.5)T_N$$

## 适用边界与失败模式

### 适用条件

- 额定电压和频率
- 负载转矩特性已知
- 电机参数准确

### 失效边界

- **启动失败**：电压过低或负载过大
- **失速**：转矩不足导致转速下降
- **过热**：长期过载
- **电压暂降**：大电机启动引起

## 与相关页面的关系

- [[dfig-model]] - DFIG模型（双馈感应发电机）
- [[synchronous-machine-model]] - 同步电机模型
- [[power-quality]] - 电能质量（电压暂降）
- [[load-model]] - 负荷模型
- [[coordinate-transformation]] - 坐标变换方法

## 代表性来源

- Krause, P.C., et al., "Analysis of Electric Machinery," *IEEE Press*, 2013.
- Fitzgerald, A.E., et al., "Electric Machinery," *McGraw-Hill*, 2003.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
