# A Numerically Efficient and Accurate Model for Real-Time Simulation of Solid-State Transformer Using Implicit-Explicit Integration Methods

Hengyu Li, Member, IEEE, Walid Hatahet, Graduate Student Member, IEEE, Jared J. Paull, Graduate Student Member, IEEE, Fei Zhang, Member, IEEE, Yuanshi Zhang, Member, IEEE, Liwei Wang, Senior Member, IEEE, and Wei Li, Member, IEEE

Hengyu Li, Walid Hatahet, Jared J. Paull, and Liwei Wang are with the School of Engineering, The University of British Columbia Okanagan, Kelowna, BC V1V 1V7, Canada (e-mail: liwei.wang@ubc.ca).
Fei Zhang and Yuanshi Zhang are with the School of Electrical Engineering, Southeast University, Nanjing 210096, China.
Wei Li is with OPAL-RT Technologies, Montreal, QC H3K 1G6, Canada (e-mail: wei.li@opal-rt.com).

**Abstract**—Electromagnetic transient (EMT) models of power electronic converters are essential for converter design, control, and fault analysis. This article proposes a switching-function-based detailed equivalent model (SFB-DEM) using combined implicit and explicit (ImEx) multistep Gear’s integration methods for numerically efficient and accurate EMT simulation. The proposed SFB-DEM integrates the benefits of ImEx solvers, featuring converter circuit decoupling, node number reduction, and constant nodal-network conductance ($G$)-matrix in the EMT model. The SFB-DEMs employing the ImEx 2nd and 3rd order Gear’s (i.e., ImEx-G2O and ImEx-G3O) methods are implemented for solid-state transformer (SST) simulation. In addition, a switching interpolation technique is proposed and integrated with the ImEx-G2O and ImEx-G3O solvers to account for intra-time-step switching events. The proposed SST SFB-DEMs greatly accelerate the EMT simulation, compared to the conventional detailed model (DM) and variable conductance ($G$)-matrix DEM (VG-DEM). For the SST with 60 SMs, the proposed SFB-DEM with ImEx-G3O method achieves the EMT simulation speedup by 171 and 7.5 folds, compared to the DM and VG-DEM, respectively.

**Index Terms**—Constant $G$-matrix, electromagnetic transient (EMT) program, implicit-explicit backward differentiation formula, solid-state transformer (SST), switching interpolation technique, switching-function-based detailed equivalent model (SFB-DEM).

## Nomenclature
| Term | Definition |
|---|---|
| SFB-DEM | Switching-function-based detailed equivalent model. |
| VG-DEM | Variable $G$-matrix detailed equivalent model. |
| A-stability | Absolute stability. |
| L-stability | Strong form of A-stability with limit of $\lim_{z \to -\infty} R(z) = 0$. |
| BDF | Backward differentiation formula. |
| TBE | Trapezoidal rule switching to Backward Euler. |
| ImEx-G2O | Implicit-explicit Gear’s 2nd order method. |
| ImEx-G3O | Implicit-explicit Gear’s 3rd order method. |
| ISOP | Input-series-output-parallel. |
| MFT | Medium-frequency transformer. |

## I. Introduction
The development of solid-state transformer (SST) (also known as a power electronic transformer) has attracted much attention from industry and academia [1], [2], [3], [4], [5]. The SST circuit topologies are commonly categorized into four types, i.e., single-stage, two-stage with low voltage dc (LVdc) link, two-stage with medium voltage dc (MVdc), and three-stage topologies [3], [4], [5], as presented in Fig. 1. An ISOP configuration is typically employed for the SST, realizing medium voltage ac (MVac) to LVdc conversion [2]. A three-phase SST following ISOP configuration often uses multilevel ac–dc converter as its Stage I, composed of ac chain-links with cascaded full-bridge submodules (FBSMs). Meanwhile, multiple dual-active-bridge (DAB) dc–dc converters are coupled with the cascaded FBSMs through MVdc capacitors as its Stage II. The DAB dc–dc converters play an important role to provide galvanic isolation between the MVdc and LVdc through MFTs, enabling bidirectional power flow and achieves high power density [6], [7].

However, the detailed model (DM) of the SST imposes tremendous computational burdens to electromagnetic transient (EMT) simulation due to its detailed representation of massive semiconductor switches and discrete circuit components. In order to enhance the numerical accuracy and simulation efficiency of the SST, various equivalent circuit modeling approaches were introduced in the prior art. A high-speed EMT modeling strategy of the SST was proposed in [8] and [9], which uses Norton equivalents to simplify the SST circuit into a two-port system for node number reduction. However, the SST system is decoupled through the ac voltages of the MFTs, which may lead to numerical inaccuracy for fast switching state changes of the FBSMs in DABs. An alternative circuit decoupling through a solver, especially designed for stiff ODEs [18]. While Gear’s 2nd order metho