## THREE PHASE TRANSFORMER MODELLING FOR FAST ELECTROMAGNETIC TRANSIENT STUDIES

**B.C. Papadias**, Senior Member IEEE  
**N.D. Hatziargyriou**, Senior Member IEEE  
**J.A. Bakopulos**, Student Member IEEE  
**J.M. Prousalidis**, Student Member IEEE  
*Electric Energy Systems Laboratory, Department of Electrical Engineering, National Technical University, Athens, GREECE*

**Keywords:** transformer modelling, EMTP, switching overvoltages, interruption of small inductive currents.

### Abstract
In this paper the overvoltages produced by switching the primary side of reactor loaded transformers are simulated using the Electromagnetic Transients Program (EMTP). Attention is focused on transformer modelling. Five general three-phase transformer models are used and from the results obtained, and comparisons with field tests positive conclusions concerning the reliability and the accuracy of these models in the study of switching fast electromagnetic transients are drawn.

## 1. INTRODUCTION

Reactive compensation, which is a necessity in many systems, is often provided by reactor coils, connected at the medium voltage tertiary winding of autotransformers.

If, for any reason, the circuit breakers positioned on the primary side are tripped to disconnect the transformer from the system, a considerable overvoltage is developed due to the interaction between the inductive and the capacitive parts of the transformer and the reactor, [13]. This overvoltage can be harmful to the insulation and the interruption itself may not be successfully accomplished. Subsequent phenomena such as reignitions of the breaker contacts, are also usual.

The circuit breaker disconnects the transformer when the current value of each phase comes close to zero, when current chopping occurs. Hence, the three phases are not electrically interrupted simultaneously. Due to the highly inductive behaviour of the circuit which is to be switched off, the instantaneous value of voltage at the time of interruption is close to peak upon current interruption. The magnetic energy stored in the inductances $L$ is now transferred to the stray capacitances $C$ of the circuit, according to the general formula of energy preservation principle:
$$\frac{1}{2}Li^2 = \frac{1}{2}Cv^2$$
where $i$ and $v$ are the instantaneous current and voltage values.

Due to the small value of the capacitances the developed switching overvoltages are high. Considering that the latter is superposed to the high, close to peak, voltage at the interruption, the total voltage can be extremely high. In addition, due to the interphase coupling the phases, which have already been interrupted, are also affected. Thus, a variety of frequencies appear on the voltage waveforms of interrupted phases on the primary side. Obviously, the voltage of the first to clear phase will include all these frequencies. It is worth noting that in this phenomenon the secondary side of the transformer does not participate and, thus, it does not need to be considered, [11]. Therefore in the following, the tertiary winding will be mentioned as secondary.

Considerable research has been carried out concerning the various factors affecting the above phenomenon. Hence [1-7] gives a thorough description of the phenomenon and its sensitivity on the various factors are investigated. In [8,9] similar phenomena without the participation of a transformer have been studied. On the other hand very few data on experimental tests have been published.

The purpose of this paper is to compare the performance of the transformer models developed so far, in the simulation of the overvoltages caused by the interruption of small inductive currents, using the widely known Electromagnetic Transients Program (EMTP) [10,11]. This comparison will test the validity of the various models used and can provide general guidelines for adequate transformer modelling in fast electromagnetic transient phenomena. The basic and critical transformer characteristics to be included in the model are [1]: the capacitances, which are frequency dependent parameters, the leakage inductance, the mutual coupling among the windings of different phases and especially the homopolar one, the winding connection and losses of any kind.

In the present work the characteristics of an actual autotransformer with a tertiary connected reactor have been used. Published field results [12] are used to validate the above simulations.

## 2. THREE PHASE TRANSFORMER MODELLING

During the last decades a number of transformer models have been developed, which have been used for the simulation of a wide range of steady state and transient phenomena. The present paper focuses on those models which can be used to represent a three-phase transformer in fast electromagnetic transient analysis. Thus, very specific, application-dependent models are not considered in the present study. Since EMTP is used for the subsequent simulation, a further requirement is that the models should be set up using the features available in EMTP. This is not a serious limitation however, since EMTP can generally accommodate any model, provided the $V=f(I)$ relationship can be directly expressed. A succinct description of the models studied follows next:

### 2.1 Saturable Transformer Component (STC)

This model is in-built in the EMTP, providing the standard