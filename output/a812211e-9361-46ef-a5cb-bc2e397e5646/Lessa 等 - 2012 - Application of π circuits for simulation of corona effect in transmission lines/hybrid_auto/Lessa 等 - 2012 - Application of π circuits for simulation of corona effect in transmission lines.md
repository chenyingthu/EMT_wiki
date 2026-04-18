# Application of π Circuits for Simulation of Corona Effect in Transmission Lines

L. S. Lessa, Student Member, IEEE, A. J. Prado, Member, IEEE, S. Kurokawa, Member, IEEE, J. Pissolato Filho, Member, IEEE, L. F. Bovolato, Non-member

Abstract—In this article, it is represented by state variables phase a transmission line which parameters are considered frequency independently and frequency dependent. Based on previous analyses, it is used the reasonable number of π circuits and the number of blocks composed by parallel resistor and inductor for reduction of numerical oscillations. It is analyzed the influence of the increase of the RL parallel blocks in the obtained results. The RL parallel blocks are used for inclusion of the frequency influence in the transmission line longitudinal parameter. It is a simple model that is been used by undergraduate students for simulation of traveling wave phenomena in transmission lines. Considering the model without frequency influence, it is included a representation of the corona effect. Some simulations are carried considering the corona effect and they are compared to the results without this phenomenon.

Index Terms-- Electromagnetic transient, EMTP, mathematical model, simulation, transmission lines, π circuit, numeric method, wave traveling.

# I. INTRODUCTION

EPRESENTING the transmission lines and electric power systems, several models are used to the electromagnetic R EPRESENTING the transmission lines and electric power transient analyses, for example, state variables, differential equations. So, these mathematical tools are included in routines and used in numerical simulations of electromagnetic transients. Based on these models, simulation programs, called EMTP type programs, were created. The EMTP index means the Electromagnetic Transient Programs [1], [2] For undergraduate students who are beginning to develop works in this area, it becomes very complicated to use this type of program [3], [4] when it is considered skin effect, ground effect and frequency influence. It is involve models and numerical routines that are very complex. For the study of these students, this research initiation can be based on basic concepts and simple models of transmission lines for transient simulations [5]. In this paper, it is used the representation of transmission lines as a single phase circuit modeled by π

circuits [6, 7], using state variables model. The used numeric routine combines the method of characteristics with the trapezoidal integration method, resulting in a simplified algorithm, which facilitates the initiation of undergraduate students, being capable for simulating electromagnetic transients in networks and obtaining results with satisfactory precision and accuracy. The state equations, which are the voltages and currents along the line, are analyzed numerically using mathematical matricial software (MatLabTM) because this software type allows extending the limits imposed by the EMTP-type programs for the number of π circuits. Using a model that does not include the frequency influence on the longitudinal line parameters, it is considered the corona effect. In this case, it is simulated that this effect reaches a small section of the represented transmission line [11].

# II. MATHEMATICAL MODEL

The state equations can be described by a linear system as:

$$
x = [ A ] x + [ B ] u \tag {1}
$$

where: x is the vector of state variables, u is input vector, A and B are system matrices.

The equation (1) using the method of Heun that is also known as trapezoidal rule. It is a widely used numerical procedure for solving differential equations and linear systems [8, 9]. Described as trapezoidal rule of integration for discrete parameters, this methodology consists of an improved form of the method of tangent or Euler's method that generally applied to solve differential equations, avoiding difficulties in the analytical solutions. The trapezoidal integration applied to solve equation (1) is given by the following equation:

$$
x [ k + 1 ] - x [ k ] = \frac {T}{2} (A x [ k + 1 ] + B u [ k + 1 ] + A x [ k ] + B u [ k ]) \tag {2}
$$

Solving the state equation (2), where T is the integration step, it is rearranged as:

$$
x [ k + 1 ] = x [ k ] + \frac {T}{2} (A x [ k + 1 ] + B u [ k + 1 ] + A x [ k ] + B u [ k ]) \tag {3}
$$

Solving the equation (3), it can be rewrite as:

$$
\left[ I - \frac {T}{2} A \right] x [ k + 1 ] = \left[ I + \frac {T}{2} A \right] x [ k ] + \frac {T}{2} B [ u [ k ] + u [ k + 1 ] ] \tag {4}
$$

Making simplifications to equation (4), it is obtained:

