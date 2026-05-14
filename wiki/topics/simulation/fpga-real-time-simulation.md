---
title: "FPGA 实时仿真 (FPGA Real-Time Simulation)"
type: topic
tags: [fpga, real-time, simulation, hardware, acceleration, hil, power-electronics]
created: "2026-05-02"
updated: "2026-05-03"
---

# FPGA 实时仿真 (FPGA Real-Time Simulation)


```mermaid
graph TD
    subgraph Ncmp[FPGA 实时仿真 (FPGA Real-Time Si…]
        N0[执行模式: 并行]
        N1[时间确定性: 严格（纳秒级抖动）]
        N2[最小步长: 50ns - 1μs]
        N3[开发难度: 高]
        N4[灵活性: 低（硬件固定）]
        N5[精度控制: 定点/自定义浮点]
        N6[调试能力: 受限]
        N7[成本（小规模）: 较高]
    end
```


## 核心原理详解

### 技术概述
FPGA 实时仿真是电力系统电磁暂态仿真领域的重要技术，对提高仿真精度和效率具有重要意义。

### 理论基础
该技术建立在严格的电磁场理论和电路分析基础之上，通过数学建模描述系统的动态行为。

### 核心机制
- **物理建模**：基于物理定律建立准确的数学模型
- **数值求解**：采用高效的数值算法求解系统方程
- **参数分析**：研究关键参数对系统性能的影响

### 技术优势
- 提高仿真精度和计算效率
- 支持复杂系统的详细分析
- 为工程设计和优化提供理论支撑

## 概述

FPGA（Field-Programmable Gate Array，现场可编程门阵列）实时仿真是一种利用可重构硬件的并行计算能力实现电力系统电磁暂态仿真的先进技术。与传统的基于CPU的仿真相比，FPGA仿真能够实现亚微秒级甚至纳秒级的仿真步长，使其特别适合于高频电力电子变换器、多电平换流器（MMC）以及需要与物理控制器交互的硬件在环（HIL）仿真应用。

FPGA实时仿真的核心优势在于其固有的并行性和确定性。不同于CPU的串行执行模型，FPGA可以在同一时钟周期内执行数千个独立计算，且每个计算的延迟是精确可预测的。这种特性对于电力系统实时仿真至关重要，因为实时仿真要求在每个仿真步长内完成所有计算，并在严格的时间约束下输出结果。

### 发展历程

FPGA在电力系统仿真中的应用始于21世纪初，最初主要用于简单的电力电子电路仿真。随着FPGA技术的发展，特别是Xilinx Virtex系列和Intel（原Altera）Stratix系列器件的出现，FPGA开始能够处理更复杂的电力系统模型。2008年左右，RTDS Technologies推出了基于FPGA的电力电子仿真卡，标志着FPGA实时仿真进入商业化阶段。近年来，随着高层次综合（HLS）工具的成熟，FPGA开发的门槛显著降低，加速了其在学术研究和工业应用中的普及。

## FPGA架构基础

理解FPGA实时仿真需要首先了解FPGA的基本架构组成。现代FPGA是一种可编程逻辑器件，由以下关键资源构成：

### 可配置逻辑块（CLB）与查找表（LUT）

可配置逻辑块（Configurable Logic Block, CLB）是FPGA的基本计算单元。每个CLB通常包含多个查找表（Look-Up Table, LUT），用于实现组合逻辑功能。

**查找表（LUT）**本质上是一个小型存储器，可以实现任意布尔函数。一个N输入的LUT可以存储2^N个条目，能够实现最多N个输入变量的任意布尔函数。例如：

- 4输入LUT：可实现任意4输入布尔函数
- 6输入LUT：现代FPGA常见配置，资源效率更高

在电力系统仿真中，LUT常用于实现：
- 非线性元件的查表法计算
- 开关状态的组合逻辑
- 控制算法中的决策逻辑

**公式**：一个K输入LUT实现的函数可表示为：
```
f(x_1, x_2, ..., x_K) = LUT[addr]
addr = Σ(x_i × 2^(i-1))
```

### 数字信号处理切片（DSP Slices）

