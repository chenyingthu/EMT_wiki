---
title: "Dead-time effect modeling for hybrid modular multilevel converter using twin mapping"
type: source
authors: ['Moke Feng']
year: 2026
journal: "International Journal of Electrical Power and Energy Systems, 175 (2026) 111623. doi:10.1016/j.ijepes.2026.111623"
tags: ['mmc']
created: "2026-04-13"
sources: ["EMT_Doc/12/1-s2.0-S0142061526000657-main.pdf"]
---

# Dead-time effect modeling for hybrid modular multilevel converter using twin mapping

**作者**: Moke Feng
**年份**: 2026
**来源**: `12/1-s2.0-S0142061526000657-main.pdf`

## 摘要

Dead-time effect modeling for hybrid modular multilevel converter using , Jianzhong Xu b, Wenxia Sima a, Ming Yang a, Hang Jing b, Keying Pan b a State Key Laboratory of Power Transmission Equipment Technology, Chongqing University, Chongqing 400044, China b State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing 102206, China Dead-time control is essential for modular multilevel converters (MMCs), but it negatively

## 核心贡献


- 提出基于二极管H桥的死区续流建模方法，将死区微观状态映射至桥臂宏观层面
- 提出孪生映射方法对电容状态分组切换，恢复桥臂完整性以适用戴维南等效定理
- 构建支持死区效应的高阶MMC戴维南等效模型，突破传统等效模型无法模拟死区的局限


## 使用的方法


- [[孪生映射法|孪生映射法]]
- [[戴维南等效|戴维南等效]]
- [[二极管h桥建模|二极管H桥建模]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[状态空间模型对比|状态空间模型对比]]


## 涉及的模型


- [[mmc-model|MMC]]
- [[半桥子模块-hbsm|半桥子模块(HBSM)]]
- [[全桥子模块-fbsm|全桥子模块(FBSM)]]
- [[戴维南等效模型|戴维南等效模型]]
- [[详细模型|详细模型]]
- [[状态空间模型|状态空间模型]]


## 相关主题


- [[死区效应建模|死区效应建模]]
- [[电磁暂态仿真加速|电磁暂态仿真加速]]
- [[mmc-model|MMC]]
- [[高压直流输电|高压直流输电]]
- [[电力电子等效建模|电力电子等效建模]]


## 主要发现


- PSCAD仿真验证该模型能精确捕捉死区引起的电压尖峰与凹陷波形特征
- 相比详细模型与状态空间模型，所提等效模型在保持精度的同时显著提升仿真速度
- 孪生映射法有效解决了死区续流破坏桥臂完整性的问题，实现了高效准确的暂态仿真


