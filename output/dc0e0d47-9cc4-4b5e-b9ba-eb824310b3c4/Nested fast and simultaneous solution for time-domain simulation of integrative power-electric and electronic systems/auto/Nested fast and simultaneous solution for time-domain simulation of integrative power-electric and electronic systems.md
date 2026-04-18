# Nested Fast and Simultaneous Solution for Time-Domain Simulation of Integrative Power-Electric and Electronic Systems

Kai Strunz and Eric Carlson

Abstract—As power electronics are increasingly used in powerelectric networks, there is an interest in the creation of time-domain simulation techniques that can model the diversity of the integrative power-electric and electronic system while achieving high accuracy and computational speed. In the proposed method, generation of electric network equivalents (GENE), this is supported through the nested structure of the overall simulation process. One or multiple parent simulations, in which the unknown voltages are calculated using nodal analysis, launch multiple child simulations concerned with diakoptic subdivisions of the system under study. The interfaces for information exchange between parent and child levels are designed to provide encapsulation. This makes the subdivisions appearing from outside in the form of network branches compatible with the nodal analysis approach. It also facilitates the use of diverse solution methods for different child simulations, as it is shown for the simultaneous solution of equations formulated with nodal analysis and state space methods. Computational efficiency is obtained through the coordinated application of sparsematrix methods, piecewise linear approximation of nonlinear characteristics, and precalculation of operations pertaining to recurring power-electronic switch statuses. The resulting overall solution process is simultaneous, distributed, and suitable for real-time simulation. The devised methodology is validated through simulation of the CIGRE HVdc benchmark model, comprising ac networks, twelve-pulse power-electronic converter stations, harmonic filters, and dc transmission.

Index Terms—Algorithms, circuit simulation, cosimulation, diakoptics, electromagnetic transients program (EMTP), HVdc transmission, modeling, numerical methods, parallel processing, power electronics, power system simulation, real-time systems, sparse-matrix techniques.

## I. INTRODUCTION

N important field of application for the simulators of A the Electromagnetic Transients Program (EMTP) type [1] is the time-domain study of integrative power-electric and electronic systems. Examples of timely interest include simulations of storage and compensation systems [2], [3]; distributed generation (DG) [4], [5]; all-electric ship power systems; and high-voltage direct current (HVdc) systems [6]–[8]. The interfacing of the power-electronic converters and networks can be made through disconnection and prediction of the common voltages and currents as shown in [6]. The time step must be small enough for the prediction to be accurate and to obtain numerical stability. Numerical stability can generally be enhanced by using an iterative scheme such as the compensation method [7] at the expense of an increased computational burden.

If no disconnections are made, then all couplings of lumped elements that exist in reality are retained in the models. This offers the possibility of designing a noniterative simultaneous solution [9] and is consistent with the objectives of this work. The method generation of electric network equivalents (GENE), proposed here, is centered on a noniterative simultaneous solution. It is to provide computational efficiency and accuracy while offering the flexibility of using locally diverse solution methods and retaining compatibility with existing simulation drivers based on nodal analysis, such as the EMTP. The computational efficiency envisaged is to be high enough to achieve at least real-time speed for the simulation of the CIGRE HVdc benchmark system on off-the-shelf PCs.

To avoid computationally expensive iterations, nonlinear device characteristics as those of power-electronic switches are here modeled through piecewise linear approximation as, for example, discussed in [10]. For the emulation of switching processes, methods for the fast noniterative simulation of switching, as described in [2], [11]–[13], are suitable. These methods have already been tested for real-time simulation.

To obtain an efficient simultaneous solution, different options have been considered. Popular schemes for the efficient simultaneous solution of a linear equation system with the vector of unknown and dependent variables are based on the exploitation of the given system topology that is mirrored through matrix . The topology of many networks is such that the corresponding nodal admittance matrix contains a significant number of zero elements. Methods aimed at retaining this sparsity by reducing the number of nonzero fill-in elements generated in the factorized lower and upper triangular matrices obtained through LU factorization do exist. The minimum degree algorithm presented in [14] achieves this while considering the overall system as a single piece, hereafter referred to as a single-piece method. In conjunction, sparse-matrix structures that only store the nonzero elements are important [15].

As opposed to a single-piece method, tearing, also known as diakoptics, is a multipiece method that enables a simultaneous solution. One possible approach to tearing, the so-called node tearing [15], leads to adopt the bordered block diagonal form as shown in Fig. 1, where symbol indicates a subdivision. It is an advantage of this formulation that part of the local solutions

$$
{ \binom { A _ { 1 1 } } { A _ { 2 1 } } } \ A _ { 1 2 } \biggl ) \left( \begin{array} { l } { { \xi _ { 1 } } } \\ { { \xi _ { 2 } } } \end{array} \right) = \left( \begin{array} { l } { { b _ { 1 } } } \\ { { b _ { 2 } } } \end{array} \right) \qquad A _ { 1 1 } = \left( \begin{array} { l l l l } { { A _ { 1 1 1 } ^ { \mathrm { c } } } } & { { } } & { { } } & { { } } \\ { { } } & { { \ddots } } & { { } } & { { } } \\ { { } } & { { } } & { { A _ { 1 1 M } ^ { \mathrm { c } } { } } } \end{array} \right)
$$

Fig. 1. From left to right: partitioned form of $\mathbf { A } \pmb { \xi } = \pmb { b } ,$ , blocks of $\mathbf { A } _ { 1 1 }$ along the diagonal.

corresponding to the $M ^ { \subset }$ pieces of subdivisions of $\pmb { A } _ { 1 1 }$ may be calculated in parallel. Then, the connections between the subdivisions through border matrices $\pmb { A } _ { 1 2 } , \pmb { A } _ { 2 1 }$ , and $\pmb { A } _ { 2 2 }$ are taken into account to get the overall solution. Of particular interest is the intersection network equation $A ^ { \cap } \pmb { \xi } _ { 2 } = \pmb { b } ^ { \cap }$ , here marked with to signify intersection

$$
A ^ { \cap } = A _ { \mathrm { 2 2 } } - A _ { \mathrm { 2 1 } } A _ { \mathrm { 1 1 } } ^ { - 1 } A _ { \mathrm { 1 2 } }\tag{1}
$$

$$
\pmb { b } ^ { \cap } = \pmb { b } _ { 2 } - \pmb { A } _ { 2 1 } \pmb { A } _ { 1 1 } ^ { - 1 } \pmb { b } _ { 1 } .\tag{2}
$$

The intersection network is an accurate miniature equivalent of the original network. The number of unknowns is so reduced to $\xi _ { 2 } , \mathrm { i . e . }$ , the unknowns of the intersection network that interconnects the subdivisions. These unknowns are therefore incident at the terminals of the subdivisions.

Multipiece and single-piece methods can be combined, for example, by first creating the bordered block diagonal form of a matrix and then considering the blocks as single pieces to which the minimum degree algorithm is applied [14].

The nested parent–child simulation method GENE presented in this work makes use of combined multi and single-piece solutions as well as sparse-matrix storage structures. In GENE, the intersection network, which is dealt with by the parent simulation, is not obtained using (1) and (2). Instead, miniature equivalents of subdivisions of power-electric network parts and power-electronic converters are calculated using Norton’s theorem in a first step. The obtained miniature equivalents are then interconnected at their terminal nodes to obtain the intersection network. The proposed method is particularly well suited as the basis of techniques for fast and simultaneous simulation of integrative power-electric and electronic systems where diverse behavior is observed.

To provide the reader with a relevant background and basis of comparison, selected foundations of transients simulation based on nodal analysis are elaborated upon in Section II. In Section III, the concept of the nested parent–child simulation is developed for nodal analysis techniques. The formulation is extended in Section IV to show the capability of simultaneous cosimulation based on both nodal analysis and state-space methods. The application and validation tests in Section V are centered on the CIGRE HVdc Benchmark model and show that accurate simulation at speeds faster than real time is achieved on an off-the-shelf PC. Conclusions are drawn in Section VI. In Appendices A and B, the application of the weight-averaged integration method for the purpose of modeling network branches and discretizing dynamic state equations is explained, respectively. In Appendix C, details of the algorithms of the nested parent–child simulation are elaborated upon.

![](images/53f6321783f8b2a400da6076333dbd0aeb4fc63f3f40779a91fbea1bed22aba1.jpg)  
Fig. 2. Access to branch admittance matrices corresponding to piecewise linear approximation.

## II. BASICS OF BRANCH AND NETWORK MODELING FOR TIME-DOMAIN TRANSIENTS SIMULATION

In order to obtain the network model for time-domain transients simulation based on nodal analysis, models of the branches that make up the network need to be available. Using the concept of companion modeling, the branches are described in the following form:

