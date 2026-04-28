---
title: "线路换相换流器 (LCC)"
type: model
tags: [lcc, hvdc, thyristor, line-commutated, converter]
created: "2026-04-14"
---

# 线路换相换流器 (LCC)

## 概述

线路换相换流器（Line-Commutated Converter, LCC）是传统高压直流输电（HVDC）的核心设备。与电压源换流器（VSC）不同，LCC使用晶闸管作为开关器件，依赖交流电网电压实现换相。

## 主要特点

- 晶闸管开关器件，不可控关断
- 依赖交流系统提供换相电压
- 换相失败是主要故障模式
- 只能向有源网络输电
- 大容量、远距离输电经济性好

## EMT建模方法

### 1. 详细换相模型
- 每个晶闸管单独建模
- 精确表征换相过程
- 适用于换相失败分析

### 2. 平均值模型
- 换相周期平均化
- 忽略开关细节
- 适用于系统级暂态仿真

### 3. 开关函数模型
- 使用开关函数表征换相
- 兼顾精度和效率
- 适用于混合仿真

## 主要故障模式

### 换相失败
- 交流电压跌落导致换相不成功
- 直流电压崩溃
- 无功功率突增
- 是LCC-HVDC最严重的故障

### 直流侧故障
- 直流线路短路
- 直流电流激增
- 需要快速保护动作

## 定义与边界

LCC 模型描述基于晶闸管、依赖交流系统换相的高压直流换流器。它与 [[vsc-model|VSC 模型]] 的边界在于 LCC 需要较强交流电压支撑，控制变量主要围绕触发角、熄弧角和直流电流；VSC 则通过自换相器件独立控制有功/无功。用于 EMT 时，LCC 页面应说明换相过程、阀组等值、控制保护接口和交流系统强度，而不是只给出平均功率方程。

该模型适合常规 HVDC、换相失败、交直流故障和多馈入相互作用研究。若研究对象是高频开关谐波、构网控制或 MMC 内部子模块暂态，应转向 [[vsc-model]]、[[mmc-model]] 或 [[average-value-model|平均值模型]]。

## 代表性来源与内部链接

代表性来源包括 [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Networks]]、[[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Failure]]、[[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algorithm for LCC-HVDC converters]] 和 [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulation for control design]]。相关主题包括 [[co-simulation]]、[[network-equivalent]]、[[nodal-analysis]] 和 [[vsc-hvdc]]。

## 相关方法
- [[average-value-model]]
- [[nodal-analysis]]

## 相关主题
- [[co-simulation]]
- [[vsc-hvdc]]
- [[mmc-model]]


## 论文方法分析
> 基于 4 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 多区域戴维南等效(MATE) | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 多速率联合仿真 | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| MATE传输线模型(MATE-TLM) | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 虚拟阻抗控制策略 | 1 | A multi-area Thevenin equivalent based multi-rate co-simulation for co |
| 理想开关表示法 | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 拓扑分解法（主网络与阀级辅助网络） | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 结构稳定求解算法 | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 自适应时间步长控制策略 | 1 | A topology-based simplified dynamic model and solving algorithm for LC |
| 参数化平均值建模(PAVM) | 1 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 正负序分量分析 | 1 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 平均值建模扩展 | 1 | Average-Value Modeling of Line-Commutated AC-DC Converters With Unbala |
| 参数化平均值建模（PAVM） | 1 | Average-Value Modeling of Line-Commutated Inverter Systems With Commut |
| 电磁暂态（EMT）仿真 | 1 | Average-Value Modeling of Line-Commutated Inverter Systems With Commut |
| 自动故障检测技术 | 1 | Average-Value Modeling of Line-Commutated Inverter Systems With Commut |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| LCC高压直流输电系统 | 1 |
| 交直流混合电网 | 1 |
| 传输线 | 1 |
| LCC-HVDC换流器 | 1 |
| TBSD（基于拓扑的简化动态模型） | 1 |
| 线换相AC-DC变换器(LCC/LCR) | 1 |
| 详细开关模型 | 1 |
| 电网换相逆变器（LCI） | 1 |
| LCC-HVDC输电系统 | 1 |
| 电力电子开关器件 | 1 |
### 验证方式分布
- **仿真**: 1 篇
- **仿真对比**: 1 篇
- **实验与仿真对比**: 1 篇
- **仿真/对比**: 1 篇
## 技术演进脉络
### 2019年 (1篇)
- **A multi-area Thevenin equivalent based multi-rate co-simulation for control desi**
  - 💡 将MATE多速率联合仿真技术与虚拟阻抗控制策略深度融合，为实用LCC HVDC系统提供了兼顾高精度、高效率仿真与换相失败抑制的一体化解决方案。
  - 提出基于MATE的多速率联合仿真框架，解决传统模型无法兼顾精度与效率的问题。
  - 构建MATE传输线模型并引入加速技术，显著提升大规模电网电磁暂态仿真效率。
