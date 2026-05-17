---
title: "风电场建模 (Wind Farm Modeling)"
type: topic
tags: [wind-farm, dfig, pmsg, wind-turbine, aggregation, equivalent-model, lvrt, clustering]
created: "2026-04-14"
updated: "2026-05-17"
---

# 风电场建模 (Wind Farm Modeling)

## 定义

风电场建模是大规模风力发电场在电磁暂态（EMT）仿真中的等值聚合方法研究。其核心目标是：在保留风机控制动态、集电网络电磁效应和故障穿越特性的前提下，将数十至数百台机组的详细模型等值为少数等值机或单机等值模型，以降低计算节点数、实现实时或超实时仿真。

风电场 EMT 建模面临三类典型挑战：① **设备异构性**——不同风机类型（DFIG/PMSG/异步机）、不同额定容量、不同控制策略共存；② **规模矛盾**——单台风机包含气动-机械-电力电子-控制多时间尺度子系统，场站级仿真若保留全部细节则计算量随机组数近似线性增长；③ **建模层次**——并网点（PCC）研究需要保留外部端口特性，内部故障振荡研究需要保留机间耦合，高频谐波研究需要保留开关细节。

## EMT 中的角色

风电场 EMT 建模在新能源并网研究中承担两层角色：

**并网接口层**：作为大电网 EMT 仿真的子网络，风电场等值模型向系统提供端口电压-电流关系。在 LCC-HVDC 或 VSC-HVDC 送端、并网点电压支撑和故障穿越研究中，需要等值模型准确反映有功/无功注入特性及低电压穿越（LVRT）响应。

**仿真加速层**：在 GPU/FPGA 实时仿真中，风电场节点是计算密集区。Lin 等（2021）证明：DFIG 节点天然满足单指令多线程（SIMT）并行条件（每台 DFIG 独立计算），但若保留全部详细开关模型，则 CPU-GPU 效率边界约为 100 台风机——超过此规模时 GPU 并行方能超越 CPU 效率。

## 主要风机类型

### 1. DFIG（双馈感应发电机）

DFIG 的定子直接并网，转子通过背靠背变流器连接电网。转子侧变流器（RSC）采用定子磁链定向的矢量控制，实现有功/无功解耦；网侧变流器（GSC）维持直流电压稳定。

**EMT 建模特点**：转子侧含电力电子变流器，需要开关级或平均值模型；定子磁链动态影响故障电流特性；Crowbar 保护电路在电网短路时投入，防止转子侧过电流。Mu 等（2019）建立了考虑 Crowbar 投切和变换器闭锁暂态的受控源型统一简化等效模型，在 PSCAD/EMTDC 中验证正确性、步长适应性和仿真速度提升。

DFIG 的 LVRT 响应特性随输出功率而异。Xu 等（2026）分析表明：不同风速下 DFIG 的主动功率轨迹差异显著，低风速时机组更早进入 LVRT 控制，有功恢复更慢——这构成同调分群的物理基础。

### 2. PMSG（永磁同步发电机）

PMSG 为全功率变流器结构，定子经全功率变频器并网，无齿轮箱（直驱），效率高、可靠性好，是海上风电主流选择。

**EMT 建模特点**：全功率变流器需要完整的开关级或平均值模型；不存在转子侧磁链动态；故障穿越期间变流器需提供无功支撑。固定导纳模型（Fixed Admittance）结合补偿法可用于 PMSG 简化建模，在保留外特性的同时消除开关动作导致的矩阵重构。

### 3. 异步风力发电机

固定转速机组，结构简单，早期风电场主要类型，已逐步被 DFIG/PMSG 替代。

## 等值聚合方法

### 1. 单机等值

将整个风电场等值为单台风机，保留端口外特性。适用于电网级机电暂态仿真和稳态分析，忽略场内风速分布和控制差异。

### 2. 多机等值（分群等值）

基于风速、运行状态或电气距离将机组分群，每群等值为单台或少数等值机。

