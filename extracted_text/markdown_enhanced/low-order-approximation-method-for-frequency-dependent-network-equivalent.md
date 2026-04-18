## 频变输电线路模型中的低阶拟合方法
刘俊 1，郭瑾程 2，魏占宏 1，方万良 1，侯俊贤 3，项祖涛 3
（1．电力设备电气绝缘国家重点实验室(西安交通大学)，陕西省 西安市 710049；2．国网陕西省电力公司经济技术研究院，陕西省 西安市 710065；3．中国电力科学研究院，北京市 海淀区 100192）

Low-Order Approximation Method for Frequency-Dependent Transmission Line Model
LIU Jun1, GUO Jincheng2, WEI Zhanhong1, FANG Wanliang1, HOU Junxian3, XIANG Zutao3
(1. State Key Laboratory of Electrical Insulation and Power Equipment(Xi’an Jiaotong University), Xi’an 710049, Shaanxi Province, China; 2. State Grid Shaanxi Electric Power Company Economic Research Institute, Xi’an 710065, Shaanxi Province, China; 3. China Electric Power Research Institute, Haidian District, Beijing 100192, China)

**ABSTRACT:** Rational function approximations of characteristic impedance and propagation coefficient are crucial in modeling of frequency-dependent transmission line. Traditional Bode asymptotic method produces lots of pole-zeros. Some of them have no contribution to fitting accuracy and cause unnecessary calculation in electromagnetic transient simulation. To avoid appearance of redundant pole-zeros, a low-order approximation method of frequency-dependent transmission line model is proposed. Firstly, low-order pole-zeros are located for characteristic impedance and propagation coefficient. Then approximation accuracy is improved with nonlinear least square method. Thus low-order rational function approximations of characteristic impedance and propagation coefficient are achieved consequently. Case studies show that compared to Bode asymptotic method, fitting with low-order approximation method is more accurate and rational function order is reduced, therefore electromagnetic transient simulation is accelerated.

**KEY WORDS:** transmission line; frequency-dependent parameter; electromagnetic transient; rational function approximation

**摘要：** 对特征阻抗和传播系数的有理函数拟合是考虑参数频变的输电线路建模中的关键步骤。传统的模域输电线路模型采用的 Bode 渐近线拟合法会产生大量零极点，其中一部分对提高模型精度没有作用并会导致电磁暂态仿真中产生不必要的计算。为避免冗余零极点的产生，提出了一种应用于频变输电线路模型中的低阶有理函数拟合方法。首先对线路特征阻抗和传播系数进行低阶零极点定位，然后用非线性最小二乘法提高拟合精度，从而实现对特征阻抗和传播系数的低阶有理函数拟合。对比 Bode 渐近线法的拟合结果，低阶拟合方法能够在保证拟合精度的同时降低拟合函数的阶数，从而提高电磁暂态计算效率。
**关键词：** 输电线路；频变参数；电磁暂态；有理函数拟合

**DOI：** 10.13335/j.1000-3673.pst.2016.1860

基金项目：国家自然科学基金项目(51507126)；国家电网公司基础性前瞻项目“大规模交直流电力系统全电磁暂态仿真理论方法研究”。
Project Supported by National Natural Science Foundation of China (51507126); Project Supported by Basic Prospective Project of State Grid Corporation of China "Research of All-Electromagnetic Transient Simulation Theories and Methods for Large-Scale AC/DC Power Systems".

