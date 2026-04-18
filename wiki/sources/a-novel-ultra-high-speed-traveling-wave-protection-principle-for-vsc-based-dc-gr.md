---
title: "A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-based DC Grids"
type: source
authors: ['未知']
year: 2019
journal: "IEEE Access;2019;7; ;10.1109/ACCESS.2019.2936276"
tags: ['vsc']
created: "2026-04-13"
sources: ["EMT_Doc/03/ACCESS.2019.2936276.pdf.pdf"]
---

# A Novel Ultra-High-Speed Traveling-Wave Protection Principle for VSC-based DC Grids

**作者**: 
**年份**: 2019
**来源**: `03/ACCESS.2019.2936276.pdf.pdf`

## 摘要

Protection of direct current (DC) transmission lines is one of the key difﬁculties to be urgently solved in the construction of the future voltage-sourced converter (VSC)-based DC grids. In this paper, a novel ultra-high-speed traveling-wave (TW) protection principle for DC transmission lines is proposed which is based on characteristics of modulus voltage TWs. First, the absolute value of the change in amplitude of the 1-mode voltage TW is used to construct the protection starting-up element. Then, the dyadic wavelet transform is utilized to extract the wavelet-transform modulus maxima (WTMM) of 1-mode and 0-mode initial reverse voltage TWs separately, which are used for fault section identiﬁcation and selection of fault line successively. A four-terminal annular VSC-based DC grid electro

## 核心贡献


- 提出基于模电压行波特征的超高速保护原理，利用一模电压幅值变化构建启动元件
- 采用二进小波变换提取一零模反向行波模极大值，实现故障区段精准识别与选线


## 使用的方法


- [[相模变换|相模变换]]
- [[二进小波变换|二进小波变换]]
- [[小波变换模极大值提取|小波变换模极大值提取]]
- [[行波保护原理|行波保护原理]]
- [[电磁暂态仿真|电磁暂态仿真]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[mmc-model|MMC]]
- [[架空输电线路|架空输电线路]]
- [[直流限流电抗器|直流限流电抗器]]
- [[直流断路器|直流断路器]]


## 相关主题


- [[直流线路保护|直流线路保护]]
- [[行波保护|行波保护]]
- [[vsc-model|VSC]]
- [[故障区段识别|故障区段识别]]
- [[超高速保护|超高速保护]]


## 主要发现


- 仿真验证表明该保护原理在不同故障条件下均具备毫秒级动作速度与高可靠性
- 模极大值特征可有效区分区内区外故障，对高阻故障及噪声干扰具有强鲁棒性



## 方法细节

### 方法概述

本文提出一种基于模电压行波特征的超高速直流线路非单元保护原理。首先，利用相模变换矩阵解耦双极直流线路的耦合电压电流，提取1模（线模）和0模（地模）电压行波。保护启动元件基于一模电压行波幅值变化绝对值构建，实现故障快速检测。随后，采用二进小波变换对初始反向电压行波进行多分辨率分析，提取小波变换模极大值（WTMM）。利用1模初始反向行波WTMM的幅值差异区分区内与区外故障，实现故障区段识别；利用0模初始反向行波WTMM的极性特征（负极性为正极接地、正极性为负极接地、接近零为极间短路）实现故障极选择。该方法无需对端通信，仅依赖本地高频采样数据，具备毫秒级动作速度与强抗干扰能力。

### 数学公式


**公式1**: $$$\Delta u_1(k) = |u_1(k) - u_1(k-1)| > TH_1$$$

*保护启动判据，计算当前时刻与上一时刻1模电压行波幅值变化绝对值，超过阈值TH1即触发启动。*


**公式2**: $$$f = \begin{cases} \text{internal fault}, & WTMM_{u1r} > TH_2 \\ \text{external fault}, & \text{others} \end{cases}$$$

*故障区段识别判据，利用1模初始反向行波WTMM幅值是否超过阈值TH2区分区内与区外故障。*


**公式3**: $$$f = \begin{cases} \text{positive pole-to-ground}, & WTMM_{u0r} < -TH_3 \\ \text{negative pole-to-ground}, & WTMM_{u0r} > TH_3 \\ \text{pole-to-pole}, & \text{others} \end{cases}$$$

*故障极选择判据，根据0模初始反向行波首个WTMM的极性特征判定具体故障类型。*


**公式4**: $$$S = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1 \end{bmatrix}$$$

*相模变换矩阵，用于将双极耦合的相电压/电流解耦为独立的0模和1模分量。*


### 算法步骤

1. 以500 kHz采样频率同步采集双极直流线路两端电压与电流数据，实时计算1模电压行波。

2. 计算1模电压行波幅值变化绝对值$\Delta u_1(k)$，若连续3个采样点均超过启动阈值$TH_1$（0.01 p.u.），则判定故障发生并触发保护启动。

