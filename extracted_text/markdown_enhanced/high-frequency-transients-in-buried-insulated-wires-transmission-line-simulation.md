## High-frequency transients in buried insulated wires: Transmission line simulations and experimental validation

Rafael Alipio $^{a,b,*}$, Naiara Duarte $^{a,b}$, Farhad Rachidi $^a$

$^a$ École Polytechnique Fédérale de Lausanne (EPFL), Lausanne, Switzerland  
$^b$ Laboratory of Electromagnetic Transients (LabTEM), Federal Center of Technological Education of Minas Gerais (CEFET-MG), Belo Horizonte, Brazil  

* Corresponding author. E-mail address: rafael.alipio@cefetmg.br (R. Alipio).

**Keywords:** Underground insulated cables, Measurements, Transients, Ground admittance, Ground impedance

**Abstract:** This paper presents experimental results on the transient response of a buried insulated wire subjected to fast transient signals. It reports measurements of voltage and current at the sending end, as well as the voltage at the receiving end of the insulated wire. The obtained experimental results are utilized to assess the accuracy of recent formulations proposed for computing the ground-return impedance and admittance of underground cables, which are important for simulation of transients using models based on the transmission line theory. The good agreement between measurements and simulations bolsters confidence in incorporating these newly proposed expressions for computing the cable’s ground-return parameters into EMT-type simulators.

## 1. Introduction

In recent years, the use of underground cables in electrical power utilities has seen a notable rise [1]. This trend encompasses a variety of applications, including the construction of new underground and hybrid power lines, as well as the extensive use of underground cables in renewable energy plants for collecting power from individual solar panels or wind turbines to the interconnecting substation. These systems are susceptible to transients from both internal and external sources, underlining the importance of accurately modeling underground cables for simulations needed in defining effective protective measures and devices [2].

Electromagnetic transient (EMT) simulations are typically conducted on EMT-type platforms, which leverage circuit and transmission line theories for efficient simulations. The reliability of these simulations heavily relies on the accuracy of the implemented models within these platforms. Recent efforts have focused on refining expressions for computing the per-unit-length (pul) ground-return impedance and admittance of underground cables, required in models based on the transmission line theory [3,4]. The validity of these expressions has been assessed through comparison with full-wave 3D finite-difference time-domain (FDTD) simulations [5,6]. However, the literature still lacks comprehensive comparisons with experimental data. Such comparisons are essential to bolster the reliability of these expressions, paving the way for their effective application and integration into commercial EMT-type platforms.

This paper takes a step in that direction and presents a first set of measurements of the transient response of an underground cable. The presented data fill the gap in the existing literature since earlier publications lack specific measurements for validating the earth-return effect in underground cables. In the conducted experiments, a single dielectric-coated wire was considered. Given that the main objective of this paper is to address the earth-return effect in underground cables, the use of a dielectric-coated wire is adequate to demonstrate the influence of ground-return parameters on the cable transient response [7,8]. This study provides experimental data and incorporates simulation results to further validate existing expressions for computing the ground-return impedance and admittance of underground cables.

## 2. Background on underground cable modeling using transmission line theory

The pul series impedance and shunt admittance of single dielectric-coated wire buried in ground is given, respectively, by [9]:

$$Z = Z_i + Z_e + Z_g \tag{1}$$

$$Y = \left( Y_e^{-1} + Y_g^{-1} \right)^{-1} \tag{2}$$

where $Z_i$ is the conductor internal impedance, $Z_e$ is the external impedance due to the magnetic field within the insulation, given by (3), $Z_g$ is the ground-return impedance, $Y_e$ is the external admittance due to the electric field within the insulation, given by (4), and $Y_g$ is the ground-return admittance. In (3) and (4), $a$ and $b$ are respectively the radius of the inner conductor and the cable outer radius, and $\varepsilon_{in}$ is the permittivity of the insulating layer.

$$Z_e = \frac{j\omega\mu_0}{2\pi} \ln\left(\frac{b}{a}\right) \tag{3}$$

different internal structures can be straightforwardly performed by applying the formulation proposed by Ametani [9], which constitutes the basis of the cable constants routines in EMT-type programs. Since the main goal of our paper is to investigate the validity of ground-return parameter equations, the internal structure of the cable was simplified to a solid core surrounded by a dielectric layer.

In order to show the differences between the results obtained using each formulation to compute the ground-return parameters, Fig. 1 presents the simulated voltage at the receiving end of a 100-m long insulated