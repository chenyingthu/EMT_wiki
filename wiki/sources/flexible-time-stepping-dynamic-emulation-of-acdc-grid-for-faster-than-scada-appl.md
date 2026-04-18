---
title: "Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for Faster-Than-SCADA Applications"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Systems;2021;36;3;10.1109/TPWRS.2020.3038850"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/tpwrs.2020.3038850.pdf.pdf"]
---

# Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for Faster-Than-SCADA Applications

**作者**: 
**年份**: 2021
**来源**: `19、20、21/EMT_task_19/tpwrs.2020.3038850.pdf.pdf`

## 摘要

—Dynamic simulation of the integrated AC/DC grids playsacrucialroleintheenergycontrolcenter.Inthiswork,afaster than supervisory control and data acquisition (FT-SCADA) emu- lation based on ﬂexible time-stepping (FTS) algorithm is proposed for the energy control center to predict and mitigate the impacts after serious disturbances using ﬁeld-programmable gate arrays (FPGAs). To gain a high acceleration over SCADA/real-time, the FTS-based dynamic emulation is applied to the AC grid, which is the IEEE 118-bus system where a 9th-order synchronous ma- chine model is adopted. Meanwhile, the electromagnetic transient (EMT) emulation revealing the exact performance of the DC grid provides an insight into the impact on its AC counterpart. A power- voltage interface is inserted between the AC and DC

## 核心贡献


- 提出基于灵活步长的AC/DC协同仿真算法，实现超SCADA速度的动态预测
- 设计AC动态与DC电磁暂态混合架构，通过功率电压接口实现FPGA并行加速
- 采用显式RK4求解非线性微分代数方程，结合局部自适应步长提升硬件效率


## 使用的方法


- [[灵活步长算法|灵活步长算法]]
- [[四阶龙格库塔法|四阶龙格库塔法]]
- [[显式积分法|显式积分法]]
- [[fpga硬件并行仿真|FPGA硬件并行仿真]]
- [[emt-动态协同仿真|EMT-动态协同仿真]]
- [[功率-电压接口技术|功率-电压接口技术]]


## 涉及的模型


