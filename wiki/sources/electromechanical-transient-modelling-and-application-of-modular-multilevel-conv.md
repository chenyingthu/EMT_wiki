---
title: "Electromechanical transient modelling and application of modular multilevel converter with embedded energy storage"
type: source
authors: ['未知']
year: 2021
journal: "IET Generation Trans & Dist 2022.16:123-136"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/17/Yu 等 - 2022 - Electromechanical transient modelling and application of modular multilevel converter with embedded.pdf"]
---

# Electromechanical transient modelling and application of modular multilevel converter with embedded energy storage

**作者**: 
**年份**: 2021
**来源**: `17/Yu 等 - 2022 - Electromechanical transient modelling and application of modular multilevel converter with embedded.pdf`

## 摘要

This paper studies the electromechanical transient modelling techniques of the modiﬁed modular multilevel converter (MMC), named active MMC, which is equipped with embed- ded energy storage in submodules. Firstly, the mathematical model of the active MMC and its equivalent circuits at the AC and DC sides are established. Then, the control scheme of active MMC that focus on the cooperation of the MMC converter and the energy stor- age submodules is illustrated. The proposed electromechanical transient model are imple- mented on PSS/E and compared with the electromagnetic transient model on PSCAD in a two terminal active MMC sytem; the results of the active MMC system under AC and DC fault prove the validity of the proposed model. Lastly, stability studies of the practical sys- tem are carri

## 核心贡献


- 推导含储能MMC机电暂态模型，直流侧引入附加电流源模拟储能动态响应
- 提出换流器与储能子模块协同控制策略，实现交直流故障下的功率解耦
- 在PSS/E平台实现模型并与PSCAD对比，验证功角与频率稳定性提升


## 使用的方法


- [[机电暂态建模|机电暂态建模]]
- [[矢量控制|矢量控制]]
- [[一阶惯性等效|一阶惯性等效]]
- [[等效电路法|等效电路法]]
- [[电磁暂态对比验证|电磁暂态对比验证]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[储能子系统-ess|储能子系统(ESS)]]
- [[双向dc-dc变换器|双向DC-DC变换器]]
- [[两端直流输电系统|两端直流输电系统]]


## 相关主题


- [[机电暂态仿真|机电暂态仿真]]
- [[mmc-model|MMC]]
- [[暂态稳定性分析|暂态稳定性分析]]
- [[故障穿越|故障穿越]]
- [[交直流系统解耦|交直流系统解耦]]


## 主要发现


- 所提机电暂态模型在交直流故障下的动态响应与PSCAD电磁暂态模型高度吻合
- 嵌入式储能有效解耦交直流功率耦合，显著抑制故障在异步电网间的传播
- 含储能MMC的应用显著提升了实际电力系统的功角稳定性与频率稳定性


