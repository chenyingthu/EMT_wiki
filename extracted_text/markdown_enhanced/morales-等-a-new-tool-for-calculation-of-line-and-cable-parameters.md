## A New Tool for Calculation of Line and Cable Parameters
**J. Morales, H. Xue, J. Mahseredjian, I. Kocar**

**Abstract**−This paper presents a new tool for the computation of per-unit-length parameters for transmission line and cable models used for simulating electromagnetic transients (EMT). The proposed methodology is based on the MoM-SO theory and state-of-the-art formulations for the computation of the series impedance and shunt admittance parameters. The new tool has major advantages compared to traditional approaches available in EMT-type software. These advantages include accurate skin and proximity effect modeling, above-ground cable modeling, modeling of stranded wires in cables, representation of multilayer soil, coupled overhead lines and underground cables, etc. This paper presents the new tool together with demonstrations of transient simulations for practical examples.

**Keywords:** EMTP, line, cable, transients, per-unit-length.

## I. INTRODUCTION
Accurate transmission line models (including both overhead lines and underground cables) in EMT-type software require accounting for the distributed parameters nature and the frequency dependency of its parameters to properly represent transient phenomena. The computation of these models is usually a two-step process: 1) computation of per-unit-length (pul) parameters and 2) parametrization of the model. The parametrization depends on the targeted type of model. It is either for constant parameter or frequency dependent models. The frequency dependent modeling requires separate fitting procedures.

Since the pul parameters are the input data for the second step, the computation of these parameters is crucial for deriving accurate and reliable time-domain models. The pul parameters are denoted as
$$Z' = R' + j\omega L' \tag{1}$$
$$Y' = G' + j\omega C' \tag{2}$$
where $Z'$ denotes the pul series impedance and $Y'$ denotes the pul shunt admittance, with $R'$, $L'$, $G'$ and $C'$ being the pul resistance, inductance, conductance, and capacitance, respectively. Pul parameters describe the transmission line behavior through the well-known Telegrapher’s equations
$$\frac{\partial V}{\partial z} = -(R' + j\omega L')I = -Z'I \tag{3}$$
$$\frac{\partial I}{\partial z} = -(G' + j\omega C')V = -Y'V \tag{4}$$

The traditional Line Constants and Cable Constants routines [1]-[3] have been used for the computation of pul parameters for many years. These routines are included in most EMT-type software. Alternatively, pul parameters can be obtained via Finite Element Method (FEM) based techniques [4]-[6], which are considered more accurate, but usually demand a significantly higher computational burden. Therefore, the Line/Cable Constants routines are often preferred for their simplicity and efficiency.

The Line/Cable Constants tools, however, have limitations and have become out of date for today’s needs. For instance, they neglect proximity effects which can be relevant for cable simulations; they can handle only bare-aerial conductors (Line Constants) or only buried cables (Cable Constants), but mixed aerial and underground conductors cannot be modeled; they can only model two different mediums (air and ground), thus, they are not suitable for submarine cables, where the sea water representation is required in addition to ground and air mediums; also, above ground cables, such as required for gas-insulated substations or some above ground cable installations, may be poorly represented due to some simplifications in earth-return current formulas.

This paper presents a new tool named Line/Cable Data for the calculation of pul parameters that overcomes the limitations of the traditional Line/Cable Constants routines while performing a level of accuracy similar to FEM-based techniques. The proposed Line/Cable Data tool applies the MoM-SO theory [7]-[10] combined with state-of-the-art formulations [11], [12]. An early version of the new approach presented in this paper is reported in [13]. Since then, further developments and the complete integration into EMTP [14] have been achieved. A similar parameters calculation tool is proposed in [15], but only for tunnel installed cables.

One of the contributions of this paper is revisiting the techniques applied and explaining how they are reunited in the new Line/Cable Data package, which is important since until now the applied methods are spread in the literature. Another contribution is the demonstration of the capabilities of the new Line/Cable Data package through transient simulations with

J. Morales is with PGSTech, Montréal (Québec) H2K 1C3, Canada (e-mail: jesus.morales@emtp.com).
H. Xue and Jean Mahseredjian are with Polytechnique Montreal, Montréal (Québec) H3C 3A7, Canada (e-mail: haoyan.xue@polymtl.ca, jean.mahseredjian@polymtl.ca).