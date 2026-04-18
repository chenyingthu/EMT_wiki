## 基于 FPGA 的双馈风力发电机定转子解耦数字镜像超实时仿真
陈厚合 1，杨 政 1，叶 华 2，裴 玮 2，KAI Strunz3
（1. 东北电力大学电气工程学院，吉林 132012；2. 中国科学院电工研究所，北京 100190；3. 柏林工业大学，柏林 10587）

## Faster-than-real-time Simulation of Stator-rotor Decoupling Digital Twin of Doubly-fed Induction Generator Based on FPGA
CHEN Houhe1, YANG Zheng1, YE Hua2, PEI Wei2, KAI Strunz3
(1. School of Electrical Engineering, Northeast Electric Power University, Jilin 132012, China; 2. Institute of Electrical Engineering, Chinese Academy of Sciences, Beijing 100190, China; 3. Technische Universität Berlin, Berlin 10587, Germany)

**摘 要：**为实现双馈风力发电机(doubly fed wind generator，DFIG)大规模实时仿真，设计了一种基于现场可编程逻辑阵列(field programmable gate array，FPGA)的 DFIG 数字镜像 IP 核。并提出面向异步机定子与转子“T 型”等效电路解耦的虚拟电容等效法，在此基础上提出 DFIG 内部各组件并行算法，最后构建 DFIG-IP。通过流水线优化设计，完成基于 FPGA 的 DFIG-IP 在 4 种工况下计算精度与计算速度的实验验证。研究结果表明：该文所提方法降低 DFIG 异步机求解模块所需 FPGA 资源约 77%；基于 FPGA 设计的 DFIG-IP 在 500 MHz 时钟频率下，超实时加速度比可达 27.8，单个 DFIG-IP 占用 ZCU106 资源不超过 20%；所提方法能够满足 DFIG 并网系统实时仿真在精度与速度上的要求。研究结果可为含大量新能源并网系统的电磁暂态仿真加速研究提供参考。
**关键词：**现场可编程逻辑阵列(FPGA)；虚拟电容等效；并行计算；双馈风力发电机；超实时仿真

**Abstract：**To achieve the large-scale real-time simulation of doubly fed wind generator (DFIG), we designed a DFIG digital image intelligent property (IP) core based on field programmable gate array (FPGA), and proposed a virtual capacitance equivalent method for decoupling the “T-shaped” equivalent circuit of the stator and rotor of the asynchronous machine. Based on this, a parallel algorithm for each component in DFIG was proposed. Finally, DFIG-IP was constructed. Through pipeline optimization design, we performed the experimental verification of the calculation accuracy and speed of DFIG-IP based on FPGA under four working conditions. The research results show that the proposed method can be employed to reduce the FPGA resource required by DFIG asynchronous machine solution module about 77%. The DFIG-IP designed based on FPGA can achieve a faster-than-real-time acceleration ratio of 27.8 at 500 MHz clock frequency, and a single DFIG-IP can occupy no more than 20% of ZCU106 resources. The method proposed can meet the requirements of DFIG grid connected system real-time simulation in accuracy and speed. The research in this paper can provide a reference for accelerating the research of electromagnetic transient simulation of grid connected systems with a large number of new energy sources.
**Key words：**field programmable gate array(FPGA); virtual capacitor equivalent; parallel computing; doubly-fed induction generator; faster-than-real-time simulation

基金资助项目：国家自然科学基金 (52177123；52077028)。
Project supported by National Natural Science Foundation of China (52177123, 52077028).

## 0 引言
双馈风力发电机作为新能源发电的一种，具有技术成熟、价格较低的优点，国内风电以双馈机型为主[1]。我国 2021 年提出，新能源要成为主体电源，海量双馈机组接入电力系统已为必然[2]。风电机组大规模接入电网，将给电力系统电磁暂态仿真带来诸多挑战[3]。电磁暂态仿真是研究电力系统动态特性的重要手段，然而双馈机型构成较为复杂，双馈风电场电磁暂态仿真效率低下，而数字孪生电力系统[4-7]又对电磁仿真的计算精度与计算速度两方面提出更高的要求。因此，亟需研究仿真效率更高和准确性更强的风电场电磁暂态仿真方法。