DSP切片是FPGA中专用的硬件乘法器单元，对于电力系统仿真中的矩阵运算和滤波器实现至关重要。

**典型DSP切片特性**：
- 25×18位或27×18位有符号乘法器
- 48位累加器
- 可级联形成更宽的数据通路
- 支持预加法器（用于对称滤波器）

在电磁暂态仿真中，DSP切片主要用于：
- 节点导纳矩阵与电压向量的乘法（Y×V = I）
- 数值积分器的系数乘法
- 控制系统中的PI调节器

**矩阵向量乘法示例**：
```
[I_1]   [Y_11 Y_12 Y_13]   [V_1]
[I_2] = [Y_21 Y_22 Y_23] × [V_2]
[I_3]   [Y_31 Y_32 Y_33]   [V_3]
```

每个乘法运算可映射到一个DSP切片，多个运算可并行执行。

### 块随机存取存储器（BRAM）

块RAM（Block RAM, BRAM）是FPGA中的嵌入式存储资源，用于存储：

- 导纳矩阵元素
- 历史项数据
- 开关状态表
- 查找表（LUT）初始化数据

**BRAM特性**：
- 典型容量：18Kb或36Kb每块
- 可配置数据宽度：从1位到72位
- 双端口访问：支持同时读写
- 级联能力：可形成更大存储器

在实时仿真中，BRAM用于存储系统状态变量：
```
存储需求 = n_buses × (导纳矩阵行 + 历史项 + 状态变量)
```

### 时钟资源与I/O

**时钟网络**：
- 全局时钟网络：低偏斜，覆盖整个器件
- 区域时钟：局部优化
- PLL/MMCM：时钟频率合成和相位调整

**I/O资源**：
- 高速收发器（GTX/GTH/GTY）：用于高速通信
- 通用I/O：与外部设备交互
- ADC/DAC接口：模拟量输入输出

对于HIL仿真，I/O延迟是关键指标：
```
总延迟 = 仿真步长 + I/O转换时间 + 传输延迟
```

## 定点运算与浮点运算

数值表示格式是FPGA实时仿真的核心设计决策，直接影响资源利用率、计算精度和最大运行频率。

### 定点数表示

定点数是FPGA中最常用的数值格式，具有资源效率高的特点。

**定点数格式**：Q(m, n)表示法
- m：整数位数（包括符号位）
- n：小数位数
- 总位宽 = m + n

**示例**：Q(8, 8)格式
- 总位宽：16位
- 整数范围：-128 到 +127
- 精度：1/256 ≈ 0.0039

**定点数运算**：

1. **加法/减法**：
   - 要求操作数具有相同的小数点位置
   - 结果位宽 = max(m1, m2) + max(n1, n2) + 1（进位）

2. **乘法**：
   - Q(m1, n1) × Q(m2, n2) = Q(m1+m2, n1+n2)
   - 16位 × 16位 = 32位结果
   - 通常需要截断或舍入

**舍入模式**：
- 截断（Truncation）：直接丢弃低位，简单但有偏
- 四舍五入（Round-half-up）：误差最小，需要额外逻辑
- 收敛舍入（Round-to-even）：统计学最优

**动态范围与精度权衡**：
```
动态范围（dB）≈ 6.02 × 整数位数
精度 = 2^(-小数位数)
```

### 浮点数表示

IEEE 754浮点数标准提供更大的动态范围，但消耗更多FPGA资源。

**单精度浮点（FP32）**：
- 符号位：1位
- 指数：8位（偏移127）
- 尾数：23位（隐含前导1）

**半精度浮点（FP16）**：
- 符号位：1位
- 指数：5位（偏移15）
- 尾数：10位

**自定义浮点格式**：
为了优化资源，研究者提出多种自定义格式：
- (1, 6, 9)：1符号+6指数+9尾数
- (1, 5, 10)：类似FP16变体
- (1, 8, 7)：扩展动态范围

**浮点运算资源消耗**：
- 单精度加法：~300-500 LUT
- 单精度乘法：~150-200 DSP切片
- 比较：定点加法仅需~20 LUT

