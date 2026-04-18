# Development of Data Translators for Interfacing Power-Flow Programs With EMTP-Type Programs: Challenges and Lessons Learned

**Task Force on Interfacing Techniques for Simulation Tools**

Francisco de León, Dariusz Czarkowski, Vitaly Spitsa, Juan A. Martinez, Taku Noda, Reza Iravani, Xiaoyu Wang, Ali Davoudi, Gary W. Chang, Ali Mehrizi-Sani, and Ilhan Kocar

**Abstract—**This paper describes the challenges and lessons learned when developing industrial-grade data translators aimed for the interfacing of power-flow programs with Electromagnetic Transients Program-type programs. It has been found that the greatest challenges to overcome include: 1) the lack, in the databases used in power-flow programs, of vital pieces of information necessary to perform transient studies; 2) inconsistency in the format of data files; 3) the presence of data entry mistakes in very large databases; 4) the validation of the translated data; and 5) the analysis of the large amount of data that transient simulations provide. Several examples are presented to show the implemented solutions. Finally, recommendations based on experience are made to help future developers of interfacing tools.

**Index Terms—**Electromagnetic transients, Electromagnetic Transients Program (EMTP), power flow.

Manuscript received October 11, 2012; accepted November 01, 2012. Date of publication February 07, 2013; date of current version March 21, 2013. Paper no. TPWRD-01092-2012.

Corresponding author: F. de León, Department of Electrical and Computer Engineering, Polytechnic Institute of New York University, Brooklyn, NY 11201 USA (e-mail: fdeleon@poly.edu).

D. Czarkowski is with the Department of Electrical and Computer Engineering, Polytechnic Institute of New York University, Brooklyn, NY 11201 USA (e-mail: dcz@poly.edu).

V. Spitsa is with the Electrical Engineering Department, San Jose State University, San Jose, CA 95192 USA (e-mail: vitaly.spitsa@sjsu.edu).

J. A. Martinez is with the Department of Electrical Engineering, Universitat Politecnica de Catalunya, Barcelona 08028, Spain (e-mail: martinez@ee.upc.edu).

T. Noda is with the Electric Power Engineering Research Laboratory, Yokosuka, Kanagawa 240-0196, Japan (e-mail: takunoda@ieee.org).

R. Iravani is with the Electrical and Computer Engineering Department, Toronto, ON M5S 3G4 Canada (email: iravani@ecf.utoronto.ca).

X. Wang is with the Electrical Engineering Department, Tsinghua University, Beijing 100084, China, (e-mail: xiaoyuw@ualberta.ca).

A. Davoudi is with the Electrical and Computer Engineering Department, University of Texas, Arlington, TX 76011 USA (e-mail: davoudi@uta.edu).

G. W. Chang is with the Electrical Engineering Department, National Chung Cheng University, Chia-Yi 621, Taiwan (e-mail: wchang@ee.ccu.edu.tw).

A. Mehrizi-Sani is with the School of Electrical Engineering and Computer Science, Washington State University, Pullman, WA 99164 USA (e-mail: mehrizi@eecs.wsu.edu).

I. Kocar is with the Electrical and Computer Engineering Department, École Polytechnique de Montréal, Montréal, QC H3T 1J4 Canada (e-mail: i.kocar@polymtl.ca).

Task Force members: S. Abhyankar, U. Annakkage, G. W. Chang, A. Davoudi, F. de León, V. Dinavahi (Task Force Chair), M. O. Faruque, S. Filizadeh, J. Fuller, A. M. Gole, R. Iravani, J. Jatskevich, A. J. Keri, I. Kocar, J. A. Martinez, A. Mehrizi-Sani, A. Monti, L. Naredo, T. Noda, A. Ramirez, M. Rioual, K. Schoder, V. Spitsa, M. Steurer, K. Strunz, X.Wang, and P. Zhang.

Task Force on Interfacing Techniques for Simulation Tools is with the Working Group on Modeling and Analysis of System Transients Using Digital Programs, General Systems Subcommittee, T&D Committee. IEEE Power and Energy Society.

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
Digital Object Identifier 10.1109/TPWRD.2012.2227836

## I. INTRODUCTION

Time domain simulations of large power systems using EMTP-type programs are becoming increasingly common. The need for electromagnetic transients programs is indispensable due to the requirement of a detailed model of control systems and nonlinear network elements. The push comes from the smart grid technologies that require a large number of switching operations for economical or reliability reasons [1]. The pull comes from the continuous increase of computing power that has made possible the simulation of electromagnetic transients of large power systems [2]–[4].

The objective of the translators is to perform automatically the data conversion between two different databases [5]–[8]. In many utilities, the available data are in power-flow program formats (e.g., PSS/E). Therefore, data translators are required to convert the power-flow program files to appropriate formats for EMTP type of programs. Several translators that have been developed in this work are intended to convert input data from power-flow (PF) programs into EMTP-type programs.

An effective technique for building and maintaining time-domain models of large networks in the EMTP-RV was reported in [3] and [4]. This technique is based on an automatic translation of text data into a graphical user interface (GUI) model using scripting (JavaScript). It was shown that the resulting model of the network can serve as a unified framework for different types of power system studies. Frequently, transient analyses are required to supplement other studies for the investigation of electrical networks.

In [6], PSCAD/EMTDC is linked to PSS/E through E-TRAN. E-TRAN is a translator that performs a direct data conversion between phasor-based power flow and stability simulation tools and electromagnetic tools. E-TRAN can initialize the machines and sources in PSCAD simulations based on the translated data from the power-flow analysis in PSS/E [6], [9]–[11].