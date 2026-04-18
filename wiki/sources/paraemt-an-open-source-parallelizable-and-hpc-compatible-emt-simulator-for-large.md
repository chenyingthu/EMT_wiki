---
title: "ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids"
type: source
authors: ['未知']
year: 2024
journal: "IEEE Transactions on Power Delivery;2024;39;2;10.1109/TPWRD.2023.3342715"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf"]
---

# ParaEMT: An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich Power Grids

**作者**: 
**年份**: 2024
**来源**: `30/Xiong 等 - 2024 - ParaEMT An Open Source, Parallelizable, and HPC-Compatible EMT Simulator for Large-Scale IBR-Rich P.pdf`

## 摘要

—The electromagnetic transient (EMT) simulation is an essential tool for studying power grids dominated by inverter-based resources (IBRs). However, due to small simulation time steps and increasing problem sizes, performing EMT simulations for large-scale power grids becomes computational-intensive, and of- ten impractical. To address this challenge, we developed ParaEMT, an open-source Python-based EMT simulator that is parallelizable and compatible with high-performance computing (HPC) systems for simulating large-scale power grids with a signiﬁcant presence of IBRs. Its key features include: 1) utilizing parallel computation for network solution by decomposing the network conductance matrix into the bordered block diagonal form; 2) enabling parallel updates of device states and network

## 核心贡献


- 提出基于加边块对角矩阵分解的网络导纳矩阵并行求解算法
- 实现设备状态变量与网络历史电流的解耦并行更新机制
- 开发适配高性能计算集群的开源Python电磁暂态仿真平台


## 使用的方法


- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[伴随电路法|伴随电路法]]
- [[加边块对角矩阵分解|加边块对角矩阵分解]]
- [[并行计算|并行计算]]


## 涉及的模型


- [[逆变器接口电源-ibr|逆变器接口电源(IBR)]]
- [[通用ibr模型|通用IBR模型]]
- [[r-l-c网络元件|R-L-C网络元件]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[高性能计算|高性能计算]]
- [[大规模电网仿真|大规模电网仿真]]
- [[高比例新能源电网|高比例新能源电网]]


## 主要发现


- 在240节点WECC系统中验证了与PSCAD一致的电磁暂态动态精度
- 在万节点级合成电网中利用HPC集群实现约25至36倍的仿真加速比
- 成功构建100%可再生能源区域案例，验证了大规模IBR交互仿真能力



## 方法细节

### 方法概述

ParaEMT采用基于Python的开源电磁暂态仿真框架，核心方法包括：1) 使用传统节点分析法（Nodal Formulation）建立网络方程，基于梯形积分法（Trapezoidal Rule）将R-L-C电路微分方程离散化为伴随电路（Companion Circuit）；2) 提出基于加边块对角矩阵（Bordered Block Diagonal, BBD）分解的并行计算策略，将网络导纳矩阵分解为子块并行求解；3) 实现设备状态变量更新与网络历史电流更新的自然解耦并行机制；4) 开发适配高性能计算（HPC）集群的通用接口，支持大规模万节点级系统的分布式并行仿真。仿真器采用固定时间步长积分，通过添加人工电阻（Artificial Resistors）抑制数值振荡。

### 数学公式


**公式1**: $$$i(t) = \frac{v(t)}{R_{eq}} + i_{hist}(t - \Delta t)$$$

*梯形积分法离散化后的支路电流方程，表示当前时刻电流由等效电阻上的瞬时电流和历史电流源组成*


**公式2**: $$$i_{hist}(t - \Delta t) = ai(t - \Delta t) + bv(t - \Delta t)$$$

*历史电流源计算公式，系数a和b由梯形积分法确定，体现存储的上一时步状态*


**公式3**: $$$Gv(t) = i(t) + i_{hist}(t - \Delta t)$$$

*网络节点电压方程，G为网络导纳矩阵（conductance matrix），v(t)为三相瞬时节点电压向量，i(t)为注入电流向量*


**公式4**: $$$v_a = V_{mag}\cos(V_{ang})$$$

*A相电压初始化公式，基于正序潮流结果的幅值和相角转换为三相瞬时波形*


**公式5**: $$$v_b = V_{mag}\cos(V_{ang} - 2\pi/3)$$$

*B相电压初始化公式，相位偏移-120度*


**公式6**: $$$v_c = V_{mag}\cos(V_{ang} + 2\pi/3)$$$

*C相电压初始化公式，相位偏移+120度*


**公式7**: $$$R_p \approx 40L/(3\Delta t)$$$

*与电感并联的人工电阻，用于抑制数值振荡*


**公式8**: $$$R_s \approx 3\Delta t/(40C)$$$

*与电容串联的人工电阻，用于抑制数值振荡*


