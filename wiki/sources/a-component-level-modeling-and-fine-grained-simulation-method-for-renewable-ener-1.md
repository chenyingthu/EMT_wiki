---
title: "A component-level modeling and fine-grained simulation method for renewable energy power systems sui"
type: source
year: 2025
journal: "IEEE Transactions on Magnetics"
created: "2026-04-13"
sources: ["EMT_Doc/01/Wang 等 - 2026 - A component-level modeling and fine-grained simulation method for renewable energy power systems sui.pdf"]
---

# A component-level modeling and fine-grained simulation method for renewable energy power systems sui

**年份**: 2025
**来源**: `01/Wang 等 - 2026 - A component-level modeling and fine-grained simulation method for renewable energy power systems sui.pdf`

## 摘要

—The detailed modeling of renewable energy power stations captures the full impedance characteristics of the system but significantly increases the scale of electromagnetic transient (EMT) simulations. Parallel computing is essential to enhance the simulation efficiency, but it requires algorithms that are specifically designed to leverage

## 核心贡献


- 提出广义延迟插入法，引入受控源突破传统拓扑限制，实现复杂系统统一建模
- 构建以三相节点支路为单元的GPU细粒度并行算法，实现线性复杂度高效求解


## 使用的方法


- [[广义延迟插入法|广义延迟插入法]]
- [[蛙跳差分法|蛙跳差分法]]
- [[gpu多线程并行|GPU多线程并行]]
- [[节点分析法|节点分析法]]
- [[细粒度并行求解|细粒度并行求解]]


## 涉及的模型