### 数值精度分析

电力系统仿真中的精度要求：

**状态变量典型范围**：
- 电压：0.1 - 2.0 p.u.（标幺值）
- 电流：0.01 - 10.0 p.u.
- 功率：0.001 - 5.0 p.u.

**精度损失来源**：
1. 导纳矩阵求逆误差
2. 数值积分截断误差
3. 定点/浮点量化误差
4. 开关模型离散化误差

**误差累积分析**：
```
总误差 = √(ε_quant² + ε_trunc² + ε_round²)
```

## 并行处理架构

FPGA的核心优势在于其大规模并行处理能力，这在电力系统仿真中有多种实现方式。

### 空间并行（Space Parallelism）

空间并行通过复制计算单元实现多任务同时执行。

**多节点并行求解**：
对于具有n个节点的系统，可以将每个节点的计算分配到独立的硬件模块：
```
模块1: I_1 = Σ(Y_1j × V_j)
模块2: I_2 = Σ(Y_2j × V_j)
...
模块n: I_n = Σ(Y_nj × V_j)
```

所有模块在同一时钟周期内并行执行。

**电力电子开关并行处理**：
对于多级换流器（MMC），每个子模块可以独立仿真：
- 子模块1：电容电压更新
- 子模块2：电容电压更新
- ...
- 子模块N：电容电压更新

**资源-性能权衡**：
```
并行度↑ → 资源消耗↑ × 计算延迟↓
```

### 时间并行（Temporal Parallelism）

时间并行通过流水线技术提高吞吐率。

**流水线原理**：
将复杂计算分解为多个阶段，每个阶段在一个时钟周期内完成：
```
周期t:   读取操作数 → 阶段1
周期t+1: 执行乘法 → 阶段2
周期t+2: 执行加法 → 阶段3
周期t+3: 结果输出 → 阶段4
```

**求解器流水线示例**：
对于梯形法积分器：
```
x(t+Δt) = x(t) + Δt/2 × (f(t) + f(t+Δt))
```

流水线阶段：
1. 计算f(t)（右端函数）
2. 乘法：Δt/2 × f(t)
3. 加法：x(t) + 中间结果
4. 存储结果

**流水线深度与延迟**：
```
流水线深度 = N级
时钟频率 = f_max
吞吐率 = f_max（结果/秒）
总延迟 = N × T_clock
```

### 混合并行策略

实际FPGA设计通常结合空间和时间并行。

**示例：多相系统仿真**：
对于三相系统，每相内部采用流水线，三相之间并行执行：
```
        ┌→ 相A流水线 →┐
输入 →  ├→ 相B流水线 →├→ 合并输出
        └→ 相C流水线 →┘
```

## 求解器实现

电磁暂态仿真的核心是数值积分求解器，在FPGA上需要特殊优化。

### 梯形法（Trapezoidal Rule）

梯形法是电力系统仿真中最常用的积分方法，具有良好的数值稳定性。

**离散化公式**：
```
dx/dt = f(x, t)

x_{n+1} = x_n + h/2 × (f(x_n, t_n) + f(x_{n+1}, t_{n+1}))
```

其中h为步长。

**电感元件的梯形等效**：
```
I_L(t) = I_L(t-Δt) + Δt/(2L) × (V_L(t) + V_L(t-Δt))

等效为：
I_L(t) = G_eq × V_L(t) + I_hist

其中：
G_eq = Δt/(2L)
I_hist = I_L(t-Δt) + Δt/(2L) × V_L(t-Δt)
```

**电容元件的梯形等效**：
```
I_C(t) = G_eq × V_C(t) + I_hist

其中：
G_eq = 2C/Δt
I_hist = -I_C(t-Δt) - 2C/Δt × V_C(t-Δt)
```

**FPGA实现结构**：
```verilog
// 梯形法积分器伪代码
module trapezoidal_integrator (
    input clk,
    input reset,
    input [15:0] v_in,      // 当前电压
    input [15:0] v_hist,    // 历史电压
    input [15:0] i_hist,    // 历史电流
    input [15:0] g_eq,      // 等效电导
    output [15:0] i_out     // 输出电流
);
    // I = G_eq × V + I_hist
    wire [31:0] mult_result = g_eq * v_in;
    wire [15:0] mult_trunc = mult_result[31:16]; // 定点截断
    assign i_out = mult_trunc + i_hist;
endmodule
```

