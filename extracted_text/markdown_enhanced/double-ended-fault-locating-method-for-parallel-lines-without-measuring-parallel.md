# Double-Ended Fault-Locating Method for Parallel Lines Without Measuring Parallel Line Currents
**Kanchanrao G. Dase**, Senior Member, IEEE, and **Connor Doyle**

Received 22 November 2024; revised 7 April 2025 and 15 July 2025; accepted 29 August 2025. Date of publication 2 September 2025; date of current version 24 November 2025. Paper no. TPWRD-01761-2024. (Corresponding author: Connor Doyle.)
The authors are with the Schweitzer Engineering Laboratories, Inc., Pullman, WA 99163 USA (e-mail: kanchanrao_dase@selinc.com; connor_doyle@selinc.com).
Digital Object Identifier 10.1109/TPWRD.2025.3605244

## Abstract
This paper introduces a novel double-ended impedance-based fault-locating method for parallel lines, effectively addressing the challenges posed by mutual coupling. Instead of directly measuring the parallel line zero-sequence current, the proposed method estimates it using synchronized currents and voltages from the local end of the faulted line and remote zero-sequence current. The proposed approach addresses field constraints where numerical relays only have this information for fault locating. The proposed phasor-based fault-locating methodology, which uses filtered data, is applicable to various parallel line topologies and can handle any number of parallel lines. Depending on the parallel line configuration, the proposed algorithm may require zero-sequence source impedance values. In case the source impedance values known to the user are inaccurate, error mitigation techniques described in this paper can be applied. This paper demonstrates the accuracy of the proposed fault-locating method through fault simulations in various parallel line configurations modelled in electromagnetic transients program (EMTP) software.

**Index Terms**—Algorithms, communication channels, distance measurement, error correction, fault location, iterative methods, mutual coupling, power system faults, protective relaying, transmission lines.

## Nomenclature
| Symbol | Description |
|---|---|
| $I$ | Faulted phase loop current. |
| $I_{FC}$ | Fault current component polarizing quantity. |
| $I_G$ | Residual or ground current. |
| $I_{0F}$ | Total zero-sequence fault current. |
| $I_{0L}$ | Local zero-sequence current in the faulted line. |
| $I_{0P}$ | Parallel line zero-sequence current. |
| $I_{0R}$ | Remote zero-sequence current in the faulted line. |
| $k_0$ | Zero-sequence compensation factor. |
| $L_1$ | Line length of the faulted line. |
| $L_P$ | Line length of the parallel healthy line. |
| $m$ | Actual fault location (FL) from the relay terminal. |
| $m_I$ | Estimated FL using iterative approach. |
| $m_{Iavg}$ | Estimated FL using iterative approach with averaging. |
| $m_Q$ | Estimated FL using quadratic approach. |
| $m_{Qavg}$ | Estimated FL using quadratic approach with averaging. |
| $m_{SL}$ | Estimated FL using modified Takagi method meant for single line without zero-sequence mutual coupling. |
| $m_{PL}$ | Estimated FL using modified Takagi method for parallel lines with zero-sequence mutual coupling. |
| SIR | Source-to-line impedance ratio. |
| $V$ | Faulted phase loop voltage. |
| $Z_{1L}$ | Positive-sequence line impedance. |
| $Z_{0L}$ | Zero-sequence line impedance. |
| $Z_{0LP}$ | Zero-sequence impedance of parallel line. |
| $Z_{0M}$ | Zero-sequence mutual coupling impedance. |
| $Z_{0R}$ | Zero-sequence remote-source impedance of faulted line. |
| $Z_{0S}$ | Zero-sequence local-source impedance of faulted line. |
| $Z_{0RP}$ | Zero-sequence remote-source impedance of parallel line. |
| $Z_{0SP}$ | Zero-sequence local-source impedance of parallel line. |

## I. INTRODUCTION
Accuracy of fault-locating methods in power systems is essential for timely and successful restoration of the system. Using the modified Takagi fault-locating method for parallel lines and not accounting for the zero-sequence mutual coupling reduces FL accuracy [1], [2]. The greater the mutual coupling from the relay terminal to the FL, the more inaccurate the FL results become. The mutual coupling issue can be avoided through traveling-wave fault-locating methods or methods that utilize voltage and current measurements from both ends of the line [3], [4], [5], [6], [7], [8]. However, numerical relays that do not have access to remote terminal voltages, like the one described in [9] cannot implement such algorithms. In case users cannot deploy such solutions, they must rely on traditional methods that require zero-sequence current of the parallel line to compensate for the mutual coupling fault-locating errors. For such methods, zero-sequence current of the parallel line is either directly measured or estimated [10], [11], [12], [13], [14], [15].

More commonly, the zero-sequence current or phase currents are directly measured from the parallel line and are used to mitigate the mutual coupling effect [10], [11], [12], [13], [14]. However, this requires the local relay to have dedicated connections to accommodate parallel line currents. In case the local line is equipped with dual current transformers, or when the local line is in parallel with more than one power line, having connections to access currents from all the parallel lines is not always feasible. Sometimes the parallel line may not even originate from the same substation as the local line. This is where estimating the parallel line zero-sequence current can help avoid issues related to direct measurement, provided the estimations are accurate.

- Lines originating from a common bus but terminating on different buses