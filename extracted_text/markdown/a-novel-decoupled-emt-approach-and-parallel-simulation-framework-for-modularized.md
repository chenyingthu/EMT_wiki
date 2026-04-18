# A Novel Decoupled EMT Approach and Parallel Simulation Framework for Modularized Solid-State Transformers

Moke Feng , Chenxiang Gao , Jianzhong Xu , Senior Member, IEEE, Chengyong Zhao, Senior Member, IEEE, and Gen Li , Senior Member, IEEE

Abstract—Electromagnetic transient (EMT) modeling for the modularized solid-state transformer (MSST) faces critical difficulties because the dynamics of the complex-structured submodules, which contain dual active bridges (DAB) and multiple active bridges (MAB), are hard to be described in analytical formulas. Existing models have problems of a narrow dynamic frequency band, insufficient simulation accuracy, or are unable to operate under fast transients. This paper proposes a parallel simulation framework for MSST that preserves the original model’s broadband characteristics and remarkably improves the simulation efficiency. The main novelty towards previous work is the detailed modeling of the multi-winding transformer, the decoupled modeling of the submodules, and the parallel design of simulation processes. Finally, the proposed framework is verified through the accuracy and efficiency analysis carried out in PSCAD/EMTDC. The simulation results verify that the proposed framework has excellent accuracy and time efficiency.

Index Terms—Electromagnetic transient modeling, modularized solid-state transformer (MSST), multiple active bridge (MAB), decoupled modeling, parallel simulation framework.

## I. INTRODUCTION

OLID-STATE transformer (SST), also called as power electronic transformer (PET), can interconnect systems with different voltage levels and achieve multi-directional power flow control [1], [2], [3], [4]. Due to the modular design, the modularized SST (MSST) can be used in high voltage and high power applications [5], [6]. MSST would be effective equipment to link the transmission system and distribution network [7], [8], [9].

The multiple active bridge (MAB)-based MSST has higher power density, less transformers and submodules, and higher flexibility than the dual active bridge (DAB)-based MSST. Intensive studies of the topology and control sheme of MAB-based MSST have been made in recent years [10]. Fig. 1(a) illustrates a cascaded H-bridge MAB MSST (CHB-MAB-MSST) whose technology readiness has been validated by the successful installation in Hebei Province, China [11].

The submodule of this novel MSST integrates the three-phase input ports to a multi-winding transformer. Consequently, the number of submodule is significantly reduced, and the H-bridges [DC-AC in Fig. 1(b)] in the three phases can use the same triggering signals to simplify the control scheme.

However, the complex structure and control priciples make it difficult to analyze the dynamic behaviors of PETs:

1) Difficult to obtain an accurate analytical expression of MSST: The submodule of the MSST contains a large number of non-linear power electronic switches (IGBTs and diodes), capacitors, inductors, and AC transformers, which will generate a large-scale state equation [12], [13]. It is difficult to obtain an accurate analytical expression in the wide frequency band.

2) Complex structure results in a slow simulation speed: Another way to analyze the dynamics in the wide frequency band is to carry out electromagnetic transient (EMT) simulations [14], [15]. However, the node admittance matrix of MSST is very large. Time-domain simulations using detailed models will be very time-consuming. A simulation of several seconds would take hours, even days, which is not suitable for practical use.

3) High operation frequency requires a small simulation time-step: The simulation speed is limited by the frequency of the AC transformer in submodules. To realize DC-DC conversion, the DC voltage is transformed into high-frequency square waves by the highfrequency AC transformer [16]. The carrier wave frequency is 1–20 kHz, requiring a small simulation timestep of 1.25 to 25 µs (assuming 40 samplings per cycle). For numerical stability and accuracy, the time-step should be minor. This will increase the computation burden.

To address the above challenges, different modeling methods have been proposed:

![](images/18909e94be7c788b7768cac07e7ccf1ac59f88871d2151615a428325199a072e.jpg)  
Fig. 1. Configuration of the CHB-MAB-MSST: (a) Topology; (b) submodule structure.

## A. Average Value Models

References [17], [18], [19], [20] propose average value models (AVM) for MSST. These models greatly simplify the circuit, and ignore the high-frequency switching actions and capacitor ripples. Therefore, it is easy to obtain MSST’s analytical expression in time-domain. AVMs are sufficient in system-level simulations wherein detailed dynamics of devices are not to be concerned. The AVMs will be inaccurate when the operation state or external environment changes and cannot be used for fault analysis.

## B. High-Accuracy and High-Speed Equivalent Models

Without relying on the analytical solution of the MSST, references [23], [24], [25], [26], [27] propose the high-accuracy and high-speed equivalent model (HEM) for MSSTs. This model is based on the work from Kai Strunz [28], where the Ward equivalent eliminates the nodes inside the circuit. Taking the advantage of the linearization characteristics inherent in EMT simulation, the circuit is dynamically simplified as time-varying Norton equivalents in each time-step. Since the HEM only produces minor interpolation errors when generating the associated discrete circuits (ADC) [29], they are as accurate as the detailed model (DM). Compared to AVM, HEM is slower but much more accurate and can be applied in both steady-state operations and fault conditions.

Considering the accuracy and acceleration capability, HEM is a potential scheme to solve the modeling problems of MSST. However, existing HEMs still have some shortcomings. In [23], the submodule is decoupled at transformer windings. The winding voltages are replaced with the history voltage value of the last step. However, the winding voltages are square waves. Therefore, the replacement will produce errors when voltage jumps, which will cause numerical instability and loss of accuracy. In [24], the submodule is modeled as a whole without decoupling. The final equivalent circuit is still complex, and the simulation burden is still heavy. Moreover, implementing HEM into MSST is still challenging because the programming is sophisticated and lacks a general framework.

To address the issues, this paper follows the principle of HEM and proposes a novel decoupled EMT modeling approach for parallel simulation of modularized SSTs. The proposed approach is verified through the engineering project in Hebei Province, China. The highlights of this paper include:

1) Detailed modeling of the multi-winding transformer: This paper gives a detailed modeling and calculation processes for a multi-winding transformer using the unified magnetic equivalent circuit (UMEC) method, which can reflect the saturation of the iron core and complex electromagnetic coupling characteristics of the transformer.

2) Decoupled modeling of MSST: A cut-set-based decoupling method is proposed, which can simplify the circuit of the power module. The bridge equivalent is consequently simplified. The decoupled equivalent circuit makes the simulation speed much faster than DM.

3) Parallel simulation framework for MSST: A simulation framework using parallel calculation is proposed. In addition to accomplishing the calculations of the UMEC transformer model, the submodule equivalents are assigned to different CPU cores to realize parallel computation. This further increases the simulation speed.