$$
x [ k + 1 ] = A ^ {\prime \prime} x [ k ] + B ^ {\prime} [ u [ k ] + u [ k + 1 ] ] \tag {5}
$$

where: A', A'' and B' are constants of the matrix described by the next equations.

The mentioned constants are described by:

$$
A ^ {\prime} = \left[ I - \frac {T}{2} A \right] ^ {- 1}
$$

$$
A ^ {\prime \prime} = A ^ {\prime} \cdot \left[ I + \frac {T}{2} A \right] \tag {6}
$$

$$
B ^ {\prime} = A ^ {\prime} \cdot \frac {T}{2} B
$$

In equation (4), I is a $( 2  { \mathbf { n } }  { \mathrm { ~ x ~ } } 2  { \mathbf { n } } )$ order matrix (2nx2n), where n is the number of π circuits, A is the matrix that represents the cascade of π circuits and B is the array of input values of the system. The transmission line represented by a π circuit cascade with frequency independent parameters is shown in Fig. 1. This single-phase transmission line representation has length d.

![](images/83b6520830f80fb08d3e53a82cfb8b58af167da08b71fd98fa48d08470c6e7da.jpg)  
Fig. 1. Line without frequency influence represented by a cascade of π circuits.

Fig. 1 shows the parameters R and L that are the line longitudinal resistance and inductance, respectively. The parameters G and C are the line transversal conductance and capacitance, respectively.

$$
R = R ^ {\prime} \frac {d}{n}; L = L ^ {\prime} \frac {d}{n} \tag {7}
$$

$$
G = G ^ {\prime} \frac {d}{n}; C = C ^ {\prime} \frac {d}{n} \tag {8}
$$

It is known that transmission lines, which parameters can be considered independent of frequency, can be modeled through a cascade of π circuits [6, 7] through a single phase representation. Figure 1 shows a single-phase transmission line representation of length d using a cascade of n π circuits.

In (7) and (8), $R ^ { \prime } , L ^ { \prime } , G ^ { \prime }$ and $C ^ { \prime }$ are the line parameters of the line per length unit. Using metric units for practical applications, the units are: $\left[ \Omega k m ^ { - 1 } \right]$ , $[ m H . k m ^ { - 1 } ]$ , $[ \mu S . k m ^ { - 1 } ] \mathrm { ~ e ~ } [ n F . k m ^ { - 1 } ]$ , respectively.

# III. DETERMINATION OF THE STATE EQUATIONS FOR A π CIRCUIT

When it is taken into account the effect of frequency, each modified π circuit is show in Figure 2, where the effect of frequency on the longitudinal line parameters is represented through associations RL parallel.

![](images/f9072e8d6ab96b3e7e3e7fe875d002ac7594290646c717b5ec04b8d9fc31205f.jpg)  
Fig. 2. Inserting the effect of frequency in a π circuit.

In Fig. 2, it is considered the currents $i _ { I 0 } ( t ) , i _ { I I } ( t ) , . . . , i _ { I m } ( t ) .$ , circulating in the inductors $L _ { 0 } , L _ { I } , L _ { 2 } , . . . , L _ { m } ,$ , respectively. The voltages at terminals A and B are respectively u(t) and $\nu _ { I } ( t )$ . These are the state variables in the modified π circuit. For the π circuit shown in Fig. 1, the state variables are only the voltages on the capacitors and the currents in inductors. Once known voltages and currents that circulate in the RL blocks, it can be written:

$$
\frac {d i _ {1 0}}{d t} = \frac {i _ {1 0}}{L _ {0}} \left(- \sum_ {j = 1} ^ {m} R _ {j}\right) + \frac {1}{L _ {L 0}} \left(\sum_ {j = 1} ^ {m} R _ {j} i _ {1 j}\right) + \frac {1}{L _ {0}} u (t) - \frac {1}{L _ {0}} v _ {1} (t) \tag {9}
$$

$$
\frac {d i _ {1 1}}{d t} = \frac {R _ {1}}{L _ {1}} i _ {1 0} - \frac {R _ {1}}{L _ {1}} i _ {1 1} \tag {10}
$$

$$
\frac {d i _ {1 2}}{d t} = \frac {R _ {2}}{L _ {2}} i _ {1 0} - \frac {R _ {2}}{L _ {2}} i _ {1 2} \tag {11}
$$

