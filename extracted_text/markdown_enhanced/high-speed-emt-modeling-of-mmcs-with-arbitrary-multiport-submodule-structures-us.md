## High-Speed EMT Modeling of MMCs With Arbitrary Multiport Submodule Structures Using Generalized Norton Equivalents
Jianzhong Xu, Member, IEEE, Shengtao Fan, Member, IEEE, Chengyong Zhao, Senior Member, IEEE, and Aniruddha M. Gole, Fellow, IEEE

**Abstract**—In order to improve features, such as fault current blocking and capacitor voltage balancing, modular multilevel converter (MMC) topologies incorporating multiport submodules (SMs) are being considered as candidates for HVdc transmission applications. This paper presents high-speed and accurate electromagnetic transient (EMT) models for MMCs composed of such multiport SMs. The approach uses the Schur’s complement technique to recursively eliminate internal nodes of the converter structure to create a multiport Norton equivalent that connects to the external network. Thus, the final admittance matrix seen by the EMT solver has a dimension orders of magnitude smaller than that of the unreduced structure. As with previously developed approaches for MMCs with single-port SMs, all internal information, such as individual SM capacitor voltages, is preserved and can be output by the program if needed. This increases the bookkeeping effort, but the overall reduction in matrix size more than compensates for any resulting time penalty. Approximately two to three orders of magnitude speedup over a straightforward implementation in an EMT program is achieved.

**Index Terms**—Modular multilevel converter (MMC), Schur’s complement, electromagnetic transient (EMT), multi-port submodules (SMs), high speed modeling, generalized Norton equivalent.

Manuscript received April 25, 2017; revised June 23, 2017; accepted August 12, 2017. Date of publication August 17, 2017; date of current version April 6, 2018. This work was supported by the National Key Research and Development Plan of China under Grant 2016YFB0900903. Paper no. TPWRD-00583-2017. (Corresponding author: Jianzhong Xu.)

J. Xu is with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing 102206, China, and also with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada (e-mail: Jianzhong.xu@umanitoba.ca).

S. Fan and A. M. Gole are with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 2N2, Canada (e-mail: shengtaofan@gmail.com; aniruddha.gole@umanitoba.ca).

C. Zhao is with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing 102206, China (e-mail: chengyongzhao@ncepu.edu.cn).

## I. INTRODUCTION
The modular multilevel converter (MMC) has become a highly desired topology for point-to-point high voltage direct current (HVdc) transmission as well as for construction of large scale dc grids [1], [2]. A traditional single-port MMC topology shown in Fig. 1 includes three phase legs each with upper and lower arms. Within each arm, there are numerous (up to several hundred) series connected single-port sub-modules (SMs). These can be half-bridge SMs (HBSM), full-bridge SMs (FBSMs), or a combination of both types [3]. The fully detailed electromagnetic transient (EMT) simulation of MMCs on EMT programs is a challenge, due to their extremely large SM count in each arm and high number of nodes in the topology [4], [5].

Reference [6] proposed the Nested Fast and Simultaneous Solutions for the power electric networks, indicating that the network can be partitioned into nested subsystems; thus reducing the computational burden of the circuit without losing any information. The approach is similar to the diakoptics approach of Kron and others [7]–[9]. Reference [10] introduced the nested theory to EMT modeling of MMCs, where each of the six arms of the MMC is reduced to a single two-node Thévenin-equivalent. This admittance matrix of this reduced system is overlaid on the admittance matrix of the remainder of the ac and dc side networks in the EMT solver. As none of the hundreds of internal nodes appear in the overlaid matrix, the admittance matrix in the EMT solver remains at a manageable size for further LU (or other) factorization when the semiconductor switches in the sub-module operate. This leads to a significant improvement in the simulation time.

**Fig. 1.** Schematic diagram of single-port three-phase MMC.

It must be realized that in these more traditional full- or half-bridge topologies as in Fig. 1, each SM is a single-port with only two terminals. Hence all SMs in an arm carry the same current [10] and this makes the procedure for obtaining a single Thévenin equivalent for the arm very straightforward.

**Fig. 2.** (a) Two-port SM and (b) its companion circuit.

After its initial introduction, several researchers have ex-

**Fig. 3.** The two-port MMC structure.

and the conventional arises from its ability to simplify voltage balancing. At any given instance, the MMC uses a certain number of sub-modules in series to provide the ordered voltage at its output. The remaining sub-modules are bypassed. Because of the availability of its second port, these idle sub-modules can then be connected with neighboring active modules so that the capacitors are paralleled and automatically become equal in