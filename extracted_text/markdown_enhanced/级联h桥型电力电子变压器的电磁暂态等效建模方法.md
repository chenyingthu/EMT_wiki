## 级联 H 桥型电力电子变压器的电磁暂态等效建模方法
丁江萍 1，高晨祥 1，许建中 1*，赵成勇 1，曹均正 2
(1．新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206；2．中电普瑞电力工程有限公司，北京市 昌平区 102200)

## Electromagnetic Transient Equivalent Modeling Method of Cascaded H-bridge Power Electronic Transformer
DING Jiangping1, GAO Chenxiang1, XU Jianzhong1*, ZHAO Chengyong1, CAO Junzheng2
(1. State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China; 2. C-EPRI Electric Power Engineering Co., Ltd., Changping District, Beijing 102200, China)

**ABSTRACT:** The power electronic transformer (PET) applied to the medium and high voltage distribution network widely adopts a two-stage cascade structure of a cascaded H-bridge rectifier and a dual-active bridge DC/DC converter. Aiming at the problem of extremely slow simulation speed in offline simulation platforms such as PSCAD/EMTDC and MATLAB, based on the Thévenin’s equivalent and nested fast simultaneous solving algorithm, an electromagnetic transient simulation accelerated model of cascaded H-bridge PET was proposed. Specifically, by arranging the decoupling companion network of the primary/secondary side of the high-frequency transformer flexibly, the cascaded sub-modules were divided into two single-port networks, and then the equivalent part of the Thévenin’s (Norton’s) equivalent parameters were forwardly solved. Then, the equivalent part was substituted into the electromagnetic transient program for overall solution and inverse solution to initialize the electrical network for the next simulation step. Since the external equivalent form was a Thevenin’s (Norton’s) equivalent circuit with only 4 external nodes, the computational complexity of the proposed model in the overall system solution process hardly increased with the number of submodules. The cascaded H-bridge PET closed-loop control system was built in the PSCAD/EMTDC. Compared with the detailed model simulation results, the proposed model can accurately simulate the PET transient steady-state process and has a high acceleration ratio.

**KEY WORDS:** cascaded H-bridge (CHB); decoupling companion circuit; power electronic transformer (PET); Norton and Thévenin’s equivalent; electromagnetic transient (EMT); equivalent modeling

**摘 要：** 应用于中高压配电网的电力电子变压器(power electronic transformer，PET)广泛采用级联 H 桥整流器与双有源桥 DC/DC 变换器两级级联结构。针对其在诸如 PSCAD/EMTDC、MATLAB 等离线仿真平台中仿真速度极慢的问题，基于诺顿等效及嵌套快速同时求解算法，提出一种级联 H 桥型 PET 的电磁暂态仿真提速模型。具体而言，即通过灵活构造高频变压器原/副边的解耦伴随网络，将级联子模块分割为两个单端口网络，进而对等效部分正向求解诺顿(戴维南)等效参数、代入电磁暂态程序整体求解，及反解以初始化下一个仿真步长的电气网络。由于对外等效为仅包含 4 个外部节点的戴维南(诺顿)等效电路，使得所提模型在系统整体求解过程中计算复杂度几乎不随子模块个数增加。在 PSCAD/EMTDC 中搭建了级联 H 桥型 PET 闭环系统，与详细模型仿真结果对比表明，所提模型能够精确仿真 PET 暂稳态过程，且具有较高的加速比。

**关键词：** 级联 H 桥；解耦伴随电路；电力电子变压器；诺顿和戴维南等效；电磁暂态；等效建模

基金项目：国家重点研发计划项目(2016YFB0900903)。
Project Supported by National Key R&D Project (2016YFB0900903).

## 0 引言
电力电子变压器(power electronic transformer，PET)将电压变换、能量控制、动态无功补偿等功能集于一身，是未来新能源并网及交直流输配电系统互联的重要接口设备[1-4]。级联 H 桥型 PET 具备模块化结构，在中高压配电网中广泛使用，因其高压侧的 AC/DC 变换器采用级联 H 桥换流器(cascaded H-bridge，CHB)而得名[3]，中间隔离级通常采用双有源桥(dual active bridge，DAB)或多有源桥(multiple active bridge，MAB)型 DC-DC 变换器。

