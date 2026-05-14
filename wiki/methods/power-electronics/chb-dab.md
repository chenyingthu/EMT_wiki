---
title: "CHB-DAB"
type: method
tags: [chb-dab, power-electronics, pet]
created: "2026-05-04"
updated: "2026-05-10"
---

# CHB-DAB: 级联H桥-双有源桥变换单元

CHB-DAB（Cascaded H-Bridge Dual Active Bridge）指级联H桥整流器与双有源桥DC-DC变换器两级级联组成的电力电子变换单元，是电力电子变压器（PET）或固态变压器（SST）的典型拓扑。本页作为CHB-DAB EMT建模方法的技术入口，聚焦仿真加速策略，不展开DAB或CHB各自的基础工作原理。

## EMT中的作用

CHB-DAB 在EMT仿真中的作用：

- **应用场景**：CHB-DAB在EMT仿真中的典型应用
- **模型集成**：CHB-DAB如何集成到EMT仿真框架中
- **性能影响**：CHB-DAB对EMT仿真性能的影响分析
## 形式化表达

CHB-DAB 的形式化数学描述：

$$
\text{待补充：CHB-DAB的数学描述}
$$
## 问题定义与挑战

CHB-DAB型PET的EMT仿真面临双重计算瓶颈：

1. **多时间尺度矛盾**：CHB整流级实际开关频率为数百Hz（~500 Hz），但DAB隔离级因高频变压器通常工作在5~20 kHz。若全系统采用统一小步长（如≤10 μs），低频CHB部分被迫以高频步长求解，浪费计算资源 [Wang 2025]。

2. **模块数量爆炸**：高压应用需要多个CHB-DAB功率单元级联（ISOP结构），导致电路节点数、状态变量数和历史项计算量随模块数线性甚至超线性增长。详细模型在PSCAD/EMTDC等平台仿真速度极慢 [丁江萍 2022]。

这两大瓶颈使得CHB-DAB型PET难以在合理时间内完成器件级EMT仿真，尤其阻碍控制参数迭代和系统级接入研究。

## 核心技术路线

针对上述挑战，现有文献提出了四条互补的技术路线：

### 路线A：等效电路法

丁江萍等（2022）基于诺顿/戴维南等效与嵌套快速同时求解算法，构造高频变压器原/副边解耦伴随网络。

- 将每个CHB单元分割为原边侧(P1)和副边侧(P2)两个单端口网络
- 多个子模块级联后对外仅保留4个外部节点（输入正负极、输出正负极）
- 采用"正向求等效参数 → 系统求解节点电压 → 反解更新内部状态"三步循环
- 计算复杂度O(1)，**几乎不随子模块数量增加**
- PSCAD/EMTDC验证，3模块A相算例，5 kHz DAB需≤10 μs步长
- 保留开关谐波，区别于平均值模型

### 路线B：延迟解耦法

许明旺等（2023）基于半隐式延迟解耦方法，从DAB状态方程出发进行矩阵分裂。

- 将系统矩阵分裂为对角自阻抗项和非对角耦合项
- 对角项保持隐式梯形积分，非对角项实施半步时延（n+1/2时刻）
- 实现状态变量（电容电压uC、变压器电流iT）间的细粒度解耦
- 解耦后导纳矩阵保持恒定，**消除开关高频动作导致的LU重分解**
- 各DAB模块可独立并行更新内部状态，误差O(Δt²)

### 路线C：多速率分区法

Wang等（2025）利用CHB-DAB两级变换电路固有频率差异，将系统划分子系统。

- 低频CHB子系统（大步长）与高频DAB子系统（小步长）独立推进
- 互联节点采用多端口诺顿等效+电流源等效数据传输
- 设计**交错等效多速率交互算法**，消除电流源等效引起的时间步长延迟
- DAB部分用MNA将变压器两侧电流作为状态变量，接受高精度触发信号
- CHB:DAB开关频率比约1:10~1:20，对应步长比10:1~20:1

### 路线D：状态平均法

Xu等（2025）基于广义状态空间平均法（GSSA）构建简化为四端口等效电压源。

- 开关函数法描述CHB交直流端口电气变量桥接，消除器件级开关
- Dommel+二元电阻法建立储能子模块Thevenin等效
- 傅里叶分解：仅保留直流+基波分量（N=1），忽略k≥2高次谐波
- 各功率模块聚合成四端口等效电压源，构建ISOP型MAB-PET模型
- 加速比100~1000x，最大相对误差<1%（PSCAD/EMTDC验证，河北崇礼实际系统）

## 四路线对比

