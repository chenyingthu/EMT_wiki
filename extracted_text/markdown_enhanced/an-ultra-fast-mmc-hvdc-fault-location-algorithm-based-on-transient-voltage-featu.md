# An ultra-fast MMC-HVDC fault location algorithm based on transient voltage features and regression neural network

**Yunqi Zhang** *, **Yue Yu**, **Guosheng Yang**  
State Key Laboratory for Security and Energy Saving, China Electric Power Research Institute, Beijing, China

**Keywords:** Fault location, MMC-HVDC, Transient voltage response, Extraction of characteristic variables, Regression neural network

**Abstract:** An ultra-fast fault location algorithm based on the single-ended transient voltage features and regression neural network (RNN) is proposed, which utilizes $2.5$ ms postfault data window and is suitable for modular multilevel converter-based high-voltage DC (MMC-HVDC) grids equipped with quick-action protections and hybrid DC circuit breakers (HDCCBs). Firstly, the analyses based on the lumped RLC equivalent circuit demonstrate that the delay time, the first negative peak time and its value all have exact relationships with the fault location. Nevertheless, considering the actual parameters and topology of the MMC-HVDC grid, three features can only be approximately extracted. Thus, RNN is utilized to estimate fault locations. $2.02 \times 10^4$ distinct fault cases validate the algorithm’s high accuracy across all fault locations and transition resistances up to $1005~\Omega$. It can well tolerate reasonable deviations of line parameter and current limiting reactor value, as well as $40$-dB white noise. Besides, it also has remarkable adaptability, and can be suitable for different systems.

## 1. Introduction

The modular multilevel converter-based high-voltage DC (MMC-HVDC) grids are usually equipped with quick-action protections and hybrid DC circuit breakers (HDCCBs) to isolate fault areas within few millionseconds. So after faults, only a quite short data window can be acquired before HDCCBs opening, which increases the difficulty of accurate fault location in MMC-HVDC grids.

Several exemplary traveling-wave-based fault location methods have been presented. Although the postfault data windows required by them are generally compatible with MMC-HVDC grids, they still have several drawbacks. The methods presented in [1–3] are all based on the fault-generated surge arrival times of the traveling waves at double terminals. The authors in [4] present a fault location scheme for HVDC cable transmission based on the time difference between modal initial peaks. However, these methods require quite high sampling frequencies up to several MHz. The fault location methods proposed in [5,6] both need synchronized currents obtained by sensors distributed along the DC lines. In fact, the accuracy of the traveling-wave-based fault location methods highly relies on the precise traveling wave propagation velocity (TWPV) through the faulted line and the accurate moment when the initial traveling wave reaches the fault locator. The TWPV depends on the propagation medium, so it is also frequency-dependent. When the fault occurs at different locations, the frequency band of the initial traveling wave distributes differently, and the TWPV is also different. Therefore, it is difficult to accurately obtain the TWPVs under different fault conditions. Besides, the initial traveling waves will have severe dispersion in the case of high-resistance faults or remote faults, so the moments they reach the fault locators are also difficult to capture accurately. By increasing the sampling frequency to several MHz or adding more measurement points along the lines, the above problems can be mitigated to some extent but cannot be eliminated. In reference [6], on an attempt to reduce the potential fault location errors resulting from low sampling frequency, while maintaining the cost to minimum, a machine learning approach is also introduced. Moreover, the accuracy of these methods depends on the strictly synchronous signals from double-ended or line-distributed sensors. Therefore, these methods have higher requirements on communication and measurement equipment. The required synchronous measurement points distributed along the line inflict more difficulties and costs in the practical implementation.

An electromagnetic time reversal (EMTR) fault location method is presented in [7] based on the lossy back-propagation model. The authors in [8] present a data-driven fault location algorithm based on EMTR voltage energy in mismatched media. However, a fairly long postfault data window is used for them, which is not applicable to MMC-HVDC grids that use HDCCBs to quickly isolate DC faults.

Reference [9] presents a fault location scheme for MMC-HVDC grids that uses an estimated $R$-$L$ representation of the transmission lines. In [10], a fault location method based on dynamic state estimation and gradient descent is presented. However, frequency-independent lumped

```
Ldc                      x
DCTransmission line
SM1         SM1     SM1
SM2         SM2     SM2
Voltage
SMn         SMn
```