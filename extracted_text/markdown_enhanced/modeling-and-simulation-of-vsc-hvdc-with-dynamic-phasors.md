## 电压源型直流输电的动态相量建模与仿真
姚伟，程时杰，文劲宇
（华中科技大学电力安全与高效湖北省重点实验室，武汉430074）

**摘要：**为适应电力系统快速精确仿真和分析控制的需要，采用了一种新的建模方法—基于时变傅立叶级数的动态相量法，对电压源型直流输电（VSC-HVDC）进行建模和仿真。该方法通过保留与系统状态变量相对应的时变傅立叶级数中的重要项对原系统进行简化，首先建立用开关函数描述的 VSC-HVDC 换流站详细时域模型，在此基础上，给出 VSC-HVDC 动态相量模型的详细推导过程。在对 VSC-HVDC 进行动态相量建模的过程中，换流站的开关函数考虑直流分量和基频分量，直流传输线路只考虑直流分量，从而大大简化高频开关过程，在保证仿真精度的同时，大大缩短了仿真时间。通过 MATLAB 仿真软件用动态相量模型与详细时域电磁暂态（EMT）模型分别对 VSC-HVDC 进行仿真比较的结果表明，动态相量模型精确而有效，不仅可以精确描述 VSC-HVDC 的暂态变化过程，而且可以大大节省仿真计算时间。
**关键词：**电力系统；电压源型直流输电；动态相量模型；时变傅立叶级数；开关函数；电磁暂态模型
中图分类号：TM721.1   文献标志码：A   文章编号：1003-6520（2008）06-1115-06

## Modeling and Simulation of VSC-HVDC with Dynamic Phasors
YAO Wei, CHENG Shi-jie, WEN Jin-yu
（Electric Power Security and High Efficiency Lab, Huazhong University of Science and Technology, Wuhan 430074, China）

**Abstract:** To meet the needs of rapid accurate simulation and analysis of the power system, a newly developed method-dynamic phasors method is applied to a model voltage sources converter based HVDC（VSC-HVDC） transmission system. This method is based on the time-varying Fourier coefficients series of the system variables, and focuses on the dynamics behavior of the Fourier coefficients. By truncating unimportant higher order series and keep only those significant series, this method can catch the dynamic behavior of the original detail model. The complexity of dynamic phasors model can be adjusted according to different application requirements. Therefore, it can significantly improve computational efficiency and maintain a good engineering precision when it is used for transient simulation. Followed by the time-domain converter station model for VSC-HVDC described by switch function, detailed analysis of the VSC-HVDC dynamic phasors model is presented. The VSC-HVDC model is simplified by keeping important system state variables corresponding to the time-varying Fourier series, which include the converter station switching function considering both the DC component and basic frequency component, and the DC transmission line considering only the DC component. Therefore, high frequency switching process is greatly simplified. The dynamic phasors model and a detailed time domain electromagnetic transient（EMT） model for the VSC-HVDC are simulated by the MATLAB software, and simulation results show that this method can ensure simulation accuracy and reduce computational cost.
**Key words:** power system; VSC-HVDC; dynamic phasors model; time-varying Fourier coefficients; switch function; electromagnetic transient model

基金项目：国家高技术研究发展中心973计划（2004CB217906）。
Project Supported by Major State Basic Research Development Program of China（973 Program）（2004CB217906）.

## 0 引言
随着电力电子技术的发展，大功率门极可关断晶闸管（GTO）和随后的绝缘双极晶体管（IGBT）等全控型器件的商业化应用，使得基于电压源型换流器（Voltage Sources Converter，VSC）的 HVDC 技术（即 VSC-HVDC）的应用成为可能。与传统 HVDC 相比，采用全控型器件的 VSC-HVDC 具有独特的优点，不仅可以同时独立控制有功和无功功率，还可以向无源网络供电，稳定交流母线电压等，在未来城市供电和新型能源发电（如风能发电、光伏发电和小水电等）并网中有着广阔的应用前景［2］。
在过去的近10年中，国内外已有学者对 VSC-HVDC 的建模和控制策略进行了比较深入的研究［1-4］。但是，在这些研究中，换流站的建模大多采用准稳态模型或过于复杂的模型，不适于大系统的分析。而随着 VSC-HVDC 的研究和应用的不断深入，对含有 VSC-HVDC 大规模电力系统分析方法的研究将成为新的热点。由于电力系统的庞大和复杂性以及计算规模和时间的限制，不可能对系统中所有开关器件都采用包含详细开关过程的电磁暂态仿真模型，而采用过于简化的模型又会导致缺乏准确性，动态相量（dynamic phasors）法就是在此需求下提出来的。
动态相量法的思想来源于传统的平均值法，是基于时变傅里叶系数推导出的一种建模方法，它可以在需要的精度上近似时域模型，又可以避免其非自治性，其概念首次在文献［5］中被引入。已经被成功用于同步感应电机［6］、STATCOM［7］、传统 HVDC［8,9］、可控串联补偿器（TCSC）［10-12］、统一潮流控制器（UPFC）［13-15］及电力系统次同步谐振［1］的建模和研究中。研究表明，将这种模型用于电力系统暂态仿真，可以大大提高计算效率又不失准确性。近几年来，我国科研人员也逐渐开展了有关研究［7-9］。
本文首次将动态相量法应用于 VSC-HVDC 输电系统的建模中。在建立了用开关函数描述的 VSC-HVDC 换流站详细时域模型的基础上，给出了 VSC-HVDC 动态相量模型的详细推导过程。该模型具有可扩展性，能依据不同开关控制策略推导相应的动态相量模型。最后，论文给出了所建立的模型在不同情况下的仿真验证结果。本文的工作是分析含有 VSC-HVDC 的大规模电力系统动态性的一项基础性工作，其成果可以直接用于这种系统的仿真研究。

## 1 动态相量法简介
动态相量法以时变 Fourier 变换为基础［8,16］，对于时域中以 $T$ 为周期的函数 $x(\tau)$，在任一区间 $\tau \in (t-T, t]$ 中，其时变 Fourier 级数可表示为
$$x(\tau) = \sum_{k=-\infty}^{\infty} X_k(t) e^{jk\omega\tau} \quad (1)$$
式中：$\omega = 2\pi/T$；$X_k(t)$ 为一系列时变 Fourier 系数，
在多相不平衡的系统中，也可以用动态相量法分相建模。本文主要针对三相平衡系统的建模，建模方法可推广到三相不平衡状态的分相建模。

## 2 VSC-HVDC 的动态相量法建模
动态相量卷积而得，即
$$\langle x_1 x_2 \rangle_k = \sum_{i=-\infty}^{\infty} \langle x_1 \rangle_{k-i} \langle x_2 \rangle_i \quad (5)$$
动态相量法基于频率分解的思想，希望仅保留时变 Fourier 级数中相对较大的系数来近似原始信号，以抓住系统的主要特征。将与所保留系数对应的相量作为系统变量，就可得到系统的动态相量模型，这种模型保留了原时域模型的非线性。动态相量法特别适合于含电力电子开关器件的设备建模，如 FACTS，HVDC 等，具有比传统的准稳态建模方法精确的优点。

1-滤波器；2-换流电抗；3-全控器件；4-直流电容；5-传输电缆
**图1 电压源型直流输电系统结构示意图**
**Fig. 1 Configuration of VSC-HVDC**