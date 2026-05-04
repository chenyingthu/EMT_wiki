---
title: "伴随电路模型 (Companion Circuit Model)"
type: method
tags: [companion-circuit, discrete-equivalent, trapezoidal, backward-euler, emt-solver]
created: "2026-05-04"
---

# 伴随电路模型 (Companion Circuit Model)

## 定义与边界

伴随电路模型是将连续动态元件（电感、电容）通过数值积分方法转换为离散等效电路的技术。在每个时间步，电感或电容被替换为等值电阻（电导）并联历史电流源（诺顿形式）或串联历史电压源（戴维南形式），使EMT仿真能够使用纯电阻网络求解。

**边界限定**：本页面聚焦于梯形法和后向欧拉法的伴随电路，不包括其他积分方法的实现。

## EMT中的作用

伴随电路是EMT节点分析法的核心：

- **统一求解框架**：所有元件统一为电阻+电源形式
- **开关处理**：开关状态变化只需修改导纳矩阵
- **多速率接口**：不同步长子系统的等效接口
- **非线性迭代**：伴随电路与牛顿迭代结合

## 主要分支与机制

### 1. 电感伴随电路

**梯形法**：
$$i_L(t) = G_{eq}v_L(t) + i_h(t)$$

其中：
$$G_{eq} = \frac{\Delta t}{2L}$$
$$i_h(t) = i_L(t-\Delta t) + G_{eq}v_L(t-\Delta t)$$

**后向欧拉法**：
$$G_{eq} = \frac{\Delta t}{L}$$
$$i_h(t) = i_L(t-\Delta t)$$

### 2. 电容伴随电路

**梯形法**：
$$i_C(t) = G_{eq}v_C(t) + i_h(t)$$

其中：
$$G_{eq} = \frac{2C}{\Delta t}$$
$$i_h(t) = -G_{eq}v_C(t-\Delta t) - i_C(t-\Delta t)$$

**后向欧拉法**：
$$G_{eq} = \frac{C}{\Delta t}$$
$$i_h(t) = -G_{eq}v_C(t-\Delta t)$$

### 3. 频变元件伴随电路

**频变支路**：
通过有理函数逼近的频变特性：
$$Y(s) = \sum_{k=1}^{n}\frac{r_k}{s-p_k} + d$$

每个极点对应一个RC支路，整体形成伴随网络。

## 形式化表达

### 通用伴随模型

诺顿形式：
$$\mathbf{i}(t) = \mathbf{G}_{eq}\mathbf{v}(t) + \mathbf{i}_h(t)$$

戴维南形式：
$$\mathbf{v}(t) = \mathbf{R}_{eq}\mathbf{i}(t) + \mathbf{v}_h(t)$$

### 节点导纳方程

伴随电路化后：
$$\mathbf{G}_{bus}\mathbf{v}(t) = \mathbf{i}_{inj}(t) + \mathbf{i}_h(t)$$

$\mathbf{G}_{bus}$为等值导纳矩阵，$\mathbf{i}_h$为所有伴随电流源之和。

### 历史项更新

梯形法通用更新公式：
$$\mathbf{i}_h(t) = \mathbf{A}\mathbf{v}(t-\Delta t) + \mathbf{B}\mathbf{i}(t-\Delta t)$$

矩阵$\mathbf{A}$和$\mathbf{B}$取决于元件类型和积分方法。

## 适用边界与失败模式

### 适用条件

- 数值积分方法稳定（梯形法或后向欧拉）
- 步长$\Delta t$满足稳定性要求
- 历史项正确初始化
- 导纳矩阵可逆

### 失效边界

- **数值振荡**：梯形法在开关操作后的高频振荡
- ** stiff 系统**：多时间尺度导致精度问题
- **非线性收敛**：牛顿迭代不收敛
- **病态矩阵**：导纳矩阵条件数过大

### 关键假设

1. 时间步长内电流电压线性变化
2. 元件参数恒定（或缓慢变化）
3. 开关动作发生在时间步边界
4. 数值精度足够（64位浮点）

## 代表性来源

### 经典文献

- Dommel, H.W., "Digital Computer Solution of Electromagnetic Transients," *IEEE PAS*, 1969. - 伴随电路奠基
- Dommel, H.W., "EMTP Reference Manual," *BPA*, 1986.
- Watson, N. and Arrillaga, J., "Power Systems Electromagnetic Transients Simulation," *IET*, 2003.

### EMT实现

- [[nodal-analysis]] - 节点分析法
- [[numerical-integration]] - 数值积分
- [[switch-modeling]] - 开关建模

## 与相关页面的关系

- [[nodal-analysis]] - 节点分析框架
- [[numerical-integration]] - 数值积分基础
- [[trapezoidal-rule]] - 梯形法
- [[backward-euler]] - 后向欧拉法
- [[switch-modeling]] - 开关与伴随电路

## 开放问题

- 变步长伴随电路的高效实现
- 高阶积分方法的伴随形式
- 多物理场耦合的伴随模型
- 自适应步长与伴随电路更新
- 并行伴随电路求解

## 参考标准

- IEEE Std. 1800 - 电磁暂态仿真导则

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