在 PET 设备接入电网使用之前，首先需要在仿真平台下进行仿真验证，在控制策略优化环节甚至需要进行多重运行以寻求最优控制参数[5-7]。然而，为精确反映 PET 的动态特性，必须在小步长环境下仿真。以 3 模块级联 H 桥型 PET 为例，如 DAB 采取单移相控制，工作频率在 5kHz，经仿真测试，需设置 $10\mu s$ 及以下的仿真步长才能较为精确控制移相角，严重拖慢整个系统的仿真效率。

针对这一问题，文献[8]建立了级联 H 桥型 PET 的平均值模型，在稳态及电压暂降过程中能够较精确得反映系统电气量的幅值，但完全忽略了开关动作产生的谐波，并且仅适用于采用脉宽调制(pulse width modulation，PWM)的 PET 系统。文献[9]基于 RT-LAB 平台开发了 PET 的纳秒级实时仿真模型，其本质是用等效电感/电容支路替代了电力电子开关[10]。开关状态的改变仅体现为等效电流源的取值不同，系统节点导纳矩阵保持不变，从而规避了高阶导纳矩阵求逆过程，但仍然是一种详细模型，需要消耗大量仿真资源。文献[11-12]针对采用新型多端口子模块的模块化多电平换流器，提出了一种广义戴维南/诺顿等效方法，对系统进行降维等效的同时保证了仿真精度。相比而言，级联 H 桥型 PET 属于输入串联输出并联(in-series-out-parallel，ISOP)型结构，端子约束关系与文献[11]中输入串联输出串联(in-series-out-series，ISOS)型的子模块存在差异，目前尚无针对级联 H 桥型 PET 的诺顿或戴维南等效方法。

本文提出一种级联 H 桥型 PET 的电磁暂态仿真提速模型，它属于能够精确仿真 PET 内部子模块电容特性的诺顿等效模型，且具有较为明显的提速效果。具体而言，即通过灵活构造高频变压器原/副边的解耦伴随网络，将级联子模块分割为两个单端口网络，接着基于文献[13]对单端口子模块的等效方法，对等效部分正向求解诺顿/戴维南等效参数、系统整体求解、反解以初始化下一个仿真步长的电气网络，使得所提模型在整体求解过程中计算复杂度几乎不随子模块个数增加。最后，在 PSCAD/EMTDC 中对级联 H 桥型 PET 闭环系统进行精度验证和开环加速比测试。

## 1 级联 H 桥型 PET 拓扑
图 1 为级联 H 桥型 PET 系统，具有 AC-DC-AC-DC-AC 五级电能变换，包含级联多电平 AC/DC 换流器、含 1 个高频隔离变压器的双有源桥 DC-DC 变换器和 DC/AC 换流器。低压直流母线可直接与直流负载相连，或通过 DC/AC 换流器接交流负载。本文的等效建模对象为 H 桥-DAB 作为基本单元的多模块部分，以下简称为 CHB 单元。各单元在输入侧端子首尾连接，为串联形式，输出端子分别接在正极和负极直流母线，为并联形式，即具有 ISOP 型结构。由于三相的 CHB 单元结构完全一致，因此下文均以 A 相为例展开。

**图 1 级联 H 桥型 PET 系统示意图**
**Fig. 1 Schematic diagram of cascaded H-bridge PET system**

图 1 虚框线内的部分经过等效后，需要预留用户自定义参数和数据接口，以实现对模块内各个量的控制。需要预留的用户自定义参数主要包括 IGBT 及二极管的导通和关断电阻，电容 $C_1$、$C_2$ 的容值，电容两端并联的均压电阻值(若有)，附加电抗的电感值和变压器参数等。需要预留的数据接口为 CHB 单元中的 $T_1$—$T_{12}$ 的触发信号，各 CHB 单元中电容 $C_1$ 两端的电压及输出电流等等。

## 2 CHB 单元的伴随电路构造
按基本组成元件划分，单个 CHB 单元包含 IGBT/二极管开关组、电感元件、电容元件和变压器。

在电磁暂态仿真中，设 $\Delta T$ 为一个仿真步长，各元件的时变电路参数整理如表 1 所示：关于各个 H 桥中的开关器件及电感、电容元件的等效方法，已有诸多文献给出[14-17]，即按照 $T_k (k=1, 2, \cdots, 12)$ 在当前时刻的状态，可将 IGBT/二极管开关组等