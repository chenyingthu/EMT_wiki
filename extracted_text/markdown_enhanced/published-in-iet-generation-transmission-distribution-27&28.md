# New model for overhead lossy multiconductor transmission lines
Juan C. Escamilla$^1$, Pablo Moreno$^2$, Pablo Gómez$^3$
$^1$ CENALTE de la Comisión Federal de Electricidad (CFE), Calle Violetas No. 7, Reserva Territorial Atlixcáyotl, C.P. 72197, San Andrés Cholula, Puebla, Mexico
$^2$ CINVESTAV del IPN, Unidad Guadalajara, Av. del Bosque 1145, Col. El Bajío, C.P. 45019, Zapopan, Jal., Mexico
$^3$ Electrical Engineering Department of SEPI-ESIME Zacatenco, Instituto Politécnico Nacional (IPN), U.P. ‘Adolfo López Mateos’, Edificio Z-4 Primer piso, C.P. 07738, México, D.F., Mexico
E-mail: pgomezz@ipn.mx

**Abstract:** A new model for time-domain electromagnetic transient analysis of overhead multiconductor transmission lines with frequency-dependent electrical parameters is presented. The model is based on the method of characteristics, which has been used before by means of the application of finite difference schemes. Conversely to the regular method of characteristics, the model presented here does not require the spatial discretisation along the line. Also, the frequency dependence of the electrical parameters is included by means of a transient resistance matrix. To validate the model, the results are compared to those from a frequency-domain method, the alternative transients program/electromagnetic transients program (ATP/EMTP) and the electromagnetic transients program-restructured version (EMTP-RV).

## 1 Introduction
Electromagnetic transient analysis of power systems usually requires line models capable of reproducing frequency-dependent effects. Although frequency-domain models are very accurate, they present difficulties when dealing with non-linearities and are impractical for interfacing with time-domain simulation programs like EMTP. On the contrary, time-domain methods possess great versatility simulating topology changes of electrical networks and non-linear elements; however, modelling the elements with frequency-dependent parameters introduces convolution procedures.

In 1982, Martí [1] developed his line model which is still in use in the EMTP. In this model, the frequency dependence of the propagation function and the characteristic impedance of the line were taken into account, but the transformation matrix was considered as real and constant.

In 1998, Gustavsen and Semlyen [2] proposed a method in the phase domain. In this work, the characteristic impedance and the propagation function were modelled by using the method of vector fitting. All the elements in each column of the transformation matrix were fitted using the same poles. Another model in phase domain, named universal line model (ULM), was proposed by Morched, Gustavsen and Tartibi in 1999 [3]. This model arose from the necessity of modelling highly frequency-dependent transformation matrices and widely different modal velocities. This model is considered today the most advanced and exact one in the time domain. Further researches have focused on improving this model in terms of passivity enforcement, stability and symmetry preservation [4–7]. Recently, it has been shown that this model, with corresponding modifications, can be effectively applied to perform real-time simulations [8].

A different approach for the modelling of transmission lines is based on state-space techniques in lumped parameter representations [9, 10]. However, this approach requires the external inclusion of frequency dependence of the electrical parameters and the discretisation of the line in a number of segments, which can be prone to numerical oscillations. A recent paper has proposed the use of a finite impulse response digital filter to reduce this problem [11].

This work presents a new model of overhead multiconductor transmission lines (MTL) for time-domain transient analysis. The model is based on the time-domain solution of the telegrapher’s equations using the method of characteristics [12]. The aim of this method is to convert partial differential equations to ordinary differential equations and then solve the problem using finite differences. The method of characteristics has been used before in modelling non-uniform, non-linear and external field-excited transmission lines as well as cables and machine windings [13–15]. In these cases using this method requires a time–distance discretisation mesh.

In the model presented in this paper, following the results presented in [16] for single-phase frequency-dependent lines, and in [17] for multiconductor frequency independent lines, the method of characteristics is reformulated for uniform MTL with frequency-dependent electrical parameters. In this model, no discretisation mesh is required and Norton equivalent circuits for the line ends are developed. This model possesses some important advantages in comparison with existing frequency-dependent line models:

- Modal transformation matrices are constant and the frequency dependence of the electrical parameters is embedded in the convolution term of the series transmission line equation.
- It requires only the synthesis of the transient resistance, while travelling wave models require synthesising the characteristic admittance and the propagation exponential matrices.
- Owing to the smoothness of the transient resistance, its rational fitting is straightforward, requires only real poles and there is no need of extracting time delays.
- It only requires two matrix vector convolutions for the transmission line Norton model.

follows
$$-\frac{dV(x, s)}{dx} = \left( R'(s) + L_0 s \right) I(x, s) \quad (3a)$$
where $R'(s)$ is the transient resistance [19] given by
$$R'(s) = \frac{Z_C(s) + Z_E(s)}{s} \quad (3b)$$
Transforming (3a) to the time domain
$$\frac{\partial v(x, t)}{\partial x} + L_0 \frac{\partial i(x, t)}{\partial t} + \frac{\partial}{\partial t} \int_0^t r'(t - \tau) i(x, \tau) d\tau = 0 \quad (4a)$$
and transforming (1b