$$
{ \pmb Y } _ { \mathrm { B } } { \pmb v } _ { \mathrm { B } } = { \pmb j } _ { \mathrm { B } } + { \pmb i } _ { \mathrm { B } }\tag{3}
$$

where $\pmb { Y } _ { \mathrm { B } }$ is the nodal admittance matrix of the branch; $j _ { \mathrm { B } }$ is the vector of the source-dependent nodal current injections that are updated at each time step in accordance with changing initial conditions of the difference equations; ${ \pmb v } _ { \mathrm { B } }$ is the vector of the nodal voltages of the branch; and $\mathbf { \dot { \imath } } _ { \mathrm { B } }$ is the vector of the currents flowing into the branch. The derivation of (3) is detailed in Appendix A.

Using the piecewise linear approximation of the nonlinear characteristic of a power semiconductor valve in [10], two statuses corresponding to two distinct companion models distinguish between conducting and blocking modes. In general, segments of straight lines may be used to approximate a nonlinear function. Then, $\mathbf { Y } _ { \mathrm { B } }$ is obtained from a tensor comprising information for distinct branch companion models. To build up the network model, the one branch model that corresponds to the active status is selected as indicated in Fig. 2. Changes of status involve modifications of $Y _ { \mathrm { B } }$ and $j _ { \mathrm { B } }$ in (3).

The network model is obtained through direct construction [16], also referred to as stamping. First, all branches are conceptually removed from the network and then added successively in order to add the entries of $\pmb { Y } _ { \mathrm { B } }$ to the emerging nodal admittance matrix in accordance with the network topology. The equation system for the network model is then partitioned to distinguish between the voltages ${ \pmb v } _ { \mathrm { d } }$ that are unknown and dependent and the voltages ${ \pmb v } _ { \mathrm { e } }$ that are known and given through excitation functions

$$
{ \begin{array} { r l } { \left( Y _ { \mathrm { d d } } \quad Y _ { \mathrm { d e } } \right) \left( { \boldsymbol { v } } _ { \mathrm { d } } \right) = { \binom { j _ { \mathrm { d } } } { j _ { \mathrm { e } } + i _ { \mathrm { e } } } } } \end{array} }\tag{4}
$$

where $j _ { \mathrm { d } } , j _ { \mathrm { e } }$ are, respectively, the source-dependent nodal current injections into the nodes with unknown and known voltages and $\dot { \pmb { \imath } } _ { \mathrm { e } }$ are the currents that flow through the nodes with known voltages.

Given that there are unknown voltages, the $N \times N$ matrix $\pmb { Y } _ { \mathrm { d d } }$ is factorized into lower and upper triangular matrices $Y _ { \mathrm { d d } } = L _ { \mathrm { d d } } \pmb { U } _ { \mathrm { d d } }$ . The unknowns are obtained through the forward and backward substitution [17] by solving the following equation derived from the first row of (4):

$$
L _ { \mathrm { d d } } { \pmb U } _ { \mathrm { d d } } { \pmb v } _ { \mathrm { d } } = { \pmb j } _ { \mathrm { d } } - Y _ { \mathrm { d e } } { \pmb v } _ { \mathrm { e } } .\tag{5}
$$

## III. NODAL-ANALYSIS-BASED SIMULATION WITH GENE

While the nested parent–child simulation method GENE supports the use of diverse solution methods, its parent simulation as the driver of the overall solution process uses nodal analysis. In Section III-A, the parent simulation is described. Before the child simulations are explained, it needs to be shown how the child subdivisions are defined and their miniature equivalents are obtained. This is done in Sections III-B and III-C, respectively. The status indicator and access scheme for precalculation and storage at the child simulation level and the child simulation process itself are then developed in, respectively, Sections III-D and III-E. An analytic evaluation of the improvement in efficiency provided by the status indicator and access scheme is proposed in Section III-F. Details of the developed algorithms are discussed in Appendix C.

## A. Parent Simulation

As mentioned in Section II, the stamping method is widely used to build up the network model using the given branch models. At the parent simulation level, however, the stamping is applied to entire child subdivisions rather than individual branches. Prior to the stamping action, child subdivisions, as the one shown in Fig. 3, are reduced to miniature equivalents where only the terminal nodes at the boundaries of the subdivisions remain. As detailed in subsequent Sections III-B and III-C, this is done in order to have the child subdivision appear in the format of branch companion models

$$
{ \pmb { Y } } _ { \mathrm { N } } ^ { \subset } { \pmb { v } } _ { \mathrm { t } } ^ { \subset } = j _ { \mathrm { N } } ^ { \subset } + i _ { \mathrm { t } } ^ { \subset }\tag{6}
$$

where $\pmb { Y } _ { \mathrm { N } } ^ { \subset }$ is the nodal admittance matrix of the miniature equivalent of the child subdivision; $j _ { \mathrm { N } } ^ { \subset }$ is the vector of the source-dependent nodal current injections into the terminal nodes of the child subdivision; $\pmb { v } _ { \mathrm { t } } ^ { \subset }$ is the vector of the nodal voltages at the terminal nodes; $\pmb { i } _ { \mathrm { t } } ^ { \subset }$ is the vector of the currents flowing into the child subdivision. Equation (6) is indeed of the same format as (3). It is this analogy, to be detailed in Section III-C, that enables the use of the stamping method for the construction of the network model in exactly the same way for companion models of simple branches as well as for miniature equivalents of entire power-electronic converters and electric network parts. Since the stamping is applied to the miniature equivalents (6), the only unknown voltages to be solved for at the parent simulation level are those at the terminals of the child subdivisions.

The main steps of the parent simulation level are detailed in the pseudocode of Fig. 4. All terminal voltages are calculated in

![](images/c90dc69d35ed66ee16fe491b86cc171d7b836df94b033c6b556432d4ae6c24c7.jpg)  
Fig. 3. AC network on the inverter side of the CIGRE HVdc benchmark model represented as a child subdivision.

Step 1: Calculate nodal voltages: ${ Y _ { \mathrm { d d } } ^ { \cap } } v _ { \mathrm { d } } ^ { \cap } = j _ { \mathrm { d } } ^ { \cap } - { Y _ { \mathrm { d e } } ^ { \cap } } v _ { \mathrm { e } } ^ { \cap }$

Step 2:For all child subdivisions do:perform child simulations.

Step 3:If there is a status change of the network, then do: Step 3.1: Reconstruct $\mathbf { Y } _ { \mathrm { d d } } ^ { \mathrm { n } }$ accordingly. Step 3.2: Refactorize $\mathbf { \Delta } \mathbf { Y } _ { \mathrm { d d } } ^ { \cap \cdots }$ into $\pmb { L } _ { \mathrm { d d } } ^ { \cap }$ and $U _ { \mathrm { { d d } } } ^ { \cap } .$

Step 4: Advance the time dependent excitation sources of the network.

Step 5:According to the sources and status of the network construct $\hat { \mathcal { A } } .$

Step 6: Increment time step counter. If termination condition is met, then exit.Else return to step 1.

Fig. 4. Course of actions in parent simulation using GENE.

![](images/54d198c30844fcd0a3193470258fee8313341f2ec41273a84fc8152a10713a5d.jpg)  
Fig. 5. Information exchange between parent and child simulations.

step 1. The symbol for intersection is used to stress that the ensemble of all unknown terminal voltages of child subdivisions makes up the vector of unknown voltages of the intersection network. Then, the child simulations are called in step 2. Thus, the parent simulation launches new child simulations, leading to a nested structure. The information exchange between parent and $M ^ { \subset }$ different child simulations is clarified in Fig. 5. At the beginning of step 2, the child simulations receive their respective terminal voltages as inputs. These terminal nodes are, of course, incident at the intersection network and, therefore, known from step 1. At the end of step 2, the subdivisions return their respective miniature equivalents to the parent simulation process.

If any of the returned ${ \cal Y } _ { \mathrm { N } } ^ { \subset }$ has been modified, for example, due to a change of status of a piecewise linear approximation, then in step 3.1, matrices are reconstructed using stamping in accordance with the updated status of the network. Furthermore, the LU factorization is performed in step 3.2. In step 4, the time-dependent excitation sources are advanced. In step 5, the vector of the source-dependent nodal current injections $j _ { \mathrm { d } } ^ { \cdot }$ is constructed. In step 6, the time step counter is incremented and the termination condition is checked. The loop is entered again at step 1 if the termination condition is not met.

For the purpose of comparison, step 2 is shown in Fig. 6 in a simulation process without nesting. As a comparison with Fig. 4 shows, branches are dealt with analogous to child subdivisions. It is important to note that all remaining steps can be retained as in Fig. 4. This analogy of simulator design ensures compatibility of the nested simulation with existing simulation drivers based on nodal analysis.

