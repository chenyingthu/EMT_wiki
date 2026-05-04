---
title: "地回路阻抗 (Earth Return Impedance)"
type: method
tags: [earth-return, impedance, carson, pollaczek, transmission-line]
created: "2026-05-02"
---

# 地回路阻抗 (Earth Return Impedance)

## 定义与边界

地回路阻抗描述电流经大地或土壤介质返回时，对线路单位长度串联阻抗矩阵产生的频率相关贡献。它常用于架空线路零序参数、地下电缆回流路径、接地系统耦合、混合架空-电缆走廊和宽频 EMT 暂态建模。

本页关注大地返回路径如何进入 [[distributed-parameter-line]] 和 [[frequency-dependent-line-model]]。它不等同于接地网接地电阻，也不应替代 [[grounding-system-model]]。

## EMT 中的作用

在 EMT 中，地回路阻抗影响以下问题：

- 零序和不平衡故障下的线路参数。
- 雷电、开关和快速暂态中高频回流路径。
- 地下电缆、护套、铠装和土壤之间的耦合。
- 多层土壤或高电阻率土壤下的宽频参数计算。
- 平行线路或架空-地下混合系统的感应耦合。

如果在高频或不平衡场景中简单采用工频近似，可能把传播损耗、相位延迟和耦合强度估错。

## 核心机制

单位长度串联阻抗矩阵可概念性写成：

$$Z'(\omega)=Z_\text{int}(\omega)+Z_\text{ext}(\omega)+Z_\text{earth}(\omega)$$

其中 $Z_\text{int}$ 描述导体内部集肤效应，$Z_\text{ext}$ 描述外部几何磁场，$Z_\text{earth}$ 描述大地返回路径。均匀半无限大地假设下，Carson/Pollaczek 类公式通过复积分刻画导体与镜像/扩散场之间的关系；多层土壤模型则通过层间边界条件修改积分核。

在多导体系统中，地回路项既出现在自阻抗，也出现在互阻抗：

$$Z_{ij}'(\omega)=R_{ij}(\omega)+j\omega L_{ij}(\omega)+Z_{\text{earth},ij}(\omega)$$

因此它与 [[mutual-impedance]]、[[phase-domain-modeling]] 和 [[modal-transformation]] 都直接相关。

## 分类与变体

| 方法族 | 典型假设 | 适合用途 | 注意事项 |
|--------|----------|----------|----------|
| Carson 类公式 | 架空导体、均匀半无限大地 | 工频和低频线路参数 | 高频、分层土壤需谨慎 |
| Pollaczek/Wedepohl 类公式 | 地下导体或电缆回流 | 电缆和埋地导体参数 | 数值积分和介质参数关键 |
| 多层土壤解析/递归公式 | 水平分层介质 | 地层影响、混合导体拓扑 | 不覆盖任意三维地质结构 |
| MoM-SO/场积分方法 | 导体表面电流和多介质格林函数 | 复杂线路/电缆参数工具 | 工具实现和频带需核查 |

## 适用边界与失败模式

- 经典公式多依赖准 TEM、无限长、平行导体和均匀/分层大地假设。有限长接地体、局部电缆附件和三维地质异常可能超出适用范围。
- 土壤电阻率、介电常数和分层厚度往往不易精确获得，参数不确定性会直接进入 EMT 结果。
- 高频下位移电流、接地返回导纳和护套/铠装细节可能不能忽略。
- 不能把某篇论文中的公式退化关系写成工程误差保证；实际误差需要算例或测量对比。

## 代表性来源

- [[earth-return-impedance-of-overhead-and-underground-conductors-considering-earth-stratification-13&14]]：给出多层大地中架空和地下导体自/互阻抗的统一理论框架；该 source 明确提醒 Part I 主要是理论推导，不能捏造 FEM 误差结论。
- [[assessment-of-the-transmission-line-theory-in-the-modeling-of-multiconductor-und]]：用全波 FDTD 评估地下电缆 TLT，适合支撑“接地返回导纳/阻抗会影响快速暂态”的边界性表述。
- [[a-new-tool-for-calculation-of-line-and-cable-parameters]]：说明现代线路/电缆参数工具把大地返回、邻近效应和并联导纳放在统一参数计算框架中。
- [[electromagnetic-transient-modeling-of-grounding-electrodes-buried-in-frequency-d]]：可作为接地电极频变土壤建模的相关入口，具体结论需回到原文。

## 与相关页面的关系

- [[mutual-impedance]] 使用地回路项解释导体间耦合。
- [[frequency-dependent-soil]] 和 [[frequency-dependent-soil-model]] 描述土壤参数随频率变化。
- [[cable-model]]、[[grounding-system-model]] 和 [[transmission-line-model]] 是主要应用对象。
- [[vector-fitting]] 可把频域地回路阻抗转为时域可实现模型。
- [[frequency-scan]] 可用于检查等效参数对系统频响的影响。

## 修订与证据使用注意事项

后续不要直接写固定“适用频率范围”或“误差小于某百分比”，除非已核对原始论文、标准或工具手册。涉及 Carson、Pollaczek、Sunde、Wedepohl、Nakagawa 等公式时，应说明它们的假设，而不是把名字作为精度背书。
