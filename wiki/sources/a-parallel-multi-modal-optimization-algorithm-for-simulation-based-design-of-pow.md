---
title: "A Parallel Multi-Modal Optimization Algorithm for Simulation-Based Design of Power Systems"
type: source
year: 2015
journal: "IEEE Transactions on Magnetics"
created: "2026-04-13"
sources: ["EMT_Doc/03/TPWRD.2015.2410172.pdf.pdf"]
---

# A Parallel Multi-Modal Optimization Algorithm for Simulation-Based Design of Power Systems

**年份**: 2015
**来源**: `03/TPWRD.2015.2410172.pdf.pdf`

## 摘要

— This paper proposes a parallel multi-modal optimization algorithm that is combined with electromagnetic transient (EMT) simulation in a platform that unifies the set-up, test, and execution of optimal designs for power systems. The algorithm speeds up the design of power systems as its computations can be executed independently on a highly parallelized environment. Additional speed-up is achieved by using a surrogate model to estimate the objective function in regions of suspected local optima. The estimated functions can be used in the subsequent stages of post-optimization studies such as sensitivity analyses. Comparative studies in terms of computation time are conducted against sequential execution of the proposed algorithm. The optimal design of a VSC-HVDC transmission is described 

## 核心贡献


- 提出结合电磁暂态仿真的并行多模态优化算法实现电力系统黑盒目标函数高效寻优
- 引入三次样条代理模型估计局部极值区域目标函数大幅减少电磁暂态仿真调用次数
- 算法支持局部区域独立并行计算显著缩短设计周期并直接生成灵敏度分析数据


## 使用的方法


- [[并行多模态优化算法|并行多模态优化算法]]
- [[代理模型-三次样条插值|代理模型(三次样条插值)]]
- [[黑盒优化|黑盒优化]]
- [[并行计算|并行计算]]
- [[基于仿真的优化设计|基于仿真的优化设计]]


## 涉及的模型


- [[vsc-model|VSC]]
- [[电磁暂态-emt-仿真模型|电磁暂态(EMT)仿真模型]]


## 相关主题


- [[基于仿真的优化设计|基于仿真的优化设计]]
- [[多模态优化|多模态优化]]
- [[并行计算|并行计算]]
- [[灵敏度分析|灵敏度分析]]
- [[vsc-model|VSC]]


## 主要发现


- 并行执行相比串行计算显著缩短优化耗时验证算法在大规模计算环境下的加速效果
- 三次样条代理模型能高精度逼近局部极值有效减少电磁暂态仿真调用次数
- 成功应用于VSC-HVDC设计实现快速动态响应并有效抑制直流电压纹波与功率误差



## 方法细节

### 方法概述

提出一种结合电磁暂态(EMT)仿真的并行多模态黑盒优化算法，专为电力系统复杂控制器参数设计。该方法首先在设计空间生成初始采样网格，通过并行EMT仿真评估目标函数值。随后利用邻域比较法自动识别潜在局部极值区域，并在各区域内构建正方形加密网格。采用三次样条插值技术拟合局部代理模型，通过解析求导快速定位极小值点，避免重复调用高耗时仿真器。算法支持多区域完全独立并行计算，大幅压缩设计周期。收敛后生成的显式代理函数可直接用于后优化灵敏度分析，兼顾全局多模态寻优能力与工程实用性。

### 数学公式


**公式1**: $$$error(i) = OF_{ac}(i) - OF_{st}(i)$$$

*收敛误差计算公式，用于比较代理模型预测极值与实际EMT仿真值的差异，判断是否满足收敛阈值*


**公式2**: $$$N_{NA} = (n_{ne})^d - (n_{ex})^d = (2n_{ex} - 1)^d - (n_{ex})^d$$$

*网格加密新增点数计算公式，其中d为决策变量维数，n_ex和n_ne分别为加密前后单轴网格点数*


**公式3**: $$$\min f(x_1, x_2) = (x_1^2 + x_1 + x_2^2 + 2.1x_2) + \sum_{i=1}^{2} 10(1 - \cos(2\pi x_i))$$$

*Rastrigin基准测试函数，用于验证算法在不同局部极值数量下的性能与并行加速效果*


**公式4**: $$$f_1(x) = C_{VT} \int_{Transient} (V_{dcref}(t) - V_{dc1}(t))^2 dt + C_{VS} \int_{SteadyState} (V_{dcref}(t) - V_{dc1}(t))^2 dt$$$

*VSC-HVDC直流电压跟踪误差目标函数（含暂态与稳态加权积分平方误差）*


