---
title: "Electromagnetic transient (EMT) and quasi static time series (QSTS) Co-simulation for analyzing integration of power electronics based generation/power quality improvement solution in secondary distribution networks"
type: source
authors: ['Dhaval', 'Yogeshbhai', 'Raval']
year: 2026
journal: "Electric Power Systems Research, 253 (2026) 112572. doi:10.1016/j.epsr.2025.112572"
tags: ['cosimulation']
created: "2026-04-13"
sources: ["EMT_Doc/15/Electromagnetic transient (EMT) and quasi static time series (QSTS) Co-simulation for analyzing inte_Raval和Pandya_2026.pdf"]
---

# Electromagnetic transient (EMT) and quasi static time series (QSTS) Co-simulation for analyzing integration of power electronics based generation/power quality improvement solution in secondary distribution networks

**作者**: Dhaval, Yogeshbhai, Raval
**年份**: 2026
**来源**: `15/Electromagnetic transient (EMT) and quasi static time series (QSTS) Co-simulation for analyzing inte_Raval和Pandya_2026.pdf`

## 摘要

Electromagnetic transient (EMT) and quasi static time series (QSTS) Co-simulation for analyzing integration of power electronics based generation/power quality improvement solution in secondary distribution a Ph.D. Scholar, Gujarat Technological University, 380005, Chandkheda Ahmedabad, Gujarat, India b Vishwakarma Government Engineering College, 380005, Chandkheda Ahmedabad, Gujarat, India

## 核心贡献


- 提出基于OpenDSS与Simulink耦合的联合仿真框架
- 设计基于戴维南等效提取的接口算法实现跨域数据交互
- 构建兼顾控制器级精度与计算效率的配电网混合仿真平台


## 使用的方法


- [[联合仿真|联合仿真]]
- [[准静态时间序列分析|准静态时间序列分析]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[戴维南等效提取|戴维南等效提取]]
- [[com接口通信|COM接口通信]]
- [[时序潮流计算|时序潮流计算]]


## 涉及的模型


- [[光伏系统|光伏系统]]
- [[电力电子发电机|电力电子发电机]]
- [[ieee-13节点测试馈线|IEEE 13节点测试馈线]]
- [[电能质量改善装置|电能质量改善装置]]
- [[戴维南等效网络|戴维南等效网络]]


## 相关主题


- [[混合仿真|混合仿真]]
- [[可再生能源并网|可再生能源并网]]
- [[电能质量分析|电能质量分析]]
- [[配电网仿真|配电网仿真]]
- [[高比例分布式电源|高比例分布式电源]]


## 主要发现


- 联合仿真结果与全电磁暂态模型高度吻合验证了框架准确性
- 相比全电磁暂态仿真计算时间显著降低约百分之六十至七十
- 在辐照度波动无功调节及电网故障工况下均保持良好动态响应



## 方法细节

### 方法概述

提出一种基于OpenDSS与MATLAB/Simulink的EMT-QSTS联合仿真框架。OpenDSS负责配电网的准静态时间序列（QSTS）潮流计算，通过COM接口与MATLAB通信。MATLAB脚本作为数据交互中枢，采用基于连续测量样本的戴维南等效提取算法，将OpenDSS输出的节点电压、电流及功率数据实时转换为等效电压源$E_{th}$和阻抗$Z_{th}$，并注入Simulink中的电力电子（PE）发电机EMT模型。Simulink完成高频暂态仿真后，将注入电网的有功/无功功率反馈至OpenDSS进行下一时间步迭代。该架构有效克服了OpenDSS无法模拟高频电力电子动态的局限，同时避免了全EMT仿真在大规模配电网长时序分析中的计算瓶颈，并预留了硬件在环（HIL）接口。

### 数学公式


**公式1**: $$$$V_z = \frac{X_{th}}{2\pi f} \frac{di_L}{dt} + R_{th} I_L$$$$

*EMT域中戴维南等效阻抗上的压降模型，用于构建受控电压源*


**公式2**: $$$$\Delta V^2 + 2\Delta P r_{th} + 2\Delta Q x_{th} = 0$$$$

*戴维南等效参数提取的线性化方程，通过连续时间步的电压、有功、无功变化量求解等效电阻与电抗*


**公式3**: $$$$r_{th} = \frac{\Delta Q_j \Delta V_k^2 - \Delta Q_k \Delta V_j^2}{2(\Delta P_j \Delta Q_k - \Delta P_k \Delta Q_j)}$$$$

*基于行列式差分法计算等效电阻$r_{th}$的解析解*


**公式4**: $$$$E_{th} = \sqrt{V_{Ln}^2 + I_{Ln}^2 (r_{th}^{*2} + x_{th}^{*2}) + 2P_n r_{th}^* + 2Q_n x_{th}^*}$$$$

*根据提取的最优阻抗和当前测量值计算戴维南等效电压幅值*


**公式5**: $$$$E_k = \frac{P_k - P_{k-1}}{V_k - V_{k-1}}$$$$

*模糊MPPT控制器的误差输入，反映P-V曲线斜率*


**公式6**: $$$$D > 1 - \frac{m_a \times N_S \times V_{mpp}}{V_{grid(RMS)} \times \sqrt{2}}$$$$

*Boost解耦变换器占空比设计下限，确保直流母线电压匹配电网需求*


### 算法步骤

1. 步骤1：建立MATLAB与OpenDSS之间的COM接口通信链路，配置数据读写权限与同步标志。

2. 步骤2：在OpenDSS中执行初始潮流计算，获取系统稳态初始值，并同步初始化Simulink中的EMT仿真环境。

3. 步骤3：在MATLAB中定义感兴趣节点（POI）及数据交互变量，设置联合仿真时间步长与同步机制。

