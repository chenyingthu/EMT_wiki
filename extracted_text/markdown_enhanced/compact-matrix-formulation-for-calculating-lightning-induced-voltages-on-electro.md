# Compact Matrix Formulation for Calculating Lightning-Induced Voltages on Electromagnetic Transient Simulators
**Osis E. S. Leal** and **Alberto De Conti**, Member, IEEE

**Abstract**—In this paper, a compact matrix formulation that simplifies the calculation of the lumped sources necessary to estimate lightning-induced effects using transmission line models available in electromagnetic transient programs is proposed. As opposed to an existing solution strategy that requires the sequential calculation of the convolution integrals involving the horizontal component of the incident electric field along multiple segments along the line, the proposed matrix solution allows such convolutions to be performed at once. This not only increases the model efficiency, but also simplifies the assembly of the solution in matrix-oriented simulation tools. The equations are described in both phase and modal domains, with formulations that are compatible with the universal line model and the frequency-dependent transmission line model proposed by Marti. It is shown that both formulations can be accurately used for calculating lightning-induced voltages on overhead lines.

**Index Terms**—Lightning-induced voltages, transmission line models, numerical analysis, electromagnetic transient simulators.

*Manuscript received April 1, 2020; revised June 4, 2020; accepted July 24, 2020. Date of publication August 17, 2020; date of current version July 23, 2021. This work was supported in part by CNPq (National Council for Scientific and Technological Development), grants 431948/2016-0 and 306006/2019-7, FAPEMIG (State of Minas Gerais Research Foundation), grant TEC-PPM-00280-17, and by Pró-Reitoria de Pesquisa (PRPq) of Universidade Federal de Minas Gerais (UFMG), which is the institution responsible for this work. Paper no. TPWRD-00492-2020. (Corresponding author: Alberto De Conti.)*

Osis E. S. Leal is with the Graduate Program of Electrical Engineering (PPGEE), Universidade Federal de Minas Gerais (UFMG), 31270-901 Belo Horizonte, Brazil, and also with the Universidade Tecnológica Federal do Paraná (UTFPR), 84261-550 Pato Branco, Brazil (e-mail: osisleal@utfpr.edu.br).

Alberto De Conti is with the Department of Electrical Engineering, Universidade Federal de Minas Gerais (UFMG), 31270-901 Belo Horizonte, Brazil (e-mail: conti@cpdee.ufmg.br).

Color versions of one or more of the figures in this article are available online at https://ieeexplore.ieee.org.

## I. INTRODUCTION
Electromagnetic transient (EMT)-type programs are usually preferred for the calculation of lightning-induced effects on realistic distribution networks [1]–[12]. The usual procedure consists in writing a separate code to solve telegrapher’s equations considering the effect of external electromagnetic (EM) fields. This code is then interfaced with the EMT simulator in order to update the voltages and currents at the line ends depending on the terminal conditions [1]–[11]. Although accurate, this procedure does not take advantage of the transmission line models already available in EMT-type programs, which may reduce the model efficiency [13].

In [12], a time-domain procedure was proposed to calculate lightning-induced voltages using transmission line models available in EMT-type programs. It consists in adding lumped sources representing the effect of the incident EM fields at both ends of the line. For a multiconductor line with $N_f$ conductors and length $\ell$ parallel to the $x$ axis, the sources are functions of $u_0(t)$ and $u_\ell(t)$ given by [14]
$$
\begin{aligned}
u_0(t) &= u_{x,0}(t) - h e_z(0, t) + a(\ell, t) * h e_z(\ell, t), \\
u_\ell(t) &= u_{x,\ell}(t) - h e_z(\ell, t) + a(\ell, t) * h e_z(0, t),
\end{aligned}
\tag{1}
$$
where
$$
\begin{aligned}
u_{x,0}(t) &= - \int_0^\ell a(x, t) * e_x(x, t) \, dx, \\
u_{x,\ell}(t) &= \int_0^\ell a(x, t) * e_x(\ell - x, t) \, dx.
\end{aligned}
\tag{2}
$$
In these expressions, $e_z(0, t)$ and $e_z(\ell, t)$ are the vertical components of the incident electric fields at the line ends, $e_x(x, t)$ is the horizontal electric field at coordinate $x$ along the line, $h$ is a diagonal matrix containing the conductor heights, and $a(x, t)$ is the time-domain equivalent of the propagation function of a line segment of infinitesimal length. The dimensions of the matrices and vectors in (1) and (2) are, respectively, $N_f \times 1$ and $N_f \times N_f$.

In order to efficiently solve the convolution integrals in (1), it suffices to represent $a(\ell, t)$ as a sum of exponential terms [15]. Dealing with the convolutions in (2) is less straightforward because different propagation functions must be fitted, convolved with the incident electric field and integrated to determine $u_{x,0}(t)$ and $u_{x,\ell}(t)$. One possibility would be performing such calculation in the frequency domain [16]. However, this would require determining the horizontal component of the incident electric field at several points of the line in a large number of frequencies, which would reduce the model efficiency. In [12], a solution is proposed to this problem based on a recursive expression that requires the fitting of the propagation function of a single line segment. However, the proposed solution is expressed in the form of multiple summation terms that, if implemented directly, reduce the efficiency of the algorithm.

This problem is overcome in this paper, whose main contribution is to propose a compact matrix formulation for the calculation of (2). As opposed to the strategy proposed in [12], which requires the sequential calculation of the convolution integrals in (2), the proposed solution allows such convolutions to be performed at once. This significantly simplifies the calculation of