$$
\frac {d i _ {1 m}}{d t} = \frac {R _ {m}}{L _ {m}} i _ {1 0} - \frac {R _ {m}}{L _ {m}} i _ {1 m} \tag {12}
$$

$$
\frac {d v _ {1} (t)}{d t} = \frac {2}{C} i _ {1 0} - \frac {G}{C} v _ {1} (t) \tag {13}
$$

From (9) to (13), the current notations $( i _ { I 0 } , \ i _ { I I } , \ . . . , \ i _ { I m } )$ notations are simplified from the currents $i _ { I 0 } ( t ) , i _ { I I } ( t ) , . . . , i _ { I m } ( t )$ , respectively. Using (3) to (7), it can be described the circuit of Fig. 2 using (1) as:

$$
A _ {\pi} = \left[ \begin{array}{c c c c c c} - \frac {\sum_ {j = 0} ^ {j = m} R _ {j}}{L _ {0}} & \frac {R _ {1}}{L _ {0}} & \frac {R _ {2}}{L _ {0}} & \dots & \frac {R _ {m}}{L _ {0}} & - \frac {1}{L _ {0}} \\ \frac {R _ {1}}{L _ {0}} & - \frac {R _ {1}}{L _ {0}} & 0 & \dots & 0 & 0 \\ \frac {R _ {2}}{L _ {2}} & 0 & - \frac {R _ {2}}{L _ {2}} & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & 0 & 0 \\ \frac {R _ {m}}{L _ {m}} & 0 & 0 & \dots & - \frac {R _ {m}}{L _ {m}} & 0 \\ \frac {2}{C} & 0 & 0 & \dots & 0 & - \frac {G}{C} \end{array} \right] \tag {14}
$$

$$
x ^ {T} = \left[ \begin{array}{l l l l l l} i _ {1 0} & i _ {1 1} & i _ {1 2} & \dots & i _ {1 m} & v _ {1} (t) \end{array} \right] \tag {15}
$$

$$
\dot {x} = \frac {d x}{d t} = \left[ \begin{array}{l l l l l l} \frac {d i _ {1 0}}{d t} & \frac {d i _ {1 1}}{d t} & \frac {d i _ {1 2}}{d t} & \dots & \frac {d i _ {1 m}}{d t} & \frac {d v _ {1} (t)}{d t} \end{array} \right] ^ {T} \tag {16}
$$

$$
B ^ {T} = \left[ \begin{array}{c c c c c c} \frac {1}{L _ {0}} & 0 & 0 & \dots & 0 & 0 \end{array} \right] \tag {17}
$$

In (15) and $( 1 6 ) , x ^ { T }$ and $B ^ { T }$ correspond to the matched x and $B ,$ respectively. The results show that $A _ { \pi }$ is a square matrix of order (m +2) and the vector x has (m +2) elements.

# IV. DETERMINATION OF THE EQUATIONS OF STATE FOR MORE THAN ONE Π CIRCUIT

Based on the equations and results for one π circuit, it can be extended the analyses to a cascade of π circuits. Thus, the matrix $\it { \Delta } I A J$ will have an order of $n ( m + 2 )$ and the vector $[ x ]$ has dimension $n ( m + 2 )$ . These elements can be written as:

$$
[ A ] = \left[ \begin{array}{c c c c} A _ {1 1} & A _ {1 2} & \dots & A _ {1 n} \\ A _ {2 1} & A _ {2 2} & \dots & A _ {2 n} \\ \vdots & \vdots & \ddots & \dots \\ A _ {n 1} & A _ {n 1} & \dots & A _ {n n} \end{array} \right] \tag {18}
$$

$$
[ x ] ^ {T} = \left[ \begin{array}{l l l l} x _ {1} & x _ {2} & \dots & x _ {n} \end{array} \right] \tag {19}
$$

In equation (18), $\it { \Delta } I A J$ is a tridiagonal matrix which elements are square matrices of order (m +2). A generic element $\left[ A _ { K K } \right]$ at main diagonal of the matrix $\it { \Delta } I A J$ is written in the form:

$$
\left[ A _ {k k} \right] = A _ {\pi} \tag {20}
$$

The $A _ { \pi }$ matrix is defined in equation (14).

