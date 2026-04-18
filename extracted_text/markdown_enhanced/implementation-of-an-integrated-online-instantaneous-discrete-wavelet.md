# Implementation of an integrated online instantaneous discrete wavelet transform decomposition toolbox in ATP-EMTP

Nima Mahmoudpour a,c, Farhad Haghjoo b,c, Seyed Mohammad Shahrtash c,⇑
a Azarbaijan Regional Electricity Company, Tabriz, Iran
b Shahid Beheshti University, Tehran, Iran
c Center of Excellence for Power System Automation and Operation, Electrical Engineering Department, Iran University of Science and Technology, Tehran, Iran

⇑ Corresponding author. Tel.: +98 21 73225613; fax: +98 21 73021613. E-mail address: shahrtash@iust.ac.ir (S.M. Shahrtash).

**Article history:** Received 7 January 2014; Received in revised form 26 November 2014; Accepted 24 December 2014; Available online 17 January 2015
**Keywords:** ATP-EMTP software, Discrete wavelet transform, Online decomposition, Power system transients simulation

**Abstract**
Although wavelet transform decomposition has wide applications in the analysis of power system transients due to its multi-resolution analyzing nature, conventional transient simulation programs do not provide an effective inbuilt wavelet transform toolbox for online studies. This paper proposes the development and implementation of an Online Instantaneous Discrete Wavelet Transform Decomposition Toolbox (IWTD toolbox) in ATP-EMTP software by its MODELS programming language. Integration of a powerful online discrete wavelet transform toolbox with alternative transient program makes this software highly functional especially with selectable different full and reduced order mother wavelets with deﬁnable reduction degree. The proposed toolbox provides a user-friendly interface with additional capabilities and features for ATP users. Numerous cases simulated and compared with the results of the well-known MATLAB Wavelet Toolbox have indicated that the proposed toolbox works reliably and accurately in the ATP-EMTP environment.

## Introduction

Discrete Wavelet Transform (DWT) is well suited to non-stationary signals whose frequency spectrum is time-variant and may contain both high-frequency components and localized impulses superimposed on power frequency and its harmonics as is typical of fast power system transient signals. The ability of the wavelets to focus on short time intervals for high-frequency components and long time intervals for low-frequency components provides non-uniform division of frequency domain and improves the analysis of wide band electromagnetic transient signals [1]. Due to the wide variety of signals and problems encountered in power engineering, there are different applications of wavelet transform in power system analysis. These include power system protection and relaying [2–13], analysis of power quality disturbances [14–19], high voltage insulation condition monitoring [20–30], power measurement [31–32], and analysis of power system transients [33–35].

Nowadays, among all known software packages for studying power system transients, ATP-EMTP is considered to be one of the most widely used universal programs for simulation of transient phenomena of electromagnetic as well as electromechanical nature in electric power systems. With this digital program, complex networks and control systems of arbitrary structure can be simulated. ATP-EMTP has also extensive modeling and additional important features besides the computation of transients.

Obviously, an integrated toolbox that can be used to perform wavelet transformation of the ATP simulated waveforms is a highly useful feature for those studies investigating wavelet transformation based techniques. Although several wavelet transform programs such as MATLAB Wavelet Toolbox are available, their usage generally requires that simulated waveforms to be saved in data ﬁles and then perform the analysis external to the simulation environment (i.e. ATP-EMTP). This kind of applying DWT and also what has been proposed in [36] should be categorized in offline approaches, as application of DWT is allowed when the whole signal is captured.

It was believed that there are some limitations in employing wavelet transformation in online applications, which had lead to using it only in ofﬂine mode; including:
a. Generating any of the upper level wavelet transform components should be performed through a successive step-by-step calculation from the ﬁrst level up to the desired level. Therefore, there is a time consuming calculation process for each new sample of the original signal when it is calculated.
b. Down-sampling, which is employed by DWT in the decomposition process to avoid increase in computational burden (although it makes the reconstruction process as compulsory, whenever the original signal is required).

Nonetheless, if an online application of DWT is going to be introduced, to the authors’ knowledge, the requirements for an online version of WT can be summarized as follows:
1. The ﬁlters’ structures should be ba

toolbox considering different cases studies. Comparison between the performance of the proposed toolbox (as an online approach) and MATLAB Wavelet Toolbox (as an ofﬂine approach) are also made in this section. Conclusions and future work are included in Section ‘Conclusion’. Appendix A presents the basic equations and programming procedure of the toolbox in brief.

## Theoretical bases of the instantaneous discrete wavelet transform decomposition