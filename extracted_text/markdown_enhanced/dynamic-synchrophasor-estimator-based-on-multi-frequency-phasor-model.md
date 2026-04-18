## 基于多频率相量模型的动态同步相量测量算法
白莎，符玲*，熊思宇，麦瑞坤
(西南交通大学电气工程学院，四川省 成都市 610031)

## Dynamic Synchrophasor Estimator Based on Multi-frequency Phasor Model
BAI Sha, FU Ling*, XIONG Siyu, MAI Ruikun
(College of Electrical Engineering, Southwest Jiaotong University, Chengdu 610031, Sichuan Province, China)

**ABSTRACT:** When the power system was suffered from unbalance and fault, the fundamental frequency would deviate from the nominal frequency, and the measurement accuracy of synchrophasor estimator also would rapidly reduce. Therefore, a dynamic synchrophasor estimator was proposed based on multi-frequency phasor model. The multi-frequency phasor model was employed to reflect the effective information around real frequency, and to establish a phasor model including multi-frequency phasor. The accuracy phasor value could be obtained by estimating rough frequency, looking the matrix table calculated offline, revising the discrete Fourier transform (DFT) value and shifting phasor. Test results of both simulated signals and PSCAD/EMTDC generated signal show that the proposed estimator can provide accurate phasor estimations under dynamic conditions of frequency ramping and power oscillation at the cost of limited increase of computational burden.

**KEY WORDS:** frequency deviation; synchrophasor estimator; multi-frequency phasor model; discrete Fourier transform (DFT); PSCAD/EMTDC simulation

**摘要：**电力系统中由于发电出力与负载不平衡导致基波频率偏移，进而造成同步相量测量精度迅速下降。基于此，该文提出基于多频率相量模型的动态同步相量测量算法。首先，算法利用多个不同旋转频率的子相量来描述真实频率附近的有效信息，并以此对动态相量进行建模；其次，通过计算粗估频率、调用离线矩阵、修正离散傅里叶变换结果及相移运算等步骤来获得精确的相量测量值。最后，仿真结果表明，算法虽然增加了有限的运算量，但在频率斜坡变化、功率振荡等动态工况中，能够减小频率偏移带来的不利影响，提供准确的测量结果。

**关键词：**频率偏移；同步相量测量；多频率相量模型；离散傅里叶变换；PSCAD/EMTDC 仿真

基金项目：国家杰出青年科学基金项目(51525702)；国家自然科学基金面上项目(51777173)；国家自然科学青年基金项目(51407150)。
The National Science Fund for Distinguished Young Scholars (51525702); The General Programs of the National Natural Science Foundation of China (51777173); National Natural Science Foundation of China (51407150).

## 0 引言
作为广域测量系统的基础和核心，同步相量测量单元(phasor measurement unit，PMU)被广泛安装以获得电网全局动态变化特性[1-4]，其算法的精确性将直接影响到广域测量系统的高级应用性能[5-8]。同时随着电网规模的不断扩大，电力系统中负荷波动、电力故障等都可能引起基波频率大范围偏移和电压、电流幅值振荡，造成同步相量测量算法出现非同步采样，测量精度下降[9-11]。

上述问题使得响应速度快、计算简便的离散傅里叶变换(discrete Fourier transform，DFT)算法，在信号测量时受到很大限制，因此有学者提出泰勒级数法[12-15]和插值法[16-18]来改善 DFT 的测量结果。泰勒级数法在动态工况下有较好的性能体现，文献[12]提出基于泰勒模型的动态相量测量算法，详尽地讨论了泰勒阶数取值对算法的影响，并在低频振荡仿真中取得良好的测量结果；文献[13-14]在泰勒模型的参数求解上分别利用时域和时频信息对信号进行处理，利用离线矩阵对 DFT 结果进行修正，减少了相应的运算量，在抗噪和响应时间等方面也取得不错的效果；为了更进一步地优化算法性能，文献[15]综合考虑泰勒模型在时域、频域的数据信息通过自适应切换，其切换条件是通过计算相量估计值，反推各采样点的理论值，并与实测值进行比较，该自适应算法兼顾时域噪声和频域精度，综合性能表现优良。但这类泰勒算法没有考虑信号频率大范围偏移带来的影响，因此应用存在一定局限。插值法则利用 DFT 后的谱线信息获得高精度的测量结果，文献[16]采用多点插值法，详细地推导了不同插值点数下的多项式，利用多项式校正 DFT 的测量结果，其测量结果精度高，在噪声工况中仍有较好的性能表现；文献[17]同样是基于 DFT 插值的同步相量测量算法，更进一步地研究了不同基波周期长度、数据窗对算法的性能影响；文献[18]则预先对信号的频率进行插值，获得较为准确的频率结果后，将其代入泰勒模型中，扩大了泰勒模型应用范围。虽然插值法在精度方面有一定优势，但算法需要性能优良的窗函数和较多的采样点数配合，因此增加了运算负担。为了拓宽泰勒级数法的应用面，同时优化插值法的运算量，文献[19]建立动态相量建模的虚指数基函数模型，将干扰信号模型加入优化目标实现对特定波形的陷波，能够有效抑制衰减直流分量或间谐波，但当基波频率出现较大偏移时，算法对基波频率的动态跟踪缺乏灵活性。

频率为 $\hat{\omega}_0 + m\Delta\omega = 2\pi(\hat{f}_0 + m\Delta f) / f_s$。

## 2 模型参数的求解
如图 1 所示，假设单个周波内的采样点数为 $N$，以等效窗的几何中心位置 $l_{\text{mid\_p}}$ 为参考点，所加数据窗为 $h(n)$，经傅里叶变换可得相量 $\hat{X}(l_{\text{mid\_p}})$：
$$
\hat{X}(l_{\text{mid\_p}}) = \sum_{n=-\frac{N-1}{2}}^{\frac{N-1}{2}} x(n + l_{\text{mid\_p}})h(n)e^{-j\omega_0 (n + l_{\text{mid\_p}})} = \sum_{n=-\frac{N-1}{2}}^{\frac{N-1}{2}} h(n) \sum_{m=-M}^{M} A_m e^{j(\hat{\omega}_0 + m\Delta\omega - \omega_0)(n + l_{\text{mid\_p}})} + \sum_{n=-\frac{N-1}{2}}^{\frac{N-1}{2}} h(n) \cdot \sum_{m=-M}^{M} A_m^* e^{-j(\hat{\omega}_0 + m\Delta\omega + \omega_0)(n + l_{\text{mid\_p}})} = CA + DA^* \quad (4)
$$
式中：DFT 滤波频率 $\omega_0 = 2\pi f_0 / f_s$，其中 $f_0$ 为基波