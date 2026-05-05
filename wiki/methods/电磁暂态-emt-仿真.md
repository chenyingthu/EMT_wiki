---
title: "电磁暂态-emt-仿真"
type: method
tags: [电磁暂态-emt-仿真, high-value-link, auto-enriched]
created: "2026-05-05"
---

# 电磁暂态-emt-仿真

## 定义与边界

电磁暂态（EMT）仿真是对电力系统电磁过程进行时域数值模拟的方法，能够精确描述纳秒至秒级时间范围内的电压电流瞬态变化。

**边界限定**：适用于电力系统电磁暂态仿真分析，时间尺度覆盖微秒至秒级。

## EMT中的作用

- 分析开关操作、故障、雷击引起的快速暂态过程
- 研究电力电子设备的开关特性和控制策略
- 验证保护装置的暂态响应特性
- 评估绝缘配合和过电压水平

## 主要分支与机制

- 离线仿真：高精度的非实时仿真
- 实时仿真：满足硬实时约束的仿真
- 硬件在环仿真：与物理控制器交互的仿真
- 多速率仿真：不同时间尺度的混合仿真

## 形式化表达


EMT仿真的核心离散化方程：

梯形法则离散：
$$x_{n+1} = x_n + \frac{h}{2}(f(t_n, x_n) + f(t_{n+1}, x_{n+1}))$$

节点导纳方程：
$$\mathbf{Y}_n\mathbf{v}_n = \mathbf{i}_n^{hist} + \mathbf{i}_n^{src}$$

其中 $\mathbf{i}_n^{hist}$ 为历史电流源，$\mathbf{i}_n^{src}$ 为独立电流源。

时间步长选择准则：
$$h \leq \frac{1}{10 f_{max}}$$

$f_{max}$ 为关注的最高频率分量。
        

## 适用边界与失败模式

- 计算精度受时间步长和数值积分方法影响
- 大规模系统实时仿真的计算资源需求高
- 模型参数准确性直接影响仿真结果可信度

## 与相关页面的关系

- [[numerical-integration]] - 数值积分方法
- [[real-time-simulation]] - 实时仿真技术
- [[hil-simulation]] - 硬件在环仿真
- [[multirate-method]] - 多速率仿真方法
- [[co-simulation]]
## 代表性来源

- Dommel, H.W. (1969). Digital Computer Solution of Electromagnetic Transients
- EMTP-RV Theory Manual

---

*本页面由自动增强脚本生成并补充专业内容。最后更新：2026-05-05*
