---
title: "声明式建模 (Declarative Modeling)"
type: method
tags: [declarative-modeling, equation-based, modelica, acausal, component-modeling]
created: "2026-05-04"
---

# 声明式建模 (Declarative Modeling)

## 定义与边界

声明式建模是一种基于方程而非赋值语句的建模范式，用户通过声明物理系统的守恒方程和本构关系来描述模型，由求解器自动处理方程排序和求解。与传统的过程式建模（如C、Fortran）不同，声明式建模关注"是什么"而非"怎么做"，适合复杂物理系统的多领域建模。

**边界限定**：本页面聚焦于声明式建模在电力系统中的应用，不包括通用编程语言对比。

## EMT中的作用

声明式建模提升模型复用性和可维护性：

- **组件复用**：模型与仿真上下文解耦
- **方程自动处理**：符号微分和方程优化
- **多领域耦合**：电气、机械、热、控制统一建模
- **模型交换**：标准化的模型描述格式

## 主要分支与机制

### 1. 因果关系与无因果建模

**过程式（因果）**：
```c
i = (v1 - v2) / R;  // 明确输入输出
```

**声明式（无因果）**：
```modelica
v1 - v2 = R * i;    // 方程关系，方向待定
```

### 2. 连接语义

**基尔霍夫定律自动生成**：
- 连接点自动应用KCL
- 回路自动应用KVL

**连接器定义**：
```modelica
connector Pin
    Real v;
    flow Real i;
end Pin;
```

### 3. EMT应用工具

**Modelica**：
- 开放的方程建模语言
- 电力系统库（PowerSystems）

**Simscape**：
- MATLAB的物理建模环境
- 电气、机械、流体领域

**PLECS**：
- 电力电子专用
- 与Simulink集成

## 形式化表达

### 方程分类

**微分方程**：
$$\frac{dx}{dt} = f(x, t)$$

**代数方程**：
$$0 = g(x, t)$$

**离散方程**：
$$x_{n+1} = h(x_n)$$

### DAE索引降阶

高索引DAE通过微分或替换降为指数1：
$$\text{Index }2 \rightarrow \text{Index }1$$

## 适用边界与失败模式

### 适用条件

- 物理关系明确
- 方程可微
- 索引适当

### 失效边界

- **代数环**：结构奇异
- **高索引**：数值困难
- **不连续**：事件处理复杂

## 与相关页面的关系

- [[modeling-language]] - 建模语言
- [[state-space-method]] - 状态空间法
- [[nodal-analysis]] - 节点分析法
- [[companion-circuit-model]] - 伴随电路模型
- [[dae-solvers]] - DAE求解器
- [[acausal-modeling]] - 无因果建模
- [[equation-based-modeling]] - 基于方程的建模
- [[modelica-language]] - Modelica语言
- [[numerical-integration]] - 数值积分方法
- [[state-space-method]] - 状态空间法

## 代表性来源

- Fritzson, P., "Principles of Object-Oriented Modeling and Simulation with Modelica 3.3," *Wiley*, 2014.

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
