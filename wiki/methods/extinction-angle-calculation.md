---
title: "关断角计算 (Extinction Angle Calculation)"
type: method
tags: [extinction-angle, gamma, lcc-hvdc, commutation, inverter]
created: "2026-05-02"
---

# 关断角计算 (Extinction Angle Calculation)


```mermaid
graph TD
    subgraph Ncmp[关断角计算 (Extinction Angle Calc…]
        N0[$\alpha$ 或 $\beta$: 触发角或超前触发角]
        N1[$I_d$: 直流电流]
        N2[$X_c$ 或 $L_c$: 换相电抗/电感]
        N3[$E$ 或 $U_{LL}$: 换相电压幅值]
        N4[$\mu$: 换相重叠角]
    end
```


## 概述

关断角计算（Extinction Angle Calculation）用于估计 LCC 逆变器中晶闸管电流降为零后，到该阀重新承受正向电压前的电角度裕度。它是 [[lcc-model]]、[[thyristor-control]] 和换相失败分析中的关键方法。

关断角 $\gamma$ 是线换相换流器的概念。它不适用于用 IGBT、IGCT 或 MMC 子模块自换相的 [[vsc-model]]。VSC 中的 PLL、dq 电流控制或 PWM 相位同步不能称为关断角控制；若页面同时讨论 LCC 和 VSC，应把两类控制边界分开。

## 定义与变量

在理想稳态换相关系中，关断角常写为：

$$\gamma=\pi-\alpha-\mu$$

其中 $\alpha$ 为触发延迟角，$\mu$ 为换相重叠角。若采用逆变器侧的超前触发角 $\beta$，则 $\beta=\pi-\alpha$，并有 $\gamma=\beta-\mu$。这些公式依赖相角定义、阀组约定和交流电压参考点；引用时必须说明使用的是整流侧还是逆变侧符号。

计算输入通常包括：

| 变量 | 含义 | 证据边界 |
|------|------|----------|
| $\alpha$ 或 $\beta$ | 触发角或超前触发角 | 来自控制器或测量同步逻辑 |
| $I_d$ | 直流电流 | 暂态中可能快速变化 |
| $X_c$ 或 $L_c$ | 换相电抗/电感 | 多由换流变漏抗和系统等值决定 |
| $E$ 或 $U_{LL}$ | 换相电压幅值 | 故障、谐波和不平衡会改变有效换相电压 |
| $\mu$ | 换相重叠角 | 可由模型、测量或阀电流过零估计 |

## 基本计算流程

关断角计算一般按以下逻辑进行：

1. 从同步电压或阀电压中确定换相电压参考相位。
2. 根据触发时刻、直流电流和换相电抗估计换相重叠角。
3. 用 $\gamma=\pi-\alpha-\mu$ 或同等符号体系计算裕度。
4. 若存在谐波或不平衡，先修正换相电压过零点和重叠角，再计算有效关断角。
5. 将计算结果与论文或工程模型中的临界关断裕度比较，但不得在无来源时给出固定最小值。

常见稳态表达会把 $\gamma$ 写成触发角、直流电流和换相电压的函数。不同教材和论文的系数会随线电压/相电压、峰值/有效值、6 脉动/12 脉动约定而变化；本页只保留关系结构，不新增未绑定来源的精确数值。

## 暂态与谐波修正

交流故障期间，关断角不再只由基波电压幅值决定。电压跌落会降低换相电压，直流电流上升会增加重叠角，谐波会移动换相电压过零点。此时应把计算结果写成“当前模型下的估计关断角”，而不是晶闸管真实恢复裕度的完整测量。

[[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-]] 将多馈入 LCC-HVDC 的谐波交互写成频域等效电路，并用谐波电压传递、过零点偏移和修正重叠角解释远端逆变器关断角变化。该来源支持“谐波交互会影响关断角”的机制性结论；当前页面不沿用其中未核验的精确误差或概率数字。

[[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] 在 LCC 逆变器 PAVM 中把关断角和临界电压跌落阈值用于自动换相失败检测。该结论应限定于线换相逆变器平均值模型和作者验证的换相失败场景。

## 测量与估算

关断角可以由阀电流过零和阀电压极性变化之间的时间差估计，也可以由换流器模型中的 $\alpha$、$\mu$ 和换相电压间接计算。直接测量更贴近阀级过程，但依赖采样、过零检测和滤波；间接计算更适合系统级仿真，但对参数、谐波和暂态电压波形敏感。

EMT 页面中应避免写成“只要 $\gamma$ 大于某个固定角度就不会换相失败”。晶闸管恢复特性、温度、阀组设计、触发脉冲、交流电压畸变和控制延迟都会改变裕度判断。若没有设备手册或论文明确数值，应写为“与临界关断裕度比较”。

## 适用边界

- 适用于 LCC-HVDC 逆变器、晶闸管整流/逆变器和换相失败分析。
- 不适用于 VSC、MMC、构网型逆变器或 PWM 调制中的相位同步问题。
- 稳态公式不应直接用于深度电压跌落、严重不平衡、谐波畸变或并发换相失败风险评估。
- 若用于保护或预警，应说明采样窗口、滤波、过零检测和控制延迟。
- 若用于平均值模型，应说明该模型是否能表示故障阀、重叠角和波形畸变。

## 代表性证据

| 来源 | 证据用途 | 边界 |
|------|----------|------|
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] | 关断角与临界电压跌落阈值用于 LCC 逆变器换相失败检测 | 当前证据未支撑页面新增固定误差或加速数字 |
| [[harmonics-interaction-mechanism-and-impact-on-extinction-angles-in-multi-infeed-]] | 谐波传递、过零点偏移和重叠角修正会影响多馈入系统关断角 | 适用于 LCC 多馈入交流故障场景 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con]] | 阀级拓扑状态和故障换相过程需要模型保留离散晶闸管行为 | 具体系统参数和耗时数字需回原文核对 |

## 与相关页面的关系

- [[thyristor-control]] 说明触发角如何生成。
- [[converter-station-inverter]] 说明 LCC 逆变站中关断角控制的系统位置。
- [[harmonic-transfer-coefficient]] 和 [[harmonic-interaction]] 支撑多馈入场景下的修正计算。
- [[lcc-model]] 是该方法的设备边界；[[vsc-model]] 是不应混用的相邻模型。

## 开放问题

关断角在线估算仍需要把阀级采样、控制延迟、交流电压畸变、直流电流动态和模型参数不确定性放在同一证据链中。当前页面只给出方法框架；工程整定值和设备恢复时间必须来自具体工程资料、器件手册或论文算例。
