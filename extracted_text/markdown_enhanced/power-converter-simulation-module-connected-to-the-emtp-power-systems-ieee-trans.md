# POWER CONVERTER SIMULATION MODULE CONNECTED TO THE EMTP

**Jean Mahseredjian**, **Serge Lefebvre**  
*Institut de Recherche d’Hydro-Quebec (IREQ)*  
1800 montee Ste-Julie, Varennes, Quebec, Canada J3X 1S1  

**Dinkar Mukhedkar**  
*Ecole Polytechnique de Montreal*  
P. O. Box 6079, Montreal, Quebec, Canada  

**ABSTRACT :** Presently the EMTP models converter valves as ideal switches in parallel with dampers designed to damp numerical oscillations introduced by the commutations. The converter network is modelled through branches with the appropriate TACS control circuits. It is assembled as any other EMTP network, without explicit topology recognition. A more efficient method, both in terms of solution and initialization, is based on a separately programmed module dedicated to power converter simulation and exploiting analytical knowledge. This paper presents the solution method used in such a module and its interface with the EMTP.

The steady increase of power converter simulation needs, within the widely used and validated EMTP, justifies research for better and more efficient models.
An alternate and more efficient approach to converter simulation is to create a separate and dedicated program module. The module described in this paper is simultaneously interfaced with the EMTP, and uses its own solution method, more appropriate to the nonlinear varying topology converter network representation. Analytical knowledge of the converter circuit operation is used to derive initial simulation conditions. The usual naturally commutated six-pulse bridge converter is the test circuit for the module design, but the formulation is general and simulation of other converter networks is not excluded.

**Keywords :** Digital simulation, EMTP, power converter

## 1. INTRODUCTION
The EMTP (Electromagnetic transients program) [1] is a nodal analysis program based on the fixed time-step trapezoidal integration method. Discretized network equations are given by $Y_n V_n = I_n$ where $Y_n$ is the nodal admittance matrix, $V_n$ is the node to ground voltage vector and $I_n$ represents node current injections including current sources for the integration history terms. The EMTP models power converter valves as ideal switches. Analog grid control schemes are simulated through the program’s TACS (Transient analysis of control systems) module. The complete converter network with control circuits is modelled through data cards and it is assembled as any other electrical network, without explicit recognition of the device. Initialization through a phasor solution cannot be achieved. To accommodate the time-varying topology created by the operation of the switches, the matrix $Y_n$ is rebuilt and re-triangularized completely whenever switch positions change. Partial re-triangularization confined to nodes connected to switches, is also possible, but it becomes less efficient for a large number of switches such as in a converter network. With the fixed integration time-step, landing on breakpoints created by converter topological changes, i.e. valve commutations, is not possible. Numerical oscillations, due to the trapezoidal integration method, following current discontinuities in inductive converter transformer branches, are alleviated by artificial damper circuits connected in parallel with converter valves.

## 2. THE CONVERTER MODULE
Figure 1 is a single line diagram showing the structure of the general converter module (CM) connected to the EMTP. The EMTP sees the converter as two sets of nonlinear elements, one set for the ac network and another set for the dc network, and it calculates a Thevenin equivalent behind each nonlinear element node. At each simulation time-point, the nonlinear element currents, found in the CM, are used to calculate the values of all EMTP network node voltages, by applying the post-compensation method [2] [3]. Figure 2 shows the EMTP network equivalents connected to the naturally commutated six-pulse converter. The ac network Thevenin resistances $R_s$ may be coupled. Any ac and dc networks can be assembled in the EMTP, but they are modelled as in Fig. 2 for the converter simulation.

The converter transformer is included in the CM network (Fig. 2). This choice eliminates ill-conditioning of the unloaded transformer nodal admittance matrix of the EMTP, and in addition permits simultaneous representation of saturation nonlinearities. The transformer is assembled from separate two-winding quadripoles, to admit modeling of any given transformer configuration. The configuration shown in Fig. 2 is for a grounded wye-wye transformer. Each quadripole is composed of an ideal two-winding transformer where each winding is in series with a leakage impedance (example: $R_{1a}$ and $L_{1a}$ for primary winding, phase a). A nonlinear current source $I_A = I_{Ab}$ is used to model saturation.

The CM has its own simulated digital control scheme [4]-[6], but is also capable of receiving separate control signals from TACS (simulated analog controls in the EMTP).

The CM can handle rectifying device (valve) characteristics ranging from ideal:
- an off-state device having negligible reverse leakage current and represented by an open circuit,
- an on-state device exhibiting negligible forward voltage drop and represented by an ideal short-circuit;
to general: the device is modelled as a nonlinear voltage-current function.

system state variables, $U$ is the vector of independent sources and $F$ is the vector of output variables. Subscript $k$ denotes network states: $k = 1, 2, \dots, k_{max}$. Two classes of solution methods can be found in the literature.
The first class is based on a varying topology approach.