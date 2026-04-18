# Analysing a power transformer’s internal response to system transients using a hybrid modelling methodology

Steven D. Mitchell $^{a,\ast}$, Gustavo H.C. Oliveira $^{b}$

$^{a}$ School of Electrical Engineering and Computer Science, University of Newcastle, Callaghan, NSW 2308, Australia  
$^{b}$ Electrical Engineering Department, Federal University of Parana, Curitiba, PR 81531-990, Brazil  

$\ast$ Corresponding author.  
E-mail addresses: steve.mitchell@newcastle.edu.au (S.D. Mitchell), gustavo@eletrica.ufpr.br (G.H.C. Oliveira).

## Abstract

This article presents a novel approach to analysing a power transformer’s internal response to system transients. In this approach a hybrid modelling methodology is adopted which leverages the distinct advantages offered by both Black and Grey Box modelling techniques. The Black Box model of the transformer is used within the EMTP system study environment in order to take advantage of its mathematical flexibility and modelling accuracy. Transients derived from network switching operations within the study can then be used for injection tests within the Grey Box modelling environment. The Grey Box model, which is based upon the physical structure of the transformer, will facilitate analysis of the transformer’s internal voltage response to the external stimulus. A fundamental difference between the approach described in this paper and more traditional approaches is that it does not require prior knowledge of the internal geometry of the transformer. All of the modelling parameters are derived from external tests, nameplate details and an intrinsic understanding of common transformer design principles. This can be a distinct advantage since in most cases a transformer’s design specifications are not readily available outside of the laboratory due to the manufacturer’s intellectual property restrictions. A study of a gas insulated substation within a hydroelectric power plant in Brazil is used to demonstrate the proposed technique.

**Keywords:** Power transformer, Black Box, Grey Box, Model, Resonant overvoltage, EMTP

**Article history:**  
Received 16 September 2013  
Received in revised form 16 December 2014  
Accepted 24 December 2014

## Introduction

Electrical power system switching operations can generate a broad spectrum of transient frequencies [1]. The transient amplitude may not be sufficiently high to initiate a reaction by surge protection, however the frequency content of the transient may be such that there is a match with the natural frequency modes of equipment connected to the electrical network. A case in point is power transformers [2]. When a switching transient frequency component aligns with an internal resonance frequency within a power transformer, voltage amplification can occur which can result in a breakdown of the transformer’s insulation system. This is an area of study with a long history [3], however the area is now receiving increased attention due to an increasing number of transformer failures which have been attributed to internal resonance overvoltage conditions [4,5]. Working groups from both IEEE [6] and CIGRE [7] have been established to investigate ways of mitigating the problem.

Power transformers each have their own characteristic frequency response [8]. To predict how a power transformer will behave under different transient conditions, a modelling approach may be adopted. In fact, mathematical modelling of dynamic systems can generally be divided into two basic approaches, in terms of procedures for selecting the model structure and calculating the model parameters [9–11]: White-Box (or physical) modelling and Black-Box modelling. A methodology that is a compromise between these two approaches is the Grey-Box model. This terminology is associated with methods and models that can be put on a scale ranging from a pure White-Box physical model to a pure Black-Box parameterized model [9–11]. Therefore, this will be the nomenclature for transformer models used here.

A White Box model uses intimate knowledge of the internal geometry and material properties of the transformer to build a lumped parameter electrical network representation of the transformer [12–14]. Another common approach is to build a distributed electrical model which views the windings as multi-conductor transmission lines (MTL) [15]. Simple White Box models can be incorporated into an electrical system model within an Electromagnetic Transients Program (EMTP). However their application within EMTP becomes difficult when implementing a more comprehensive model which will be accurate across a broader frequency spectrum. Such a model will need to take into account various non-linear frequency dependent parameter properties such as the complex permittivity of the transformer’s insulation system, magnetic skin effects associated with the transformer core, and the skin and proximity effects within the transformer’s windings.

The procedure for transient analysis is described in Section ‘Black Box modelling for electrical system transient analysis’. The Grey Box modelling procedure and the estimation of an internal winding transient response is presented in Section ‘Grey Box modelling to estimate the internal transient response’.