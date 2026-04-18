## RATIONAL APPROXIMATION OF FREQUENCY DOMAIN RESPONSES BY VECTOR FITTING

**Bjørn Gustavsen (M)**  
EFI, Trondheim, Norway  
Email: bjorn.gustavsen@efi.sintef.no

**Adam Semlyen (LF)**  
University of Toronto, Toronto, Canada  
Email: semlyen@ecf.toronto.edu

**Abstract** The paper describes a general methodology for the fitting of measured or calculated frequency domain responses with rational function approximations. This is achieved by replacing a set of starting poles with an improved set of poles via a scaling procedure. A previous paper [5] has described the application of the method to smooth functions using real starting poles. This paper extends the method to functions with a high number of resonance peaks by allowing complex starting poles. Fundamental properties of the method are discussed and details of its practical implementation are described. The method is demonstrated to be very suitable for fitting network equivalents and transformer responses. The computer code is in the public domain, available from the first author.

## 1 INTRODUCTION

One of the problems encountered in power system transients modeling is the accurate inclusion of frequency dependent effects in a time domain simulation. Such effects arise from eddy currents in conducting materials and sometimes from relaxation phenomena in dielectrics. These effects materialize as a frequency domain variation in the resistance, inductance and capacitance matrices used in the formulation of the model. In practice, the frequency dependent responses are obtained via calculations or measurements as discrete functions of frequency.

A linear model of a power system component can in general be included in a time domain simulation via convolutions between terminal quantities (e.g. node voltages) and impulse responses characterizing the dynamics of the model. A full numerical convolution is always possible, but this becomes computationally inefficient because of the many time steps in a simulation. A much more efficient implementation is achieved if the frequency domain responses are replaced with low order rational function approximations, as the convolutions can then be given a recursive formulation [1]. The ability of finding a good rational function approximation is therefore important in power system modeling.

In principle, an approximation of a given order can be found by fitting a ratio of two polynomials to the data [2]:
$$f(s) = \frac{a_0 + a_1 s + a_2 s^2 + \dots + a_N s^N}{b_0 + b_1 s + b_2 s^2 + \dots + b_N s^N} \tag{1}$$
Equation (1) is nonlinear in terms of the unknown coefficients but can be rewritten as a linear problem of the type $A x = b$ by multiplying both sides with the denominator. However, the resulting problem is badly scaled and conditioned as the columns in $A$ are multiplied with different powers of $s$. This limits the method to approximations of very low order, particularly if the fitting is over a wide frequency range.

The difficulty in formulating a general fitting methodology has resulted in many methods which are tailored for particular problems. For instance, Bode type fitting restricted to real poles and zeros has been successfully applied to transmission line modeling based on modal characteristics [3]. Transformer models and network equivalents need complex poles to represent resonance peaks. Such responses have been approximated by fitting partial fractions to the data in an optimization procedure, with precalculated poles [4].

An attempt at formulating a general fitting methodology was introduced in [5]. This method—vector fitting—was based on doing the approximation in two stages, both with known poles. The first stage was carried out with real poles distributed over the frequency range of interest. In addition, an unknown frequency dependent scaling parameter was introduced which permitted the scaled function to be accurately fitted with the prescribed poles. From the fitted function a new set of poles were obtained and then used in the second stage in the fitting of the unscaled function. This procedure was very successful in fitting the smooth functions occurring in transmission line modeling [5-6]. However, later investigations by the authors have shown that the method fails when there are many resonance peaks in the response to be fitted.

This paper shows that the above mentioned limitations can easily be overcome by using complex starting poles. This result is demonstrated by numerical examples involving artificially created frequency responses, a measured transformer response, and a network equivalent. The paper also provides details on the practical implementation of vector fitting.

## 2 VECTOR FITTING BY POLE RELOCATION

Consider the rational function approximation
$$f(s) = \sum_{n=1}^{N} \frac{c_n}{s - a_n} + d + s h \tag{2}$$
The residues $c_n$ and poles $a_n$ are either real quantities or come in complex conjugate pairs, while $d$ and $h$ are real. The problem at hand is to estimate all coefficients in (2) so that a least squares approximation of $f(s)$ is obtained over a given frequency interval. We note that (2) is a nonlinear problem in terms of the unknowns, because the unknowns $a_n$ appear in the denominator.

Vector fitting solves the problem (2) sequentially as a linear problem in two stages, both times with known poles.

### Stage #1: Pole identification
Specify a set of starting poles $\bar{a}_n$ in (2), and multiply $f(s)$ with an unknown function $\sigma(s)$. In addition we introduce a rational approximation for $\sigma(s)$. This gives the augmented problem:

Note that in (3) the rational approximation for $\sigma(s)$ has the same poles as the approximation for $\sigma(s)f(s)$. Also, note that the ambiguity in the solution for $\sigma(s)$ has been removed by fo