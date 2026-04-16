---
title: "A Novel Distance Protection Algorithm in Frequency Domain Based on Parameter Identification"
type: source
authors: ['bgriffiths']
year: 2012
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/A novel distance protection algorithm in frequency domain based on parameter identification.pdf"]
---

# A Novel Distance Protection Algorithm in Frequency Domain Based on Parameter Identification

**作者**: bgriffiths
**年份**: 2012
**来源**: `13&14/files/A novel distance protection algorithm in frequency domain based on parameter identification.pdf`

## 摘要

6FKRRORI(OHFWULFDO(QJLQHHULQJ;L¶DQ-LDRWRQJ8QLYHUVLW\&KLQD(PDLOVXRQDQ#QHW 6FKRRORI(OHFWULFDO(QJLQHHULQJ;L¶DQ-LDRWRQJ8QLYHUVLW\&KLQD(PDLO]KRQJ\LQJ#VWX[MWXHGXFQ Á6FKRRORI(OHFWULFDO(QJLQHHULQJ;L¶DQ-LDRWRQJ8QLYHUVLW\&KLQD(PDLOVRQJJE#PDLO[MWXHGXFQ .H\ZRUGV GLVWDQFH SURWHFWLRQ RYHUUHDFK DFWLRQ SDUDPHWHU LGHQWLILFDWLRQPDWUL[SHQFLODOJRULWKP5/PRGHO

## 核心贡献


- 提出基于参数辨识的频域距离保护算法，构建含故障距离与过渡电阻的三元线性方程
- 引入矩阵束算法提取暂态基频与直流分量，消除DFT直流偏移干扰与微分误差
- 假设故障点后零序阻抗为纯电感，推导唯一解方程，从根本上解决传统保护超越动作难题


## 使用的方法


- [[参数辨识|参数辨识]]
- [[矩阵束算法|矩阵束算法]]
- [[频域分析|频域分析]]
- [[相模变换|相模变换]]
- [[线性方程求解|线性方程求解]]
- [[r-l模型|R-L模型]]


## 涉及的模型


- [[输电线路|输电线路]]
- [[r-l模型|R-L模型]]
- [[零序网络|零序网络]]
- [[双端电源系统|双端电源系统]]
- [[故障分量网络|故障分量网络]]


## 相关主题


- [[距离保护|距离保护]]
- [[单相接地故障|单相接地故障]]
- [[超越动作抑制|超越动作抑制]]
- [[故障测距|故障测距]]
- [[暂态信号处理|暂态信号处理]]
- [[高阻接地|高阻接地]]


## 主要发现


- 仿真验证表明算法在远端故障时测距准确，近端误差恒为正，有效防止距离继电器超越
- 算法对高过渡电阻抗干扰能力强，线性求解避免迭代多解，计算效率高满足实时保护要求
- 矩阵束算法能精准分离暂态直流与基频分量，显著提升频域参数辨识在故障初期的可靠性