### 后向欧拉法（Backward Euler）

后向欧拉法具有更好的稳定性，适合刚性系统。

**离散化公式**：
```
x_{n+1} = x_n + h × f(x_{n+1}, t_{n+1})
```

**电感元件**：
```
G_eq = Δt/L
I_hist = I_L(t-Δt)
```

**电容元件**：
```
G_eq = C/Δt
I_hist = -C/Δt × V_C(t-Δt)
```

**稳定性比较**：
- 梯形法：A-稳定，但可能产生数值振荡
- 后向欧拉：L-稳定，更适合开关电路

### 多速率积分

电力系统中不同元件具有不同的时间常数，可以采用多速率方法。

**分区策略**：
```
快速子系统：电力电子开关（步长 < 1μs）
慢速子系统：传输线、电机（步长 10-100μs）
```

**插值接口**：
慢速子系统向快速子系统提供插值：
```
V_fast(t) = V_slow(t_0) + (t-t_0)/Δt_slow × (V_slow(t_1) - V_slow(t_0))
```

## 开关建模

电力电子开关的建模是FPGA实时仿真的关键挑战。

### 理想开关模型

**状态转换**：
```
开关导通：R_on ≈ 0.001Ω（小电阻）
开关关断：R_off ≈ 1MΩ（大电阻）
```

**导纳矩阵修改**：
开关状态变化时，需要更新导纳矩阵：
```
Y_ii_new = Y_ii_old + 1/R_switch_new - 1/R_switch_old
```

### 插值开关模型

为了精确捕捉开关时刻，使用插值方法。

**线性插值**：
```
t_switch = t_n + Δt × |V_n| / |V_n - V_{n+1}|
```

当检测到电压过零时，回退并插值计算精确的开关时刻。

### 开关状态机

FPGA实现的开关控制器：
```verilog
module switch_controller (
    input clk,
    input [15:0] v_gate,    // 门极电压/控制信号
    input [15:0] v_anode,   // 阳极电压
    input [15:0] v_cathode, // 阴极电压
    input [15:0] i_switch,  // 开关电流
    output reg switch_state // 开关状态
);
    // 开通条件：门极信号正且正向偏置
    wire turn_on = (v_gate > V_th) && (v_anode > v_cathode);
    
    // 关断条件：电流反向或门极信号移除
    wire turn_off = (i_switch < 0) || (v_gate < V_th);
    
    always @(posedge clk) begin
        if (turn_on) switch_state <= 1;
        else if (turn_off) switch_state <= 0;
    end
endmodule
```

## FPGA与CPU仿真对比

| 特性 | FPGA仿真 | CPU仿真 |
|------|----------|---------|
| 执行模式 | 并行 | 串行 |
| 时间确定性 | 严格（纳秒级抖动） | 可变（微秒级抖动） |
| 最小步长 | 50ns - 1μs | 10μs - 100μs |
| 开发难度 | 高 | 低 |
| 灵活性 | 低（硬件固定） | 高（软件可重配置） |
| 精度控制 | 定点/自定义浮点 | IEEE标准浮点 |
| 调试能力 | 受限 | 强大 |
| 成本（小规模） | 较高 | 较低 |
| 成本（大规模并行） | 较低 | 较高 |

### 性能对比示例

**MMC子模块仿真**：
- CPU：单核可仿真~100子模块@50μs步长
- FPGA：单片可仿真~5000子模块@1μs步长

**加速比**：
```
加速比 = (CPU时间步长 / FPGA时间步长) × 并行度因子
典型值：10× - 1000×
```

### 适用场景

**FPGA优势场景**：
- 高频电力电子（>10kHz开关频率）
- 大规模MMC换流器
- HIL实时测试
- 确定性延迟要求的应用

