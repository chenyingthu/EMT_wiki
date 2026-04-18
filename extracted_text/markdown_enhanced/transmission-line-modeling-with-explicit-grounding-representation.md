# Transmission Line Modeling with Explicit Grounding Representation

**G. J. COKKINIDES**  
Electrical Engineering Department, University of South Carolina, Columbia, SC (U.S.A.)  

**A. P. SAKIS MELIOPOULOS**  
School of Electrical Engineering, Georgia Institute of Technology, Atlanta, GA 30332-0250 (U.S.A.)  

*(Received September 8, 1987)*

## Summary
This paper presents a new model of an overhead transmission line for electromagnetic transient computations. The unique feature of the model is the explicit representation of the tower grounding configuration and terminal substation grounds. Other properties of the model are: (1) accurate frequency dependent parameter representation from DC to several MHz; (2) explicit modeling of line asymmetries; and (3) high numerical efficiency.

The model implementation is based on the solution of the transmission line differential equations resulting in a set of step response functions, forming a matrix. The step response matrix is utilized in a time domain simulation of electric power networks by a linear convolution scheme. The transmission line model is validated with actual system test data. The model is useful for computing the ground potential rise of transmission towers due to lightning or switching surges, insulation stress, etc. Typical applications are described in the paper.

## 1. Introduction
Electromagnetic transients in power transmission systems, resulting from switching or lightning, play an important role in the overall cost and reliability of the power system. For this reason power line performance has been studied extensively, both analytically and experimentally. The present design of transmission lines is based on a wealth of data. For analysis purposes, many transmission line models have been developed over the years [1-5]. Many of these models have been incorporated into the EMTP program [6] which is an excellent analytical tool for studies of electromagnetic transients. At present, the EMTP contains several transmission line models (weight function model, Ametani setup, Semlyen setup, Marti model, etc.) which can incorporate the frequency dependence of the transmission line parameters. However, none of these models can represent the grounding system associated with a transmission line (tower grounding and substation grounding). Explicit representation of grounding structures is necessary to predict the transient ground potential rise at the tower and substation grounds during switching or lightning surges.

This paper describes a unified transmission line model with the following unique features: (a) explicit representation of transmission line grounding systems and (b) explicit modeling of line asymmetries. In addition, the model accurately represents the frequency dependence of line parameters and is numerically efficient.

## 2. Model Description
An overhead transmission line is viewed as a multiport linear network. The network terminals are the line conductors at the two ends of the line. Such a system is described with a set of step response functions which form a matrix and which shall be called the line step response matrix (LSRM). In general, the line step response is computed as the inverse Fourier transform of its frequency response. The frequency response is derived from the line admittance matrix, defined by

$$ I(\omega) = Y(\omega) V(\omega) \quad (1) $$

where $V(\omega)$ and $I(\omega)$ are vectors containing the voltage and current phasors at the terminals of the line and $\omega$ is the angular frequency.

```
                               a       j
    J                                                                               J
    J                                                                                j           -------___
    J                          c           j                                             J
```

solution of the transmission line partial differential equations

$$ \frac{\partial^2 i(t, y)}{\partial y^2} = C L \frac{\partial^2 i(t, y)}{\partial t^2} + C R \frac{\partial i(t, y)}{\partial t} \quad (2a) $$
$$ \frac{\partial v(t, y)}{\partial y} = R i(t, y) + L \frac{\partial i(t, y)}{\partial t} \quad (2b) $$

where $v$ and $i$ are vectors of voltages and currents, respectively, which are functions of time $t$ and one space coordinate $y$ along the line. $R$, $L$ and $C$ are the resistance, inductance and capacitance matrices in $\Omega \text{ m}^{-1}$, $\text{H m}^{-1}$ and $\text{F m}^{-1}$, respectively.

Equation (2) is formulated so that the earth current path is implicitly represented. Thus, for the four-wire line of Fig. 1 these matrices are $4 \times 4$. The resistance and inductance matrices ($R$ and $L$) exhibit a strong