---
title: "Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inverter Control Systems"
type: source
authors: ['未知']
year: 2024
journal: "2024 IEEE Power & Energy Society General Meeting (PESGM);2024; ; ;10.1109/PESGM51994.2024.10688962"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/06/Ranasinghe 等 - 2024 - Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inve.pdf"]
---

# Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inverter Control Systems

**作者**: 
**年份**: 2024
**来源**: `06/Ranasinghe 等 - 2024 - Advanced DSOGI PLL with Adaptive Bandwidth for Improved Transient Performance of Grid Connected Inve.pdf`

## 摘要

² 7KLV SDSHU SURSRVHV DQDGYDQFHGPRGLILHG 'RXEOH 6HFRQG 2UGHU *HQHUDOL]HG ,QWHJUDWRU '62*, 3KDVH/RFNHG /RRS3//WDLORUHG VSHFLDOO\ IRULQYHUWHUEDVHGV\VWHPV ZKLFK XVHV GHFRXSOHG FRQWURO V\VWHPV 7KH SURSRVHG HQKDQFHPHQWV LQFRUSRUDWH D WUDQVLHQW GHWHFWRU IRU WHPSRUDULO\ IUHH]LQJ WKH 3//IUHTXHQF\ ZKLFKLVXVHG ZLWKLQWKH'62*,3//FRQWURO V\VWHPGXULQJWUDQVLHQWV$GGLWLRQDOO\DQDGDSWLYHEDQGZLGWK WHFKQLTXH G\QDPLFDOO\ DGMXVWV WKH 3// EDQGZLGWK HQVXULQJ VZLIWUHVSRQVHDQGUHGXFHGSKDVHHUURUGXULQJGLVWXUEDQFHV7KH VWXG\ XQGHUVFRUHV WKH LPSRUWDQFH RI WKHVH PRGLILFDWLRQV LQ DFKLHYLQJ UDSLG DQG DFFXUDWH V\QFKURQL]DWLRQ HVSHFLDOO\ LQ LQYHUWHUEDVHG V\VWHPV 6LPXODWLRQ UHVXOWV YDOLGDWH

## 核心贡献


- 提出集成暂态检测器的改进型DSOGI-PLL，扰动期间冻结频率以维持滤波稳定性
- 设计自适应带宽调节机制，依相位误差动态调整PLL带宽，实现快速同步并降低暂态误差
- 引入反正切线性化方法，消除电压幅值波动对PLL带宽的影响，提升弱网同步鲁棒性


## 使用的方法


- [[dsogi-pll|DSOGI-PLL]]
- [[srf-pll|SRF-PLL]]
- [[小信号建模|小信号建模]]
- [[自适应带宽控制|自适应带宽控制]]
- [[暂态检测|暂态检测]]
- [[正序分量计算|正序分量计算]]
- [[反正切线性化|反正切线性化]]


## 涉及的模型


- [[并网逆变器|并网逆变器]]
- [[光伏系统|光伏系统]]
- [[弱电网|弱电网]]
- [[输电网络|输电网络]]
- [[dsogi-pll模型|DSOGI-PLL模型]]
- [[srf-pll模型|SRF-PLL模型]]


## 相关主题


- [[锁相环控制|锁相环控制]]
- [[弱网同步|弱网同步]]
- [[暂态稳定性|暂态稳定性]]
- [[故障穿越|故障穿越]]
- [[逆变器控制|逆变器控制]]
- [[新能源并网|新能源并网]]


## 主要发现


- 仿真验证表明，暂态冻结机制有效抑制了扰动期间的频率波动，维持了DSOGI滤波性能
- 自适应带宽策略显著缩短了故障同步时间，大幅降低暂态相位误差，提升系统恢复速度
- 改进型PLL在弱网故障下有效抑制逆变器失稳风险，且未牺牲稳态精度与谐波抑制能力



## 方法细节

### 方法概述

本文提出一种面向弱电网并网逆变器的改进型DSOGI-PLL。该方法在传统DSOGI-PLL基础上引入三大核心机制：首先，采用反正切函数替代直接q轴电压反馈，消除电压幅值波动对PLL带宽的非线性影响，实现环路线性化；其次，设计暂态检测器，当检测到频率突变时，将输入SOGI滤波器的频率值冻结为暂态前瞬时值，持续固定时长，防止频率剧烈波动破坏滤波特性；最后，构建自适应带宽调节机制，当相位误差超过阈值时，将PLL带宽大幅提升以加速同步，随后随时间线性恢复至标称值以抑制超调。三者协同工作，在保持稳态谐波抑制能力的同时，显著提升故障与相位跳变下的暂态跟踪速度与系统鲁棒性。

### 数学公式


**公式1**: $$$G_{ol_{DSOGI}} = \left(\frac{K_p s + K_i}{s}\right)\left(\frac{\omega_p}{\omega_p + s}\right)\frac{1}{s}$$$

*DSOGI-PLL开环传递函数，用于分析系统动态响应与带宽特性*


**公式2**: $$$s^3 + \omega_p s^2 + K_p \omega_p s + K_i \omega_p = 0$$$

*系统闭环特征方程，用于推导极点分布与稳定性条件*


**公式3**: $$$\omega_p = 2\xi\omega_n + A,\quad A\omega_n^2 = K_i \omega_p,\quad \omega_n^2 + 2\xi\omega_n A = \omega_p K_p$$$

*PI控制器参数整定关系式，通过匹配特征方程系数实现目标阻尼比与自然频率*


**公式4**: $$$RMSE = \sqrt{\frac{\sum_{k=1}^{N}(h_{predicted} - h_{actual})^2}{N}}$$$