3. 启动后截取包含启动前64个采样点与启动后192个采样点的256点数据窗（总时长0.512 ms），利用相模变换矩阵计算1模与0模反向电压行波。

4. 对1模初始反向行波进行二进小波变换（尺度$2^4$），提取小波变换模极大值$WTMM_{u1r}$。若$WTMM_{u1r} > TH_2$，判定为区内故障并进入下一步；否则判定为区外故障，闭锁保护出口。

5. 对0模初始反向行波进行二进小波变换，提取首个模极大值$WTMM_{u0r}$。根据其极性判定故障极：负值为正极接地，正值为负极接地，接近零为极间短路。

6. 输出故障区段与故障极信息，向直流断路器（DB）发送跳闸指令，完成超高速主保护动作。


### 关键参数

- **采样频率**: 500 kHz

- **启动阈值_TH1**: 0.01 p.u. (额定直流电压)

- **数据窗长度**: 256点 (启动前64点 + 启动后192点)

- **小波变换尺度**: $2^4$

- **直流限流电抗器**: 150 mH

- **噪声测试水平**: 20 dB 高斯白噪声

- **测试线路**: OHL24 (张北±500 kV四端环形电网)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 区内高阻接地故障 | 距ZB站205.5 km处发生400 Ω正极接地故障，1模初始反向行波WTMM幅值达128.9，0模WTMM为负极性，正确识别区内正极接地故障。 | 特征幅值远超阈值，较传统基于稳态量的保护方案动作时间缩短至0.512 ms以内，速动性提升2个数量级。 |

| 区外金属性故障 | 在DB24与L24之间发生正极金属性接地故障，1模初始反向行波WTMM绝对值均小于0.5，保护可靠闭锁未误动。 | 区内外WTMM幅值差异超250倍，识别裕度显著优于传统行波幅值比较法，抗区外故障干扰能力极强。 |

| 不同故障极性与过渡电阻 | 在100 km处分别设置正极接地、负极接地及极间短路故障（过渡电阻最高400 Ω），0模WTMM极性始终保持负、正、近零特征，选极准确率100%。 | 在高阻条件下极性特征无翻转，较依赖幅值阈值的传统选线方法鲁棒性提升显著。 |

| 强噪声干扰工况 | 在1模与0模反向行波信号中叠加20 dB高斯白噪声，区外故障WTMM仍<0.5，区内故障WTMM仍显著大于阈值，无误动或拒动。 | 二进小波多分辨率分析有效滤除高频噪声，抗噪性能较传统傅里叶变换或简单差分法提升明显。 |



## 量化发现

- 保护动作数据窗仅0.512 ms（256点@500kHz），实现毫秒级超高速动作。
- 区内故障1模WTMM（128.9）与区外故障（<0.5）幅值差异超250倍，区段识别裕度极大。
- 在400 Ω高过渡电阻及线路末端故障条件下，0模WTMM极性特征保持稳定，故障极选择准确率100%。
- 在20 dB强高斯白噪声干扰下，启动元件与WTMM特征提取仍保持高可靠性，未发生误动或拒动。
- 连续3点启动判据有效滤除瞬时扰动，启动阈值0.01 p.u.在正常运行时$\Delta u_1(k)$接近0，启动可靠性达100%。


## 关键公式

### 保护启动判据

$$$\Delta u_1(k) = |u_1(k) - u_1(k-1)| > TH_1$$$

*用于实时监测1模电压行波突变，当连续3个采样点超过0.01 p.u.时触发保护启动，确保速动性与抗扰动能力。*

### 故障区段识别判据

$$$WTMM_{u1r} > TH_2$$$

*利用区内故障时1模初始反向行波WTMM幅值显著大于区外故障的特征，实现非单元式区内/区外故障精准判别。*

### 正极接地1模初始行波幅值解析式

$$$u_1 = -\frac{\sqrt{2}U_{dc}Z_1}{Z_0+Z_1+4R_f}$$$

*推导自故障附加网络与相模变换，揭示1模初始行波幅值与过渡电阻$R_f$及模波阻抗的关系，为WTMM特征提取提供理论依据。*



## 验证详情

- **验证方式**: 电磁暂态仿真验证
- **测试系统**: 张北±500 kV四端环形VSC直流电网示范工程模型（含KB、ZB、BJ、FN四站，架空线路，150 mH直流限流电抗器）
- **仿真工具**: PSCAD/EMTDC
- **验证结果**: 在不同故障类型（正极/负极接地、极间短路）、过渡电阻（0~400 Ω）、故障距离及20 dB噪声干扰下，保护原理均能在0.512 ms内准确启动、识别区段并选择故障极。仿真结果表明该方案具备优异的速动性、可靠性与鲁棒性，可作为VSC直流电网的超高速主保护。
