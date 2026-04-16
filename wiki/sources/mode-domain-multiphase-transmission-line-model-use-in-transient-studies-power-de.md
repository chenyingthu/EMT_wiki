---
title: "Mode domain multiphase transmission line model - use in transient studies - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/26/Tavares 等 - 1999 - Mode domain multiphase transmission line model - use in transient studies.pdf"]
---

# Mode domain multiphase transmission line model - use in transient studies - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `26/Tavares 等 - 1999 - Mode domain multiphase transmission line model - use in transient studies.pdf`

## 摘要

This paper presents a new model te represent multiphase transmission lines in transient studies, including the frequency dependence of longitudinal parameters. The mndel iises the exact modes, fnr ideally transposed lines, and "quasi-modes'' for non-transpcaed lines. For the latter it is necessary to have a vertical symmetry plane. The frequency dependence is represented with synthetic circuits, with one IT- circuit fnr each mode. The transf~~rmatimi matrix used for the entire frequency range is tlie Clarke's (me ant1 as it is a real matrix it is modeled through ideal transformers. The model is described for three-phase lines and double three-phase lines. An application nf the metlioclology is presented for a 440 kV single three-phase transmission line where it is macle mecle analysis, sta

## 核心贡献


- 提出基于Clarke变换的模域多相线路模型，实现全频域实数相模变换。
- 采用理想变压器构建相模接口，解决复数变换矩阵在时域仿真中的实现难题。
- 利用综合电路与级联π型网络，精确表征各模态纵向参数的频率相关性。


## 使用的方法


- [[clarke变换|Clarke变换]]
- [[模域分析|模域分析]]
- [[级联π型电路|级联π型电路]]
- [[综合电路拟合|综合电路拟合]]
- [[理想变压器建模|理想变压器建模]]
- [[emtp时域仿真|EMTP时域仿真]]


## 涉及的模型


- [[三相输电线路|三相输电线路]]
- [[双回三相输电线路|双回三相输电线路]]
- [[semlyen频变线路模型|Semlyen频变线路模型]]
- [[π型等值电路|π型等值电路]]


## 相关主题


- [[频率相关建模|频率相关建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[模域变换|模域变换]]
- [[线路合闸暂态|线路合闸暂态]]
- [[相模解耦|相模解耦]]


## 主要发现


- 具垂直对称面的非换位线路经Clarke变换后，耦合模态可近似为独立准模态。
- 440kV线路合闸与扫频验证表明，该模型与Semlyen频变模型结果高度吻合。
- 理想变压器接口结合综合电路，在保障仿真精度的同时有效降低了时域计算负担。


