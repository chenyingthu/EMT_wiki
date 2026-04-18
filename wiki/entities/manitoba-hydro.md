---
title: "Manitoba Hydro International"
type: entity
entity_type: institution
tags: [manitoba-hydro, pscad, institution]
created: "2026-04-13"
---

# Manitoba Hydro International

## 概述

曼尼托巴水电国际公司（Manitoba Hydro International）是曼尼托巴水电公司的国际业务部门，负责PSCAD/EMTDC的商业化和技术支持。

## 贡献

- PSCAD/EMTDC商业化
- 全球技术支持
- 培训和咨询服务
- 与曼尼托巴大学合作研究

## 相关实体
- [[university-manitoba]]
- [[pscad-emtdc]]

## 深度增强内容

 基于提供的论文数据，Manitoba Hydro International作为PSCAD/EMTDC的开发者与Nelson River复杂多馈入HVDC系统的运营商，其技术实践代表了大规模电磁暂态实时仿真的前沿水平。以下为针对该机构技术特色的深度增强内容，聚焦于**大规模混合实时仿真与多馈入HVDC系统建模**这一主题。

---

# Manitoba Hydro International（深度增强）

## 1. 关键技术详解

### 1.1 大规模混合实时仿真架构（Hybrid HIL）

Manitoba Hydro在Nelson River工程中构建的混合实时仿真系统，本质上是**软件-硬件闭环耦合架构**（Software-in-the-Loop + Hardware-in-the-Loop）。该系统将RTDS电磁暂态仿真器与Bipole III物理控制保护装置（C&P）通过标准化I/O接口互联，形成闭环测试环境。

实时仿真的数学基础是离散化电磁暂态方程的步长约束：
$$\Delta t \leq \frac{1}{10 \cdot f_{max}}$$

其中$f_{max}$为系统最高特征频率（HVDC阀组开关频率及其谐波，通常需考虑2-5 kHz范围）。对于Nelson River系统，为满足14个12脉动换流桥的详细建模需求，仿真步长需控制在**20-50 μs**以内。

HIL接口的功率守恒模型可表述为：
$$\mathbf{V}_{physical}(t) = \mathbf{Z}_{interface} \cdot \mathbf{I}_{simulated}(t-\tau_d) + \mathbf{V}_{source}(t)$$
$$\mathbf{I}_{physical}(t) = f_{controller}(\mathbf{V}_{physical}(t), \text{Logic State})$$

其中$\tau_d$为接口延迟（RTDS的GTAO/GTAI模块典型延迟<1 μs），$\mathbf{Z}_{interface}$为接口变压器或功率放大器的等效阻抗。

### 1.2 多馈入HVDC系统的模块化解耦

针对Dorsey换流站多回直流（Bipole I, II, III）馈入的复杂性，论文提出了**基于动态等效的子系统解耦策略**：

**换流站详细模型**：
保留单极内多个12脉动桥的触发逻辑与换相过程，阀组电压-电流关系满足：
$$V_{dc} = \frac{3\sqrt{2}}{\pi} N_{valve} V_{LL} \cos\gamma - \frac{3}{\pi} N_{valve} X_c I_{dc} - R_{line} I_{dc}$$

其中$N_{valve}$为每极6脉动桥数量（原14个阀组对应复杂拓扑），$\gamma$为熄弧角，$X_c$为换相电抗。

**直流线路分布参数模型**：
采用Bergeron行波模型描述900 km直流线路：
$$i_k(t) = \frac{1}{Z_c} v_k(t-\tau) + I_{history,k}(t-\tau)$$
$$\tau = \frac{l}{v_{wave}} = l\sqrt{L'C'}$$

其中$Z_c = \sqrt{L'/C'}$为波阻抗，$\tau$为行波传播时间。

### 1.3 模型降阶与算力优化

面对Dorsey站原配置（**14个12脉动阀组 + 9台同步调相机**）超出单RTDS计算组（Single Rack）算力限制的瓶颈，Manitoba Hydro实施了以下等效简化：

**换流器聚合技术**：
将同极内多个12脉动桥聚合成等效单桥，保持额定功率$P_{rated}$和等效惯性：
$$P_{dc,eq} = \sum_{i=1}^{N} V_{dio,i} I_{dc,i} \cos\gamma_i - I_{dc}^2 \sum_{i=1}^{N} R_{eq,i}$$

