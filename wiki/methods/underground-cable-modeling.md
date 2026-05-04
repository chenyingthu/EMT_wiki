---
title: "地下电缆建模 (Underground Cable Modeling)"
type: method
tags: [underground-cable, cable, modeling, emt, distribution]
created: "2026-05-02"
---

# 地下电缆建模 (Underground Cable Modeling)

## 定义与边界

地下电缆建模是在 EMT 中把导体、绝缘、金属护套、铠装、外护套、土壤和接地连接共同表示为可求解电路或端口模型的方法。它关注电缆端口电压、电流、护套电压、护套电流、传播延时、频变损耗和过电压响应，而不是单纯的稳态载流量或土建敷设设计。

本页讨论电缆作为 EMT 线路/网络元件的建模。热稳定、老化、敷设经济性和标准试验只在它们改变电气参数或验证边界时出现。海底埋设电缆、交叉互联和接地网属于相邻问题，应分别与 [[cross-bonded-cable]]、[[grounding-system-modeling]] 和 [[earth-return-impedance]] 连接。

## EMT 中的作用

地下电缆在 EMT 中通常用于研究：

- 电缆投切、重燃、故障清除和雷电侵入波造成的导体与护套过电压。
- 高电容、低波阻抗线路对开关暂态、谐振和保护动作的影响。
- 单芯电缆护套接地方式对零序通道、护套感应电压和环流的影响。
- 海底、城市地下和架空-电缆混合线路中的频变传播、反射和损耗。
- 电缆参数模型与 [[universal-line-model]]、[[bergeron-line-model]]、[[frequency-dependent-line-model]] 或节点导纳型实现之间的接口。

如果电缆被简化成单一工频阻抗或短段 PI 等值，可能足以做低频近似，但不应默认适用于雷电、陡波或宽频谐振研究。

## 核心机制

多导体电缆频域模型通常从单位长度矩阵开始：

$$-\frac{\partial \mathbf{v}}{\partial x}=\mathbf{Z}'(\omega)\mathbf{i},\quad
-\frac{\partial \mathbf{i}}{\partial x}=\mathbf{Y}'(\omega)\mathbf{v}$$

其中 $\mathbf{v}$ 和 $\mathbf{i}$ 可包含芯线、金属护套、铠装或回流导体的相域变量。串联阻抗可概念性分解为：

$$\mathbf{Z}'(\omega)=\mathbf{Z}_\text{core}(\omega)+\mathbf{Z}_\text{sheath}(\omega)+\mathbf{Z}_\text{mutual}(\omega)+\mathbf{Z}_\text{earth}(\omega)$$

并联导纳描述绝缘层、半导电层和外部介质的电容/损耗：

$$\mathbf{Y}'(\omega)=\mathbf{G}'(\omega)+j\omega\mathbf{C}'(\omega)$$

进入 EMT 时有两类常见接口。传播函数路线计算特征导纳 $\mathbf{Y}_c(\omega)$ 与传播矩阵 $\mathbf{H}(\omega)$，再通过延时和递归卷积形成历史电流源。节点导纳路线直接拟合整段电缆端口关系：

$$\begin{bmatrix}\mathbf{i}_1\\ \mathbf{i}_2\end{bmatrix}
=\mathbf{Y}_n(\omega)
\begin{bmatrix}\mathbf{v}_1\\ \mathbf{v}_2\end{bmatrix}$$

时域实现可把 $\mathbf{Y}_n$ 或其分解形式拟合成稳定有理函数，形成固定导纳、历史项和内部状态变量。

## 分类与变体

