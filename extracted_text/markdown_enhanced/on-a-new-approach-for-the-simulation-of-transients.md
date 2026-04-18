## On a new approach for the simulation of transients in power systems
J. Mahseredjian a,∗, S. Dennetière b, L. Dubé c, B. Khodabakhchian d, L. Gérin-Lajoie e
a École Polytechnique de Montréal, Canada
b Électricité de France, Clamart, France
c DEI Technology, Montréal, Canada
d TransÉnergie Technologies, Hydro-Québec, Montréal, Canada
e Hydro-Québec, Montréal, Canada

Available online 10 October 2006

### Abstract
This paper presents a new simulation tool named EMTP-RV. EMTP-RV is a completely new program with a new graphical user interface and a new computational engine. The simulation uses a new matrix formulation for computing load-flow, steady state and time-domain solutions. Theoretical advantages are emphasized and demonstrated through practical examples. An open-architecture graphical user interface (GUI) is developed to maximize flexibility and allow creating and maintaining complex designs.

### Keywords
Simulation tools; Numerical methods; EMTP

## 1. Introduction
Since its initial concept presented in 1969 [1] the basic EMTP type simulation approach remained unchanged. It is used in various commercial (DCG-EMTP Version 3, EMTP-V3 [2]) and non-commercial packages. The main system of symmetric equations used in [1] is given by
$$Yv = i \quad (1)$$
This is referred to in the literature as the standard nodal analysis formulation. It assumes that all network components can be given an admittance matrix model. Matrix $Y$ is the admittance matrix, $v$ the vector of unknown voltages and $i$ is the vector of current sources combined with history current sources for the trapezoidal integration method. Since $v$ also includes known voltage sources, Eq. (1) is actually implemented taking only a submatrix $Y_n$ of $Y$ for finding $n$ unknown voltages. One of the important disadvantages of this formulation is the inability to incorporate ungrounded voltage sources. This has been corrected in [3] by using modified-nodal analysis, which incorporates an extra row for the voltage source equation and an extra column for the voltage source current which becomes listed in the vector of unknowns.

The assumption of admittance model existence for every component is a significant limitation. An ideal transformer model, for example, does not have admittance matrix formulation. This can be partially avoided by adding losses, but can then cause ill-conditioning problems. Other limitations are found in the representation of ideal switches. An ideal switch has pure zero resistance when closed and becomes infinity when opened. This is a fundamental principle in such a model to avoid superfluous natural frequencies and matrix conditioning problems. That is why system (1) is a variable rank system where closing a switch eliminates a matrix column and the corresponding row. The disadvantage of such manipulations is the computational effort, especially when the number of switches and switching frequency become high.

The EMTP-V3 code was written using the legacy Fortran-77 language and related methods. Such codes have significant limitations in automatic memory management, in code organization and interfacing with external programs. Modern computing languages and methods provide much more powerful and efficient environments for software development while providing crucial advantages in code evolution and maintenance.

Another major aspect in the simulation of transients is the graphical user interface (GUI). It constitutes the first and the main facet directly apparent to the user. It also represents a technological barrier into the design and simulation of more complex systems.

**Fig. 1.** EMTP-RV main architecture.

This is an augmented formulation which is keeping only the $Y_n$ part from Eq. (1). Although submatrices are identified due to their typical contents and for symbolic explanations given below, Eq. (2) can be viewed as a generic $Ax = b$ system. Matrix $A$ is not necessarily symmetric which provides another advantage over Eq. (1) for some device models.

For a voltage source connected between two nodes $k$ and $m$, the source equation is given by: $v_k - v_m = v_{b_{km}}$. It is directly inserted into the main system by placing a 1 and a $-1$ in columns $k$ and $m$, respectively, of $V_r$. The source voltage is $v_{b_{km}}$. The source current condition is accounted by transposition in the submatrix $V_c$. If the source is disconnected, then only its diagonal cell in $V_d$ is set to 1 and $v_{b_{km}} = 0$. A similar approach is used for entering other models. An ideal transformer with secondary nodes $k$–$m$, primary nodes $i$–$j$ and a transformation ratio $g$ is modeled with the equation: $v_k - v_m - g v_i + g v_j = 0$. This equation is again directly accommodated in the submatrix $D_r$ with the equivalent row transposition appearing in $D_c$.