**CPU优势场景**：
- 大规模电网（>1000节点）
- 复杂控制算法
- 快速原型验证
- 算法迭代开发

## 商业FPGA仿真平台

### RTDS Technologies

RTDS是电力系统实时仿真的领先厂商，其Simulator产品广泛用于HIL测试。

**技术特点**：
- 基于FPGA的电力电子仿真卡
- 步长：1μs（电力电子）/ 50μs（电网）
- 支持MMC仿真（最多1000+子模块）

**硬件架构**：
```
Rack-based系统
├── 处理器卡（PB5）：电网仿真
├── GTFPGA卡：电力电子仿真
└── GTIO卡：模拟/数字I/O
```

### Typhoon HIL

Typhoon HIL专注于电力电子和微电网的FPGA实时仿真。

**产品系列**：
- HIL 404：入门级，适合中小功率变换器
- HIL 604+/606：中高端，支持复杂系统
- HIL 604+ CM：模块化多核架构

**技术特点**：
- 纯FPGA实现（无CPU参与电力电子计算）
- 步长：500ns - 1μs
- 自动代码生成（从Simulink模型）

**仿真能力**：
- 最多支持1000+开关器件
- 自动处理开关死区
- 内置示波器和频谱分析

### OPAL-RT

OPAL-RT提供eFPGASim等FPGA仿真解决方案。

**技术路线**：
- CPU+FPGA协同仿真
- 电力电子在FPGA上运行
- 电网和控制算法在CPU上运行

### dSPACE

dSPACE的DS1007和SCALEXIO系统支持FPGA扩展。

**特点**：
- 与MATLAB/Simulink深度集成
- 支持FPGA编程（Xilinx工具链）
- 主要面向汽车电子和电机控制

## 开发工具链

### 高层次综合（HLS）

HLS工具允许使用C/C++描述硬件，自动综合为RTL代码。

**Xilinx Vitis HLS**：
```cpp
// 梯形法积分器C++描述
void trapezoidal_integrator(
    fixed_t v_in,
    fixed_t v_hist,
    fixed_t i_hist,
    fixed_t g_eq,
    fixed_t& i_out
) {
    #pragma HLS PIPELINE II=1
    i_out = g_eq * v_in + i_hist;
}
```

**Intel HLS**：
类似功能，针对Intel FPGA优化。

**优化指令**：
- `#pragma HLS PIPELINE`：启动流水线
- `#pragma HLS UNROLL`：循环展开
- `#pragma HLS ARRAY_PARTITION`：数组分区

### HDL开发

传统硬件描述语言（Verilog/VHDL）提供更精细的控制。

**设计流程**：
1. 功能设计（算法描述）
2. RTL编码（HDL实现）
3. 功能仿真（ModelSim/VCS）
4. 综合实现（Vivado/Quartus）
5. 时序收敛（约束文件）
6. 硬件验证（板上测试）

### 模型驱动开发

**Simulink HDL Coder**：
从Simulink模型自动生成HDL代码。

**流程**：
```
Simulink模型 → HDL Coder → RTL代码 → FPGA比特流
```

**限制**：
- 代码效率可能低于手工设计
- 需要硬件友好的建模风格
- 定点定标需要手动配置

## 应用案例

### MMC-HVDC实时仿真

对于1000+子模块的MMC换流器：

**资源消耗估算**：
```
每个子模块：
- 电容模型：2 DSP + 100 LUT
- 开关模型：50 LUT
- 控制逻辑：100 LUT

1000子模块总计：
- DSP：2000个
- LUT：250K个

典型FPGA（Xilinx Kintex-7）：
- DSP：1920个（需要资源优化）
- LUT：200K-400K（可行）
```

**优化策略**：
- 时间复用：多个子模块共享计算单元
- 近似计算：降低电容模型精度
- 区域分解：多FPGA并行

### 电机驱动HIL测试

永磁同步电机（PMSM）的FPGA仿真：

**电机模型方程**：
```
dλ_d/dt = V_d - R_s × I_d + ω_e × λ_q
dλ_q/dt = V_q - R_s × I_q - ω_e × λ_d
```