当前开展风电大规模仿真，主要利用风电场等值方法、改良求解算法及提升计算平台硬件性能来实现。风电场等值建模方法 [8-10]，主要用于研究风电场外特性，而在研究宽频振荡问题时，需要考虑具体换流器的内外环及其锁相角度的控制措施[8]，多机等值忽略了每台风电机配置参数的特异性[11]，这对于数字化电力系统智能终端的建立是不可接受的。而改良求解算法[12-14]，如采用解耦算法或采用换流器平均值模型，可保留每台风电机的特异性且可加快其电磁暂态仿真速度，但对于风电机大规模仿真仍不能实时计算[12]。对于提升硬件性能主要采用中央处理器(central processing unit，CPU)多核并行计算、CPU 与图形处理器(graphics processing unit，GPU)异构并行计算以及建造实时仿真平台来实现。GPU 较 CPU 更适合并行计算场景。文献[15]基于 CPU 的多线程运算能力对含 DFIG 的风电场进行加速计算，但实验结果表明，此方法对于大规模风电并网系统电磁仿真仍有缺陷。文献[16-17]突破传统单 CPU 架构，采用 CPU+GPU 异构平台对电磁暂态仿真加速。文献[16]研发的 CloudPSS 电磁仿真平台，对 500 台直驱风机 1 s 物理过程仿真，采用 GPU 异加速时，耗时 5 s，极大的提高了仿真速度。文献[17]构建了一个基于 GPU 的并行仿真平台，在 100 台双馈风力发电机(doubly fed wind generator，DFIG)风场算例下验证了 CPU+GPU 相结合的仿真较传统 CPU 仿真拥有计算速度优势。虽然这些方法提高了风场电磁暂态仿真速度，但对数据预处理以及每个时步仿真结果的处理仍依赖 CPU，仍会付出较大的时间成本，此外 GPU 售价高昂，工程上采用此方法开展电磁暂态仿真代价巨大。由此可知：1）采用新的加速算法，如果仿真平台的性能不改善，仿真速度仍不会有质的提升；2）建造性能更好的仿真平台花费巨大，工程上难以实现。

现场可编程逻辑阵列(field programmable gate array，FPGA)内部拥有海量查找表(look-up-table，LUT)、触发器(flip flop，FF)等资源，较 CPU 具有低功耗、高灵活性及高实时性等优点，较 GPU 又具有价格优势。FPGA 在解决电力系统电磁暂态仿真问题方面已体现出优良的性能 [18] 。有研究采用 FPGA 开发了一种嵌入式实时仿真器，可模拟实际物理对象的动态特性，如文献[19]研究了电力电子设备中基于 FPGA 嵌入式实时模拟器，当换流器故障后，FPGA 可替代换流器的控制部分发出正确的控制信号维持换流器正常运行。也有研究将物理实体抽象为数据模型，采用 FPGA 的高并行计算能力对模型进行求解。又如文献[20]将换流器定义为 1 个具有随机变量的概率模型，并将该模型嵌入到 FPGA 设备上进行实时求解并发出控制信号。这种模拟方法在一些文献中被定义为电力系统器件级数字孪生[4-7,15,20-21]。以上文献针对矩阵的求逆运算均预先存于 FPGA 的随机存储器 (random access memory，RAM)中，此方法虽可降低资源使用率，但同时会降低模型的通用性。

从现有研究看，针对单个 DFIG 设备内部各模块间的并行研究不足，对 DFIG 进行实时“镜像复现”的数字镜像系统[22]设计亦鲜有研究。其次，由于异步机电压–磁链方程每时步求解需要对矩阵进行求逆运算[15]，在 FPGA 器件中实现较为困难，因此风场仿真多基于 CPU，目前未有采用纯 Verilog 语言编制的 DFIG 数字镜像 IP 核(Intellectual Property，用于表征具有自主知识产权的预定义系统级功能模块或核心模块）对 DFIG 仿真加速的相关研究，以下简称为 DFIG-IP。

针对以上问题，本文提出虚拟电容等效法，将其用于异步机定转子解耦，避免异步机电压–磁链方程每时步矩阵求逆计算。其次，本文基于时步内数据无关可并行原则提出 DFIG 内部各组件并行算法，并在此基础上采用 Verilog 语言设计 DFIG-IP。最后，将本文设计的 DFIG-IP 烧录至 FPGA 中，进行与 RT-lab 互联平台的硬件实验，验证基于 FPGA 的 DFIG-IP 的计算精度与速度。

## 1 虚拟电容等效法与异步机定转子解耦
### 1.1 虚拟电容等效法
由戴维南定理可知，系统稳态时，阻抗相同的元件接入同一电路，端口电压可保持不变。考虑电机机械部分比电气部分时间尺度长，在电磁仿真极短的离散时间内转子转速近似不变，即在离散时间内存在短暂的稳态。因此，在这个极短的离散时间内，采用与实际电感相同阻抗的虚拟电容接入原电路，可保持励磁电压不变。

图 1 为三支路均为电感的“T 型”电路。考虑节点 m 对地支路为励磁电感 $L_m$ 时，列写基尔霍夫定律(KVL)并采用中点积分法在$(n-1/2, n+1/2)$时段内离散化可得式(1)。考虑短暂稳态，用虚拟电容 $C_m$ 替代励磁电感 $L_m$ 并采用中点积分法在$(n,n+1)$时段内离散化可得式(2)。对节点 m 两侧的 ab 绕组列写 KVL 并采用中点积分法在$(n-1/2,n+1/2)$时段内离散化可得式(3)。

$$u_m^{n+1/2} = \frac{L_m}{\Delta t} \left( i_m^{n+1/2} - i_m^{n-1/2} \right) \quad (1)$$

图 1 虚拟电容励磁支路解耦
Fig.1 Virtual capacitor magnetizing branches decoupling

的所有关系式。将其相加后，m 节点的电压恒等变化并相加可得
$$n-1$$