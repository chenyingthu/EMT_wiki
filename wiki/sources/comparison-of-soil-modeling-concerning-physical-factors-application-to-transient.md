---
title: "Comparison of soil modeling concerning physical factors: Application to transient analysis in wind turbines"
type: source
authors: ['Walter', 'Luiz', 'Manzi', 'de', 'Azevedo']
year: 2023
journal: "International Journal of Electrical Power and Energy Systems, 155 (2024) 109505. doi:10.1016/j.ijepes.2023.109505"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/10/Azevedo 等 - 2024 - Comparison of soil modeling concerning physical factors Application to transient analysis in wind t.pdf"]
---

# Comparison of soil modeling concerning physical factors: Application to transient analysis in wind turbines

**作者**: Walter, Luiz, Manzi 等
**年份**: 2023
**来源**: `10/Azevedo 等 - 2024 - Comparison of soil modeling concerning physical factors Application to transient analysis in wind t.pdf`

## 摘要

Electrical Power and Energy Systems 155 (2024) 109505 0142-0615/© 2023 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by- International Journal of Electrical Power and Energy Systems Comparison of soil modeling concerning physical factors: Application to Walter Luiz Manzi de Azevedo, Wagner Costa da Silva, Anderson Ricardo Justo de Araújo ∗,

## 核心贡献


- 对比六种土壤模型在频变、含水量及孔隙率下的电气特性，评估其对风机雷击暂态电压的影响
- 结合全波电磁软件FEKO与ATP，建立含真实接地系统的风机雷击暂态联合仿真方法
- 揭示高阻土壤高频下物理因素对接地阻抗及地电位升的显著影响规律，为绝缘设计提供依据


## 使用的方法


- [[矩量法-mom|矩量法(MoM)]]
- [[全波电磁仿真|全波电磁仿真]]
- [[atp电磁暂态仿真|ATP电磁暂态仿真]]
- [[集中参数电路模型|集中参数电路模型]]
- [[频变土壤建模|频变土壤建模]]
- [[谐波阻抗计算|谐波阻抗计算]]


## 涉及的模型


- [[风力发电机|风力发电机]]
- [[接地系统|接地系统]]
- [[机舱与塔基|机舱与塔基]]
- [[雷电流源|雷电流源]]
- [[频变土壤模型|频变土壤模型]]
- [[archie孔隙模型|Archie孔隙模型]]


## 相关主题


- [[雷击暂态分析|雷击暂态分析]]
- [[接地系统建模|接地系统建模]]
- [[频变土壤特性|频变土壤特性]]
- [[地电位升-gpr|地电位升(GPR)]]
- [[风机防雷保护|风机防雷保护]]
- [[土壤物理参数影响|土壤物理参数影响]]


## 主要发现


- 频变与高含水率显著降低高频接地阻抗，使地电位升及机舱电压峰值较恒定土壤明显下降
- Portela模型预测电压降幅最大，Datsios-Mikropoulos模型最接近恒定土壤
- 土壤孔隙率增大会导致地电位升峰值升高，而含水量增加则因导电性增强使暂态电压降低



## 方法细节

### 方法概述

采用全波电磁仿真与电磁暂态(EMT)联合仿真方法。首先基于矩量法(MoM)在FEKO中建立风机真实接地系统模型，计算100 Hz至10 MHz频段的谐波阻抗(HI)。引入六种土壤模型（5种频变模型VP/P/VA/AV/DM及1种孔隙率/含水率模型Archie），与恒定参数(FC)干土壤进行对比。通过归一化均方根偏差(NRMSD)量化土壤电参数差异。随后将频域阻抗转换为冲击阻抗(Zp)，导入ATP软件构建集中参数等效电路。风机塔筒与叶片采用无损传输线模型（波阻抗与传播速度经几何参数计算），雷电流源（首次回击FRS与后续回击SRS）注入叶片尖端。利用逆傅里叶变换计算地电位升(GPR)，并在ATP中求解机舱与塔基的暂态过电压，评估不同物理因素对绝缘配合的影响。

