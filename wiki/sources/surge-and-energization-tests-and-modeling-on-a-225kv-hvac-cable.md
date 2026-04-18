---
title: "Surge and energization tests and modeling on a 225kV HVAC cable"
type: source
authors: ['Isabel Lafaia']
year: 2018
journal: "Electric Power Systems Research, 160 (2018) 273-281. doi:10.1016/j.epsr.2018.03.003"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/37/j.epsr.2018.03.003.pdf.pdf"]
---

# Surge and energization tests and modeling on a 225kV HVAC cable

**作者**: Isabel Lafaia
**年份**: 2018
**来源**: `37/j.epsr.2018.03.003.pdf.pdf`

## 摘要

1. Introduction we can excite each propagation mode separately and observe the respective cable responses, which is useful for model validation. In Projects of new cable installations have taken place worldwide the energization test, the full 64 km long cable was connected to in the last few year...

## 核心贡献

- 提供了225kV长距离XLPE地下电缆（64km，交叉互联护套）的浪涌与投切实验现场测试数据
- 在EMTP中对比了详细分段模型与全长均匀等效简化模型的仿真表现
- 验证了简化电缆模型在特定应用场景下的有效性与工程实用性

## 使用的方法

- [[现场浪涌测试-surge-tests|现场浪涌测试（Surge tests）]]
- [[现场投切测试-energization-tests|现场投切测试（Energization tests）]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]
- [[详细分段建模与均匀等效简化建模对比分析|详细分段建模与均匀等效简化建模对比分析]]

## 涉及的模型

- [[225-kv-xlpe地下交流电缆-含交叉互联护套|225 kV XLPE地下交流电缆（含交叉互联护套）]]
- [[电网变压器|电网变压器]]
- [[无功补偿装置|无功补偿装置]]
- [[emtp电缆详细模型-各小段独立建模|EMTP电缆详细模型（各小段独立建模）]]
- [[emtp电缆简化模型-全长均匀等效|EMTP电缆简化模型（全长均匀等效）]]

## 相关主题

- [[电磁暂态-emt|电磁暂态（EMT）]]
- [[地下电缆建模与测试|地下电缆建模与测试]]
- [[电缆投切与浪涌过电压|电缆投切与浪涌过电压]]
- [[交叉互联接地系统|交叉互联接地系统]]
- [[emtp仿真验证|EMTP仿真验证]]

## 主要发现

- 浪涌测试能有效激发不同的传播模式并观测电缆响应，为模型验证提供了有效手段
- 投切测试的瞬态测量结果清晰反映了系统中变压器和无功补偿装置对暂态过程的影响
- 当仿真仅关注芯线导体的电压和电流时，使用全长均匀等效的简化电缆模型不会降低仿真精度

## 方法细节

### 方法概述

本文采用现场实验与电磁暂态仿真相结合的方法，对225kV、64km长XLPE高压交流电缆系统进行浪涌测试和投切测试。浪涌测试在电缆建设期间进行，通过2kV、1.2/50μs标准浪涌波分别施加于1080m minor section和3952m major section，以激发不同传播模式（同轴模式、护套间模式、大地返回模式）。投切测试在电缆投入运行前进行，测量从两端分别 energizing 全长电缆时的暂态电压和电流。在EMTP中建立了两种电缆模型进行对比验证：详细分段模型（对每个minor section单独建模，考虑交叉互联）和全长均匀等效简化模型（homogeneous equivalent），以评估简化模型在芯线暂态量计算中的精度。

### 数学公式


**公式1**: $$$Z_S = \frac{1}{2\pi}\sqrt{\frac{\mu_0}{\varepsilon_r \varepsilon_0}} \ln\frac{r_3}{r_2}$$$

*同轴模式(cable-coaxial mode)浪涌阻抗计算公式，其中r3为金属护套内半径，r2为芯线外半径（含半导体屏蔽层），用于计算芯线-护套间的特性阻抗*


**公式2**: $$$v = \frac{2L}{\Delta t}$$$

*基于反射波时间差计算 propagation velocity，L为电缆长度，Δt为相邻同极性峰值间的时间差*


**公式3**: $$$v_{coaxial} = \frac{c}{\sqrt{\varepsilon_{r1}}}$$$

*理论同轴模式传播速度计算公式，c为光速，εr1为XLPE绝缘层相对介电常数（取2.5），理论计算值约为167 m/μs*


### 算法步骤

1. 现场浪涌测试准备：在minor section（1080m）两端安装接地棒，测量接地电阻（偏远地区30Ω，变电站5Ω），配置2kV、1.2/50μs浪涌发生器（输出阻抗2Ω）

2. 多模式浪涌激励：依次实施芯线对地（护套开路/接地）、芯线对护套、两相护套间、三相护套间、护套对地（单相/两相/三相）等测试配置，以分离不同传播模式

3. 高速数据采集：记录发送端和接收端的电压、电流波形，采样率足以分辨μs级暂态过程，捕捉反射波峰值时间差

4. 传播参数计算：基于测量波形计算传播速度（v=2L/Δt）和浪涌阻抗（Z=V/I），与理论公式计算值对比验证

5. 全长电缆投切测试：从Boutre和Trans两端分别 energize 64km电缆，测量发送端暂态电流和电压，观察变压器和无功补偿装置的影响

6. EMTP详细模型建立：建立17个major section的详细模型，每个minor section单独建模，准确模拟交叉互联护套（cross-bonding）连接方式和终端避雷器

7. EMTP简化模型建立：建立全长均匀等效模型（homogeneous equivalent），不考虑分段细节，将64km电缆视为连续均匀介质

