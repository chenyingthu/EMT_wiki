---
title: "频率相关建模"
type: topic
tags: []
created: "2026-04-13"
---

# 频率相关建模

## 定义
频率相关建模描述线路、电缆、土壤、变压器、接地系统、网络等值或电力电子端口参数随频率变化的行为，并将频域特性转换为 EMT 可求解的时域模型。核心问题不是“是否有频率响应”，而是如何在宽频精度、无源性、阶数和计算成本之间取舍。

## 合成定位
在 P0 taxonomy 中，频率相关建模是 [[co-simulation]]、[[real-time-simulation]]、[[harmonic-analysis]] 和 [[network-equivalent]] 的底层模型支撑。它与 [[vector-fitting]]、[[passivity-enforcement]]、[[state-space-method]]、[[fdne-model]] 和 [[transmission-line-model]] 关系最紧。

## 分类或机制
- 线路/电缆频变模型：处理导体、土壤、大地回路、相域/模域变换和传播函数的频率依赖。
- 频率相关网络等值：用 [[fdne-model]] 压缩外部网络端口频响，常配合 [[vector-fitting]] 与无源性强制。
- 设备/端口宽频模型：基于测量或解析推导构建变压器、接地网、DC-DC 变换器、逆变器等宽频等效。
- 时域实现机制：常见路径包括递归卷积、状态空间实现、Norton 等效、数值拉普拉斯反变换和 FPGA/实时部署。

## 适用边界与失败边界
适用场景包括雷电/开关暂态、谐波与超谐波、长线/电缆、电力电子端口交互和混合仿真边界等宽频问题。失败边界包括频带选择不足、DC 值不准确、极点/留数拟合病态、相模变换不光滑、无源性破坏、测量数据噪声或高阶模型无法实时执行。原页面/来源汇总未给出统一频带和误差门槛，应随研究对象报告。

## 代表性论文
- “Multi-port frequency dependent network equivalents for the EMTP”：多端口 FDNE 的基础工作。
- “Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical”：将 FDNE 用于 EMT-机电混合边界。
- “Development of phase domain frequency-dependent transmission line model on FPGA”：代表频变线路模型的实时硬件实现。
- “A guaranteed passive model for multi-port frequency dependent network equivalent”：强调严格无源性的 FDNE 构建。
- “Advanced Wideband Line/Cable Modeling for Transient Studies”：聚焦宽频线路/电缆建模的数值稳定改进。

## 验证共识
验证通常需要频域拟合误差、时域波形对比和无源性/稳定性检查同时成立。单独给出拟合曲线不足以证明 EMT 可用；论文普遍需要与解析模型、现有 EMT 工具、现场/实验数据或全波仿真对比。

## 相关方法
- [[vector-fitting|矢量拟合]] - 频响有理函数拟合
- [[passivity-enforcement|无源性强制]] - 模型无源性保证
- [[state-space-method|状态空间法]] - 频变状态空间实现
- [[prony-analysis|Prony分析]] - 时域模态参数辨识
- [[model-order-reduction|模型降阶方法]] - 高阶模型压缩

## 相关模型
- [[fdne-model|频变网络等值(FDNE)]] - 外部网络宽频等值
- [[transmission-line-model|输电线路模型]] - 频变线路建模
- [[cable-model|电缆模型]] - 频变电缆建模
- [[transformer-model|变压器模型]] - 宽频变压器模型
- [[grounding-system-model|接地系统模型]] - 频变接地建模

## 相关主题
- [[network-equivalent|网络等值]] - 系统级频变等值
- [[harmonic-analysis|谐波分析]] - 宽频谐波建模
- [[real-time-simulation|实时仿真]] - 频变模型实时实现
- [[co-simulation|混合仿真]] - 多域频变接口
- [[wideband-modeling|宽频建模方法]] - 全频段统一建模

## 论文方法分析
> 基于 52 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|
| 矢量拟合(Vector Fitting) | 3 | A New Approach to Represent the Corona Effect and Frequency-Dependent  |
| 有理函数逼近 | 3 | A New Approach to Represent the Corona Effect and Frequency-Dependent  |
| 频率相关网络等值(FDNE) | 3 | FPGA-based simulation of grid-tied converters using frequency-dependen |
| 状态空间法 | 2 | Accelerated frequency-dependent method of characteristics for the simu |
| 梯形积分法 | 2 | An Inverter Model Simulating Accurate Harmonics with Low Computational |
| 数值拉普拉斯变换 | 2 | Analytical and measurement-based wideband two-port modeling of DC-DC c |
| 频变相域(FDPD)建模 | 2 | Development of phase domain frequency-dependent transmission line mode |
| 矢量拟合(VF) | 2 | Enhancing computation performance of rational approximation for freque |
| 并行计算技术 | 2 | Enhancing computation performance of rational approximation for freque |
| C语言底层线性代数实现 | 2 | Enhancing computation performance of rational approximation for freque |
| 频率自适应仿真 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 动态相量法 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 解析信号理论 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| 模态分解 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
| π型等效电路自动插入 | 1 | 27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power T |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|
| 地下电缆 | 6 |
| 频变输电线路模型 | 5 |
| 架空输电线路 | 4 |
| 通用线路模型(ULM) | 4 |
| 架空线路 | 3 |
| 地下电缆系统 | 3 |
| 输电线路 | 2 |
| 多导体输电线路(MTL) | 2 |
| 频变相域(FDPD)输电线路模型 | 2 |
| 频率相关网络等值(FDNE) | 2 |
| 8端口网络模型 | 2 |
| 频变电缆模型(FDCM) | 2 |
| 多相输电线路 | 1 |
| 多端口频率相关网络等值模型(FDNE) | 1 |
| 外部线性电网等值模型 | 1 |
### 验证方式分布
- **仿真**: 10 篇
- **仿真对比**: 9 篇
- **仿真/对比**: 8 篇
- **仿真验证**: 5 篇
- **仿真与对比**: 3 篇
- **仿真与实验对比**: 2 篇
- **仿真验证与对比**: 2 篇
- **实验对比**: 1 篇
- **对比（与文献中的三组现场实测数据进行对比验证）**: 1 篇
- **仿真对比与现场实验**: 1 篇
- **仿真对比验证**: 1 篇
- **仿真对比与案例验证**: 1 篇
- **仿真验证/与经典解析模型对比**: 1 篇
- **仿真与现场试验对比**: 1 篇
- **实验**: 1 篇
- **仿真计算与实测数据对比/现有EMT工具对比**: 1 篇
- **仿真与实验**: 1 篇
- **仿真验证（频域模态分析与时域数值拉普拉斯变换对比）**: 1 篇
- **仿真与文献实测数据及全波方法对比验证**: 1 篇
- **仿真验证与算例对比**: 1 篇
## 技术演进脉络
### 1998年 (1篇)
- **Digital Time-Domain Investigation of Transient Behavior of Coupling Capacitor Vo**
  - 💡 相较于已有简化模型，首次构建了全面涵盖变压器饱和特性、多分接头、保护设备、谐振抑制电路及多种负载模型的精细化CCVT数字时域模型。
  - 开发了包含变压器饱和特性、分接头、保护设备及谐振抑制电路的详细CCVT EMTP模型。
  - 通过对比仿真结果与物理测试数据，验证了所建模型的高精度。
