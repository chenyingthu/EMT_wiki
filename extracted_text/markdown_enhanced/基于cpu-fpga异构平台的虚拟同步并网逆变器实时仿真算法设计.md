## 基于 CPU-FPGA 异构平台的虚拟同步并网逆变器实时仿真算法设计
吴 盼，汪可友，徐 晋，李国杰
(电力传输与功率变换控制教育部重点实验室(上海交通大学)，上海 200240)

**摘要：** 随着电力系统中电力电子器件的广泛应用，对于小步长($\le 2\ \mu\text{s}$)电磁暂态实时仿真的需求逐渐增加。此时，单独依靠 CPU 已难以满足其要求，转而结合现场可编程门阵列(Field Programmable Gate Array, FPGA)来实现是一大趋势。搭建了适用于虚拟同步并网逆变器系统实时仿真的 CPU-FPGA 异构计算平台。其中，FPGA 电路部分采用优化 EMTP (Electro-Magnetic Transient Program)流程实现，综合利用恒导纳开关建模、支路拆分并行处理及矩阵化流程计算来优化仿真实时性能。CPU 控制部分采用虚拟同步控制，并设计了与 FPGA 异步通信的数据交互接口。最后，针对该并网逆变器系统进行小步长实时仿真，与 Simulink 离线仿真结果相对比，同时分析平台实时性能与 FPGA 上资源消耗，验证了基于所提平台实现虚拟同步并网逆变器系统实时仿真的准确性与有效性。
**关键词：** 并网逆变器系统；实时仿真；虚拟同步控制；电磁暂态仿真算法；现场可编程门阵列

### Real-time simulation algorithm design of a virtual synchronous grid-connected inverter system based on a CPU-FPGA heterogeneous platform
WU Pan, WANG Keyou, XU Jin, LI Guojie
(Key Laboratory of Control of Power Transmission and Conversion, Ministry of Education (Shanghai Jiao Tong University), Shanghai 200240, China)

**Abstract:** With the wide application of power electronic devices in power systems, the demand for small time-step ($\le 2\ \mu\text{s}$) electromagnetic transient real-time simulation increases. While a CPU is unable to meet the demand alone, there is a trend to complement it with a Field Programmable Gate Array (FPGA). A CPU-FPGA heterogeneous computing platform available for real-time simulation of virtual synchronous grid-connected inverter system is built. Within it, the circuit part on the FPGA is implemented with an optimized Electro-Magnetic Transient Program (EMTP) algorithm. Constant admittance switch modeling, branch division with parallel processing and high efficiency matrix operation are used to improve real-time performance. The control part on the CPU adopts virtual synchronization control and designs a data interaction interface for asynchronous communication with the FPGA. A small step real-time simulation of the grid-connected inverter system is conducted and compared with the results of a Simulink offline simulation. At the same time, the real-time performance of the platform and resource consumption on FPGA is analyzed. All results above can verify the accuracy and effectiveness of a real-time simulation of the virtual synchronous grid-connected inverter system based on the proposed platform.
This work is supported by National Natural Science Foundation of China (No. 51877133).
**Key words:** grid-connected inverter system; real-time simulation; virtual synchronization control; electromagnetic transient simulation algorithm; field programmable gate array

## 0 引言
对电力系统动态过程做准确、详细、快速的仿真分析有助于保障系统安全稳定运行[1]。随着新能源和分布式发电技术的快速发展，以逆变器为代表的电力电子设备已深入到电力系统各方面[2-3]，其保护控制系统也越来越复杂。此时，电磁暂态小步长实时仿真凭借计算效率高、精度好、交互性强等特点[4]，能适应电力电子器件的快速动态[5]，逐渐得到广泛研究与应用。针对虚拟同步并网逆变器开展控制与故障特性仿真研究，可为研制相关控制与保护装置提供参考，降低试验成本。

离线电磁暂态仿真和传统实时仿真大多基于通用计算机或高性能计算机，以多核 CPU 为主要计算单元。随着高频动作电力电子开关的引入，离线仿真尚可采用插值算法重新计算开关动作的精确时刻[6-8]，而实时仿真中插值算法较难实现，只能采用更小的仿真步长，给 CPU 带来极大的计算负担。

当前，以 RTDS、RT-LAB 为代表的商业化实时仿真软件已在电力领域获得了广泛应用[9-10]，且开始采用 FPGA 实现电力电子器件的小步长实时仿真。相比 CPU，FPGA 具有计算能力强、高并行度、深度流水线等优势，更适合电磁暂态小步长实时仿真的实现。围绕基于 FPGA 的实时仿真实现，国内外已有相关研究。文献[11-12]提出了适用于 FPGA 的伴随离散电路(Associated Discrete Circuit, ADC)开关模型，该模型具备开关动作前后导纳矩阵不变的特点，有助于改善 EMTP 算法的实时性能。文献[13-14]采用小步长 ADC 开关模型，开发了基于 FPGA 的实时仿真器；国内研究则关注故障保护[15]、分布式发电[16-17]、有源配网[18]等多场景应用，并构建有 FPGA-RTDS[19]、多 FPGA 并行[18,20]等架构。然而，基于 FPGA 的电力电子实时仿真仍存在以下问题：1) 传统 ADC 开关模型在高频开关动作下，存在显著开关虚拟损耗，严重影响仿真精度；2) 传统 EMTP 算法串行程度高，难以发挥 FPGA 高度并行的天然优势；3) 由于电力电子设备控制系统的多样性和复杂度，在 FPGA 上同时实现电路与控制系统的小步长实时仿真，将极大地限制仿真规模。