### 算法步骤

1. 初始化与初始网格生成：在设计变量约束范围内均匀散布n个初始试验点，通过并行EMT仿真计算各点目标函数值，构建覆盖全局的初始评估网格。

2. 局部极值区域定位：遍历网格中每个点，将其目标函数值与拓扑直接相邻点进行比较。若某点函数值严格小于所有邻居，则标记为潜在局部极值中心，并划定其所属的独立局部搜索区域。

3. 代理模型构建与极值估计：在每个局部区域内生成规则正方形网格，并行执行EMT仿真获取网格点函数值。采用三次样条插值法拟合该区域的显式代理模型，通过令代理模型梯度为零解析求解其理论极小值点坐标及函数值。

4. 收敛性检验：将代理模型预测的极小值点坐标输入EMT仿真器获取实际目标函数值。计算预测值与实际值的绝对误差，若误差小于预设容差（0.001），则判定该区域收敛；否则进入加密步骤。

5. 网格密度递增：对未收敛区域，在原有正方形网格的每条连线中点插入新采样点，按指数规律增加网格密度。重新并行评估新点，更新三次样条代理模型，并重复极值估计与收敛检验，直至所有局部区域均满足收敛条件。


### 关键参数

- **收敛阈值**: 0.001

- **并行计算节点数**: 60个处理器

- **代理模型类型**: 三次样条插值(Cubic-Spline)

- **目标函数类型**: 黑盒型(依赖EMT仿真输出)

- **网格加密策略**: 连线中点插入法



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| Rastrigin基准函数(16个极值) | 串行计算耗时337秒，并行计算耗时11秒，共需337次目标函数评估，成功定位全部16个极值 | 并行加速比达1.2倍 |

| Rastrigin基准函数(500个极值) | 串行计算耗时23625秒，并行计算耗时2768秒，成功定位495个极值(因网格粒度遗漏5个极近极值) | 并行加速比达10.8倍，计算效率提升显著 |

| VSC-HVDC输电系统控制器优化 | 优化VSC1/VSC2控制器参数，使直流电压Vdc1、有功功率Pdc2及交流端电压Vc1/Vc2在暂态与稳态下紧密跟踪参考值，有效抑制直流电压纹波与功率误差 | 相比传统串行黑盒优化，设计周期大幅缩短，且直接生成可用于灵敏度分析的显式代理函数 |



## 量化发现

- 在500个局部极值的复杂测试中，并行架构实现10.8倍计算加速(23625s降至2768s)
- 收敛判定误差阈值设定为0.001，代理模型预测值与实际EMT仿真值偏差控制在此范围内
- 网格加密后新增点数遵循指数增长规律，对于2维问题初始4点网格加密一次新增(2*4-1)^2 - 4^2 = 33个点
- 算法在极值密集区域(间距极小)存在约1%的漏检率(500极值漏检5个)，但整体多模态寻优成功率>99%
- 三次样条代理模型将后续灵敏度分析的计算成本从耗时EMT仿真降至毫秒级解析求导


## 关键公式

### 收敛误差判据

$$$error(i) = OF_{ac}(i) - OF_{st}(i)$$$

*用于判断代理模型拟合的局部极值是否足够精确，决定是否终止迭代或继续加密网格*

### 网格加密点数公式

$$$N_{NA} = (2n_{ex} - 1)^d - (n_{ex})^d$$$

*在未收敛的局部区域内动态增加采样点密度，提升三次样条插值精度*

### 加权积分平方误差目标函数

$$$f_k(x) = C_{kT} \int_{Transient} e_k^2(t) dt + C_{kS} \int_{SteadyState} e_k^2(t) dt$$$

*VSC-HVDC系统多目标优化核心，量化直流电压、有功功率及交流电压的暂态/稳态跟踪性能*



## 验证详情

- **验证方式**: 数值基准测试对比(串行vs并行)与电力系统EMT仿真验证
- **测试系统**: Rastrigin多峰测试函数(2维)及双端VSC-HVDC输电系统(含60Hz/50Hz弱电网SCR=2.6、直流电缆及换流站控制器)
- **仿真工具**: PSCAD/EMTDC(电磁暂态仿真引擎)、60节点并行计算集群、自定义多模态优化算法平台
- **验证结果**: 算法在数学基准测试中验证了并行加速与多极值定位能力；在VSC-HVDC实际工程中成功实现控制器参数黑盒优化，显著缩短设计周期，代理模型输出直接支持后优化灵敏度评估，整体方案具备高计算效率与工程实用性。
