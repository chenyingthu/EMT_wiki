# Dynamic Average-Value Modeling of CIGRE HVDC Benchmark System
**IEEE Task Force on Dynamic Average Modeling**

H. Atighechi, S. Chiniforoosh, J. Jatskevich, TF Chair, A. Davoudi, J. A. Martinez, M. O. Faruque, V. Sood, M. Saeedifard, J. M. Cano, J. Mahseredjian, D. C. Aliprantis, and K. Strunz

**Abstract—**High-voltage direct-current (HVDC) systems play an important role in modern energy grids, whereas efficient and accurate models are often needed for system-level studies. Due to the inherent switching in HVDC converters, the detailed switch-level models are computationally expensive for the simulation of large-signal transients and hard to linearize for small-signal frequency-domain characterization. In this paper, a dynamic average-value model (AVM) of the first CIGRE HVDC benchmark system is developed in a state-variable-based simulator, such as Matlab/Simulink, and nodal-analysis-based electromagnetic transient program (EMTP), such as PSCAD/EMTDC. The 12-pulse converters in the HVDC system are modeled with a set of nonlinear algebraic functions that are extracted numerically. The results from the average-value models are compared with the results of the detailed simulation to verify the accuracy of the AVMs in predicting the large-signal time-domain transients. The developed dynamic average models are shown to have computational advantages.

**Index Terms—**Average-value modeling, CIGRE HVDC benchmark, electromagnetic transients, inverter, line-commutated converter, rectifier.

Manuscript received August 20, 2012; revised July 31, 2013 and January 13, 2014; accepted July 16, 2014. Date of publication August 11, 2014; date of current version September 19, 2014. Paper no. TPWRD-00872-2012.

Task Force on Dynamic Average Modeling is with the Working Group on Modeling and Analysis of System Transients Using Digital Programs, General Systems Subcommittee, T&D Committee, IEEE Power & Energy Society.

**Task Force Members:** S. A. Abdulsalam, D. C. Aliprantis, U. Annakkage, H. Atighechi, J. Belanger, J. M. Cano, S. Chiniforoosh, A. Davoudi, V. Dinavahi, O. Faruque, S. Filizadeh, D. Goldsworthy, A. Gole, R. Iravani, J. Jatskevich (Chair), R. Jayasinghe, H. Karimi, M. Kuschke, A. St. Leger, J. Mahseredjian, J. A. Martinez, N. Nair, L. Naredo, T. Noda, J. N. Paquih, J. Peralta, A. Ramirez, A. Rezaei-Zare, M. Rioual, M. Saeedifard, K. Schoder, V. Sood, K. Strunz, A. VanDerMeer, X. Wang, A. Yazdani.

H. Atighechi, S. Chiniforoosh, and J. Jatskevich are with the Electrical and Computer Engineering Department, University of British Columbia, Vancouver, BC V6T 1Z4 Canada.
A. Davoudi is with the Electrical and Computer Engineering Department, University of Texas, Arlington, TX 76011 USA.
J. A. Martinez is with the Department Eng. Electrica-ETSEIB, Universitat Politecnica de Catalunya, Barcelona 08028, Spain.
M. O. Faruque is with the Center for Advanced Power Systems, Florida State University, Tallahassee, FL 32310 USA.
V. Sood is with the Faculty of Engineering and Applied Science, University of Ontario Institute of Technology, Oshawa, ON L1H 7K4 Canada.
M. Saeedifard is with the Electrical and Computer Engineering Department, Purdue University, West Lafayette, IN 47907 USA.
J. M. Cano is with the Universidad de Oviedo, Ingeniería Eléctrica, Gijón 33204, Spain.
J. Mahseredjian is with the Ecole Polytechnique, Montreal, QC H3C 3A7 Canada.
D. C. Aliprantis is with the Electrical and Computer Engineering Department, Iowa State University, Ames, IA 50011 USA.
K. Strunz is with the Technische Universität Berlin, Elektrotechnik und Informatik, Berlin 10587, Germany.

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

## I. INTRODUCTION

HVDC SYSTEMS are frequently employed for long-distance transmission due to their lower electrical losses. For shorter distances, the higher costs of the power-electronic equipment may still be justified due to other benefits achieved by HVDC, such as improved system stability and interconnection between unsynchronized ac systems.

Design and analysis of power-electronic-based systems, such as HVDC transmission, rely extensively on modeling and computer simulation. The procedures for design and analysis of such complex systems typically involve a large number of time-domain transient studies as well as analysis in frequency domain for control purposes.

The detailed modeling of HVDC transmission system, wherein the switching of all devices is represented in full detail, may be readily accomplished in the state-variable-based (SV-based) [1]–[7] and Electromagnetic Transient (EMT) programs (EMTP type) [8]–[12]. Although the efficiency of detailed models can be increased (e.g., [13]), the detailed models are generally computationally expensive, and require significant simulation time especially for system-level studies. Moreover, due to switching, these models are discontinuous and not suitable for small-signal frequency-domain analysis. It is therefore desirable to develop equivalent models that do not include switching and may be used to predict the system’s slower transient behavior and steady-state characteristics.

Developing steady-state and dynamic equivalent models for HVDC transmission systems has been of great interest in the power system research community. Steady-state models for HVDC systems were first proposed in [14] and further improved in [15] and [16]. The effects of harmonics and interharmonics in steady-state HVDC models have been discussed in the literature [17]. The impedance mapping and equivalent circuit of HVDC systems have been considered in [18]. More recent improvements have been made in [1