### 数学公式


**公式1**: $$$i(t) = \sum_{k=1}^{m} \frac{I_{0k}}{\eta_k} \frac{(t/\tau_{1k})^{n_k}}{1+(t/\tau_{1k})^{n_k}} e^{-t/\tau_{2k}}$$$

*Heidler函数雷电流波形模型，用于生成FRS和SRS注入电流*


**公式2**: $$$GPR = \mathcal{F}^{-1} \{ I(j\omega) \times Z_h(j\omega) \}$$$

*频域地电位升计算公式，通过雷电流频谱与接地系统谐波阻抗乘积的逆傅里叶变换获得时域波形*


**公式3**: $$$Z_p = \frac{\max[GPR]}{\max[i(t)]} = \frac{V_p}{I_p}$$$

*冲击阻抗定义，用于将频变接地系统等效为ATP中的集中参数模型*


**公式4**: $$$\sigma(W, \phi) = \sigma_{dry} + \left( \frac{\sigma_{sat} - \sigma_{dry}}{\phi^2} - \eta \right) W^2 + \eta \phi W$$$

*Archie广义土壤电导率模型，关联含水率W与孔隙率φ对土壤导电性的影响*


### 算法步骤

1. 步骤1：构建风机几何与接地系统模型。定义88m高塔筒（分4段无损传输线）、47.5m长叶片（细导线模型）及由同心环与8根垂直接地极组成的真实接地网。

2. 步骤2：设定土壤物理参数与模型。选取低频电阻率ρ0（500/1000/2500/5000 Ωm）、含水率W（1%~25%）及孔隙率φ（2.5%~25%），加载VP、P、VA、AV、DM及Archie六种模型，以FC干土壤为基准。

3. 步骤3：全波电磁计算谐波阻抗。在FEKO中调用MoM算法，扫描100 Hz至10 MHz频段，计算各模型下的接地系统复阻抗Zh(jω)。

4. 步骤4：参数偏差量化分析。利用NRMSD公式计算各频变模型电阻率ρ(f)与相对介电常数εr(f)相对于FC基准的偏差，评估模型适用性。

5. 步骤5：雷电流注入与频域响应计算。将FRS与SRS电流波形进行FFT得到I(jω)，与Zh(jω)相乘后执行逆FFT，获取时域GPR波形。

6. 步骤6：提取冲击阻抗并构建EMT电路。根据GPR与电流峰值比计算Zp，在ATP中建立包含叶片波阻抗Zb、塔段波阻抗Zi及接地冲击阻抗Zp的集中参数网络。

7. 步骤7：暂态过电压求解与对比。在ATP中运行EMT仿真，记录塔基与机舱电压峰值，横向对比不同土壤模型、雷电流类型及物理参数组合下的暂态响应差异。


### 关键参数

- **低频电阻率_ρ0**: 500, 1000, 2500, 5000 Ωm

- **频率扫描范围**: 100 Hz - 10 MHz

- **雷电流类型**: 首次回击(FRS)与后续回击(SRS)，通道阻抗400 Ω

- **风机几何参数**: 塔高88m，叶片长47.5m/半径5mm，波速vt=0.85c, vb=0.65c

- **Archie模型参数**: 孔隙率φ: 2.5%~25%，含水率W: 1%~25%，沙土组分系数α=0.654, β=0.018



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 不同ρ0下FRS冲击阻抗对比 | 在FRS雷击下，FC土壤模型的冲击阻抗Zp随ρ0增加而上升：500Ωm时为6.19Ω，1000Ωm时为8.02Ω，2500Ωm时为12.30Ω，5000Ωm时为22.32Ω。VP模型在500Ωm时Zp降至5.39Ω（较FC下降13%）。 | 频变模型在高频段显著降低接地阻抗，高阻土壤(5000Ωm)下Portela(P)模型预测的阻抗降幅最大，Datsios-Mikropoulos(DM)模型最接近FC基准。 |

