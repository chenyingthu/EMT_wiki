---
title: "雷电过电压 (Lightning Overvoltage)"
type: topic
tags: [lightning, surge, overvoltage, arrester, grounding, insulation-coordination]
created: "2026-05-01"
---

# 雷电过电压 (Lightning Overvoltage)


```mermaid
graph TD
    subgraph S0[雷电过电压 (Lightning Overvoltage)]
        N0[定义与边界]
        N1[EMT 中的作用]
        N2[主要分支与机制]
        N3[适用边界与失败模式]
        N4[代表性来源]
        N5[与相关页面的关系]
    end
    N0 --> N1
    N1 --> N2
    N2 --> N3
    N3 --> N4
    N4 --> N5
```


## 定义与边界

雷电过电压（Lightning Overvoltage）是雷电流、雷电电磁场、线路行波、杆塔和接地系统共同作用下产生的快速过电压。它包括直击导线、击中杆塔或避雷线后的反击、附近雷击造成的感应电压，以及从线路或电缆入口传播到设备端子的侵入波。

本页讨论雷电造成的 EMT 过电压。它不同于一般 [[switching-transient]]，后者由断路器或隔离开关操作触发；也不同于 [[grounding-lightning-overvoltage]]，后者更聚焦接地系统和地电位升。没有绑定雷电流、线路几何、土壤、接地、端接和保护装置时，不应给出确定的峰值或保护裕度。

## EMT 中的作用

雷电过电压研究把外部电磁扰动转换为 EMT 网络中的电流源、电压源、行波边界或端口激励，用于绝缘配合、避雷器能量校核、接地系统设计和保护配置。EMT 的价值在于保留波前、反射、折射、频变损耗、非线性避雷器动作和设备端子瞬时应力。

常见输出包括端口电压 $v(t)$、雷电流 $i_L(t)$、避雷器电流和能量 $W=\int v_a(t)i_a(t)\,dt$、接地电位升以及绝缘闪络判据。若只关心长期故障率或雷暴日统计，需要概率模型和运维数据补充，不能仅靠单次 EMT 波形外推。

## 主要分支与机制

- 雷电流源：工程算例常用双指数、Heidler 或分段波形表示 $i_L(t)$。例如双指数形式可写为 $i_L(t)=I_0(e^{-\alpha t}-e^{-\beta t})$，其中 $I_0,\alpha,\beta$ 必须由标准波形或来源论文给定。
- 线路耦合：直击雷可近似为电流注入和行波传播；感应雷需要把外部场沿线积分后等效为端口源或分布源。
- 频变传播：雷电波包含宽频分量，线路、土壤和接地响应通常依赖 [[frequency-dependent-soil]]、[[wideband-modeling]] 和 [[transmission-line-theory]]。
- 接地和杆塔：杆塔阻抗、塔脚接地、地电位升和土壤电离会改变反击和设备端电压。
- 保护装置：[[surge-arrester-model]] 通过非线性伏安关系限制残压，但能量吸收、老化和配合裕度必须按具体型号和工况校核。

一个端口级保守表达为

$$
v_{\mathrm{term}}(t)=v^{+}(t)+\Gamma v^{-}(t)+z_g(t)*i_L(t)-v_a(t),
$$

其中 $v^{+}$ 与 $v^{-}$ 表示入射和反射波，$\Gamma$ 为端接反射系数，$z_g(t)$ 为接地或杆塔等效冲激响应，$v_a(t)$ 为避雷器限制后的电压贡献。该式是关系示意，不替代具体线路模型。

## 适用边界与失败模式

- 雷电流幅值、波头、波尾和通道模型不能用单一“典型值”代替；标准冲击、实测波形和统计雷电流对应不同问题。
- 感应雷模型通常依赖雷击距离、通道高度、土壤参数和线路走向；这些条件改变时，端口源需要重新计算。
- 把土壤看作常数电阻率或把接地系统等效为低频电阻，可能不适合波头很陡或接地结构宽频响应敏感的算例。
- 避雷器模型若缺少伏安曲线、能量容量和热恢复参数，只能用于定性限压，不能用于寿命或失效结论。
- 单篇论文中对某个网络、土壤或雷击事件的误差和效率结果，不应写成所有雷电过电压计算的通用精度。

## 代表性来源

- [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines]] 讨论架空-电缆混合线路中扩展传输线、频变土壤和频变接地对护套雷电过电压的影响；其结论应限于原文混合线路和接地设置。
- [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-]] 把雷电场耦合等效为端口独立电流源，并在 ATP/JMarti 频变线路框架中处理大规模配电网感应电压。
- [[an-electromagnetic-model-for-the-calculation-of-tower-surge-impedance-based-on-t]] 可作为杆塔浪涌阻抗电磁建模的来源入口。
- [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o]] 支撑土壤频变特性会影响线路地回路参数和雷电暂态响应，但不等同于所有接地网实测验证。
- [[a-waveform-dependence-lightning-impulse-corona-model-in-pscademtdc-for-investiga]] 可作为雷电冲击电晕和波形相关传播畸变的来源入口。

## 与相关页面的关系

- [[electromagnetic-transient]] 给出总体现象边界；本页聚焦雷电激励。
- [[grounding-lightning-overvoltage]] 更适合讨论地网、塔脚和地电位升；本页保留线路和设备端过电压视角。
- [[lightning-transient-analysis]] 是方法入口，说明如何组织雷电暂态计算。
- [[frequency-dependent-soil]]、[[grounding-system-modeling]] 和 [[earth-return-impedance]] 支撑土壤与接地参数。
- [[insulation-coordination]] 使用本页结果，但绝缘配合还需要标准、统计裕度和设备耐受数据。

## 开放问题

- 如何把雷电定位、现场录波和 EMT 模型参数校核连接起来。
- 如何在宽频接地、土壤电离、电晕和避雷器老化之间建立可验证的联合模型。
- 如何为配电网和新能源场站建立既可计算大范围网络又保留关键波前的模型降阶策略。
- 如何报告雷电概率、单次波形和设备绝缘风险之间的证据边界。