### 2021年 (1篇)
- **Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne**
  - 💡 将参数化平均值建模扩展至交流不平衡工况，通过显式解析正负序谐波与直流纹波关系，实现高精度与高计算效率的统一。
  - 将参数化平均值建模(PAVM)方法扩展至交流电网不平衡工况下的LCC仿真。
  - 建立了交流侧正负序谐波与直流侧纹波相对于电网不平衡度的解析关系。
### 2022年 (1篇)
- **Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail**
  - 💡 首次将参数化平均值建模与自动故障检测相结合，为含换相失败故障的LCC-HVDC系统提供了一种高精度、低计算成本的EMT仿真方法。
  - 将参数化平均值建模（PAVM）方法从交流-直流整流器成功扩展至直流-交流逆变器系统。
  - 在平均值模型框架内首次引入并准确表征了开关器件的换相失败故障动态。
### 2025年 (1篇)
- **A topology-based simplified dynamic model and solving algorithm for LCC-HVDC con**
  - 💡 提出融合拓扑分解、定维矩阵求解与自适应步长的TBSD模型，有效解决了LCC-HVDC换相失败仿真中计算效率与阀级动态精度难以兼顾的难题。
  - 提出基于拓扑的简化动态（TBSD）模型，通过理想开关保留晶闸管离散开关特性。
  - 开发结构稳定求解算法，在不同开关拓扑下保持矩阵维度一致以提升求解稳定性。
## 关键发现汇总
- [2019] **A multi-area Thevenin equivalent based multi-rate co-simulat**: 所提MATE多速率联合仿真方法在保持电磁暂态精度的同时大幅降低了计算耗时。
- [2019] **A multi-area Thevenin equivalent based multi-rate co-simulat**: 虚拟阻抗控制策略成功减少了换相失败发生概率并缩短了直流电压与功率的恢复时间。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 所提PAVM在不平衡工况下能高精度重构交流侧与直流侧电压/电流波形。
- [2021] **Average-Value Modeling of Line-Commutated AC-DC Converters W**: 相比传统详细开关模型，新模型的计算速度显著提升，大幅降低仿真耗时。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 所提PAVM能够准确预测换相失败事件，并重构出与详细开关模型高度一致的交直流侧波形。
- [2022] **Average-Value Modeling of Line-Commutated Inverter Systems W**: 相比传统详细开关模型，该平均值模型在系统级多场景仿真中实现了更高的计算效率。
- [2025] **A topology-based simplified dynamic model and solving algori**: TBSD模型能够精确复现LCC-HVDC换流器的换相失败动态过程。
- [2025] **A topology-based simplified dynamic model and solving algori**: 相比传统高精度EMT模型，该模型在维持同等精度的前提下显著提升了计算效率。
- [2025] **A topology-based simplified dynamic model and solving algori**: 自适应步长策略有效平衡了仿真速度与暂态波形跟踪精度。
## 来源论文