This paper is arranged as follows: Section II presents the UMEC modeling theory of multi-winding transformers. Section III proposes the decoupled modeling method of the submodule and gives a parallel simulation framework for MSST. Section IV applies the detailed modeling processes to the CHB-MAB-MSST. Section V shows the simulation results in terms of accuracy and time efficiency to validate the proposed method. Section VI concludes the paper.

## II. UNIFIED MAGNETIC EQUIVALENT CIRCUIT OF MULTI-WINDING TRANSFORMER

The multi-winding transformer is an essential interface in MSST submodules that undertakes the vital task of power transfer. A multi-winding AC transformer is a crucial device to realize voltage level conversion and power transfer inside the submodule. The unified magnetic equivalent circuit (UMEC)

![](images/58e750d61494cba949fce5755ce53f3794c3c9813f103df7b2a5ef089161b534.jpg)  
Fig. 2. Geometry of the multi-winding transformer.

![](images/179a5e159f9e00488fc01d3b2c53550210484aea162a002a62ecd540444ecb2c.jpg)  
Fig. 3. UMEC of the multi-winding transformer.

![](images/8c75ef8f1140503d0d7969edf3759e10b0dd815e68f3e3a78c67701fb1866dc9.jpg)  
Fig. 4. The m.m.f relationship in the limb.

modeling method takes the physical structure, saturation characteristic and magnetic decoupling mechanism of the transformer into account, which makes it capable of reflecting the complex characteristics of a real transformer. The UMEC modeling of the multi-winding transformer is presented as follows.

Fig. 2 shows a 6-winding transformer with wounded windings on a common iron core. For each winding $w _ { i } ( i = 1 , 2 , 3$ X), the core flux through $w _ { i }$ is $\Phi _ { i } ,$ the leakage flux is $\Phi _ { l k i } ,$ and the direction of winding voltage $\nu _ { i }$ and current $i _ { i }$ is specified in the figure.

The magnetic circuit of the multi-winding transformer is composed of the core fluxes and leakage fluxes, as shown in Fig. 3, where $P _ { i }$ is the permeance of limb $i ,$ and $P _ { l k i }$ is the leakage permeance of limb i.

Fig. 4 illustrates the geometry of the limb, where the limb length is $L _ { i } ,$ the cross-sectional area of the limb is $A _ { i } ,$ and the number of turns is Ni. Bi and $H _ { i }$ are the magnetic induction intensity and magnetic field intensity generated by the winding currents. µ is the magnetic permeability of the iron core. Combining Figs. 2, 3, and 4, the magnetic circuit and electric circuit is related through flux Φ and winding current $i ,$ which is derived as follows.

The relationship between the magnetomotive force (m.m.f) $M _ { i } ,$ , m.m.f drop $M _ { d i }$ and total m.m.f drop $M _ { t d i }$ is:

$$
M _ { i } - M _ { d i } = M _ { t d i } = M _ { f r o m } - M _ { t o }\tag{1}
$$

where

$$
M _ { i } = N _ { i } i _ { i }\tag{2}
$$

$M _ { f r o m }$ and $M _ { t o }$ are the magnetic potentials of the terminals of the limb.

$\Phi _ { i }$ is influenced by the limb permeances:

$$
\Phi _ { i } = P _ { i } M _ { d i } = P _ { i } ( N _ { i } i _ { i } - M _ { t d i } )\tag{3}
$$

where