An element of any upper subdiagonal in equation (18) is a square matrix of order $( m + 2 )$ which only nonzero element is located in the first column of last row and has the value $( - \bigtriangledown _ { C } )$ . The structure is:

$$
\left[ A _ {i k} \right] = \left[ \begin{array}{c c c c} 0 & 0 & \dots & 0 \\ \vdots & \ddots & \dots & \vdots \\ 0 & \dots & \ddots & \vdots \\ - \frac {1}{C} & 0 & \dots & 0 \end{array} \right] \tag {21}
$$

$$
i = k - 1, \quad 2 \leq k \leq n
$$

The subdiagonal elements in the equation (18) are square matrices of order $( m + 2 )$ . These arrays have a single nonzero element which is in the last column of first row. It is a value of $\left( \mathop { V } _ { L _ { 0 } } \right)$ . The structure is:

$$
\left[ A _ {i k} \right] = \left[ \begin{array}{c c c c} 0 & \dots & 0 & \frac {1}{L _ {0}} \\ \vdots & \ddots & \dots & 0 \\ \vdots & \dots & \ddots & \vdots \\ 0 & 0 & \dots & 0 \end{array} \right] \tag {22}
$$

$$
i = k + 1, \quad 1 \leq k \leq n - 1
$$

Considering a cascade of π circuits, the vector B has dimension of n(m +2) and if it is connected a u(t) source at the beginning of the line, the vector B has a single nonzero element, which is the first array element and it has the value $\left( \mathop { V } _ { L _ { 0 } } \right)$ . From equation (19), the vector $[ x _ { k } ]$ is written in generic form:

$$
\left[ x _ {k} \right] ^ {T} = \left[ \begin{array}{l l l l l l} i _ {k 0} & i _ {k 1} & i _ {k 2} & \dots & i _ {k m} & v _ {k 1} (t) \end{array} \right] \tag {23}
$$

# V. TESTING THE MODEL

Checking the effectiveness of the developed model, it is simulated the energizing of a transmission line, considering frequency independent line parameters and frequency dependent ones. The energizing source is a 1 kV step source and it is connected to the sending end terminal line. The

receiving end terminal is opened. For frequency dependent line parameters, it is considered that the longitudinal parameters of the line per unit length can be perfectly summed up by a circuit consisting of four RL parallel blocks connected in series. The structure is completed using a RL series block (Fig. 3).

![](images/ae7116cc7be6a2de3b4af1e46484f8d70cdf69034c27d796d986e6f96034d5c0.jpg)  
Fig. 3. Circuit that represent the longitudinal parameters of the modeled line.

The values of R and L used to synthesize the effect of frequency on the longitudinal parameters of the line were obtained using the method proposed by [10] and are shown in Table 1. The parameters of the unit transverse line shown in figure 3 are $G ^ { \prime } = \theta ,$ 556 μS/km $\mathbf { e } C ^ { \prime } = I I$ , 11nF/km.

TABLE I VALUE OF ELEMENTS USED IN R AND L CALCULATION OF PARAMETER OF THE LINE UNIT.   

<table><tr><td colspan="2">Resistors (Ω/km)</td><td colspan="2">Inductors (mH/km)</td></tr><tr><td>R0</td><td>0,026</td><td>L0</td><td>2,209</td></tr><tr><td>R1</td><td>1,470</td><td>L1</td><td>0,74</td></tr><tr><td>R2</td><td>2,354</td><td>L2</td><td>0,12</td></tr><tr><td>R3</td><td>20,149</td><td>L3</td><td>0,10</td></tr><tr><td>R4</td><td>111,111</td><td>L4</td><td>0,05</td></tr></table>

Since the values of R and L elements of the cascade of π circuits that describe the line are known, it can be obtained the state equations that describe the behavior of currents and voltages along the line. The simulations using the model proposed in this paper were performed in MatLabTM program, using the trapezoidal integration method [10]. Considering the frequency independent line parameters, the circuit of Fig. 3 is reduced to the RL series block composed by the $\mathrm { R } _ { 0 }$ and $\mathrm { L } _ { 0 }$ elements. In this case, the values are: $R _ { 0 } = 0 . 0 5$ Ω/km and $L _ { \theta }$ $= I \ m H / k m$ .

# VI. OBTAINED RESULTS