Step 2:For all branch models do: perform branch simulations.

Fig. 6. Step 2 in simulation without further nesting.

While the pseudocode in Fig. 4 gives the basic outline of the parent simulation, selected techniques have been added to increase accuracy and computational speed. Especially when power electronics are to be simulated in real time, it is important to track switching events accurately and efficiently, and this can be done here as described in [11].

If the network contains transmission paths for which the wave traveling times between both ends are equal to or larger than the time step size, then both ends are isolated mathematically for at least one time step interval [18]. For each portion, a separate nodal admittance matrix can be established.

## B. Child Subdivision

As an example of realizing a child subdivision, the three-phase ac network on the inverter side of the CIGRE HVdc benchmark system, shown in Fig. 3, is considered. The excitation voltages $\pmb { v } _ { \mathrm { e } } ^ { \subset }$ are given by the three-phase voltage source. Voltages ${ \pmb v } _ { \mathrm { d 1 } } ^ { \subset } , { \pmb v } _ { \mathrm { d 2 } } ^ { \subset }$ , and $\pmb { v } _ { \mathrm { d 3 } } ^ { \subset }$ are dependent and unknown. Terminal voltages $\pmb { v } _ { \mathrm { t } } ^ { \subset }$ appear as inputs coming from the parent simulation. When all inductors are replaced by their companion models as shown in Appendix A and stamping is applied, child subdivisions can be described in the following general form:

$$
\left( \begin{array} { c c c } { Y _ { \mathrm { d d } } ^ { \subset } } & { Y _ { \mathrm { d e } } ^ { \subset } } & { Y _ { \mathrm { d t } } ^ { \subset } } \\ { Y _ { \mathrm { e d } } ^ { \subset } } & { Y _ { \mathrm { e e } } ^ { \subset } } & { Y _ { \mathrm { e t } } ^ { \subset } } \\ { Y _ { \mathrm { t d } } ^ { \subset } } & { Y _ { \mathrm { t e } } ^ { \subset } } & { Y _ { \mathrm { t t } } ^ { \subset } } \end{array} \right) \left( \begin{array} { c } { \pmb { v } _ { \mathrm { d } } ^ { \subset } } \\ { \pmb { v } _ { \mathrm { e } } ^ { \subset } } \\ { \pmb { v } _ { \mathrm { t } } ^ { \subset } } \end{array} \right) = \left( \begin{array} { c } { j _ { \mathrm { d } } ^ { \subset } } \\ { j _ { \mathrm { e } } ^ { \subset } + i _ { \mathrm { e } } ^ { \subset } } \\ { j _ { \mathrm { t } } ^ { \subset } + i _ { \mathrm { t } } ^ { \subset } } \end{array} \right) .\tag{7}
$$

In the case of the example, vector ${ \pmb v } _ { \mathrm { d } } ^ { \subset }$ then comprises three threephase voltages ${ \pmb v } _ { \mathrm { d } } ^ { \subset } = ( { \pmb v } _ { \mathrm { d 1 } } ^ { \subset } { \pmb v } _ { \mathrm { d 2 } } ^ { \subset } { \pmb v } _ { \mathrm { d 3 } } ^ { \subset } ) ^ { \top }$

The creation of child subdivisions in the format described allows for encapsulation. This means that all computations that concern a child subdivision are performed locally within the child simulation process. In order to perform forward and backward substitutions locally, $\pmb { Y } _ { \mathrm { d d } } ^ { \subset }$ is factorized into lower and upper triangular matrices $\pmb { L } _ { \mathrm { d d } } ^ { \subset }$ and $U _ { \mathrm { d d } } ^ { \subset }$ . Based on the first row of $( 7 ) , \pmb { v } _ { \mathrm { d } } ^ { \subset }$ is then calculated with the following equation:

$$
\pmb { L } _ { \mathrm { d d } } ^ { \subset } \pmb { U } _ { \mathrm { d d } } ^ { \subset } \pmb { v } _ { \mathrm { d } } ^ { \subset } = \pmb { j } _ { \mathrm { d } } ^ { \subset } - \pmb { Y } _ { \mathrm { d e } } ^ { \subset } \pmb { v } _ { \mathrm { e } } ^ { \subset } - \pmb { Y } _ { \mathrm { d t } } ^ { \subset } \pmb { v } _ { \mathrm { t } } ^ { \subset } .\tag{8}
$$

In order to boost the efficiency at the child simulation level, the minimum degree algorithm and sparse-matrix storage structures, as discussed in Section I, are applied.

## C. Contractual Interfacing Through Companion Model Emulation

In order to obtain the companion model of a miniature equivalent of a child subdivision given through (6), $\pmb { v } _ { \mathrm { d } } ^ { \subset }$ is eliminated in (7) using the Kron reduction formula [19]. The miniature equivalents of the nodal admittance matrix and source vector then constitute Norton equivalents in the form given through (3). A comparison of (3) and (6) shows that vector $\pmb { v } _ { \mathrm { t } } ^ { \subset }$ corresponds to $\pmb { v } _ { \mathrm { B } } ^ { \subset }$ , and ${ \cal Y } _ { \mathrm { N } } ^ { \subset }$ and $j _ { \mathrm { N } } ^ { \subset }$ , respectively, correspond to $Y _ { \mathrm { B } } ^ { \mathcal { \bar { C } } }$ and $\pmb { j } _ { \mathrm { B } } ^ { \subset }$ . As already indicated in Section III-A, interfacing parent and child simulations through companion models allows for the use of the stamping method. This interfacing involves no disconnection so that couplings between multiple subdivisions are retained as in reality. An intersection network description analogous to the one of (1) and (2) is therefore directly obtained through stamping. Further details on the calculation of the Norton equivalent are given in Appendix C.1.

![](images/893b0326f4393b5fb9e32882e0c5586928e9825824834e4019f16766da2e9a40.jpg)  
Fig. 7. Power-electronics converter represented as a child subdivision.

## D. Subdivision Status Indicator and Access Scheme

As justified and mentioned in Sections I and II, piecewise linear approximation is used here to model nonlinear characteristics of branches. Since statuses are associated with branches as shown in Fig. 2, statuses must also be associated with child subdivisions. This is because the miniature equivalents adopt the same format as branch companion models. Through the status indicator scheme, a subdivision status variable is associated with each possible combination of status values of piecewise linear approximations in a subdivision. Details of the algorithms involved in the status indicator and access scheme are given in Appendix C.2.

Consider the child subdivision in Fig. 7, where, for the purpose of this example, the nonlinearities of the thyristors and saturable smoothing inductor $L _ { \mathrm { s m } }$ are studied. If the thyristor is represented through two statuses and the smoothing inductor saturation characteristic is represented through three statuses, then the total number of possible statuses of this child subdivision with six thyristors and one smoothing inductor is $S =$ $2 ^ { 6 } \cdot 3 ^ { 1 } = 1 9 2$

Child subdivisions can be defined in very different ways as the comparison of Figs. 3 and 7 shows. The subdivision status indicator and access scheme is flexible in that it can be applied to any of them and is not confined to any preselected type of circuit. The particular selection of the child subdivision boundaries as shown in Fig. 7 mirrors the definition of an HVdc object model for fast simulation presented in [8]. A twelve-pulse HVdc converter station can so be modeled by the connection of two six-pulse arrangements for each of which in the example 192 different statuses do exist. In general, for subdivision , there are $S _ { m }$ different statuses, and information is stored for each status. Given that there are $M ^ { \subset }$ child simulation processes, there are $\textstyle \sum _ { m = 1 } ^ { M ^ { \subset } } S _ { m }$ different statuses for which information is stored at the child simulation level. At the parent simulation level, there are $\Pi _ { m = 1 } ^ { M ^ { \subset } } S _ { m }$ statuses because with each subdivision added, the number of different statuses is multiplied by $S _ { m }$ . Since $\textstyle \sum _ { m = 1 } ^ { M ^ { \subset } } S _ { m }$ can be made much lower than $\prod _ { m = 1 } ^ { \bar { M } ^ { \subset } } S _ { m } .$ tearing into subdivisions and considering status values at the child simulation level can reduce storage requirements significantly. In the example of the twelve-pulse HVdc converter station, this becomes obvious since $1 9 2 + 1 9 2 \ll 1 9 2 \cdot 1 9 2$

Before the simulation starts, matrices associated with a child subdivision, such as the miniature equivalent matrix ${ \pmb Y } _ { \mathrm { N } } ^ { \subset }$ , are calculated and stored in a sparse-matrix storage structure [15] in fast accessible memory for each status of a subdivision. The memory addresses showing where the matrices can be accessed are stored in an array [20]. Access to the matrices is then possible in the same way as described in Fig. 2. However, rather than accessing branches of status $\sigma ,$ child subdivisions of status are accessed.

