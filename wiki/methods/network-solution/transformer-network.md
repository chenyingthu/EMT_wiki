---
title: "变压器网络建模 (Transformer Network Modeling)"
type: method
tags: [transformer, network, modeling, equivalent-circuit, matrix, nodal-analysis, duality, magnetic-saturation]
created: "2026-05-02"
updated: "2026-05-19"
---

# 变压器网络建模 (Transformer Network Modeling)

## 定义与边界

变压器网络建模是在 EMT 或 EMTP 型仿真中，把变压器绕组、铁芯、漏磁、连接组别和端口网络关系转化为可求解电路方程的方法。它关注变压器如何进入节点导纳矩阵、伴随模型或多端口端口方程，而不是变压器制造设计的完整电磁场求解。

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 380" xmlns="http://www.w3.org/2000/svg">
  <!-- Layer 1: Input -->
  <rect x="310" y="10" width="280" height="50" rx="6" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="450" y="40" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">物理变压器 (输入)</text>
  <text x="450" y="56" text-anchor="middle" font-size="11" fill="#3b82f6">绕组柱 · 轭部 · 铁芯 · 杂散电容</text>

  <!-- Arrow 1-2 -->
  <line x1="450" y1="60" x2="450" y2="85" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#333"/></marker></defs>

  <!-- Layer 2: Core mechanisms (3 cards) -->
  <rect x="30" y="95" width="250" height="80" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="155" y="118" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">理想变比 + 漏抗</text>
  <text x="155" y="134" text-anchor="middle" font-size="10" fill="#15803d">匝比约束 · 功率守恒</text>
  <text x="155" y="150" text-anchor="middle" font-size="10" fill="#15803d">端口导纳矩阵 · 伴随模型</text>
  <text x="155" y="166" text-anchor="middle" font-size="10" fill="#15803d">$v_1=n v_2,\; i_2=-n i_1$</text>

  <rect x="325" y="95" width="250" height="80" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="450" y="118" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">磁饱和 + 对偶等效</text>
  <text x="450" y="134" text-anchor="middle" font-size="10" fill="#15803d">非线性磁化支路 · 渐近光滑</text>
  <text x="450" y="150" text-anchor="middle" font-size="10" fill="#15803d">$\tilde{L}_w^q(\lambda)$ · 励磁涌流</text>
  <text x="450" y="166" text-anchor="middle" font-size="10" fill="#15803d">漏感互感矩阵 · 多绕组支持</text>

  <rect x="620" y="95" width="250" height="80" rx="6" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="745" y="118" text-anchor="middle" font-size="13" font-weight="bold" fill="#166534">宽频端口模型</text>
  <text x="745" y="134" text-anchor="middle" font-size="10" fill="#15803d">频变导纳 $\mathbf{Y}_{tr}(s)$</text>
  <text x="745" y="150" text-anchor="middle" font-size="10" fill="#15803d">有理函数拟合 · RLC 综合</text>
  <text x="745" y="166" text-anchor="middle" font-size="10" fill="#15803d">操作过电压 · 高频谐振</text>

  <!-- Layer labels -->
  <text x="10" y="130" font-size="11" fill="#666" font-weight="bold">阻抗型</text>
  <text x="10" y="145" font-size="11" fill="#666">非线性</text>
  <text x="10" y="160" font-size="11" fill="#666">磁路型</text>

  <text x="280" y="130" font-size="11" fill="#666" font-weight="bold">对偶型</text>
  <text x="280" y="145" font-size="11" fill="#666">饱和/磁滞</text>
  <text x="280" y="160" font-size="11" fill="#666">多柱铁芯</text>

  <text x="575" y="130" font-size="11" fill="#666" font-weight="bold">端口型</text>
  <text x="575" y="145" font-size="11" fill="#666">黑箱等效</text>
  <text x="575" y="160" font-size="11" fill="#666">频域扫描</text>

  <!-- Arrow 2-3 -->
  <line x1="450" y1="175" x2="450" y2="200" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 3: Output -->
  <rect x="310" y="205" width="280" height="50" rx="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="450" y="232" text-anchor="middle" font-size="14" font-weight="bold" fill="#5b21b6">EMT 网络节点方程</text>
  <text x="450" y="248" text-anchor="middle" font-size="11" fill="#7c3aed">$[G]\mathbf{V}=\mathbf{I}$ · 改进增广节点法</text>

  <!-- Arrow 3-4 -->
  <line x1="450" y1="255" x2="450" y2="280" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Layer 4: Application scenarios -->
  <rect x="130" y="285" width="640" height="55" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="450" y="305" text-anchor="middle" font-size="13" font-weight="bold" fill="#92400e">应用场景</text>
  <text x="250" y="325" text-anchor="middle" font-size="11" fill="#b45309">故障电流计算</text>
  <text x="400" y="325" text-anchor="middle" font-size="11" fill="#b45309">合闸涌流 · 剩磁</text>
  <text x="550" y="325" text-anchor="middle" font-size="11" fill="#b45309">操作过电压</text>
  <text x="680" y="325" text-anchor="middle" font-size="11" fill="#b45309">换流站端口等值</text>

  <!-- Legend -->
  <rect x="10" y="300" width="12" height="12" fill="#dbeafe" stroke="#2563eb"/>
  <text x="26" y="310" font-size="10" fill="#666">输入</text>
  <rect x="10" y="316" width="12" height="12" fill="#dcfce7" stroke="#16a34a"/>
  <text x="26" y="326" font-size="10" fill="#666">建模方法</text>
  <rect x="10" y="332" width="12" height="12" fill="#ede9fe" stroke="#7c3aed"/>
  <text x="26" y="342" font-size="10" fill="#666">网络方程</text>
  <rect x="10" y="348" width="12" height="12" fill="#fef3c7" stroke="#d97706"/>
  <text x="26" y="358" font-size="10" fill="#666">应用</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 变压器网络建模方法体系架构：三层建模方法（阻抗型/对偶型/端口型）向 EMT 网络方程的映射</p>