In all simulations, it is used the following values: the transmission line has 10 km. It is represented through 200 π circuits. The time step used in the simulations is 50 ns and the simulation period is 600μs.

Figs. 4, 5, 6 and 7 show the relationship between the number of RL parallel blocks and the inclusion of the frequency influence. In Figure 4, the longitudinal resistance values are obtained using four RL parallel blocks. In this case, each RL parallel is related to a frequency decade in the range from 10 Hz to 10 kHz. It is the minimum number of RL parallel blocks in π circuits, because if this number decreases, the resistance values do not have a similar characteristic to the transmission line resistance. Confirming this affirmation, it is shown comparisons among resistance values in Fig. 5, considering the variation on the number of RL parallel blocks.

Figs. 6 and 7 show the analyses related to the longitudinal

inductance values. These results confirm the conclusions about Figs. 4 and 5.

![](images/ce046704f002a270f472b2da407e46a86eebdaf4e00f45936233e26c952edc58.jpg)  
Fig. 4. Synthesis of resistance per unit length using four RL parallel blocks.

![](images/f011083ec4cbfebc5bb37f66354d859827387c81a73e2b5d5f8d7e089eea75dc.jpg)  
Fig. 5. Comparisons for longitudinal resistance values with the variation of RL parallel block quantity.

![](images/21af63c507d6b5a36774f5aa032c2d77367d39baa135febaa4edd8fb82909ac5.jpg)  
Fig. 6 Synthesis of inductance per unit length using four RL parallel blocks.

![](images/2be5c0167639bfef59ec9e3285a81eee7502a2ffc6849bee7c776559d5e80081.jpg)  
Fig. 7. Comparisons for longitudinal inductance values with the variation of RL parallel block quantity.

From the results of Figures 6 and 7, it is observed that the synthesis of the effect of frequency on the resistance can only be considered when inserted in the cascade of π circuits, at least, two RL parallel blocks, because each block is related to a frequency set point. So, the more blocks used, the more frequency set points obtained. This conclusion is confirmed

through the results shown in Figures 8, 9, 10 and 11 where the time domain simulations are shown. These simulations are carried out considering a 1 kV step source connected to the sending end terminal. The receiving end terminal is opened.

![](images/01aeb0d74ca092a44d645763f491b282c49c1473523279aecdccf978465a7f82.jpg)  
Fig. 8. Energization of the transmission line without the effect of frequency considering 200 π circuits.

![](images/b66219f869a55e5fcc572cd8531fae0611fe3ba72bc4fe649c7ee0726aa8a053.jpg)  
Fig. 9. Voltage at the end of the transmission line with the effect of frequency considering 200 π circuits.

![](images/fc89d7e7e0af24ba80041f853311d811183b49d2e86a187d62fd45c7e0c6c7fc.jpg)  
Fig. 10. Comparisons between both time domain simulations: with frequency influence and without this influence.

![](images/6bc2832bbf92c1f1ae5cb552dd4d19e916e7fd74a0cdacb6819a950224373c6a.jpg)  
Fig. 11. Comparisons considering the influence of the number of RL parallel blocks in time domain simulations.

Using the routine without the influence of frequency, it is observed that there is a period of time related to the time of

signal propagation through the line. Thus, it represents a time delay between input signal and output signal. After the delay, there are oscillations associated with wave reflections on the transmission line terminals that make up the output voltage shown. Using the routine with frequency influence in longitudinal parameters, the voltage signal is attenuated because the inclusion of the frequency influence.

Figs. 12 and 13 show the influence of frequency on the current results. Without the frequency influence, the obtained signal current is not attenuated and is highly modified by numeric oscillations. On the other hand, when the routine considers the influence of frequency, it is clear that the current signal could not contain those oscillations shown in Fig. 12. So, those oscillations are numeric oscillations and they can be associated to the representation of the longitudinal line parameters which does not consider the frequency influence. So, for the sequence of this work, it should be investigated what is the saturation point for the number of the π circuits and the number of the RL parallel blocks. It is carried out using the simulation results from several voltage signals that will be used as voltage sources at the initial line terminal.

![](images/ecd98a82cadcc774cedbf6f7917178f468e1b3d45eee5fc19f5b52c3098690bf.jpg)  
Fig. 12: Current at the end of the transmission line without the effect of frequency.