| 论文 | 年份 |
|------|------|
| [[average-value-modeling-of-line-commutated-ac-dc-converters-with-unbalanced-ac-ne|Average-Value Modeling of Line-Commutated AC-DC Converters With Unbalanced AC Ne]] | 2021 |
| [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail|Average-Value Modeling of Line-Commutated Inverter Systems With Commutation Fail]] | 2022 |
| [[a-multi-area-thevenin-equivalent-based-multi-rate-co-simulation-for-control-desi|A multi-area Thevenin equivalent based multi-rate co-simulation for control desi]] | 2019 |
| [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con|A topology-based simplified dynamic model and solving algorithm for LCC-HVDC con]] | 2025 |

## 深度增强内容

 基于提供的25篇高水平文献，为LCC-HVDC模型生成以下深度增强内容：

---

## 1. 各类模型数学描述

### 1.1 详细开关模型（Detailed Switching Model）

详细模型将每个晶闸管视为理想开关或双值电阻（导通时 $R_{on} \approx 0$，关断时 $R_{off} \to \infty$）。换相过程由以下微分方程描述：

**换相阶段微分方程**：
$$
L_c\frac{di_k}{dt} + R_c i_k = v_k(t) - v_{k+1}(t), \quad k=1,2,...,6
$$

其中 $L_c$ 为换相电感，$v_k$ 为阀侧电压。换相成功判据为关断角满足：
$$
\gamma = \arccos\left(\frac{\sqrt{2}I_d X_c}{V_{LL}} + \cos\beta\right) > \gamma_{min}
$$

**拓扑分解形式（TBSD）**：
为保持矩阵维度恒定，采用结构稳定求解算法，将网络分解为主网络（恒定拓扑）与阀级辅助网络（时变拓扑）：

$$
\begin{bmatrix} G_{main} & 0 \\ 0 & G_{aux} \end{bmatrix} 
\begin{bmatrix} V_{main} \\ V_{aux} \end{bmatrix} = 
\begin{bmatrix} I_{main} \\ I_{aux} \end{bmatrix}
$$

其中主网络在6脉动系统中恒定为 $3\times3$ 矩阵，12脉动系统为 $5\times5$ 矩阵，彻底消除开关动作导致的矩阵重构开销。

### 1.2 参数化平均值模型（Parametric Average-Value Model, PAVM）

PAVM通过代数方程描述换相周期内的平均行为，消除开关细节。直流侧电压-电流关系为：

$$
v_d = \frac{3\sqrt{2}}{\pi}V_{LL}\cos\alpha - \frac{3}{\pi}X_c i_d + \sum_{h=6k\pm1} \Delta v_{d,h}
$$

**交流不平衡工况扩展**：
当交流电网不平衡时，引入正负序分量分解：

$$
v_{abc} = v_{abc}^{(1)} + v_{abc}^{(-1)} + \sum_{|h|>1} v_{abc}^{(h)}
$$

直流纹波与谐波电压的解析关系：
$$
\Delta v_d^{(h)} = \frac{3\sqrt{2}}{2\pi} \left[ V_{+}^{(1)}e^{j\theta_+} + V_{-}^{(-1)}e^{-j\theta_-} \right] \cdot \frac{Z_{dc}(jh\omega_0)}{Z_{dc}(jh\omega_0) + Z_{load}}
$$

**换相失败检测**：
引入临界电压跌落阈值函数：
$$
g_{crt}(\alpha, i_d) = \frac{V_{dip}}{V_{nom}} \cdot \frac{1}{1+k_\alpha(\alpha-\alpha_0)} \cdot \frac{I_{rated}}{i_d}
$$

当 $g_{crt} < g_{th}$ 时判定换相失败，模型自动切换至故障模式，采用电流源接口技术保持数值稳定性。

### 1.3 动态相量模型（Dynamic Phasor Model, DPM）

动态相量法将状态变量展开为傅里叶级数，保留 $k=0,\pm1$ 分量：

$$
x(t) = \sum_{k=-1}^{1} X_k(t)e^{jk\omega_0 t}
$$

**改进DPM（考虑换相电流正弦变化）**：
传统准稳态模型假设换相期间电流线性变化，改进模型考虑正弦特性：

$$
i_v(t) = I_s\sin(\omega t + \phi), \quad t \in [t_0, t_0+\mu/\omega]
$$

