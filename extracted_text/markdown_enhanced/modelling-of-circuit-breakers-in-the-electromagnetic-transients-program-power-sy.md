## MODELLING OF CIRCUIT BREAKERS IN THE ELECTROMAGNETIC TRANSIENTS PROGRAM

**V. I. PHANIRAJ**, Student Member, IEEE  
**A. G. PHADKE**, Fellow, IEEE  
*Virginia Polytechnic Institute and State University*

**ABSTRACT** - The recent publication of experimental and theoretical results from verified arc models has made possible the implementation and testing of a dynamic circuit breaker model in the Electromagnetic Transients Program (EMTP). An estimator was developed to obtain model parameters from test data. Results from this are given, and it’s data requirements specified. To illustrate an application of the model not previously possible with the existing capabilities of EMTP, simulations of load current interruption in a multi-terminal HVDC system were performed. Results from these are included, along with a discussion of the effects of system and model parameter variation on the interruption process.

## INTRODUCTION

The Electromagnetic Transients Program (EMTP) is an extensively used tool for the analysis and simulation of power system transients [1,2]. It contains a large number of independent modules, each modelling a different component such as a transformer, a synchronous machine or a transmission line. Inductances and capacitances are represented by an equivalent circuit consisting of resistances in parallel with current sources. These equivalent circuits are obtained by the application of the trapezoidal rule of integration [1]. Through this transformation, the nodal admittance matrix $[Y]$ becomes real and symmetric, and the differential equations for capacitances and inductances become algebraic equations. Thus the governing equation of the system is:

$$[Y]e(t) = i(t) - [I] \tag{1}$$

where $e(t)$ and $i(t)$ are column vectors of the node voltages and injected currents, and $[I]$ is the known vector of equivalent current sources representing the system history. Eq. (1) is to be solved repeatedly as the simulation progresses, and therefore in order to enhance the program speed, the $[Y]$ matrix is factored and stored in the L-U form. This technique requires that the $[Y]$ matrix remain constant, making it difficult to simulate switches, saturable devices and elements whose impedance is time-varying, such as circuit breakers. The effect of switching operations however can be pre-computed and the resulting modifications made directly to the L-U factors.

Since a large proportion of all power system transients are initiated by circuit breaker operations, the need to represent breakers accurately in EMTP has long been recognized [3]. Until now, the approximations used for modelling circuit breakers included voltage or current controlled switches, and predetermined time-dependent or nonlinear resistances. These are adequate for cases such as Transient Recovery Voltage (TRV) calculation, but are not suitable for many other applications. In particular, phenomena such as thermal and dielectric failure cannot be modelled. A more realistic model would perform these and other functions, and find application in the following types of studies:

* **Circuit Breaker Testing:** With the increase in short-circuit capacity of power systems and the consequent rise in interrupting capabilities, direct testing of breakers is becoming more difficult because of the high short-circuit capacity test source requirement. Though synthetic testing is commonly used, an accurate EMTP model could be used to simulate a direct test, and supplement the synthetic tests.
* **Interruption of Small Inductive Currents:** This situation, which arises often in transformer and reactor switching, may lead to current chopping and multiple restrikes which in turn cause dangerous overvoltages. The model could be used to identify such problems, and determine the nature of corrective action, such as the ratings of a surge arrester to be connected.

The need for a better model having been established, the next task was to choose appropriate models to fulfill the requirements. The main criteria used for selection were:
1. Availability of Model Parameters and Test Results.
2. Numerical Simplicity and Robustness.
3. Range of Applications.

Based on these factors, three models were chosen, and these are discussed in the next section.

## ARC MODELS

The three models chosen for implementation were, (1) the modified Mayr or Avdonin model [4]; (2) the Urbanek model [4]; and (3) the Kopplin model [5].

### Avdonin Model

The Avdonin model equation is:

$$\frac{dr}{dt} = \frac{1}{A} r^{-\alpha} - \frac{1}{A \cdot B} r^{-\alpha-\beta} i v$$

where $v$, $i$ and $r$ are the arc voltage, current and resistance respectively, and $A$, $B$, $\alpha$ and $\beta$ are the breaker model parameters. This model is a derivative of the Mayr model with the time constant $\theta$ replaced by $A r^{\alpha}$ and the power constant $P$ replaced by $B r^{\beta}$. This model has been tested at Hydro-Quebec, and published results are available [4] for validation of the EMTP simulations. The model is capable of representing arc interruption and thermal failure, and has been used for modelling current chopping. It cannot simulate dielectric breakdown or multiple restrikes, but has the advantages of being computationally simple and robust.

stage procedure. At first, the nonlinear element is open-circuited and the response of the network calculated, specifically the open-circuit voltage $V_n$ and the Thevenin impedance $Z_{thev}$. If the nonlinearity can be characterized by the equation:

$$V_n = f(I_n) \tag{5}$$

then the actual value of $I_n$ can be evaluated from

$$V_n - Z_{thev} I_n = f(I_n) \tag{6}$$

where for multiple nonlinearities, $V_n$ and $I_n$ are column