| 建模路线 | 核心处理 | 适合用途 | 主要边界 |
|----------|----------|----------|----------|
| 集总 PI/多段 PI | 把电缆分成 RLCG 段 | 短段、低频、初始化 | 分段长度和高频传播误差需检查 |
| 常参数行波模型 | 使用固定 $Z_c$ 与传播延时 | 中低频行波教学或粗略暂态 | 不充分表示集肤、邻近和大地返回频变 |
| 相域频变线路模型 | 拟合 $\mathbf{Y}_c$、$\mathbf{H}$ 或 $\mathbf{Y}_n$ | 宽频过电压、地下/海底电缆 | 依赖参数计算、拟合和无源性 |
| 节点导纳/FLE 路线 | 直接拟合端口导纳或开路/短路块 | 短电缆、多尺度仿真、强频变电缆 | 需要低频极限、历史项和步长切换检查 |
| 场-路或全波校核 | 用场模型计算局部参数/响应 | 附件、复杂介质、研究级验证 | 计算量和输入数据要求高 |

## 建模流程

1. 明确电缆结构：芯线数量、护套/铠装、绝缘层、屏蔽层、接地箱、终端和接头。
2. 定义 EMT 变量：导体相电压、电缆端口电流、护套电位、护套电流、接地点电流或等效端口量。
3. 计算宽频参数：导体集肤/邻近效应、护套耦合、介质损耗、[[earth-return-impedance]] 和 [[frequency-dependent-soil]]。
4. 选择时域实现：PI 分段、[[bergeron-line-model]]、[[universal-line-model]]、FLE 或节点导纳有理拟合。
5. 检查数值条件：传播延时与时间步长、拟合频带、极点稳定性、无源性、低频/DC 极限和端口方向约定。
6. 用目标工况验证：开关、故障、雷电或频扫工况应与模型选择一致，不能用低频稳态通过来证明高频暂态可信。

## 适用边界与失败模式

- 电缆参数对几何、土壤、护套连接和介质参数敏感；缺少这些输入时只能给出方法级结论。
- 护套接地方式改变零序路径和暂态护套电位；不能把芯线模型与护套/接地模型割裂。
- 高频暂态下，节点导纳拟合、延时插值和无源性处理可能比线路方程本身更决定时域稳定性。
- 海底埋设电缆的外部介质可能同时包含海水和海床有损路径；普通地下电缆参数例程未必覆盖该边界。
- 论文中的算例长度、步长、误差或加速结论只对其参数与对比基线有效，不应写成电缆建模通用保证。

## 代表性证据

- [[multi-scale-formulation-of-admittance-based-modeling-of-cables]]：支撑节点导纳型电缆模型可作为短电缆和多尺度 EMT/机电暂态接口；该 source 明确提醒不能外推为固定加速倍数或任意拓扑有效。
- [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb]]：支撑宽频线路/电缆模型需要处理 DC 或低频拟合边界，尤其在 HVDC 线路/电缆场景中。
- [[time-domain-modeling-of-a-subsea-buried-cable]]：支撑海底埋设电缆需要把海水与海床双有损介质纳入参数计算，并比较 MoC/ULM 与 FLE 节点导纳路线；结论限于原文海缆算例和 NLT 对比。
- [[cable-modeling]]：提供电缆建模主题层的文献入口，不替代具体 source 页证据。

## 与相关页面的关系

- [[cable-model]] 是电缆作为模型对象的页面，本页是方法组织。
- [[cross-bonded-cable]] 处理单芯电缆护套交叉互联和接地箱连接。
- [[grounding-system-modeling]] 与 [[ground-potential-rise]] 处理接地系统和地电位升。
- [[earth-return-impedance]]、[[frequency-dependent-soil]] 和 [[frequency-dependent-soil-model]] 决定外部回流路径参数。
- [[lightning-transient-analysis]]、[[high-frequency-transient-analysis]] 和 [[insulation-coordination]] 使用电缆模型评估过电压和保护裕度。

## 开放问题

- 电缆附件、接头、护层保护器和局部接地箱的宽频参数往往比主电缆段更缺少可复核数据。
- 多段电缆-架空线混合线路中的拟合频带、延时插值和过电压保护设备模型需要共同验证。
- 频变土壤、海底介质和护套连接的不确定性应通过敏感性分析或现场测量约束，而不是用单一典型参数代替。
