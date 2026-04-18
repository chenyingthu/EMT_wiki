## 含分层接入特高压直流的交直流混联电网机电—电磁暂态混合仿真研究
熊华强 1，杨程祥 2，马 亮 1，熊永新 2，舒 展 1，姚 伟 2，陈 波 1，程思萌 1，陶 翔 1
(1.国网江西省电力有限公司电力科学研究院，江西 南昌 330096；2.强电磁工程与新技术国家重点实验室(华中科技大学)，湖北 武汉 430074)

**摘要：**特高压直流分层接入系统在提升受端电网电压支撑的同时也带来了不同层间系统耦合关系复杂等问题。为准确研究特高压分层接入后交直流混联系统运行特性，结合±800 kV 雅中—江西分层接入特高压直流输电工程，基于 ADPSS 搭建含特高压分层直流输电系统的交直流电网混合仿真模型。首先通过仿真对比验证了纯电磁暂态模型的正确性。然后对比分析关断角独立控制指令阶跃响应下混合仿真模型和纯电磁暂态模型的仿真结果，验证了混合仿真模型的准确性和优越性。最后与机电暂态模型进行故障仿真对比。仿真分析表明，混合仿真能够准确反映特高压直流分层接入后混联系统动态特性，提供很好的仿真模型基础。
**关键词：**分层接入；交直流混联电网；电磁暂态模型；机电暂态模型；ADPSS；混合仿真

## Electromechanical-electromagnetic transient hybrid simulation of an AC/DC hybrid power grid with UHVDC hierarchical connection mode
XIONG Huaqiang1, YANG Chengxiang2, MA Liang1, XIONG Yongxin2, SHU Zhan1, YAO Wei2, CHEN Bo1, CHENG Simeng1, TAO Xiang1
(1. State Grid Jiangxi Electric Power Research Institute, Nanchang 330096, China; 2. State Key Laboratory of Advanced Electromagnetic Engineering and Technology, Huazhong University of Science and Technology, Wuhan 430074, China)

**Abstract:** UHVDC hierarchical connection to a system not only improves the voltage support of the receiving end grid but also brings problems such as the complex coupling relationship between different layers of the system. In order to study the operating characteristics of an AC/DC hybrid system with a UHVDC hierarchical connection, this paper examines the ±800 kV Yazhong-Jiangxi UHVDC transmission project. An AC/DC hybrid simulation model with UHVDC hierarchical connection mode is built based on ADPSS. First, the correctness of the electromagnetic transient model is verified. Then the accuracy and superiority of the hybrid simulation model are verified by comparing the simulation results under extinction angle step response of independent control command with the electromagnetic transient model. Finally, the fault simulation of the hybrid model is compared with the electromechanical transient model. Results show that hybrid simulation can accurately reflect the dynamic characteristics of a hybrid system and provide a simulation foundation model.
This work is supported by National Natural Science Foundation of China (No. 51577075).
**Key words:** hierarchical connection; AC/DC hybrid grid; electromagnetic transient model; electromechanical transient model; ADPSS; hybrid simulation

## 0 引言
近年来，特高压直流输电技术的成熟发展和不断应用[1-3]，促进了西北风电、光伏以及西南水电等绿色能源的开发外送[4-6]；同时，区域电网之间的互联缓解了河南、上海等中东部地区电网的用电缺口。而多回特高压直流接入同一受端电网导致交流电网电压支撑能力受到严峻挑战[7-9]，因此文献[10]从电网结构改进出发，创造性地提出特高压直流高、低端逆变器以分层方式分别接入 500 kV 和 1 000 kV不同电压等级交流电网中[11-12]。

特高压分层接入结构应用的同时也存在不同层级系统耦合关系复杂、协调控制困难等问题[13]。为准确研究特高压分层接入后混联系统运行特性，如何建立高效而精确的含特高压分层接入直流的交直流混联电网模型变得至关重要。

目前有关分层特高压直流的仿真分析大多基于电磁暂态建模[14-15]和机电暂态建模[16-17]。文献[18-19]指出以上两种建模方式分别存在等值化简误差和仿真模拟精度不够的问题，降低了仿真计算的准确性[20-21]。而采用混合仿真能够兼顾二者的优势[22-24]，且目前针对特高压分层直流系统混合仿真模型搭建鲜有研究和详细介绍。