### 2001年 (1篇)
- **Frequency-dependent transmission line modeling utilizing transposed conditions -**
  - 💡 通过恒定变换矩阵与降阶相/模态块结合，利用线路连续换位特性实现计算效率与精度的最优平衡。
  - 提出结合相域与模域优势的混合输电线路建模方法。
  - 利用连续换位特性引入恒定变换矩阵与矩阵平均处理以降低计算维度。
### 2003年 (1篇)
- **A simple and efficient method for including frequency-dependent effects in trans**
  - 💡 提出将频变分布参数线路等效为无损线路与简单L-R阻抗电路的组合模型，以极简结构高效替代复杂的递归卷积计算。
  - 提出了一种将频变分布参数线路等效为无损线路与简单L-R阻抗电路组合的建模方法。
  - 基于四端参数理论推导频变阻抗电路，有效克服了传统递归卷积法内存消耗大和数值不稳定的缺陷。
### 2004年 (2篇)
- **Frequency-Dependent Transformation Matrices for Untransposed Transmission Lines **
  - 💡 首次将牛顿-拉夫逊法引入频变变换矩阵求解，实现了多回路非换位线路模态参数在宽频带内的光滑化与稳定有理拟合。
  - 提出基于牛顿-拉夫逊法计算频变变换矩阵的新方法，克服了传统对角化算法在多回路架空线中矩阵元素不光滑的缺陷。
  - 证明了NR方法生成的模态参数在宽频带内具有良好的光滑性与渐近特性，可直接用于最小相移型有理函数拟合。
- **Multi-port frequency dependent network equivalents for the EMTP - Power Delivery**
  - 💡 将单端口频率相关等效技术成功扩展至多端口，并改进宽频导纳拟合算法，实现了大型复杂电网在EMTP中的高效高精度降阶建模。
  - 提出了一种将大型电力系统降阶为单端口及多端口频率相关等效网络(FDNE)的系统方法。
  - 改进了导纳拟合技术，使等效模型能在宽频范围内精确匹配原网络的频率响应特性。
### 2005年 (1篇)
- **Validation of Frequency-Dependent**
  - 💡 结合自适应非等距频域采样与半解析积分的逆傅里叶变换方法，实现了高效、高精度的频变传输线模型时域验证。
  - 提出基于逆傅里叶变换的频变传输线模型时域验证流程。
  - 引入自适应非等距采样策略，大幅减少解析频域响应所需的样本数量。
### 2006年 (1篇)
- **Inclusion of Frequency-Dependent Soil Parameters in**
  - 💡 提出仅需三个参数的土壤频率特性一阶模型，并结合高斯数值积分法扩展传统Carson/Pollaczek公式，实现宽频下输电线路大地回路阻抗的精确建模。
  - 提出了一种仅需三个统计独立参数的简单一阶模型来综合频率相关的土壤电导率和介电常数。
  - 推导了适用于架空线路和地下电缆的考虑频率相关土壤参数的新大地回路阻抗公式。
### 2008年 (1篇)
- **Earth Return Impedance of Overhead and Underground Conductors Considering Earth **
  - 💡 构建了统一的多层土壤大地返回阻抗计算理论框架与数值求解方法，突破了传统均匀/半无限大地假设的局限
  - 推导了多层土壤中任意拓扑导体排列的广义自阻抗与互阻抗表达式
  - 证明了现有经典均匀大地模型均为该广义公式在特定近似下的特例
### 2012年 (2篇)
- **Frequency Dependent Network Equivalent for Electromagnetic and Electromechanical**
  - 💡 将矢量拟合与半尺寸无源性强制技术相结合，构建了兼顾宽频带精度与数值稳定性的电磁-机电混合仿真网络等值新方法。
  - 提出了一种适用于电磁-机电暂态混合仿真的频率相关网络等值方法
  - 采用矢量拟合算法实现外部网络宽频带阻抗特性的精确建模
- **电磁–机电暂态混合仿真中的频率相关网络等值**
  - 💡 将修正矢量拟合法与摄动无源性校正相结合，构建了适用于电磁-机电混合仿真的频率相关网络等值模型，有效解决了接口高频波形畸变与模型无源性保障难题。
  - 提出了基于简化元件模型获取网络频率响应采样值的高效方法。
  - 应用修正矢量拟合法构建FDNE，并引入摄动校正策略严格保证模型无源性。
### 2015年 (1篇)
- **Application of Frequency-Partitioning Fitting to the Phase-Domain Frequency-Depe**
  - 💡 将频率分区与自适应加权技术引入相域输电线路建模，有效替代传统矢量拟合方法并提升了频率相关矩阵的拟合精度与计算效率。
  - 将基于频率分区和自适应加权的线性系统辨识方法成功应用于架空输电线路的相域频率相关建模
  - 提出了针对该相域线路建模应用以增强辨识过程的数值技术
### 2016年 (2篇)
- **A Wideband Equivalent Model of Type-3 Wind Power Plants for EMT Studies**
  - 💡 提出了一种结合静态频变网络等效与动态低频等效的宽频降阶聚合方法，在保证宽频电磁暂态精度的同时大幅提升了Type-3风电场的EMT仿真效率。
  - 提出了一种兼顾计算效率与精度的Type-3风电场宽频降阶动态等效模型。
  - 构建了由静态频变网络等效和动态低频等效组成的复合架构，完整覆盖宽频电磁暂态响应。
- **Frequency-dependent line model in the time domain for simulation of fast and imp**
  - 💡 将频率相关特性融入传统Bergeron集中参数模型，并通过级联电路与状态矩阵实现宽频带快速瞬态的纯时域高精度仿真。
  - 提出了一种将频率相关效应引入传统Bergeron模型纵向参数的新型时域输电线路建模方法。
  - 采用级联频率相关Bergeron电路结构，有效扩展了模型在宽频带范围内的适用性。
### 2017年 (1篇)
- **27&28/Multi-Scale and Frequency-Dependent Modeling of Electric Power Transmissio**
  - 💡 提出基于动态相量与频率自适应平移的多尺度频变输电线路模型，实现宽频电磁与机电暂态的高效统一仿真。
  - 提出了一种适用于多尺度仿真的频变输电线路模型，支持宽频带暂态的统一仿真。
  - 引入频率自适应仿真机制，通过频域傅里叶谱自适应平移有效减少时域离散步长。