简化后等效阀组数$N_{eq} \ll 14$，通过调整等效换相电抗$X_{c,eq}$保持暂态响应一致性。

**同步调相机动态聚合**：
9台调相机的惯性时间常数与阻尼系数按容量加权聚合：
$$H_{eq} = \frac{\sum_{k=1}^{9} H_k S_{rated,k}}{\sum_{k=1}^{9} S_{rated,k}}, \quad D_{eq} = \sum_{k=1}^{9} D_k \frac{S_{rated,k}}{S_{base}}$$

聚合后模型在2-20 Hz关键振荡频段内保持与原系统一致的机电暂态特性。

### 1.4 控制系统标准化重构

将原PSCAD/EMTDC模型中**100+个自定义模块（Custom Components）**转换为RTDS标准库，涉及以下数学标准化：

**标幺值系统统一**：
所有接口信号转换为标幺值（p.u.）以消除量纲差异：
$$x_{pu} = \frac{x_{actual}}{x_{base}}, \quad \text{其中 } S_{base}=100\text{MVA}, V_{base}=500\text{kV}$$

**离散化控制算法**：
PI控制器从连续域$s$转换到离散域$z$（后向欧拉法）：
$$G_{PI}(z) = K_p + \frac{K_i T_s}{1 - z^{-1}}$$
其中$T_s = 50\mu s$为RTDS仿真步长。

## 2. 硬件平台对比与选型策略

虽然Manitoba Hydro是PSCAD/EMTDC的开发者，但在此项目中选择RTDS作为实时仿真平台，反映了不同硬件架构的技术权衡：

| 特性 | RTDS Simulator | RT-LAB (OPAL-RT) | HyperSim | 自研PSCAD实时化 |
|------|---------------|------------------|----------|----------------|
| **计算架构** | 专有并行处理器（IBM PowerPC） | 商业多核CPU+FPGA | 定制FPGA阵列 | 多核CPU/GPU加速 |
| **典型步长** | 10-50 μs | 20-100 μs (CPU)<br>1-10 μs (FPGA) | 1-10 μs | 10-100 μs |
| **最大节点数** | 720+三相节点（NovaCor） | 取决于PC配置 | 数千节点 | 受限于CPU算力 |
| **HIL接口延迟** | <1 μs（专用I/O） | 5-20 μs | <2 μs | 软件依赖（较高） |
| **HVDC建模** | 成熟库（LCC/VSC） | 需自定义 | 专用电力电子库 | 原生支持（非实时） |
| **与PSCAD兼容性** | 需手动代码转换 | Simulink接口 | 专用格式 | 原生兼容 |

**Manitoba Hydro的技术选择依据**：
1. **确定性实时性**：RTDS的专用硬件架构保证步长严格恒定，满足HVDC阀组级建模的时序要求
2. **工业级I/O密度**：支持数百路模拟/数字I/O接口，满足多馈入系统的复杂HIL测试需求
3. **LCC-HVDC验证**：在基于晶闸管的常规高压直流（LCC-HVDC）领域，RTDS具有最成熟的模型库与工程验证案例

## 3. 实际应用案例汇总

### 3.1 Nelson River多馈入HVDC系统基准模型

**系统规模与特征**：
- **输电走廊**：北部Nelson River水电站群（Keenay, Kettle等）至南部Winnipeg负荷中心
- **直流线路**：Bipole I/II线路全长约**900 km**，输送曼尼托巴水电总发电量的**约70%**
- **拓扑复杂性**：Dorsey换流站作为多馈入节点（Multi-Infeed Point），同时连接Bipole I, II, III及本地交流电网（500kV/230kV）

**建模难点与突破**：
- **详细与实时矛盾**：原详细模型包含14个阀组、9台调相机、数十组交流滤波器，需占用多个RTDS机柜并产生机间通信延迟
- **优化成果**：通过聚合简化，成功将模型压缩至**单计算组（Single Rack）**内运行，消除跨机通信延迟，实现无延迟（Zero-latency）高精度仿真

### 3.2 Bipole III控制系统的HIL验证

**测试配置**：
- **被测设备（DUT）**：Bipole III实际控制保护系统（包含极控、站控、交流保护等物理装置）
- **仿真环境**：RTDS运行Nelson River等效电网模型（含Bipole I/II及简化后的Dorsey站）
- **闭环接口**：模拟量（±10V/4-20mA）与数字量（GOOSE/硬接点）混合接口