$$
\left\{ \begin{array} { l l } { P _ { i } = \frac { \Phi _ { i } } { H _ { i } L _ { i } } = \frac { \Phi _ { i } \mu } { B _ { i } L _ { i } } = \frac { \mu _ { i } A _ { i } } { L _ { i } } } \\ { \mu _ { i } = \frac { B _ { i } } { H _ { i } } } \end{array} \right.\tag{4}
$$

$P _ { i }$ is the limb permeance of limb $i , \mu$ is the magnetic permeability of the limb, which is a time-varying value determined by the instantaneous magnetic induction intensity $B _ { i }$ and magnetic field intensity $H _ { i }$ . The non-linear relationship between $B _ { i }$ and $H _ { i }$ is given in the manufacturer’s manual of the iron core.

Considering all the circuits in the magnetic circuit, and rewrite (3) in matrix form:

$$
\Phi _ { ( b \times 1 ) } = P _ { ( b \times b ) } \left( N _ { ( b \times b ) } i _ { ( b \times 1 ) } - M _ { t d ( b \times 1 ) } \right)\tag{5}
$$

In (5), the subscripts of each matrix indicate the dimension of the matrix. Particularly, P and N are diagonal matrices. Φ, i, and $M _ { t d }$ are column vectors.

According to Fig. 3, write the node-line coincidence matrix $\boldsymbol { A } _ { ( b \times X ) }$ , and obtain:

$$
A _ { ( X \times b ) } ^ { T } \Phi _ { ( b \times 1 ) } = \mathbf { 0 } _ { ( X \times 1 ) }\tag{6}
$$

where X is the total number of windings, (6) means the sum of branch fluxes is 0.

Moreover, considering (1) and the magnetic potentials of the nodes $M _ { n o d e }$ , the m.m.f relationship is written as:

$$
A _ { ( b \times X ) } M _ { n o d e ( X \times 1 ) } = M _ { t d ( b \times 1 ) }\tag{7}
$$

Combing (5), (6) and (7), the relationship between fluxes Φ and terminal current i is obtained as:

$$
\Phi _ { ( b \times 1 ) } = Q _ { ( b \times b ) } P _ { ( b \times b ) } N _ { ( b \times b ) } \dot { \imath } _ { ( b \times 1 ) }\tag{8}
$$

where

$$
Q _ { ( b \times b ) } { = } E _ { ( b \times b ) } - P _ { ( b \times b ) } A _ { ( b \times X ) } \biggl ( A _ { ( X \times b ) } ^ { T } P _ { ( b \times b ) } A _ { ( b \times X ) } \biggr ) ^ { - 1 } A _ { ( X \times b ) } ^ { T }
$$

In (9), E is an identity matrix.

(9)

Partitioning (8) into limb branch associated blocks and leakage branch associated blocks, the limb fluxes and leakage fluxes canb be obtained:

$$
\left\{ \begin{array} { l l } { \Phi _ { w \left( a \times 1 \right) } = Q _ { w w \left( a \times a \right) } P _ { w \left( a \times a \right) } N _ { w \left( a \times a \right) } i _ { w \left( a \times 1 \right) } } \\ { \Phi _ { k \left( a \times 1 \right) } = Q _ { k w \left( a \times a \right) } P _ { w \left( a \times a \right) } N _ { w \left( a \times a \right) } i _ { w \left( a \times 1 \right) } } \end{array} \right.\tag{10}
$$

where the subscript w refers to the windings of limb branches, and k corresponds to leakage branches.

![](images/2d9e5152468be42009cba53e5f91515d52375f9218fd7b8b2b40a4f0baf0496e.jpg)  
Fig. 5. EC of multi-winding transformer when X = 2, 3, 4, 6: (a) X = 2; (b) X = 3; (c) X = 4; (d) X = 6.

Also, the winding voltage v and limb flux $\Phi _ { w }$ satisfy:

$$
{ \pmb v } _ { ( a \times 1 ) } = { \pmb N } _ { ( a \times a ) } \frac { d { \pmb \Phi } _ { w ( a \times 1 ) } } { d t }\tag{11}
$$

Discretize (11) with the trapezoidal integration method:

$$
\Phi _ { w } ( t ) = \Phi _ { w } ( t - \Delta t ) + \frac { \Delta t } { 2 } N ^ { - 1 } \left[ { \pmb v } ( t ) + { \pmb v } ( t - \Delta t ) \right]\tag{12}
$$

Combining (10) and (12), the relationship between v and i is derived:

$$
\pmb { i } _ { w } ( t ) = \pmb { Y } _ { w w } \pmb { v } ( t ) + \pmb { J } _ { w } ( t )\tag{13}
$$

where

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { Y _ { w w } = \frac { \Delta t } { 2 } ( Q _ { w w } P _ { w } N _ { w } ) ^ { - 1 } N _ { w } ^ { - 1 } } \\ { J _ { w } = \frac { \Delta t } { 2 } N _ { w } ^ { - 1 } ( Q _ { w w } P _ { w } N _ { w } ) ^ { - 1 } v ( t - \Delta t ) + i _ { w } ( t - \Delta t ) } \end{array} \right. } \end{array}\tag{14}
$$

According to (13), the equivalent circuit of the transformer is constructed. The structure of equivalent circuits is shown in Fig. 5 when X = 2, 3, 4, 6. Each winding refers to a Nortan branch with a current source and a conductor. Other branches only contain conductors.

Fig. 6 shows the calculation process of the UMEC model of multi-winding transformer: $\mathbf { A } \mathbf { t } \ t = 0$ , read the non-linear B-H curve from a curve file, and initialize the winding voltage, current, and fluxes to 0. Then, within each time-step, measure the winding currents $\pmb { I } _ { \mathrm { w } }$ to obtain the winding fluxes $\Phi _ { w }$ and calculate leakage fluxes $\Phi _ { l k } . \mathrm { A t }$ last, calculate $P , Q , Y _ { w w } ,$ and $J _ { w w }$ in order, and obtain the equivalent circuit of the UMEC model.

## III. DECOUPLED MODELING AND PARALLEL SIMULATION FRAMEWORK FOR MSST

## A. Decoupled Modeling Method for Submodule Based on Cut-Set Matrix

The UMEC transformer model in Section II is a coupled model where the winding current $\pmb { i } _ { w } ( \mathbf { t } )$ is associated with all winding voltages $\nu _ { w } ( \mathfrak { t } )$ . The coupling characteristics result in a complex equivalent circuit and considerable computation. In power electronic simulations, the winding voltage does not change fast between neighboring time-steps. Therefore, they can be replaced with the history values from the last time-step. For winding i, replace $\nu _ { j } ( j \neq i )$ with history values:

![](images/4d5730e9c054584f6b00d86e2eaf39edb7a18e1a6e5fdaef3b03ac6b5fee650e.jpg)  
Fig. 6. Calculation process of transformer’s UMEC model.

$$
\begin{array} { r l } & { \dot { \iota } _ { w } ( t ) = \left[ \begin{array} { c c c c } { y _ { 1 1 } } & { 0 } & { \cdots } & { 0 } \\ { 0 } & { y _ { 2 2 } } & { \cdots } & { 0 } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 0 } & { 0 } & { \cdots } & { y _ { X X } } \end{array} \right] v _ { w } ( t ) } \\ & { \qquad + \left[ \begin{array} { c c c c } { 0 } & { y _ { 1 2 } } & { \cdots } & { y _ { 1 X } } \\ { y _ { 2 1 } } & { 0 } & { \cdots } & { y _ { 2 X } } \\ { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { y _ { X 1 } } & { y _ { X 2 } } & { \cdots } & { 0 } \end{array} \right] v _ { w } ( t - \Delta t ) + J _ { w } ( t ) } \\ & { \qquad \stackrel { \mathrm { ( i f ~ } } { = } Y _ { D w } v _ { w } ( t ) + J _ { D w } ( t ) } \end{array}\tag{5}
$$

where $y _ { i j } ( i , j = 1 , 2 , 3 , . . . , X )$ are elements of $Y _ { w w } .$

The corresponding equivalent circuit becomes a combination of independent circuits, as shown in Fig. 7(X = 4).

However, directly decoupling the transformer will lead to numerical instabilities and less accuracy. In MSSTs, the voltage of the submodule capacitor varies more smoothly than the transformer port. The model’s performance will be improved if the submodule is decoupled from the capacitor link. Following this idea, a cut-set-matrix-based decoupling method is proposed in this section.

![](images/471f79cd978e8030122309eca453d621c1e887121f7b1ea792853374d1187b3b.jpg)  
Fig. 7. Decoupled equivalent circuit of a four-winding transformer.

![](images/4c599eaf3cea3a31ddbec131f856cbb2bb17daedf96ad14befbc2d7618a233ff.jpg)  
Fig. 8. Circuit and ADC of DAB submodule: (a) Original circuit; (b) ADC.

![](images/167b68926afa3768f42d12fda8082a86431038f72f8b17efac89c89eb6c12418.jpg)  
Fig. 9. Circuit and companion circuit of CHB-DAB submodule.

For simplicity and generality, this method is illustrated with a DAB-based submodule, as depicted in Fig. 8(a). Utilizing the UMEC approach and ADC principle, the circuit is transformed into its ADC where the AC transformer, capacitors and IGBT/Diodes are distretized as Norton branches, as shown in Fig. 8(b).

The directed graph corresponding to Fig. 8(b) is drawn in Fig. 9, where the solid lines represent twigs, and the dotted lines represent links. $f _ { 1 }$ to $f _ { \mathrm { N } }$ are fundamental cuts (f-cuts).

Write the cut set matrix $\varrho$ following Fig. 9. The rows of Q represent f-cuts. The columns represent edges (twigs and links are collectively called edges). The element in $\varrho$ is

defined as:

$$
Q _ { i j } =
$$

⎧1, if edge j is in the same direction as f cut i ⎨ 1, if edge j is in the opposite direction of f  cut i ⎩0, if edge j is not included in f cut i

(16)

According to Kirchhoff’s voltage law (KVL) and Kirchhoff’s current law (KCL):

$$
Q Y _ { e } Q ^ { T } U _ { t } = Q \left( I _ { s } + I _ { e c } \right) - Q Y _ { e } U _ { s }\tag{17}
$$

where $Y _ { e }$ is a diagonal matrix that contains the edge admittances in Fig. $9 . U _ { t }$ is the voltage vector of all twigs. $. I _ { s }$ and $U _ { \varepsilon }$ are current and voltage sources of edges, $\pmb { I _ { e c } }$ is the external twig current.

The Thevenin branches can be transformed into Norton branches, so $U _ { s } = 0$ . Rewrite (17) in partitioned matrix form:

$$
\left[ \begin{array} { c c } { Y _ { Q 1 1 } } & { Y _ { Q 1 2 } } \\ { Y _ { Q 2 1 } } & { Y _ { Q 2 2 } } \end{array} \right] \left[ \begin{array} { c c } { U _ { t E X } } \\ { U _ { t I N } } \end{array} \right] = \left[ \begin{array} { c c } { I _ { s E X } } \\ { I _ { s I N } } \end{array} \right] + \left[ \begin{array} { c c } { I _ { c E X } } \\ { \mathbf { 0 } } \end{array} \right]\tag{18}
$$

where

$$
\left[ \begin{array} { l l } { \pmb { Y } _ { Q 1 1 } } & { \pmb { Y } _ { Q 1 2 } } \\ { \pmb { Y } _ { Q 2 1 } } & { \pmb { Y } _ { Q 2 2 } } \end{array} \right] = \pmb { Y } _ { e } \pmb { Q } ^ { T }\tag{19}
$$

The subscript EX indicates the external twigs, and IN indicates internal twigs.

It is noted that $\pmb { U } _ { t E X }$ is the external port voltage of the circuit, and $I _ { \mathrm { s } E X }$ is the port current. The relationship between $\pmb { U } _ { t E X }$ and $I _ { \mathrm { s } E X }$ is obtained from (18):

$$
\begin{array} { r l } & { \left( { { { \cal Y } } _ { Q 1 1 } } - { { \cal Y } } _ { Q 1 2 } { { \cal Y } } _ { Q 2 2 } ^ { - 1 } { { \cal Y } } _ { Q 2 1 } \right) { { \cal U } } _ { t E X } } \\ & { = { { \cal I } } _ { e c E X } + \left( { { { \cal I } } _ { s E X } } - { { \cal Y } } _ { Q 1 2 } { { \cal Y } } _ { Q 2 2 } ^ { - 1 } { { \cal I } } _ { s I N } \right) } \end{array}\tag{20}
$$

Define

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { Y _ { r e d u c e d } = Y _ { Q 1 1 } - Y _ { Q 1 2 } Y _ { Q 2 2 } ^ { - 1 } Y _ { Q 2 1 } } \\ { I _ { s r } = I _ { s E X } - Y _ { Q 1 2 } Y _ { Q 2 2 } ^ { - 1 } I _ { s I N } } \end{array} \right. } \end{array}\tag{21}
$$

Equation (20) indicates an equivalent circuit of Fig. 8(a). In view of the external circuit, it has the same dynamic characteristics as Fig. 8. This is because they always have identical feedback $U _ { t E X }$ when the input $I _ { \mathrm { s } E X }$ is the same.

Replace the voltage values with history values in (20). The transformer and H-bridges are decoupled at the capacitor link. This method is also applicable to arbitrary multi-winding transformers.

## B. Parallel Simulation Framework for MSST

After using the modeling method introduced in Sections II and III, the time-varying Norton equivalent circuit of MSST is computed in every time-step. The simulation framework within a time-step is shown in Fig. 10.

a) Calculation of UMEC transformer model: measure the winding current $i _ { w } ,$ which is zero at $t = 0$ or is obtained from the last time-step. Calculate the transformer parameters $Y _ { w w }$ and $J _ { w w }$ in the order illustrated in Fig. 6.

