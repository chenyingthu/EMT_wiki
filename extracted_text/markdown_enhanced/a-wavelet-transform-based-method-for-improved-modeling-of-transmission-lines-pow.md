## A Wavelet Transform-Based Method for Improved Modeling of Transmission Lines
Ali Abur, Fellow, IEEE, Omer Ozgun, and F. H. Magnago

**Abstract**—This paper is concerned about the accurate representation of transmission lines for electromagnetic transients simulation studies. The frequency dependent (FD) line model (also known as the J. Marti model) which is currently used in most electromagnetic transient programs [1], has been a major contribution to the power system transient simulations. However, despite its accuracy and computational efficiency for most simulation cases, it still requires improvement due to the approximation it makes in choosing the modal transformation matrix $T_v$. This matrix is, in general, frequency dependent and used in transforming variables between the phase and modal domains at each simulation time step. Currently, it is approximated as a constant matrix which may not hold true for certain tower configurations and/or conductor types where line parameters vary drastically with frequency. In this paper, a wavelet-based alternative solution, which incorporates frequency dependence of transformation matrices into the simulation process, is proposed. Simulation results, illustrating the effects of using the proposed model versus the existing FD line model, are also presented.

**Index Terms**—Electromagnetic transients simulations, frequency dependent transmission line parameters, modal transformations, wavelet transform.

*Manuscript received February 7, 2003. This work was supported by NSF Grant ESC-9821090.*
*A. Abur is with the Texas A&M University, College Station, TX 77843 USA (e-mail: abur@ee.tamu.edu).*
*O. Ozgun is with Applied Materials, Inc., Santa Clara, CA 94086 USA (e-mail: omer_ozgun@amat.com).*
*F. H. Magnago is with the Universidad Nacional de Río Cuarto, 5800, Argentina (e-mail: fhmagnago@arnet.com.ar).*
*Digital Object Identifier 10.1109/TPWRS.2003.814846*

## I. INTRODUCTION
SIMULATION of transients along transmission lines can be best performed in the frequency domain, since the line parameters are known to vary significantly as a function of frequency. However, most of the power systems include components with time varying and/or nonlinear operating characteristics such as solid state rectifiers, saturated transformers, surge arresters, metal-oxide varistors, etc. whose models are best realized in the time domain.

Therefore, simulations are preferably carried out in the time domain when studying events involving the overall system with switching operations and nonlinear devices.

Reconciling the simulation and modeling requirements of this mixed set of components has been one of the challenges faced in the analysis of transients so far. This paper addresses this challenge by presenting an alternative simulation method, which is motivated by the unique properties of the wavelet transform.

Direct application of the wavelet transform is one way to accomplish the modeling of lossy transmission lines with frequency dependent parameters. One approach is to start with the general form of the multiconductor transmission line partial differential equations, for the voltages and currents along the line, expressed in terms of the spatial distance and time. Then, use the wavelet transform to convert them into large sparse algebraic equations whose solutions will yield coefficients of the wavelet transform of the voltages and currents of interest. However, integration of such a computational procedure into an existing transients simulator may not be trivial. Instead, a fairly simple modification of the well known, constant but distributed parameter line model, or the so called the Bergeron’s model [2], is proposed by the authors in [3] and [4]. This model makes use of the discrete wavelet transform to account for the frequency dependence of the line parameters. In [3], the method is developed for single-phase lines only. On the other hand, simulation of transients along multiphase transmission lines has the additional drawback, that the line equations ought to be decoupled into independent modal equations, so that each one can be solved easily in the respective modal domain. This decoupling is done through a linear transformation matrix, which will in general be a function of frequency due to the frequency dependent line parameters. In time domain simulations, a constant transformation matrix, which is typically evaluated at a chosen frequency, is used as an approximation. So, even when using the advanced frequency dependent (FD-model) model of [5], modal transformation matrix will have to be approximated. The simulation method, which is presented in this paper, provides a rather simple avenue to improve this approximation by using the wavelet transform.

The paper is organized such that a review of the discrete-time wavelet transform (DWT) implementation along with the FD-model and the Bergeron’s constant parameter (CP-model) distributed line model are presented first. The proposed wavelet-based method for the simulation and modeling of transmission lines with frequency dependent parameters are discussed next. Simulation results of some power system transients are then shown, followed by their discussion and conclusions.

## II. IMPLEMENTATION OF THE DISCRETE-TIME WAVELET TRANSFORM (DWT)
Even though the main ideas that lead to the development of the Wavelet transform (WT) have been known for some time, it has been introduced in mathematics relatively recently. Similar to the case of Fourier analysis, wavelet analysis is based on expansions in terms of a set of basis functions. These functions are generated in the form of translations and dilations of a particular function referred to as the mother wavelet, which satisfies certain necessary conditions [7], [8].

**Fig. 1.** Implementation of the DWT.

**Fig. 2.** CP-model of a lossless transmission line.

Continuous WT of a function is defined by the inner product between and a family of wavelets. For a given scalar matrix for the