![](images/1ea1a0396c7a02aebfadae58a7b22e3eb2084ec4bf0bcca125ad322adf87924f.jpg)  
Fig. 13: Current at the end of the transmission line considering effect of frequency.

# VII. ANALYSES WITH THE CORONA EFFECT

Considering the corona effect, Gary’s model is applied with the routine described in the previous items. It is used the line representation without frequency influence, because the representation with frequency influence has not hardly analyzed. The corona effect is introduced by [11]:

$$
C _ {C O R O N A} = C \cdot \eta \cdot \left(\frac {V}{V _ {C O R O N A}}\right) ^ {\eta - 1} \tag {24}
$$

$$
\eta = 0. 2 2 \cdot R _ {C O N D} + 1. 2
$$

In this case, $R _ { C O N D }$ is the conductor phase radius in [cm], C is the transversal line capacitance and the $C _ { C O R O N A }$ is the new value of the transversal line capacitance because the corona effect. In this paper, the $R _ { C O N D }$ value is 2.54 cm. The simulations are carried out for some relations between V and $V _ { C O R O N A } .$ . The V value is 1 pu for all following shown simulations.

![](images/679f5783051abb620275997b7a3be1ba003c7d54f883e15949e4de17d2027df2.jpg)  
Fig. 14. The time domain simulations with the corona effect for $V _ { C O R O N A } = 0 . 3 5 ~ V .$ .

![](images/800e2a85fd62faa7724a12fcf87347ad8caa414c53c8a676f0204d3adadaf668.jpg)  
Fig. 15. The time domain simulations with the corona effect for $V _ { C O R O N A } = 0 . 5 ~ V .$

![](images/99a45caacc62973fd611f440fb824d63b3c7d3b8d8b9d3f90c537886047cc76c.jpg)  
Fig. 16. The time domain simulations with the corona effect for $\bar { V _ { C O R O N A } } = 0 . 7 V .$

![](images/35979a25779d2fb5b7d6fe008577f43a1893c56635fa1573440c4203ab26f3af.jpg)  
Fig. 17. The time domain simulations with the corona effect for $\bar { V _ { C O R O N A } } = 0 . 9 V .$

![](images/65390ca6aff6a76bdaf16798091570c7dcff4025b07c7016e82ea8e14eeb8183.jpg)  
Fig. 18. Comparisons of the time domain simulations with the corona effect for some VCORONA values.

Considering Figs. 14 to 180, the corona effect is related to the 10 π circuits in the middle line. It corresponds to the 500 m of the represented line. Figs. 14 to 17 show results for different relative values of the corona voltage when compared to the line nominal voltage. In Fig. 18, it is shown the comparisons among the results for the voltage values in the receiving end terminal. So, using a simple routine based on π circuits for transmission line representation, undergraduate students can analyze and simulate traveling wave phenomena in transmission lines.

For future development, the frequency influence will be introduced in the routine used for the corona effect simulation.

# VIII. CONCLUSIONS

Several simulations are performed considering the mathematical model using state variables for transmission line transients based on the single phase line representation. It is considered the effect of frequency influence insertion, comparing it to the representation without frequency influence. It is also carried out corona effect simulations. In case of the introduction of frequency influence, it is carried out including RL parallel blocks in the π circuits. The π circuit cascade is the simple model for transmission lines and it can be easily assimilated by undergraduate students. So, these students can use the RL parallel blocks for modifying the π circuit structure for transmission line transient analyses that considers the frequency influence.

In this paper, the number of RL parallel blocks is varied, investigating the effect on the frequency influence modeling. This number is necessary in order to have set points for the resistance and admittance values between the low and high frequencies. It is concluded that the number of RL parallel blocks can be expanded according to the accuracy of a performed simulation. Increasing the number of π circuits, the accuracy of the obtained results can be also improved.

Finally, considering a single phase transmission line representation, it is simulated the line energization. It is applied 200 π circuits. For each π circuit, it is applied four RL parallel blocks for a frequency range from 10 Hz to about 10 kHz. These quantities are reasonable and lead to a satisfactory accuracy for the obtained results compared to those results obtained by other authors. The accuracy of the obtained can be considered satisfactory because the used

model is simple and it is recommended for undergraduate students’ analyses. Also considering the amount of number of RL parallel blocks and π circuits, the proposed routine has numerical stability in the basic transmission line transient simulations. In future, it is intended to expand the concepts used in this article proposing improvements for the numeric routine and the solution of the used state equations.

