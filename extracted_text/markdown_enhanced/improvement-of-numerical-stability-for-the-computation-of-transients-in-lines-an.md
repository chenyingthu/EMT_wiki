## Improvement of Numerical Stability for the Computation of Transients in Lines and Cables
Ilhan Kocar, Student Member, IEEE, Jean Mahseredjian, Senior Member, IEEE, and Guy Olivier, Senior Member, IEEE

**Abstract**—This paper discusses numerical stability problems of a frequency-dependent transmission-line and cable modeling approach used for electromagnetic transient analysis. Time-domain numerical errors due to the discrete computation of convolution integrals can be estimated in terms of transfer function parameters for a given line or cable model. Based on this estimation, a methodology for the improvement of numerical stability is presented. The numerical advantages of the new method are supported by demonstrations and comparisons with existing models. The method presented in this paper is applicable to power cables and transmission lines.

**Index Terms**—Electromagnetic transients, Electromagnetic Transients Program (EMTP), fitting, wideband line and cable model.

*Manuscript received November 06, 2008; revised February 20, 2009, May 24, 2009. First published February 02, 2010; current version published March 24, 2010. Paper no. TPWRD-00833-2008.*
*The authors are with École Polytechnique de Montréal, Montréal H3T 1J4 QC, Canada (e-mail: jeanm@polymtl.ca).*
*Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.*
*Digital Object Identifier 10.1109/TPWRD.2009.2037633*

## I. INTRODUCTION

In the simulation of electromagnetic transients with the method of characteristics (MoC), transmission lines and cables can be characterized by two matrix functions in the frequency domain: for the propagation function and for characteristic admittance. Although many works are related to the meticulous fitting and modeling of transmission line and cable functions in the frequency domain, numerical stability problems of existing models in the time domain remain complex and require further research.

Existing frequency-dependent line and cable models in the Electromagnetic Transients Program (EMTP) approximate transmission system functions with rational transfer functions over a range of frequencies in order to properly assess electromagnetic transients [1]–[3]. Rational function approximations are preferred as they allow an efficient computation of convolution integrals in the time domain with a recursive scheme [4]. Convolution integrals are, in general, computed via numerical integration techniques in the time domain in accordance with the discrete timestep of the EMTP simulation.

The numerical computation of convolution integrals, including terms, is associated with two error conditions. The first error is due to the conversion of the integral to difference equations (truncation error) and the second is due to the interpolation on input as a result of modal time delays of . These delays are not, in general, integer multiples of the simulation step in EMTP. In the modeling approach presented in [3] for the universal line model (ULM), every modal time delay is present in each element of ; therefore, the interpolation error may have an important effect.

In this paper, and are identified by using partial fraction expansions (PFE) in the frequency domain, in conformity with [3]. Then, the convolution integrals expressed with state-space equations are used to estimate local numerical errors in terms of PFE variables. Based on this relation between errors and PFE variables, constraints are determined for residue/pole ratios so that time-domain errors are confined within a safe boundary. In the proposed approach, the identification in phase domain becomes a constrained linear least-squares problem.

## II. BACKGROUND

### A. General Description of the Transient-Line Equations

The voltage and current relations of an arbitrary transmission line or cable (transmission device) connected between arbitrary ends and can be written in the frequency domain as (see [5])
$$ (1) $$
where and represent current and voltage column vectors of dimension standing for the number of conductors. Matrices and vectors are denoted with bold characters. The by matrices for propagation and characteristic admittance are given by
$$ (2) $$
$$ (3) $$
where is the length of the transmission device, is the shunt admittance matrix per-unit length, and is the series impedance matrix per-unit length. Both matrices are numerically available from the geometry and electrical parameters of the line or cable [6], [7].

The time-domain solution of (1) is obtained by applying convolution
$$ (4) $$
where
$$ (5) $$
A widely accepted approach in EMTP-type computations is to use rational transfer function approximations for and in order to solve (4). The convolution integrals of (4) are computed at each discrete solution timepoint.

### B. Adopted Frequency-Domain Model

This paper is based on the ULM formulation [3]. For a multiphase transmission system, contains different