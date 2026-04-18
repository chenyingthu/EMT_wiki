## 适用于电磁暂态仿真的变阶变步长 3S-DIRK 算法
Variable Order/Step Integration by 3-stage Diagonally Implicit Runge-Kutta Method for Electromagnetic Transient Simulations
叶小晖 1，汤涌 1，宋强 2，刘文焯 1，吕广宪 1，陆一鸣 1
（1．中国电力科学研究院有限公司，北京市 海淀区 100192；
2．清华大学 电机工程与应用电子技术系，北京市 海淀区 100084）
YE Xiaohui1, TANG Yong1, SONG Qiang2, LIU Wenzhuo1, LÜ Guangxian1, LU Yiming1
(1. China Electrical Power Research Institute, Haidian District, Beijing 100192, China;
2. Dept. of Electrical Engineering, Tsinghua University, Haidian District, Beijing 100084, China)

ABSTRACT: When dealing with the numerical oscillation in electromagnetic transient simulation, a lower order numerical integration switched may lead to a larger numerical error. Based on the butcher tableau, firstly, the accuracy and stability of the critical damping adjustment method are studied and a 3-stage diagonally implicit Runge-Kutta(3S-DIRK) formula is proposed. This formula is composed of 4 methods with different advantages suitable for different electromagnetic transient situations. Then the simulation strategies are given by switching among these 4 methods to solve the electromagnetic simulation problems. The accuracy of the proposed 3S-DIRK is no less than 2nd order during the whole calculation, and its L-stable property can eliminate the numerical oscillation and moreover can calculate in variable steps. The equivalent circuit of the linear components is derived, illustrating the application of the 3S-DIRK method. Finally, 2 cases are listed to verify the effectiveness and advantages of the 3S-DIRK method.

KEY WORDS: electromagnetic transient simulation; diagonally implicit RK formula; numerical oscillation; butcher tableau; switching strategy

摘要：电磁暂态仿真在计算过程中将产生数值振荡现象，现有算法切换到低阶数值积分算法将导致较大的数值误差。文章利用布彻矩阵和龙格库塔理论对数值临界阻尼 CDA 算法的准确性和稳定性进行了分析，提出一种三级半角隐式龙格库塔 (3-stage diagonally implicit Runge-Kutta formula，3S-DIRK)算法，该算法具有 4 个分算法，分算法具有不同的优点，可以用在电磁暂态的不同计算情形。文章给出了算法应用于电磁暂态的仿真策略，在切换算法时可以保证元件的等值导纳不变，整个仿真过程中计算精度不低于 2 阶，且故障期间具有 L 稳定可以消除数值振荡，支持变步长计算。文章利用该算法推导了线性元件的等值电路，对该算法的使用方法进行了说明。最后使用 2 个算例验证 3S-DIRK 算法的有效性和优点。

关键词：电磁暂态仿真；半角隐式龙格库塔算法；数值振荡；布彻矩阵；算法切换策略
DOI：10.13335/j.1000-3673.pst.2020.0918

基金项目：国家重点研发计划项目(2016YFB0900601)。
Project Supported by National Key Research and Development Program of China (2016YFB0900601).

## 0 引言
电力系统电磁暂态仿真主要用于仿真和分析故障或操作后的电磁场变化以及可能出现的暂态过电压和过电流问题[1]。随着高电压大容量直流输电系统、新能源场站和柔性交流输电技术(flexible ac transmission system，FACTS)装置在电力系统中的广泛应用，互联电网的动态特性发生了深刻的变化，电力电子元件引起的波形畸变及其快速暂态过程对电网稳定性的影响越来越大[2-4]。基于稳态理想状态的机电暂态准稳态模型无法模拟电力电子元件快速开关过程，对换流器特殊运行状态、换相失败等问题的模拟准确度与实际系统仍有一定差距[5-6]。特高压直流工程的详细动态模拟和直流输电系统对电网稳定性的影响分析，需要求助于电磁暂态仿真工具[7-9]。

电磁暂态求解是典型的微分代数方程(differential algebraic equation，DAE)求解问题，这种方程的求解比常微分代数方程(ordinary differential equation，ODE)更复杂[10]。电磁暂态仿真可以分为状态变量法和节点分析法 2 种，在状态变量法中可以根据 DAE 的微分指数将其转换为 ODE 方程进行求解[11]，但是这种转换求解方法的缺点是，破坏了方程中变量的明确物理意义，也不能保持方程可能存在的系数结构。电磁暂态中应用更广的主要是节点电压法，并采用隐式梯形法作为主算法进行求解，该算法具备对称 A 稳定特性，能够将系统中的不稳定模式都表现出来，同时不存在超稳定性问题，目前在电力系统仿真中应用最广[12-13]。

针对 DAE 的数值求解问题，文献[10]发现由于代数方程的存在，A 稳定算法将产生数值振荡问题，需要利用 L 稳定的算法消除数值振荡。电磁暂态程序在处理开关时，也遇到了类似的数值振荡问题，这主要是由于电容电感等元件在换路过程中隐式梯形积分算法对非状态变量突变的处理不当造成的，一般采用增加数值缓冲电路[14]、阻尼梯形法[15]、数值临界阻尼法(critical damping adjustment，CDA)[16]、2 级对角隐式龙格库塔算法(2 stage diagonally implicit Runge-Kutta，2S-DIRK)[17-18]、root-matching 法[19]等来解决，其中 CDA 法采用两步后退欧拉法不需要修改导纳矩阵，且具有很好的适应性，被广泛应用于 EMTP 软件中[20]。

## 1 龙格库塔算法
### 1.1 算法概述
标准的数值积分算法可以分为 3 类：单步多级龙格库塔法、多步 Adams 算法、多步 Gear 算法，后 2 种属于多步算法。由于电磁暂态在仿真电力电子元件动作时，需要处理不连续的间断点，多步法需要重新启动，在 DAE 方程中容易造成不收敛的情况，因此，电力电子元件仿真一般采用单步法计算。单步法都可以转换为龙格库塔格式，s 级的龙格库塔法可以写成式(1)的形式。
$$
\begin{cases}
F_i = f(t_n + c_i h, y_n + h \sum_{j=1}^s a_{ij} F_j) \\
y_{n+1} = y_n + h \sum_{i=1}^s b_i F_i
\end{cases} \tag{1}
$$
式中 $F_i$ 表示单步法的中间计算变量。为了描述式(1)，常常使用布彻矩阵对其描述和分析[29]：
$$
\begin{array}{c|c}
\mathbf{c} & \mathbf{A} \\
\hline
& \mathbf{b}^\mathrm{T}
\end{array} \tag{2}
$$