## E. Child Simulation Process

As shown in Fig. 5, the child simulation receives the terminal voltages as input. It uses this information to calculate the nodal voltages within the child subdivision using (8). It performs further steps to return the Norton source as detailed in the pseudocode developed in Appendix C.3. The use of the subdivision status indicator and access scheme allows the avoidance of refactorizations. Thanks to the contractual interfacing through branch emulation, the overall solution process is simultaneous.

## F. Efficiency Contributions of Subdivision Status Indicator and Access Scheme

In order to obtain an efficient overall simulation process, suitable intersection and subdivision networks to associate with the parent and child simulation processes are selected. In particular, when using parallel processing, it is advantageous to keep the computational effort for the different child simulation processes at a similar level by defining subdivisions of similar complexity. Reductions in storage requirement are usually achieved by reducing the number of status values per subdivision as discussed in Section III-D. At the same time, it is desirable to keep the size of the intersection network small to obtain a fast parent simulation process. General guidelines and further discussions on the network tearing are, for example, given in [15], [21]–[23].

As the multiplication count performed in Appendix C.4 demonstrates, the computational speed of GENE exceeds the one that is obtained when just using node tearing. This speedup is attributed to the subdivision status indicator and access scheme. When status changes occur, costly refactorizations do not need to be performed at the child simulation level. For the same reason, in GENE, the multiplication count does not change with status changes but remains constant. This makes the method suitable for real-time applications where a constant computational burden at any time step is desired.

## IV. SIMULTANEOUS COSIMULATION WITH GENE

A feature of GENE is the ability to integrate diverse solution techniques within a simultaneous overall simulation process.

## A. Concept

The child simulation uses the input information ${ \pmb v } _ { \mathrm { t } } ^ { \subset }$ in order to calculate and return ${ \cal Y } _ { \mathrm { N } } ^ { \subset } , j _ { \mathrm { N } } ^ { \subset }$ as output. Due to the encapsulation property, the implementation of these calculations is hidden. The use of diverse solution methods in different child simulation processes is therefore supported. This is useful if models of subdivisions are available in a format not based on nodal analysis. As long as the presented rules for contractual interfacing described in Section III-C are respected, simultaneous cosimulation is obtained.

## B. Case Study: Cosimulation With State-Space Methods

The state-space method and associated dynamic state equations provide a well-established framework [24] for the modeling of dynamic systems.

1) Child Subdivision: For the purpose of illustrating the simultaneous cosimulation of nodal and dynamic state equations, a linear lumped passive circuit is modeled with dynamic state equations and brought into a format that allows for use in a child simulation

$$
\begin{array} { r } { \left( \begin{array} { l l } { A ^ { \subset } } & { B ^ { \subset } } \\ { C ^ { \subset } } & { D ^ { \subset } } \end{array} \right) \left( \begin{array} { l } { x ^ { \subset } } \\ { v _ { \mathrm { t } } ^ { \subset } } \end{array} \right) = \left( \begin{array} { l } { \dot { x } ^ { \subset } } \\ { i _ { \mathrm { t } } ^ { \subset } } \end{array} \right) } \end{array}\tag{9}
$$

where the newly introduced symbol refers to the vector of dynamic state variables. Using weight-averaged integration, (9) can be discretized as shown in detail in Appendix B. The result is the model of the child subdivision

$$
\left( \begin{array} { c c } { P ^ { \subset } } & { Q ^ { \subset } } \\ { C ^ { \subset } } & { D ^ { \subset } } \end{array} \right) \left( \begin{array} { c } { x ^ { \subset } } \\ { v _ { \mathrm { t } } ^ { \subset } } \end{array} \right) = \left( \begin{array} { c } { \eta _ { x } ^ { \subset } } \\ { i _ { \mathrm { t } } ^ { \subset } } \end{array} \right)\tag{10}
$$

where $\pmb { \eta } _ { \pmb { x } } ^ { \subset }$ only depends on results from previous time steps as shown in Appendix B. Once $\pmb { v } _ { \mathrm { t } } ^ { \subset }$ is obtained at the beginning of step 2 from the parent simulation, the state variables can be calculated as

$$
L _ { P } ^ { \subset } U _ { P } ^ { \subset } x ^ { \subset } = \eta _ { x } ^ { \subset } - Q ^ { \subset } v _ { \mathrm { t } } ^ { \subset }\tag{11}
$$

where

$$
\begin{array} { r } { P ^ { \subset } = L _ { P } ^ { \subset } U _ { P } ^ { \subset } . } \end{array}\tag{12}
$$

2) Contractual Interfacing Through Companion Model Emulation: Equation (10) is already brought into a form to provide the possibility of contractual interfacing through companion model emulation. To obtain the miniature equivalent of (6), the first row of (10) is eliminated using Kron’s reduction

$$
Y _ { \mathrm { N } } ^ { \subset } = D ^ { \subset } - T _ { C P } ^ { \subset } Q ^ { \subset }
$$

$$
j _ { \mathrm { N } } ^ { \subset } = - T _ { C P } ^ { \subset } \eta _ { x } ^ { \subset }\tag{13}
$$

(14)

and the transfer matrix $\pmb { T } _ { C P } ^ { \subset }$

$$
T _ { C P } ^ { \zeta } P ^ { \zeta } = C ^ { \zeta } .\tag{15}
$$

The elements of $\pmb { T } _ { C P } ^ { \subset }$ are obtained using forward and backsubstitutions. Equations (13)–(15) define the companion model of

![](images/9b0395dc1f90645a984a394e51d85740fd1bfe1b30ae82459995f6e22a2108f0.jpg)  
Fig. 8. Test circuit for evaluation of the child subdivision.

![](images/4218f983098efe03ee99e19ab14c8c47f34db7d7d7952566b3982cc276bffab5.jpg)  
Fig. 9. Fourth-order highpass ac filter.

(6) to be stamped into the parent simulation process with the information exchange of Fig. 5.

## V. APPLICATION AND VALIDATION

The nested parent–child simulation method GENE was implemented in the simulator virtual integrator for synthesis, testing, and analysis (VISTA). Two studies are presented for the purpose of validating the performance of the nested parent–child simulation. In the first study, a harmonic filter is represented in the form of a child subdivision. Then, the CIGRE HVdc benchmark model is implemented.

## A. Lumped Linear Circuit

This validation test is aimed at verifying the methodology when a child simulation process is formulated based on the state-space method while nodal analysis is used for the parent simulation. For the validation test, the terminal voltage is applied through an ideal voltage source as shown in Fig. 8. The considered lumped linear circuit in the subdivision is the fourth-order highpass ac filter of the CIGRE HVdc benchmark model and is shown in Fig. 9. The dynamic state variables are the currents through the inductors and the voltages across the capacitors $\pmb { x } ^ { \subset } = ( \bar { i } _ { \mathrm { L 1 } } i _ { \mathrm { L 2 } } v _ { \mathrm { C 1 } } v _ { \mathrm { C 2 } } ) ^ { \mathrm { T } }$ . The parameters are as follows:

$$
R _ { 1 } = 8 3 . 0 0 \Omega , \quad R _ { 2 } = 5 0 . 0 0 \Omega , \quad L _ { 1 } = 1 5 . 1 0 \mathrm { m H } ,
$$

$$
L _ { 2 } = 9 . 6 9 ~ \mathrm { m H } , ~ C _ { 1 } = 6 . 5 7 ~ \mu \mathrm { F } , ~ C _ { 2 } = 7 8 . 9 0 ~ \mu \mathrm { F } .
$$

![](images/442ff32365f3ef277da4a18f5810d0c41d9d39bb8a94e2ccfc740423b0b8d11d.jpg)

![](images/ffbf88fb96c70559ea498a47526e0295fbd2f7a03c49f972705e2af2e8c48433.jpg)

![](images/9c2b56f1831174757a6306b8371f2252a7224bfa1c11c6266df605b3d734eed2.jpg)  
Fig. 10. Bode diagram for the fourth-order highpass filter; exact , simulated with method GENE .

The time step size of the simulation is equal to 50 s and, in the weight-averaged method discussed in Appendix B, is selected to obtain the trapezoidal method because it is very well suited for simulating the sinusoidal waveforms.

The bode diagram of the impedance of the harmonic filter measured at different source frequencies is depicted in Fig. 10. As a reference, the exact solution is drawn in the same diagram. The agreement of the measured and exact curves is clearly recognizable and confirms the high degree of accuracy of the simulation process. The deviation observed at very high frequencies is caused by the numerical integration.

