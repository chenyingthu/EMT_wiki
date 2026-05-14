---
title: "配电变压器 (Distribution Transformer)"
type: model
tags: [distribution-transformer, distribution-network, step-down, power-quality, emt]
created: "2026-05-04"
updated: "2026-05-12"
---

# 配电变压器 (Distribution Transformer)



## 定义与边界

配电变压器是将中压配电网（ typically 6-35 kV）电压降至低压用户电压（220/380 V）的电力变压器，是配电网与用户的接口设备。在EMT仿真中，配电变压器模型需要考虑饱和特性、连接组别、阻抗参数以及负载引起的电压调整。

**边界限定**：本页面聚焦于配电变压器的EMT建模，不包括输电变压器或换流变压器。

## EMT中的作用

配电变压器是配电网EMT仿真的关键设备：

- **电压变换**：中压到低压的精确变换
- **故障分析**：短路电流和过电压传播
- **电能质量**：谐波传递、电压暂降分析
- **保护配合**：熔断器、断路器保护整定
- **分布式电源**：DG接入对变压器的影响

## 主要分支与机制

### 1. 基本参数

**额定参数**：
- 额定容量：$S_N$（kVA）
- 电压比：$k = V_1/V_2$
- 短路阻抗：$Z_k$%（通常4-6%）
- 空载损耗、负载损耗

**等效电路**：
- 串联阻抗：$R_k + jX_k$
- 并联导纳：$G_0 + jB_m$（励磁支路）

### 2. 连接组别

**Dyn11**：
- 高压侧三角形，低压侧星形
- 相位差330°（11点钟）
- 可带不平衡负载

**Yyn0**：
- 高压侧星形，低压侧星形
- 同相位
- 三相四线制

### 3. 饱和特性

磁化曲线：
$$i_m = f(\phi)$$

常用模型：
- 分段线性
- 反正切函数
- Frolich方程

## 形式化表达

### 电压调整率

$$\Delta U = \beta(R_k\cos\phi + X_k\sin\phi) \times 100\%$$

其中$\beta$为负载率。

### 短路电流

三相短路：
$$I_k = \frac{I_N}{Z_k\%} \times 100$$

### 谐波传递

谐波电压传递系数：
$$T_h = \frac{V_{2h}}{V_{1h}} = \frac{1}{|1 + hZ_k/Z_{load}|}$$


## 量化性能边界

**Shukla 2021 配电网EMT FPGA硬件加速**（SoC-FPGA Zynq-7000, 古瓦哈提市Jail变电站）:
- FPGA实现相比MATLAB基线速度提升约 **12.5倍**（1秒仿真，Zedboard开发板）
- 配电网导纳矩阵稀疏度由0.94（50节点）增至 **0.997**（1000节点），呈高度病态特性
- 导纳矩阵条件数维持在 **2.907×10^5 ~ 2.974×10^5**，PCG预处理共轭梯度法是有效求解策略
- 32位单精度浮点，5级流水线乘加器实现每时钟周期1次吞吐
- 数据缺口：仅与MATLAB对比，未与商业EMT软件（PSCAD/EMTP）、GPU或其他硬件平台系统比较

**Chandrasena 2004 配电变压器GIC低频模型**（3 kVA, 115 V/2300 V单相，M4硅钢片）:
- 基于Jiles-Atherton磁滞理论的改进变压器模型，在EMTDC中实现
- 额定工况（1.0 p.u., 60Hz）励磁电流RMS仿真误差 **1.98%**，功率因数误差仅 **3%**（实测0.672 vs 仿真0.692）
- 1.1 p.u.电压下，新模型励磁电流最大误差 **5.38%**，优于传统电阻模型的11.25%
- 1.1 p.u.时相位角偏差 **2.57°**，导致功率因数误差在高电压时扩大
- 数据缺口：验证仅基于单相小容量样机，未在大型三相多柱变压器和实际GIC注入场景下验证；低频GIC模型忽略绕组电容，不适用于雷电/VFTO等宽频暂态

**Jazebi 2015 对偶原理变压器宽频模型**（含涡流效应，1 kVA单相变压器）:
- 基于几何尺寸和材料参数的解析Cauer等效电路，适用 **1 Hz至1 MHz** 宽频范围
- 等效电阻与电感计算误差 **<5%**（对比有限元FEM）
- 忽略涡流效应时高频阻抗幅值误差 **>30%**，证明涡流建模对MHz级暂态至关重要
- 7阶模型有效预测范围延伸至 **15 MHz以上**；实验室实测谐振频率最大偏差约20%（归因于介电常数不确定性与制造公差）
- 数据缺口：主要验证两绕组单相变压器，三相多柱/非圆柱绕组结构的验证尚未充分展开

**数据缺口声明**：配电变压器的EMT建模性能数据主要来自小容量单相样机（3 kVA、1 kVA），实际配电网中数百kVA至数MVA三相配电变压器的宽频建模精度和仿真加速比缺乏系统报告。GIC铁芯模型和FPGA加速分别在低频和硬件维度提供了有益参考，但配电变压器在分布式电源大量接入场景下的谐波/暂态仿真精度尚待系统验证。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[empirical-model-of-a-current-limiting-fuse-using-emtp|Empirical model of a current-limiting fuse using EMTP]] | 1998 |
| [[an-fpga-based-electromagnetic-transient-analysis-of-power-distribution-network|An FPGA based electromagnetic transient analysis of power di]] | 2021 |
| [[a-thvenin-type-version-of-the-extended-modal-domain-model-for-lightning-induced-|A Thévenin-Type Version of the Extended Modal-Domain Model f]] | 2023 |
| [[calculation-of-lightning-induced-voltages-on-a-large-scale-distribution-network-|Calculation of lightning-induced voltages on a large-scale d]] | 2025 |
## 相关模型

- [[transformer-model]] - 变压器通用模型
- [[converter-transformer-model]] - 换流变压器
- [[load-model]] - 负荷模型

## 相关方法

- [[frequency-dependent-modeling]] - 频率相关建模
- [[nodal-analysis]] - 节点分析
- [[vector-fitting]] - 矢量拟合

## 相关主题

- [[real-time-simulation]] - 实时仿真
- [[frequency-dependent-modeling]] - 宽频建模
- [[ferroresonance]] - 铁磁谐振

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
