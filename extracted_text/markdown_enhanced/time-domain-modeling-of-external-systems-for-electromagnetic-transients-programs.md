## TIME DOMAIN MODELING OF EXTERNAL SYSTEMS FOR ELECTROMAGNETIC TRANSIENTS PROGRAMS

Ali Abur and Harinderpal Singh  
Department of Electrical Engineering,  
Texas A&M University  
College Station, Texas 77843

### ABSTRACT
An external network model to be used in Electromagnetic Transients Programs (EMTPs) is developed based on techniques directly applicable in the time domain. This is in contrast to the currently available models which are derived based on the frequency domain methods. The model is in form of a discrete-time filter which is built from the EMTP simulation of the external system’s response to a multisine excitation signal. The developed filter is converted into a Norton equivalent source and integrated into the EMTP model of the study (internal) system. The proposed model is verified by simulating the energization transients on an open-ended transmission line connected to the (external) network in a three phase test system.

**Keywords:** Network Equivalents, Electromagnetic Transients, System Identification, Modeling, Simulations.

## I. Introduction
Power system electromagnetic transients can be simulated very efficiently using time domain methods [1, 2, 3, 4, 5]. Such studies require very detailed modeling of the system under study. Modeling of the entire system in great detail may be prohibitive in terms of available computing resources and time. This is especially true in the case of statistical studies that are conducted to obtain the probability of overvoltages for insulation coordination of an overhead transmission line [6]. In such studies a large number of cases need to be run while the subsystem of interest remains to be a very small part of the entire system. Thus, the use of proper equivalents to reduce the system model complexity will greatly reduce the overall study time.

The conventional power frequency short circuit equivalents cannot accurately represent the external network behavior when the simulated transients have a broad frequency spectrum. The need for accurate network equivalents has long been recognized by various researchers [7, 8, 9, 10, 11]. However, most of the research efforts have concentrated on the frequency domain methods. The external system is replaced by an appropriate network of lumped R, L, and C components whose values are determined in such a way that the equivalent network will have approximately the same frequency response as the external system. This is achieved in the frequency domain via an optimal curve fitting procedure over a wide range of frequencies [7].

In this paper, a time domain equivalencing method will be described. The proposed method avoids the frequency domain altogether and generates a discrete-time equivalent by using the response of the external system to a special excitation signal. No explicit network of R, L and C’s is synthesized to replace the external system. Instead, a discrete-time Norton equivalent for the external system is directly obtained and attached to the study subsystem at the boundary nodes. The proposed equivalent is easy to obtain and can be readily implemented in any existing EMTP. In the paper, the proposed external system modeling approach will be described only for the single port equivalents. However, the same approach can be extended to generate multi-port equivalents as well.

## II. External System Discrete-Time Model
Consider the system shown in Figure 1. In this example it is assumed that the full system is divided into two parts:

1. **Study subsystem** - is the system of interest for studying transients and is modeled in great detail.
2. **External system** - is that part of the full system which is to be represented by an equivalent. Note that while the signals in the external system are of no interest to the user, those generated at the boundary bus are of vital importance. Therefore, it is required that the equivalent produces an accurate response at the boundary, over a broad frequency range, to the signals incoming from the study system.

*Fig. 1. External system and the study subsystem connected at a single port.*

The external system can, in general, be described by a driving-point admittance function $H(s)$ relating the terminal voltage and the injected current at the boundary bus, as given below:

The frequency response of a network consisting of distributed parameter elements (the external system) is known to exhibit multiple and consecutive series/parallel resonances (poles and zeros) [7, 8, 9, 10, 11], the order $p$ (number of lag terms) is related to the frequency range, or bandwidth, for which the model is desired to be valid. Once the order $p$ is specified, then the parameters $a_k$ and $g_t$ of the model have to be estimated and this constitutes the parameter estimation step.