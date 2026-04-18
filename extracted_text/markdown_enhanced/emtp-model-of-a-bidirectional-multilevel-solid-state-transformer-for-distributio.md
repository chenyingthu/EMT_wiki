# EMTP Model of a Bidirectional Multilevel Solid State Transformer for Distribution System Studies
Francisco González, and Jacinto Martin-Arnedo, Salvador Alepuz, and Juan A. Martinez, Senior Member, IEEE

**Abstract**—This paper presents a model for a MV/LV bidirectional solid state transformer (SST) for distribution system studies. A multilevel converter configuration is used in the MV side for voltage and current harmonic reduction. The model has been implemented in the ATP version of the EMTP. Several case studies have been carried out in order to evaluate the behavior of the SST model under different operating conditions and test the impact on the power quality.

**Index Terms**—Bidirectional power electronics converter, distribution system, dual active bridge converter, EMTP, modeling, multilevel topology, power quality, pulse width modulation (PWM), solid state transformer.

## I. INTRODUCTION
THE conventional iron-and-copper transformer has been, and still is, the traditional link between end-users and the distribution network. However, the solid state-transformer (SST) is foreseen as a potential replacement of the conventional transformer and a fundamental component of the future smart grid. Compared to the conventional transformer, the SST offers reduced size and weight, and significant enhancements in power quality performance [1]-[3].

A realistic configuration for the MV side of the SST, assuming Si-based technologies are used, must consider multilevel converters [4], some of them based on a modular structure [5].

A MV/LV SST model using a three-level converter for its MV side converter is presented here. The goal is to develop a custom-made SST model for EMTP (ElectroMagnetic Transient Program) implementation [6]. The approach followed in this work is to obtain an encapsulated model that could be easily used in distribution system studies for which an EMTP-like tool was applied. This model will be the base for a future modular structure; see for instance [5].

The document is organized as follows. The configuration of the proposed bidirectional SST and the switching strategies are presented in Section II. The transformer model has been implemented in the ATP version of the EMTP. Section III presents the system used in this work for testing the behavior of the bidirectional SST, and several simulation results that verify the validity of the proposed model and confirm the enhanced behavior of the SST in comparison to the conventional transformer. Main conclusions and future development are discussed in Section IV.

Francisco González is with the Dept. of Electrical Engineering, Universitat Rovira i Virgili, Tarragona, Spain.
Jacinto Martin-Arnedo is with Estabanell Energia, Granollers, Spain.
Salvador Alepuz is with the Mataró School of Engineering (Tecnocampus Mataró-Maresme), Mataró, Spain.

## II. SOLID STATE TRANSFORMER CONFIGURATION AND SWITCHING STRATEGIES
### A. System description
The bidirectional SST includes three parts: a high-voltage stage, an isolation stage, and a low-voltage stage [7]. Fig. 1 shows the configuration.

The input voltage at power frequency is first converted into dc voltage by the HV-side three-phase pulse width modulated (PWM) Neutral Point Clamped (NPC) converter [8] working as rectifier, see Fig. 1a.

The isolation stage is implemented by means of a dual active bridge dc-dc converter, see Fig 1b. This stage consists of three series-connected subsystems: A dc-to-staircase voltage waveform, a high-frequency transformer and a square wave-to-dc converter.

The HV-side converter shown in Fig. 1b has been implemented with two three-level NPC legs in an H-bridge, similar to an inverter [4], which converts the HV dc voltage into a high-frequency five-level staircase voltage waveform applied to the primary of the high-frequency transformer [9].

In the secondary side, the H-bridge has a conventional square wave voltage waveform with 50% duty cycle, converting the transformed high-frequency square voltage waveform into a LV dc voltage by the LV-side converter.

Finally, the LV-side three-phase PWM dc/ac converter shown in Fig. 1c works as inverter and provides the output power-frequency ac waveform to LV loads.

When the power flow comes from the secondary side, in case it operates in generation mode, the transformer behavior is similar to that described above. Basically, input and output stages swap functions, so the converters, the respective switching strategies and control methods must be properly designed to work under bidirectional power flow conditions.

### B. Switching strategies and control description
A simple but very effective strategy, the voltage oriented control (VOC), with feedforward of the negative-sequence grid voltage [10] has been applied in this work for the NPC converter shown in Fig. 1a. A sequence separation method is applied to the grid voltag