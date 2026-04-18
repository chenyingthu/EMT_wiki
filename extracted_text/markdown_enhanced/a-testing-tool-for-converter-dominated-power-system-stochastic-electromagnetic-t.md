# A Testing Tool for Converter-Dominated Power System: Stochastic Electromagnetic Transient Simulation
Pengwei Chen, Member, IEEE, Liang Lu, Xinbo Ruan, Fellow, IEEE, and Nian Liu, Member, IEEE

**Abstract—** To investigate the impact of uncertain variability and provide a rigorous testing environment for converter-dominated power systems, this article develops a testing tool called stochastic electromagnetic transient simulation. The tool is derived from the stochastic differential equation (SDE) representing the stochastic process of parameter migration. By inheriting the principle of companion circuit, the dynamic companion circuits of the lumped elements with parameter migration are further established. Combined with the analysis of the numerical stability in discrete simulation as well as the stability of the continuous system with parameter migration, a numerical algorithm that is compatible with the electromagnetic transients program (EMTP) framework is designed, as well as a C program package. The verification results on a grid-connected three-phase two-level rectifier and a two-terminal dc distribution system demonstrate that the developed tool can simulate the parameter migrations and the stimulated system dynamic process simultaneously, which can also be used to efficiently reflect the real performance of various control subsystems and their coordination in extreme cases.

**Index Terms—** Converter-dominated power system, electromagnetic transient (EMT) simulation, numerical algorithm, stochastic differential equation (SDE), stochastic dynamic.

### NOMENCLATURE
| Symbol | Description |
|---|---|
| $W(t)$ | Wiener process, and $W(t) - W(0)$ satisfies the normal distribution $N(0, t)$. |
| $\xi$ | White noise and $\xi = dW(t)/dt$. |
| $\alpha(\cdot)$ | Drift process of the stochastic perturbation. |
| $\beta(\cdot)$ | Diffusion process of the stochastic perturbation. |
| $R(t)$ | Resistance of an element with parameter migration at time $t$. |
| $L(t)$ | Inductance of an element with parameter migration at time $t$. |
| $\psi_L(t)$ | Magnetic flux through inductance at time $t$. |
| $C(t)$ | Capacitance of an element with parameter migration at time $t$. |
| $Q_C(t)$ | Energy stored in capacitance at time $t$. |
| $\Delta t$ | Discretization time step in a simulation. |
| $\tau_n$ | $\tau_n = n\Delta t$. |
| $R_n$ | Numerical approximation to $R(\tau_n)$ in stochastic electromagnetic transient simulation. |
| $L_n$ | Numerical approximation to $L(\tau_n)$ in stochastic electromagnetic transient simulation. |
| $C_n$ | Numerical approximation to $C(\tau_n)$ in stochastic electromagnetic transient simulation. |
| $v_{i,n}, v_{j,n}$ | Voltages of two terminal nodes $i$ and $j$ in numerical simulation at time $\tau_n$. |
| $i_{R,n}$ | Current through resistance in numerical simulation at time $\tau_n$. |
| $i_{L,n}$ | Current through inductance in numerical simulation at time $\tau_n$. |
| $i_{C,n}$ | Current injected into capacitance in numerical simulation at time $\tau_n$. |
| $W_n$ | Sampling value of $W(t)$ at time $\tau_n = n\Delta t$. |
| $G_E, G_T$ | Nodal admittance matrices used in stochastic electromagnetic transient simulation. |

Besides, the subscripts $R$, $L$, and $C$ are used for resistance, inductance, and capacitance, respectively, while the superscript $^*$ is used for the controller reference values or the exact value of simulation, and other symbols are defined as required.

Manuscript received 4 October 2021; revised 3 December 2021 and 7 January 2022; accepted 22 January 2022. Date of publication 25 January 2022; date of current version 3 October 2022. This work was supported in part by the National Natural Science Foundation of China under Grant 52007080, in part by the China Postdoctoral Science Foundation under Grant 2020TQ0142 and Grant 2020M681583, and in part by the Opening Foundation of State Key Laboratory of Alternate Electrical Power System with Renewable Energy Sources under Grant LAPS21008. Recommended for publication by Associate Editor Firuz Zare. (Corresponding author: Pengwei Chen.)

Pengwei Chen, Liang Lu, and Xinbo Ruan are with the Jiangsu Key Laboratory of New Energy Generation and Power Conversion, College of Automation Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing 210016, China (e-mail: chenpw2019@nuaa.edu.cn; sx2003088@nuaa.edu.cn; ruanxb@nuaa.edu.cn).

Nian Liu is with the State Key Laboratory for Alternate Electrical Power System with Renewable Energy Sources, North China Electric Power University, Beijing 102206, China (e-mail: nianliu@ncepu.edu.cn).

Color versions of one or more figures in this article are available at https://doi.org/10.1109/JESTPE.2022.3146231.

## I. INTRODUCTION
Driven by the rapid development of power electronics and control technologies in the past decades, converter-dominated power systems are becoming important components of electrical grids to facilitate the integration of renewable energy sources and the power supply of high quality, such as renewable power plants [1], microgrids [2], dc distribution systems [3], and high-voltage dc transmission systems [4]. Although these convert