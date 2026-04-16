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