**关键测试场景**：
1. **分级交流故障测试（Graded AC Faults）**：
   在Dorsey 500kV母线施加电压跌落梯度为10%、30%、50%、70%、90%的三相及单相接地故障，验证：
   - 低压穿越（LVRT）能力
   - 换相失败（Commutation Failure）预防与恢复
   - 多馈入系统间的故障传递特性

2. **直流线路故障与重启**：
   模拟900 km直流线路不同位置（距整流站0%、50%、100%）的接地故障，测试直流再启动逻辑与功率恢复特性。

**工程价值量化**：
- **风险降低**：在Bipole III投运前发现并修正控制逻辑缺陷，避免现场调试阶段的电网冲击风险
- **成本节约**：替代传统现场实物模拟（Physical Mock-up），节省调试成本约**30-40%**
- **精度验证**：与离线PSCAD详细模型对比，关键动态（故障后100ms功率恢复过程）误差**<5%**

## 4. 研究趋势与开放问题

### 4.1 技术演进趋势

**1. 多速率协同仿真（Multi-Rate Co-Simulation）**
未来方向是将Nelson River系统的**机电暂态过程**（同步稳定性，步长10-20 ms）与**电磁暂态过程**（阀组开关，步长50 μs）通过接口算法（如IRA、DSDR）耦合。Manitoba Hydro面临的挑战是如何在不损失PSCAD详细建模优势的前提下，实现与机电暂态仿真器（如PSD-BPA、PSS/E）的实时数据交换。

**2. 电力电子化电网的FPGA加速**
随着曼尼托巴电网接入更多基于电压源换流器（VSC）的风电与太阳能，开关频率超过2 kHz的电力电子设备需要**<10 μs**的仿真步长。传统CPU-based RTDS面临算力瓶颈，需向**FPGA-based实时仿真**（如OPAL-RT的eFPGAsim）迁移，利用并行硬件逻辑实现纳秒级步长。

**3. 数字孪生与在线仿真（Digital Twin）**
基于本文的HIL技术，构建Nelson River系统的数字孪生体，实现：
- **在线参数辨识**：利用PMU数据实时修正仿真模型参数
- **预测性控制**：在实时仿真器中预演极端工况（如N-2故障），为实际控制系统提供前馈策略
- **虚拟 commissioning**：未来Bipole IV等新建工程可在数字孪生环境中完成100%控制逻辑验证

### 4.2 开放研究问题

**1. 模型简化的理论边界与误差量化**
当前Dorsey站的阀组/调相机聚合依赖于工程经验，缺乏严格的**最优降阶理论**。开放问题包括：
- 如何建立聚合误差$\epsilon = \|G_{detailed}(s) - G_{reduced}(s)\|_{\infty}$与系统稳定裕度的定量关系？
- 对于多馈入HVDC系统，是否存在保证交互稳定性（Interaction Stability）的最小保留模型阶数？

**2. 大规模HIL系统的接口稳定性**
当仿真规模扩大至多机RTDS系统时，机间通信延迟$\tau_{delay}$（通常1-2个步长）可能引发数值振荡。需要研究基于**传输线建模（TLM）**的延迟补偿算法：
$$ \text{稳定性条件：} \frac{dP}{d\delta}\bigg|_{interface} < \frac{1}{\tau_{delay}} $$

**3. 控制代码的自动移植与标准化**
论文中100+自定义模块的手动转换耗时且易错。亟需开发**PSCAD/EMTDC至RTDS的自动代码生成器**，基于IEC 61970 CIM（Common Information Model）或Modelica标准，实现控制逻辑的一次建模、多平台部署。

**4. 多馈入HVDC-HIL测试标准缺失**
目前IEEE或CIGRE缺乏针对多馈入直流系统HIL测试的导则。Manitoba Hydro的实践经验表明，不同直流系统间的**故障传递系数（Fault Transfer Ratio）**与**同时换相失败概率（SCF Probability）**需通过HIL量化，但测试场景的标准化（如故障类型、持续时间、考核指标）尚待建立。

**5. 云化实时仿真的可行性**
随着电网规模扩大，单站点RTDS算力可能不足。研究**分布式实时仿真**（Distributed Real-Time Simulation），通过高速光纤通信（<10 μs延迟）实现多地点RTDS集群协同，是支撑未来跨区互联电网超大规模HIL测试的关键。