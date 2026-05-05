---
title: "Grid Connected Inverter"
type: model
tags: [grid-connected-inverter]
created: "2026-05-04"
---

# Grid Connected Inverter

## 定义与边界

本页面为自动创建的model类型页面，用于修复断链。内容待补充。

**边界限定**：待完善。

## EMT中的作用

- 待补充


基于相关研究的技术应用：

## 主要分支与机制

- 待补充

## 形式化表达

### 核心数学表达

并网逆变器功率输出：
$$P = rac{3}{2} (v_d i_d + v_q i_q)$$
$$Q = rac{3}{2} (v_q i_d - v_d i_q)$$

PLL锁相环角度估计：
$$\hat{	heta} = \int (\omega_{ff} + k_p v_q + k_i \int v_q dt) dt$$

电流环PI控制：
$$u_d = k_p (i_{d,ref} - i_d) + k_i \int (i_{d,ref} - i_d) dt - \omega L i_q$$


## 适用边界与失败模式

**适用条件**：
- 新能源并网逆变器建模
- 弱电网条件下的稳定性分析
- 电能质量评估

**失效边界**：
- 短路比(SCR)低于临界值
- PLL失稳导致同步丢失
- 电流限幅导致无功支撑不足


## 与相关页面的关系

- [[emt-simulation]] - EMT仿真基础
- [[power-system]]
- [[electromagnetic-transient]]
## 代表性来源

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]
---

*本页面为自动生成的stub，需要进一步补充完善。*

- [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i]]
- [[comparison-and-selection-of-grid-tied-inverter-models-for-accurate-and-efficient]]
- [[advancing-grid-forming-inverter-technology-comprehensive-pq-capability-and-perfo]]
- [[equivalent-grid-following-inverter-based-generator-model-for-atpatpdraw-simulati]]
- [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid]]
