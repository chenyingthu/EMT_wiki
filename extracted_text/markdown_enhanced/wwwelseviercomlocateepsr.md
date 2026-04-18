# Vacuum circuit breaker modelling for the assessment of transient recovery voltages: Application to various network configurations

C.L. Bak^a^, A. Borghetti^b^, J. Glasdam^a^, J. Hjerrild^c^, F. Napolitano^b,∗^, C.A. Nucci^b^, M. Paolone^d^

^a^ Institute of Energy Technology, Aalborg University, Denmark  
^b^ University of Bologna, Italy  
^c^ DONG Energy, Denmark  
^d^ École Polytechnique Fédérale de Lausanne, Switzerland  

∗ Corresponding author.  
E-mail address: fabio.napolitano@unibo.it (F. Napolitano).

**Article history:**  
Received 24 October 2016  
Received in revised form 22 September 2017  
Accepted 12 November 2017  
Available online 25 November 2017  

**Keywords:**  
Vacuum circuit breakers  
Transient recovery voltages  
Motor inrush currents  
Cable inrush currents  
Wind farms  
EMTP simulations  

**Abstract**  
Vacuum circuit breakers (VCBs) are widely used for medium voltage applications when low maintenance, long operating life, and large number of allowable switching cycles are required. The accurate estimation of the transient recovery voltages (TRVs) associated with their switching operation is indispensable for both VCB sizing and insulation coordination studies of the components nearby the switching device. In this respect, their accurate modelling, which is the object of the paper, becomes crucial. In particular, the paper illustrates two applications of a VCB model, which show the model capabilities of simulating TRVs due to opening/closing operation, namely the switching of large electrical motors and the switching of cables collecting offshore wind farms (OWFs). Data from digital fault recorder (DFR) in a water-pumping plant and from a measurement campaign in an OWF using a high-bandwidth GPS-synchronised measurement system, respectively, are used for model validation. It is shown that the inclusion of detailed VCB models significantly improves the agreement between the measurements related to both pre- and restrikes and the corresponding simulation results obtained by using two well-known electromagnetic transient simulation environments, namely, EMTP-RV and PSCAD/EMTDC. The procedure adopted for the identification of the VCB model parameters is described.

## 1. Introduction

Several international standards provide indications on the sizing of vacuum circuit breakers (VCBs) taking into account the effect of transient recovery voltages (TRVs) occurring during closing and opening switching operations (e.g., [1–3]). The sizing methods described in the standards cover most of the possible operating conditions of the VCBs, which are characterised by an improved reliability with respect other types of circuit breakers [4]. However, some peculiar scenarios exist that may require more detailed studies and the use of electromagnetic transient simulations. This paper deals with two of such typical scenarios: (a) the case in which the VCB is demanded to interrupt the inrush current of a large motor shortly after the closing sequence due to the intervention of a motor relay; (b) the switching of cables collecting offshore wind farms (OWFs).

In the former scenario, the VCB is requested to interrupt a large inductive current with a superposed a-periodic component. The combination of peculiar systems configurations, together with the VCB’s fast recovery of its dielectric strength and ability to interrupt high-frequency currents, might result in large TRVs and VCB current re-ignition [5].

The latter scenario is particularly interesting since the possible consequences of components failures associated to OWFs are more severe compared to land based ones due to higher repair costs and loss of revenue [6]. Since switching overvoltages are the possible cause of component failures observed in some existing OWFs [7], simulations are widely used for the identification of the overvoltages experienced by the electrical equipment in the OWF, as well as for assessment of the adequacy of the adopted design decisions [8]. In Refs. [8,9] it has been shown that insufficient representation of the VCB is the main cause of discrepancies between measurement and simulation results of inrushes occurring in OWFs.

The post-current zero period of VCBs is well described in the literature (e.g., [10,11] and references therein). In particular, the re-ignition behaviour when the VCB is called upon interrupting a low amplitude inductive current has been investigated in several studies (e.g., [12–19]). Similarly, the occurrence of multiple prestrikes during the VCB closing sequence in OWFs have been investigated in, e.g., Refs. [8,9,20–23].

The purpose of this paper is to present the application of a VCB electromagnetic transient (EMT) model for the accurate assessment of the TRVs generated both during opening and closing switching operations and its implementation in two well-known simulation environments, namely, EMTP-RV and PSCAD/EMTDC. The VCB model is capable to represent the main phenomena taking place in

### 2.2. VCB model

The specific characteristics of the VCB model are described in the following for the opening and closing sequences. As this paper deals with two scenarios, one relevant to the opening switching of the large inductive currents of motor start-ups, and the other relevant to the closing operation in an OWF,