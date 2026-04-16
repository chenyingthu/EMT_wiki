---
title: "Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Liu 等 - 2010 - Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri.pdf"]
---

# Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri

**作者**: 
**年份**: 2026
**来源**: `17/Liu 等 - 2010 - Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri.pdf`

## 摘要

An effective solution of electromechanical transient and electromagnetic transient hybrid simulation was proposed, including interface selection, mutual equivalence methods between electromechanical transient and electro- magnetic transient network. It is able to deal with the situation that the positive and negative sequence parameters of equiva- lence circuit are different. Least square method was adopted to obtain three-sequence fundamental frequency current which indicated the influence of electromagnetic transiet simulation on the electromechanical network. The solution is demonstrated effective and feasible through several cases. Problems in hybrid simulation are solved when various faults (including symmetric and asymmetric faults) occur in electromechanical network. KEY WORDS: HVDC

## 核心贡献


- 提出机电与电磁混合仿真接口选取及双向诺顿等值交互方法，实现多端口耦合等效
- 提出基波负序补偿法处理等值电路正负序参数不等问题，有效消除稳态计算误差
- 采用最小二乘法提取三序基波电流，实现电磁暂态结果对机电网络的精确反馈


## 使用的方法


- [[混合仿真|混合仿真]]
- [[诺顿等值|诺顿等值]]
- [[补偿法|补偿法]]
- [[最小二乘法|最小二乘法]]
- [[序网-三相坐标变换|序网-三相坐标变换]]
- [[迭代交互求解|迭代交互求解]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[换流器|换流器]]
- [[换流变压器|换流变压器]]
- [[同步发电机|同步发电机]]
- [[动态负荷|动态负荷]]
- [[交流电网|交流电网]]


## 相关主题


- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[不对称故障|不对称故障]]
- [[网络等值|网络等值]]
- [[接口交互技术|接口交互技术]]
- [[正负序参数处理|正负序参数处理]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 正负序参数不等会导致导纳矩阵不对称，若不处理将引发显著的稳态功率计算误差
- 所提方案在对称与不对称故障下均能保持接口数据交互稳定，混合仿真结果准确可靠
- 经IEEE九节点及大电网验证，该方法兼顾局部电磁暂态精度与全网计算效率


