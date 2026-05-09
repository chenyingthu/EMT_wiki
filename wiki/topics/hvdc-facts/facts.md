---
title: "柔性交流输电系统 (FACTS)"
type: topic
tags: [facts, power-electronics, transmission, control, hvac, compensation]
created: "2026-05-02"
---

# 柔性交流输电系统 (FACTS)


```mermaid
graph TD
    subgraph S0[柔性交流输电系统 (FACTS)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[主要分支与机制]
        N3[形式化表达]
        N4[适用边界与失败模式]
        N5[代表性来源]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

柔性交流输电系统（FACTS）是利用电力电子装置调节交流输电系统电压、无功、等效阻抗或相角的设备族。它包括 SVC、STATCOM、TCSC、SSSC、UPFC 等不同拓扑。FACTS 不是单个设备模型，也不能笼统声称提高某个固定比例的输电能力；作用大小取决于装置容量、接入点、控制目标、系统强度和运行约束。

本页作为 topic 页，强调 FACTS 在 EMT 中的角色、分支边界和证据使用。具体装置模型应分别阅读 [[svc-model]]、[[statcom-model]]、[[tcsc-model]] 和 [[statcom]]。

## EMT 中的作用

FACTS 在 EMT 仿真中主要用于研究：

- 晶闸管或 VSC 装置的开关、触发、限幅、控制延迟和保护动作。
- 无功补偿与电压支撑在故障、投切、弱网或新能源并网场景中的暂态响应。
- 串联补偿与线路、电机、风电或 HVDC 控制之间的次同步和宽频交互。
- 控制器硬件在环、保护配合和参数整定验证。

## 主要分支与机制

- 并联补偿：SVC 通过晶闸管控制电抗器/电容器改变等效电纳，STATCOM 通过 VSC 输出可控电流。两者都可用于电压支撑，但动态、谐波和限流边界不同。
- 串联补偿：TCSC 等装置改变线路等效串联阻抗，可影响潮流分布和功角稳定，同时可能引入次同步相互作用风险。
- 组合型控制器：UPFC 或多端 VSC 结构同时调节串联和并联通道。其 EMT 模型需要明确直流侧、换流器控制和保护逻辑。
- 模型层级：开关级模型适合谐波、触发和保护细节；[[average-value-model]] 适合系统级动态；正序或潮流模型只适合较慢的规划和运行分析。

## 形式化表达

FACTS 在网络方程中的作用可抽象为受控并联注入或串联阻抗调节：

$$
i_{\mathrm{sh}} = B_c(x_c,u_c)v,\qquad
v_{\mathrm{line}} = Z_{\mathrm{line}}(x_c,u_c)i_{\mathrm{line}}
$$

其中 $x_c$ 是装置控制状态，$u_c$ 是电压、功率或阻抗指令，$B_c$ 表示并联补偿等效电纳，$Z_{\mathrm{line}}$ 表示线路等效串联阻抗。SVC、STATCOM 和 TCSC 的主要差异，不是“是否提升系统能力”的口号，而是控制变量、阀/换流器实现、限幅保护和频带边界不同。

## 适用边界与失败模式

- FACTS 的“快速控制”不能替代容量约束、限流器、热限制、谐波滤波和保护动作验证。
- 只用稳态潮流或正序模型评估 FACTS，可能遗漏触发延迟、阀组暂态、谐波放大和控制相互作用。
- 串联补偿改变线路等效阻抗时，应检查 [[frequency-domain-analysis]]、[[harmonic-analysis]] 和时域 EMT 中的振荡风险。
- 多 FACTS 或 FACTS-HVDC 协调控制结论应绑定具体控制器、通信延迟和运行点，不能从单装置算例外推。

## 代表性来源

- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]] 适合支撑 SVC 动态相量或混合仿真中的模型层级讨论。
- [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems]] 可作为 HVDC 与 FACTS 联合暂态分析的来源入口，结论应限定在作者系统和模型。
- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]] 支撑 HIL 场景下 SVC/VSC 建模方式选择的边界。
- [[mmc-upfc电磁-机电混合仿真技术研究]] 可作为 UPFC 混合仿真应用来源，不应替代通用 FACTS 设备定义。

## 与相关页面的关系

- [[statcom-model]]、[[svc-model]]、[[tcsc-model]] 是设备模型页；本页只做主题综合和边界说明。
- [[vsc-hvdc]] 同样使用 VSC 技术，但目标是交直流能量转换；FACTS 主要服务于交流输电参数调节。
- [[renewable-energy-integration]] 涉及新能源电压支撑和无功控制；FACTS 是可能的支撑装置之一。
- [[optimal-power-flow]] 可用于规划 FACTS 设点和定值；EMT 负责验证暂态和控制保护可行性。

## 开放问题

- 如何在规划模型、平均值模型和开关级 EMT 之间保持 FACTS 控制参数一致。
- 如何报告 FACTS 控制对振荡阻尼的贡献，同时避免把单个算例结果写成通用能力。
- 如何在多 FACTS、HVDC 和逆变器型电源共存时识别控制交互的主导机制。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems|Combined transient and dynamic analysis of HVDC and FACTS sy]] | 2004 |
