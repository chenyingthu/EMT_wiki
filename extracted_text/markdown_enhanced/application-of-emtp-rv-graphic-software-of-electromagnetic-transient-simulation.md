# 图形化电磁暂态仿真软件EMTP-RV及其应用
曹玉胜，陈允平
（武汉大学电气工程学院，武汉 430072）

**摘要：** 为在电力行业中推广基于Windows平台的新一代图形化电磁暂态仿真工具EMTP-RV（Restructured Version），以便能高效研究电力系统及装置的动态行为，详细说明了该软件包的3个组成部分：EMTP-RV核心计算引擎、EMTPWorks图形化编辑界面和ScopeView可视化数据处理程序；描述了其主要元器件模型的基本功能；通过对1台$35\ \text{kV}$、$100\ \text{MVA}$静止无功补偿器（SVC）三相阀组动态开关过程的建模和仿真，演示了EMTP-RV的友好界面和强大功能。结果表明，EMTP-RV有效简化了电力系统中暂态过程的研究工作，为复杂电力系统的仿真提供了有力支持。
**关键词：** 电磁暂态；软件仿真；开关暂态；EMTP；SVC；ScopeView
中图分类号：TM743；TM86  文献标志码：A  文章编号：1003-6520（2007）07-0154-05

# Application of EMTP-RV Graphic Software of Electromagnetic Transient Simulation
CAO Yu-sheng, CHEN Yun-ping
(School of Electrical Engineering, Wuhan University, Wuhan 430072, China)

**Abstract:** In order to introduce how to use EMTP-RV (Restructured Version), a new generation Windows-platform-based graphic software of electromagnetic transient simulation which is developed by EMTP-DCG (Development Coordination Group), and to efficiently research and simulate the dynamic processes of power system and its apparatuses, this paper elaborates the basic features of three components of the software package: EMTP-RV core computation engine, graphical user interface EMTPWorks and signal post-processing program ScopeView. Meanwhile, the libraries which include most important device models are depicted. A $35\ \text{kV}$, $100\ \text{MVA}$ Static Var Compensator simulation model was constructed to simulate the switching processes of its three-phase thyristors. The intuitive and user-friendly Graphical User Interface and powerful computation engine of EMTP-RV is vividly demonstrated by the modeling and simulation processes of SVC. The results of simulation proved that EMTP-RV can be effectively used to simplify the research task of electromagnetic transient simulations in power system, and provide powerful aid to power engineers on the simulation of complicated power system. Its wide application will benefit the development of whole power industry.
**Key words:** electromagnetic transients; software simulation; switch transients; EMTP; SVC; ScopeView

## 0 引言
现代电力系统是集发电、输电、配电和用电为一体的复杂非线性网络系统。对其物理本质的研究涉及到$1\ \mu\text{s} \sim 1\ \text{h}$的动态过程。为保证实际运行的电力系统安全稳定性，不便采用在线物理试验的方法对电力系统的动态行为进行研究。目前主要利用电力系统仿真软件离线计算法对电力系统及装置的动态行为进行仿真研究。

根据需要研究的动态过程作用时间长短，电力系统暂态过程主要分为机电暂态过程和电磁暂态过程两大类。一般把$>1\ \text{ms}$的动态过程归类为机电暂态过程，它包含电力系统的次同步振荡、电力系统暂态稳定、发电机组控制过程、潮流和短路等物理过程，常用PSS/E[1]，Simpow，Eurostag，BPA，Power World Simulator，POWERTECH DSA，PSASP等机电类仿真软件进行研究。而把$<1\ \text{ms}$的动态过程归类为电磁暂态过程，它包含电力线行波现象、开关暂态、谐波、雷击过电压、电抗器和变压器饱和、电力电子开关状态转换、气体放电等物理过程，常用EMTP/ATP[2-5]、PSCAD/EMTDC等电磁类仿真软件进行研究。部分软件象NETOMAC[6]、DIgSILENT、SimPowerSystems同时具有电磁和机电类动态过程的仿真能力[7,8]。

本文介绍的EMTP-RV（Restructured Version）[9]是基于Windows平台的新一代图形化电磁类仿真软件，它是对经典电磁暂态工具EMTP的重新构造。在介绍其基本功能和组成的基础上，通过对1台$35\ \text{kV}$，$100\ \text{MVA}$静止无功补偿器（SVC）三相阀组动态开关过程的建模和仿真，演示EMTP-RV的友好界面和强大功能。

基金资助项目：湖北自然科学基金（2005ABA289）。
Project Supported by Natural Science Foundation of Hubei Province (2005ABA289).

## 1 EMTP-RV组成结构
从1960年加拿大H.W. Dommel教授进行电磁暂态分析程序的研究工作开始[2]，到现在EMTP已经经历了近半个世纪的发展。目前最新版本EMTP-RV是由EMTP开发协作组（EMTP-DCG：EMTP Development Coordination Group）负责开发与维护的，是对早期DOS版本EMTP的Windows图形化重构。重构的EMTP-RV使用面向对象的编程模式，根据所处理对象的不同分为EMTP-RV核心数据处理引擎、EMTPWorks图形化编辑界面和ScopeView可视化数据处理程序3个不同部分。

**图1 EMTP-RV组织结构图** (Fig. 1 Framework of EMTP-RV)

图1按照数据处理流程展示了EMTP-RV的3个组成部分间的相互关系。EMTPWorks提供给用户一个图形化的建模环境，它将使用者用图形模块搭建的系统模型转换为EMTP-RV计算引擎可识别的网络表`*.NET`文件。EMTP-RV计算引擎则根据读入的网络表`*.NET`文件，分析网络拓扑结构，解析元器件模型，构成系统计算矩阵并按给定的条件进行仿真，最后将仿真结果写入二进制的数据文件`*.mda`和相关ASCII文本绘图文件`*.m`。可视化数据处理程序ScopeView对EMTP-RV计算引擎输出的数据做进一步加工处理，最终以多组彩色曲线图的形式显示仿真结果。这3个组成部分为用户提供了一个完善的集成环境。由于不受传统DOS版本字符界面的限制，对同一网络模型，它提供频域、时域、稳态和统计分析4种可选计算模式；还能够自动初始化稳态求解过程，并可提供稳态模型的谐波求解。其开放的体系结构允许用户使用自定义的复杂模型，并对现有的专用工具箱进行扩展。

ScopeView可视化数据处理程序能够对Matlab、Comtrade和EMTP-RV格式的数据文件进行处理。它提供了基本的图形缩放、叠印、多列和多页图形显示功能；能够动态跟踪显示光标所在处数据值，显示节选图形区域内的最大值、最小值、均值和有效值。内建的函数编辑器可以对数据进行后处理，实现从简单的加减乘除类算术运算到复杂的离散傅里叶变换、谐波分析等函数功能。支持线性和指数形式的坐标轴表示，并能方便地使用属性页编辑显示曲线的标题、坐标轴标签、显示线型和图例等属性。能够将当前显示模式和数据处理过程保存为