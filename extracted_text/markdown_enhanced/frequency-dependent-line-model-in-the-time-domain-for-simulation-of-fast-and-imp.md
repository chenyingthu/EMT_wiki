# Frequency-dependent line model in the time domain for simulation of fast and impulsive transients

Pablo Torrez Caballero $^a$, Eduardo C. Marques Costa $^{b,\ast}$, Sérgio Kurokawa $^a$

$^a$ Unesp – Univ. Estadual Paulista, Faculdade de Engenharia de Ilha Solteira – FEIS, Departamento de Engenharia Elétrica, Ilha Solteira, SP, Brazil
$^b$ Universidade de São Paulo – USP, Escola Politécnica, Departamento de Engenharia de Energia e Automação Elétricas – PEA, São Paulo, SP, Brazil

$\ast$ Corresponding author. E-mail addresses: educosta@pea.usp.br (E.C. Marques Costa), kurokawa@dee.feis.unesp.br (S. Kurokawa).

## Abstract

A new transmission line model is proposed based on the well-established Bergeron method. The conventional Bergeron model is characterized by the line representation by concentrated longitudinal and transversal parameters, i.e., electrical parameters of the line are represented by means of electric circuit elements. The original approach of this research is the inclusion the frequency effect in the longitudinal parameters of the Bergeron line representation. In order to increase the frequency range covered by the proposed model, the line is represented by a cascade of line segments which are modeled following the proposed frequency-dependent Bergeron circuit. The differential equations resulted from the proposed development are represented by state matrices. The line representation by cascade of frequency-dependent Bergeron circuits enables to extend the application of the new modeling technique for simulations considering a wide range of frequencies, from a switching up to an atmospheric impulse. The proposed line model is validated based on results obtained from the well-established line model using numerical Laplace transform.

## Keywords

Bergeron method; Transmission line modeling – TLM; Electromagnetic transients; Time-domain analysis

## Introduction

There are several transmission line models available in the technical literature to study electromagnetic transients in power transmission systems. Basically, these models may be classified into two general groups: by lumped parameters or by distributed parameters.

In the first group, transmission lines are modeled from the representation by lumped elements, i.e., line is modeled by an equivalent representation by means of electric circuits composed of resistive, inductive and capacitive elements. These models are developed directly in the time domain, which means that can be applied for transient simulations including time-variable and non-linear elements, as: metal-oxide surge arresters, relays, non-linear loads and many other power components. This characteristic is the principal advantage in the transmission line modeling (TLM) by lumped elements [1]. The line representation by lumped parameters is well established in the technical literature for simulation of electromagnetic transients as well as other applications for power flow studies, fault location through long transmission lines and steady state phenomena [2–4].

The line modeling by distributed parameters is developed directly from the frequency-dependent parameters of the line representation by two-port circuit in the frequency domain. From this approach, the line modeling and simulations are carried out in the frequency domain and time-domain results are obtained using numeric transforms [5]. The frequency-dependent parameters of the line are accurately represented using frequency-domain models; however, these models have restrictions for inclusion of time-variable elements in the simulation process, since most power components are well established and modeled in the time domain [6].

Despite line models by lumped elements are developed in the time domain, the frequency effect on the longitudinal parameters can be included in the model using fitting methods. New frequency-dependent models based on the electric circuit approach have been described in the technical literature on TLM. These models are developed directly in the time domain from the line representation by cascade of $\pi$ circuits, where the frequency effect on the electrical parameters is fitted by rational functions $R_{fit}(x)$ and $L_{fit}(x)$ (resistance and inductance) based on the longitudinal impedance of the line $Z(x)$, which is calculated taking into account the earth-return impedance (soil effect) and the skin effect on the cables. For example, the frequency-dependent line model described in Refs. [7,8] shows to be robust and accurate for most of transient conditions on power transmission systems.

However, depending of the transmission system characteristics (source, line and load) and transient conditions, the frequency-dependent model based on cascade of lumped elements shows to be costly in computational terms, depending of the quantity of line equivalent circuits in the cascade, total simulation time and integration step. Furthermore, hard unbalanced conditions could lead