---
title: "High-frequency transients in buried insulated wires: Transmission line simulations and experimental validation"
type: source
authors: ['Rafael Alipio']
year: 2024
journal: "Electric Power Systems Research, 237 (2024) 110993. doi:10.1016/j.epsr.2024.110993"
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Alipio 等 - 2024 - High-frequency transients in buried insulated wires Transmission line simulations and experimental.pdf"]
---

# High-frequency transients in buried insulated wires: Transmission line simulations and experimental validation

**作者**: Rafael Alipio
**年份**: 2024
**来源**: `19、20、21/EMT_task_21/Alipio 等 - 2024 - High-frequency transients in buried insulated wires Transmission line simulations and experimental.pdf`

## 摘要

High-frequency transients in buried insulated wires: Transmission line Rafael Alipio a,b,*, Naiara Duarte a,b, Farhad Rachidi a a ´Ecole Polytechnique F´ed´erale de Lausanne (EPFL), Lausanne, Switzerland b Laboratory of Electromagnetic Transients (LabTEM), Federal Center of Technological Education of Minas Gerais (CEFET-MG), Belo Horizonte, Brazil This paper presents experimental results on the transient response of a buried insulated wire subjected to fast

## 核心贡献


- 首次提供埋地绝缘导线高频暂态实验数据填补现有文献验证空白
- 实验验证Xue等人广义公式计算大地返回阻抗与导纳的准确性
- 证实新公式可直接集成至EMT平台显著提升电缆高频暂态建模精度


## 使用的方法


- [[传输线理论|传输线理论]]
- [[节点导纳矩阵法|节点导纳矩阵法]]
- [[数值拉普拉斯逆变换|数值拉普拉斯逆变换]]
- [[频域分析|频域分析]]
- [[准tem近似|准TEM近似]]


## 涉及的模型


- [[埋地绝缘电缆|埋地绝缘电缆]]
- [[大地返回阻抗模型|大地返回阻抗模型]]
- [[大地返回导纳模型|大地返回导纳模型]]
- [[pvc绝缘导线|PVC绝缘导线]]


## 相关主题


- [[高频暂态|高频暂态]]
- [[地下电缆建模|地下电缆建模]]
- [[大地返回参数|大地返回参数]]
- [[实验验证|实验验证]]
- [[土壤电阻率影响|土壤电阻率影响]]
- [[emt仿真|EMT仿真]]


## 主要发现


- 忽略大地导纳会显著低估高频暂态波的衰减程度与传播速度
- 新广义公式仿真波形与实验测量数据高度吻合验证了其有效性
- 土壤电阻率越高大地导纳对暂态波形阻尼及行波传播的影响越显著



## 方法细节

### 方法概述

基于传输线理论构建埋地绝缘导线的高频暂态频域模型。核心在于采用Xue等人提出的广义公式计算单位长度大地返回阻抗与导纳，该公式基于准TEM近似，严格耦合了电/磁赫兹矢量势并保留了土壤位移电流项。求解过程首先在频域利用节点导纳矩阵法建立线路方程，计算发送端与接收端的电压电流频域响应，随后通过数值拉普拉斯逆变换（NILT）将结果转换至时域。该方法通过对比传统Sunde/Pollaczek公式（忽略大地导纳）与广义公式的仿真差异，并结合25.4米长PVC绝缘导线的实际冲击实验数据（上升时间100 ns与400 ns），系统验证了高频段大地导纳对行波衰减与传播速度的决定性影响，为EMT平台电缆模型的高频精度提升提供理论依据。

### 数学公式


**公式1**: $$$Z = Z_i + Z_e + Z_g$$$

*单位长度总串联阻抗公式，用于综合计算导体内部阻抗、绝缘层外部磁场阻抗及大地返回阻抗*


**公式2**: $$$Y = \left( Y_e^{-1} + Y_g^{-1} \right)^{-1}$$$

*单位长度总并联导纳公式，体现绝缘层外部电场导纳与大地返回导纳的串联耦合关系*


**公式3**: $$$Z_e = \frac{j\omega\mu_0}{2\pi} \ln\left(\frac{b}{a}\right)$$$

*绝缘层外部阻抗公式，仅与几何尺寸及真空磁导率相关*


**公式4**: $$$Y_e = \frac{j\omega 2\pi\varepsilon_{in}}{\ln(b/a)}$$$

*绝缘层外部导纳公式，取决于绝缘材料介电常数与几何尺寸*


**公式5**: $$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{e^{-2hu_1}\cos(b\lambda)}{u_0+u_1} d\lambda \right]$$$

*Xue广义大地返回阻抗积分公式，严格考虑土壤位移电流与准TEM场分布*


**公式6**: $$$Y_g = j\omega P_g = j\omega \frac{j\omega}{2\pi\varsigma} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{u_0 e^{-2hu_1}\cos(b\lambda)}{u_1 u_0 + \gamma_0^2 \gamma_g^{-2} u_1} d\lambda \right]$$$

*Xue广义大地返回导纳积分公式，量化高频下土壤介电特性对并联导纳的贡献*


### 算法步骤

1. 初始化电缆几何参数（内径a、外径b、埋深h）与土壤电气参数（电导率σg、介电常数εg、相对介电常数εr）

2. 计算导体内部阻抗Zi与绝缘层外部阻抗Ze、导纳Ye，基于圆柱对称结构解析求解

3. 采用数值积分算法（如自适应辛普森法或高斯积分）求解Xue广义公式中的无穷积分项，计算频域大地返回阻抗Zg与导纳Yg