4. 步骤4：将上一轮EMT仿真计算得到的分布式电源注入有功功率和无功功率值，通过COM接口更新写入OpenDSS模型。

5. 步骤5：在OpenDSS中执行当前QSTS时间步的配电网潮流分析，求解全网节点电压与支路电流。

6. 步骤6：通过MATLAB API从OpenDSS读取POI节点的潮流计算结果（包括$V_L, I_L, P, Q$等）。

7. 步骤7：利用MATLAB脚本中的戴维南等效提取算法，基于连续$n$个时间步的测量数据构建差分方程组，计算多组$(r_{th}, x_{th})$候选值。

8. 步骤8：对候选阻抗值进行众数（mode）统计分析，筛选出最优等效参数$r_{th}^*$和$x_{th}^*$，并代入公式计算$E_{th}$，随后更新至Simulink EMT模型。

9. 步骤9：在Simulink中运行EMT仿真，仿真时长为$T_{EMT}$，内部求解步长$T_s \ll T_{EMT}$，精确模拟电力电子开关动态与控制器响应。

10. 步骤10：EMT仿真结束后，提取PCC点的功率交换数据及关键状态变量，返回至MATLAB工作区。

11. 步骤11：判断是否达到总仿真时间，若未达到则返回步骤4继续迭代，直至完成全部时序分析。


### 关键参数

- **OpenDSS_QSTS步长**: 1分钟

- **负载缩放比例**: 10%（降至额定值的1/10）

- **PV系统容量**: 9 kW单相，接入Bus 634 A相

- **戴维南提取样本数**: $n$（组合数$N = n(n-1)(n-2)/6$）

- **电感电流纹波设计范围**: 5% ~ 10% of $I_L$

- **输出电压纹波系数$\gamma$**: 2%

- **模糊MPPT输入范围**: [-1, 1]归一化

- **模糊隶属函数**: NB, NS, ZE, PS, PB（梯形）

- **同步时钟机制**: $T_{hold}(t) = \lfloor t/T_{hold} \rfloor \cdot T_{hold}$



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 辐照度波动工况 | 在0.5-3.0s内施加0.8/1.0/0.9/0.7/0.6 p.u.阶梯辐照度变化。联合仿真准确捕捉了直流母线电压的瞬态跌落与恢复过程，稳态纹波特性与全EMT模型高度一致。 | 直流母线电压稳态纹波平均RMSE仅为0.0026 p.u.（如0.5-1.0s区间EMT为0.040 p.u.，联合仿真为0.036 p.u.），计算时间减少约60%-70%。 |

| 无功功率注入调节 | 测试PV逆变器无功支撑能力。联合仿真显示PCC电压随无功注入平稳上升，直流母线电压保持稳定，动态响应曲线与全EMT基准完全重合。 | 电压调节误差<0.5%，验证了QSTS域与EMT域功率交互的数值稳定性。 |

| 电网侧故障工况 | 模拟配电网短路故障。联合仿真成功复现了PCC电压瞬时跌落、直流母线电压过冲及故障电流尖峰，控制器保护逻辑动作时序与全EMT一致。 | 故障瞬态波形吻合度>95%，克服了传统QSTS无法模拟高频暂态的缺陷。 |



## 量化发现

- 联合仿真框架计算时间较全系统EMT仿真显著降低约60%~70%。
- 直流母线电压稳态纹波平均RMSE为0.0026 p.u.，最大单区间偏差仅0.0040 p.u.。
- 戴维南等效提取算法通过$N = n(n-1)(n-2)/6$种组合计算，利用众数筛选有效抑制了测量噪声对阻抗估计的影响。
- 模糊MPPT控制器在[-1, 1]归一化输入下，通过25条规则实现占空比微调，确保MPP跟踪无超调。
- 负载降至10%后，IEEE 13节点系统仍保持数值收敛，验证了框架在轻载/高渗透率场景下的鲁棒性。


## 关键公式

### 戴维南等效线性化提取方程

$$$$\Delta V^2 + 2\Delta P r_{th} + 2\Delta Q x_{th} = 0$$$$

*用于从OpenDSS输出的连续QSTS潮流数据中，通过差分法解耦计算配电网等效电阻$r_{th}$和电抗$x_{th}$，是跨域数据交互的核心桥梁。*

### 戴维南等效电压源重构公式

$$$$E_{th} = \sqrt{V_{Ln}^2 + I_{Ln}^2 (r_{th}^{*2} + x_{th}^{*2}) + 2P_n r_{th}^* + 2Q_n x_{th}^*}$$$$

*在EMT仿真步长内，根据提取的最优阻抗和当前节点测量值实时计算等效电压源幅值，驱动Simulink中的受控源模型。*

### 模糊MPPT占空比更新律

$$$$D_{new} = D_{old} + \Delta D$$$$

*结合模糊推理输出的$\Delta D$，实时调节Boost变换器开关管占空比，实现光伏阵列最大功率点跟踪。*



## 验证详情

- **验证方式**: 对比分析（联合仿真结果 vs 全系统MATLAB/Simulink EMT基准模型）
- **测试系统**: 修改版IEEE 13节点测试馈线（总负载降至额定值10%，Bus 634 A相接入9kW单相光伏系统）
- **仿真工具**: OpenDSS（QSTS/相量域潮流计算）、MATLAB/Simulink（EMT/电力电子动态建模）、COM接口（跨平台数据通信）
- **验证结果**: 在辐照度波动、无功调节及电网故障三种典型工况下，联合仿真与全EMT模型的电压、电流及直流母线动态波形高度吻合。稳态指标RMSE<0.004 p.u.，瞬态响应一致，同时计算效率提升60%-70%，验证了框架在兼顾精度与效率方面的有效性。
