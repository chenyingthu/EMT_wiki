**Fast and efﬁcient calculation of lightning-induced voltages in frequency-dependent transmission lines over lossy ground**

Sina Mashayekhi a,1 , Behzad Kordi b,∗
a Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC, Canada V6T 1Z4
b Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, Canada R3T 5V6

**Article history:**
Received 24 February 2012
Received in revised form 4 January 2013
Accepted 9 January 2013
Available online 13 February 2013

**Keywords:**
Multiconductor transmission line
Lightning
Macro-model
Overvoltage
Power system simulation

**Abstract**
This paper presents a fast and efﬁcient algorithm for the calculation of electromagnetic ﬁelds radiated from lightning return-stroke channel as well as lightning-induced voltages in frequency-dependent transmission lines. The algorithm developed in this paper employs a mixed time-frequency macro-model that is based on tracing the poles and residues of the transfer function of the lightning-transmission-line system. Accurate and fast calculation of electromagnetic ﬁeld data along the excited transmission line is critical to obtain the source terms (or forcing functions) in ﬁeld-to-transmission-line coupling equations. Using the proposed method, we are able to obtain a closed form solution for the lumped sources required for the analysis of a two-conductor transmission line exposed to nonuniform electromagnetic ﬁelds. The algorithm provides high accuracy as well as signiﬁcant speed gain for multiconductor transmission lines (MTL) as well. To demonstrate the application of the proposed method, we will compare our results with those obtained using other methods or measurements.

## 1. Introduction
Lightning-induced voltages on overhead transmission lines have been the subject of many theoretical and experimental investigations. Incorporation of accurate and efﬁcient calculation of over-voltages induced by indirect lightning strikes in power system networks is important in electromagnetic transient (EMT) type simulators. A fundamental difﬁculty arises in integrating transmission line simulation into an EMT-type simulator. The reason is that network nonlinearities and time-dependant components require a time-domain analysis whereas transmission line characteristics such as conductor loss and dispersion are best described in the frequency domain. The issue of mixed time-frequency domain modeling of lossy coupled multiconductor transmission lines has been studied in both power systems and electronics communities for many years.

There are several models available to analyze transmission lines which can be categorized into terminal-based models and distributed ones. Terminal-based models [1–7], have access only to the information of the transmission line’s terminals. These models are not inherently capable of calculating external-ﬁeld coupling, such as those induced by indirect lightning strikes, whereas one of the inherent features of distributed models, such as those based on the FDTD method [8–16], is the capability of determining the response of the line to external exciting ﬁelds. However, these models are time consuming and need massive memory space which decreases the efﬁciency of the calculations. A distributed-model procedure for the calculation of lightning-induced voltages on transmission lines has been implemented as a computer code known as LIOV (lightning induced over voltage) [17] where an extension of the Agrawal model [8] for the case of lossy ground has been employed. Improvements to this approach [18], incorporation within EMT-type simulators [19], and consideration of the distribution network topology and terminations [20] have been presented in the literature.

For a terminal-based model, the problem of incident plane-wave electromagnetic ﬁeld coupling to MTL has already been addressed in the literature, for example, in [21–29]. However, there are few papers that consider the case of non-uniform electromagnetic ﬁelds such as [30], where a hybrid FDTD and similarity transformation technique are used to calculate the additional voltage sources due to excitation of lossless transmission line.

In this paper, a fast and efﬁcient macro-model is presented for the calculation of induced voltages by external nonuniform electromagnetic ﬁelds in frequency-dependent transmission lines. Radiated electromagnetic ﬁelds from indirect lightning strikes that are signiﬁcant sources of high power electromagnetic radiation in power systems analysis, are studied in this work as the source of nonuniform excitation of the transmission lines.

∗ Corresponding author. Tel.: +1 204 474 7851; fax: +1 204 261 4639.
E-mail addresses: Sina@ece.ubc.ca (S. Mashayekhi), Behzad Kordi@UManitoba.CA (B. Kordi).
1 Tel.: +1 778 320 5555.

## 2. Problem statement
ﬁeld, respectively. The lightning external excitation of the transmission line is represented by distributed voltage and current sources in transmission line circuit model. T