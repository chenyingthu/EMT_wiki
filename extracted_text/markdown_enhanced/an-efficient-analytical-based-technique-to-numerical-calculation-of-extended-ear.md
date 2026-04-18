## An efficient analytical based technique to numerical calculation of extended earth return impedance and admittance of overhead lines

Z. Liu $^a$, H.M.J. De Silva $^{a,*}$
$^a$ Manitoba Hydro International, MB, Canada R3Y0C5

* Corresponding author.
E-mail addresses: jliu@mhi.ca (Z. Liu), jeewantha@mhi.ca (H.M.J. De Silva).

**Keywords:** Electromagnetic transient modelling, Earth return impedance and admittance, Numerical integration, Overhead lines

**Abstract:** This paper describes an efficient numerical integration technique for the extended overhead line earth return impedance and admittance formula. In-appropriate handling of the infinite integral in the formula can lead to erroneous calculated earth-return parameters at extreme frequencies, and a significant increase in computational effort. In this paper, an efficient technique based on an analytical approach is introduced to enforce proper discretization of the extended transmission line equations. Firstly, the line equations are analyzed, and a common cause of improper discretization is identified. Then the equations are further broken down numerically, based on which a procedure to suitably select a discretization interval and step is developed. Validation was conducted by calculating the earth return parameters of overhead-line cases using the proposed method and equal distance discretization. The proposed technique shows accurate results while using fewer discretization points than equal distance discretization.

## 1. Introduction

Electromagnetic transient study of power system requires transmission line’s earth return parameters to be accurately evaluated in a wide range of frequencies [1-4]. The frequency of interest can vary from 0 Hz for DC operation [5], to serval MHz for lightning transient, and Gas insulated substation studies [6-7].

Carson/Pollaczek’s earth-return impedance and space admittance (classical transmission line (TL) approach) are widely used in EMT programs [8,9]. The recent extended TL approach with accurate earth-return impedance and admittance [10,11] improves the accuracy for a wide frequency range and more importantly enhances the stability of the time domain simulation [7].

Numerous amounts of previous studies on proper implementation of the classic TL formula has been conducted, but not for the extended TL formula. Although they are technically different, it is still possible to develop similar implementation methods by correlating with pervious works. This is due to the similarity of complexity in the formula themselves (i.e. integrand components). Previous studies have developed serval different approaches to the classic TL formulas. These includes generalized discretization variable [12], solving the infinite integral via series expansion [1], Taku Noda’s integral transformation techniques [13], asymmetric extraction method [2], or custom partitioning of integrand and applying various suitable integration method to each partitions [14]. However, most of the time the evaluation of integration variables such as truncation length, and discretization step size is not straightforward. This leads to the use of recursive algorithms which enforces convergence by recalculating using different integration parameters repeatedly. To avoid recursive methods, past researchers have developed analytical based approach for Pollaczek’s underground cable earth impedance [15], however, no similar methods has yet been conducted for the extended TL formula for overhead line.

This paper proposes a systematic procedure derived analytically to compute the earth return parameters extended TL formulas accurately, numerically efficiently, and without recursive steps.

## 2. Review of Overhead Line equations

### 2.1. The approximate overhead line earth return formula

In this paper, $Z, Y, R, L, G, C, f, \omega$ represents per unit length impedance, admittance, resistance, inductance, conductance, capacitance, frequency, angular frequency respectively.

Fig. 1 shows a typical two conductors overhead transmission line system. Where, $\sigma_e, \mu_e, \epsilon_e, y, h$ represent earth resistivity, permeability, permittivity, line separation, and height above ground respectively.

Fig. 1. Transmission line configuration with overhead lines and cables.

$$F_1(s) = \frac{e^{-(h_i + h_j)s} \cos(ys)}{\sqrt{s^2 + \omega^2 \mu_0 \epsilon_0 (1 - \mu_r \epsilon_r) + j\omega\mu_e \sigma_e}} \tag{11}$$

$$M + jN = 2 \int_{0}^{\infty} F_2(s) \, ds \tag{12}$$

$$F_2(s) = \frac{e^{-(h_i + h_j)s} \cos(ys)}{\sqrt{s^2 + \omega^2 \mu_0 \epsilon_0 (1 - \mu_r \epsilon_r) + j\omega\mu_e \sigma_e + j\omega\epsilon_0 (\sigma_e + j\omega\epsilon_e)s}} \tag{13}$$

Where, $\mu_0$ is the vacuum permeability, $\mu_r$ is the relative permeability, $\epsilon_0$ is the vacuum permittivity, $\epsilon_r$ is the relative permittivity.

The earth return admittance can be calcu