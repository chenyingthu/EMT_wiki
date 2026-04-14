---
title: "Extension of a modal-domain transmission line model for including frequency-dependent soil parameters"
type: source
authors: ['未知']
year: 2016
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/18/De Conti和Emídio - 2016 - Extension of a modal-domain transmission line model to include frequency-dependent ground parameters.pdf"]
---

# Extension of a modal-domain transmission line model for including frequency-dependent soil parameters

**作者**: 
**年份**: 2016
**来源**: `18/De Conti和Emídio - 2016 - Extension of a modal-domain transmission line model to include frequency-dependent ground parameters.pdf`

## 摘要

*（摘要未提取到）*

## 核心贡献

- 扩展了基于模域的输电线路模型，使其能够纳入频率相关的土壤参数
- 提出将频域传播函数和特征阻抗拟合为有理函数和的方法，并生成ATP可识别的.pch文件以实现频变线路模型的时域仿真
- 系统评估了在低导电率土壤中假设恒定与频变接地参数对地回路阻抗和接地导纳修正计算带来的误差

## 使用的方法

- [[模域输电线路建模|模域输电线路建模]]
- [[频域有理函数拟合技术|频域有理函数拟合技术]]
- [[基于现场测量的宽频土壤参数建模|基于现场测量的宽频土壤参数建模]]
- [[atp-emtp时域电磁暂态仿真|ATP/EMTP时域电磁暂态仿真]]
- [[地回路阻抗与接地导纳修正计算|地回路阻抗与接地导纳修正计算]]

## 涉及的模型

- [[架空配电线路|架空配电线路]]
- [[频变土壤-接地参数模型|频变土壤/接地参数模型]]
- [[模域输电线路模型|模域输电线路模型]]
- [[atp频变线路模型-pch文件|ATP频变线路模型（.pch文件）]]

## 相关主题

- [[电磁暂态-emt-仿真|电磁暂态（EMT）仿真]]
- [[频率相关接地参数|频率相关接地参数]]
- [[输电线路建模|输电线路建模]]
- [[接地导纳修正|接地导纳修正]]
- [[频域拟合与时域转换|频域拟合与时域转换]]

## 主要发现

- 在土壤导电性较差的情况下，考虑频率相关的接地参数对输电线路高频电磁暂态仿真结果具有显著影响
- 线路分支的存在往往会削弱或最小化频变接地参数带来的仿真差异
- 只要为土壤相对介电常数选择合适的恒定值，使用恒定的土壤电导率和介电常数也能获得与频变土壤模型相当的仿真精度
