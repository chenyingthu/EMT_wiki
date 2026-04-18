# Multi-scale formulation of admittance-based modeling of cables

**Felipe Camara**^a^, **Antonio C.S. Lima**^*, b^, **Kai Strunz**^c^

^a^ Furnas Centrais Elétricas, Dept. Electrical Studies and Operation Planning, RJ, Brazil  
^b^ Federal University of Rio de Janeiro, COPPE/UFRJ, RJ, Brazil  
^c^ Technische Universität Berlin, TU-Berlin, SENSE Laboratory, Germany  

\* Corresponding author.  
E-mail addresses: fcamara@furnas.com.br (F. Camara), acsl@coppe.ufrj.br (A.C.S. Lima), kai.strunz@tu-berlin.de (K. Strunz).

**Keywords:** Electromagnetic transients, cable, transmission line, frequency dependency, multi-scale simulation, dynamic phasor, analytic signal

**Abstract:** This paper proposes a novel multi-scale cable model in phase-coordinates exploiting the fully-coupled structure of the nodal admittance matrix instead of using the conventional approach based on the Method of Characteristics (MoC). The usage of the admittance modeling allows a straightforward representation of cables regardless of their lengths as it does not require a minimum time-step below the transient time associated with the fastest mode. In addition, some accuracy issues regarding the rational modeling of the nodal admittance matrix are overcome resorting to the Folded Line Equivalent (FLE) transformation.

Following the so-called frequency-adaptive simulation of transients (FAST) concept, the trapezoidal rule and recursive convolution expressions are rewritten to perform computations using analytic signals or complex variables. This will allow the possibility to combine electromagnetic and electromechanical transients phenomena in the same simulation environment with a unique mathematical model.

A novel variable time-step algorithm is presented and its flexibility is so general that can be incorporated in Electromagnetic Transient (EMT) software such as EMTP-RV, PSCAD or Hypersim in straightforward way.

Besides keeping the accuracy of the classic EMT-modeling, the proposed formulation provides a sensible gain in the overall computation time without significant loss of accuracy and also smooth transitions regardless of the time-step length.

## 1. Introduction

The complexity of electric power systems has increased considerably in the last decades. Besides the deregulation process, there has been an ever growing usage of power electronics devices associated with distributed generation, renewable power such as wind and solar, and HVDC just to name a few. This scenario demands a higher knowledge and a detailed description of the main components of the network instead of the conventional approach based on positive sequence phasor representation. However, a detailed modeling of all the network would demand a computer burden that is barely feasible even considering nowadays computing power. Alternatively, one may resort to a combined approach where a large part of the network is represented in the conventional way with a small part being modeled in more detail. The usage of the so-called hybrid simulation can provide such framework [1].

The joint simulation of electromagnetic transients (EMT) and transient stability (TS) is not a new topic as the first attempts to do so date back to the 1980s [2]. However, integrating these two types of simulators brings up some issues, for instance, communication protocols between algorithms, exchanging data timings, waveform-to-phasor conversions and conversely. In the early 1990s, the concept of time-varying or dynamic phasors was proposed [3] and extended the phasor-based notation to accommodate fast electromagnetic transients. This formulation was then incorporated to power system modeling and stated as Shifted Frequency Analysis (SFA) [4–7].

Later, the so-called Frequency-Adaptive Simulation of Transients (FAST) [8–11] technique applied the dynamic phasor concept in order to allow a variable time-step environment as opposed to interfacing diverse programs.

The modeling of overhead lines and cables are carried out mostly by means of the method of characteristics (MoC). This implies in dealing with a rather small time-step to track the transient behavior [12,13]. This scenario becomes even more restricted in the case of short overhead lines and cables where very small time-steps may be needed as it should be smaller than the travel time of the fastest mode. In the past, very short lines were represented using $\pi$-sections [14] which precludes the possibility to include the frequency dependent behavior.

Recent research with FAST addressed the modeling of transmission lines gathering the structure of a MoC-based constant parameter line model with an equivalent $\pi$-circuit to overcome the limitation of using a time-step shorter than the traveling time [15], i.e., it enables the topological coupling between the line ends when the time-step is larger than the traveling time. Adopting the same concept, the frequency dependency of parameters was introduced in [16].

The aforementioned line models are not a general approach as they cannot deal with underground/submarine cables which present a heavy frequency dependent transformation matrix and cannot consider the case of a full frequency dependent line model for large time-steps. Furthermore, for short lengths, there will be a need to interpolate the model gi

Fig. 2. Fourier spectra signal $s(t)$.