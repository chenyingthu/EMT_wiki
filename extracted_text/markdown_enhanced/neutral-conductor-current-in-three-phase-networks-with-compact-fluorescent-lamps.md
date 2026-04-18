# Neutral conductor current in three-phase networks with compact fluorescent lamps
J. Cunill$^a$, L. Sainz$^{b,*}$, J.J. Mesas$^b$
$^a$ Department of Electrical Engineering, EPSEM-UPC, Av. de las Bases 61-73, 08240 Manresa, Spain
$^b$ Department of Electrical Engineering, ETSEIB-UPC, Av. Diagonal 647, 08028 Barcelona, Spain

*Corresponding author. Tel.: +34 93 4011759; fax: +34 93 4017433. E-mail addresses: cunill@ee.upc.edu (J. Cunill), sainz@ee.upc.edu, sainz@ee.upc.es (L. Sainz), juan.jose.mesas@upc.edu (J.J. Mesas).

**Abstract**
In this paper, expressions of the neutral conductor current in three-phase networks with compact fluorescent lamps (CFLs) are obtained from a CFL “black-box” model proposed in the literature. These expressions allow studying and performing a sensitivity analysis of the impact of CFLs on neutral current. The influence of CFL model parameters, as well as supply voltage unbalance, number of CFLs per phase and different types of CFLs per phase, on the neutral current is also investigated. The obtained results are validated with measurements and PSCAD/EMTDC simulations.

**Keywords:** Compact fluorescent lamps, Power system harmonics, Least-squares algorithms

## 1. Introduction
CFLs are used increasingly because of their low energy consumption and long average useful life compared to traditional incandescent bulbs. However, the former are linear time-variant electrical loads and the current waveform they absorb is extremely distorted (far removed from the sinusoidal form). Although they are small-power single-phase loads ($<25$ W), they can be an important source of harmonics because a large number of them can be connected to the same bus, causing problems in installations and affecting voltage waveform quality [1,2]. One of these problems is the harmonic current flow in the neutral conductor [3–5]. In balanced three-phase systems, the first- and fifth-order harmonics in the phase currents ($k = 1, 7, \dots$ and $k = 5, 11, \dots$, respectively) are a positive sequence system and a negative sequence system, respectively, while the third-order harmonics ($k = 3, 9, \dots$) are a zero sequence system. In this situation, only the third-order harmonic currents flow into the neutral conductor and are three times as high as the corresponding harmonics in phase currents. System unbalances such as supply voltage unbalance and load unbalance cause the loss of positive and negative sequence symmetry in the first- and fifth-order harmonics. Hence, the sum of these harmonics in the neutral conductor is now not zero. This can increase the rms value of the neutral conductor current. Studies on this harmonic problem require CFL models to calculate the harmonic currents injected into the installation [1,6–9]. In [1], the Norton equivalents are used to characterize the CFL harmonic currents. In [6,7], the concept of tensor analysis with phase dependency is introduced to consider the harmonic interaction of the supply voltage in CFL harmonic currents. In [8], the CFL study is based on the CFL equivalent circuit. In [9], external CFL behaviour is modelled paying particular attention to the current waveform absorbed as a “black-box” function of the voltage applied.

This paper studies the impact of CFLs and three-phase unbalances on the neutral conductor current. Section 2 presents the CFL model used in the neutral conductor current study, which is based on the “black-box” model in [9]. In Section 3, the expression of the neutral conductor current is determined based on the above model, and the influence of CFL parameters on the neutral current is studied. Analytical expressions to determine the impact of supply voltage unbalance, different number of converters per phase and converters with different parameters per phase on the neutral conductor current are provided in Sections 4–6. Moreover, this influence is analyzed using the previous expressions. Section 7 gives an overview of the simplifications of the study. In Section 8, the obtained results are validated with four experimental tests and PSCAD/EMTDC simulations.

## 2. Compact fluorescent lamp modelling
### 2.1. CFL electronic ballast and current waveform
The typical circuit of the CFL electronic ballast is composed of a diode bridge with an ac resistance and a DC-smoothing capacitor that feeds the tube inverter [6–8]. The inverter and tube can

*Model fitting parameters:*
Actual measurements vs. Model fitting: $K_G = 38.6 \text{ mS}\cdot\text{V}^{1/2}$, $K_{td} = 0.159 \text{ ms}\cdot\text{V}$
$K_1 = 15.8 \text{ ms}\cdot\text{V}$, $K_2 = 0.33 \text{ ms}$
$G_{\text{exp}}$, $u(t)$, $t_{td}$