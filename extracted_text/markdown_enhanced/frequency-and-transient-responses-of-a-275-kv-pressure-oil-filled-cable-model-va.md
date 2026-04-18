# Frequency and transient responses of A 275 kV pressure oil-filled cable: Model validation

Yanfei Liu $^a$, Haoyan Xue $^{c,*}$, Jesus Morales $^b$, Jean Mahseredjian $^a$, Ilhan Kocar $^a$

$^a$ Department of Electrical Engineering, Polytechnique Montréal, Montréal, QC, H3T 0A3, Canada  
$^b$ R&D Division, PGSTech, Montréal, QC, H2K 1C3, Canada  
$^c$ Power System Division, Powertech Labs Inc, Surrey, BC, V3W 7R7, Canada

**Keywords:** Transients, Frequency responses, POF cable, Model validation

**Abstract:** This paper investigates frequency and transient responses on a 275 kV pressure oil-filled (POF) cable. The modeling methods of the POF cable are discussed. The internal propagation characteristics, i.e., inter-sheath and sheath-pipe modes are further investigated. The reduced model of the POF cable is also studied and compared with the results obtained using the detailed model. The input impedance of the POF cable is evaluated based on various mode currents. Electromagnetic transients are also studied, i.e., energization, fault and lightning stroke. Finally, the results of field measurement are used to validate the transient simulation results.

## 1. Introduction

ELECTROMAGNETIC transient (EMT) simulation plays a significant role in the evaluation of power systems for dynamic and transient responses [1]. Depending on the type of study, the required levels of modeling techniques can be different for the components of power systems.

For high voltage power cables, various models can be used, including a PI section, a constant parameter or a frequency dependent model [2]. In EMT-type simulations, the related simulation models should be selected mainly based on frequency consideration and time-step requirement. In this paper, the focus is on accurate frequency dependent modeling for a 275 kV pressure oil-filled (POF) cable [3], which is a typical pipe-type (PT) configuration [4].

The POF cable is implemented in transmission systems. It has three cable cores with oil-impregnated paper insulation, and the cores are drawn into a steel pipe at the construction site. Each core is equipped with helical skid wires, which facilitate the installation of the cores within the pipe. Once the cores are installed and evacuated, the pipe is filled with pressurized oil up to approximate 1.5 kPa. In the engineering applications, the POF cable is typically used for voltages from 69 kV to 345 kV.

In recent years, the POF cables are largely being replaced by XLPE cables for new installations due to their superior performance, lower maintenance requirements, and environmental benefits. However, the POF cables remain relevant in specific high voltage legacy systems and some specialized applications where their robustness and long-term reliability are essential.

In the traditional technique, i.e., Cable Constants, the parameters of POF cable can be evaluated using its PT cable function [5]. It basically assumes the infinite pipe thickness without earth-return loop. If the penetration depth is less than the pipe thickness, the voltage is not induced on the outside of the pipe. As a result, the earth-return current loop (pipe to earth) can be assumed to be zero. Then, the pipe serves as the sole return circuit. This method permits to find the internal parameters of different cores using a PT cable model which is based on the formulas initially proposed in [6], and then improved by [7]. These formulas can deal with the eccentricity of multiple cores within a common metallic pipe based on a filament current assumption in each core. The external parameter (earth-return) represented by Pollaczek’s formula [2] is approximately cascaded with internal parameter to set up full matrices of parameters on a PT cable. It leaves a significant assumption that the internal parameters are evaluated using infinite thickness of pipe with superposition of external parameters calculated by an isolated pipe buried in earth. This method is applicable to conductors when proximity effects can be neglected. However, significant challenges arise in accounting for mutual couplings among the three sheaths and between each sheath and the pipe.

The FEM technique is an alternative approach to overcome the limitations of traditional calculation methods. However, FEM requires dramatically larger computing times which makes it less practical [5].

The recently developed Line/Cable Data (LCD) technique is also available for the computation of the per-unit-length (pul) parameters for PT cables, offering similar accuracy to the FEM method but with much better efficiency. The proposed tool applies the Method of Moments - of the POF cable. As a result, the skid wire holds the same potential level on the sheath since it is closely adhered to the cable sheath. Moreover, the cross-sectional area of the skid wire is smaller than that of the cable sheath, with the majority of the current primarily flowing through the sheath. Therefore, the skid wires are neglected in the following study.

The 275 kV POF cable studied in this paper is modelled as buried 3.22 m underground and the soil resistivity of 100 Ωm is assumed to be frequency-independent. The cable length is 3.384 km.

As shown in Fig. 2, four different c