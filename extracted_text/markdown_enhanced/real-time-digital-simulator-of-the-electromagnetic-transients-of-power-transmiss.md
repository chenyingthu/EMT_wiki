# REAL-TIME DIGITAL SIMULATOR OF THE ELECTROMAGNETIC TRANSIENTS OF POWER TRANSMISSION LINES

**R.M. Mathur**, Senior Member  
Faculty of Engineering Science  
The University of Western Ontario  
London, Canada N6A 5B9  

**Xuegong Wang**  
Dept. of Electrical Engineering  
The University of Manitoba  
Winnipeg, Canada R3T 2N2  

**ABSTRACT** This paper presents the theory and results of a new real-time digital simulator of transmission lines. The simulator is based on time domain formulation. It obtains the electromagnetic transient performance of balanced three-phase lines in real-time. Sample results of energizing a transmission line from balanced and unbalanced sources are presented. The real-time digital simulator results are verified for accuracy by simulating the same system, off line, on EMTP program. The newly developed real-time digital simulator can readily be incorporated into modern TNA and hvdc simulators. Their application, in place of large number of $\pi$ or $T$ sections of passive networks, is economical, space saving and accurate. As well the realization of real-time digital simulators of transmission lines signals the imminent arrival of totally digital, real-time simulators of power networks.

**KEYWORDS:** Distributed lines; Validation by EMTP; Digital signal processing.

## INTRODUCTION

This paper presents for the first time, real-time digital simulation of the electromagnetic transient performance of a power transmission line. Real-time simulation implies computation and reproduction of a phenomena which is likely to take place if a test was performed.

Real-time simulation of a comparatively slow changing electrical system is easy to accomplish with the help of a modern, general purpose computer. In such simulation it is usually adequate to use a phasor domain mathematical model.

The subject of this paper deals with a much more difficult problem where electromagnetic transient simulation is desired in real-time. Currently this need is fulfilled by transient network analysers (TNA) and hvdc simulators which rely largely on reduced scale modelling of power system components.

Reliable mathematical models and numerical techniques for time domain simulation of the electromagnetic transient performance of power systems have been available for some time. Two well known examples are EMTP and EMTDC computer programs. Also, the techniques have been validated by test results [1] [2]. Such simulation is however performed off line. That is, the computation time of an event turns out to be orders of magnitude longer than the actual event time.

Under the circumstances intense efforts are underway to develop reliable and economical alternatives to TNA. Application of electronic analog simulators, also called parity simulators [3] is one solution. The other is the digital solution which takes advantage of new hardware and novel architecture [4].

Real-time digital simulation of the synchronous machines has been an important step in this direction [5]. In this paper realization of real-time digital simulation of transmission lines is described. This simulation is of great value for the current use and is of a significant importance for future developments as described below.

### Current Application

In TNA and hvdc simulators transmission line modelling is done by connecting a large number of $\pi$ or $T$ sections made up of passive circuit elements each section representing typically $15$ to $50$ km line length. The models occupy majority space and indeed become fairly expensive part of the TNA/hvdc simulator. Further more, representation of frequency dependent ground modes require special attention. A digital transmission line model connected between appropriate buses through controlled current amplifiers offers a neat, flexible and economical solution. In our judgment the market is ready to adopt this technology right now.

### Future Applications

Availability of real-time, digital, transmission line models, considerably advance the state-of-the-art for the realization of a totally digital alternative of TNA and hvdc simulator. Also, one needs to proceed only marginally further to have these digital simulators operating faster than the real-time in order to be able to employ them for predictive control and protection.

This paper presents the mathematical foundation of the chosen technique, discusses the selection and architecture of hardware and presents a digital model. As well, the real-time performance of this model is compared with the predicted energization performance of a balanced three phase line by using EMTP simulation. The results demonstrate that the proposed model is accurate, flexible and reliable.

## DIGITAL MODELLING OF TRANSMISSION LINES

Conceptually two mathematical approaches are available.

(a) Time domain formulation: where a solution is obtained in sequential time steps.

(b) Frequency domain formulation: in which the solution is constituted from discrete frequency points.

Marti et al [6] provide a valuable comparative evaluation of the two techniques. Considering that the real-time transmission line model may have to deal with switching operations, system non-linearities and simulations lending to and maintaining steady-state for considerably long time, the time domain formulation is chosen. Although it is recognized that modelling of frequency dependent line parameters will be cumbersome and