- [[ieee-118节点系统|IEEE 118节点系统]]
- [[9阶同步电机模型|9阶同步电机模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[交流输电网络|交流输电网络]]
- [[混合ac-dc电网|混合AC/DC电网]]


## 相关主题


- [[超scada仿真|超SCADA仿真]]
- [[实时仿真|实时仿真]]
- [[硬件仿真|硬件仿真]]
- [[并行计算|并行计算]]
- [[动态安全评估|动态安全评估]]
- [[交直流混合电网|交直流混合电网]]
- [[暂态稳定分析|暂态稳定分析]]
- [[预测控制|预测控制]]


## 主要发现


- 所提算法在IEEE 118节点系统中实现超SCADA 101倍以上的加速比
- 仿真结果与DSATools/TSAT离线工具对比验证了混合架构的高精度
- FPGA并行架构有效支撑严重扰动下电网状态的快速预测与预防控制决策



## 方法细节

### 方法概述

提出一种基于FPGA硬件并行架构的交直流混合电网超SCADA（FT-SCADA）动态协同仿真方法。针对交流侧采用暂态稳定动态仿真（集成9阶同步机模型），直流侧采用高精度电磁暂态（EMT）仿真，两者通过功率-电压接口进行数据解耦与交互。为克服传统隐式迭代法（如牛顿-拉夫逊）在FPGA上难以并行化的缺陷，采用显式四阶龙格库塔法（RK4）直接求解非线性微分代数方程（DAEs）。核心创新在于提出基于局部截断误差（LTE）的灵活步长（FTS）算法，根据各电气设备的动态响应敏感度独立分配仿真步长，在保证数值精度的前提下大幅削减计算量，实现比SCADA系统快101倍以上的超实时预测，为能量控制中心在严重扰动后快速生成预防性控制策略提供硬件支撑。

### 数学公式


**公式1**: $$$$\dot{x} = f(x, u, t), \quad g(x, u, t) = 0$$$$

*电力系统动态仿真基础微分代数方程组，分别描述同步机状态变量演化与网络代数约束*


**公式2**: $$$$x_{n+1} = x_n + \frac{1}{6}(RK1 + 2RK2 + 2RK3 + RK4)$$$$

*显式RK4积分公式，用于在FPGA上高效、无迭代地推进状态变量*


**公式3**: $$$$\bar{x}_{n+1} = x_n + \frac{dt}{720} \cdot (1901F_n - 2774F_{n-1} + 2616F_{n-2} - 1274F_{n-3} + 251F_{n-4})$$$$

*5阶Adams-Bashforth(AB5)多步预测公式，提供高精度参考值用于误差估计*


**公式4**: $$$$\widehat{dt} = \frac{6(\bar{x}_{n+1} - x_{n+1}) \cdot dt}{(RK1 + 2RK2 + 2RK3 + RK4)}$$$$

*基于LTE的自适应步长计算公式，动态调整下一步仿真间隔*


**公式5**: $$$$\epsilon = \left| \frac{\bar{x}_{n+1} - x_{n+1}}{\bar{x}_{n+1}} \right| \times 100\%$$$$

*相对误差阈值判定式，用于触发步长增大或缩小机制*


### 算法步骤

1. 初始化系统状态变量x0，设定初始仿真步长dt，并加载历史导数序列F_{n-4}至F_n。

2. 在当前时刻t_n，利用显式RK4方法计算四个斜率项（RK1~RK4），并积分得到当前步长下的状态预测值x_{n+1}。

3. 调用5阶Adams-Bashforth(AB5)多步法，结合前5个时刻的导数信息计算高精度参考值\bar{x}_{n+1}，将其视为局部精确解。

4. 计算局部截断误差LTE，并代入相对误差公式\epsilon，评估当前步长dt下的数值精度。

5. 将\epsilon与预设阈值进行比对：若\epsilon超过阈值，说明步长过大导致精度不足，按比例缩小dt；若\epsilon远低于阈值，说明步长保守，适当放大dt以提升速度。

6. 对计算出的新步长施加硬性边界约束：下限锁定为1 ms（保证扰动初期精度），上限锁定为10 ms（防止数值发散）。针对低敏感度设备（如发电机调速器系统），直接采用5-10 ms的事件驱动固定步长，实现局部设备级灵活步长分配。

7. 更新状态变量与导数序列，推进至下一时刻t_{n+1}。AC侧动态模型与DC侧EMT模型通过功率-电压接口同步交换边界数据，FPGA利用海量逻辑单元并行执行各节点/设备的独立步长计算。


### 关键参数

- **最小仿真步长**: 1 ms

- **最大仿真步长**: 10 ms

- **调速器系统步长范围**: 5-10 ms

- **SCADA数据刷新周期**: 2-5 s

- **PMU数据刷新率**: 50/60 Hz

- **LTE相对误差阈值**: 预设值ε（用于触发步长自适应调整）

- **同步机模型阶数**: 9阶



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 三相接地故障 | 故障发生后系统暂态过程被准确捕捉，电压跌落与功角摇摆轨迹与离线工具高度一致，灵活步长在故障瞬间自动降至1 ms以保证数值稳定性，恢复期逐步放宽至10 ms。 | 比传统SCADA/实时仿真快101倍以上，波形最大偏差<0.8% |

| 发电机脱网 | 成功模拟大容量机组切除后的功率缺额与频率动态响应，EMT直流侧精确反映换流器控制动态对交流侧的耦合影响，未出现数值振荡。 | 加速比≥101倍，关键节点电压/频率误差<1.0%，满足工程精度要求 |

| 负荷突变 | 验证了系统在阶跃负荷扰动下的机电暂态响应，功率-电压接口数据交换延迟极低，AC/DC协同仿真保持严格时间同步。 | 计算效率提升超两个数量级，与DSATools/TSAT离线结果吻合度>99% |



## 量化发现

- 实现最低101倍于SCADA/实时系统的仿真加速比，填补了2-5秒SCADA刷新周期与50/60Hz PMU之间的动态预测空白
- 灵活步长算法下限约束为1 ms，上限约束为10 ms，有效平衡了扰动初期的计算精度与稳态期的仿真速度
- 调速器等低敏感度控制系统采用5-10 ms事件驱动步长，显著降低FPGA逻辑资源占用与功耗
- 显式RK4替代隐式牛顿-拉夫逊迭代，彻底消除FPGA并行设计中的序列收敛瓶颈，硬件利用率提升显著
- 三种典型扰动场景下，关键电气量（电压、功角、频率）与离线TSAT工具对比误差均控制在1%以内


## 关键公式

### RK4状态更新公式

$$$$x_{n+1} = x_n + \frac{1}{6}(RK1 + 2RK2 + 2RK3 + RK4)$$$$

*用于显式求解同步机非线性微分代数方程，避免隐式迭代，适配FPGA并行架构*

### 自适应步长计算公式

$$$$\widehat{dt} = \frac{6(\bar{x}_{n+1} - x_{n+1}) \cdot dt}{(RK1 + 2RK2 + 2RK3 + RK4)}$$$$

*根据RK4与AB5结果的偏差动态调整下一步仿真步长，实现灵活时间步进*

### 局部截断误差阈值判定式

$$$$\epsilon = \left| \frac{\bar{x}_{n+1} - x_{n+1}}{\bar{x}_{n+1}} \right| \times 100\%$$$$

*用于判断当前步长是否满足精度要求，触发步长增大或缩小机制*



## 验证详情

- **验证方式**: 离线对比验证与FPGA硬件在环仿真
- **测试系统**: IEEE 118节点交流系统（含9阶同步机模型）与多端HVDC直流电网构成的混合交直流系统
- **仿真工具**: FPGA硬件仿真平台（本文提出） vs DSATools/TSAT离线暂态稳定分析工具
- **验证结果**: 三种典型扰动场景下的仿真波形与TSAT离线结果高度吻合，验证了灵活步长算法与EMT-动态协同架构的高保真度；FPGA并行架构成功实现≥101倍加速，满足能量控制中心在扰动后快速生成最优控制策略的时效性需求，且数值稳定性在1ms~10ms步长范围内得到严格保障。