**DFIG 两步增强 K-means 分群法**（Xu 等 2026）：
- **第一步**：按有功功率输出和 LVRT 响应特性将全场机组分为两类——具有聚类特征的机组与不具有聚类特征的机组
- **第二步**：对后者应用增强 K-means 算法，采用 K-means++ 概率初始化、KD-Tree 高效检索（较传统方法搜索效率提升约 75%）和 Davies-Bouldin Index（DBI）自动确定最优聚类数
- 避免传统方法需手动指定初始中心和聚类数的缺陷
- 量化结果：仿真时间减少约 90%，精度保持 >98%（与详细模型对比）

### 3. 宽频等值模型

Hussein 等（2016）提出 Type-3（DFIG）风电场宽频等值模型，由两部分组成：
- **静态频率相关网络等值**（FDNE）：表征全场无源元件（集电线路、变压器）的宽频阻抗特性，响应外部扰动
- **动态低频等值模型**（DLFE）：表征聚合的 DFIG 机组、局部控制器和场站监控控制的集体动态

FDNE 仅代表线性元件，适用于外部扰动研究；DLFE 包含发电机和变流器的聚合动态及其控制回路。

### 4. 受控源解耦加速模型

针对大规模海上风电场的受控源解耦加速方法：将每台机组等值为受控电流源与等效阻抗的并联结构，实现节点削减和计算加速。

### 5. GPU 细粒度并行等值

将风电场拆分为三相节点/支路并行计算单元（GLIM 方法），在 GPU 上实现 100+ 风机实时仿真，加速比达 20-50 倍。