考虑到虚拟同步并网逆变器系统中虚拟同步控制环节的复杂性与慢动态，本文将系统控制部分与电路部分拆开分别以大、小步长进行仿真，并基于 NI-PXI 系统搭建了一种 CPU-FPGA 异构计算平台用于上述系统的实时仿真实现。其中，针对现存问题，FPGA 电路部分采用了优化 EMTP 流程实现，利用广义 ADC 开关建模、支路拆分并行处理及矩阵化流程计算来优化仿真实时性能；CPU 控制部分采用虚拟同步控制，并设计了基于 PXIe 总线的数据交互接口与 FPGA 进行异步通信。最后，针对该并网逆变器系统进行算例分析，与 Simulink 离线仿真相对比，同时分析平台实时性能与 FPGA 上资源消耗，验证了基于本平台实现虚拟同步并网逆变器系统实时仿真的准确性与有效性。

## 1 基于 NI-PXI 的 CPU-FPGA 异构计算平台
离线的电磁暂态仿真软件，如 Simulink、PSCAD 等，一般运行在通用计算机 CPU 上，其模型和算法设计通常无需考虑底层硬件实现。相比之下，小步长实时仿真出于仿真速度的需要，其模型和算法往往需要结合硬件计算平台的特点进行设计。CPU 和 FPGA 两种计算单元的对比，如表 1 所示。

**表 1 CPU 和 FPGA 架构对比**
Table 1 Framework contrast between CPU and FPGA
| 平台 | 架构特点 | 优缺点 | 适用场合 |
|---|---|---|---|
| CPU | 通用型设计，兼顾计算与控制，串行架构 | 可处理复杂逻辑，计算效率一般 | 上层控制和调度处理 |
| FPGA | 可编程逻辑，计算能力强，并行架构 | 运算效率高，不适用复杂流程 | 并行高速运算 |

可见，FPGA 适合处理算法流程简单、运算量大、对运算速率要求高的计算任务；而 CPU 则适合处理算法流程复杂、运算量不大、对运算速率要求不高的计算任务。本文研究虚拟同步并网逆变器系统的实时仿真，其中包含逆变器在内的拓扑电路仿真需要小步长的高速运算，而上层逆变器控制环节流程复杂，但无需很高的处理速率，兼有上述两种计算任务，所以考虑设计一种 CPU+FPGA 异构计算的实时仿真平台。

美国国家仪器公司(National Instruments, NI)开发的 PXI 系统，是一种集成 PXIe 总线、嵌入式 CPU 控制器和可扩展 FPGA 模块的自动化平台，灵活性和可扩展性好、可靠性高。基于该 NI-PXI 平台，可搭建适用于虚拟同步并网逆变器系统实时仿真的 CPU-FPGA 异构计算平台，如图 1 所示。

图 1 中并网逆变器采用文献[21-23]所述虚拟同步发电机控制，采集逆变器出口电流 $i_{oabc}$ 及滤波后电压 $u_{abc}$、电流 $i_{abc}$ 作为控制输入，结合即时功率指令 $P_{\text{ref}}$、$Q_{\text{ref}}$，在 $dq$ 坐标系下进行解耦控制，输出逆变器所需 PWM 调制波 $m_{\text{pwm}}$。

所搭建的基于 NI-PXI 的 CPU-FPGA 实时仿真平台由上位机、PXI 机箱组件和相关外设硬件组成。图 1 中，机箱 CPU 控制器(NI PXIe-8135)运行控制部分，仿真步长取为 $100\ \mu\text{s}$；机箱 FPGA 模块(NI PXIe-7975R，Kintex-7 XC7K410T)基于优化 EMTP 算法进行小步长电气拓扑仿真，仿真步长为 $1\ \mu\text{s}$，以满足精度与实时性要求；上位机人机界面与 CPU 控制器进行观测量和控制指令交互，时间尺度设为 $500\ \mu\text{s}$，满足观测需求；外设硬件经 FPGA IO 模块进行实时波形观测及闭环控制(可选)。

**图 1 适用于虚拟同步并网逆变器系统实时仿真的 CPU-FPGA 异构平台**
Fig. 1 CPU-FPGA heterogeneous platform for real-time simulation of virtual synchronous grid-connected inverter system

各组件具体说明如表 2 所示。

**表 2 实时仿真平台各部分介绍**
Table 2 Introduction to real-time simulation platform
| 组成部分 | 时间尺度/$\mu\text{s}$ | 承担功能 |
|---|---|---|

影响仿真效率；
2) 算法串行度高，各环节计算需要大量循环遍历等串行操作，计算时间长；
3) FPGA 上多采用定点数据类型，为兼顾不同