## B. CIGRE HVDC Benchmark Model

The CIGRE HVdc benchmark model [25], shown in Fig. 11, is a well-accepted testbed for simulation.

1) Decomposition Into Parent and Child Simulations: Modeling the wave propagation of the dc line using distributed parameters and its losses through lumped elements, the model can be partitioned into two portions assigned to parents A and B. Each parent simulation calls five child simulations to simulate the child subdivisions. Subdivisions A.4 and A.5 are defined in accordance with suggestions in [8]. Valves are modeled with a snubber $R _ { \mathrm { s n } } = 6 0 0 0 \Omega , C _ { \mathrm { s n } } = 4 0$ nF as shown in Fig. 7. The valve modeling technique described in [10] is applied. With one three-phase node counted as three single-phase nodes, the intersection network of the parent simulation in portion A has only five single-phase nodes. Portion B, the inverter side, is dealt with in the same way as portion A.

![](images/9895d07311815a369750f15c68ba2389d055d41c1ec74bf0a4e6d5bf14b0edc0.jpg)  
Fig. 11. CIGRE HVdc benchmark model.

2) Compilation and Hardware: The program for the execution was generated by means of the compiler and linker DJGPP, version 2. The hardware comprises one processor Intel Pentium 4 2.4 GHz and a random-access memory (RAM) of 256 MB.

3) Waveform Comparison: The simulations of the valve voltage $v _ { \mathrm { V 1 } }$ and valve current marked in Fig. 7 are depicted in Fig. 12. The results obtained with a simultaneous solution using the DCG EPRI Version 3.a of the EMTP at a time step of 10 s are depicted on the left. The results obtained with GENE at a time step size of 100 s are shown on the right. In the used EMTP version, a method to pinpoint switching events through interpolation is not available. In the GENE simulation, switching events were tracked as discussed in [11]. Therefore, a much larger time step size could be selected for the method GENE.

The results show very close agreement and are in accordance with the commutation processes observed in HVdc converter stations. In general, it can be said that the observed accuracy matches that obtained with simultaneous single-piece solutions where comparable methods for the representation of nonlinearities are employed. This is plausible because the process of generating miniature equivalents of the child subdivision does not involve further approximations, and the nested multipiece solution is simultaneous.

4) Time Comparison: Applying the method GENE as a nested simulation, the largest measured computation time for the execution of all calculations per time step was of the order of 30 s. Real-time or faster-than-real-time speed can be achieved on an off-the-shelf PC with one processor when selecting a time step size larger than 30 s. In Table I, this time is compared with results obtained using alternative solutions.

valve voltage simulated with EMTP valve voltage simulated with GENE  
![](images/0cb8198074eace51127b2fcb959945ebc346f5a0f8ded40728d682d44f74ed65.jpg)  
Fig. 12. Valve voltages and currents of the CIGRE HVdc benchmark model.

Applying the minimum degree algorithm to each of the parent simulations separately and considering each of the two associated networks as a single piece, the time obtained is 39 s. In the full-matrix solution, no such optimizations are applied. The results confirm the computational efficiency of the nested parent–child simulation.

The method GENE, as a combination of multipiece and single-piece methods, simulated the benchmark faster than the single-piece method alone. This performance shows that the methodology of reducing the size of the matrix to where refactorization is applied at the parent simulation level and then using the minimum degree method, precalculation, and storage at the child simulation level is effective.

TABLE I  
MAXIMAL COMPUTATION TIMES PER TIME STEP
<table><tr><td rowspan=1 colspan=1>GENE</td><td rowspan=1 colspan=1>minimum degree</td><td rowspan=1 colspan=1>full-matrix</td></tr><tr><td rowspan=1 colspan=1> $3 0 ~ \mu \mathrm { s }$ </td><td rowspan=1 colspan=1> $3 9 \ \mu \mathrm { s }$ </td><td rowspan=1 colspan=1> $3 0 0 ~ \mu \mathrm { s }$ </td></tr></table>

Parallel processing of multiple child simulation processes can further improve the computation time although this requires multiple processors. With the single-processor hardware as mentioned in Section V-B2, parallel processing cannot be performed. Together with the cosimulation capability, the possibility to run fast simulation appears here as one of the main advantages of GENE. Speeds faster than real time are achieved with a single processor for the CIGRE HVdc benchmark system.

## VI. CONCLUSION

The method GENE as a nested solution for the time-domain simulation of transients of integrative power-electric and electronic systems was proposed, implemented, and tested. The overall solution process is decomposed hierarchically into parent and child simulations. The parent simulation calculates the voltages at the terminal nodes of the child subdivisions. In the child simulations, the local voltages at the nodes within the subdivisions are calculated. The proposed interfacing between parent and child simulations through companion model emulation is clearly defined and organized in that child subdivisions are treated in the same way as companion models of branches. This enables compatibility with existing simulation drivers based on nodal analysis. Furthermore, the calculations within the child simulations are encapsulated and the application of locally different solution procedures is so supported. This was demonstrated through a simultaneous cosimulation involving both the nodal analysis and state-space methods.

A subdivision status indicator and access scheme was devised in order to avoid refactorizations at the child simulation level and, thus, enhance computational speed. For each status, a set of sparse matrices and vectors is precalculated and prestored, retaining the sparsity so that the corresponding information is readily available during the simulation. It requires that nonlinear characteristics inside a child subdivision be modeled by means of piecewise linear approximation. The application of the status indicator and access scheme is of particular interest in real-time simulation as the computational burden is well balanced over successive time step intervals.

The boundaries of the child subdivisions are selected manually by the user. An idea for future work is to devise an algorithm that automatically decomposes the overall system into child subdivisions. The objective function of the algorithm would aim to minimize the overall computational effort. In this context, the multiplication count formulas presented in this paper constitute an important step towards the evaluation of the computational effort.

![](images/d4dc379f7e5db93e33520353aa1e1b358affe1464f103d28b7c320bd923b09f5.jpg)  
Fig. 13. Conventions for inductor: Left: description in continuous time domain. Right: companion branch model in discrete time domain.

In conjunction with a method for the tracking of switching events, the GENE method was implemented in the simulator virtual infrastructure for synthesis, testing, and analysis (VISTA) and tested through the simulation of the CIGRE HVdc benchmark model. The simultaneous nested solution has shown to give the same level of accuracy as a simultaneous single-piece solution. The nested solution has shown to be faster than the single-piece solution. Faster than real-time performance was achieved on a standard PC. The combination of computational efficiency and accuracy at any time step, the flexibility of using locally diverse solutions, and the compatibility with existing simulation drivers based on nodal analysis make the method so well suited for time-critical transients simulation of the diverse combination of power-electric and electronic systems.

## APPENDIX

## A. Companion Branch Modeling With Weight-Averaged Integration

The differential equations describing individual network branches are approximated by means of numerical integration. For example, the behavior of the inductor in Fig. 13 is described through the following differential equation:

$$
\frac { \mathrm { d } i _ { \mathrm { L } } ( t ) } { \mathrm { d } t } = \frac { v _ { \mathrm { L } } ( t ) } { L } .\tag{A.1}
$$

Using weight-averaged integration with time step size , (A.1) is discretized

$$
i _ { \mathrm { L } } ( k ) = \frac { \tau ( 2 - w ) } { 2 L } v _ { \mathrm { L } } ( k ) + i _ { \mathrm { L } } ( k - 1 ) + \frac { \tau w } { 2 L } v _ { \mathrm { L } } ( k - 1 ) .\tag{A.2}
$$

For $w = 1$ , the trapezoidal method and for $w = 0$ , the backward-Euler method are obtained as discussed in [12]. By substituting

$$
G _ { \mathrm { L } } = \frac { \tau ( 2 - w ) } { 2 L } , \quad \eta _ { \mathrm { L } } ( k ) = i _ { \mathrm { L } } ( k - 1 ) + \frac { \tau w } { 2 L } v _ { \mathrm { L } } ( k - 1 )
$$

the inductor is modeled through a companion model as shown on the right-hand side of Fig. 13. By setting $\mathbf { \dot { \iota } } _ { \mathrm { B } } = ( \dot { \iota } _ { \mathrm { B } 1 } \dot { \iota } _ { \mathrm { B } 2 } ) ^ { \mathrm { T } }$ ${ \pmb v } _ { \mathrm { B } } ~ = ~ \overline { { ( } } \upsilon _ { \mathrm { B 1 } } ~ { \upsilon } _ { \mathrm { B 2 } } ) ^ { \mathrm { T } }$ and using the conventions indicated in Fig. 13, and $j _ { \mathrm { B } }$ of (3) can be determined for the inductor example

