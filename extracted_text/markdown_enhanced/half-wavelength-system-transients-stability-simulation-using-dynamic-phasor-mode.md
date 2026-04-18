# 输电线路工频动态相量模型在半波长交流输电系统机电暂态仿真中的应用研究
## Half-wavelength System Transients Stability Simulation Using Dynamic Phasor Model of AC Transmission Line

**张彦涛**$^{1}$，**秦晓辉**$^{2}$，**汤涌**$^{2}$，**苏丽宁**$^{2}$，**王义红**$^{2}$，**孙玉娇**$^{2}$，**姜懿郎**$^{2}$，**董毅峰**$^{2}$，**王毅**$^{2}$，**葛磊蛟**$^{1}$
(1．天津大学，天津市 南开区 300072；2．电网安全与节能国家重点实验室(中国电力科学研究院)，北京市 海淀区 100192)

**ZHANG Yantao**$^{1}$, **QIN Xiaohui**$^{2}$, **TANG Yong**$^{2}$, **SU Lining**$^{2}$, **WANG Yihong**$^{2}$, **SUN Yujiao**$^{2}$, **JIANG Yilang**$^{2}$, **DONG Yifeng**$^{2}$, **WANG Yi**$^{2}$, **GE Leijiao**$^{1}$
(1. Tianjin University, Nankai District, Tianjin 300072, China; 2. State Key Laboratory of Power Grid Safety and Energy Conservation (China Electric Power Research Institute), Haidian District, Beijing 100192, China)

**ABSTRACT:** In order to accurately simulate the wave transmission characteristics of the half wavelength AC line in the electromechanical transient simulation, this paper presents the application of AC line dynamic phasor model to the half wavelength transmission system simulation. The key to the application of the dynamic phasor model in the electromechanical transient simulation is the simulation precision and the simulation step size. When simulating external fault, half cycle simulation time step can be directly applied. While simulating internal faults of the half wavelength AC line still with half cycle time step, the approximate linear interpolation method must be used. To take account of simulation precision and speed, variable time step method was proposed. Based on the results comparison of electromagnetic transient simulation and electomechanical transient simualtion, it shows that the dynamic phasor model is more accurate than the traditional AC line steady state model, and the variable time step method is superior to the approximate linear interpolation method with fixed large time step.

**摘要：** 为了在机电暂态仿真中准确模拟半波长交流线路的波传输动态特性，提出将交流线路的动态相量模型应用于半波长输电系统仿真。动态相量模型在机电暂态仿真中得以应用的关键是仿真精度和仿真步长问题。半波长线路区外故障时，可以直接应用半周波固定步长进行机电暂态仿真；而当模拟半波长线路区内故障时，若仍采用半周波固定步长，则需应用线性插值的近似方法计算注入电流源。为保证仿真精度，并兼顾仿真速度，提出采用变步长仿真方法用于半波长线路区内故障。以电磁暂态仿真结果为基准，点对网半波长交流输电系统算例表明，动态相量模型比传统的交流线路稳态模型具有更高的仿真精度，且变步长仿真方法优于线性插值近似法。

**KEY WORDS:** half wavelength; electromagnetic transient; transient stability; dynamic phasor; point to network transmission

**关键词：** 半波长；电磁暂态；机电暂态；动态相量；点对网输电

**基金项目：** 国家电网公司科技项目(JS71-16-001, XT71-16-001)。
**Project of State Grid Corporation of China (JS71-16-001, XT71-16-001).**

## 0 引言

随着我国西电东送战略的实施，半波输电技术作为一种具备发展前景的远距离、大容量交流输电方式[1-9]，重新成为新的研究热点。近年来，我国电力学者对特高压交流半波长输电技术的技术经济可行性进行了较为全面而详细的研究，内容涵盖半波长输电的稳态运行及潮流特性[10-14]、机电暂态特性及输送能力[10]，线路单相重合闸过程的潜供电流及其恢复电压、工频过电压、操作过电压及其限制措施[15-17]、绝缘配合、继电保护[18-21]、经济性和可靠性[22-23]等。在半波长输电系统机电暂态相关计算中，目前的处理方法仍是采用传统的稳态交流线路模型，该模型只考虑了分布参数的影响，与短线路的稳态模型没有本质上的差别。

交流线路的功率传输本质上是电磁波的传输过程，当交流线路长度较短(远小于电磁波的波长)时，线路一端电压发生变化，沿线的电压、电流分布几乎在瞬间即可结束过渡过程达到新的稳态。对于机电暂态过程尺度而言，该过渡过程是可以忽略的，从而线路模型可近似用稳态方程描述。但是当交流线路的长度达到与电磁波的波长可比时(如半波长输电)，该过渡过程将足以影响到机电暂态仿真的结果。电磁暂态的仿真结果表明，当半波长线路末端短路时，故障点与两侧系统之间电磁波反射过程需持续 0.8~1.0s 左右沿线电压电流才能达到短路稳态。如果忽略该过渡过程，而将电气量瞬间达到稳态的模型用于机电暂态仿真，势必会造成较大的偏差。

为了弥补稳态模型的不足，同时又不像电磁暂态模型那样详细，1994 年 V. Venkatasubramanian 把基于状态空间平均理论的“动态相量法”引入电力系统分析中[24]。动态相量法能有目的地选择系统占主导优势的频率进行相量域内的分析，与电磁暂态仿真相比，能有效减少计算量，加快仿真速度。目前关于动态相量模型的应用研究主要集中于高压直流输电 [25-26]、可控串补 [27]、柔性直流输电 [28]等含电力电子器件系统在较宽频谱下的响应特性。文献[29-30]对交流线路的动态相量模型进行初步探索，但其研究场景仍是常规短线路的仿真分析，没有充分体现交流线路动态相量模型的价值。关于动态相量模型的应用研究已持续十余年，但尚未见到在商业化仿真工具中普及应用的报道。

半波长输电线路的特征，决定其有必要并且非常适合应用动态相量模型进行机电暂态仿真。电磁波在半波长交流输电线路的传输时间刚好可以达到半个工频周波，而通常机电暂态仿真的步长也为半个工频周波，这使得半波长交流线路的工频动态...

设 $u=u(x,t)$、$i=i(x,t)$ 分别为 $t$ 时刻位置 $x$ 处的电压、电流瞬时值，$L_0$、$R_0$、$C_0$、$G_0$ 为传输线基本电气参数，分别为单位长度的电感、电阻、电容和电导。传输线方程可表示为：
$$
\begin{cases}
\frac{\partial u}{\partial x} + L_0 \frac{\partial i}{\partial t} + R_0 i = 0 \\
\frac{\partial i}{\partial x} + C_0 \frac{\partial u}{\partial t} + G_0 u = 0
\end{cases} \tag{1}
$$

为了与机电暂态仿真中其他各元件保持一致，只计及网络电气量的工频分量。处于波传输过渡过程中的交流线路，其沿线各位置的电压、电流工频分量均随时间变化。$t$ 时刻位置 $x$ 处的电压、电流瞬时值可分别用相量表示为：
$$
\begin{cases}
u(x, t) = \text{Re}[\dot{U}(x, t) e^{j\omega t}] \\
i(x, t) = \text{Re}[\dot{I}(x, t) e^{j\omega t}]
\end{cases} \tag{2}
$$
式中：$\omega$ 为工频角速度；$\dot{U}(x, t)$、$\dot{I}(x, t)$ 分别为线路上 $x$ 位置相对于同步转速旋转相量空间的电压、电流时变相量。

将式(2)代入传输线方程(1)，可得用时变相量表示的传输线方程，如式(3)所示，该式与文献[29]基于总的平均方法理论推导出的动态相量交流线路模型具有相同的形式。需要说明的是，对于传统的稳态方程，由于忽略波传输过程中各点电气量随时间变化的过程，认为瞬间到达稳态，这相当于方程(3)中电压、电流对时间的微分项置零。
$$
\begin{cases}
\frac{\partial \dot{U}}{\partial x} + (R_0 + j\omega L_0)\dot{I} + L_0 \frac{\partial \dot{I}}{\partial t} = 0 \\
\frac{\partial \dot{I}}{\partial x} + (G_0 + j\omega C_0)\dot{U} + C_0 \frac{\partial \dot{U}}{\partial t} = 0
\end{cases} \tag{3}
$$

为了求解式(3)，通常先忽略传输线的损耗，从而得到无损传输线电气量的解析表达式，即贝瑞隆方程。然后将有损传输线处理为两段，并将电阻集中在分段线路的两侧[29-30]，此处不再重复，直接给