The time domain simulations of the corona effect confirm that the proposed model is simple and it can be used by undergraduate students for introduction of concepts about transmission line representation, traveling waves, electromagnetic transient phenomena, simulation methods and numerical methods for solving of linear systems.

# IX. REFERENCES

[1] Microtran Power System Analysis Corporation, Transients Analysis Program Reference Manual, Vancouver, Canada, 1992.   
[2] H. W. Dommel, EMTP Theory Book, Department of Electrical Engineering, University of British Columbia, Vancouver, 1996.   
[3] Mamis, M. S. (2003). Computing of electromagnetic Transients on Transmissions Lines with Nonlinear Components. IEE Proceedings Generation, Transmission and Distribution, Vol. 150, N0. 2; pp. 200- 203.   
[4] Mamis, M. S. and A. Nacaroglu (2003). Transient Voltage and Current Distributions on Transmission Lines. IEE Proceedings Generation, Transmission and Distribution, Vol. 149, N0. 6; pp. 705-712.   
[5] F. N. R. Yamanaka, S. Kurokawa, A. J. Prado, J. Pissolato, L. F. Bovolato, “Analysis of longitudinal and temporal distribution of electromagnetic waves in transmission lines by using state-variable techniques”, Sixty Latin-American Congress: Electricity Generation and Transmission – VI CLAGTEE, Mar Del Plata, 2005.   
[6] H. W. DOMMEL, "Digital computer solution of electromagnetic transients in single and multiphase networks", IEEE Transactions on Power Apparatus and Systems, vol. PAS-88, pp. 388-399, April, 1969.   
[7] R. M. NELMS, STEVEN, R. NEWTON, G. B. SHEBLE, L. L. GRIGSBY. “Using a personal Computer to teach power system Transients”, IEEE Transactions on Power System, Vol. 4, No. 3, August 1989.   
[8] J. A. R. MACÍAS, A. G. EXPÓSITO, A. B. SOLER, “A Comparison of Techniques for State Space Transient Analysis of Transmission Lines”, IEEE Transactions on Power Delivery, vol. 20, nº 2, pp. 894-903, April, 2005.   
[9] W. E. Boyce and R. C. DiPrima, Equações Diferenciais Elementares e Problemas de Valores de Contorno, Rio de Janeiro: Guanabara Koogan, 1994.   
[10] Tavares, M. C. (1998).Modelo de Linha de Transmissão Polifásico Utilizando Quase-Modos, Doctor Thesis, UNICAMP – The State University of Campinas, Campinas, Brazil.   
[11] M. S. Mamis, “State-Space Transient Analysis of Single-Phase Transmission Lines with Corona”, The International Conference on Power Systems Transients - IPST 2003, 28th September – 2nd October, 2003,New Orleans, Louisiana, USA.

# X. BIOGRAPHIES

Leonardo da Silva Lessa is a 3th year undergraduate student of Electrical Engineering at UNESP (State University of São Paulo). Currently, he develops studies of electromagnetic transients in transmission lines with a research group in this area.

Afonso José do Prado - Electrical engineering (1991) at FEIS/UNESP – The University of São Paulo State, Brazil, M.Sc. (1995) at FEIS/UNESP and D.Sc. at UNICAMP – The State University of Campinas – UNICAMP (2002). His main research interests are in electromagnetic transients of transmission lines.

Sérgio Kurokawa has been Assistant Professor at FEIS/UNESP since 1994. He received D.Sc. degree from UNICAMP (2003). His main research interests are electromagnetic transients in power electric systems and long transmission line models used in electromagnetic transient analyses.

José Pissolato Filho was born in Campinas, São Paulo, Brazil, in 1951. He received the PhD. degree in electrical engineering from Université Paul Sabatier, France, 1986. Since 1979, he has been with Department of Energy and Control of UNICAMP. His main research interests are in high voltage engineering, electromagnetic transients and electromagnetic compatibility.

Luiz Fernando Bovolato – M.Sc. in Electrical engineering (1983) at UFRJ - Federal University of Rio de Janeiro, Brazil, Brazil, D.Sc (1993) at USP – State University of São Paulo. His main research interests are in transient analyses and line parameter calculations. Presently, he is a researcher at FEIS/UNESP.