## 0 引言
随着灵活交流输电技术、高压直流输电技术为代表的先进电力电子技术的广泛应用[1-3]，我国电网将发展成为超大规模的超、特高压交直流混联的复杂电网[4-6]。电力系统的发展对电力系统仿真技术提出了新的挑战。考虑网络中所有元件电磁暂态过程的系统级全电磁暂态仿真，理论上将更接近系统的实际运行情况。
输电线路作为系统中的一个重要元件，对其建立合理的数学模型在电磁暂态仿真中十分关键。由于输电线路是典型的分布参数元件[7]，并且由于集肤效应线路参数成为频率的函数，因此描述输电线路上电压电流动态过程的方程是与频率有关的微分方程。在潮流计算和机电暂态计算的准稳态假设下，一般使用以“π 型等值电路”为代表的集中参数线路稳态模型[8]。然而，这类模型是在正弦稳态下推导得出的，因此理论上并不适用于电磁暂态计算。有的文献中对线路采用级联模型来模拟线路的分布特性[9-14]，但是级联模型将增加系统的节点数，并且易引发系统的虚假数值振荡[15]。Bergeron 使用行波法建立了无损输电线路的常参数模型[16]，Dommel 在其基础上进一步考虑电阻的影响，将线路电阻集中起来接入线路[17]。这 2 种模型都属于常参数输电线路模型，计算经验表明常参数输电线路模型会造成高次谐波的放大从而使波形产生畸变[18]。频变输电线路模型由于考虑了输电线路参数的频变特性，其理论比常参数输电线路模型更加严密[18-22]。这类模型根据是否使用相模变换矩阵分为相域模型和模域模型 2 大类，其代表分别是 Noda 模型和 J. R. Marti 模型。
频变输电线路模型需要对线路参数进行有理函数拟合。本文以模域频变输电线路模型为基础，研究了传统模型中的 Bode 渐近线法造成冗余零极点的问题，并通过低阶零极点初始定位和最小二乘方法改进了对特征阻抗和传播系数的有理函数拟合方法，在保证拟合精度的同时降低拟合阶数。最后通过算例仿真验证该方法的正确性及其在提高电磁暂态计算效率方面的有效性。

## 1 频变输电线路模型
频变输电线路的数学模型建立在求解电报方程的基础上[18]，不难得到单相输电线路两端的电压、电流在频域的关系式如下：
$$[U_m(\omega) + I_m(\omega) Z_C(\omega)] A(\omega) = U_k(\omega) - I_k(\omega) Z_C(\omega) \tag{1}$$
$$[U_k(\omega) + I_k(\omega) Z_C(\omega)] A(\omega) = U_m(\omega) - I_m(\omega) Z_C(\omega) \tag{2}$$
式中：$k$、$m$ 分别代表线路的首端和末端；$Z_C(\omega)$ 表示线路的特征阻抗；$A(\omega)$ 表示长度为 $l$ 时的线路传播系数。其中 $\omega=2\pi f$，$f$ 为频率。由于本文主要讨论输电线路的频域模型，因此下文如无特殊说明，为

理可描述如下。
**定理 1 (递归卷积)** 若 $f(t)$ 在 $t \le 0$ 的值已知，$g(t)=e^{-\alpha(t-T)}\varepsilon(t-T)$，其中 $\alpha$、$\varepsilon$、$T$ 是常数，则卷积 $s(t)=f(t)*g(t)$ 可由历史值计算得到，即
$$s(t) = m s(t - \Delta t) + p f(t - T) + q f(t - \Delta t - T) \tag{5}$$
式中 $m$、$p$、$q$ 均为常数。
在建立时域线路两端电压、电流关系的基础上，得到单相输电线路等值电路如图 1 所示。频变输电线路模型具有和常参数输电线路模型同样的拓扑结构：线路两端解耦，每端各由一个等效电阻和一个历史电流源并联而成，而且单相频变输电线路模型可通过相模变换推广至多相输电线路。

图 1 单相输电线路等值电路
Fig. 1 Equivalent circuit of single phase line model

## 2 有理函数拟合问题
### 2.1 有理函数拟合概述
在频变输电线路模型中，为应用递归卷积定理，需将特征阻抗和传播系数拟合为有理函数的形式，即
$$F(s) = H \frac{(s - z_1)(s - z_2)\cdots(s - z_m)}{(s - p_1)(s - p_2)\cdots(s - p_n)} \tag{6}$$
式中：$z_i$ 表示拟合的零点；$p_i$ 表示拟合的极点；$H$ 为常数。对于特征阻抗：$n=m$；对于传播系数：