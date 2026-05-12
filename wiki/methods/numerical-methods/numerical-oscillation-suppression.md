
---
title: "数值振荡抑制 (Numerical Oscillation Suppression)"
type: method
tags: [numerical-oscillation, cda, interpolation, backward-euler, 2s-dirk]
created: "2026-05-02"
updated: "2026-05-10"
---

# 数值振荡抑制 (Numerical Oscillation Suppression)

## 1. 物理背景与工程需求

### 为什么需要数值振荡抑制？

数值振荡是固定步长 EMT 仿真中特有的一种非物理伪影。当系统发生不连续事件（开关动作、故障投入、保护跳闸、二极管换相）时，梯形法的稳定性函数 $R(z) \to -1$ 会使高频数值分量在相邻步之间交替换号但不衰减——表现为波形上的步间毛刺。

数值振荡抑制不是把真实的线路行波、谐振或控制振荡压平。它的目标是区分并消除**纯粹由离散化方式导致的虚假振荡**。

### 三条技术路线

数值振荡抑制有三种根本不同的方法：

1. **事件定位 + 插值**：对齐真实开关时刻，消除事件定位误差
2. **积分公式切换（CDA）**：用后向欧拉的 L-稳定特性阻尼高频数值模态
3. **替换主积分器（2S-DIRK）**：从积分格式层面避免 $R(z) \to -1$ 问题

| 软件 | 主积分器 | 振荡抑制策略 |
|------|---------|-------------|
| PSCAD/EMTDC | 梯形法 | 瞬时解插值（插值修复） |
| EMTP-RV | 梯形法 + CDA | 积分公式切换 |
| XTAP | 2S-DIRK（可选） | 替换积分器 |

---

## 2. 数学描述

### 振荡的数学根源

梯形法的稳定性函数：

$$
R(z) = \frac{1 + z/2}{1 - z/2}, \quad z = \lambda \Delta t
$$

当 $z \to -\infty$（高频刚性模态）：$R(z) \to -1$。

对测试方程 $\dot{x} = \lambda x$，$\lambda$ 为大的负实数：

$$
x_{n+1} \approx -x_n
$$

这就是数值振荡的数学本质——步间交替但不发散。

### 振荡的物理触发场景

Nzale et al. (2021) 系统分析了三种误差的叠加效应：

1. **事件定位误差**：开关时刻 $t_s$ 落在 $[t_n, t_{n+1}]$ 之间
2. **同时换相遗漏**：多个器件在极短时间内联动切换
3. **历史项污染**：切换前拓扑的历史信息带入切换后网络

---

## 3. 计算模型与离散化

### 策略一：事件插值 + 半步 BE（Na et al., 2023）

BE 的历史电流源只依赖上一时刻的电感电流 $i_L(t_z)$，不像梯形法还依赖电压差，因此不会把电压不连续注入历史项。

**量化效果**（Na et al. 2023, 双有源桥）：
- 虚假开关损耗：212.6 $\mu$J（普通插值）$\to$ 约 2 $\mu$J（该方法），消除率 > 99%
- 消除了瞬时插值法固有的“提前一个时间步”的数值误差
- 半步 BE 的等效导纳与全步梯形法兼容，无需额外矩阵分解

### 策略二：CDA（Critical Damping Adjustment）

Marti 和 Lin (1989) 提出，EMTP 中最经典的振荡抑制：

```text
正常步进：... 梯形法 -> 梯形法 -> 梯形法 -> ...
突变时刻：... 梯形法 -> [开关动作] -> BE(半步) -> BE(半步) -> 梯形法 -> ...
```

Zhao et al. (2020) 用 CQLF 理论证明了 CDA 在严格无源条件下不破坏稳定性。

### 策略三：2S-DIRK 替代主积分器

Noda (2014) 将 2S-DIRK 用于 EMT。不需要 CDA 的事件检测机制，由积分格式本身避免振荡。代价：每步两次隐式求解。

---