$$
\begin{array} { r } { Y _ { \mathrm { B } } = \left( \begin{array} { c c } { G _ { \mathrm { L } } } & { - G _ { \mathrm { L } } } \\ { - G _ { \mathrm { L } } } & { G _ { \mathrm { L } } } \end{array} \right) , \quad \pmb { j } _ { \mathrm { B } } = \left( \begin{array} { c c } { - \eta _ { \mathrm { L } } ( k ) } \\ { \eta _ { \mathrm { L } } ( k ) } \end{array} \right) . } \end{array}\tag{A.3}
$$

## B. Discretization of Dynamic State Equations With Weight-Averaged Integration

Using the weight-averaged method for flexible integration as in Appendix A, the differential equation in the first row of (9) is discretized

$$
\begin{array} { r } { \displaystyle \frac { 2 - w } { 2 } \left( A ^ { \subset } \pmb { x } ^ { \subset } ( k ) + B ^ { \subset } \pmb { v } _ { \mathrm { t } } ^ { \subset } ( k ) \right) + \displaystyle \frac { w } { 2 } \left( A ^ { \subset } \pmb { x } ^ { \subset } ( k - 1 ) + \right. } \\ { \displaystyle \left. B ^ { \subset } \pmb { v } _ { \mathrm { t } } ^ { \subset } ( k - 1 ) \right) = \displaystyle \frac { \pmb { x } ^ { \subset } ( k ) - \pmb { x } ^ { \subset } ( k - 1 ) } { \tau } . } \end{array}\tag{B.4}
$$

The GENE method requires (B.4) to be rearranged as follows:

$$
\begin{array} { r } { P ^ { \subset } \pmb { x } ^ { \subset } ( k ) + \pmb { Q } ^ { \subset } \pmb { v } _ { \mathrm { t } } ^ { \subset } ( k ) = \pmb { \eta } _ { \pmb { x } } ( k ) . } \end{array}
$$

Comparison of this format with (B.4) gives

$$
P ^ { \subset } = \left( \frac { 2 - w } { 2 } A ^ { \subset } - E _ { \kappa } / \tau \right)\tag{B.5}
$$

$$
Q ^ { \subset } = { \frac { 2 - w } { 2 } } B ^ { \subset }\tag{B.6}
$$

$$
\begin{array} { r l } & { { \boldsymbol { \eta } } _ { \pmb { x } } = - \left( \frac { w } { 2 } { \pmb { A } } ^ { \top } + { \pmb { E } } _ { \kappa } / \tau \right) { \pmb { x } } ^ { \top } ( k - 1 ) } \\ & { \quad \quad - \frac { w } { 2 } { \pmb { B } } ^ { \top } { \pmb { v } } _ { \mathrm { t } } ^ { \top } ( k - 1 ) . } \end{array}\tag{B.7}
$$

Matrix $\pmb { E } _ { \kappa }$ is the identity matrix of dimension , where is the number of dynamic state variables. The second row of (9) is an algebraic matrix equation and does not require the application of numeric integration.

## C. Details of Algorithms in GENE

In Section III, the nodal-analysis-based simulation with GENE is introduced conceptually. In the following, the description is detailed through thorough discussions of the algorithms.

1) Details of Contractual Interfacing Through Companion Model Emulation: The Kron reduction formula is applied to eliminate ${ \pmb v } _ { \mathrm { d } } ^ { \subset }$ in (7) and obtain the nodal admittance matrix and source vector of the companion model emulation (6) for the child subdivision

$$
\pmb { Y } _ { \mathrm { N } } ^ { \subset } = \pmb { Y } _ { \mathrm { t t } } ^ { \subset } - \pmb { T } _ { \mathrm { t d } } ^ { \subset } \pmb { Y } _ { \mathrm { d t } } ^ { \subset }\tag{C.8}
$$

$$
\begin{array} { r } { \pmb { j } _ { \mathrm { N } } ^ { \subset } = \pmb { j } _ { \mathrm { t } } ^ { \subset } - \pmb { T } _ { \mathrm { t d } } ^ { \subset } \pmb { j } _ { \mathrm { d } } ^ { \subset } - \pmb { Y } _ { \pmb { j } _ { \mathrm { N } } \pmb { v } _ { \mathrm { e } } } ^ { \subset } \pmb { v } _ { \mathrm { e } } ^ { \subset } } \end{array}\tag{C.9}
$$

and the transfer matrices $\pmb { T } _ { \mathrm { t d } } ^ { \subset } \pmb { Y } _ { j _ { \mathrm { N } } \pmb { v } _ { \mathrm { e } } } ^ { \subset } ;$

$$
\pmb { T } _ { \mathrm { t d } } ^ { \subset } \pmb { Y } _ { \mathrm { d d } } ^ { \subset } = \pmb { Y } _ { \mathrm { t d } } ^ { \subset } ,\tag{C.10}
$$

$$
\begin{array} { r } { Y _ { j _ { \mathrm { N } } v _ { \mathrm { e } } } ^ { \subset } = Y _ { \mathrm { t e } } ^ { \subset } - { T } _ { \mathrm { t d } } ^ { \subset } Y _ { \mathrm { d e } } ^ { \subset } . } \end{array}\tag{C.11}
$$

The elements of $\pmb { T } _ { \mathrm { t d } } ^ { \subset }$ are obtained using forward and backsubstitutions based on the factorization of $\pmb { Y } _ { \mathrm { d d } } ^ { \subset }$ into $\pmb { L } _ { \mathrm { d d } } ^ { \subset }$ and $\pmb { U } _ { \mathrm { d d } } ^ { \subset }$

2) Details of Subdivision Status Indicator and Access Scheme: The following notation is introduced to detail the status indicator and access scheme:

$\psi$ number of different types of piecewise linear branch models for which instances exist in a subdivision;

v counter which indicates the type of a piecewise linear branch model for which instances exist in the subdivision $\nu \in \{ 0 , \ldots , \psi - 1 \}$ ;

$\phi _ { \nu }$ number of instances of the piecewise linear branch model of type in a subdivision min $\phi _ { \nu } = 1 ;$ ;

$\mu _ { \nu }$ counter which indicates the instance of a piecewise linear branch model $\mu _ { \nu } \in \{ 0 , \ldots , \phi _ { \nu } - 1 \} ;$

$P _ { \nu }$ number of different statuses of the piecewise linear branch model of type $\nu ;$

$\sigma _ { \nu \mu _ { \nu } }$ active status of the instance $\mu _ { \nu }$ of the piecewise linear branch model of type $\sigma _ { \nu \mu _ { \nu } } \in \{ 0 , \ldots , P _ { \nu } - 1 \}$ ;

S number of possible status values of a child subdivision;

S status of a child subdivision $s \in \{ 0 , . . . , S - 1 \}$

For the purpose of illustration, the child subdivision in Fig. 7 with the nonlinearities of the thyristors and saturable smoothing inductor $L _ { \mathrm { s m } }$ is considered. Let both nonlinear types be modeled through piecewise linear approximations and, therefore, $\psi = 2$ . Let the thyristor type be assigned $\nu = 0$ and the saturable smoothing inductor type $\nu ~ = ~ 1$ . Then, $\phi _ { 0 } ~ = ~ 6$ and $\phi _ { 1 } = 1$ . The six instances of type $\nu = 0$ are assigned numbers $\mu _ { 0 } \in \{ 0 , \ldots , 5 \}$ , and for the one instance of $\nu = 1$ , there is only $\mu _ { 1 } = 0$ . If the thyristor model is represented through two statuses, then $P _ { 0 } = 2 .$ . It is reasonable to associate the blocking status of the thyristor model’s instance number $\mu _ { 0 }$ with $\sigma _ { 0 \mu _ { 0 } } ~ = ~ 0$ and its conducting status with $\sigma _ { 0 \mu _ { 0 } } ~ = ~ 1$ . If the smoothing inductor saturation characteristic is modeled through three different statuses, then $P _ { 1 } = 3$ and $\sigma _ { 1 0 }$ can adopt three values, i.e., $\sigma _ { 1 0 } \in \{ 0 , 1 , 2 \}$

Through each additional instance of a model of type within a subdivision, the total number of possible statuses of this subdivision is multiplied by $P _ { \nu }$ . The total number of possible statuses of a child subdivision is thus

