---
title: "双闭环PI控制器 (Dual-Loop PI Controller)"
type: method
tags: [dual-loop, pi-controller, cascade, current-control, voltage-control]
created: "2026-05-02"
---

# 双闭环PI控制器 (Dual-Loop PI Controller)

## 概述

双闭环 PI 控制器（Dual-Loop PI Controller）是电力电子变流器中常见的级联控制结构：外环根据功率、电压、直流母线或交流电压目标生成电流参考，内环跟踪电流并输出调制电压或等效控制量。它常用于 [[models/vsc-model.md]]、[[models/mmc-model.md]]、并网逆变器、储能变流器和部分电机驱动模型。

该方法页讨论级联 PI 结构本身，不把它写成所有变流器的“标准最优控制”。双闭环 PI 主要属于 VSC/逆变器控制范畴；LCC-HVDC 的晶闸管触发角和关断角控制应放在 [[methods/thyristor-control.md]] 和 [[methods/extinction-angle-calculation.md]] 中。

## 控制接口

| 环节 | 常见输入 | 常见输出 | 说明 |
|------|----------|----------|------|
| 外环 | 直流电压、有功/无功功率、交流电压或频率附加信号 | $i_d^*$、$i_q^*$ 或三相电流参考 | 通常比内环慢，受限幅和模式切换影响 |
| 内环 | 电流参考与测量电流 | $v_d^*$、$v_q^*$ 或调制参考 | 与滤波电感、电网电压前馈和解耦项相关 |
| 同步 | PLL 相位或内部振荡器相位 | dq 变换角 $\theta$ | 跟网型 VSC 依赖 PLL，构网型控制可能不同 |
| 执行 | PWM/平均值模型/受控源接口 | 开关脉冲或等效电压源 | 具体实现决定 EMT 细节 |

在同步旋转坐标系下，简单 L 滤波并网模型常写成：

$$L\frac{di_d}{dt}=v_d-v_{gd}-Ri_d+\omega L i_q$$

$$L\frac{di_q}{dt}=v_q-v_{gq}-Ri_q-\omega L i_d$$

电流内环 PI 输出可与电网电压前馈和交叉耦合补偿组合。上述方程说明解耦项的来源，但其符号取决于 dq 变换约定；页面不把某一符号约定外推为全站标准。

## 设计步骤

1. 明确坐标系和同步方式：PLL、虚拟角频率或外部相位。
2. 写出被控对象：L、LCL、变压器漏抗、MMC 等效桥臂或平均值模型。
3. 先设计电流内环，确定采样、延迟、限幅和前馈项。
4. 再设计外环，保证其动态要求与内环能力、容量限制和模式切换相容。
5. 加入抗饱和、限流、无扰切换和故障穿越逻辑。
6. 在 EMT 中用阶跃、故障、电压跌落、弱网和控制模式切换验证。

“内环快、外环慢”是级联控制的常见设计原则，但具体带宽比、PI 参数和采样周期必须来自被控对象、控制器实现和验证来源。无来源时不应新增固定频率或固定比例。

## PI 与解耦项

PI 控制器本身可写为：

$$u(t)=K_p e(t)+K_i\int e(t)\,dt$$

离散实现需要说明积分方法、采样周期和限幅方式。若控制输出达到调制或电流限制，积分项继续累积可能导致恢复时过冲，因此 EMT 模型中应显式表示条件积分、反算抗饱和或其他抗饱和策略。

dq 解耦项只是基于线性化滤波器方程的前馈补偿。它在参数准确、采样延迟较小和运行点接近设计点时有助于减少轴间耦合；在弱电网、PLL 动态显著、LCL 谐振或限流模式下，解耦项可能不再等效于理想补偿。

## VSC-HVDC 与嵌入式 HVDC 证据

[[sources/dynamic-performance-of-embedded-hvdc-with-13&14.md]] 明确使用常规 dq 双环结构：外环根据直流电压、有功功率或交流电压目标生成 d/q 电流参考，内环跟踪电流并生成调制信号。论文还在有功参考层叠加频率相关补偿，用于嵌入式 HVDC 的功率振荡分担。该来源可支撑“双环 PI 作为 VSC-HVDC 控制骨架”的场景化表述，但其暂态稳定收益只适用于该 PSCAD/EMTDC 算例和同步交流网络内的嵌入式 HVDC 条件。

[[sources/characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir.md]] 将 MMC 内部动态、PLL、内外环、环流抑制和延时并入阻抗模型，用于解释高频振荡。它提醒双闭环 PI 不能脱离 PLL、延时和主电路动态单独评价稳定性。

## 适用边界

- 适用于跟网型 VSC、VSC-HVDC、并网逆变器、储能变流器和部分平均值模型控制接口。
- 不适用于 LCC 晶闸管换相控制；LCC 逆变器的关断角裕度不是 dq 电流内环问题。
- 在弱电网、低电压穿越、PLL 失锁、限流或控制模式切换时，线性 PI 小信号设计可能不足。
- LCL 滤波器、数字延迟、PWM 饱和和测量滤波会显著改变可实现带宽。
- 构网型控制可能使用电压源、虚拟同步或下垂控制结构，不能默认仍是 PLL 加双 PI 内外环。

## 代表性证据

| 来源 | 证据用途 | 边界 |
|------|----------|------|
| [[sources/dynamic-performance-of-embedded-hvdc-with-13&14.md]] | VSC-HVDC 常规 dq 双环 PI 结构及有功参考层附加控制 | 稳定性结论限于嵌入式 HVDC PSCAD 算例 |
| [[sources/characteristic-analysis-of-high-frequency-resonance-of-flexible-high-voltage-dir.md]] | MMC 高频阻抗模型中 PLL、内外环、环流控制和延时共同影响稳定性 | 面向 MMC-HVDC 高频振荡，不代表所有 VSC |
| [[models/pi-controller-model.md]] | PI 的连续、离散和抗饱和模型背景 | 该模型页含较多参数示例，引用时需核验来源 |

## 与相关页面的关系

- [[models/pi-controller-model.md]] 给出单个 PI 控制器模型。
- [[models/vector-control-model.md]] 和 [[methods/dq-transformation.md]] 给出坐标变换背景。
- [[models/pll-model.md]] 决定跟网型控制的同步参考。
- [[models/vsc-model.md]]、[[models/mmc-model.md]] 和 [[models/inverter-model.md]] 决定被控对象边界。

## 开放问题

双闭环 PI 页面仍需后续用具体来源补齐不同拓扑、滤波器、采样延迟和抗饱和实现的参数整定证据。当前页面只保留结构和证据边界，不新增未绑定来源的带宽、采样周期或响应时间。