其中 $\mu$ 为换相角。由此导出换相电压-电流关系：

$$
\frac{dI_d}{dt} = \frac{1}{L_{eq}}\left( V_{d0}\cos\alpha - V_{d0}\cos(\alpha+\mu) - R_{eq}I_d \right)
$$

**接口模型**：
采用动态相量形式的诺顿等效实现EMT与机电暂态混合仿真：

$$
I_{int}(t) = \sum_{k=-1}^{1} I_k(t)e^{jk\omega_0 t}, \quad Y_{int} = \text{diag}(Y_0, Y_1, Y_{-1})
$$

### 1.4 多速率接口模型（MATE-Based Multi-Rate Model）

基于多区域戴维南等值（MATE）的传输线模型（MATE-TLM）实现交直流解耦：

$$
V_{Th} = Z_{Th}I_{TL} + V_{hist}
$$

其中 $Z_{Th}$ 为诺顿等值阻抗，$V_{hist}$ 为历史电压源。接口传输线模型满足：

$$
I_{TL}(t) = Y_{TL}V_{TL}(t-\tau) + I_{hist}(t-\tau)
$$

$\tau$ 为传播时延，允许交流侧采用大步长 $\Delta T = n\cdot\Delta t$（通常 $n=10$，$\Delta t=50\,\mu\text{s}$，$\Delta T=500\,\mu\text{s}$），而直流侧保持小步长。

---

## 2. 仿真参数参考表

| 参数类别 | 详细开关模型 | PAVM | TBSD | 动态相量模型 | 多速率MATE |
|---------|-------------|------|------|-------------|-----------|
| **典型步长** | 10–20 μs | 100 μs–2 ms | 50–200 μs（自适应） | 100–500 μs | EMT: 50 μs, TS: 500 μs |
| **矩阵维度** | 时变（12脉动约24×24） | 降阶（约6×6） | 恒定（6脉动3×3，12脉动5×5） | 缩减70–80% | 子网独立求解 |
| **计算速度提升** | 基准 | 100–1000× | 单次求解降低70%计算量 | 85–90%（较EMT） | 150–160×（交流侧大步长） |
| **电压/电流误差** | <0.1% | <1%（基频），<0.5%（直流纹波） | <0.8% | <1.5%（基频），<2%（直流） | 平均误差0.0084–0.012 |
| **谐波范围** | 全频带（开关频率） | 至2kHz（可配置） | 低频至中频 | 基频±1次谐波 | 取决于子网设置 |
| **换相失败捕捉** | 精确（μs级） | 支持（自动检测） | 精确（理想开关） | 支持（时序偏差<0.5ms） | 支持（延迟误差<1ms） |
| **实时性** | 难以实现 | 支持 | 支持（配合自适应步长） | 支持 | 支持（CPU-FPGA协同） |

**关键阈值参数**：
- **关断角安全裕度**：$\gamma_{min} = 7^\circ \sim 9^\circ$
- **换相失败检测阈值**：$g_{th}$ 通常取0.3–0.5（标幺值）
- **自适应步长放大系数**：稳态时可达暂态步长的5–8倍
- **虚拟阻抗值**：$Z_{vir} = R_{vir} + j\omega L_{vir}$，通常 $R_{vir}=0.1\,\text{p.u.}, L_{vir}=0.05\,\text{p.u.}$

---

## 3. 模型选择指南