8. 仿真-实测对比验证：对比两种模型计算的芯线电压、电流与现场投切测试测量值，评估简化模型在仅关注芯线导体暂态量时的精度损失


### 关键参数

- **cable_length_total**: 64 km

- **cable_sections_major**: 17 major sections with cross-bonding

- **minor_section_length**: 1080 m

- **major_section_length**: 3952 m

- **surge_voltage**: 2 kV (1.2/50 μs)

- **generator_impedance**: 2 Ω

- **grounding_resistance_remote**: 30 Ω

- **grounding_resistance_substation**: 5 Ω

- **core_conductor_rho**: 1.76×10⁻⁸ Ω·m

- **sheath_rho**: 2.84×10⁻⁸ Ω·m

- **insulation_permittivity**: εr1=2.5, tanδ=0.0008

- **outer_insulation_permittivity**: εr2=2.5, tanδ=0.001

- **cable_sizes**: 2000 mm² and 2500 mm²

- **hdpe_tube_diameter**: D1=198.5 mm, D2=225 mm



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Core-to-sheath surge impedance verification | minor section芯线对护套浪涌测试测得初始峰值电压1752V、电流68.74A，计算得浪涌阻抗25Ω，与理论公式计算的同轴模式浪涌阻抗22.9Ω基本吻合，误差约9.2% | 实测值25Ω vs 理论值22.9Ω |

| Coaxial mode propagation velocity | 通过芯线对地测试波形第二、三峰值时间差12.6μs计算得传播速度171 m/μs；通过芯线对护套测试振荡周期27.4μs计算得158 m/μs，均接近理论同轴模式速度167 m/μs | 实测158-171 m/μs vs 理论167 m/μs，偏差<6% |

| Inter-sheath mode velocity (2-phase vs 3-phase) | 两相护套间测试测得平均峰峰时间42.1μs，对应速度102.6 m/μs；三相护套间测试测得振荡周期38μs，对应速度114 m/μs，三相模式因并联回路电感较低而速度较高 | 两相102.6 m/μs vs 三相114 m/μs，差异11% |

| Earth-return mode attenuation | 护套对地测试显示大地返回模式存在高衰减，单相/两相/三相护套对地测试的接收端峰值电压分别为1149V、750V、623V，电流波形呈现强衰减特性，传播速度约70 m/μs（基于225μs反射时间计算） | 速度70 m/μs显著低于同轴模式167 m/μs |

| Energization test simulation accuracy | 64km全长电缆投切测试中，采用全长均匀等效简化模型与详细分段模型对比，两种模型计算的芯线电压和电流结果一致，简化模型未降低仅关注芯线导体暂态量的仿真精度 | 简化模型 vs 详细模型：芯线暂态量误差可忽略 |



## 量化发现

- 同轴模式传播速度实测值：171 m/μs（基于12.6μs时间差）和158 m/μs（基于27.4μs周期），与理论值167 m/μs偏差在5%以内
- 同轴模式浪涌阻抗实测值25Ω，理论计算值22.9Ω，误差9.2%
- 两相护套间模式传播速度：102.6 m/μs（基于42.1μs周期）
- 三相护套间模式传播速度：114 m/μs（基于38μs周期），比两相模式快11%
- 大地返回模式传播速度：70 m/μs（基于225μs反射时间和1080m长度计算）
- 护套对地测试峰值电压：单相激励1149V、两相激励750V、三相激励623V，呈现多导体分流效应
- 接地电阻：电缆终端偏远区域30Ω，变电站区域5Ω
- 电缆几何参数：2000mm²电缆芯线外半径28.4mm（修正值），护套内半径56.4mm；2500mm²电缆芯线外半径31.9mm，护套内半径59.9mm
- 投切测试表明系统变压器和无功补偿装置对暂态电流波形有显著影响，在仿真中必须准确建模
- 全长均匀等效简化模型在计算芯线导体电压和电流时，与详细分段模型结果等效，计算误差可忽略


## 关键公式

### 同轴模式浪涌阻抗公式

$$$Z_S = \frac{1}{2\pi}\sqrt{\frac{\mu_0}{\varepsilon_r \varepsilon_0}} \ln\frac{r_3}{r_2}$$$

*用于计算芯线与金属护套之间的特性阻抗，验证芯线对护套浪涌测试的测量结果（理论值22.9Ω）*

### 传播速度计算公式

$$$v = \frac{2L}{\Delta t}$$$

*基于现场测量的反射波时间差计算实际传播速度，用于区分同轴模式（~167 m/μs）、护套间模式（102-114 m/μs）和大地返回模式（~70 m/μs）*



## 验证详情

- **验证方式**: 现场实测数据与EMTP仿真结果对比验证，包括浪涌测试（surge tests）和投切测试（energization tests）两种场景
- **测试系统**: 225 kV XLPE地下交流电缆系统，全长64km，17个major sections，交叉互联护套，两端连接变电站并装有无功补偿装置
- **仿真工具**: EMTP（Electromagnetic Transients Program），建立详细分段模型（separate model for each minor section）和全长均匀等效简化模型（homogeneous equivalent）
- **验证结果**: 浪涌测试验证了不同传播模式的传播速度和浪涌阻抗，实测同轴模式速度158-171 m/μs（理论167 m/μs），浪涌阻抗25Ω（理论22.9Ω）。投切测试表明当仅关注芯线导体暂态量时，全长均匀等效简化模型与详细分段模型具有同等精度，为长电缆EMT仿真提供了模型简化依据。