$$
S = \left\{ \begin{array} { l l } { { 1 , } } & { { \mathrm { f o r } \psi = 0 } } \\ { { \displaystyle { \prod _ { \nu = 0 } ^ { \psi - 1 } P _ { \nu } ^ { \phi _ { \nu } } } , } } & { { \mathrm { f o r } \psi \ge 1 } } \end{array} \right. .\tag{C.12}
$$

The pseudocode of the algorithm for the calculation of the status of a child subdivision is given in Fig. 14. The status variable is set to zero at the beginning. Then, a loop that covers all different types of piecewise linear branch models is started. In the mentioned example, these are the types of thyristor and saturable smoothing inductors. Within this loop, a second loop covers all instances of the present type. All of the statuses $\sigma _ { \nu \mu _ { \imath } }$ of the instances of piecewise linear branch models are successively polled, multiplied by the factor $n ,$ and added to . The factor gives the number of different possible statuses due to the ensemble of those piecewise linear branch models which have so far been dealt with by the algorithm. As the algorithm terminates, gives the status of the subdivision. The functioning can be verified by considering again the example of a subdivision with six instances of the thyristor type and one instance of a saturable smoothing inductor type. For the thyristor type, let instances 1 and 2 be conducting and instances 0, 3, 4, and 5 be blocking. Then, , , , , , and

$$
{ \begin{array} { r l } & { n : = 1 ; s : = 0 } \\ & { { \mathrm { f o r ~ } } \nu : = 0 { \mathrm { ~ t o ~ } } \psi - 1 { \mathrm { ~ d o } } } \\ & { { \mathrm { ~ f o r ~ } } \mu _ { \nu } : = 0 { \mathrm { ~ t o ~ } } \phi _ { \nu } - 1 { \mathrm { ~ d o } } } \\ & { \qquad s : = s + n \sigma _ { \nu \mu _ { \nu } } } \\ & { \qquad n : = n P _ { \nu } } \end{array} }
$$

Fig. 14. Algorithm for the calculation of the status of a child subdivision.

Step 1: Calculate nodal voltages: $\begin{array} { r } { \pmb { Y } _ { \mathrm { d d } } ^ { \subset } \pmb { v } _ { \mathrm { d } } ^ { \subset } = \pmb { j } _ { \mathrm { d } } ^ { \subset } - \pmb { Y } _ { \mathrm { d e } } ^ { \subset } \pmb { v } _ { \mathrm { e } } ^ { \subset } - \pmb { Y } _ { \mathrm { d t } } ^ { \subset } \pmb { v } _ { \mathrm { t } } ^ { \subset } } \end{array}$

Step 2:For all branches do: perform branch simulations.

Step 3:According to the status of the subdivision activate prestored $\mathbf { Y } _ { \mathrm { N } } ^ { \epsilon }$ $T _ { \mathrm { t d } } ^ { \mathrm { c } } , \ : Y _ { j _ { \mathrm { N } } v _ { \mathrm { e } } } ^ { \mathrm { c } ^ { \mathrm { c } } } , \ : Y _ { \mathrm { d e } } ^ { \mathrm { c } } , \ : Y _ { \mathrm { d t } } ^ { \mathrm { c } }$ ,and ${ \mathbfcal { L } } _ { \mathrm { d d } } ^ { \scriptscriptstyle \subset } , { \mathbfcal { U } } _ { \mathrm { d d } } ^ { \scriptscriptstyle \subset }$ in sparse-matrix storage structure.

Step 4: Advance the time dependent excitation sources.

Step 5:According to the sources and the status of the subdivision construct $j _ { \mathrm { d } } ^ { \scriptscriptstyle \subset } , j _ { \mathrm { t } } ^ { \scriptscriptstyle \subset }$

Step 6:Calculate the Norton source: $\pmb { j } _ { \mathrm { N } } ^ { \mathrm { c } } = \pmb { j } _ { \mathrm { t } } ^ { \mathrm { c } } - \pmb { T } _ { \mathrm { t d } } ^ { \mathrm { c } } \pmb { j } _ { \mathrm { d } } ^ { \mathrm { c } } - \pmb { Y } _ { j _ { \mathrm { N } } v _ { \mathrm { e } } } ^ { \mathrm { c } } \pmb { v } _ { \mathrm { e } } ^ { \mathrm { c } }$

Fig. 15. Course of actions in child simulation using GENE.

$\sigma _ { 0 5 } = 0$ . For the one saturable transformer, let $\sigma _ { 1 0 } = 2$ . Then, the status as obtained by the algorithm is

$$
s : = 2 ^ { 0 } \cdot 0 + 2 ^ { 1 } \cdot 1 + 2 ^ { 2 } \cdot 1 + 2 ^ { 3 } \cdot 0 + 2 ^ { 4 } \cdot 0 + 2 ^ { 5 } \cdot 0 + 2 ^ { 6 } \cdot 2 = 1 3 4 .
$$

Matrices $\pmb { L } _ { \mathrm { d d } } ^ { \subset }$ and $\pmb { U } _ { \mathrm { d d } } ^ { \subset }$ are calculated and stored in a sparse-matrix storage structure [15] for each status of a subdivision before the simulation starts. Furthermore, matrices $Y _ { \mathrm { d e } } ^ { \subset } , Y _ { \mathrm { d t } } ^ { \subset } , Y _ { \mathrm { t d } } ^ { \subset } , Y _ { \mathrm { t e } } ^ { \subset }$ , and $\pmb { Y } _ { \mathrm { t t } } ^ { \subset }$ are constructed for all statuses of the subdivision, and the miniature equivalent matrices $\pmb { Y } _ { \mathrm { N } } ^ { \subset }$ and the associated transfer matrices $T _ { \mathrm { t d } } ^ { \subset } , \dot { Y } _ { j _ { \mathrm { N } } { \pmb v } _ { \mathrm { e } } } ^ { \subset }$ are then calculated using (C.8), (C.10), and (C.11), respectively. For each subdivision status , the information given through matrices ${ \cal Y } _ { \mathrm { N } } ^ { \subset } , { \pmb T } _ { \mathrm { t d } } ^ { \subset } ,$ $Y _ { j _ { \mathrm { N } } v _ { \mathrm { e } } } ^ { \subset } , Y _ { \mathrm { d e } } ^ { \subset } , \dot { Y } _ { \mathrm { d t } } ^ { \subset } .$ , and $\pmb { L } _ { \mathrm { d d } } ^ { \subset } , \pmb { U } _ { \mathrm { d d } } ^ { \breve { \subset } }$ is then stored in fast accessible memory and so rapidly available during the simulation run.

3) Details of Child Simulation Process: The pseudocode of the child simulations, which are called in step 2 of the parent simulation process, is given in Fig. 15. Step 1 is concerned with the calculation of the unknown nodal voltages. In step 2, simulations of the branches are performed in the same way as done in Fig. 6 since no further nesting is assumed here within the child simulations. In step 3, refactorizations can be avoided by making use of the subdivision status indicator and access scheme. After advancing the time-dependent excitation sources in step $4 , j _ { \mathrm { d } } ^ { \subset }$ and $j _ { \mathrm { t } } ^ { \subset }$ are constructed in step 5, and the Norton source is calculated in step 6.

Step 6 is performed to provide information to the parent simulation process and, therefore, is different from step 6 of the parent simulation itself. For all other steps, the actions performed at both levels correspond to one another. Differences are mainly concerned with efficiency improvements due to the status indicator and access scheme.

4) Details of Efficiency Contributions of Subdivision Status Indicator and Access Scheme: When simulating electromagnetic transients, the computational speed of GENE exceeds the one that is obtained when just using node tearing. This can be recognized by performing an efficiency assessment of the child simulation process for a subdivision with $N _ { \mathrm { d } } ^ { \subset }$ dependent nodal voltages and $N _ { \mathrm { t } } ^ { \subset }$ terminal nodal voltages. The number of elementary multiplications involved in the matrix operations of the child simulation process at each time step is counted. No output variables are requested and the initial conditions considered at the branch level are assumed to be known. As a worst-case scenario, it is considered that the matrices are full and that a status change occurs. For the purpose of illustration, passive subdivisions are analyzed, i.e., excitation voltages are only associated with the parent simulation.

Under these assumptions, the solution of the voltages in step 1 of the child simulation in Fig. 15 amounts to $N _ { \mathrm { d } } ^ { \subset 2 } + N _ { \mathrm { d } } ^ { \subset } N _ { \mathrm { t } } ^ { \dot { \subset } }$ multiplications. In step $6 , N _ { \mathrm { d } } ^ { \mathrm { C } } N _ { \mathrm { t } } ^ { \mathrm { C } }$ multiplications are involved in the calculation of the Norton source. The multiplication count for GENE gives

$$
m _ { \mathrm { c h g } } ^ { \mathrm { G C } } = N _ { \mathrm { d } } ^ { \subset ^ { 2 } } + 2 N _ { \mathrm { d } } ^ { \subset } N _ { \mathrm { t } } ^ { \subset } .
$$