| 应用场景 | 推荐模型 | 配置建议 | 关键考量 |
|---------|---------|---------|---------|
| **阀级暂态机理研究**<br>（换相失败物理过程、晶闸管应力） | 详细开关模型<br>（TBSD或标准EMTDC） | 步长：10–20 μs<br>晶闸管：理想开关或双值电阻<br>触发：精确过零检测 | 需捕捉μs级换相细节，关注阀级过电压（可达2.5 p.u.） |
| **控制保护设计验证**<br>（直流功率调制、低压限流控制） | PAVM或TBSD | 步长：100–200 μs<br>启用自动换相失败检测<br>不平衡度：0–100%可调 | 兼顾精度与效率，支持数千次蒙特卡洛仿真 |
| **实时仿真/HIL测试**<br>（物理控制器闭环） | 多速率MATE或<br>FPGA加速模型 | CPU-FPGA协同：FPGA侧2 μs<br>离散电感解耦<br>接口：标幺值信号 | 满足实时性（步长>计算耗时），NRMSE<7% |
| **系统级小干扰稳定性**<br>（次同步振荡、模态分析） | 改进动态相量模型 | 阶数：39阶（CIGRE标准系统）<br>保留k=0,±1分量<br>线性化：时域解析 | 消除准稳态近似误差，幅值误差<0.2% |
| **机电-电磁混合仿真**<br>（大规模交直流电网） | 动态相量接口模型 | EMT步长：20 μs<br>TS步长：5 ms<br>牛顿法残差阈值：$10^{-5}$ p.u. | 接口无延迟，迭代次数3–5次/步 |
| **不平衡/谐波分析**<br>（负序电压、多馈入交互） | 扩展PAVM | 正负序分离<br>谐波项：动态或代数形式<br>频域：10 Hz–2 kHz | 谐波电压传递系数精度<3.5%，支持CCF概率评估 |
| **超大规模系统**<br>（>1000节点） | 嵌套GENE架构<br>+平均值模型 | 父层：节点分析法（5个单相节点）<br>子层：状态空间法<br>开关预计算：192种状态 | 单步计算时间降至30 μs，支持超实时运行 |

---

## 4. 前沿研究方向

### 4.1 异构多速率实时仿真架构
基于CPU-FPGA协同的仿真框架成为主流，FPGA侧实现2 μs步长捕捉晶闸管级换相细节，CPU侧处理50–100 μs步长的交流网络。关键突破在于**离散电感解耦方法**，通过最小损耗误差准则推导最优导纳参数，消除传统试错调参，使0–5 kHz频带内阻抗误差<3.3%。

### 4.2 换相失败免疫建模与预测
最新研究聚焦于**混合串联换流阀（HSCV）**建模，将晶闸管与IGBT串联，利用IGBT主动关断能力（关断时间~226.9 ns）为晶闸管争取额外门极恢复时间（~263 μs）。建模需考虑两者关断时间3个数量级的差异，以及动态均压支路设计。

### 4.3 宽频带阻抗建模与稳定性分析
针对混合HVDC（LCC-MMC级联），建立多输入多输出（MIMO）阻抗模型：
$$
\mathbf{Z}_{MIMO}(s) = \begin{bmatrix} Z_{dd} & Z_{dq} \\ Z_{qd} & Z_{qq} \end{bmatrix}
$$

通过等效单输入单输出（SISO）阻抗法揭示振荡传播路径，结合灵敏度分析指导阻抗重塑，可将主导振荡模态阻尼比提升>0.13，故障恢复时间缩短至0.35 s。

### 4.4 数据驱动的自适应模型降阶
基于**自动故障检测技术**与机器学习，开发自适应PAVM。利用 $g_{crt}$ 阈值函数实时判定故障状态，动态切换模型复杂度：正常工况采用代数相量形式（计算量降低30%），故障瞬间切换至详细微分形式，实现"故障聚焦"的高精度仿真。

### 4.5 传输线模型与多物理场耦合
基于MATE-TLM的宽频变压器建模（5 Hz–10 MHz），结合矢量拟合与特征值缩放技术，解决小信号测量导致的50 Hz励磁电流失真问题。未来趋势是将电磁暂态模型与阀厅电弧、热力学模型耦合，实现换相失败后的阀应力全物理场仿真。

### 4.6 虚拟阻抗控制与模型协同设计
在仿真模型中嵌入**虚拟阻抗控制策略**（$Z_{vir}$ 介入），不仅用于提升仿真效率，更直接用于实际控制设计。研究表明，该策略可使单相故障下电压跌落改善14.03%，过电流抑制3.45%，实现"仿真即设计"的数字化孪生体系。