## 风电场 EMT 建模方法体系

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- 层级1: 输入层 -->
  <rect x="280" y="15" width="340" height="50" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="5"/>
  <text x="450" y="45" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#1e40af">风电场物理系统输入</text>
  <text x="450" y="60" text-anchor="middle" font-family="Arial" font-size="11" fill="#3b82f6">风速分布 · 机组类型 · 拓扑结构</text>
  
  <!-- 箭头1 -->
  <line x1="450" y1="65" x2="450" y2="90" stroke="#333" stroke-width="2"/>
  <polygon points="450,95 445,85 455,85" fill="#333"/>
  
  <!-- 层级2: 机组类型 -->
  <rect x="40" y="100" width="260" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="5"/>
  <text x="170" y="125" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#92400e">DFIG 双馈感应发电机</text>
  <text x="170" y="142" text-anchor="middle" font-family="Arial" font-size="11" fill="#b45309">RSC/GSC矢量控制 · Crowbar保护</text>
  <text x="170" y="155" text-anchor="middle" font-family="Arial" font-size="10" fill="#d97706">Mu 2019 · Xu 2026</text>
  
  <rect x="320" y="100" width="260" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="5"/>
  <text x="450" y="125" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#92400e">PMSG 永磁同步发电机</text>
  <text x="450" y="142" text-anchor="middle" font-family="Arial" font-size="11" fill="#b45309">全功率变流器 · 直驱结构</text>
  <text x="450" y="155" text-anchor="middle" font-family="Arial" font-size="10" fill="#d97706">固定导纳模型</text>
  
  <rect x="600" y="100" width="260" height="60" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="5"/>
  <text x="730" y="125" text-anchor="middle" font-family="Arial" font-size="13" font-weight="bold" fill="#92400e">异步风力发电机</text>
  <text x="730" y="142" text-anchor="middle" font-family="Arial" font-size="11" fill="#b45309">固定转速 · 结构简单</text>
  <text x="730" y="155" text-anchor="middle" font-family="Arial" font-size="10" fill="#d97706">早期风电场</text>
  
  <!-- 箭头2 -->
  <line x1="450" y1="160" x2="450" y2="190" stroke="#333" stroke-width="2"/>
  <polygon points="450,195 445,185 455,185" fill="#333"/>
  
  <!-- 层级3: 聚合方法 -->
  <rect x="30" y="200" width="200" height="55" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>
  <text x="130" y="220" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">单机等值</text>
  <text x="130" y="237" text-anchor="middle" font-family="Arial" font-size="10" fill="#15803d">端口外特性保留</text>
  <text x="130" y="250" text-anchor="middle" font-family="Arial" font-size="10" fill="#16a34a">电网级仿真</text>
  
  <rect x="250" y="200" width="200" height="55" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>
  <text x="350" y="220" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">多机等值（分群）</text>
  <text x="350" y="237" text-anchor="middle" font-family="Arial" font-size="10" fill="#15803d">K-means/LVRT分群</text>
  <text x="350" y="250" text-anchor="middle" font-family="Arial" font-size="10" fill="#16a34a">Xu 2026: 90%加速</text>
  
  <rect x="470" y="200" width="200" height="55" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>
  <text x="570" y="220" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">宽频等值 (FDNE+DLFE)</text>
  <text x="570" y="237" text-anchor="middle" font-family="Arial" font-size="10" fill="#15803d">Hussein 2016</text>
  <text x="570" y="250" text-anchor="middle" font-family="Arial" font-size="10" fill="#16a34a">宽频10Hz-1kHz</text>
  
  <rect x="690" y="200" width="180" height="55" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="5"/>
  <text x="780" y="220" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#166534">受控源解耦</text>
  <text x="780" y="237" text-anchor="middle" font-family="Arial" font-size="10" fill="#15803d">节点削减加速</text>
  <text x="780" y="250" text-anchor="middle" font-family="Arial" font-size="10" fill="#16a34a">大规模海上风电</text>
  
  <!-- 箭头3 -->
  <line x1="450" y1="255" x2="450" y2="285" stroke="#333" stroke-width="2"/>
  <polygon points="450,290 445,280 455,280" fill="#333"/>
  
  <!-- 层级4: 数值方法 -->
  <rect x="80" y="295" width="180" height="55" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2" rx="5"/>
  <text x="170" y="315" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#5b21b6">开关函数平均化</text>
  <text x="170" y="332" text-anchor="middle" font-family="Arial" font-size="10" fill="#7c3aed">Mu 2019: 简化PWM</text>
  <text x="170" y="345" text-anchor="middle" font-family="Arial" font-size="10" fill="#6d28d9">避免超越方程</text>
  
  <rect x="280" y="295" width="160" height="55" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2" rx="5"/>
  <text x="360" y="315" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#5b21b6">Crowbar等效模型</text>
  <text x="360" y="332" text-anchor="middle" font-family="Arial" font-size="10" fill="#7c3aed">受控电压源</text>
  <text x="360" y="345" text-anchor="middle" font-family="Arial" font-size="10" fill="#6d28d9">短路故障保护</text>
  
  <rect x="460" y="295" width="180" height="55" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2" rx="5"/>
  <text x="550" y="315" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#5b21b6">GPU SIMT并行</text>
  <text x="550" y="332" text-anchor="middle" font-family="Arial" font-size="10" fill="#7c3aed">Lin 2021: CPU-GPU异构</text>
  <text x="550" y="345" text-anchor="middle" font-family="Arial" font-size="10" fill="#6d28d9">~20×加速(8000WT)</text>
  
  <rect x="660" y="295" width="160" height="55" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2" rx="5"/>
  <text x="740" y="315" text-anchor="middle" font-family="Arial" font-size="12" font-weight="bold" fill="#5b21b6">平均值模型</text>
  <text x="740" y="332" text-anchor="middle" font-family="Arial" font-size="10" fill="#7c3aed">等效受控源</text>
  <text x="740" y="345" text-anchor="middle" font-family="Arial" font-size="10" fill="#6d28d9">保留控制动态</text>
  
  <!-- 箭头4 -->
  <line x1="450" y1="350" x2="450" y2="380" stroke="#333" stroke-width="2"/>
  <polygon points="450,385 445,375 455,375" fill="#333"/>
  
  <!-- 层级5: 输出 -->
  <rect x="280" y="390" width="340" height="50" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" rx="5"/>
  <text x="450" y="415" text-anchor="middle" font-family="Arial" font-size="14" font-weight="bold" fill="#5b21b6">等值模型输出 · EMT仿真结果</text>
  <text x="450" y="432" text-anchor="middle" font-family="Arial" font-size="11" fill="#6d28d9">并网点V-I特性 · 故障穿越响应 · 谐波特性</text>
  
  <!-- 层级标签 -->
  <text x="15" y="130" font-family="Arial" font-size="10" fill="#6b7280">机组类型</text>
  <text x="15" y="230" font-family="Arial" font-size="10" fill="#6b7280">聚合方法</text>
  <text x="15" y="325" font-family="Arial" font-size="10" fill="#6b7280">数值方法</text>
  
  <!-- 图例 -->
  <rect x="30" y="465" width="15" height="15" fill="#dbeafe" stroke="#2563eb"/>
  <text x="50" y="477" font-family="Arial" font-size="10" fill="#374151">物理输入</text>
  <rect x="150" y="465" width="15" height="15" fill="#fef3c7" stroke="#d97706"/>
  <text x="170" y="477" font-family="Arial" font-size="10" fill="#374151">机组类型</text>
  <rect x="270" y="465" width="15" height="15" fill="#dcfce7" stroke="#16a34a"/>
  <text x="290" y="477" font-family="Arial" font-size="10" fill="#374151">聚合方法</text>
  <rect x="400" y="465" width="15" height="15" fill="#f3e8ff" stroke="#7c3aed"/>
  <text x="420" y="477" font-family="Arial" font-size="10" fill="#374151">数值方法</text>
  <rect x="520" y="465" width="15" height="15" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="540" y="477" font-family="Arial" font-size="10" fill="#374151">输出结果</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 风电场EMT建模方法体系架构：物理输入→机组类型→聚合方法→数值方法→输出结果</p>