Without the status indicator and access scheme, additional operations need to be performed. The factorization of $\pmb { Y } _ { \mathrm { d d } } ^ { \subset }$ into upper and lower triangular matrices takes $( N _ { \mathrm { d } } ^ { \subset 3 } - N _ { \mathrm { d } } ^ { \subset } ) / 3$ multiplications. The calculations (C.10) involve $\mathrm { \ddot { N } _ { d } ^ { C 2 } } N _ { \mathrm { t } } ^ { \breve { C } }$ multiplications, and (C.8) is accomplished through $N _ { \mathrm { d } } ^ { \breve { \subset } } N _ { \mathrm { t } } ^ { \breve { \subset } 2 }$ multiplications. The total multiplication count for diakoptics alone then gives

$$
\begin{array} { r l } & { m _ { \mathrm { c h g } } ^ { \mathrm { D C } } = \left( N _ { \mathrm { d } } ^ { \mathrm { C } ^ { 3 } } - N _ { \mathrm { d } } ^ { \mathrm { C } } \right) \bigg / 3 + N _ { \mathrm { d } } ^ { \mathrm { C } ^ { 2 } } } \\ & { \qquad + N _ { \mathrm { d } } ^ { \mathrm { C } ^ { 2 } } N _ { \mathrm { t } } ^ { \mathrm { C } } + N _ { \mathrm { d } } ^ { \mathrm { C } } N _ { \mathrm { t } } ^ { \mathrm { C } ^ { 2 } } + 2 N _ { \mathrm { d } } ^ { \mathrm { C } } N _ { \mathrm { t } } ^ { \mathrm { C } } . } \end{array}
$$

When factorizations are to be performed as a result of status changes, the number of multiplications rises with the cube of the number of nodes with unknown nodal voltages, i.e., with $N _ { \mathrm { d } } ^ { \subset 3 }$ in the count of $m _ { \mathrm { c h g } } ^ { \mathrm { D C } }$ . This is not the case for GENE as evidenced by $m _ { \mathrm { c h g } } ^ { \mathrm { G C } }$ . In fact, in GENE, the multiplication count does not change with status changes but remains constant. This makes the method suitable for real-time applications where a constant computational effort at any time step is desired.

## REFERENCES

[1] H. W. Dommel, “Digital computer solution of electromagnetic transients in single- and multiphase networks,” IEEE Trans. Power App. Syst., vol. PAS-88, no. 4, pp. 388–399, Apr. 1969.

[2] V. R. Dinavahi, M. R. Iravani, and R. Bonert, “Real-time digital simulation of power electronic apparatus interfaced with digital controllers,” IEEE Trans. Power Del., vol. 16, no. 4, pp. 775–781, Oct. 2001.

[3] B. K. Johnson, “Benchmark systems for simulation of TCSC and SVC,” in Proc. IEEE Power Eng. Soc. Winter Meeting, New York, Jan. 2002, pp. 484–487.

[4] N. D. Hatziargyriou and A. P. S. Meliopoulos, “Distributed energy sources: technical challenges,” in Proc. IEEE Power Eng. Soc. Winter Meeting, New York, Jan. 2002, pp. 1017–1022.

[5] F. Katiraei, M. R. Iravani, and P. W. Lehn, “Micro-grid autonomous operation during and subsequent to islanding process,” IEEE Trans. Power Del., vol. 20, no. 1, pp. 248–257, Jan. 2005.

[6] D. A. Woodford, A. M. Gole, and R. W. Menzies, “Digital simulation of DC links and AC machines,” IEEE Trans. Power App. Syst., vol. PAS-102, no. 6, pp. 1616–1623, Jun. 1983.

[7] J. Mahseredjian, S. Lefebvre, and D. Mukhedkar, “Power converter simulation module connected to the EMTP,” IEEE Trans. Power Syst., vol. 6, no. 2, pp. 501–510, May 1991.

[8] S. Acevedo, L. R. Linares, J. R. Martí, and Y. Fujimoto, “Efficient HVDC converter model for real time transients simulation,” IEEE Trans. Power Syst., vol. 14, no. 1, pp. 166–171, Feb. 1999.

[9] R. W. Hamming, Numerical Methods for Scientists and Engineers. New York: McGraw-Hill, 1962.

[10] K. Strunz, X. Lombard, O. Huet, J. R. Martí, L. Linares, and H. W. Dommel, “Real time nodal-analysis-based solution techniques for simulations of electromagnetic transients in power electronic systems,” in Proc. 13th Power System Computation Conf. (PSCC), Trondheim, Norway, Jun. 1999, pp. 1047–1053.

[11] K. Strunz, L. R. Linares, J. R. Martí, O. Huet, and X. Lombard, “Efficient and accurate representation of asynchronous network structure changing phenomena in digital real time simulators,” IEEE Trans. Power Syst., vol. 15, no. 2, pp. 586–592, May 2000.

[12] K. Strunz, “Flexible numerical integration for efficient representation of switching in real time electromagnetic transients simulation,” IEEE Trans. Power Del., vol. 19, no. 3, pp. 1276–1283, Jul. 2004.

[13] K. L. Lian and P. W. Lehn, “Real-time simulation of voltage source converters based on time average method,” IEEE Trans. Power Syst., vol. 20, no. 1, pp. 110–118, Feb. 2005.

[14] W. F. Tinney and J. W. Walker, “Direct solutions of sparse network equations by optimally ordered triangular factorization,” Proc. IEEE, vol. 55, no. 11, pp. 1801–1809, Nov. 1967.

[15] I. S. Duff, A. M. Erisman, and J. K. Reid, Direct Methods for Sparse Matrices. Oxford: Oxford Univ. Press, 1986.

[16] L. O. Chua and P.-M. Lin, Computer Aided Analysis of Electronic Circuits: Algorithms and Computational Techniques. Englewood Cliffs, NJ: Prentice-Hall, 1975.

[17] J. Stoer and R. Bulirsch, Introduction to Numerical Analysis, 2nd ed. New York: Springer-Verlag, 1992.

[18] N. Watson and J. Arrillaga, Power Systems Electromagnetic Transients Simulation. London: Inst. Elect. Eng., 2003.

[19] G. Kron, Tensor Analysis of Networks. New York: Wiley, 1939.

[20] B. W. Kernighan and D. M. Ritchie, The C Programming Language, 2nd ed. Englewood Cliffs, NJ: Prentice-Hall, 1988.

[21] J. M. Undrill and H. H. Happ, “Automatic sectionalization of power system networks for network solution,” IEEE Trans. Power App. Syst., vol. PAS-90, no. 1, pp. 46–52, Jan. 1971.

[22] M. R. Irving and M. J. H. Sterling, “Optimal network tearing using simulated annealing,” Proc. Inst. Elect. Eng., vol. 137-C, no. 1, pp. 69–72, Jan. 1990.

[23] O. Ruhle, Echtzeitsimulation schneller transienter Vorgänge mit Hilfe von Parallelrechnern. Düsseldorf, Germany: VDI Verlag, 1994.

[24] T. Kailath, Linear Systems. Englewood Cliffs, NJ: Prentice-Hall, 1980.

[25] CIGRE Working Group 14.02 (Control in HVDC Systems) of Study Committee 14, “The CIGRE HVDC benchmark model—a new proposal with revised parameters,” Electra, no. 157, pp. 60–66, Dec. 1994.

![](images/7f9d0cac9cd7291cf5408bd3dbddb482434b8de05c346dded84da74ac0de0196.jpg)

Kai Strunz received the Dipl.-Ing. degree in electrical and electronic engineering and the Dr.-Ing. degree (Hons.) from the Faculty of Physics and Electrical Engineering of the University of Saarland, Saarbrücken, Germany, in 1996 and 2001, respectively.

Seattle.

From 1995 to 1997, he was with Brunel University, London, U.K. From 1997 to 2002, he was with the Division Recherche et Développement of Electricité de France (EDF), Paris, France. In 2002, he became Assistant Professor with the University of Washington,

Dr. Strunz received the Dr.-Eduard-Martin Award from the University of Saarland in 2002, the National Science Foundation (NSF) CAREER Award in 2003, and the Outstanding Teaching Award from the Department of Electrical Engineering of the University of Washington in 2004. He is the Convener of CIGRE Task Force C6.04.02 on computational tools for the study of distributed energy resources. In 2005, he was Advisor to the University of Washington student team that designed a next-generation hydrogen power park and received the honorable mention award from the National Hydrogen Association.

![](images/cc8f5ae996fdff065d8da75630bdda5b36050ac72eac38b41d466e159c25f3e0.jpg)

Eric Carlson studies electrical engineering at the University of Washington, Seattle.

His research in power systems simulation has been supported through an award from the National Science Foundation.