*均方根误差计算公式，用于量化相位与频率跟踪精度*


### 算法步骤

1. 信号预处理与正序提取：三相电网电压经Clarke变换得到αβ静止坐标系分量，输入双SOGI-QSG模块进行带通/低通滤波与正交信号生成，随后经正序分量计算器(PSC)提取基波正序分量。

2. 线性化相位误差计算：将提取的正序分量经Park变换至dq同步旋转坐标系，采用反正切函数计算相位误差，彻底消除电压幅值波动对环路增益的非线性耦合。

3. 暂态检测与频率冻结：实时监测PLL输出频率的变化率，若突变超过设定阈值，立即触发暂态检测器，将反馈至SOGI模块的频率值锁定为暂态发生前一时刻的数值，保持冻结状态直至预设时间结束。

4. 自适应带宽切换与PI增益重算：实时计算相位误差绝对值，若大于阈值，将目标穿越频率提升至标称值5倍；利用特征方程系数匹配法在线计算对应的Kp与Ki；当误差衰减后，控制增益随时间线性平滑恢复至稳态标称值。

5. 闭环同步输出：PI控制器输出角频率偏差，叠加系统额定角频率后进行积分运算，得到最终估计相位角，完成电网电压的快速、精准同步。


### 关键参数

- **SOGI阻尼系数_k**: 1.414（对应0.7阻尼比）

- **标称穿越频率_ωc**: 62 rad/s（针对60Hz系统）

- **标称PI参数_Kp_Ki**: 57.1, 1660.1

- **相位误差阈值_ε**: 0.1 rad

- **频率冻结时间_Tfz**: 0.1 s

- **暂态带宽放大倍数**: 5倍

- **目标阻尼比_ξ**: 0.7



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 人工测试波形（不对称故障） | 在不对称故障注入下，改进型PLL的相位误差调节时间从0.040s缩短至0.016s，超调量从0.272 rad降至0.113 rad。 | 调节时间缩短60%，超调量降低58.5% |

| 人工测试波形（90°相位跳变） | 在90°相位阶跃下，调节时间从0.15s大幅缩短至0.03s，超调量从2.003 rad降至1.719 rad。 | 调节时间缩短80%，超调量降低14.2% |

| IEEE 9节点弱电网光伏系统（SCR≈1.8） | 传统DSOGI-PLL在故障清除后失稳，改进型PLL在约0.5s内恢复稳定运行，且系统临界稳定短路比(SCR)从2.3扩展至1.0。 | 弱电网稳定极限SCR提升约56.5%，实现极弱网下的可靠同步 |

| 频率跟踪精度（8.0-9.0s暂态区间） | 无ABW时频率RMSE为2.16 Hz，仅用ABW为1.880 Hz，结合暂态检测器后骤降至0.001 Hz。 | 暂态频率跟踪误差降低99.95%，有效抑制带宽提升带来的高频振荡 |



## 量化发现

- 不对称故障下调节时间缩短60%（0.040s→0.016s），超调量降低58.5%（0.272 rad→0.113 rad）
- 90°相位跳变下调节时间缩短80%（0.15s→0.03s），超调量降低14.2%（2.003 rad→1.719 rad）
- 关键暂态区间（8.0-9.0s）频率跟踪RMSE从2.16 Hz降至0.001 Hz，降幅达99.95%
- 稳态谐波抑制能力未退化，THD 4%工况下相位误差RMSE从0.0078 rad优化至0.0063 rad
- 系统稳定运行临界短路比(SCR)从2.3扩展至1.0，弱电网适应性提升56.5%
- 7Hz/s极端频率斜坡下，相位误差RMSE保持0.015 rad，与传统方法持平且未引入额外稳态误差


## 关键公式

### DSOGI-PLL开环传递函数

$$$G_{ol_{DSOGI}} = \left(\frac{K_p s + K_i}{s}\right)\left(\frac{\omega_p}{\omega_p + s}\right)\frac{1}{s}$$$

*用于分析PLL动态特性、设计标称带宽及推导自适应增益切换逻辑*

### 自适应PI参数整定方程组

$$$\omega_p = 2\xi\omega_n + A,\quad A\omega_n^2 = K_i \omega_p,\quad \omega_n^2 + 2\xi\omega_n A = \omega_p K_p$$$

*在暂态检测触发带宽切换时，实时计算满足目标阻尼比(ξ=0.7)的Kp与Ki值*

### 线性化相位误差计算式

$$$\theta_{err} = \tan^{-1}\left(\frac{V_q}{V_d}\right)$$$

*替代传统SRF-PLL的直接Vq反馈，消除电压幅值波动对PLL带宽的非线性影响*



## 验证详情

- **验证方式**: 电磁暂态仿真对比分析（含人工波形测试与系统级并网测试）
- **测试系统**: 1) 柔性人工测试波形发生器系统（支持动态幅值/相位/频率调节及谐波注入）；2) 替换同步发电机的IEEE 9节点系统（接入光伏逆变器，运行于SCR≈1.8的弱电网环境）
- **仿真工具**: PSCAD/EMTDC（仿真步长50 μs）
- **验证结果**: 仿真全面验证了所提改进型DSOGI-PLL的有效性。在不对称故障、相位跳变及频率斜坡等极端暂态下，同步速度提升3-5倍，超调显著抑制，频率跟踪误差降低两个数量级；在SCR低至1.0的极弱电网中仍能保持稳定，且稳态谐波抑制性能未受影响，综合性能显著优于传统DSOGI-PLL与SRF-PLL。