## 形式化表达

### 容量加权等效风速

风电场聚合后等效机组的容量加权风速为：

$$v_{\mathrm{eq}}=\sqrt[3]{\frac{\sum_i S_i v_i^3}{\sum_i S_i}}$$

其中 $S_i$ 为第 $i$ 台机组额定容量，$v_i$ 为该机组输入风速。该公式体现了风功率与风速的三次方关系，是风电场等值的基础约束之一。

### DFIG 定子磁链定向 dq 功率方程

定子磁链定向控制下，定子有功、无功功率表达为：

$$P_s = \frac{3L_m}{2L_s\omega_1\psi_s}i_{rq}$$

$$Q_s = \frac{3L_m\omega_1\psi_s}{2L_s}i_{rd} - \frac{3\omega_1\psi_s^2}{2L_s}$$

其中 $L_m$ 为互感，$L_s$ 为定子电感，$\psi_s$ 为定子磁链，$\omega_1$ 为同步转速，$i_{rd}, i_{rq}$ 分别为转子 d/q 轴电流。

### LVRT 故障期间有功/无功控制

DFIG 在 LVRT 期间，转子电流和主动功率参考值为：

$$i_{rq}^* = \min\left\{K_{ppr}\left(P_s^{fault}-P_s\right)+K_{ipr}\int\left(P_s^{fault}-P_s\right)dt,\ \sqrt{i_{r\lim}^2-\left(i_{rd}^*\right)^2}\right\}$$

$$P_s^{fault} = \min\left\{P_0,\ \frac{3L_m\omega_1\psi_s}{2L_s}\left(i_{r\lim}^2-\left(i_{rd}^*\right)^2\right)\right\}$$

其中 $K_{ppr}, K_{ipr}$ 为转子侧 PI 控制器参数，$i_{r\lim}$ 为 RSC 电流限值，$P_0$ 为故障前输出功率。

### 等值前后功率约束

集电网络等值要求等值前后损耗或 PCC 电压保持一致：

$$P_{\mathrm{loss,eq}} = P_{\mathrm{loss,detail}}, \qquad V_{\mathrm{PCC,eq}} \approx V_{\mathrm{PCC,detail}}$$

### 宽频等值模型结构

Hussein（2016）的 Type-3 风电场宽频等值模型结构为：

$$Y_{FDNE}(s) = \text{静态频率相关网络等值导纳}, \quad G_{DLFE}(s) = \text{动态低频等值传递函数}$$

两部分联合使用才能准确表征风电场在宽频扰动下的端口响应。

### K-means 聚类目标函数

Xu 等（2026）的增强 K-means 聚类采用组内平方和（WCSS）：

$$\text{WCSS} = \sum_{i=1}^K\sum_{x\in C_i}\|x-\mu_i\|^2$$

其中 $C_i$ 为第 $i$ 个聚类，$\mu_i$ 为该聚类质心。

### GPU 并行加速边界

Lin 等（2021）的 CPU-GPU 异构计算框架中，GPU 并行效率边界为：

$$N_{th} \approx 100 \text{ 台风机（DFIG）}, \quad N_{th} \approx 15 \text{ 级（MMC）}$$