## 4. 实现方法与算法细节

### 振荡识别

可用离散二阶差分作为筛查工具：

$$
d_n = x_{n+1} - 2x_n + x_{n-1}
$$

该指标不能单独证明振荡是数值伪影，需结合能量、步长收敛和物理模型判断。

### 三种策略的组合效果

| 方法组合 | 振荡幅值降低 | 额外计算代价 |
|----------|-------------|-------------|
| 仅 CDA (TR+BE) | 中等 | 无 |
| TR+BE+线性插值 | 约 3000 倍 | 每次事件 1 次额外求解 |
| TR+BE+插值+外推重初始化 | 约 3000 倍 | 每次事件 2 次额外求解 |
| 2S-DIRK（替代主积分器） | 无持续振荡 | 每步 2 次隐式求解 |

---

## 5. 适用边界与失效模式

### 什么条件下好用？

- 开关/故障事件后需要快速消除步间振荡
- 梯形法主积分器配合 CDA/插值作为事件后补充

### 什么条件下会出问题？

| 问题场景 | 表现 | 原因 | 缓解办法 |
|----------|------|------|----------|
| CDA 未配合插值 | 振荡仍明显 | 只处理了历史项污染 | 配合线性插值 |
| 多开关同步动作 | 结果取决于处理顺序 | 同时换相遗漏 | 同时处理机制 |
| 真实高频暂态是研究对象 | CDA 抑制了物理振荡 | 无差别阻尼所有高频 | CDA 窗口调整 |
| 非线性元件工作点跨段 | 不被事件检测捕获 | 限幅/磁化曲线切换 | 扩展事件检测范围 |
| 非严格无源系统 | 稳定性未保证 | CQLF 分析仅处理充分条件 | 单独验证 |

### 工程经验值

- CDA 窗口通常为 1 步（2 个 $\Delta t/2$ 半步）
- CDA 检测判据：$|x_{n+1} - x_n| > K \cdot \max(|x_n|, |x_{n-1}|)$，$K$ 取 3-5
- Na et al. (2023) 方法使虚假损耗降低 > 99%
- 若高频暂态是研究对象（GIS VFTO），强阻尼策略需谨慎

---

## 6. 应用案例

### RL 电路的振荡消除对比

$L = 50$ mH，$R = 10$ $\Omega$，$\tau = L/R = 5$ ms。投入 $V_s = 100$ V：

$$
i(t) = \frac{V_s}{R}(1 - e^{-t/\tau}) = 10(1 - e^{-t/0.005})
$$

### 验证步骤

1. 用纯梯形法仿真，在 $t = 10$ ms 处短路
2. 观察短路后电流是否出现步间交替
3. 对比 CDA、插值+BE、小步长参考解三种策略

数值试验请使用 EMTP 类软件或自行编程实现。

---

## 7. 延伸阅读

### 核心参考文献

- [[an-improved-high-accuracy-interpolation-method-for-switching-devices-in-emt-simu]] — Na et al. (2023)：插值+半步 BE，损耗降 > 99%
- [[stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da]] — Zhao et al. (2020)：CQLF 稳定性框架
- [[suppression-of-numerical-oscillations-in-the-emtp-power-systems]] — Marti (2004)：CDA 算法
- [[accurate-time-domain-simulation-of-power-electronic-circuits]] — Nzale et al. (2021)：三种误差源
- [[supplementary-techniques-for-2s-dirk-based-emt-simulations]] — Noda (2014)：2S-DIRK 替代方案

### 相关页面

- [[trapezoidal-rule]] — 数值振荡的常见来源
- [[backward-euler]] — CDA 的核心积分器
- [[gear-method]] — 替代积分规则
- [[numerical-damping-optimization]] — 阻尼强度与优化权衡
- [[switch-modeling]] — 开关模型细节
- [[companion-circuit]] — 伴随电路与历史项的关系
- [[voltage-interpolation]] — 开关时刻对齐的局部方法
