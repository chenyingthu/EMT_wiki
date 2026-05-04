# 机电-电磁暂态混合仿真 (Electromechanical-Electromagnetic Hybrid Simulation)

## 定义与边界

机电-电磁暂态混合仿真把电力系统划分为机电暂态相量域和电磁暂态瞬时值域，并通过接口在同一仿真任务中交换边界信息。机电侧通常描述发电机转子、励磁、调速、负荷和大规模网络的基频动态；EMT 侧描述三相瞬时电压电流、开关、电力电子控制、非线性元件和快速故障暂态。

它是 [[hybrid-modeling]] 的专门形式，不等同于所有混合建模；它依赖 [[interface-technique]]，但接口技术本身还覆盖纯 EMT 分区、场路耦合和工具协同。

## EMT 中的作用

该方法用于研究“局部快速电磁过程会影响系统级慢动态，或系统级慢动态会改变局部 EMT 响应”的问题。例如 HVDC、FACTS、MMC、风电和光伏并网研究中，研究区可能需要 EMT 细节，而远端交流系统只需机电暂态表示。若研究目标只关心大系统功角稳定，可使用 [[electromechanical-simulation]]；若研究目标由开关、谐波、非对称故障或保护采样主导，应扩大 EMT 区域或使用全 EMT 验证。

## 域间变量转换

### 机电侧到 EMT 侧

机电侧输出通常是基频相量。接口需要把相量转换为 EMT 三相瞬时源：

$$
v_a(t) = \sqrt{2}|V|\cos(\omega t + \theta)
$$

$$
v_b(t) = \sqrt{2}|V|\cos(\omega t + \theta - 2\pi/3), \quad
v_c(t) = \sqrt{2}|V|\cos(\omega t + \theta + 2\pi/3)
$$

若存在负序、零序或频率偏移，应说明是否使用序分量、动态相量或 abc 相域接口。

### EMT 侧到机电侧

EMT 侧输出是瞬时波形。机电侧通常需要基频正序相量、功率或等效注入：

$$
\hat{V}_1(t_k) = \mathcal{P}\{v_a(t), v_b(t), v_c(t)\}
$$

其中 $\mathcal{P}$ 表示相量提取算子，可能是 DFT、dq 低通滤波、PLL 或动态相量估计。相量提取必须说明窗口长度、参考角、滤波延迟和不平衡处理。

## 接口等值

常见机电侧外部网络等值包括：

- Thevenin/Norton 基频等值：适合研究频带主要在基频附近、接口波形较平稳的场景。
- 多端口等值：保留多个接口母线之间的耦合。
- [[fdne-model]]：用频率相关导纳或阻抗表示外部网络宽频响应，适合接口处谐波或快速暂态不能忽略的场景。
- 动态相量接口：在相量域保留有限频带的调制分量，作为全 EMT 与传统机电模型之间的折中。

接口处至少应检查功率符号、电流方向、相量基准、基准容量和三相序分量定义。

## 多速率工作流

1. 初始化潮流，建立机电侧相量状态和 EMT 侧瞬时状态。
2. 根据研究对象选择接口母线和 EMT 详细区域。
3. 机电侧形成外部网络等值，EMT 侧把该等值实现为受控源、导纳或频率相关网络。
4. EMT 侧在多个小步长内推进，并记录接口电压电流。
5. 在机电交换时刻提取相量或功率，更新机电侧网络注入。
6. 机电侧推进一个或多个大步长，回传新的边界相量或等值参数。
7. 若采用并行或松耦合时序，使用预测、迭代或补偿检查接口功率偏差和相角延迟。

## 主要变体

- 串行混合仿真：实现简单，接口因果关系清晰，但存在数据等待和延迟。
- 并行混合仿真：适合实时或分布式计算，但需要预测校正和稳定性验证。
- 动态相量接口：在相量域保留部分非基频动态，减轻瞬时波形到基频相量的损失。
- FDNE 外部网络：保留外部系统频率响应，但需要拟合、无源性检查和时域实现。
- 模式切换混合仿真：扰动前后在相量、平均和 EMT 详细模型之间切换，必须处理状态一致性。

## 适用边界与失败模式

- 接口相量提取会引入窗口延迟，故障初期波形可能不能立即转化为可靠基频量。
- 基频等值不能表达超出其假设的谐波、行波或高频谐振。
- 非对称故障需要明确负序和零序如何在两侧传递。
- 接口位置过近可能把强畸变波形直接交给机电模型；接口位置过远会增加 EMT 区域规模。
- 并行时序和实时通信可能引入相角误差或能量不平衡。
- 机电侧控制、保护和限幅若与 EMT 侧实现不一致，混合结果可能由模型语义差异主导。

## 代表性证据与证据边界

该类论文常以具体 HVDC、VSC、MMC、SVC 或新能源接入算例验证接口策略。页面不应把单一算例中的误差、加速比、平台规模或实时性结果写成通用能力。任何数值结论都应绑定来源、系统规模、步长、接口位置、频带和对比基准。

可作为来源入口的页面包括 [[interfacing-techniques-for-transient-stability-and-electromagnetic-transient-hyb]]、[[frequency-dependent-network-equivalent-for-electromagnetic-and-electromechanical]]、[[dynamic-phasor-based-interface-model-for-emt-and-transient-stability-hybrid-simu]]、[[hybrid-transient-stability-simulation-using-dynamic-phasor-based-interface-model]] 和 [[application-of-electromagnetic-transient-transient-stability-hybrid-simulation-t]]。

## 与相关页面的关系

- [[hybrid-modeling]]：更一般的模型层级和物理域组合方法。
- [[interface-technique]]：接口变量、等值和时序的总览。
- [[fdne-model]]：机电侧外部网络的宽频等值模型。
- [[phasor-model]]：机电侧相量模型的基础。
- [[phase-domain-modeling]]：EMT 侧 abc 瞬时模型的基础。
- [[dq-transformation]]：相量提取和控制坐标变换常用工具。
- [[transient-stability]]：机电侧稳定性指标背景。