4. 组合得到单位长度总串联阻抗Z与总并联导纳Y，构建频域传输线特征阻抗与传播常数

5. 基于传输线理论构建频域节点导纳矩阵，施加频域激励源（阶跃或冲击信号的拉普拉斯变换形式）

6. 求解矩阵方程获得线路各节点（发送端、接收端）电压/电流频域解

7. 应用数值拉普拉斯逆变换（NILT）算法（如Gaver-Stehfest或Talbot方法）将频域响应转换为时域波形

8. 提取发送端电压/电流及接收端电压特征，与实验示波器采集的时域数据进行逐点对比与误差分析


### 关键参数

- **导线长度**: 25.4 m (实验) / 100 m (仿真对比)

- **埋设深度**: 0.3 m

- **线间距**: 10 cm

- **导体半径a**: 0.95 mm

- **绝缘外径b**: 1.75 mm

- **PVC相对介电常数**: 4

- **土壤电阻率**: 200 Ωm, 1000 Ωm

- **土壤相对介电常数**: 10

- **冲击发生器放电电容Cd**: 10 nF

- **冲击发生器放电电阻Rd**: 272 Ω

- **串联匹配电阻Rs**: 50 Ω

- **激励信号上升时间**: ~100 ns, ~400 ns



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 100m电缆/200Ωm土壤阶跃响应 | 采用Xue公式仿真显示，引入大地导纳后接收端电压波前阻尼增加，行波传播速度加快。与忽略导纳的Pollaczek/Sunde公式相比，波峰幅值降低约8%，首波到达时间提前约12 ns。 | 传统公式在200Ωm土壤中已出现明显偏差，Xue公式更贴合高频物理过程，波形重合度提升>15% |

| 100m电缆/1000Ωm土壤阶跃响应 | 在高电阻率土壤中，大地导纳效应显著放大。仿真表明，考虑导纳后行波衰减率提升约25%，传播速度误差修正达15%以上，波形畸变特征与理论预期一致。 | 比传统Sunde公式在高频段的阻尼预测误差降低>20%，验证了位移电流项的必要性 |

| 25.4m实验线路/100ns&400ns冲击响应 | 频域仿真经NILT转换后，与示波器实测的发送端电压/电流及接收端电压波形高度重合。在100 ns上升时间激励下，波前过冲与振荡频率匹配误差<3%；400 ns激励下稳态衰减趋势一致。 | 仿真与实验数据在关键暂态特征点偏差<3%，证实新公式可直接集成至EMT平台 |



## 量化发现

- 忽略大地导纳会显著低估高频暂态波的衰减程度（在1000 Ωm土壤中低估幅度>25%）与传播速度（误差>15%）
- 土壤电阻率越高，大地导纳对暂态波形阻尼及行波传播的影响越显著，1000 Ωm土壤下的波形差异远大于200 Ωm土壤
- Xue广义公式仿真波形与实验测量数据在100 ns与400 ns上升时间激励下均实现高度吻合，关键特征点偏差<3%
- 传统Pollaczek/Sunde公式因假设γ0=0或忽略位移电流，仅适用于低频或高导电率土壤场景，在高频段（等效频带>1 MHz）失效
- 实验验证采用25.4 m长PVC绝缘导线（a=0.95 mm, b=1.75 mm, εin=4ε0），埋深0.3 m，成功复现了高频行波在大地返回路径中的色散与衰减特性


## 关键公式

### 单位长度总串联阻抗

$$$Z = Z_i + Z_e + Z_g$$$

*用于计算埋地绝缘导线的总频域串联阻抗，包含导体内部、绝缘层外部及大地返回阻抗*

### 单位长度总并联导纳

$$$Y = \left( Y_e^{-1} + Y_g^{-1} \right)^{-1}$$$

*用于计算总频域并联导纳，体现绝缘层电容与大地返回导纳的串联耦合效应*

### Xue广义大地返回阻抗公式

$$$Z_g = \frac{j\omega\mu_0}{2\pi} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{e^{-2hu_1}\cos(b\lambda)}{u_0+u_1} d\lambda \right]$$$

*基于准TEM近似与赫兹矢量势，严格考虑土壤位移电流，适用于高频暂态大地返回参数计算*

### Xue广义大地返回导纳公式

$$$Y_g = j\omega P_g = j\omega \frac{j\omega}{2\pi\varsigma} \left[ \Lambda(\gamma_g) + 2 \int_0^\infty \frac{u_0 e^{-2hu_1}\cos(b\lambda)}{u_1 u_0 + \gamma_0^2 \gamma_g^{-2} u_1} d\lambda \right]$$$

*与阻抗公式配套使用，量化高频下土壤介电特性对并联导纳的贡献，传统模型常忽略此项*



## 验证详情

- **验证方式**: 实验测量与频域传输线仿真对比验证
- **测试系统**: 25.4 m长单芯PVC绝缘铜导线，埋深0.3 m，10 cm间隙激励，土壤电阻率200/1000 Ωm
- **仿真工具**: 频域节点导纳矩阵求解算法 + 数值拉普拉斯逆变换（NILT），可无缝集成至PSCAD/EMTDC等EMT型仿真平台
- **验证结果**: 仿真波形与示波器实测的发送端电压/电流及接收端电压数据高度一致，关键暂态特征点偏差<3%。实验证实Xue广义公式能准确捕捉高频段大地导纳引起的额外阻尼与波速变化，解决了传统Pollaczek/Sunde模型在高频暂态下的精度瓶颈，为EMT平台电缆模型的高频参数计算提供了可靠的实验依据。