![](images/f6836c98abdd4ce20077612d6dcd216db164398d38a4087f1d474cc8a9e92ccc.jpg)  
Fig. 10. Parallel simulation framework for SST.

b) Decoupled modeling for submodule at capacitor links: Utilize the cut-set-based decoupling method, and decouple the submodule circuit at capacitor links.

c) Node elimination of the first AC-DC link: Every branch in the decoupled circuit, which contains H-bridge branches and UMEC branches, is equivalent to a simple Norton branch with the equivalent principle of the Norton circuit.

d) Calculation of bridge equivalents: The submodule equivalent circuits are connected in cascade to produce the bridge equivalent circuit.

e) EMT solving of the simulation tool: The equivalent circuit is solved in the EMT simulation tool to obtain the voltages and currents of the entire simulated system.

f) Update of history variables: The capacitor and transformer winding voltages/currents are required to update the history current source values. In the simulation tools, the port voltages of the bridges can be measured directly. Then, through an opposite path of the equivalent process, the needed voltages/currents are obtained.

It is noted that the equivalent process and update process of each submodule does not rely on the information of other submodules, Steps a)-c) and f) are operated in parallel.

## IV. MODELING PROCESS FOR THE CHB-MAB-MSST

In this section, the proposed method is applied to the CHB-MAB-MSST described in Section I, and the modeling process of CHB-MAB-MSST is depicted in Figs. 11–14. Fig. 11 is the ADC of the CHB-MAB-MSST submodule, in which the IGBT/Diode switches and capacitors are replaced with Norton equivalents. The four-winding transformer is modeled as UMEC equivalents.

In Fig. 12, the four-winding transformer and the DC-AC link are decoupled. Then, the single-port equivalent circuit of each phase is transformed into a Norton circuit.

In phases A, B, and C, the equivalent circuits of submodules are cascaded. The DC side equivalent circuits are connected in parallel. Finally, the bridge equivalent, a decoupled circuit with four separated Norton circuits, is obtained, as shown in Fig. 13.

![](images/b6181807dce855b78e177b882509a4438dddd817f2baa7cb72892bd379c5cd84.jpg)  
Fig. 11. ADC of CHB-MAB-MSST submodule.

![](images/41f1a27a623b0b13dff13794fdaf452c69984a0d799540302d40e6628e74738d.jpg)  
Fig. 12. Decoupling and node-shrinking of the submodule.

Referring to [24], the blocking circuits are added to the bridge equivalent circuits, as shown in Fig. 14. The equivalent circuits of the upper bridge and lower bridge are overlaid onto the external system for the EMT solution.

It is noted that the proposed model has full electrical interfaces to the external system. Therefore, when the external system changes (e.g., adding a battery in the DC stage or other power sources), the proposed model will not be affected.