本页把变压器看作网络元件和端口模型。若研究目标是铁芯饱和、内部故障或绕组局部电压，需要转向更详细的 [[transformer-model]]、[[multi-winding-transformer]] 或源页中的分布式磁路模型。若研究目标只是潮流或短路初始化，理想变比和漏抗模型可能足够，但不能用于高频暂态或内部应力结论。

## EMT 中的作用

变压器在 EMT 网络中通常承担以下角色：

- 在不同电压等级之间施加变比、相移和连接组别约束
- 用漏抗、绕组电阻和励磁支路影响故障电流、涌流和暂态恢复过程
- 通过相间耦合、零序通道和杂散电容影响开关过电压和高频振荡
- 在换流站、风电场、配电网和外部系统等值中作为端口导纳矩阵的一部分

因此，变压器网络建模的核心问题不是"模型越详细越好"，而是"目标暂态需要保留哪些端口和内部动态"。

## 核心机制

### 理想变比约束

最基本的双绕组理想变压器约束为：

$$

v_1 = n v_2,\quad i_2 = -n i_1

$$

其中 $n=N_1/N_2$ 是匝比，电流符号取决于端口方向约定。该约束保持瞬时功率平衡：

$$

v_1 i_1 + v_2 i_2 = 0

$$

实际网络建模通常在理想变比两侧加入绕组电阻、漏感、励磁支路、连接组别和可能的杂散电容。

### 节点导纳嵌入

带变比的线性支路可写成端口导纳关系：

$$

\begin{bmatrix} i_i \\ i_j \end{bmatrix} = \begin{bmatrix} y/a^2 & -y/a \\ -y/a & y \end{bmatrix} \begin{bmatrix} v_i \\ v_j \end{bmatrix}

$$

其中 $a$ 是从节点 $i$ 到节点 $j$ 的变比，$y$ 是串联支路导纳。若存在相移或三相连接组别，$a$ 应扩展为复变比或相域变换矩阵。多绕组变压器则需要用端口矩阵表示绕组间耦合，不能简单拆成互不相关的双绕组支路。

### 伴随模型

对漏感或励磁电感采用梯形积分时，可形成诺顿伴随支路：

$$

i^{n+1}=G_{\mathrm{eq}} v^{n+1}+i_{\mathrm{hist}}^{n}

$$

其中 $G_{\mathrm{eq}}$ 与步长和电感有关，$i_{\mathrm{hist}}^{n}$ 包含上一时刻电压电流历史。非线性励磁支路需要在每个时间步更新增量导纳或通过迭代求解。

### 磁饱和与对偶等效电路

基于 Shafieipour 2020 的对偶原理灰箱建模方法，铁芯各分段（绕组柱 $w$、轭部 $y$、外柱 $o$）的非线性磁化电感解析表达式为：

$$

\tilde{L}_\alpha^q(\lambda) = \frac{V_c}{j\omega} \left[ \pm \left( \frac{\sqrt{(-\lambda - \lambda_{0\alpha})^2 + 4d_\alpha L_{\alpha air}} - \lambda - \lambda_{0\alpha}}{2L_{\alpha air}} - \frac{d_\alpha}{\lambda_{0\alpha}} \right) \pm \frac{D_\alpha}{2} \right]^{-1}

$$

其中 $V_c$ 为铁芯参考电压（通常取各绕组额定电压最小值），$\lambda_{0\alpha}$ 为各分段饱和磁链阈值，$L_{\alpha air}$ 为空气芯电感，$d_\alpha$ 和 $D_\alpha$ 为磁滞回线参数。

多绕组间的互感矩阵由短路试验漏感直接解析计算：

$$

M_{i,j} = \frac{1}{2}(L_{i,j+1} + L_{i+1,j} - L_{i,j} - L_{i+1,j+1})

$$

该方法支撑任意数量绕组（含分接头）的漏感网络构建，已验证可稳定支持最多 12 个绕组的任意组合。

膝点磁链阈值与标幺值膝点电压的关系为：

$$

\lambda_{0w} = k_w \cdot \frac{V_c}{\omega}

$$

其中 $k_w$ 为绕组柱膝点电压（合理工程区间 $1.0$~$1.25$ pu），$\omega$ 为额定角频率。

