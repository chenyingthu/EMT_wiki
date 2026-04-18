# New multiphase mode domain transmission line model

**M.C. Tavares** a,*, **J. Pissolato** b,1, **C.M. Portela** c,2  
a São Carlos Engineering School, São Paulo University, Av. Dr. Carlos Botelho 1465, P.O. Box 359, São Carlos, São Paulo 13560-250, Brazil  
b Faculdade de Engenharia Elétrica e de Computação, UNICAMP, State University of Campinas, C.P. 6101, Campinas 13081-970, Brazil  
c COPPE, Federal University of Rio de Janeiro, Rua Eng. Cesar Grillo, Rio de Janeiro 22640-150, Brazil  

Received 26 February 1998; received in revised form 9 April 1999; accepted 20 April 1999

* Corresponding author. Tel.: +55-16-2739365; fax: 55-16-2739372. E-mail addresses: cristina@sel.eesc.sc.usp.br (M.C. Tavares), pisso@dt.fee.unicamp.br (J. Pissolato), portelac@coep.ufrj.br (C.M. Portela)  
1 Tel.: +55-19-7883861; fax: +55-19-7883860  
2 Tel.: +55-21-2605010; fax: +55-21-4934201

## Abstract
This article presents a new model to represent transmission lines including the frequency dependence of longitudinal parameters. The model uses exact modes, for ideally transposed lines, and “quasi-modes” for non-transposed lines. The line is represented through a cascade of p-circuits, with one p-circuit for each mode. The transformation matrix used is real and it is modeled with ideal transformers. The model is described for three-phase lines, dc lines, double three-phase lines and six-phase lines. An ATP-EMTP implementation of a 440 kV three-phase transmission line is performed to illustrate the model and a comparison with two frequency dependent ATP line models are made, the Semlyen and JMarti ones. © 1999 Elsevier Science Ltd. All rights reserved.

**Keywords:** Transmission line model; Frequency dependence; Mode domain; Electromagnetic transients

## 1. Introduction
One of the main difficulties when dealing with transient simulation studies in a digital simulator program like ATP [1] is the correct representation of transmission lines. The ATP works in the time domain and the line is generally represented by its phase quantities. Nevertheless, the transmission line parameters, namely the longitudinal parameters, vary with distance and frequency.

The former is represented through the hyperbolic function in the distributed parameter model or through p-circuits. With the last, the line is represented by cascading the p-circuit, and some care should be taken with the p-length. The number of cascaded elements can become very large if the line is too long.

To model the frequency dependence, it is more complex. First, the impedance matrix varies with frequency, which means that there is one full matrix for each frequency. The impedance matrix is a full one due to the phase (and ground wire) coupling. As a program like ATP works in time domain the frequency dependence of an element is not a straightforward model.

It is proposed then to work not with phase but with modes and therefore deal with diagonal rather than full matrix. In mode domain there is no coupling and the frequency dependence of the impedance can be properly represented with synthetic circuits. Nevertheless, there is the transformation matrix, which makes the link between phase and mode domain, which also varies with frequency.

In the present model a real transformation matrix is used as the unique transformation matrix for the entire frequency range. As the matrix elements are real ones they can be represented in a time domain program like ATP using ideal transformers. This is implemented making the proper connections with the transformers, using their ratios and polarities.

This model can be implemented in any digital program that has ideal transformer components or in an analog simulator (TNA). This means that with any digital program it is possible to have a good representation of a multiphase transmission line, even if the program only has a single-phase transmission line model or resistor, inductors and capacitors (used to make the p-sections of each mode), but has ideal transformer elements.

The theory is described for a three-phase line, dc, double three-phase and six-phase line. A 440 kV three-phase transmission line illustrates the model and a comparison with two frequency dependent ATP-EMTP line models is made, the Semlyen [2] method and the JMarti [3] model, both incorporated in ATP-EMTP. The line is supposed both transposed and non-transposed. First the modes are analyzed, permitivity frequency dependence, non uniform soil, e.g. with layers of different electric parameters.

## 3. Mode domain
Once the electrical parameters (longitudinal and transversal impedance) have been properly calculated in phase domain, the line can be represented to start the desired simulations. It is proposed then to work with mode components.

The transformation matrix is unique for each impedance matrix, which means that for a defined line there is one impedance matrix for each frequency. This seems to make the mode determination very complex. It is usual to make some simplifications as in both Semlyen and JMarti ATP

*Fig. 1. Schematic representation of a single three-phase line.*