## V. VALIDATION AND PERFORMANCE

The simulation results will show the effectiveness in modeling complex MSST and accelerating simulation speed of the proposed framework.

## A. Accuracy Test

In this section, the CHB-MAB-MSST with four submodules in each arm is established in PSCAD/EMTDC. The comparisons between the detailed model (DM) and the proposed equivalent model (EM) are given in terms of accuracy and simulation speed. The output power and voltage of MVAC, MVDC, and LVDC ports are ( 1.6 MW, 115 kV), (0.8 MW, 10 kV), and (0.8 MW, ±0.35 kV). The system parameters are shown in Table I.

![](images/7ae0b95e2013165890a52dd389d60c1a6ec43775bb76b0e6e62429f94fed66b6.jpg)  
Fig. 13. Modeling of bridges.

![](images/9d0042f28050ed817ac2b8a8ab2b5dd7f7a1368afe0ebff7a19c49b775632a8a.jpg)  
Fig. 14. Equivalent model with blocking circuits overlaid onto the external system.

The performance of the proposed model in terms of accuracy under different working conditions is tested. The working conditions are set as shown in Fig. 15:

For precise comparisons, the averaged relative error (ARE) between the reference solution s (the simulation result of DM) and the given solution ˜s (the simulation result of EM) is used, which is calculated as in (22):

$$
e ^ { 0 } / 0 = \frac { \sum _ { i = 1 } ^ { M } \left| \frac { { \bf s } _ { i } - \tilde { \bf s } _ { i } } { { \bf s } _ { i } } \right| \times 1 0 0 \% } { M }\tag{22}
$$

where e% is the ARE in percent, i is the number of sample points, and M is the total number of sample points.

The DC port voltages $V _ { \mathrm { M V D C } }$ and $V _ { \mathrm { L V D C } }$ are shown in Fig. 16. During the charging process, from t = 0 to t = 0.8 s, the MVDC voltage rises steadily to the set value of 20kV. ${ \bf A t } \ t = { \bf 0 . 8 \ s }$ , the MAB absorbs energy from MVDC capacitors and starts charging. At t = 1.0 s, the LVDC capacitors are fully charged, and their voltages rise to 0.75kV. During t = 1.0 s to 1.5 s, the system operates in a steady state. At t = 1.5 s, LVDC fault occurs, and LVDC voltage drop to zero immediately. It also causes fluctuation in the MVDC voltage. At t = 1.6 s, the LVDC fault is cleared, and the LVDC voltage recovers. At t = 2.0 s, MVDC fault occurs. Both MVDC and LVDC sides are blocked. Thus, the MVDC and LVDC side voltages drop to zero. At t = 2.1 s, the fault is cleared, and the system returns to a steady state. The $e \%$ of $V _ { \mathrm { M V D C } }$ and $V _ { \mathrm { L V D C } }$ are 0.07% and 0.79%, respectively.

TABLE I  
SYSTEM PARAMETERS OF THE CHB-MAB-MSST
<table><tr><td>Symbols</td><td>Parameter Description</td><td>Values</td></tr><tr><td> $N _ { \mathrm { P M } }$ </td><td>Number of PMs per arm</td><td>4</td></tr><tr><td> $X _ { \mathrm { A C t r } }$ </td><td>AC Transformer&#x27;s leakage inductance (p.u.)</td><td>0.15</td></tr><tr><td> $f _ { \mathrm { s y s } }$ </td><td>System fundamental frequency (Hz)</td><td>50</td></tr><tr><td> $V _ { \mathrm { L - L s y s } }$ </td><td>Line-to-line RMS voltage on AC grid side (kV)</td><td>115</td></tr><tr><td> $V _ { \mathrm { L - L v a l } }$ </td><td>Line-to-line RMS voltage on valve side (kV)</td><td>10.5</td></tr><tr><td> $S _ { \mathrm { t r } }$ </td><td>AC transformer&#x27;s rated capacity (MVA)</td><td>2.5</td></tr><tr><td> $V _ { \mathrm { { C l } } }$ </td><td>Rated capacitor Voltage in CHB side (kV)</td><td>5</td></tr><tr><td> $V _ { \mathrm { M V D C } }$ </td><td>MVDC rated output voltage (kV)</td><td>±10</td></tr><tr><td> $P _ { \mathrm { M V D C } }$ </td><td>MVDC rated output real power (MW)</td><td>0.8</td></tr><tr><td> $C _ { \mathrm { C H B } }$ </td><td>CHB side PM capacitance (μF)</td><td>1000</td></tr><tr><td> $R _ { \mathrm { M V D C } }$ </td><td>MVDC output load (Ω)</td><td>500</td></tr><tr><td> $S _ { \mathrm { t r \_ h f } }$ </td><td>Rated capacity of high-frequency transformers (MVA)</td><td>0.1875</td></tr><tr><td> $X _ { \mathrm { h f f r } }$ </td><td>High-frequency Transformer&#x27;s leakage inductance (p.u.)</td><td>0.188</td></tr><tr><td> $V _ { \mathrm { t r } 1 }$ </td><td>High-frequency Transformer&#x27;s CHB side voltage rating (kV)</td><td>5</td></tr><tr><td> $V _ { \mathrm { t r } 2 }$ </td><td>High-frequency Transformer&#x27;s MAB side voltage rating (kV)</td><td>0.75</td></tr><tr><td> $C _ { \mathrm { M A B } }$ </td><td>MAB side PM capacitance (μF)</td><td>3500</td></tr><tr><td> $V _ { \mathrm { L V D C } }$ </td><td>LVDC rated output DC voltage (kV)</td><td>0.75</td></tr><tr><td> $R _ { \mathrm { L V D C } }$ </td><td>LVDC output load (Ω)</td><td>0.703</td></tr></table>

![](images/b4d3b532bd8e734dc48d87fbc39019a01bc722d79740f5dc94dc452d69d43471.jpg)  
Fig. 15. The working condition flow of the accuracy test.

![](images/1feb1b371270c18c67d513bb47b6cd32c0d3dad5bf8919bd9b29faeadc38b8a4.jpg)  
(a)

![](images/0bd74f82d0b6bcc0fa84c3dab0a8d52a753a7e3d6fd84c304400d8b6195d9e5f.jpg)  
(b)

Fig. 16. Voltages of MVDC and LVDC ports: (a) MVDC voltage; (b) LVDC voltage.  
![](images/0418979f4658a095efec6575cfcaf99ad2d5d7476149bec1988421df7b9964f5.jpg)  
(a)

![](images/3d44e80b130e8d372dac146ba3b72a1fa950465017073042e0627256975349a5.jpg)  
(b)  
Fig. 17. Active power of MVDC and LVDC ports: (a) MVDC power; (b) LVDC power.