关键工程参数约束：空气芯电感 $L_{air}$ 合理区间为 $0.1$~$0.3$ pu（偏离此范围指示参数提取错误），短路漏抗仿真误差可控制在 $<0.1\%$。

### 宽频端口模型

当绕组杂散电容、频变损耗或高频谐振影响结果时，端口关系可写成：

$$

\mathbf{i}(s)=\mathbf{Y}_{\mathrm{tr}}(s)\mathbf{v}(s)

$$

$\mathbf{Y}_{\mathrm{tr}}(s)$ 可由测量、详细物理模型或频率扫描得到，再用有理函数和 RLC 网络综合进入 EMT。该模型适合端口暂态研究，但不能提供绕组内部任意点电压，除非模型本身保留内部节点。

## 分类与变体

| 模型层级 | 主要内容 | 适合用途 | 主要限制 |
|----------|----------|----------|----------|
| 理想变压器 | 匝比、相移、功率守恒 | 电压等级接口、标幺化、简化网络 | 无损耗、无漏磁、无饱和 |
| 漏抗加励磁支路 | 绕组电阻、漏感、励磁电感和铁损 | 故障、合闸、常规 EMT 网络 | 高频电容和内部空间分布不足 |
| 三相耦合模型 | 连接组别、相间互感、零序路径 | 不平衡、开断过电压、接地故障 | 需要可靠的序参数或耦合矩阵 |
| 多绕组矩阵模型 | 多端口阻抗或导纳矩阵 | 自耦、三绕组、换流变压器 | 参数归算和端口方向容易出错 |
| 对偶等效电路模型 | 非线性磁化支路、互感漏感网络、渐近饱和函数 | 合闸涌流、剩磁、多柱铁芯饱和 | 零序漏感难以精确匹配 |
| 宽频端口模型 | 频率相关 $\mathbf{Y}(s)$ 或 RLC 网络 | 操作过电压、高频谐振、黑箱端口等值 | 不直接给内部绕组电压 |

## 适用边界与失败模式

变压器网络模型的常见失效边界包括：

- 用理想变压器或工频漏抗模型研究高频操作过电压，忽略杂散电容和频变损耗
- 在三相不平衡或接地故障中忽略零序磁通通道和连接组别
- 把多绕组短路试验参数转换为星形等值时出现负漏抗，却未检查数据一致性和基准换算
- 饱和支路只在稳态附近校准，却用于大涌流、直流偏磁或铁磁谐振结论
- 宽频端口导纳拟合后未检查稳定性和无源性，连接到 EMT 网络后出现非物理振荡
- 用端口黑箱模型推断绕组内部绝缘应力，这是模型输出边界之外的结论
- 对偶等效电路模型忽略零序漏感（任意绕组零序漏感约束问题尚未解决）

## 量化性能边界

| 建模层级 | 精度 | 典型误差 | 验证场景 | 代表性来源 |
|----------|------|----------|----------|------------|
| 漏抗加励磁支路 | 工业级 | 短路漏抗 <0.1% | 50 MVA 三铁芯短路试验 | Shafieipour 2020 |
| 对偶等效电路 | 工业级 | 励磁电流峰值误差 <2% | 多饱和度开路试验 | Shafieipour 2020 |
| 磁滞/涌流模型 | 经验级 | 涌流峰值 $6$~$12 I_n$ | 含剩磁合闸涌流 | Shafieipour 2020 |
| 宽频端口模型 | 频域精度 | 依赖拟合质量 | 操作过电压/高频谐振 | 端口频率扫描 |
| 伴随模型 | 步长依赖 | 梯形积分稳定 | 故障电流/暂态恢复 | 通用 EMT 验证 |

关键参数合理区间：空气芯电感 $L_{air}\in[0.1,0.3]$ pu（偏离提示参数错误），膝点电压 $k_w\in[1.0,1.25]$ pu（超范围易数值发散）。

## 相关页面

- [[ideal-transformer-equivalent]] 解释理想匝比约束，是本页最简层级
- [[equivalent-circuit-method]] 提供从物理元件到端口电路的通用方法
- [[norton-equivalent]] 和 [[companion-model]] 解释 EMT 时域求解中常用的电流源并联导纳形式
- [[detailed-equivalent-model]] 覆盖宽频端口等值和模型降阶，可用于变压器或外部网络
- [[magnetic-saturation-modeling]] 关注非线性励磁支路和饱和曲线
- [[converter-transformer-model]] 是换流站场景下的专门模型页
- [[nodal-admittance-matrix]] 与 [[nodal-analysis]] 是变压器进入网络方程的数值基础
- [[multi-winding-transformer]] 覆盖三绕组、自耦变压器和多绕组的端口矩阵建模

## 来源论文

- [[application-of-duality-based-equivalent-circuits-for-modeling-multilimb-transfor]] — Shafieipour 2020, 对偶原理多铁芯变压器灰箱模型，短路漏抗误差<0.1%，励磁涌流6~12倍额定电流，50 MVA/390 MVA工业验证
- [[dual-reversible-transformer-model-for-the-13&14]] — 对偶可逆变压器模型，用于13/14节点系统

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*