**FPGA实现**：
- 状态空间求解器
- 旋转变压器模型
- 逆变器开关模型
- 位置传感器接口

## 挑战与发展趋势

### 当前挑战

1. **开发复杂度**：需要硬件设计知识
2. **调试困难**：信号可见性有限
3. **浮点性能**：标准浮点运算资源消耗大
4. **模型规模**：大规模电网难以单片实现
5. **验证周期**：硬件编译时间长（分钟-小时级）

### 发展趋势

1. **异构计算**：CPU+FPGA+GPU协同
2. **高级综合**：HLS工具成熟降低门槛
3. **云端FPGA**：AWS/Azure FPGA实例
4. **AI辅助**：机器学习优化资源分配
5. **标准化**：IEEE P2851实时仿真标准

## 相关主题

- [[real-time-simulation]] - 实时仿真技术概述
- [[hil-simulation]] - 硬件在环仿真
- [[parallel-computing]] - 并行计算技术
- [[hardware-acceleration]] - 硬件加速技术
- [[co-simulation]] - 联合仿真方法
- [[power-electronics]] - 电力电子仿真

## 相关方法

- `fixed-point-arithmetic` - 定点运算技术
- [[numerical-integration]] - 数值积分方法
- `pipeline-design` - 流水线设计
- `hls` - 高层次综合
- [[switch-modeling]] - 开关建模技术

## 相关模型

- [[mmc-model]] - MMC换流器模型
- [[vsc-model]] - VSC换流器模型
- [[pmsm-model]] - 永磁同步电机模型
- [[dc-dc-converter]] - DC-DC变换器模型
- [[inverter-model]] - 逆变器模型

## 来源论文

| 论文 | 年份 |
|------|------|
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[29tpwrd20162518676-2|29/TPWRD.2016.2518676]] | 2016 |
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|An automated FPGA real-time simulator for power electronics ]] | 2016 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[32tpwrd20182812753-2|32/TPWRD.2018.2812753]] | 2018 |
| [[32tpwrd20182812753-2|32/TPWRD.2018.2812753]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Control and Simulation of a Grid-Forming Inverter for Hybrid]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[ground-potential-rise-in-wind-farms-due-to-direct-lightning|Ground Potential Rise in Wind Farms due to Direct Lightning]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[fast-detection-of-ssr-for-wind-parks-connected-to-series-compensated-transmissio|Fast Detection of SSR for Wind Parks Connected to Series-Com]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Real-Time HIL Emulation of DRM With Machine Learning Acceler]] | 2023 |
| [[fixed-admittance-modeling-method-of-pmsg-based-on-compensation-of-impedance-基于虚拟|Fixed-admittance Modeling Method of PMSG Based on Compensati]] | 2024 |
| [[基于fpga的电力电子恒导纳开关模型修正算法及实时仿真架构|基于FPGA的电力电子恒导纳开关模型修正算法及实时仿真架构]] | 2024 |
| [[discretized-impedance-based-modeling-of-converter-interfaced-energy-resources-fo|Discretized Impedance-Based Modeling of Converter-Interfaced]] | 2025 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Fine-grained hardware resource optimization and design for F]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |
## EMT中的作用

FPGA 实时仿真 (FPGA Real-Time Simulation) 在EMT仿真中的核心作用：

- **研究范围**：界定FPGA 实时仿真 (FPGA Real-Time Simulation)在EMT仿真中的研究边界和应用场景
- **分析方法**：提供FPGA 实时仿真 (FPGA Real-Time Simulation)相关的EMT分析方法和工具
- **系统影响**：分析FPGA 实时仿真 (FPGA Real-Time Simulation)对电力系统电磁暂态特性的影响
- **仿真验证**：为FPGA 实时仿真 (FPGA Real-Time Simulation)相关研究提供仿真验证框架
## 形式化表达

从EMT仿真角度，FPGA 实时仿真 (FPGA Real-Time Simulation)可形式化表达为：

$$
\text{待补充：FPGA 实时仿真 (FPGA Real-Time Simulation)的数学形式化描述}
$$
## 来源论文