当 DFIG 数量超过约 100 台或 MMC 电压等级超过约 15 级时，GPU 并行方能超越纯 CPU 效率。

## 关键技术挑战

### 1. 场内异构性导致的等值误差

同场机组可能处于不同运行状态（满发/部分出力/停机）、不同控制策略（LVRT 响应差异）、不同电气距离（相对于 PCC 的阻抗差异）。传统单机等值假设所有机组响应一致，但实际上风速三次方加权的等效风速仅在稳态分析中成立，动态过程中机间控制相互作用无法由单机等值保留。**量化边界**：多机等值将 100 台机组等值为 4-6 群时，仿真时间从小时级降至分钟级（Xu 2026），但故障后 200ms 内的暂态功率恢复轨迹误差可能达 5-15%。

### 2. 集电网络频变特性的保留与等值

集电网络含长距离海缆或埋地电缆时，其阻抗呈频率相关特性。在次同步谐振（SSR）和宽频振荡研究中，忽略频变效应会导致等值模型在 10Hz-1kHz 频段误差超过 5%。Hussein（2016）的 FDNE 模型虽然能在宽频范围内表征无源网络，但需要拟合频域阻抗数据，建模复杂度较高。

### 3. Crowbar 保护与变流器闭锁暂态的等值建模

DFIG 在电网短路期间，Crowbar 保护电路短接转子侧变流器，切换为定子侧磁链动态控制的异步机模式；故障清除后变流器重新闭锁投入。该过程包含非线性切换和暂态过程，Mu 等（2019）证明若忽略 Crowbar 动态，则转子电流和直流电压的故障后暂态误差显著增大。**等值难点**：Crowbar 的离散投切使等值模型不再能简单表示为线性时不变电路。

### 4. GPU 并行效率与内存带宽的矛盾

Lin 等（2021）的实验表明：当风电场规模不足（< 100 台 DFIG）时，GPU 并行因内存拷贝开销反而低于 CPU；但当规模足够大时，计算时间可减少至纯 CPU 的 1/20（8000 台风机场景）。挑战在于：**动态边界判定**——需要在线监测计算同质性，实时切换 CPU/GPU 处理模式。

### 5. LVRT 分群指标的自动化选择

传统 K-means 需要手动指定初始聚类中心和聚类数 $K$，Xu 等（2026）提出的增强 K-means 方法通过 DBI 自动优化 $K$，通过 K-means++ 概率初始化改善收敛性，KD-Tree 使数据搜索效率提升约 75%。但该方法针对 DFIG 风电场设计，对 PMSG 或混合类型风电场的适用性尚需验证。

## 量化性能边界

| 建模方法 | 适用场景 | 计算效率 | 精度/误差 | 代表数据 |
|---------|---------|---------|----------|---------|
| 单机等值 | 电网级机电暂态 | 最高（等值比 100:1） | 低（忽略场内差异） | 稳态潮流分析 |
| 传统 K-means 分群 | 并网点故障响应 | 较高（等值比 10-20:1） | 中等（误差 3-8%） | LVRT 验证 |
| 增强 K-means 两步法（Xu 2026） | 故障穿越动态 | 等值 90% 仿真时间减少 | >98% 精度保持 | 10 台风机分群验证 |
| FDNE+DLFE 宽频等值（Hussein 2016） | SSR/宽频振荡分析 | 中等 | <5% (10Hz-1kHz) | 串补电网 SSR |
| 开关函数平均化（Mu 2019） | DFIG 快速 EMT | 仿真步长放宽至 20-50μs | 与详细模型高度一致 | 1.5MW DFIG 验证 |
| GPU SIMT 并行（Lin 2021） | 实时/超实时仿真 | 8000WT 场景 ~20× 加速 | 与详细模型一致 | NVIDIA Tesla V100 |
| 受控源解耦加速 | 大规模海上风电 | 节点削减显著 | 待验证 | 海上风电工程 |

**CPU-GPU 效率边界**（Lin 2021）：
- DFIG 数量 < 100 台：CPU 效率更高
- DFIG 数量 > 100 台：GPU 效率开始超越 CPU
- 8000 DFIG + 401-level MMC：GPU 加速比约 20 倍

