# Development and validation of a new detailed EMT-type component-based load model

M. Torabi Milani $^{a,*}$, B. Khodabakhchian $^{b}$, J. Mahseredjian $^{a}$, K. Sheshyekani $^{a}$

$^{a}$ Polytechnique Montreal, Montreal, QC H3C 3A7, Canada  
$^{b}$ Hydro-Quebec, Montreal, QC H5B 1H7, Canada  

* Corresponding author. E-mail addresses: maryam.torabi@polymtl.ca (M. Torabi Milani), khodabakhchian.bahram@hydroquebec.com (B. Khodabakhchian), jean.mahseredjian@polymtl.ca (J. Mahseredjian), keyhan.sheshyekani@polymtl.ca (K. Sheshyekani).

**Keywords:** Component-based, EMTP simulation, Load modeling

**Abstract:** Load modeling is one of the most important parts in power system simulation. This paper describes the efforts to develop a detailed EMT-type component-based load model. The aim of this new model is to capture the accurate behavior of loads in commercial and residential sectors. The developed model is validated and refined against field data which were recorded by Hydro-Quebec during voltage sag events. The simulations are performed using the time-domain simulation tool EMTP.

## 1. Introduction

LOAD modeling is one of the most important areas in power system modeling. Previous research has reported discrepancies between the recorded and simulated system responses as a result of employing incorrect load models. Examples are several unsuccessful attempts to reproduce the behavior observed in the Swedish blackout in 1983 [1], the Tokyo network collapse of 1987 [2] and the Western Systems Coordinating Council (WSCC) blackout in 1996 [3]. Accordingly, accurate analysis of power systems requires accurate load models.

Load models can be divided into two basic groups, being static and dynamic. Static models describe the load characteristics with respect to voltage and frequency variations assuming no machine dynamics. Existing static models such as exponential load model, polynomial load model (ZIP) and linear load model are described in [4,5]. Various existing dynamic load models including exponential dynamic load model and dynamic models of induction motor have been presented in [4]. Composite load models can represent the structure of a given load as a combination of static and dynamic load components. The most common composite load model is the combination of an induction motor model and a static load. In [6,7], the static part is represented with a conductance and a susceptance in parallel. A ZIP model has been used in [5] and [8] to represent the static component.

To represent aggregated loads at power system buses, two most widely used methodologies exist; the measurement-based and the component-based approach. In the former, load characteristics are derived based on measurements performed in the actual power system. In the latter however, a load model is constructed from the models of the individual load components. Examples of measurement-based approach are available in [9,10]. Component-based approach has been reported in [11,12,13] to develop aggregated household, industrial and residential-commercial loads respectively.

Although the importance of load modeling is generally recognized and different load modeling efforts have been documented in existing literature, little has been done to develop detailed composite load models. Such models provide a more accurate representation of the reality of aggregated loads, as they recognize the diversity in end-use characteristics (e.g., different types of motors and lighting sources). The research papers available on detailed composite load models are [13,14]. The latest development in this field belongs to the composite load model (CMLD) in PSSE [14]. This model is an aggregation of three-phase and single-phase induction motors, power electronics and static loads. However, it suffers from inaccuracy in modeling power electronics and single-phase motors; power electronics are grouped as constant power loads which is a simplistic assumption. The single-phase motor is approximated by a “performance model” using algebraic equations to represent the motor power consumption in terms of terminal voltage.

This paper presents a new detailed component-based load model based on electromagnetic transient (EMT) computations. The aim of this model is to approach the real load behavior under disturbances, e.g., voltage variations. The new model not only captures the diversity in end-use applications, but also includes modern elements such as variable speed drives and energy efficient lighting sources. To the author’s best knowledge, such a comprehensive EMT-type load model has not been previously presented in the literature. The developed model is used to simulate load behavior in voltage variation events, and its performance is validated against field data recorded by Hydro-Quebec. Results of the validation studies reveal the capability of the proposed model in reproducing the measured dynamic behavior of loads during and after a disturbance. Obtaining such results is not possible by employing traditional load models, especially static ones which are the current practice in most dynamic studies [4]. Moreover, in this paper, measured data is also used to derive relevant characteristics of the modelled loads (e.g., connection or reconnection pattern of motor loads during and following voltage sags) which are subsequently exploited in the development and practice of the proposed model. This combination of

*Fig. 2. SMPS circuit topology.*

**Table 1** Equivalent resistance of SMPS and CFL.
| Component | $R_{eq}$ |
|---|---|
| SMPS | $v_{dc}^2$ |