### 2018年 (3篇)
- **Accelerated frequency-dependent method of characteristics for the simulation of **
  - 💡 提出了一种结合拓扑稀疏性优化、内存访问优化及时间离散误差校正的加速频率相关特征线法，大幅提升了多导体输电线路时域电磁暂态仿真的计算效率。
  - 利用系统电路拓扑结构有效减少了状态方程的数量。
  - 对状态空间矩阵进行分组并结合稀疏技术加速常微分方程组的求解。
- **An Enhanced Average Value Model of Modular Multilevel Converter for Accurate Rep**
  - 💡 通过引入桥臂电流初始化机制，在无需详细开关调制信号的前提下，实现了MMC阻塞工况的高精度、高效率平均值建模。
  - 提出了一种增强型MMC平均值模型，有效补偿了传统AVM的初始条件缺陷。
  - 设计了桥臂电流初始化算法，显著提升了仿真启动阶段的数值稳定性与精度。
- **Development and Applicability of Online Passivity Enforced Wide-Band Multi-Port **
  - 💡 将在线无源强化RLS辨识与离散z域导纳矩阵结合，实现了无需先验参数即可直接部署的宽频多端口FDNE混合仿真方法。
  - 提出了一种基于在线无源强化RLS算法的单/多端口FDNE构建方法
  - 实现了在未知网络参数下仍能准确辨识z域导纳矩阵的离散化等效模型
### 2019年 (4篇)
- **Accelerated frequency-dependent method of characteristics for the simulation of **
  - 💡 融合拓扑降阶、稀疏求解、模态解耦与误差校正技术，实现了多导体输电线路时域仿真计算效率与内存占用的同步优化。
  - 提出利用电路拓扑结构减少状态方程数量的加速特征线法实现方案。
  - 通过状态空间矩阵分组与稀疏技术加速常微分方程组求解。
- **Development of high frequency (Supraharmonic) models of small-scale (amplt;5kW),**
  - 💡 首次将黑盒建模方法系统应用于2-150 kHz超谐波频段，克服了传统白盒模型高频参数未知且难以获取的瓶颈。
  - 提出了一种基于黑盒方法的通用高频建模流程，适用于2-150 kHz频段的小型单相光伏逆变器。
  - 成功开发了三款主流商用光伏逆变器的高频等效模型，填补了超谐波仿真研究的模型空白。
- **Grounding grids in electro-magnetic transient simulations with frequency-depende**
  - 💡 提出了一种将电磁场频域计算结果转化为拉普拉斯域有理函数双端口等效电路的混合建模方法，实现了接地网宽频特性在ATP-EMTP中的高效时域仿真。
  - 提出了一种结合电磁场理论与电路理论的混合建模方法，用于精确表征接地网的宽频阻抗特性。
  - 构建了内部导纳由拉普拉斯域有理函数定义的双端口等效电路组件，解决了复杂电磁模型难以直接接入EMT软件的问题。
- **Measurement-based frequency-dependent model of a HVDC transformer for electromag**
  - 💡 首次融合特征值缩放与模态揭示变换技术，基于终端实测数据构建了兼顾物理合理性与数值稳定性的HVDC变压器宽频黑盒模型。
  - 首次将黑盒建模技术应用于HVDC变压器，成功构建了宽频五端子频率相关模型。
  - 提出新颖的特征值缩放程序，有效将测量数据中的励磁电流修正至物理合理水平。
### 2020年 (6篇)
- **A Harmonic Phasor Domain Co-Simulation Method and New Insight for Harmonic Analy**
  - 💡 首创谐波相量域(HPD)与EMT混合协同仿真架构，突破传统方法无法同步获取瞬时与谐波相量信息的瓶颈，实现大规模电力电子交直流电网宽频振荡的高效精准分析。
  - 提出电力电子直流电网的谐波相量域(HPD)建模方法，可同时输出瞬时波形与谐波相量。
  - 构建HPD传输线模型(HPD-TLM)，实现EMT交流侧与HPD直流侧的高效接口与协同。
- **An Inverter Model Simulating Accurate Harmonics with Low Computational Burden fo**
  - 💡 通过推广时间平均法至梯形积分法并设计简易开关时刻识别公式，实现了兼顾高精度谐波复现与低计算负担的大步长电磁暂态仿真。
  - 将时间平均法（TAM）从后向欧拉法推广至离线仿真广泛使用的梯形积分法。
  - 提出一种简易公式用于识别开关时刻，摆脱了原TAM对FPGA硬件计数器的依赖，便于在普通PC上实现。
- **Effect of frequency-dependent soil parameters on wave propagation and transient **
  - 💡 系统量化了土壤频变特性对多相地下电缆波传播及暂态行为的影响，指出了传统恒参土壤模型在EMT仿真中的局限性。
  - 系统总结并对比了多种频变土壤模型，验证了Longmire/Smith模型与实测数据的最佳吻合度。
  - 结合扩展传输线法，研究了恒参土壤与频变土壤模型下地下电缆的波传播频率响应特性。
- **Electromagnetic transient modeling of grounding electrodes buried in frequency d**
  - 💡 将频变土壤特性与可变含水量相结合，通过全波FEM与FRVF技术构建了高精度且适用于EMT仿真的接地极等效模型。
  - 系统回顾并对比了四种考虑土壤含水量变化的频变土壤模型。
  - 基于全波FEM频域仿真与FRVF技术，开发了适用于EMT仿真的接地极等效电路。
- **Partitioned fitting and DC correction in transmission line/cable models for wide**
  - 💡 采用高频拟合与低频直流校正分离的两阶段策略，在避免大留数/极点比的同时精准还原直流响应，突破了传统单阶段宽频拟合的数值稳定性瓶颈。
  - 提出并详细阐述了用于宽频EMT研究的分区拟合与直流校正两阶段方法。
  - 提供了基于分区拟合的状态空间实现的完整时域实现细节。
- **Passivity enforcement of wideband line model through coupled perturbation of res**
  - 💡 首次将特征导纳的极点与常数项纳入无源性强制扰动框架，并结合新型精度保持度量实现更优的模型修正。
  - 提出同时扰动特征导纳留数、极点和常数矩阵的无源性强制新方法
  - 引入基于相对误差和Frobenius距离的偏差度量以在修正过程中保持模型精度
### 2021年 (5篇)
- **A guaranteed passive model for multi-port frequency dependent network equivalent**
  - 💡 将Brune与Tellegen网络综合法结合并实现自动化，直接基于离散频响数据构建严格无源的多端口FDNE模型。
  - 提出了一种基于Brune和Tellegen网络实现方法的新型FDNE构建流程。
  - 从数学原理上严格保证了所构建等值网络的全频段无源性，确保EMT仿真稳定。
- **Analysis of Frequency-Dependent Network Equivalents in Dynamic Harmonic Domain**
  - 💡 将动态相量法与矢量拟合有理模型深度融合，并引入平衡实现降阶技术，实现了频变网络等效在频域谐波分析中的高效稳定求解。
  - 提出了将动态相量法与有理函数模型相结合的通用框架，适用于频域电磁暂态谐波分析。
  - 应用平衡实现理论对高阶状态空间系统进行降阶，有效缓解了频变网络分析的计算负担。
