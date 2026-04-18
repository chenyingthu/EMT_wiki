## 耦合双回线路电弧故障测距的新相模变换方法
束洪春$^1$, 刘振松$^2$, 彭仕欣$^3$
（1．昆明理工大学电力工程学院，昆明 650051；
2．云南电力研究院，昆明 650051；
3．云南电网公司昆明供电局，昆明 650051）

**摘 要：** 输电线路故障测距一直是经久不衰的研究课题。根据三相系统和同塔双回线系统的阻抗矩阵关系，从能用单一模量反映所有普通三相系统故障的新相模变换矩阵出发，推导出适用于双回线的相模变换矩阵。提出了一种基于新模量变换的双回线故障定位时域算法，该算法利用某一故障模量电弧电压、电流的转移特性来构造测距算法。它具有如下特点：算法在时域中进行，所需的时间窗短，不需要滤波等环节；用最小二乘法来提高测距精度，且测距的精度不受过渡电阻、故障类型及对端系统阻抗变化的影响。大量的电磁暂态仿真结果表明，该算法具有很高的精度。
**关键词：** 六相系统；耦合双回线；电弧故障；最小二乘法；电磁暂态；故障测距；相模变换
中图分类号：TM77 文献标志码：A 文章编号：1003-6520（2009）03-0480-07

基金资助项目：国家自然科学基金（90610024；50467002；50347026；50847043）；云南省科技攻关项目（2003GG10）；云南省自然科学基金项目（2005F0005Z；2004E0020M；2002E0025M）。
Project Supported by National Natural Science Foundation of China (90610024, 50467002, 50347026, 50847043), Scientific and Technological Project in Yunnan Province (2003GG10), Natural Science Foundation of Yunnan Province (2005F0005Z, 2004E0020M, 2002E0025M).

## Locating Arc Faults on Coupling Two Parallel Transmission Lines Using the Novel Phase-model Transformation
SHU Hong-chun$^1$, LIU Zhen-song$^2$, PENG Shi-xin$^3$
（1. School of Electrical Engineering, Kunming University of Science and Technology, Kunming 650051, China;
2. Yunnan Electric Power Research Institution, Kunming 650051, China;
3. Kunming Power Supply Bureau of Yunnan Power Grid, Kunming 650051, China）

**Abstract:** According to the relationship between the impedance matrix of three-phase system and parallel transmission line system, a novel phase-mode transform matrix of parallel transmission line system was deduced from the phase-mode transform matrix of three-phase system which could reflect all types of faults by single mode, and a novel algorithm was put forward which was based on phase-mode transform for locating faults on coupling parallel transmission lines. The algorithm is obtained by the transfer characteristics relationship of the arc voltage and current at one mode. The proposed algorithm has following characteristics: it is a time-domain method, and uses the method of least squares to improve the accuracy; it is independent of source impedance. Electromagnetic transient simulation indicates that the presented algorithm maintains high accuracy for two parallel transmission lines.
**Key words:** six-phase system; coupling two parallel transmission lines; arcing fault; least error square method; electromagnetic transient; fault location; phase-mode transformation

## 0 引言
同塔双回线路共用杆塔，所需出线走廊窄，具有建设速度快、输送能力强、节省投资等优势，能够较好地满足现代电力系统对供电可靠性和大容量输电的要求，在国内外电力系统中的应用日益广泛。同杆双回线同用一杆塔，不仅相间存在互感，回线间也存在互感，故障分析时需要对双回线进行解耦计算。解耦计算就是将相互耦合的线路相量分解成彼此独立的模量，也就是相模变换。比较经典的相模变换有：对称分量变换、Clarke变换、Karenbauer变换等[1,2]，其中，对称分量变换中含有复数因子，适用于工频稳态下的相序变换，Clarke变换和Karenbauer变换等变换矩阵中元素全为实数，适用于频域分析同时也适用于时域分析。研究[3]发现Clarke和Karenbauer变换在故障分析时必须使用双模量或与选相配合，使计算量大大增加。文献[3]在分析现有相模变换矩阵不足的基础上，构造出一种新的相模变换矩阵，该方法用单一模量就能反映三相系统中所有的故障类型。
本文根据三相系统和同塔双回线系统之间的关系，推导出能用单一模量反映所有双回线故障的相模变换矩阵，并用此相模变换矩阵将双回线解耦为6个独立的模量，在某一模量下利用电弧电压、电流的转移特性构造测距算法来实现测距。大量的电磁暂态仿真表明，该算法具有很高的测距精度。

## 1 六相系统相模变换矩阵的推导
对于如图1所示的三相线路[4,5]，$Z_s$为线路各相的自阻抗，$Z_m$为线路各相之间的互阻抗，根据图1可以写出矩阵
$$
\begin{bmatrix} U_{mnA} \\ U_{mnB} \\ U_{mnC} \end{bmatrix} = \begin{bmatrix} Z_s & Z_m & Z_m \\ Z_m & Z_s & Z_m \\ Z_m & Z_m & Z_s \end{bmatrix} \begin{bmatrix} I_{mnA} \\ I_{mnB} \\ I_{mnC} \end{bmatrix} \tag{1}
$$
即 $U_{mn} = Z I_{mn}$。从$Z$中可以看出，三相输电线路之间存在耦合关系，要进行线路故障分析首先要对线路进行解耦计算[6]，解耦计算的实质就是对阻抗矩阵进行对角化。
由特征值方程 $\det(Z - \lambda I) = 0$，可以解得
$$
\begin{aligned}
\lambda_1 &= Z_s + 2Z_m, \\
\lambda_2 &= \lambda_3 = Z_s - Z_m.
\end{aligned} \tag{2}
$$
式中，$\lambda_i$为模变换矩阵$P$的第$i$（$i=1,2,3$）个特征值。设$X_i$为对应于$\lambda_i$的特征向量，由矩阵特征值和特征向量的性质可得[7,8]

图1 三相输电线路示意图
Fig. 1 Schematic of transmission line

图2 同塔双回线示意图
Fig. 2 Schematic of double-circuit transmission line