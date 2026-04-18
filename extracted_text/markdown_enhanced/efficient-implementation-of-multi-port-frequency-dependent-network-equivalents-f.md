# Efficient Implementation of Multi-Port Frequency Dependent Network Equivalents for Electromagnetic Transient Studies using Norton Equivalent Circuits
Claudio Saldaña *, Graciela Calzolari
*Consulting Engineer, Montevideo, Uruguay*

**Keywords:** EMT, FDNE, Norton equivalent, Rational models

**Abstract**
Power system electromagnetic transient studies require that a small part of the electrical network be modelled in detail. The rest of the system is represented by a network equivalent taking into account the frequency dependence of the system components (FDNE). With the purpose of getting a FDNE, this paper presents a procedure for including high-order rational models in EMTP-type simulation programs based on Norton equivalent circuits. This approach has the advantage of using few conductance branches compared to those obtained by fitting any particular circuit structure.
In relation to the work carried out, this paper presents the following issues: a) a procedure for calculating the admittance matrix of the rest of the system as a function of frequency b) this matrix is synthesized in the form of multi-terminal $\pi$-equivalent circuits, whose branches are fitted by rational functions in the pole-residue form c) each partial fraction is converted into a differential equation in time domain. The trapezoidal rule of integration is applied to that differential equation, resulting in a conductance in parallel with a history term current source. Considering all the partial fractions corresponding to a branch, a Norton equivalent circuit is obtained for that branch.
This paper also shows how the procedure is implemented in three different ways in an EMTP-type program, along with the validation of such approach through simulations in an electric utility 500 kV transmission system.

* Corresponding author.
E-mail addresses: claugra07@gmail.com (C. Saldaña), gracielacc99@gmail.com (G. Calzolari).
Submitted to the 22nd Power Systems Computation Conference (PSCC 2022).

## 1. Introduction
The size and complexity of current power systems continue to grow due to the deployment of renewable energy sources and the increased interconnections using high voltage direct current (HVDC) links. Because of this, Electromagnetic Transient (EMT) simulation studies demand a large amount of data and require long computer processing times.
In order to save time and effort, it is common practice in EMT studies to model in detail a selected small area of the power system under study, denominated “study area”. The representation of the rest of the system, termed “external area”, is performed using a frequency dependent network equivalent (FDNE).
The FDNE should be able to replicate the responses of the external area to the changes in the study area with reasonable accuracy, but demanding much less computation.
With the purpose of getting a multi-port FDNE, this paper presents a procedure for including high-order rational models in EMTP-type simulation programs based on Norton equivalent circuits. This approach has the advantage of using few conductance branches compared to those based on the fitting of any particular circuit structure. It is important to note that the procedure followed does not involve the special handling of complex poles.
To validate the procedure, a few switching transient events are simulated in an electric utility 500 kV transmission system. The results obtained with a complete power system representation, along with the FDNE implementations, are compared.
The processing times of the different implementations are also compared.

## 2. External Area Admittance Matrix
The first step for getting the FDNE is to calculate the frequency dependent admittance matrix $Y(\omega)$ of the external area, as seen from its boundary. In the case of a three-phase bus bar, the admittance matrix $Y(\omega)$ is a $3 \times 3$ complex matrix whose elements are functions of frequency. In this work, the frequency domain characteristic of the external area is obtained by frequency scans.
The Harmonic Frequency Scan (HFS) routine of the EMTP-ATP program [1,2] is utilized. This routine performs a sequence of phasor solutions for sinusoidal voltage/current sources of various frequencies, amplitudes and angles specified by the user.
As it is well known EMTP-ATP is a free licensed program widely used by the researches who investigate in the electromagnetic transient area.
To perform frequency scans, it is necessary to have the frequency dependent model of each component of the external area. The models used are presented below.
a) an input data file for the JMARTI SETUP routine should be created. This file contains the geometry of the line and conductor data, three lines of frequency data and one line specifying the output file name.
The first line of the frequency data that bears parameter FREQTRAN, should be replaced by the following line: `$INSERT, LINE1.INS`. The `$INSERT` is an EMTP-ATP command that inserts the `LINE1.INS` file into the input data file. The `LINE1.INS` file contains the value of the parameter FREQTRAN as required by the frequency scan.
The line specifying the output file name should be replaced by the following line: `$INSERT, LINE2.INS`, where `LINE2.INS` is an ASCII file that bears the name of the output file. In this way the name of the output file is changed for each frequency of the frequency sweep.
a) A Fortran 2003 program was written with the purpose of generating `LINE1.INS` and `LINE2.INS` files and calling the JMARTI SETUP routine for each frequency. The program execution produces a set of