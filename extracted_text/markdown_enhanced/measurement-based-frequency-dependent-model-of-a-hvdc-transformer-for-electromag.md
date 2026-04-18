# Measurement-based frequency-dependent model of a HVDC transformer for electromagnetic transient studies
**Bjørn Gustavsen\*, Yannick Vernay**  
SINTEF Energy Research, P.O. Box 4761 Sluppen, Trondheim, NO-7465, Norway

**Keywords:**  
HVDC transformer  
Measurements  
Black box model  
Electromagnetic transients

**Abstract:**  
A wide-band, frequency-dependent five-terminal model is developed that represents one HVDC transformer unit in the French-English IFA2000 HVDC interconnection. Three such interconnected 1-ph units constitute one 3-ph transformer bank needed in 12-pulse conversion. The model is obtained via admittance frequency sweep measurements on the transformer's terminals, including common-mode measurements to capture the high-impedance coupling to earth at lower frequencies. The data set is modified to reduce the magnetizing current to a realistic level by a novel eigenvalue scaling procedure. The final data set is subjected to modeling by a stable and passive rational model while utilizing a mode-revealing transformation to retain the accuracy of the small eigenvalues that are related to the high-impedance coupling to earth. The paper describes details related to the measurements and modeling steps as well as the many intermediate accuracy validations that were done. Also is described challenges in the measurements that resulted due to interference of the measurements by a nearby 400 kV overhead line. The model is applied in a time domain simulation of the complete HVDC link in normal operation where voltage waveforms resulting from line commutations are compared against those by a classical model with added stray capacitances.

## 1. Introduction
HVDC transformers are together with thyristor valves the fundamental components in any LCC-type HVDC converter. The protection of these transformers is therefore essential for the reliable operation of the HVDC link. Overvoltages due to switching events, lightning impulses and in-station flashovers on the AC side result in steep-fronted overvoltages that stress the transformer AC side insulation parts, and voltages are also transferred to the DC-side where they stress and interfere the thyristor components [1]. Conversely, line faults and lightning strokes to a DC overhead line may result in overvoltages that impose stresses on the transformer DC-side terminals. The protection of HVDC substation against overvoltages therefore requires insulation co-ordination studies to be performed to determine the appropriate location of surge arresters [1].

Insulation co-ordination studies requires the use of models with adequate accuracy up to several hundred kHz in order to represent the actual waveshapes of the overvoltages. The representation of the HVDC transformer is a main obstacle in such studies since frequency-dependent transformer models are in general not available. Therefore, simplified models are usually employed, often consisting of a 50 Hz model in combination with lumped capacitors.

To overcome the accuracy limitation of simplified transformer models, one must use of either a detailed white-box transformer model [2–7] supplied by the manufacturer, or one may extract a black-box model [8–12] of the transformer from terminal measurements. The latter is of course only possible if the transformer has already been built, or if there is a sister unit available. The use of black-box models is attractive because a high level of accuracy can often be achieved compared to a white-box models calculated from detailed design data.

In this work we demonstrate for the first time the use of black-box modeling to an HVDC transformer. The transformer is a single-phase unit belonging to the French-English IFA2000 interconnection. Using a dedicated equipment for frequency sweep measurements of the transformer's terminal voltage/current characteristics, we obtain a multi-port admittance description under the assumption of linear behavior. From the admittance description we extract a stable and passive rational model (state-space) which is amenable for inclusion in general simulation programs of electromagnetic transients such as EMTP-RV, PSCAD and ATP. We demonstrate the many steps in the measurement and modeling process, including the required validation of measurement accuracy and consistency in both frequency domain and time domain, as well as in the model extraction step. The challenges due to interference from a nearby 400 kV HVAC line are also demonstrated.

## 2. HVDC transformer
Fig. 1. HVDC transformers utilized in bipolar 12-pulse configuration.

Two important contributions in this work are (1) handling of two ungrounded windings (which leads to widely different modal components towards lower frequencies), and (2) a procedure to obtain a realistic magnetizing current at 50 Hz (since small-signal measurements give unrealistically large magnetizing currents). Finally, we demonstrate the application of the model in a simulation of the complete HVDC link where we compare the effect of commutation induced voltage waveforms against those by a simplified model.

Fig. 3. HVDC 1-ph transformer measurement object.

## 3. Work strategy
The transformer was available for a total of five days. Within this time frame, it was required to connect the measurement equipment, perform measurements, create a model, v