- **Computation of ground potential rise and grounding impedance of simple arrangeme**
  - 💡 将分层介质格林函数矩量法与矢量拟合及递归卷积相结合，实现了频率依赖型分层土壤中接地系统瞬态特性的高效精确建模。
  - 提出基于分层介质格林函数的频域矩量法求解器，用于计算100 Hz至10 MHz范围内的接地阻抗。
  - 结合矢量拟合与递归卷积技术，将频域等效电路转换为时域模型以计算瞬态地电位升（GPR）。
- **Development of phase domain frequency-dependent transmission line model on FPGA **
  - 💡 在FPGA平台上实现全流水线并行化的频变相域输电线路模型，结合自定义高精度浮点格式突破了实时仿真中速度与精度的瓶颈。
  - 开发了适用于FPGA实时数字仿真器的频变相域输电线路模型。
  - 设计了全流水线与并行化的硬件架构以最小化仿真步长。
- **Development of phase domain frequency-dependent transmission line model on FPGA **
  - 💡 将频变相域输电线路模型在FPGA上进行全流水线并行化实现，并结合自定义浮点格式突破了实时仿真中精度与速度的瓶颈。
  - 开发了基于FPGA的全流水线并行化频变相域输电线路模型。
  - 设计了自定义48位浮点数据格式以提升硬件计算精度。
### 2022年 (4篇)
- **A New Approach to Represent the Corona Effect and Frequency-Dependent Transmissi**
  - 💡 首次将电晕效应的电压依赖性与线路参数的频率依赖性直接耦合于统一的分布式线路模型中，并通过矢量拟合实现EMT程序的高效兼容。
  - 提出了一种新型电压与频率相关线路模型(VFDLM)，将电晕效应与频率依赖性直接整合到输电线路的分布式参数公式中。
  - 利用矢量拟合和递归卷积技术求解时域行波方程，实现了与EMT型程序完全兼容的诺顿等效表示。
- **Analysis on Induced Voltages in Wind Farms Close to Distribution Lines on Freque**
  - 💡 将频变土壤模型引入风电塔雷击瞬态与邻近配电线感应电压的耦合分析中，揭示了土壤频率依赖性对过电压传播的关键影响机制。
  - 系统评估了频变土壤参数对风电塔雷击瞬态电压分布的影响
  - 量化了雷击风电塔时对邻近配电线路感应过电压的幅值与波形特征
- **Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents f**
  - 💡 通过梯形积分直接将频域有理导纳模型转换为时域电导与历史电流源并联的Norton支路，避免了复数极点特殊处理并大幅简化了等效电路结构。
  - 提出了一种将高阶有理导纳模型直接转化为Norton等效电路以嵌入EMTP程序的FDNE构建流程。
  - 通过梯形积分将频域导纳矩阵的有理分式转换为时域电导与历史电流源并联结构。
- **Time-Domain Coupling Model for Nonparallel Frequency-Dependent Overhead Multicon**
  - 💡 首次将非平行多导体线路与频变损耗大地的耦合效应以时域闭式方程形式直接嵌入EMT仿真器，兼顾了全波精度与电路仿真效率。
  - 提出了一种适用于非平行、有限长多导体线路的时域色散散射场传输线（DSFTL）模型。
  - 基于修正FDTD算法推导了时域闭式方程，并成功集成至PSCAD/EMTDC仿真平台。
### 2023年 (6篇)
- **Algorithms for fast calculation of energization overvoltage of hybrid overhead l**
  - 💡 融合全频域频变参数提取、相模解耦与改进数值拉普拉斯逆变换，实现了混合输电线路合闸过电压的高精度快速解析计算。
  - 提出了一种基于全频域频率相关参数的混合线路合闸过电压快速计算算法
  - 通过相模解耦与改进数值拉普拉斯逆变换实现了频域到时域的高效转换
- **An Enhanced Method to Achieve Exact DC Values for Frequency-dependent Transmissi**
  - 💡 通过修改有理函数形式并引入低频加权因子强制实现精确直流值，结合降阶技术兼顾了低频拟合精度与EMT仿真计算效率。
  - 提出改进的有理函数逼近方法，强制在0 Hz处实现精确的直流响应值。
  - 引入低频加权因子优化拟合过程，有效提升了低频段精度并抑制了大残差/极点比。
- **Analytical and measurement-based wideband two-port modeling of DC-DC converters **
  - 💡 结合解析推导与终端测量数据，为DC-DC变换器提供高精度、宽频带的两端口黑箱EMT建模新方案。
  - 提出基于模态平均并包含开关效应的解析型两端口导纳建模方法。
  - 开发基于终端测量数据重构变换器两端口导纳模型的黑箱方法。
- **Harmonics Interaction Mechanism and Impact on Extinction Angles in Multi-Infeed **
  - 💡 首次建立MI-HVDC系统谐波传递等效电路模型，实现了计及谐波交互影响的关断角定量计算与并发换相失败机理揭示。
  - 揭示了单端接入与分层接入MI-HVDC系统中交流故障期间谐波的产生与交互机理。
  - 建立了MI-HVDC系统谐波传递的等效电路模型并推导了谐波电压传递系数。
- **Passivity enforcement of wideband model through a new and full perturbation form**
  - 💡 首次提出同时扰动特征导纳与传播函数残差矩阵的完整扰动公式，以最小化整体扰动并实现宽频模型的无源性强制。
  - 提出了一种用于宽频线路和电缆模型无源性强制的新方法。
  - 首次推导并给出了相域中通过传播函数残差进行无源性强制的完整复杂方程组。
- **Wideband model based on constant transformation matrix and rational Krylov fitti**
  - 💡 将RKF算法引入恒定变换矩阵的宽频线路建模中，在揭示恒定T无源性风险的同时实现了低阶高精度的模型拟合。
  - 首次证明恒定变换矩阵的频率点选择会内在破坏传输线系统的无源性。
  - 评估了基于有理Krylov拟合(RKF)的新策略，证明其相比传统矢量拟合能生成更精确且阶数更低的模型。
### 2024年 (5篇)
- **Advanced Wideband Line/Cable Modeling for Transient Studies**
  - 💡 通过最小相位时延优化、自适应模态分组与衰减模态频率限制三项协同改进，从根本上解决了大规模短距离线/缆系统宽频带EMT仿真中的数值不稳定难题。
  - 提出基于最小相位的最优时延计算方法，有效降低传播函数相位角振荡并提高拟合精度。
  - 设计基于时延接近度的自适应模态分组新策略，显著缓解高留数/极点比问题。
- **Comprehensive [formula omitted] impedance modeling of AC power-electronics-based**
  - 💡 首次将具有分布和频率相关参数的完整输电线路模型直接融入AC电力电子系统的DQ阻抗建模中，克服了传统有理近似和时域仿真的局限。
  - 提出了一种直接从频域模型纳入频率相关分布参数输电线路的DQ阻抗建模方法。
  - 开发了基于混合时频谐波平衡法的精确稳态计算方法，避免了时域仿真和快速傅里叶变换。