### 算法步骤

1. 系统初始化：加载PSSE格式的电网数据文件，使用牛顿-拉夫逊法求解正序潮流，获得节点电压幅值V_mag和相角V_ang

2. 三相波形转换：将正序相量电压和电流转换为三相瞬时波形v_a, v_b, v_c，使用余弦函数生成初始电压波形

3. 设备初始化：通过控制框图方程的变量反向传播（backward propagation），初始化同步发电机、机控系统和IBR（逆变器接口电源）的动态模型状态变量

4. BBD矩阵分解：将大规模网络导纳矩阵G自动分解为加边块对角形式（Bordered Block Diagonal），划分为多个子网络块和边界节点

5. 并行网络求解：利用HPC集群的多核处理器并行求解各子块的节点电压方程，通过Schur补方法处理边界节点耦合

6. 设备状态并行更新：各IBR和旋转电机模型独立并行更新内部状态变量（控制器状态、滤波器状态等），计算注入电流

7. 历史电流并行更新：基于梯形积分法并行计算各支路的历史电流源i_hist，为下一时步准备

8. 时步推进：以固定步长Δt（通常50-100微秒）推进仿真时间，重复执行步骤5-7直至仿真结束


### 关键参数

- **time_step**: 50-100 microseconds (μs) 或更小，确保数值稳定性和精度

- **artificial_resistor_inductor**: $R_p \approx 40L/(3\Delta t)$，并联在电感两端抑制振荡

- **artificial_resistor_capacitor**: $R_s \approx 3\Delta t/(40C)$，串联在电容支路抑制振荡

- **simulation_language**: Python 3.x

- **HPC_platform**: NREL Eagle supercomputer

- **matrix_format**: Bordered Block Diagonal (BBD)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 缩减240母线WECC系统（720节点三相） | 验证ParaEMT与PSCAD的动态响应一致性，包含同步发电机和传统负荷的机电暂态行为，波形对比显示电压和电流动态误差小于典型工程精度要求 | 与PSCAD的EMT仿真结果对比，动态精度一致（波形吻合），未报告具体百分比误差但声明'validated'和'benchmarked' |

| 100%可再生能源场景（240母线WECC系统的加州区域改造） | 将加州区域替换为100% IBR渗透率，模拟系统级IBR交互作用，成功捕捉逆变器控制交互和宽频动态 | 首次实现该规模系统的高比例IBR详细EMT仿真，传统工具在该规模下计算不可行 |

| 合成10080母线系统（30240节点三相） | 大规模合成电网测试，利用HPC集群Eagle进行并行仿真，验证加速比和可扩展性 | 相比串行仿真实现25-36倍加速比（speedup），具体取决于使用的计算核心数 |



## 量化发现

- 在10080母线（30240节点）大规模系统上，利用HPC集群实现约25至36倍的仿真加速比
- EMT仿真时间步长采用50-100微秒或更小，确保数值A稳定性和模型精度
- 人工电阻取值：电感并联电阻$R_p \approx 40L/(3\Delta t)$，电容串联电阻$R_s \approx 3\Delta t/(40C)$，有效抑制虚构数值振荡同时保持精度
- 在240母线（720节点）WECC系统上完成与PSCAD的精度验证，三相瞬时电压波形对比显示一致性
- 成功模拟100%可再生能源渗透率场景，处理大规模IBR（逆变器接口电源）控制交互
- 网络导纳矩阵采用BBD分解后，子块间通过Schur补处理边界耦合，实现并行效率与数值精度的平衡


## 关键公式

### 节点电压方程（Network Nodal Equation）

$$$Gv(t) = i(t) + i_{hist}(t - \Delta t)$$$

*每个仿真时步求解网络电压的核心方程，基于伴随电路模型和基尔霍夫电流定律（KCL）建立，其中G为包含所有等效电阻的导纳矩阵*

### 梯形积分历史电流（Trapezoidal History Current）

$$$i_{hist}(t - \Delta t) = ai(t - \Delta t) + bv(t - \Delta t)$$$

*体现梯形积分法的A稳定性，用于计算伴随电路中的历史电流源，存储上一时步的电流和电压状态*



## 验证详情

- **验证方式**: 对比验证（Benchmarking against commercial software）
- **测试系统**: 缩减的240母线（720节点三相）西部电力协调委员会（WECC）系统，包含详细同步发电机模型、励磁系统、调速器和传统负荷
- **仿真工具**: PSCAD/EMTDC（商业EMT仿真软件作为基准）
- **验证结果**: ParaEMT与PSCAD的EMT动态响应完全一致（identical EMT dynamics），验证了基于BBD矩阵分解的并行算法在保持数值精度方面的有效性，确认并行计算引入的误差在工程可接受范围内