In the overall dynamic process, the active power of MVDC and LVDC ports agree well, as shown in Fig. 17. The e% of $P _ { \mathrm { M V D C } }$ and $P _ { \mathrm { L V D C } }$ are 0.39% and 0.93%, respectively.

The AC side dynamics of EM have an excellent fit with DM, as shown in Fig. 18. When MVDC fault occurs at $t = 2 . 0 \ : \mathrm { s } ,$ the CHB-MAB-MSST is blocked. The amplitude and phase of DM and EM agree well during steady-state and fault.

In [25], the authors proposed a modeling method for MSST using a non-decoupled equivalent circuit (EM2). Fig. 19 shows the comparison of the capacitor voltages of EM and EM2. The time-domain dynamics match well, which indicates that EM has as high accuracy as EM2 does, even though EM is a more simplified model.

![](images/53f1637195a5e8d8406a531b57648e6c8fc4e3104c6931e0fbdc93cb5ef8bf84.jpg)  
(a)

![](images/c491fadc4e8958025d2e7c446fa636d59658bcd126f282d5a5c3d1e65232523c.jpg)  
(b)

Fig. 18. Grid voltages and currents: (a) Voltages; (b) currents.  
![](images/602b978b28c4533dcf1105fff223ea88345079ec3cd3f98a59d6e3f0edaa9324.jpg)  
Fig. 19. Capacitor voltage comparison of EM and EM2.

TABLE II  
SIMULATION TIME OF DM AND EM
<table><tr><td>Number of modules</td><td> $t _ { \mathrm { D M } } ( \mathbf { s } )$ </td><td> $t _ { \mathrm { E M } } ( \mathrm { s } )$ </td><td> $F _ { \mathrm { s } }$ </td></tr><tr><td>4</td><td>674.23</td><td>150.56</td><td>4.48</td></tr><tr><td>8</td><td>3260.64</td><td>376.22</td><td>8.67</td></tr><tr><td>10</td><td>18653.46</td><td>463.67</td><td>40.23</td></tr><tr><td>20</td><td>256295.68</td><td>629.28</td><td>407.28</td></tr><tr><td>30</td><td>708231.55</td><td>745.25</td><td>950.33</td></tr></table>

## B. Simulation Speed Test

The simulation speed of DM and EM is tested. The simulation time is set to 1.5 s, and the time-step is $2 . 5 \mu \mathrm { s }$ . Table II shows the acceleration ability of EM, where tDM and tEM are CPU times measured by the inherent runtime tool in PSCAD/EMTDC. $F _ { \mathrm { s } }$ is the speedup factor defined as $F _ { \mathrm { s } } = t _ { \mathrm { D M } } / t _ { \mathrm { E M } }$

With the increase of modules, the simulation time of DM rises exponentially while EM rises linearly. EM considerably improves the simulation efficiency with low loss of accuracy. Although the accuracy is retained, EM has a final speedup factor of 950.33 over 738.05 of EM2, according to Table I. This means EM has more potential for modeling complicated-structured equipment.

## C. Performance Test

The bi-directional power flow capability, frequency adaptability and system disturbance test are carried out to test the performance of the model. Table III show the cases that the power flowing out of the port is positive.

TABLE III  
WORKING CONDITIONS FOR POWER FLOW CAPABILITY TEST
<table><tr><td></td><td> $P _ { \mathrm { L V D C } }$ </td><td> $P _ { \mathrm { M V D C } }$ </td><td> $\mathbf { \mathit { P } _ { M V A C } }$ </td></tr><tr><td>Condition 1</td><td>1.0MW</td><td>0.4MW</td><td>-1.4MW</td></tr><tr><td>Condition 2</td><td>-6.1MW</td><td>2.1MW</td><td>4.0MW</td></tr><tr><td>Condition 3</td><td>1.1MW</td><td>-5.1MW</td><td>4.0MW</td></tr></table>

![](images/a4b281e336273a929dfed23adf00a8d1a2998c0859efd49bf5202f05cceca502.jpg)  
Fig. 20. Power flow test of different conditions.

Simulation result in Fig. 20 show that regardless of the power flow direction, the proposed model is able to stably transmit power, and every port of it has the full ability to send or absorb power.

Frequency is an important parameter of MSST. It is not included in the mathematical derivation process and does not directly impact the accuracy of the model. However, frequency determines the maximum simulation step because the carrier wave in the PWM control loop needs a small enough time-step to reflect its high-frequency details.

Tests are designed that the frequency of the high-frequency transformer varies from 1 kHz to 10 kHz. Fig. 21 shows the CHB side capacitor voltage $U _ { \mathrm { C } }$ . With a frequency of 1–3 kHz and a simulation time-step of 2.5 $\mu \mathrm { s } ,$ EM is always accurate. Yet, at 5 kHz, $U _ { \mathrm { C } }$ has a large deviation. This is because that a time-step of 2.5 µs is not sufficient to reflect the details of a 5 kHz carrier wave in this MSST system. By changing the time-step to 1 µs, the simulation results are again precise at both 5 kHz and 10 kHz.

The simulation results indicate that the proposed model has a wide range of applicability of frequency. Theoretically, it works under any frequency value. However, the relationship between the simulation step and frequency should be considered when the frequency becomes high.

![](images/adb55c2982b29e71a0fe1e7f9b693cba9b48577a8143d3fafc4bfa4f6d360850.jpg)  
Fig. 21. Frequency adaptability tests.

![](images/e8445ac8b51d099f369d3ee09898a70eb1eb2d102f21c4d6f71d8a90c070aadd.jpg)  
Fig. 22. System level dynamics when under grid voltage sagging/swelling.

![](images/f34acfb7245d55e5670d6a0fe5d57fa88e5a1a44ae6dbcd688d2f52dae58a37e.jpg)  
Fig. 23. MVDC voltage and LVDC power change when LVDC load changing happens.

For the system-level dynamic performance, the grid voltage sagging/swelling and LVDC load changing are tested. $\mathrm { A t } t = 2$ s and 2.2 s, the AC grid has a 10% drop of the rated voltage and then a 10% increase of the rated voltage. The dynamics of EM are shown in Fig. 22. It is observed that when grid voltage sagging/swelling happens, EM has the same system-level dynamics as DM.

For DC side system-level dynamics, set LVDC load drops from 0.8 MW to 0.4 MW at t = 2 s. The LVDC power dynamics

$P _ { \mathrm { L V D C } }$ and corresponding MVDC voltage $U _ { \mathrm { M V D C } }$ are shown in Fig. 23. It is observed that the results of EM and DM agree well during the transient processes, indicating that the EM is sufficient to capture the dynamics of transients.

## VI. CONCLUSION

This paper proposes a novel decoupled electromagnetic transient (EMT) modeling approach and parallel simulation framework for modularized solid-state transformers (MSST). The detailed unified magnetic equivalent circuit (UMEC) for the multiwinding transformer is derived. Relying on the UMEC model, a cut-set-based decoupled modeling method of the submodule is proposed. Then, a parallel simulation framework for MSST is proposed to achieve remarkable simulation acceleration. The overall process is arranged in parallel in the CPU.

The proposed approach utilizes the high frequency and small simulation time-step feature of MSST to obtain a decoupled equivalent model, which is beneficial in efficient bridge circuit cascading, parallel computing, and Norton equivalent integration. By doing this, the decoupled model realizes reduced computation burden and increased simulation speed, and is easy to be used in real-time simulations. Compared to the previous work in [25], the new approach is the same accurate while being 29% faster.

According to the theoretical analysis and simulation results, the operation of the proposed model is affected by the stability of the original system and the time-step. Because the proposed model can always accurately reflect the dynamics of the original electrical system, the topology and control strategy of the original system must be rationally designed. Moreover, the frequency of high-frequency transformers requires the simulation time-step to be small enough to reflect the details of the carrier wave, unreasonable time-step values will make the simulation result deteriorate.

The proposed framework is a potential solution for accurate and fast EMT simulation of MSST, whose high accuracy and efficiency make it applicable under different working conditions in both off-line and real-time simulations.

## REFERENCES

[1] J. E. Huber and J. W. Kolar, “Applicability of solid-state transformers in today’s and future distribution grids,” IEEE Trans. Smart Grid, vol. 10, no. 1, pp. 317–326, Jan. 2019.

[2] G. Zhang, J. Chen, B. Zhang, and Y. Zhang, “A critical topology review of power electronic transformers: In view of efficiency,” Chin. J. Elect. Eng., vol. 4, no. 2, pp. 90–95, Jun. 2018.

[3] J. Han, Z. Zhang, Y. Chen, X. Yin, and Q. Ran, “Research on fault characteristics and protection system of cascaded power electronic transformers,” Int. J. Elect. Power Energy Syst., vol. 137, May 2022, Art. no. 107854.

[4] Z. Ji, L. Hua, J. Yao, and X. Sun, “Research on control strategy of cascaded power electronic transformer based on capacitance minimization,” Energy Rep., vol. 8, pp. 164–175, Oct. 2022.

[5] X. Meng, Y. Jia, C. Ren, X. Lin, and B. Zhang, “Modular DC solid-state transformer with fault-tolerant function,” in Proc. 10th Int. Conf. Power Electron. Energy Convers. Congr. Expo. Asia, 2019, pp. 1–6.

[6] S. G. Paul and C. S. Ravichandran, “An algorithm implementation for harmonics reduction in power electronic transformer based electric locomotives,” in Proc. Int. Conf. Intell. Comput., Inf. Control Syst., 2019, vol. 1039, pp. 274–281.

[7] D. Mishra et al., “A review on solid-state transformer: A breakthrough technology for future smart distribution grids,” Int. J. Elect. Power Energy Syst., vol. 133, Jun. 2021, Art. no. 107255.

[8] L. Zheng et al., “Solid-state transformer and hybrid transformer with integrated energy storage in active distribution grids: Technical and economic comparison, dispatch, and control,” IEEE Trans. Emerg. Sel. Topics Power Electron., vol. 10, no. 4, pp. 3771–3787, Aug. 2022.

[9] S. Sharma, R. A. Chaudhary, and K. Singh, “Evolution in solid-state transformer and power electronic transformer for distribution and traction system,” Emerg. Res. Electron., Comput. Sci. Technol., vol. 545, pp. 1367–1383, Apr. 2019.

[10] L. F. Costa, F. Hoffmann, G. Buticchi, and M. Liserre, “Comparative analysis of multiple active bridge converters configurations in modular smart transformer,” IEEE Trans. Ind. Electron., vol. 66, no. 1, pp. 191–202, Jan. 2019.

[11] J. Xu et al., “Fast electromagnetic transient simulation methods and prospects of high-frequency isolated power electronics transformers,” CIGRE ELECTRA, vol. 316, pp. 29–35, Jun. 2021.

[12] F. Xu, Z. Li, F. Gao, C. Zhao, P. Wang, and Y. Li, “A fast simulation model of cascaded H bridge-power electronic transformer,” in Proc. IEEE IECON 45th Annu. Conf. Ind. Electron. Soc., 2019, pp. 6755–6760.

[13] G. Zheng, Y. Chen, and Y. Kang, “Modeling and control of the modular multilevel converter (MMC) based solid-state transformer (SST) with magnetic integration,” Counselor Educ. Supervision Trans. Elect. Mach. Syst., vol. 4, no. 4, pp. 309–318, Dec. 2020.

[14] S. Subedi et al., “Review of methods to accelerate electromagnetic transient simulation of power systems,” IEEE Access, vol. 9, pp. 89714–89731, 2021.

[15] J. Mahseredjian, V. Dinavahi, and J. A. Martinez, “Simulation tools for electromagnetic transients in power systems: Overview and challenges,” IEEE Trans. Power Del., vol. 24, no. 3, pp. 1657–1669, Jul. 2009.

[16] S. A. M. Saleh et al., “Solid-state transformers for distribution systems– Part I: Technology and construction,” IEEE Trans. Ind. App., vol. 55, no. 5, pp. 4524–4535, Sep./Oct. 2019.

[17] A. R. Alonso, J. Sebastian, D. G. Lamar, M. M. Hernando, and A. Vazquez, “An overall study of a dual active bridge for bidirectional DC/DC conversion,” in Proc. IEEE Energy Convers. Congr. Expo., 2010, pp. 1129–1135.

[18] H. Bai, Z. Nie, and C. C. Mi, “Experimental comparison of traditional phase-shift, dual-phase-shift, and model-based control of isolated bidirectional DC-DC converters,” IEEE Trans. Power Electron., vol. 25, no. 6, pp. 1444–1449, Jun. 2010.

[19] H. Qin and J. W. Kimball, “Generalized average modeling of dual active bridge DC-DC converter,” IEEE Trans. Power Electron., vol. 27, no. 4, pp. 2078–2084, Apr. 2012.

[20] C. Zhao, S. D. Round, and J. W. Kolar, “Full-order averaging modelling of zero-voltage-switching phase-shift bidirectional DC-DC converters,” Inst. Eng. Technol. Power Electron., vol. 3, no. 3, pp. 400–410, May 2010.

[21] Y. Zhu et al., “Discrete state event-driven framework for simulation of switching transients in power electronic systems,” in Proc. IEEE Energy Convers. Congr. Expo., 2019, pp. 895–900.

[22] Y. Zhu, Z. Zhao, B. Shi, and Z. Yu, “Discrete state event-driven framework with a flexible adaptive algorithm for simulation of power electronic systems,” IEEE Trans. Power Electron., vol. 34, no. 12, pp. 11692–11705, Dec. 2019.

[23] J. Xu et al., “High-speed electromagnetic transient (EMT) equivalent modelling of power electronic transformers,” IEEE Trans. Power Del., vol. 36, no. 2, pp. 975–986, Apr. 2021.

[24] M. Feng, C. Gao, J. Ding, H. Ding, J. Xu, and C. Zhao, “Hierarchical modeling scheme for high-speed electromagnetic transient simulations of power electronic transformers,” IEEE Trans. Power Electron., vol. 36, no. 9, pp. 9994–10004, Sep. 2021.

[25] M. Feng, C. Gao, J. Xu, C. Zhao, and G. Li, “Modeling for complex modular power electronic transformers using parallel computing,” IEEE Trans. Ind. Electron., vol. 70, no. 3, pp. 2639–2651, Mar. 2023.

[26] J. Xu et al., “High-speed electromagnetic transient (EMT) equivalent modelling of power electronic transformers,” IEEE Trans. Power Del., vol. 36, no. 2, pp. 975–986, Apr. 2021.

[27] C. Gao et al., “Accelerated electromagnetic transient (EMT) equivalent model of solid-state transformer,” IEEE Trans. Emerg. Sel. Topics Power Electron., vol. 10, no. 4, pp. 3721–3732, Aug. 2022.

[28] K. Strunz and E. Carlson, “Nested fast and simultaneous solution for time-domain simulation of integrative power-electric and electronic systems,” IEEE Trans. Power Del., vol. 22, no. 1, pp. 277–287, Jan. 2007.

[29] Q. Mu, J. Liang, X. Zhou, Y. Li, and X. Zhang, “Improved ADC model of voltage-source converters in DC grids,” IEEE Trans. Power Electron., vol. 29, no. 11, pp. 5738–5748, Nov. 2014.

![](images/7f0d90098d631e063d18c61ac715646896f33e6b2e69ef443b148c150fa2a601.jpg)  
Moke Feng was born in Suining City, Sichuan Province, China. He received the B.Eng. degree in North China Electric Power University, Beijing, China, where he is currently working toward the Ph.D. degree with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Resources. His research interests include the modeling of the key equipment in distribution network and HVDC transmission system.

![](images/4d22c49c4364210db1582d28cbe348d57099ebfcdabba7f5ce84f9c5661bfa18.jpg)

Chenxiang Gao was born in Shanxi, China. He received the B.S. degree and Degree from North China Electric Power University, Beijing, China, in 2019 and 2022, respectively. He is currently working toward the Ph.D. degree with Shanghai Jiao Tong University, Shanghai, China. His research interests include the electromagnetic transient (EMT) equivalent modelling and real-time simulation of the MMC-HVDC and the solid-state transformers (SST) in DC Grid.

![](images/eeb4ddc42e0cd857525f27718bb9f9c94034c9004e73a838a01439d600602d97.jpg)

Jianzhong Xu (Senior Member, IEEE) was born in Shanxi, China. He received the B.S. and Ph.D. degrees from North China Electric Power University (NCEPU), Beijing, China, in 2009 and 2014, respectively.

He is currently a Professor and Ph.D. Supervisor with the State Key Laboratory of Alternate Electrical Power System with Renewable Energy Resources, NCEPU. From 2012 to 2013 and 2016 to 2017, he was a Visiting Ph.D. Student and Postdoctoral Fellow with the University of Manitoba, Winnipeg, MB, Canada.

He has authored or coauthored 24 IEEE Transaction/Journal papers and four of them are ‘Scopus Top 1% highly cited paper’. He is also a Reviewers of ten IEEE/IET journals and nine Chinese journals. He is also an Associate Editor for the CSEE JOURNAL OF POWER AND ENERGY SYSTEMS. He is working on the Electromagnetic Transient (EMT) equivalent modelling, fault analysis and protection of HVDC Grids.

![](images/d8446d2a95e7315b8b54d56848be05c52e7c97836d1afcf9d0b5eee239a60744.jpg)

Chengyong Zhao (Senior Member, IEEE) was born in Zhejiang, China. He received the B.S., M.S. and Ph.D. degrees in power system and its automation from North China Electric Power University (NCEPU) ), Beijing, China, in 1988, 1993 and 2001, respectively. From January 2013 to April 2013 and September 2016 to October 2016, he was a Visiting Professor with the University of Manitoba, Winnipeg, MB, Canada. He is currently a Professor with the School of Electrical and Electronic Engineering, NCEPU. He has authored or coauthored 24 IEEE

Transaction/Journal papers and four of them are ‘Scopus Top 1% highly cited paper’. He is also a Reviewers of ten IEEE/IET journals and nine Chinese journals. His research interests include HVDC system and DC grid.

![](images/22606fc93bdda8463eda803d193a5aea345639c2b6f922e271987f049052dbe2.jpg)

Gen Li (Senior Member, IEEE) received the B.Eng. degree in electrical engineering from Northeast Electric Power University, Jilin, China, in 2011, the M.Sc. degree in power engineering from Nanyang Technological University, Singapore, in 2013, and the Ph.D. degree in electrical engineering from Cardiff University, Cardiff, U.K., in 2018.

He is currently an Associate Professor of power system with the Technical University of Denmark (DTU), Lyngby, Denmark. From 2013 to 2016, he has been a Marie Curie Early Stage Research Fellow

funded by the European Commission’s MEDOW Project. He has been a Visiting Researcher with China Electric Power Research Institute and Global Energy Interconnection Research Institute, Beijing, China, Elia, Brussels, Belgium, and with Toshiba International (Europe), London, U.K. From 2018 to 2022, he was also a Research Associate with the School of Engineering, Cardiff University. His research interests include control and protection of HV and MV DC technologies, offshore wind, offshore energy islands, reliability modelling, and evaluation of power electronics systems.

Dr. Li is also a Chartered Engineer in U.K., Young Editorial Board Member of Applied Energy, Associate Editor for the CSEE JOURNAL OF POWER AND ENERGY SYSTEMS, Editorial Board Member of CIGRE ELECTRA and Global Energy Interconnection and IET Professional Registration Advisor. His Ph.D. thesis was the recipient of the First CIGRE Thesis Award in 2018. He is the Academic Initiatives and Sub-committee Coordinator of IEEE PES Young Professionals, Vice-Chair of IEEE PES Women in Power Denmark, Technical Panel Sectary of CIGRE U.K. B5 Protection and Automation and a Steering Committee Member of CIGRE Denmark NGN.