因此，本文结合规划建设中±800 kV 雅中-江西分层接入特高压直流；应用 ADPSS 软件平台，详细阐述了对含特高压分层直流输电系统的交直流混联电网混合仿真模型的搭建。首先在 ADPSS 中搭建分层特高压直流电磁暂态模型，并与 PSCAD模型进行对比分析，验证了电磁暂态模型的正确性。然后，结合关断角指令独立控制阶跃响应仿真，仿真对比说明混合仿真模型的有效性和优势。最后对比交流故障下混合仿真模型和机电暂态模型的仿真波形。结果表明，混合仿真模型能够提供很好的仿真模型基础和参考。

*图 1 2020 年规划江西电网网架结构*
*Fig. 1 Planning of Jiangxi power grid architecture in 2020*

## 1 ADPSS 混合仿真流程
本节以雅中-江西分层接入特高压直流系统为例，对 ADPSS 混合仿真流程进行介绍。

### 1.1 雅中特高压直流分层接入系统
为弥补江西电网用电缺口，计划 2020 年建成±800 kV 雅中-江西特高压直流输电工程[17]。特高压直流双极运行，高压阀组和低压阀组以分层方式分别接入 500 kV 和 1 000 kV 不同层级交流系统。特高压直流分层接入方式下江西受端电网网架结构如图 1 所示。

雅中-江西分层特高压直流输电工程输送功率 10 000 MW，额定直流电流 6.25 kA，额定直流电压±800 kV[25]。基于 2020 年丰平大潮流运行方式，江西电网总负荷约 2 500 万 kW，通过 3 回 500 kV交流联络线和南昌-武汉 1 000 kV 特高压双回交流线和湖北电网相连，通过南昌-长沙 1 000 kV 特高压双回交流线和湖南电网相连。

*图 2 混合仿真接口等值示意图*
*Fig. 2 Interface equivalent diagram of hybrid simulation*

### 1.2 基于 ADPSS 的混合仿真流程
ADPSS 混合仿真通过等值原理和数据接口技术实现[19]。如图 2 所示，在进行混合仿真计算时将对方模型进行戴维南/诺顿等值处理[26-27]。对特高压直流分层接入后交直流混联电网进行机电—电磁暂态混合仿真建模需要完成机电侧数据和电磁侧数据准备[22]。在 PSASP 中搭建机电模型并进行网络分割，然后进行并行计算验证机电数据无误；在 ETSDAC 中搭建电磁模型并与 PSCAD 模型对比分析验证电磁数据无误。最后，进行任务分配并提交数据，启动混合仿真计算[28]。混合仿真模型搭建流程如图 3 所示。

*图 3 混合仿真模型搭建流程*
*Fig. 3 Building process of hybrid simulation model*

## 2 特高压直流分层接入系统仿真建模
本节基于 ADPSS 平台建立雅中—江西分层接入...

### 2.1 特高压分层接入一次系统建模
雅中—江西特高压直流输电工程一次系统模型拓扑如图 4 所示。该系统主要包括等值钳位电压源、整流侧换流站、逆变侧 500 kV 和 1 000 kV 换流站、直流输电线路。其中，受端 500 kV 和 1 000 kV 交流系统短路比分别为 4.53 和 6.10，换流站主要包含有换流变压器、交直流滤波器、换流器和平波电抗器[29]等设备。换流器采用双桥 12 脉波换流阀搭建而成，高、低端换流器关断角稳态运行值均为 17°[29]。

各换流器通过 Y/Y 接线与 Y/D 接线的换流变压器和交流系统相连。各换流变压器的主要参数如表 1 所示。

**表 1 换流变压器参数列表**
**Table 1 List of converter transformer parameters**
| 参数 | 整流侧 | 逆变 500 kV | 逆变 1 000 kV |
|---|---|---|---|
| 容量/MVA | 1 551 | 1 470 | 1 470 |
| 绕组电压/kV | 512/175.3 | 532/161.8 | 1021/161.8 |
| 短路阻抗/% | 23 | 19 | 20 |

### 2.2 分层接入直流输电控制系统建模
直流输电控制系统对交直流混联电网安稳运行具有重要影响[30]。由于特高压直流分层接入不同电压等级的交流电网，因此每极逆变阀组应进行独立控制[31]。以正极控制为例，整流侧和逆变侧高、低端换流站控制系统结构如图 5 所示。

图 5 中，逆变侧高、低端换流器分别进行独立控制[14]，下标 1 和 2 分别表示 500 kV 和 1 000 kV系统换流器控制量。整流侧配置有定电流控制；逆变侧