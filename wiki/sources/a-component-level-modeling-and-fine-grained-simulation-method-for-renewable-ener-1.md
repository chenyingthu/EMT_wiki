---
title: "A component-level modeling and fine-grained simulation method for renewable energy power systems sui"
type: source
year: 2025
journal: "IEEE Transactions on Magnetics"
created: "2026-04-13"
sources: ["EMT_Doc/01/Wang 等 - 2026 - A component-level modeling and fine-grained simulation method for renewable energy power systems sui.pdf"]
---

# A component-level modeling and fine-grained simulation method for renewable energy power systems sui

**年份**: 2025
**来源**: `01/Wang 等 - 2026 - A component-level modeling and fine-grained simulation method for renewable energy power systems sui.pdf`

## 摘要

—The detailed modeling of renewable energy power stations captures the full impedance characteristics of the system but significantly increases the scale of electromagnetic transient (EMT) simulations. Parallel computing is essential to enhance the simulation efficiency, but it requires algorithms that are specifically designed to leverage

## 核心贡献


- 提出广义延迟插入法，引入受控源突破传统拓扑限制，实现复杂系统统一建模
- 构建以三相节点支路为单元的GPU细粒度并行算法，实现线性复杂度高效求解


## 使用的方法


- [[广义延迟插入法|广义延迟插入法]]
- [[蛙跳差分法|蛙跳差分法]]
- [[gpu多线程并行|GPU多线程并行]]
- [[节点分析法|节点分析法]]
- [[细粒度并行求解|细粒度并行求解]]


## 涉及的模型


- [[风电场|风电场]]
- [[风力发电机组|风力发电机组]]
- [[电力电子变换器|电力电子变换器]]
- [[三相节点支路模型|三相节点支路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[细粒度仿真|细粒度仿真]]
- [[gpu加速|GPU加速]]
- [[新能源并网建模|新能源并网建模]]


## 主要发现


- 与PSCAD对比验证了GLIM模型的高精度，能准确捕捉系统全阻抗特性
- GPU仿真耗时不随风电场规模扩大显著增加，验证了算法的线性时间复杂度优势