| 技术路线 | 核心机制 | 复杂度特征 | 精度保留 | 关键约束 |
|---------|---------|-----------|---------|---------|
| A:等效电路 | 变压器伴随网络解耦 | O(1)，不随模块数增 | 开关谐波保留 | 需变压器线性参数 |
| B:延迟解耦 | 矩阵分裂+半步延迟 | 导纳矩阵恒定 | 二阶精度O(Δt²) | 半步延迟引入截断误差 |
| C:多速率 | 频率分区+交错接口 | 步长比10:1~20:1 | 开关瞬态保留 | 需接口延迟补偿 |
| D:状态平均 | GSSA谐波截断N=1 | 加速100~1000x | 误差<1% | 丢失高频谐波信息 |

## 适用边界

### 适用条件

- 拓扑为CHB-DAB型PET，ISOP或类似串并联结构
- 目标为系统级EMT仿真、控制参数迭代、AC/DC混合配电网接入验证
- 可在精度与效率间折中时使用路线D（最快速）或路线A/B（保留开关谐波）
- 多时间尺度问题优先考虑路线C

### 失效边界

- 需要器件级损耗、EMI/EMC分析的场景不适合路线D
- 故障穿越、保护闭锁、极端非线性暂态需用路线A/B且重新校核详细模型
- MAB（多有源桥）等变体拓扑需额外推导等效关系
- 硬件实时仿真平台上的步长约束需单独验证（见[[real-time-simulation]]）

### 关键假设

- 方法A/B均假设IGBT/二极管可用二值电阻等效（Ron/Roff）
- 方法D假设高频分量可忽略（仅保留N=1），据方法推断此假设在开关频率远高于系统基频时合理
- 变压器励磁、漏感视为线性参数（方法A/C），未考虑饱和效应

## 链接使用

- 基础原理：[[dual-active-bridge]]（DAB主入口）、[[submodule-model]]（CHB入口）
- PET系统背景：[[solid-state-transformer]]、[[pet]]
- 相关建模方法：[[multirate-method]]、[[network-equivalent]]、[[average-value-model]]、[[state-space-method]]
- 控制与调制：[[power-electronics-control]]、[[pwm-modulation]]、[[dc-dc-converter]]
- 分类导航：[[power-electronics]]

CHB-DAB的具体数值结论（加速比、误差、步长）必须回到对应来源页，本页仅汇总方法层面的对比与索引。

## 代表性来源

| 来源 | 年份 | 技术路线 | 主要数值证据 |
|------|------|---------|-------------|
| [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme|Xu 等 - Simplified EMT Model of MAB-PET]] | 2025 | D:状态平均 | SEM快2~3个量级，误差<1%，PSCAD/EMTDC |
| [[multirate-emt-simulation-of-power-electronic-transformers-with-high-precision-fi|Wang 等 - Multirate PET EMT]] | 2025 | C:多速率 | 步长比10:1~20:1，零延迟接口 |
| [[一种级联h桥型电力电子变压器电磁暂态解耦与仿真模型|许明旺 - CHB-PET半隐式解耦]] | 2023 | B:延迟解耦 | 导纳矩阵恒定，O(Δt²)精度 |
| [[级联h桥型电力电子变压器的电磁暂态等效建模方法|丁江萍 - CHB-PET等效建模]] | 2022 | A:等效电路 | 4节点O(1)复杂度，PSCAD/EMTDC验证 |
| [[high-efficiency-modeling-of-multi-layer-cascaded-dual-active-bridge-dab-units-on|Qi 等 - 多层DAB实时聚合]] | 2024 | 聚合建模 | 1.0 μs步长，100 kHz，节点降~80% |

## 证据边界

- 丁江萍（2022）：原文报告"极高加速比"但未给出具体加速倍数/CPU时间；3模块A相算例，未覆盖三相不平衡/故障场景
- 许明旺（2023）：原文未给出具体算例参数、步长设置、加速倍数；误差分析基于梯形积分理论O(Δt²)而非实测
- Wang（2025）：原文未报告加速比、具体步长取值或误差百分比；CHB:DAB步长比10:1~20:1为据频率比推断
- Xu（2025）：误差<1%和100~1000x加速来自原文摘要，但逐变量误差、仿真步长、计算机配置未完整报告
- Qi（2024）：节点降~80%和资源降~70%为量化发现，直流偏置<0.1%有原文支持

## 来源论文

| 论文 | 年份 |
|------|------|
| [[analysis-and-prospect-of-development-of-chinas-independent-electromagnetic-trans-fix|Analysis and Prospect of Development of China]] | 2022 |
| [[portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si|Portal Analysis Approach Used for the Efficient Electromagne]] | 2023 |