| SRS与FRS地电位升(GPR)峰值对比 | SRS雷电流因具有更陡峭的波头（T10=0.50μs）和更高频分量，其激发的GPR峰值显著高于FRS。在FC土壤5000Ωm条件下，SRS的Zp达44.60Ω，约为FRS(22.32Ω)的2倍。 | SRS引起的暂态过电压与GPR峰值较FRS提升约100%，凸显高频土壤频变特性对后续回击防护设计的关键影响。 |

| 含水率W与孔隙率φ对低频电阻率的影响 | 基于Archie模型，当φ固定为25%时，W从1%增至25%，土壤电导率显著提升，低频电阻率RLF下降，导致GPR峰值降低。当W固定为1%时，φ从2.5%增至25%，RLF上升并趋近干沙土值，GPR峰值相应增大。 | 含水率增加使暂态电压降低（导电通路增多），孔隙率增大使GPR峰值升高（空气孔隙阻断电流），物理参数变化对RLF的调节幅度可达数倍。 |



## 量化发现

- 频变土壤模型在高频段(>100kHz)使接地阻抗显著下降，高阻土壤(ρ0=5000Ωm)下Portela模型预测的GPR峰值较FC模型下降幅度最大，而DM模型偏差最小（最接近FC响应）。
- NRMSD分析表明，土壤电阻率偏差随ρ0增大而增加（VP模型除外，其偏差恒定），P模型在ρ0=5000Ωm时相对介电常数与电阻率偏离FC基准最显著，DM模型因针对湿润沙土开发，偏差最低。
- SRS雷电流激发的GPR峰值约为FRS的2倍（如5000Ωm下44.60Ω vs 22.32Ω），主要归因于SRS更短的波头时间(0.25~2μs)激发的高频土壤频变效应。
- 孔隙率φ每增加10%，低频接地电阻RLF呈非线性上升，导致GPR峰值同步增大；含水率W从1%提升至25%时，土壤电导率呈二次方增长，暂态电压峰值下降幅度可达30%以上。
- ATP联合仿真验证表明，忽略土壤频变特性与物理参数将导致高阻土壤下风机绝缘配合设计偏保守（FC模型预测电压偏高），采用P或AV模型可优化防雷接地设计裕度。


## 关键公式

### 频域地电位升计算方程

$$$GPR = \mathcal{F}^{-1} \{ I(j\omega) \times Z_h(j\omega) \}$$$

*用于将全波电磁软件计算的频变接地阻抗与雷电流频谱结合，转换至时域以获取GPR波形*

### 冲击阻抗等效方程

$$$Z_p = \frac{\max[GPR]}{\max[i(t)]}$$$

*将频变非线性接地系统简化为ATP电磁暂态仿真中的集中参数元件，用于暂态过电压求解*

### Heidler雷电流源模型

$$$i(t) = \sum_{k=1}^{m} \frac{I_{0k}}{\eta_k} \frac{(t/\tau_{1k})^{n_k}}{1+(t/\tau_{1k})^{n_k}} e^{-t/\tau_{2k}}$$$

*定义首次回击(FRS)与后续回击(SRS)的时域波形，作为全波仿真与EMT仿真的激励源*



## 验证详情

- **验证方式**: 全波电磁-电磁暂态联合仿真对比验证，以恒定参数(FC)干土壤为基准，通过NRMSD量化频变模型偏差，并在ATP中评估暂态响应差异
- **测试系统**: 88m高风力发电机（4段塔筒+47.5m叶片）及真实接地系统（同心环+8根垂直接地极）
- **仿真工具**: FEKO/Altair Engineering (全波电磁/MoM), ATP (电磁暂态仿真)
- **验证结果**: 验证表明频变土壤模型与物理参数(W, φ)对高频接地阻抗影响显著。Portela模型预测的GPR与机舱电压降幅最大，DM模型最接近FC基准。SRS雷击因高频分量丰富，其GPR峰值约为FRS的2倍。含水率增加有效降低暂态过电压，孔隙率增大则抬升GPR峰值。联合仿真方法为高阻土壤风机防雷绝缘设计提供了精确的物理依据。
