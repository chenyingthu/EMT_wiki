## MULTIPHASE POWER FLOW SOLUTIONS USING EMTP AND NEWTON'S METHOD

**J. J. Allemong, R. J. Bennon, P. W. Selent**  
*American Electric Power Service Corporation, Columbus, Ohio*

### ABSTRACT
This paper describes a reliable and very flexible multiphase load-flow solution process which is applicable for large transmission systems (up to 500 nodes). The process consists of an interface between the Electromagnetic Transients Program (EMTP) and a newly developed multiphase load flow algorithm that is based on the Newton-Raphson method. Subjects discussed include derivation of basic algorithm, structure of the Jacobian matrix, and convergence characteristics.

### INTRODUCTION
Well known and reliable methods exist today for solving AC single-phase power flow problems. Most of these are based on the Newton-Raphson method, which has become the method of choice. Single-phase load flows always assume balanced three-phase system operation, and are ideally suited for representing large transmission networks. Studies performed usually deal with long term area planning, bulk power transfers, or outages of a major component where the unbalance effects may not be especially significant or of concern. However, as the number of high-voltage untransposed transmission lines increases, the effects of unbalance become significant and need to be properly analyzed [1]. These effects lead to the malfunction of protective relaying and the presence of significant generator negative sequence currents.

Many of these unbalance studies, requiring three-phase analysis, have been performed at American Electric Power (AEP) over the past several years. They have been, and continue to be, conducted using the three-phase and phasor solutions of the existing Electromagnetic Transients Program (EMTP). Modeling limitations exist in this method and for further studies involving system operation under unbalanced reactor or open-pole conditions, the limitations will make this procedure quite difficult. Additional limitations include poor convergence and the inability to specify load flow constraints such as, specific bus voltage regulation, PQ output for single and three phase generators and loads, etc. These limitations have also been recognized outside of AEP, by the EMTP EPRI Development Coordination Group (EPRI DCG). Consequently a project was initiated in which AEP, as an Associate member of the EMTP EPRI DCG, would develop a full function three-phase load flow in EMTP.

A three phase load flow method was begun [9]. The intent of the present paper is to explore the viability of this method with respect to networks of practical size and complexity. The algorithm is based on Newton's method and addresses the previously noted limitations. The algorithm is capable of handling relatively large (practical) systems. A branch current method rather than a nodal method is used, resulting in greater flexibility for modeling loads and generators (e.g., delta connections). By integrating this into EMTP, full advantage is taken of EMTP's many network modeling capabilities (e.g., transmission lines and transformers). Integration into EMTP also provides an accurate steady state network admittance matrix that does not need to be created by the load flow algorithm. Additionally, this integration provides a direct and more accurate steady-state initialization of dynamic and transient simulations. The multiphase load flow method is scheduled to be made available as part of the EPRI DCG Version 3.0 EMTP.

### DERIVATION OF BASIC ALGORITHM
Modern single-phase load flow analysis uses real and reactive power mismatches to obtain a solution. Iterations are based on the relationship between power mismatches and voltage and angle mismatches. This relationship is established through the sparse Jacobian equation:

$$
\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \mathbf{J} \begin{bmatrix} \Delta \theta \\ \Delta V \end{bmatrix}
$$

Analysis in terms of polar coordinates lends itself well to problems formulated in terms of power mismatches, and three-phase load flows have been developed based on this formulation [9]. However, as will be seen, three-phase load flows require generalized models of generators and loads. It is convenient to express the equations for these models in terms of nodal currents instead of nodal powers. This formulation largely offsets the advantages of using polar coordinates.

The multiphase load flow algorithm described in this paper is based on Newton's method. Rectangular coordinates are used along with system constraints and component models based on branch quantities [3]. By using a branch representation, components can be connected in any fashion (delta-connected loads, phase-phase voltage sources, etc.), thus allowing a greater flexibility and more accurate system representation. The network components are not difficult to model using this representation, and consist of: three-phase synchronous machines, voltage sources, current sources, single-phase PQ loads, and three-phase static PQ loads. The reader is referred to [3] for a discussion of these components and their constraint equations.

### FORMULATION OF THE JACOBIAN MATRIX
The problem formulation consists of the expression of Kirchhoff's Current Law and a set of constraint equations for the various non-linear elements. The effects of the linear elements (branches and shunts) are contained in the $Y_{BUS}$ matrix while the non-linear elements contribute unknown currents. These currents are contained in a set of non-linear equations which define constraints that the solution is to satisfy. Equations 2-8 define the linear and non-linear equations.

| Component | Constraint | Controlling Quantity |
|---|---|---|
| PQ Machine | $P, Q$ (3-phase) | $E$ (internal voltage) |

*Table 1 - Constraints and Controlling Quantities*

The elements comprising the Jacobian matrix are found by taking partial derivatives of the constraint equations with respect to node voltages, currents, machine internal voltages, and the static load parameter $y$. Without any restructuring or reordering, the system of equations to be solved is: