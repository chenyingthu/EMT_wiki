**General approach for accurate resonance analysis in transformer windings**

M. Popov  
Delft University of Technology, Faculty of EEMCS, Mekelweg 4, 2628CD, Delft, The Netherlands

**Article history:**  
Received 10 October 2017  
Received in revised form 9 March 2018  
Accepted 2 April 2018

**Keywords:**  
Resonance  
Overvoltages  
Transformer winding  
Voltage distribution  
Amplification factor

**Abstract**  
In this paper, resonance effects in transformer windings are thoroughly investigated and analyzed. The resonance is determined by making use of an accurate approach based on the application of the impedance matrix of a transformer winding. The method is validated by a test coil and the numerical results are verified by an ATP-EMTP model. Further analysis is applied on a transformer winding for which the inductance and the capacitance matrix as well as the winding losses are previously determined. By having determined the amplification factor, it can be found the location where the most severe transients may occur. It is also shown that maximum resonance overvoltage depends on the duration of the excitation and its resonance frequency.

## 1. Introduction

Transformers are important devices which are inevitable for the existence and the operation of power systems. The study of transient behavior of transformer voltages and currents is important for transformer designers and system planners, in order to know the interaction between the transformer and the system during different disturbances.

Transformers may normally possess more resonance (natural) frequencies, which exist because transformer windings and coils can be seen as a number of series inductances and shunt capacitances. When a transformer is excited by a voltage that oscillates with a frequency equal to some of the resonance frequencies, a resonance occurs. During this process, the total winding impedance is determined by the copper losses of the transformer winding. Hence, the resonance is a phenomenon in which the terminal transformer impedance is fully resistive and the imaginary impedance part is equal to zero. In this case, the total impedance becomes either minimum (series resonance) or maximum (parallel or anti-resonance). In case of a series resonance, the transformer is exposed to high overvoltages voltages, and the voltage distribution in the winding is non-linear since winding capacitances cannot be ignored. The evaluation of this distribution is important in order to know, which of the windings experience the highest stresses and under which conditions; lightning or switching. One important parameter that provides insight about voltage amplitudes along the winding is the amplification factor. This parameter was studied in Ref. [1]. During non-standard waves, resonance overvoltages may take different values. The analysis is performed to a single transformer even though the procedure is valid for multi-transformer windings as long as the impedance matrices, the elements of which are frequency dependent, are accurately determined.

Nowadays different types of models are applied to study transformer transients. The powerful vector fitting model, which is very accurate belongs to the group of blackbox modeling [2]. Its application depends on the measured admittance matrices within broad frequency range. A model based on 2 port network representation by making use of a Frequency Response Analysis (FRA) is another example of an efficient black box approach [3]. Another type of models are white box models. These are numerical models that make use of inductance-, capacitance- and resistance matrices. The advantage of the white box models is that transient analysis is performed within broad frequency range. However, the disadvantage is that the accuracy strongly depends on the accuracy of computed parameters, particularly inductance and capacitance matrix as well as losses, which are frequency dependent [4–6]. Finally, the last type of models are gray box models. These models are built in EMTP-based software packages, and some transformer parameters previously determined by white box model can be tuned to the measured values (black-box). In this way, inaccuracies of white box model can be eliminated.

In this work, an accurate modeling of the transformer winding based on the nodal admittance matrix is presented. Firstly, the modeling approach is described and applied to a transformer winding for which the parameters are known. Besides, the C-, L- and R-matrices are with constant parameters, so the model can also be implemented in ATP-EMTP environment and verified by a numerical analysis. Thereafter, a detailed analysis is performed on a foil-type transformer [4].

The paper is organized as follows. Section 2 explains the computational procedure. Section 3 deals with the verification of the model by an EMTP model; white box

**Fig. 1.** An illustration of the test circuit.

arbitrary coil point $j$ and the terminal voltage with respect to the terminal voltage can be represented as:

$$ AF = \frac{u_1(j\omega) - u_j(j\omega)}{u_1(j\omega)} = \frac{Z_{11}(j\omega) - Z_{j1}(j\omega)}{Z_{11}(j\omega)} \tag{5} $$

Eq. (5) is known as an amplification factor. When the source voltage $u_1$ is also known, the voltage at each coil $u_j$ can be determined