**宽频等值精度**（Hussein 2016）：
- 10Hz-1kHz 频段误差 < 5%
- 阶跃响应与详细模型高度吻合

**K-means 聚类效率**（Xu 2026）：
- KD-Tree 搜索：较传统方法减少 75% 数据搜索时间
- DBI 优化：自动确定最优聚类数，避免主观选择

## 适用边界与选择指南

**单机等值**：适用于大电网稳定性和规划分析，仅需保留并网点功率响应，忽略机组间动态和场内故障。

**多机等值（分群）**：适用于并网点电压跌落故障研究，需要保留场内机组 LVRT 响应差异的场景。推荐增强 K-means 两步法（Xu 2026），可自动优化聚类数且精度 >98%。

**宽频等值**：适用于串补电网次同步谐振（SSR）分析和宽频振荡研究，需要保留 10Hz-1kHz 频段响应的场景。需配合 FDNE 频域拟合和 DLFE 动态等值两部分。

**快速 EMT 等值**：适用于 DFIG 风电场机电暂态研究，需要较高仿真效率但保留 Crowbar 和变流器闭锁动态的场景。开关函数平均化方法可放宽步长至 20-50μs。

**GPU 并行**：适用于 100+ 台风机的大规模场站实时仿真，当硬件具备 GPU（NVIDIA Tesla V100 或更高）且仿真时长 > 1 秒时加速效果显著。

**混合策略**：对于同时含 DFIG 和 PMSG 的混合风电场，建议按机组类型分组后各自采用适用的等值方法，再通过受控源并联实现整体等值。

## 相关模型
- [[dfig-model]]
- [[pmsm-model]]
- [[synchronous-machine-model]]
- [[vsc-model]]
- [[vsc-hvdc]]

## 相关方法
- [[state-space-method]]
- [[average-value-model]]
- [[fixed-admittance]]
- [[coherency-clustering]]
- [[parallel-computing]]
- [[electromechanical-electromagnetic-hybrid-simulation]]

## 相关主题
- [[co-simulation]]
- [[real-time-simulation]]
- [[parallel-computing]]
- [[renewable-energy-integration]]
- [[vsc-hvdc]]

## 来源论文

| 论文 | 年份 | 贡献说明 |
|------|------|---------|
| Mu 等 - 双馈风力发电机组快速电磁暂态仿真模型 | 2019 | 开关函数平均化 + Crowbar 等效 + 预测校正调制量，1.5MW DFIG 验证 |
| Hussein 等 - A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies | 2016 | FDNE+DLFE 宽频等值框架，10Hz-1kHz 误差 <5% |
| Lin 等 - Adaptive Heterogeneous Transient Analysis of Wind Farm Integrated Comprehensive AC/DC Grids | 2021 | CPU-GPU 异构计算，100WT/15-level MMC 效率边界，8000WT 场景 ~20× 加速 |
| Xu 等 - An Enhanced K-means Two-step Clustering Method for Dynamic Equivalent Modeling of DFIG Wind Farms | 2026 | LVRT 特征 + KD-Tree + DBI 自动聚类，仿真时间减少 90%，精度 >98% |
| Guo 等 - Electromagnetic Transient Aggregation of Large-scale Doubly-fed Induction Wind Farm | 2025 | 解析聚合方法，DFIG 风电场 EMT 聚合 |
| an-aggregation-method-of-permanent-magnet-synchronous-wind-farms-for-electromech | 2023 | PMSG 风电场聚合方法 |
| modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag | 2025 | DFIG 高效实时 EMT 建模方法 |
| efficient-electromagnetic-transient-simulation-for-dfig-based-wind-farms-using-f | 2024 | DFIG 风电场高效 EMT 仿真 |
| fine-grained-optimal-allocation-of-wind-farm-decoupled-models-for-cpu-gpu-parall | 2025 | CPU-GPU 细粒度最优分配 |
| adaptive-heterogeneous-transient-analysis-of-wind-farm-integrated-comprehensive-. | 2021 | 风电场 AC/DC 网格自适应异构瞬态分析 |
| an-enhanced-k-means-two-step-clustering-method-for-dynamic-equivalent-modeling-o | 2026 | 增强 K-means 两步分群法 |