- **Electromagnetic Transient Analysis Using a Frequency Dependent Network Equivalen**
  - 💡 将离散时间有理函数FDNE与RLS参数辨识结合，实现了含风电系统外部网络的高效降阶电磁暂态建模。
  - 提出基于离散时间有理函数的FDNE模型，实现含风电系统外部网络的高效降阶表征。
  - 结合多频正弦激励与RLS算法，完成边界母线频率相关导纳的精确参数辨识。
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 将复数矢量拟合(CVF)首次引入FDNE导纳/阻抗矩阵综合，并结合C语言并行化实现大幅提升有理逼近的计算性能。
  - 首次将复数矢量拟合(CVF)应用于FDNE的导纳/阻抗矩阵综合，突破了传统算法必须成对处理复共轭极点的限制。
  - 采用C语言及底层线性代数库独立开发VF与CVF算法，彻底摆脱了对MATLAB等商业软件的依赖。
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 首次将复向量拟合(CVF)与并行化C语言实现相结合，突破传统向量拟合的共轭约束与商业软件瓶颈，大幅提升FDNE有理逼近的计算性能。
  - 首次将复向量拟合(CVF)引入FDNE有理逼近，消除了传统方法对复共轭极点的强制约束。
  - 基于C语言与底层线性代数库开发了VF与CVF的并行化实现，摆脱了对商业软件的依赖。
### 2025年 (3篇)
- **FPGA-based simulation of grid-tied converters using frequency-dependent network **
  - 💡 将频率相关网络等值(FDNE)技术与FPGA硬件加速深度融合，在大幅简化外部电网建模的同时，实现了并网变流器系统的高保真、快于实时电磁暂态仿真。
  - 提出了一种基于FPGA的并网变流器实时仿真框架，实现了亚微秒级计算延迟。
  - 引入频率相关网络等值(FDNE)技术，将非研究区域电网简化为频变导纳模型，有效降低系统阶数与计算负担。
- **Improving numerical efficiency of frequency dependent transmission line models f**
  - 💡 将模态截断与平衡截断模型降阶技术应用于频变输电线路传播矩阵优化，在保障精度的前提下大幅提升了大规模电缆系统EMT仿真的数值效率与实时性。
  - 对比了模态截断与平衡截断两种模型降阶技术在频变线路传播矩阵优化中的应用效果。
  - 通过降低矩阵阶数显著减少了大规模多回路电缆系统EMT仿真的计算负担与内存占用。
- **Improving numerical efficiency of frequency dependent transmission line models f**
  - 💡 将模态截断与平衡截断模型降阶技术引入频变输电线路模型，通过降低传播矩阵阶数有效突破大规模电缆系统EMT仿真的计算效率瓶颈。
  - 系统对比了模态截断与平衡截断两种降阶技术在频变线路传播矩阵中的应用效果。
  - 有效降低了高维传播矩阵的阶数，显著提升了大规模电缆系统EMT仿真的数值效率。
### 2026年 (2篇)
- **Harmonic-Preserved Average-Value Model for Converters in Electromagnetic Transie**
  - 💡 将平均值模型的高效计算与谐波分量精确计算融合于统一时域框架，在系统级仿真中同时实现高计算效率与开关级谐波精度。
  - 提出了一种谐波保留平均值模型（HP-AVM），将AVM计算与谐波分量计算集成到统一的时域仿真框架中。
  - 克服了传统AVM忽略开关谐波的缺陷，在系统级仿真中实现了与开关函数模型（SFM）相当的精度。
- **Low-order approximation method for frequency-dependent network equivalent**
  - 💡 通过先定位低阶零极点再结合非线性最小二乘优化，实现了在保证精度的前提下大幅降低有理函数阶数，从而加速电磁暂态仿真。
  - 提出了一种避免冗余零极点的低阶有理函数拟合方法
  - 结合零极点定位与非线性最小二乘法优化，在保证精度的同时显著降低拟合阶数
