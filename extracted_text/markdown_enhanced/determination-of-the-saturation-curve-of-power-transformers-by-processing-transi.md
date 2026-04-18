## Determination of the saturation curve of power transformers by processing transient measurements
Toussaint Canal *, François-Xavier Zgainski, Vincent-Louis Renouard  
EDF-DTG (General Technical Department), chemin de l’étang, 38950 St-Martin-Le-Vinoux, France

*Corresponding author. E-mail addresses: toussaint.canal@edf.fr (T. Canal), francois.zgainski@edf.fr (F.-X. Zgainski), vincent-louis.renouard@edf.fr (V.-L. Renouard).*

**Keywords:** Transformer re-energization, Saturated inductance, Switching field tests

**Abstract:** The sudden energization of large power transformers may lead to the saturation of the magnetic core and induce resonant overvoltage on weak networks due to low frequency high module inrush currents. The magnetization curve of the transformer and the value of its air-core inductance play a key role in the constraints that can be applied to the equipment due to the switching. The method set out in that document allows to identify the saturation curve of three-phase power transformers from measurements recorded during switching transients.

## 1. Introduction
To ensure Nuclear Safety, several voltage recovery schemes are defined to supply power to a nuclear power-plant facing a total loss of its electrical sources. They consist in re-energizing the auxiliary transformers of the power-plant as fast and as safe as possible in order to supply its safety systems thanks to overhead HV lines of several hundreds of kilometers and an islanded power plant available in the near area of the plant out of power (Fig. 1). Risk analysis studies (based on EMT simulations) and field tests allow to prove the feasibility and the robustness of these recovery schemes [1, 2].

The sudden energization of power transformers may lead to the saturation of the magnetic core and induce RMS-voltage drops and resonant overvoltages due to low frequency high inrush currents [3]. These high overvoltages and inrush currents may damage the involved equipment by causing the failure of the protective systems (surge arresters) [4], dielectric degradations [5] and large deformations due to electrodynamic forces on windings [6]. In the end, these phenomena can lead to the failure of the recovery process.

The magnetization curve of the transformer and the value of its air-core inductance play a key role in the stresses and constraints that can be applied to the equipment. As an example, a 10% overestimation of the saturated inductance, computed from the air-core inductance, can lead to underestimate voltages constraints during the transformer energization by a factor of 30% [7]. An analytical approach was therefore developed in [8] to determine the air-core reactance of transformers with precision, without having to engage heavy computations based on modeling and simulations performed with finite element electromagnetic 3D software.

The method set out in that document allows to identify the saturation curve and the saturated inductance of three-phase large power transformers from several switching transients records. The simple resulting transformers model presents many interests to simulate low frequency transients ($< 1$ kHz).

## 2. Transformer model used in voltage recovery studies and its limitations
In this section, we try to present the well-known model of transformer that is used in voltage recovery studies [1]. The method used to identify its main parameters is also detailed. This section is mainly a presentation of the scientific literature and a reminder of the modeling of transformers for switching studies.

There are complex transformer models available to simulate transformer switching transients [9]. The model of the three-phase shell transformer used here is built from three single phase models whose terminals are connected according to the coupling of the transformer. The following figure shows the example of an Ynd11 three-phase transformer (Fig. 2).

The single phase model used is the traditional “T”-equivalent model (Kapp’s model) that is commonly used for low frequency transient studies (below 1 kHz) (Fig. 3).

This section summarizes how this model is classically established (Part A) and how the proposed method to identify the saturation curve

Fig. 1. Network configuration to re-energize the auxiliary transformer of a nuclear power-plant.

sinusoidal voltage applied at the LV side, the peak value of the magnetizing current at the corresponding flux is adjusted in the model in order to reproduce the RMS values of the no-load current measured in the physical test.

The model provides a relatively good estimation of the knee saturation curve (flux as a function of the magnetizing current) of the power transformer in the linear and possibly the low-saturated area of the curve.

The slope of the saturation curve under highly saturated conditions ($L_{sat}$) is deduced from the value of the air-core inductance provided by the manufacturer. In most cases, this value is calculated by approximate