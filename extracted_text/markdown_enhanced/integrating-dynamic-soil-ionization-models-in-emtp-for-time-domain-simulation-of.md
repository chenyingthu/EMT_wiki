# Integrating dynamic soil ionization models in EMTP for time-domain simulation of grounding resistance
Ruyguara A. Meyberg a,* , Maria Teresa Correia de Barros c , Jean Mahseredjian b
a RTE International, 69007, Lyon, France
b Polytechnique Montreal, Montreal, QC H3T 1J4, Canada
c Instituto Superior Tecnico, Universidade de Lisboa, 1049-001 Lisbon, Portugal

**Keywords:** Electromagnetic transient simulation, Grounding electrode, Simulation, Soil ionization, Surge

**Abstract:** Soil ionization can have a significant impact on the surge characteristics of grounding electrodes and should be considered when assessing the lightning performance of concentrate arrangements of grounding electrodes in power systems. The dynamics of this phenomenon can be properly represented by the variation in soil resistivity, an approach successfully applied in finite-difference time-domain (FDTD) simulations. The FDTD method, however, has a high computational cost, making it unsuitable for large scale cases. This article presents the integration of existing soil ionization models, based on the variable resistivity approach, into the Electromagnetic Transients Program (EMTP®) via a dynamic link library (DLL), for calculating grounding resistance. Three application examples are presented, and the results are compared with measurements and values calculated in the literature using FDTD. Single vertical rods and four parallel rods with bipolar or unipolar injected currents are covered. The results show good accuracy and remarkable agreement with FDTD results, demonstrating their equivalence and great potential in representing the phenomenon accurately in high-performance electromagnetic transients software.

*This work was supported by NSERC IRC grant, Hydro-Quebec, EDF, Opal-RT and RTE.*
*Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.*
* Corresponding author.
E-mail addresses: ruyguara.meyberg@rte-international.com (R.A. Meyberg), teresa.correiadebarros@tecnico.ulisboa.pt (M.T. Correia de Barros), jean.mahseredjian@polymtl.ca (J. Mahseredjian).

## 1. Introduction
LIGHTNING performance of power systems depends greatly on the surge characteristics of the grounding electrodes, whose representation can become particularly complex when the effects of soil ionization are considered. This phenomenon occurs when large current densities flow from the grounding electrode into the soil, leading to exceeding the disruptive electric field of the soil. Corona-type discharges occur around the electrode and the conductivity of the ionized region increases, reducing the electrode grounding resistance.

Different approaches for representing the impact of soil ionization on grounding resistance can be found in literature. Some authors represent it by increasing the electrode transversal dimensions [1–4]; others by varying the soil resistivity [5,6]; or by empirical expressions [7–9].

Empirical models represent a conservative simplification of the phenomenon [8] but are widely used (see [10–13]) due to their simplicity and easy implementation in electromagnetic transient (EMT) simulation programs. The variable soil resistivity approach has been employed in finite-difference time-domain (FDTD) [14] simulations, and shows good accuracy for various electrode configurations and surges, see [15–17]. In this approach, proposed in [15], the electric field strength and the resulting resistivity variation are calculated in each FDTD cell depicting the soil, and the electrode resistance is modified due to the local soil resistivity variations. This FDTD method, however, has a high computational burden, as it requires the use of a refined mesh close to the electrode, and a small simulation time-step, which is related to the smallest cell size used. Therefore, despite its accuracy and the importance of representing the phenomenon, the method has not been used in larger-scale FDTD simulations, such as those involving lightning strikes on transmission towers, see [18–21]. In [22], a new method is proposed for representing the effect of soil ionization on grounding resistance in FDTD simulations. The method is also based on the variable soil resistivity approach, but avoids mesh refinement by using a dynamic soil ionization model ([5] or [6]), which assumes equipotential surfaces

From the moment the electric field strength reaches the critical value $E_c$, the process of soil ionization begins and the value of the resistivity in the shell varies. In the widely used model [5], the variation in resistivity during soil ionization is represented by
$$ \rho(t) = \rho_0 \exp(- t / \tau_i ) \tag{3} $$
where $\tau_i$ is the ionization time constant. As can be seen, resistivity in (3) only varies as a function of time. In [6] it is proposed that resistivity also varies with the strength of the local electric field, assuming a critical

**Fig. 1.** Scheme of cylindrical-hemisphere equipotential surface for a single