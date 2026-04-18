# Grounding grids in electro-magnetic transient simulations with frequency-dependent equivalent circuit

**Alessandro Manunza**  
Electrical Engineer, M2EC, Italy  
*Address:* Manunza Alessandro, Via Copernico n°5, 09060 Settimo San Pietro (CA), Italy.  
*E-mail address:* m2ec@manunza.com.

**Keywords:** Grounding grids, Fast transients, ATP-EMTP, Frequency-dependent equivalent circuit

**Abstract:** The frequency behaviour of a grounding grid cannot be neglected in insulation coordination studies. This paper proposes a new approach, which consists of calculating the frequency behaviour of a grounding grid by means of a software which implements the electromagnetic theory, building a two-port component, whose internal admittances are defined as rational functions in the Laplace domain, and finally using this two-port component for time-domain fast transient simulations.

## 1. Introduction

The behaviour of a grounding grid at power frequencies is well-known, while the behaviour during a fast transient is much more complicated because it requires the knowledge of the physics of a grounding grid in a wide frequency range. Probably for this reason, grounding grids of Overhead Line (OHL) towers are usually simulated by resistors, whose resistances are measured or calculated at power frequency. However, this simple model is not adequate to simulate the physical phenomena during high frequency transients, like those related to lightning. Furthermore, the grounding grids of substations are usually neglected and their components are connected to the ideal ground node, which is the zero-potential node, or they are represented by a resistor, whose resistance is calculated at power frequency. This could be a vague simplification because, from the physical point of view, each grounding grid conductor is coupled with any other conductor by resistive, inductive and capacitive phenomena as well as with all the soil. This means that part of the voltage wave injected in the grounding grid can travel along these buried conductors, while another part is dispersed into the ground. Consequently, different conductors of the grounding grid have different potentials and their impedances are frequency-dependent.

In order to simulate grounding grids, technical literature reports several studies that can be grouped in three main categories:
* **The Network Approach**, based circuit theory methods, including distributed parameters typically used for transmission line modelling.
* **The Electromagnetic Approach** is based on the electromagnetic theory and with the least neglects possible.
* **Hybrid Approach**, which applies the electromagnetic theory to obtain an equivalent circuit.

The transmission line approach is a suitable for the considered frequency range and it allows the simulation of even the non-linear phenomenon of soil ionization, but it could be difficult to apply to large grounding grids [4,7,11,13,14].

The electromagnetic approach allows the construction of a complete model, but is difficult to interface with software programs for the simulation of power systems subject to fast transients.

The hybrid approach can implement most of the advantages of the electromagnetic approach but permits building a model that can be integrated inside software for transient simulations [3,5,9,12,15,16,17].

After neglecting the breakdown phenomena of the soil ionisation and the mutual coupling between underground and above-ground structures, this paper proposes a new hybrid approach, which consists of three steps:
1. Use of software, named XGSLab [18], to calculate the frequency behaviour of a grounding grid;
2. Building a two-port component, whose internal admittances are defined as rational functions in the Laplace domain;
3. Finally, the two-port component is used in software, named ATP-EMTP [1], for time-domain fast transient simulations.

The proposed method is similar to the one described in [17]. The main difference lies in how the grounding grid is modelled in ATP-EMTP: the authors of [17] represented the grounding grid by means of two branches in parallel. Each branch is composed by a rational function in the Laplace domain and a voltage source controlled by an algorithm written in language MODELS. This language is interpreted during the simulation and consequently is time consuming. The grounding grid model proposed in this paper is composed by a simple passive network of components, which are directly implemented inside ATP-EMTP. The proposed approach is more straightforward and less time consuming and can be applied to any kind of soil model and any shape of grounding grid.

## 2. High frequency model

In an HV substation, usually an incoming voltage surge ($V_A$) is deemed sufficient to model it as a two-port component: port 1 corresponds to the point of connection of the surge arrester, while port 2 is the point of connection of the transformer. The chosen internal model for this two-port component is a PI circuit, composed by $Z_1(\omega)$, $Z_2(\omega)$ and $Z_3(\omega)$, shown in Fig. 1. $Z_1(\omega)$ and $Z_3(\omega)$ allow the simulation of the current dispersed into the ground in correspondence of the surge arrester and the transformer, while $Z_2(\omega)$ allows the modelling of the wave propagation between these two points.

**Fig. 1.** Equivalent circuit.

**Fig. 3.** Substation grounding grid.

In ord