---
title: "柔性交流输电系统 (FACTS)"
type: topic
tags: [facts, power-electronics, transmission, control, hvac, compensation, svc, statcom, upfc, tcsc]
created: "2026-05-02"
updated: "2026-05-11"
---

# 柔性交流输电系统 (FACTS)


```mermaid
graph TD
    subgraph S0[柔性交流输电系统 (FACTS)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[主要分支与机制]
        N3[形式化表达]
        N4[量化性能边界]
        N5[适用边界与失败模式]
        N6[代表性来源]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
    N5 --> N6
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
- 老旧 SVC 改造为混合 SVC-VSC 拓扑时，HIL 测试中大步长与小步长建模方法的精度-效率权衡（Le-Huy 2023）。

## 主要分支与机制

- **并联补偿**：SVC 通过晶闸管控制电抗器/电容器改变等效电纳，STATCOM 通过 VSC 输出可控电流。两者都可用于电压支撑，但动态、谐波和限流边界不同。SVC 的响应受触发延迟限制，STATCOM 可更快调节但需考虑 VSC 损耗和谐波。
- **串联补偿**：TCSC 等装置改变线路等效串联阻抗，可影响潮流分布和功角稳定，同时可能引入次同步相互作用风险。
- **组合型控制器**：UPFC 或多端 VSC 结构同时调节串联和并联通道。其实 EMT 模型需要明确直流侧、换流器控制和保护逻辑。
- **混合 SVC-VSC 拓扑**：Le-Huy (2023) 在 Hydro-Québec La Verendrye 735-kV 变电站中验证了混合 SVC-VSC 拓扑（2 个 VSC 支路 + 2 个 TSC 支路），VSC 支路最大贡献 70 Mvar/支路，TSC 支路 95 Mvar/支路，总容量维持原 SVC 的 +330/-110 Mvar，VSC 电流上限 1.45 kA。
- **模型层级**：开关级模型适合谐波、触发和保护细节；[[average-value-model]] 适合系统级动态；正序或潮流模型只适合较慢的规划和运行分析。

## 形式化表达

FACTS 在网络方程中的作用可抽象为受控并联注入或串联阻抗调节：

$$
i_{\mathrm{sh}} = B_c(x_c,u_c)v,\qquad
v_{\mathrm{line}} = Z_{\mathrm{line}}(x_c,u_c)i_{\mathrm{line}}
$$

其中 $x_c$ 是装置控制状态，$u_c$ 是电压、功率或阻抗指令，$B_c$ 表示并联补偿等效电纳，$Z_{\mathrm{line}}$ 表示线路等效串联阻抗。SVC、STATCOM 和 TCSC 的主要差异，不是"是否提升系统能力"的口号，而是控制变量、阀/换流器实现、限幅保护和频带边界不同。

对于含 VSC 的混合 SVC 拓扑，Pejovic 等效开关模型采用等效 LC 支路模拟电力电子器件的导通与关断：

$$
R_{eq} = \frac{2L}{\Delta T} = R + \frac{\Delta T}{2C}
$$

其中 $\Delta T$ 为小步长仿真步长，$L$ 和 $C$ 为等效电感电容参数，需根据步长和阻尼因子精密配置（Le-Huy 2023）。

## 量化性能边界

FACTS 在 EMT 仿真中已有可核验的量化结果：

- **Le-Huy (2023)**：混合 SVC-VSC 拓扑的 HIL 测试中，常规大步长（32.5521 μs，即 512 点/周波）与小步长（3 μs）波形高度一致，动态响应偏差 < 1%。采用双路 Intel Scalable Gold 6244 处理器时，无需 FPGA 加速即可在 32.5521 μs 步长下稳定运行完整控制保护副本。小步长 EMT 仿真受硬件限制，单任务最多 30 个单相节点，仅允许 6 个标准 Ron/Roff 开关。
- **Sultan (1998)**：提出 EMT-TSP 混合仿真方法，在含 HVDC 和 FACTS 的系统中验证了电磁暂态和机电暂态的联合求解，为 FACTS-HVDC 协调控制的混合仿真奠定基础。

## 适用边界与失败模式

- FACTS 的"快速控制"不能替代容量约束、限流器、热限制、谐波滤波和保护动作验证。
- 只用稳态潮流或正序模型评估 FACTS，可能遗漏触发延迟、阀组暂态、谐波放大和控制相互作用。
- 串联补偿改变线路等效阻抗时，应检查 [[frequency-domain-analysis]]、[[harmonic-analysis]] 和时域 EMT 中的振荡风险。
- 多 FACTS 或 FACTS-HVDC 协调控制结论应绑定具体控制器、通信延迟和运行点，不能从单装置算例外推。
- Le-Huy (2023) 的结论仅基于 Hydro-Québec La Verendrye 变电站的特定拓扑，不自动覆盖其他 SVC 拓扑或控制保护版本。

## 代表性来源

- [[hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model]]：SVC 动态相量或混合仿真的模型层级讨论。
- [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems]]：HVDC 与 FACTS 联合暂态分析的来源入口。
- [[hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation]]：HIL 场景下 SVC/VSC 大步长建模方法选择（< 1% 偏差，无需 FPGA）。
- [[mmc-upfc电磁-机电混合仿真技术研究]]：UPFC 混合仿真应用。

## 与相关页面的关系

- [[statcom-model]]、[[svc-model]]、[[tcsc-model]] 是设备模型页；本页只做主题综合和边界说明。
- [[vsc-hvdc]] 同样使用 VSC 技术，但目标是交直流能量转换；FACTS 主要服务于交流输电参数调节。
- [[renewable-energy-integration]] 涉及新能源电压支撑和无功控制；FACTS 是可能的支撑装置之一。
- [[average-value-model]]：FACTS 系统级研究可使用的等效模型方法。

## 开放问题

- 如何在规划模型、平均值模型和开关级 EMT 之间保持 FACTS 控制参数一致。
- 如何报告 FACTS 控制对振荡阻尼的贡献，同时避免把单个算例结果写成通用能力。
- 如何在多 FACTS、HVDC 和逆变器型电源共存时识别控制交互的主导机制。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems|Combined transient and dynamic analysis of HVDC and FACTS sy]] | 2004 |