| 论文 | 年份 |
|------|------|
| [[fpga-based-real-time-emtp|FPGA-Based Real-Time EMTP]] | 2009 |
| [[an-iterative-real-time-nonlinear-electromagnetic-transient-solver-on-fpga|An Iterative Real-Time Nonlinear Electromagnetic Transient S]] | 2011 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[digital-hardware-emulation-of-universal-machine-13&14|Digital Hardware Emulation of Universal Machine]] | 2011 |
| [[massively-parallel-implementation-of-ac-machine-modeling-for-real-time-simulatio|Massively Parallel Implementation of AC Machine Modeling for]] | 2011 |
| [[29tpwrd20162518676-2|29/TPWRD.2016.2518676]] | 2016 |
| [[an-automated-fpga-real-time-simulator-for-power-electronics-and-power-systems-el|An automated FPGA real-time simulator for power electronics ]] | 2016 |
| [[modeling-of-modular-multilevel-converters-with-different-levels-of-detail-13&14|Dynamic Electro-Magnetic-Thermal Modeling of MMC-Based DC-DC]] | 2017 |
| [[32tpwrd20182812753-2|32/TPWRD.2018.2812753]] | 2018 |
| [[32tpwrd20182812753-2|32/TPWRD.2018.2812753]] | 2018 |
| [[real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso|Real-time Simulation of Hybrid Modular Multilevel Converters]] | 2018 |
| [[35tpwrd20192933610|Small Time-Step FPGA-based Real-Time Simulation of Power Sys]] | 2019 |
| [[control-and-simulation-of-a-grid-forming-inverter-for-hybrid-pv-battery-plants-i|Control and Simulation of a Grid-Forming Inverter for Hybrid]] | 2021 |
| [[development-of-phase-domain-frequency-dependent-transmission-line-model-on-fpga-|Development of phase domain frequency-dependent transmission]] | 2021 |
| [[ground-potential-rise-in-wind-farms-due-to-direct-lightning|Ground Potential Rise in Wind Farms due to Direct Lightning]] | 2021 |
| [[parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks|Parallel computation of power system EMTs through Polyphase-]] | 2021 |
| [[fast-detection-of-ssr-for-wind-parks-connected-to-series-compensated-transmissio|Fast Detection of SSR for Wind Parks Connected to Series-Com]] | 2022 |
| [[faster-than-real-time-hardware-emulation-of-transients-and-dynamics-of-a-grid-of|Faster-Than-Real-Time Hardware Emulation of Transients and D]] | 2023 |
| [[faster-than-real-time-simulation-of-stator-rotor-decoupling-digital-twin-of-doub|Faster-than-real-time Simulation of Stator-rotor Decoupling ]] | 2023 |
| [[real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode|Real-Time HIL Emulation of DRM With Machine Learning Acceler]] | 2023 |
| [[fixed-admittance-modeling-method-of-pmsg-based-on-compensation-of-impedance-基于虚拟|Fixed-admittance Modeling Method of PMSG Based on Compensati]] | 2024 |
| [[基于fpga的电力电子恒导纳开关模型修正算法及实时仿真架构|基于FPGA的电力电子恒导纳开关模型修正算法及实时仿真架构]] | 2024 |
| [[discretized-impedance-based-modeling-of-converter-interfaced-energy-resources-fo|Discretized Impedance-Based Modeling of Converter-Interfaced]] | 2025 |
| [[fpga-based-simulation-of-grid-tied-converters-using-frequency-dependent-network-|FPGA-based simulation of grid-tied converters using frequenc]] | 2025 |
| [[fine-grained-hardware-resource-optimization-and-design-for-fpga-based-real-time-|Fine-grained hardware resource optimization and design for F]] | 2025 |
| [[mtof-a-novel-fpga-based-emt-toolbox-in-matlab|MTOF: A Novel FPGA-Based EMT Toolbox in MATLAB]] | 2025 |
| [[modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag|Modeling Method for DFIG-Based Wind Farm in High-Efficiency ]] | 2025 |
| [[nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt|Nuclear-Powered Hybrid Energy System for Clean Hydrogen Prod]] | 2026 |