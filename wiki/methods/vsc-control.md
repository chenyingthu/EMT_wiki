---
title: "VSC 控制 (VSC Control)"
type: method
tags: [vsc-control, converter-control, dq-control, inverter-control]
created: "2026-05-06"
updated: "2026-05-06"
---

# VSC 控制 (VSC Control)


```mermaid
graph TD
    subgraph S0[VSC 控制 (VSC Control)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[形式化表达]
        N3[相关页面]
        N4[代表性来源]
        N5[开放问题]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

VSC 控制是指电压源换流器及其并网逆变器场景中的同步、内外环、限流、调制和故障控制结构。本页作为概念入口，承接泛化的 `[[vsc-control]]` 链接，不替代具体拓扑或具体控制器页面。

## EMT 中的作用

VSC 控制决定换流器如何跟踪有功/无功、电压或直流侧目标，并在弱网、故障、限流和模式切换时维持可接受动态行为。

## 形式化表达

在 dq 坐标下，VSC 控制常围绕电流内环和外环参考生成组织：

$$
\mathbf{i}_{dq}^* = f_o(\mathbf{r}, \mathbf{y}_m), \qquad
\mathbf{v}_{dq}^* = K_p(\mathbf{i}_{dq}^*-\mathbf{i}_{dq}) + K_i \int (\mathbf{i}_{dq}^*-\mathbf{i}_{dq}) dt + \mathbf{v}_{ff}
$$

其中 $\mathbf{r}$ 为功率、电压或直流侧参考，$\mathbf{y}_m$ 为测量量，$\mathbf{v}_{ff}$ 为前馈和解耦补偿项。这个表达说明接口关系，不代表所有 VSC 都使用同一控制结构。

## 相关页面

- [[vsc-model]]：换流器主电路和接口模型。
- [[dual-loop-pi-controller]]：常见 dq 内外环结构。
- [[pll-model]]：并网同步参考。
- [[vector-control]]：坐标变换和电流/电压控制组织方式。
- [[current-injection]]：控制输出注入网络时的接口形式。
- [[converter-station-inverter]]：VSC 在站级模型中的运行边界。

## 代表性来源

- [[a-vsc-hvdc-model-with-reduced-computational-intensity]]：说明简化 VSC 模型仍需保留控制接口。
- [[dynamic-performance-of-embedded-hvdc-with-13&14]]：说明双环 PI 与运行模式切换在 VSC-HVDC 中的具体组织。
- [[characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir]]：说明 PLL、内外环和延时共同决定控制稳定性。

## 开放问题

- 跟网型与构网型 VSC 是否共享同一入口页，仍需继续细分。
- 弱网、LCL 谐振和延时主导场景下，常规双环表达如何与阻抗分析页衔接。

## 证据边界

本页不把任何控制结构写成通用最优解，也不提供无来源参数。具体控制收益、稳定边界和实现细节必须绑定来源和算例。
