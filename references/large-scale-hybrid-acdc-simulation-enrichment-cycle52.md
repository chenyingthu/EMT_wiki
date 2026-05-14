# Large-Scale Hybrid AC/DC Simulation Enrichment — Cycle 52

## 概览

| 项目 | 值 |
|------|------|
| 页面 | large-scale-hybrid-acdc-simulation.md |
| 分类 | topics/simulation/ |
| 类型 | 门户概述页 |
| 改进前 | ~1378字, 8公式, 16wikilinks, 0SVG, 8章节, 1mermaid模板图 |
| 改进后 | ~4175字, 40公式(10块级+30行内), 15wikilinks(全部验证有效), 0SVG, 9章节, 7表格 |
| 跳过SVG | 是 — 公式密集型门户页，量化数据和决策表是核心交付物 |

## 来源论文（6篇核心PDF）

1. **Shu 等 2018** — "A Multirate EMT Co-Simulation of Large AC and MMC-Based MTDC Systems"
   - 多速率协同仿真框架、Thevenin/Norton接口模型、移动窗预测、数值振荡抑制算法
   - PDF缓存：`extracted_text/markdown_enhanced/a-multirate-emt-co-simulation-of-large-ac-and-mmc-based-mtdc-systems.md` (4900 bytes)

2. **Zhou 等 2021** — "Large-scale hybrid real time simulation modeling and benchmark for Nelson River multi-infeed HVdc system"
   - Manitoba Hydro Nelson River LCC-HVDC 多端系统混合实时仿真工程实践
   - PDF提取：`pdftotext` (41392 bytes)

3. **Xiong 等 2020** — "Electromechanical-electromagnetic transient hybrid simulation of an AC/DC hybrid power grid with UHVDC"
   - ±800 kV 雅中-江西 UHVDC 分层接入，ADPSS 混合仿真模型，误差 < 2%
   - PDF提取：`pdftotext` (41020 bytes)

4. **van der Meer 等 2015** — "Advanced Hybrid Transient Stability and EMT Simulation for VSC-HVDC Systems"
   - 三项改进：故障后阻抗重新因式分解、Thevenin源更新协议、故障相量确定协议
   - PDF提取：`pdftotext` (74965 bytes)

5. **Le-Huy 等 2023** — "Lessons learned in porting offline large-scale power system simulation to real-time"
   - Hydro-Québec 1666母线 EMTP→HYPERSIM 移植经验，组件统计表
   - PDF缓存：`extracted_text/pdftotext/25/Le-Huy 等 - 2023 - Lessons learned...` (54240 bytes)

6. **Xiong 等 2024** — "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator"
   - BBD分区并行网络求解，10080总线系统36×加速比，42分区最优
   - PDF缓存：`extracted_text/pdftotext/30/Xiong 等 - 2024 - ParaEMT...` (73816 bytes)

## 写作策略

**门户概述页四层次体系模式**：页面采用"四层次仿真方法体系"（全EMT→EMT-机电混合→多速率EMT→等值降阶）组织内容，而非单一方法深度分析。每层次包含原理、数学表达、特点和适用场景。

**量化数据驱动**：页面包含7个表格（Hydro-Québec组件统计、加速性能数据、精度数据、多速率步长扩展、方法选择决策表、外部系统等值选择指南），所有数据点标注来源论文。

**公式密度**：40个公式覆盖伴circuit离散化、BBD分区并行、多速率接口更新、初始化等核心机制。

## 改进要点

1. **门户页结构重构**：原页面有8个章节但内容以描述性文字为主，缺乏量化数据。新页面将"主要分支与机制"扩展为详细的"仿真方法体系"四层次框架，每层次含独立公式推导。
2. **引入工程基准数据**：从 Le-Huy 2023 和 Xiong 2024 提取 Hydro-Québec 1666母线全系统组件统计和 ParaEMT 10080总线加速数据。
3. **方法选择决策表**：新增场景-方法决策表，指导用户在不同应用场景下选择合适的仿真方法。
4. **接口稳定性深入分析**：从 van der Meer 2015 提取三项改进协议，从 Shu 2018 提取数值振荡抑制算法公式。
5. **UHVDC分层接入案例**：从 Xiong 2020 提取雅中-江西工程的具体精度数据（混合仿真vs纯EMT误差<2%，vs机电暂态误差15-20%）。
6. **跳过SVG**：页面以公式和量化数据为核心交付物，跳过SVG以避免强行加图导致内容冗余。

## 队列更新

- 数据行（第78行）：`pending |` → `completed |`
- 轮次记录：追加 `||| 52 | large-scale-hybrid-acdc-simulation.md | ... | 完成 | 4175字/40公式/15wikilinks/7表格/9章节/6篇来源论文/四层次仿真方法体系+BBD并行+多速率接口 |`