## 关键发现汇总
- [1998] **Digital Time-Domain Investigation of Transient Behavior of C**: 所建EMTP模型能够精确复现CCVT的铁磁谐振等暂态现象，仿真波形与实测数据高度一致。
- [1998] **Digital Time-Domain Investigation of Transient Behavior of C**: 在故障或开关暂态下，CCVT内部的非线性元件会导致二次侧输出波形显著偏离一次侧输入波形。
- [1998] **Digital Time-Domain Investigation of Transient Behavior of C**: 模型成功量化了不同保护与抑制装置参数对CCVT暂态响应特性的具体影响。
- [2001] **Frequency-dependent transmission line modeling utilizing tra**: 混合模型相比全相域模型计算速度提升3至4倍。
- [2001] **Frequency-dependent transmission line modeling utilizing tra**: 在连续换位条件下模型未牺牲精度，仿真结果高度准确。
- [2001] **Frequency-dependent transmission line modeling utilizing tra**: 当无换位线路时模型可自动退化为标准全相域模型。
- [2003] **A simple and efficient method for including frequency-depend**: 所提方法的计算结果与频域瞬态程序(FTP)的精确解高度一致，验证了模型的理论精度。
- [2003] **A simple and efficient method for including frequency-depend**: 现场测试数据对比表明该方法能准确复现包含频变效应的实际线路瞬态波形。
- [2003] **A simple and efficient method for including frequency-depend**: 相比传统实时卷积法，该方法大幅降低了历史数据存储需求并消除了数值振荡问题。
- [2004] **Frequency-Dependent Transformation Matrices for Untransposed**: NR方法计算出的变换矩阵元素在1 Hz至1 MHz宽频范围内保持连续光滑，消除了传统方法的数值突变。
- [2004] **Frequency-Dependent Transformation Matrices for Untransposed**: 拟合后的模态参数具备实数负极点与零点，可通过梯形法则直接稳定嵌入EMTP时域仿真程序。
- [2004] **Frequency-Dependent Transformation Matrices for Untransposed**: 相比传统对角化算法，NR法在计算效率和多回路非换位线路适用性上具有显著优势。
- [2004] **Multi-port frequency dependent network equivalents for the E**: 等效模型仅由简单RLC模块构成，即可高度还原原网络在宽频范围内的导纳特性。
- [2004] **Multi-port frequency dependent network equivalents for the E**: 在500kV大型电网算例中验证了该方法在保持高精度的同时大幅提升了计算效率。
- [2004] **Multi-port frequency dependent network equivalents for the E**: 相比传统详细建模，该方法显著缩短了仿真时间，特别适用于需大量重复计算的统计分析场景。
- [2005] **Validation of Frequency-Dependent**: 自适应采样策略显著降低了频域计算所需的样本数量，提升了计算效率。
- [2005] **Validation of Frequency-Dependent**: 半解析积分方法有效克服了传统傅里叶变换在长时域计算中的精度与效率瓶颈。
- [2005] **Validation of Frequency-Dependent**: 所提验证流程在架空线路和电缆系统测试中，与高精度相域模型(ULM)的响应结果高度一致。
- [2006] **Inclusion of Frequency-Dependent Soil Parameters in**: 在雷电频段（数百kHz以上），土壤介电常数与电导率量级相当，传统良导体假设不再适用。
- [2006] **Inclusion of Frequency-Dependent Soil Parameters in**: 频率相关土壤参数显著改变了地模传播特性及线路不对称响应。
- [2006] **Inclusion of Frequency-Dependent Soil Parameters in**: 所提一阶模型与高斯积分法在宽频范围内能精确复现大地回路阻抗特性。
- [2008] **Earth Return Impedance of Overhead and Underground Conductor**: 广义公式可统一涵盖Carson、Pollaczek等所有传统大地返回阻抗模型
- [2008] **Earth Return Impedance of Overhead and Underground Conductor**: 所提数值积分方案能直接精确求解多层土壤下的复杂阻抗积分项
- [2008] **Earth Return Impedance of Overhead and Underground Conductor**: 该理论模型为含分层大地的电磁暂态仿真提供了高精度参数计算基础
- [2012] **Frequency Dependent Network Equivalent for Electromagnetic a**: FDNE模型在目标频带内能高精度复现原网络的频率响应特性
- [2012] **Frequency Dependent Network Equivalent for Electromagnetic a**: 无源性强制策略有效避免了混合仿真中的数值发散问题
- [2012] **Frequency Dependent Network Equivalent for Electromagnetic a**: 该方法在保持关键暂态过程精度的同时显著降低了计算规模
- [2012] **电磁–机电暂态混合仿真中的频率相关网络等值**: FDNE能够同时精确表征网络的基频与高频响应特性，有效消除混合仿真接口处的波形畸变。
- [2012] **电磁–机电暂态混合仿真中的频率相关网络等值**: 摄动校正算法成功确保了等值模型的无源性，避免了数值仿真过程中的不稳定发散现象。
- [2012] **电磁–机电暂态混合仿真中的频率相关网络等值**: 算例结果表明该方法在维持高精度的同时，大幅降低了大规模电力系统电磁暂态仿真的计算量。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[new-multiphase-mode-domain-transmission-line-model|New multiphase mode domain transmission line model]] | 1999 |
| [[transmission-line-model-for-variable-step-size-simulation-algorithms|Transmission line model for variable step size simulation al]] | 1999 |
| [[a-wavelet-transform-based-method-for-improved-modeling-of-transmission-lines-pow|A wavelet transform-based method for improved modeling of tr]] | 2001 |
| [[frequency-dependent-transmission-line-modeling-utilizing-transposed-conditions-p|Frequency-dependent transmission line modeling utilizing tra]] | 2001 |
| [[modeling-nonuniform-transmission-lines-for-time-domain-simulation-of-electromagn|Modeling nonuniform transmission lines for time domain simul]] | 2001 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[transmission-line-modeling-with-explicit-grounding-representation|Transmission Line Modeling with Explicit Grounding Represent]] | 2002 |
| [[zfunction-convolution-in-ehv|Z.function convolution in EHV]] | 2002 |
| [[a-simple-and-efficient-method-for-including-frequency-dependent-effects-in-trans|A simple and efficient method for including frequency-depend]] | 2003 |
| [[a-z-transform-model-of-transformers-for-the-study-of-electromagnetic-transients-|A Z-transform model of transformers for the study of electro]] | 2004 |
| [[combined-transient-and-dynamic-analysis-of-hvdc-and-facts-systems|Combined transient and dynamic analysis of HVDC and FACTS sy]] | 2004 |
| [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on|EMTP Modeling Of Electromagnetic Transients - Power Delivery]] | 2004 |
| [[emtp-modeling-of-electromagnetic-transients-power-delivery-ieee-transactions-on|EMTP Modeling Of Electromagnetic Transients - Power Delivery]] | 2004 |
| [[frequency-dependent-transformation-matrices-for-untransposed-transmission-lines-|Frequency-Dependent Transformation Matrices for Untransposed]] | 2004 |
| [[mode-domain-multiphase-transmission-line-model-use-in-transient-studies-power-de|Mode domain multiphase transmission line model - use in tran]] | 2004 |
| [[modelling-of-single-phase-nonuniform-transmission-lines-in-electromagnetic-trans|Modelling of Single-Phase Nonuniform Transmission Lines in E]] | 2004 |
| [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i|Multi-port frequency dependent network equivalents for the E]] | 2004 |
| [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del|Rational approximation of frequency domain responses by vect]] | 2004 |
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha|State equation approximation of transfer matrices and its ap]] | 2004 |
| [[suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie|Suppression of numerical oscillations in the EMTP power syst]] | 2004 |
| [[three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow|Three phase transformer modelling for fast electromagnetic t]] | 2004 |
| [[a-systematic-approach-to-the-evaluation|A Systematic Approach to the Evaluation]] | 2005 |
| [[a-new-procedure-to-derive-transmission-line-parameters-applications-and-restrict|A new procedure to derive transmission-line parameters Appli]] | 2005 |
| [[a-new-procedure-to-derive-transmission-line-parameters-applications-and-restrict|A new procedure to derive transmission-line parameters Appli]] | 2005 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[validation-of-frequency-dependent|Validation of Frequency-Dependent]] | 2005 |
| [[inclusion-of-frequency-dependent-soil-parameters-in|Inclusion of Frequency-Dependent Soil Parameters in]] | 2006 |
| [[potential-risk-of-failures-in-switching-ehv-shunt-reactors|Potential risk of failures in switching EHV shunt reactors]] | 2006 |
| [[potential-risk-of-failures-in-switching-ehv-shunt-reactors|Potential risk of failures in switching EHV shunt reactors]] | 2006 |
| [[noda-a-binary-frequency-region-partitioning-algorithm-for-the-identification-of-|Noda | A Binary Frequency-Region Partitioning Algorithm for ]] | 2007 |
| [[real-time-transient-simulation-based-on-a-robust|Real-Time Transient Simulation Based on a Robust]] | 2007 |
| [[passivity-enforcement-for-transmission-line-models|Passivity Enforcement for Transmission Line Models]] | 2008 |
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[fast-realization-of-the-modal-vector-fitting|Fast Realization of the Modal Vector Fitting]] | 2009 |
| [[improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an-fix|Improvement of Numerical Stability for the Computation of Tr]] | 2010 |
| [[robust-passivity-enforcement-scheme-for|Robust Passivity Enforcement Scheme for]] | 2010 |
| [[analyses-of-the-modifications-in-the-pi-circuits-for-inclusion-of-frequency-infl|Analyses of the modifications in the pi circuits for inclusi]] | 2011 |
| [[application-of-pi-circuits-for-simulation-of-corona-effect-in-transmission-lines|Application of pi circuits for simulation of corona effect i]] | 2011 |
| [[parametric-study-of-transient-electromagnetic-fields|Parametric Study of Transient Electromagnetic Fields]] | 2011 |
| [[proposal-of-an-alternative-transmission-line-model-for-symmetrical-and-asymmetri|Proposal of an alternative transmission line model for symme]] | 2011 |
| [[a-type-4-wind-power-plant-equivalent-model|A Type-4 Wind Power Plant Equivalent Model]] | 2012 |
| [[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical|Frequency Dependent Network Equivalent for Electromagnetic a]] | 2012 |
| [[modal-domain-based-modeling-of-parallel-transmission-lines|Modal Domain Based Modeling of Parallel Transmission Lines]] | 2012 |
| [[time-domain-transformation-method|Time Domain Transformation Method]] | 2012 |
| [[基于频率相关网络等值的电磁-机电暂态解耦混合仿真|基于频率相关网络等值的电磁-机电暂态解耦混合仿真]] | 2012 |
| [[电磁机电暂态混合仿真中机电侧故障的仿真方法|电磁–机电暂态混合仿真中机电侧故障的仿真方法]] | 2012 |
| [[电磁机电暂态混合仿真中的频率相关网络等值|电磁–机电暂态混合仿真中的频率相关网络等值]] | 2012 |
| [[fast-and-efficient-calculation-of-lightning-induced-voltages-in-frequency-depend|Fast and efficient calculation of lightning-induced voltages]] | 2013 |
| [[published-in-iet-generation-transmission-distribution|Multi-FPGA digital hardware design for detailed large-scale ]] | 2013 |
| [[published-in-iet-generation-transmission-distribution-27&28|Numerical Integration by the 2-Stage Diagonally Implicit Run]] | 2013 |
| [[fitting-the-frequency-dependent-parameters-in-the-bergeron-line-model|Fitting the frequency-dependent parameters in the Bergeron l]] | 2014 |
| [[proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca|Proximity effect in fast transient simulations of an undergr]] | 2014 |
| [[analysing-a-power-transformers-internal-response-to-system-transients-using-a-hy|Analysing a power transformer⠒s internal response to system ]] | 2015 |
| [[application-of-frequency-partitioning-fitting-to-the-phase-domain-frequency-depe|Application of Frequency-Partitioning Fitting to the Phase-D]] | 2015 |
| [[duality-based-transformer-model-including-13&14|Duality-Based Transformer Model Including]] | 2015 |
| [[frequency-domain-simulation-of-electromagnetic-transients-using-variable|Frequency-Domain Simulation of Electromagnetic Transients Us]] | 2015 |
| [[frequency-dependent-multiconductor-line-model-based-on-the-bergeron-method|Frequency-dependent multiconductor line model based on the B]] | 2015 |
| [[loewner-matrix-approach-for-modelling-fdnes-of-power-systems|Loewner matrix approach for modelling FDNEs of power systems]] | 2015 |
| [[a-wideband-equivalent-model-of-type-3-wind-power-plants-for-emt-studies|A Wideband Equivalent Model of Type-3 Wind Power Plants for ]] | 2016 |
| [[an-efficient-and-accurate-calculation-of-electric-field-and-temperature-distribu|An Efficient and Accurate Calculation of Electric Field and ]] | 2016 |
| [[frequency-dependent-line-model-in-the-time-domain-for-simulation-of-fast-and-imp|Frequency-dependent line model in the time domain for simula]] | 2016 |
| [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o|Influence of frequency characteristics of soil on lightning ]] | 2016 |
| [[influence-of-frequency-characteristics-of-soil-on-lightning-transient-response-o|Influence of frequency characteristics of soil on lightning ]] | 2016 |
| [[a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat|A full frequency dependent line model based on folded line e]] | 2017 |
| [[modal-decoupling-of-overhead-transmission-lines-using-real-and-constant-matrices|Modal decoupling of overhead transmission lines using real a]] | 2017 |
| [[2728multi-scale-and-frequency-dependent-modeling-of-electric-power-transmission-|Multi-scale and Frequency-dependent Modeling of Electric Pow]] | 2017 |
| [[accelerated-frequency-dependent-method-of-characteristics-for-the-simulation-of-|Accelerated frequency-dependent method of characteristics fo]] | 2018 |
| [[development-and-applicability-of-online-passivity-enforced-wide-band-multi-port-|Development and Applicability of Online Passivity Enforced W]] | 2018 |
| [[efficiently-computing-the-electrical-parameters-of-cables-with-arbitrary-cross-s|Efficiently computing the electrical parameters of cables wi]] | 2018 |
| [[fast-electromagnetic-transient-model-for-mmc-hvdc-considering-dc-fault|Fast Electromagnetic Transient Model for MMC-HVDC Considerin]] | 2018 |
| [[new-investigations-on-the-method-of-characteristics-for-the-evaluation-of-line-t|New investigations on the method of characteristics for the ]] | 2018 |
| [[partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran|Partitioned Fitting and DC Correction for the Simulation of ]] | 2018 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[a-multi-rate-co-simulation-of-combined-phasor-domain-and-time-domain-models-for-|A Multi-rate Co-simulation of Combined Phasor-Domain and Tim]] | 2019 |
| [[grounding-grids-in-electro-magnetic-transient-simulations-with-frequency-depende|Grounding grids in electro-magnetic transient simulations wi]] | 2019 |
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency-dependent model of a HVDC transf]] | 2019 |
| [[modeling-a-voltage-source-converter-assisted-resonant-current-dc-breaker-for-rea|Modeling a voltage source converter assisted resonant curren]] | 2019 |
| [[multi-layer-earth-structure-approximation-by-a-homogeneous-conductivity-soil-for|Multi-layer Earth Structure Approximation by a Homogeneous C]] | 2019 |
| [[compacting-and-partitioningbased-simulation-solution-for-frequencydependent-netw|Compacting and partitioning‐based simulation solution for fr]] | 2020 |
| [[effect-of-frequency-dependent-soil-parameters-on-wave-propagation-and-transient-|Effect of frequency-dependent soil parameters on wave propag]] | 2020 |
| [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb|Partitioned fitting and DC correction in transmission line/c]] | 2020 |
| [[passivity-enforcement-of-wideband-line-model-through-coupled-perturbation-of-res|Passivity enforcement of wideband line model through coupled]] | 2020 |
| [[real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid|Real-time simulation with an industrial DCCB controller in a]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-|Simulation of electromagnetic transients with Modelica, accu]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc|Time-Domain Implementation of Damping Factor White-Box Trans]] | 2020 |
| [[an-accurate-analysis-of-lightning-overvoltages-in-mixed-overhead-cable-lines|An accurate analysis of lightning overvoltages in mixed over]] | 2021 |
| [[an-efficient-analytical-based-technique-to-numerical-calculation-of-extended-ear|An efficient analytical based technique to numerical calcula]] | 2021 |
| [[an-improved-passivity-enforcement-algorithm-for-transmission-line-models-using-p|An improved passivity enforcement algorithm for transmission]] | 2021 |
| [[analysis-of-frequency-dependent-network-equivalents-in-dynamic-harmonic-domain|Analysis of Frequency-Dependent Network Equivalents in Dynam]] | 2021 |
| [[comparison-of-dynamic-phasor-discrete-time-and-frequency-scanning-based-ssr-mode|Comparison of dynamic phasor, discrete-time and frequency sc]] | 2021 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[earth-return-admittance-impact-on-crossbonded-underground-cables|Earth return admittance impact on crossbonded underground ca]] | 2021 |
| [[evaluation-of-the-extended-modal-domain-model-in-the-calculation-of-lightning-in|Evaluation of the extended modal-domain model in the calcula]] | 2021 |
| [[expanding-the-measuring-range-via-s-parameters-in-a-ehv-voltage-transformer-mode|Expanding the measuring range via S-parameters in a EHV volt]] | 2021 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth-19、20、21|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[generalized-formulation-of-overhead-line-parameters-for-multi-layer-earth|Generalized Formulation of Overhead Line Parameters for Mult]] | 2021 |
| [[implementation-of-the-universal-line-model-in-the-alternative-transients-program|Implementation of the universal line model in the alternativ]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[large-scale-hybrid-real-time-simulation-modeling-and-benchmark-for-nelson-river-|Large-scale hybrid real time simulation modeling and benchma]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie|Modeling of overhead transmission lines for trapped charge d]] | 2021 |
| [[multi-scale-formulation-of-admittance-based-modeling-of-cables|Multi-scale formulation of admittance-based modeling of cabl]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin|Review and comparison of frequency-domain curve-fitting tech]] | 2021 |
| [[考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型|考虑中间变压器饱和特性的电容式电压互感器宽频非线性模型]] | 2021 |
| [[a-new-approach-to-represent-the-corona-effect-and-frequency-dependent-transmissi|A New Approach to Represent the Corona Effect and Frequency-]] | 2022 |
| [[a-modified-implementation-of-the-folded-line-equivalent-transmission-line-model-|A modified implementation of the Folded Line Equivalent tran]] | 2022 |
| [[algorithm-for-fast-calculating-the-energization-overvoltages-along-a-power-cable|Algorithm for fast calculating the energization overvoltages]] | 2022 |
| [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f|Efficient Implementation of Multi-Port Frequency Dependent N]] | 2022 |
| [[implementation-of-modal-domain-transmission-line-models-in-the-atp-software|Implementation of Modal Domain Transmission Line Models in t]] | 2022 |
| [[new-compact-white-box-transformer-model-for-the-calculation-of-electromagnetic-t|New Compact White-Box Transformer Model for the Calculation ]] | 2022 |
| [[time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon|Time-Domain Coupling Model for Nonparallel Frequency-Depende]] | 2022 |
| [[using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet|Using the Exact Equivalent &#x03C0;-Circuit of Transmission ]] | 2022 |
| [[大规模电力电子设备接入的电力系统混合仿真接口技术综述|大规模电力电子设备接入的电力系统混合仿真接口技术综述]] | 2022 |
| [[a-new-tool-for-calculation-of-line-and-cable-parameters|A new tool for calculation of line and cable parameters]] | 2023 |
| [[admittance-based-modelling-of-cables-and-overhead-lines-by-idempotent-decomposit|Admittance-based modelling of cables and overhead lines by i]] | 2023 |
| [[algorithms-for-fast-calculation-of-energization-overvoltage-of-hybrid-overhead-l|Algorithms for fast calculation of energization overvoltage ]] | 2023 |
| [[alternative-method-to-include-the-frequency-effect-on-transmission-line-paramete|Alternative method to include the frequency-effect on transm]] | 2023 |
| [[an-enhanced-method-to-achieve-exact-dc-values-for-frequency-dependent-transmissi|An Enhanced Method to Achieve Exact DC Values for Frequency-]] | 2023 |
| [[impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables|Impact of solenoid effects on series impedance of three-core]] | 2023 |
| [[optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e|Optimized high-frequency white-box transformer model for imp]] | 2023 |
| [[passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form|Passivity enforcement of wideband model through a new and fu]] | 2023 |
| [[switch-averaged-frequency-domain-simulation-of-photovoltaic-systems|Switch-Averaged Frequency Domain Simulation of Photovoltaic ]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an|Tower-foot grounding model for EMT programs based on transmi]] | 2023 |
| [[wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti|Wideband model based on constant transformation matrix and r]] | 2023 |
| [[双导体有损频变均匀传输线的电磁暂态时域仿真模型研究|双导体有损频变均匀传输线的电磁暂态时域仿真模型研究]] | 2023 |
| [[双导体有损频变均匀传输线的电磁暂态时域仿真模型研究|双导体有损频变均匀传输线的电磁暂态时域仿真模型研究]] | 2023 |
| [[comprehensive-formula-omitted-impedance-modeling-of-ac-power-electronics-based-p|Comprehensive [formula omitted] impedance modeling of AC pow]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend-17|Enhancing computation performance of rational approximation ]] | 2024 |
| [[enhancing-computation-performance-of-rational-approximation-for-frequency-depend|Enhancing computation performance of rational approximation ]] | 2024 |
| [[time-domain-modeling-of-a-subsea-buried-cable|Time-domain modeling of a subsea buried cable]] | 2024 |
| [[efficient-modeling-of-parallel-counterpoise-wires-using-an-fdtd-based-transmissi|Efficient modeling of parallel counterpoise wires using an F]] | 2025 |
| [[electromagnetic-transient-model-reconstruction-of-generalized-power-transmission|Electromagnetic Transient Model Reconstruction of Generalize]] | 2025 |
| [[frequency-and-transient-responses-of-a-275-kv-pressure-oil-filled-cable-model-va|Frequency and transient responses of A 275 kV pressure oil-f]] | 2025 |
| [[high-accuracy-emt-simulations-through-pole-residue-compensation|High-accuracy EMT simulations through pole-residue compensat]] | 2025 |
| [[improving-emt-simulations-using-frequency-shifted-rational-approximations|Improving EMT simulations using frequency-shifted rational a]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f|Improving numerical efficiency of frequency dependent transm]] | 2025 |
| [[influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss|Influence of approximate internal impedance formula on half-]] | 2025 |
| [[realization-of-rational-models-for-tower-footing-grounding-systems|Realization of rational models for tower-footing grounding s]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator|The fdLoad model for accurate frequency dynamics in the SFA-]] | 2025 |
| [[z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit|Z-Tool: Frequency-domain characterization of EMT models for ]] | 2025 |
| [[low-order-approximation-method-for-frequency-dependent-network-equivalent|Low-order approximation method for frequency-dependent netwo]] | 2026 |
| [[time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models|Time-delay estimation through all-pass functions for ULM lin]] | 2026 |