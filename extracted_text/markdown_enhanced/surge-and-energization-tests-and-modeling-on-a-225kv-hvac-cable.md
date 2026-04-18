# Surge and energization tests and modeling on a 225 kV HVAC cable

Isabel Lafaia^a^, Maria Teresa Correia de Barros^b^, Jean Mahseredjian^a,∗^, Akihiro Ametani^a^, I. Kocar^a^, Y. Fillion^c^

^a^ Polytechnique Montreal, Montréal, Québec, Canada  
^b^ Instituto Superior Técnico, University of Lisbon, Lisboa, Portugal  
^c^ Réseaux de Transport d’Électricité, Paris La Défense, France  

∗ Corresponding author.  
E-mail addresses: jeanm@polymtl.ca (J. Mahseredjian), ilhan.kocar@polymtl.ca (I. Kocar).

**Abstract**  
This paper presents experimental results from surge and energization field tests carried out on a 225 kV underground XLPE cable with 64 km and 17 major sections with cross-bonding of sheaths. The surge tests applied a 2 kV surge to minor and major sections having 1080 m and 3952 m, respectively. The tests on the minor section were intended to excite different propagation modes and observe the respective cable responses. In the energization tests, the transient current and voltage at the sending end were measured, when energizing the full cable, from each end. Measured results of current show the impact of transformers in the network and the reactive compensator. The energization tests were simulated in EMTP using detailed and simplified cable models, corresponding to using a separate model for each cable minor section or a homogeneous equivalent for the whole cable length. Computed results show that using the simplified model does not reduce the accuracy of simulations of core voltages and currents, because the simulated test concerned only core conductor quantities.

**Keywords:** Underground cable, Field tests, Electromagnetic transients, EMTP

## 1. Introduction
Projects of new cable installations have taken place worldwide in the last few years. These cable links are used for intercontinental connections, to reinforce the grid with reduced impact in the surrounding environment, and to connect renewable energy sources to the grid [1–5].

The increase of computer capacity and the improvement of simulation tools allowed the development of more accurate cable models used for electromagnetic transient (EMT) studies, cable fault location and harmonic studies [6–13]. A cable model can be validated based on simulations only [6–11], but a more reliable validation requires a comparison of the simulation results with measurements from field tests performed on the actual cable system [7,9,13–18].

This paper presents experimental results from field tests carried out on a high-voltage alternate-current (HVAC) cable. Part of these results were previously presented at IPST 2017 [29].

In the surge tests, a 2 kV surge was applied to a minor section and to a major section of the cable having, 1080 m and 3952 m, respectively. The advantage of testing a single minor section is that we can excite each propagation mode separately and observe the respective cable responses, which is useful for model validation. In the energization test, the full 64 km long cable was connected to the grid. The energization test is simulated in EMTP.

## 2. Characteristics of the cable system
The tested system is a 225 kV XLPE underground cross-bonded cable, with 64 km length, connecting Boutre and Trans stations in France. The cable phases are enclosed by high-density polyethylene (HDPE) tubes embedded in concrete. Fig. 1 depicts the layout of the cable and Table 1 shows the cable data. Both $2000\ \text{mm}^2$ and $2500\ \text{mm}^2$ cables are installed, depending on location. The cable has 17 major sections. The cross-bonding joints of the terminal major sections are protected by surge arresters. Reactive compensators are connected at both cable ends.

The minor and major sections used in the surge tests are represented in Fig. 2.

## 3. Surge tests
The surge tests were conducted during the cable construction. In these tests a 2 kV $1.2/50\ \mu\text{s}$ surge was applied to a minor and to a major cable sections, having 1080 m and 3952 m, respectively. The generator output impedance is $2\ \Omega$. Grounding rods had to be installed next to the two terminals of the minor section and the

**Fig. 1.** Layout of the 225 kV XLPE underground cable: a) cable system layout; b) one-phase layout.

**Table 1** Data for 225 kV XLPE underground cable.

| Parameter | 2000 mm² cable | 2500 mm² cable |
|---|---|---|
| Core cond. ($r_1 = 0$), $\rho = 1.76 \times 10^{-8}\ \Omega\text{m}$ | $r_{2n} = 34.5\ \text{mm}^a$, $r_2 = 28.4\ \text{mm}^b$ | $r_{2n} = 37.1\ \text{mm}^a$, $r_2 = 31.9\ \text{mm}^b$ |
| Semicond. screens | $\delta = 3\ \text{mm}$ (thickness) | |
| Core insulation | $\varepsilon_{r1} = 2.5$, $\tan \delta = 0.0008$ | |
| Metallic sheath $\rho = 2.84 \times 10^{-8}\ \Omega\text{m}$ | $r_3 = 56.4\ \text{mm}$, $r_4 = 57.2\ \text{mm}$ | $r_3 = 59.9\ \text{mm}$, $r_4 = 60.7\ \text{mm}$ |
| Outer insulation $\varepsilon_{r2} = 2.5$, $\tan \delta = 0.001$ | $r_5 = 62.2\ \text{mm}$ | $r_5 = 65.7\ \text{mm}$ |
| HDPE tubes $\varepsilon_{r3} = 2.5$, $\tan \delta = 0.001$ | $D_1 = 198.5\ \text{mm}$, $D_2 = 225\ \text{mm}$ | |

^a^ Nominal