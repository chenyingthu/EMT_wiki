---
title: "University of Manitoba"
type: entity
entity_type: institution
tags: [manitoba, pscad, institution]
created: "2026-04-13"
---

# University of Manitoba

## 概述

曼尼托巴大学（University of Manitoba）是PSCAD/EMTDC软件的发源地，在电力系统EMT仿真领域有重要影响力。

## 核心原理详解

University of Manitoba 在本 wiki 中主要连接 [[pscad-emtdc|PSCAD/EMTDC]]、HVDC 电磁暂态建模、实时仿真和混合仿真研究。与 [[polytechnique-montreal|Polytechnique Montreal]] 偏重 EMTP-RV 和频变等值不同，Manitoba 线索更常出现在 PSCAD/EMTDC 工具、[[gole|A.M. Gole]] 的 HVDC/FACTS 建模，以及与 [[manitoba-hydro|Manitoba Hydro]] 相关的工程验证中。

HVDC EMT 建模通常要同时满足换流器微秒级电磁过程和交流系统毫秒级动态。其基本功率关系可概括为：

$$
P_{dc}=V_{dc}I_{dc}, \qquad
V_{dc}\approx V_{d0}\cos\alpha-X_c I_{dc}
$$

因此工具和模型必须能表达换相过程、控制系统、交流故障和直流线路暂态的耦合。

## EMT研究贡献

- PSCAD/EMTDC开发
- 电力系统仿真
- HVDC系统研究
- 风电场建模

## 关键技术详解

- **PSCAD/EMTDC 源流**：图形化建模与 EMTDC 求解器构成大量论文的详细 EMT 基准。
- **HVDC/FACTS 建模**：包括 LCC-HVDC、VSC-HVDC、SVC、换流器控制与交流系统交互。
- **混合仿真与实时仿真**：将详细 EMT 子系统接入大系统暂态稳定或实时 HIL 环境。
- **工程数据闭环**：与 Manitoba Hydro 的工程项目共同形成“模型-控制保护-现场系统”的验证链。

## 代表性研究线索

| 线索 | Wiki 中的意义 | 典型判断问题 |
|------|---------------|--------------|
| PSCAD/EMTDC 详细模型 | 用作平均模型、状态空间模型、接口模型的 EMT 基准 | 是否说明时间步长、开关模型、控制采样和故障条件 |
| HVDC/FACTS 控制 | 关注换流器控制、交流系统强度和保护动作的相互作用 | 是否包含控制保护细节，而不只是主电路拓扑 |
| 实时/混合仿真 | 将详细 EMT 子系统接到 TS、RTDS 或 HIL 平台 | 接口变量、延迟补偿和同步策略是否明确 |
| 工程系统验证 | 与 Manitoba Hydro 项目背景相关时可增强可信度 | 工程数据是否公开，还是只作为背景引用 |

## 代表性页面

- [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-]]：围绕 Nelson River HVDC 系统建立大规模混合实时仿真基准，是 Manitoba 线索中“工程系统+仿真平台”的典型页面。
- [[hybrid-model-transient-stability-simulation-using-dynamic-phasors-based-hvdc-22]]：展示 HVDC 动态相量接口模型如何服务 EMT/TS 混合仿真。
- [[pscad-emtdc]]：作为大量源论文的详细 EMT 基准工具，应和具体模型贡献分开判断。

## 证据使用规则

- “University of Manitoba”不是质量标签；只有当页面给出具体作者、工具、工程系统或模型接口时，才应作为技术谱系证据。
- PSCAD/EMTDC 结果适合作为详细 EMT 对照，但不能自动证明实时可运行、参数可迁移或保护逻辑完整。
- HVDC 页面要优先核对控制器、换流器类型、交流系统强弱和故障工况，这些因素通常比机构归属更影响结论。

## 页面质量检查清单

| 检查项 | 应确认的信息 | 常见误判 |
|--------|--------------|----------|
| PSCAD 基准 | 时间步长、开关模型、控制采样、故障时刻这 4 类设置 | 只写“PSCAD 验证” |
| HVDC 类型 | LCC、VSC、MMC、混合 HVDC 或 FACTS 的具体拓扑 | 把所有直流系统混成一类 |
| 工程背景 | 是否涉及 Manitoba Hydro、Nelson River 或具体工程参数 | 把机构名当作工程数据证据 |
| 混合/实时接口 | EMT-TS、RTDS、HIL 的接口变量和同步延迟 | 只报告一条对比波形 |

Manitoba 相关页面的质量重点是“详细 EMT 基准是否可复核”。对于 HVDC 或 FACTS 论文，至少要写清 3 个层级：主电路拓扑、控制保护逻辑、交流系统条件。若这 3 层缺失，即便使用 PSCAD/EMTDC，也只能说明作者运行了一个详细仿真工具，不能说明模型适合迁移到实时平台、大系统混合仿真或不同短路比条件。对 Nelson River 这类工程基准，还要区分公开参数、工程背景和作者自行构造的简化模型。

## 适用边界与注意事项

- 提到 University of Manitoba 时，应区分学术研究、PSCAD/EMTDC 工具发展和 Manitoba Hydro 工程应用三类证据。
- HVDC 模型的可信度依赖控制保护细节、换流器参数和交流系统强度；只有软件名称不足以说明模型质量。
- 若论文只用 PSCAD 作为仿真工具，不应自动推断其与 Manitoba 研究谱系有直接贡献关系。

## 开放问题

- 高比例电力电子系统中，PSCAD 详细模型如何与实时平台和大电网稳定分析模型保持参数一致。
- HVDC/FACTS 详细模型如何在保护动作、控制延迟和弱交流系统条件下建立可复核基准。

## 相关实体
- [[pscad-emtdc]]
- [[manitoba-hydro]]
- [[gole]]
- [[rtds]]
- [[co-simulation]]