- [[风电场|风电场]]
- [[风力发电机组|风力发电机组]]
- [[电力电子变换器|电力电子变换器]]
- [[三相节点支路模型|三相节点支路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[细粒度仿真|细粒度仿真]]
- [[gpu加速|GPU加速]]
- [[新能源并网建模|新能源并网建模]]


## 主要发现


- 与PSCAD对比验证了GLIM模型的高精度，能准确捕捉系统全阻抗特性
- GPU仿真耗时不随风电场规模扩大显著增加，验证了算法的线性时间复杂度优势



## 方法细节

### 方法概述

提出广义延迟插入法(GLIM)，通过引入受控电压/电流源突破传统LIM对节点必须含电容、支路必须含电感的拓扑限制。将新能源场站复杂设备（如PMSG、背靠背变流器、滤波器、电网侧元件）统一等效为三相节点与三相支路的基本拓扑单元。采用蛙跳差分法对微分方程进行离散化，使节点电压与支路电流的求解在时间步上交错进行，实现各节点/支路求解的完全解耦。结合GPU多线程架构，以三相节点/支路为细粒度并行单元，设计块对角矩阵并行求解策略与多速率控制-电气交互机制，实现大规模新能源系统电磁暂态仿真的线性复杂度高效计算。

### 数学公式


**公式1**: $$U_i^{n+1/2} = \left(\frac{C_i}{\Delta t} + G_i\right)^{-1} \left[ \frac{C_i}{\Delta t} U_i^{n-1/2} + \left(-\sum_{k=1}^{M} I_{ik}^n + I_{i,ctrl}^n\right) \right]$$

*节点电压半步更新方程，利用当前步支路电流与受控电流源显式计算下一半步节点电压，各节点求解相互独立*


**公式2**: $$I_{ij}^{n+1} = \left(\frac{L_{ij}}{\Delta t}\right)^{-1} \left[ \left(\frac{L_{ij}}{\Delta t} - R_{ij}\right) I_{ij}^n + \left(U_i^{n+1/2} - U_j^{n+1/2} + U_{ij,ctrl}^{n+1/2}\right) \right]$$

*支路电流全步更新方程，基于已更新的节点电压与历史电流显式递推，适用于普通支路与含受控源支路*


**公式3**: $$\left(\frac{C}{\Delta t} + G\right) U^{n+1/2} = \frac{C}{\Delta t} U^{n-1/2} - M_{GLIM} I_b^n$$

*GLIM系统级节点电压矩阵方程，系数矩阵呈块对角形式，M_GLIM为节点-支路关联变换矩阵*


**公式4**: $$\left(\frac{A_{PMSG-L}}{\Delta t}\right) I_{ij}^{n+1} = \left(\frac{A_{PMSG-L}}{\Delta t} - B_{PMSG-L}\right) I_{ij}^n + \left(C_{PMSG-L} U_j^{n+1/2} + U_{PMSG-L,ctrl}^{n+1/2}\right)$$

*永磁同步发电机及串联电感(PMSG-L)的离散化GLIM模型，将微分方程转化为含时变系数矩阵与受控电压源的三相支路形式*


### 算法步骤

1. 系统拓扑分解与GLIM建模：将电网侧线路、变压器、负载、同步发电机及机侧PMSG、背靠背变流器、滤波器等统一映射为含受控源的三相节点与三相支路基本单元，构建块对角形式的系统导纳/阻抗矩阵。

2. 蛙跳法离散化：采用二阶精度的蛙跳差分格式，对节点电压与支路电流进行半步交错采样离散，将微分代数方程转化为显式递推形式，消除单步内迭代需求。

3. GPU细粒度并行初始化：将每个三相节点/支路分配至独立GPU线程块，利用共享内存预加载系数矩阵、历史状态变量及受控源参数，优化全局内存访问延迟。

4. 节点电压并行求解：各线程独立计算对应节点的电压更新，通过关联矩阵M_GLIM聚合相邻支路电流与受控电流源注入量，完成对角块矩阵的显式求解。

5. 支路电流并行求解：基于已更新的节点电压，各线程并行求解支路电流。对于耦合三相支路，采用直接三角分解法（LU分解）并行求解3阶线性方程组；非耦合支路直接显式计算。

6. 受控源与多速率控制交互：电气系统以微秒级步长推进，控制系统以数十微秒级步长运行。当时间到达控制步长整数倍时，完整执行控制逻辑生成开关信号；否则直接利用上一控制步的调制波与当前载波比较生成开关状态。通过共享内存与线程束（Warp）路径优化减少分支发散开销。

7. 状态更新与迭代：同步更新所有节点电压、支路电流及机械转子状态，进入下一仿真步，直至达到设定仿真时长。


### 关键参数

- **simulation_step**: 微秒级（μs）

- **control_step**: 数十微秒级

- **gpu_hardware**: GeForce RTX 3060 Laptop GPU

- **switch_on_resistance**: 0 Ω (正常运行模式)

- **switch_off_resistance**: ∞ (正常运行模式)

- **discretization_method**: 蛙跳差分法（Leap-frog）

- **matrix_decomposition**: 直接三角分解法（LU）

- **parallel_unit**: 三相节点/三相支路



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 多风电场并网系统三相接地故障 | 在包含4个风电场（共48台WTG）的系统中验证GLIM模型动态响应，电压、电流波形与PSCAD基准高度吻合，完整捕捉系统全阻抗特性与高频谐波动态。 | 与PSCAD仿真结果波形重合度极高，误差可忽略，验证了GLIM在复杂故障下的高精度建模能力。 |

| 含直流侧斩波保护的低电压穿越(LVRT)工况 | 引入直流侧斩波电路消耗过剩能量，GLIM模型通过增加并联支路受控源实现LVRT动态过程仿真，准确反映制动电阻投切对直流电压与机侧电流的抑制作用。 | 在大规模设备接入下，GPU仿真耗时未随风电场规模扩大显著增加，验证了算法的线性时间复杂度优势。 |



## 量化发现

- 仿真时间复杂度严格为线性O(N)，系统规模扩大时GPU计算耗时基本保持稳定，无显著增长。
- 采用微秒级电气步长与数十微秒级控制步长的多速率交互策略，在保证开关信号高频精度的同时，降低控制逻辑计算开销。
- 节点与支路求解完全解耦，单步内无需迭代，3阶块对角矩阵通过GPU线程直接并行求解，计算效率较传统NAM/LU分解方法显著提升。
- GPU共享内存优化与线程束（Warp）路径对齐技术有效掩盖了全局内存访问延迟与分支发散带来的性能损失。


## 关键公式

### GLIM节点电压矩阵更新方程

$$\left(\frac{C}{\Delta t} + G\right) U^{n+1/2} = \frac{C}{\Delta t} U^{n-1/2} - M_{GLIM} I_b^n$$

*用于并行求解所有三相节点电压，系数矩阵为块对角形式，各节点独立计算*

### GLIM支路电流显式递推方程

$$I_{ij}^{n+1} = \left(\frac{L_{ij}}{\Delta t}\right)^{-1} \left[ \left(\frac{L_{ij}}{\Delta t} - R_{ij}\right) I_{ij}^n + \left(U_i^{n+1/2} - U_j^{n+1/2} + U_{ij,ctrl}^{n+1/2}\right) \right]$$

*基于当前步节点电压与历史支路电流，显式计算下一时刻支路电流，适用于普通支路与含受控源支路*

### PMSG转子运动离散方程

$$\omega^{n+1/2} = \frac{J}{J+K_D\Delta t}\omega^{n-1/2} + \frac{\Delta t}{J+K_D\Delta t}(T_m^n - T_e^n)$$

*用于同步更新永磁同步发电机机械角速度与转子位置，与电气方程耦合求解*



## 验证详情

- **验证方式**: 数字仿真对比验证
- **测试系统**: 含4个风电场（共48台WTG及SVG）的多馈入新能源并网系统
- **仿真工具**: PSCAD/EMTDC（基准对比），自定义GPU并行求解代码（运行于GeForce RTX 3060 Laptop GPU）
- **验证结果**: GLIM模型在正常工况、三相接地故障及LVRT工况下均与PSCAD结果高度一致，准确捕捉全频段阻抗特性与开关动态；GPU细粒度并行算法实现线性时间复杂度，仿真效率不随系统规模扩大而显著下降，验证了其在大规模新能源系统EMT仿真中的高精度与高效性。
