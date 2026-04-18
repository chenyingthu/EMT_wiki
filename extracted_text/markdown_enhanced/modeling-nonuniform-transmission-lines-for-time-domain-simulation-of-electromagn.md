## Modeling Nonuniform Transmission Lines for Time Domain Simulation of Electromagnetic Transients
**Abner I. Ramirez**, Member, IEEE, **Adam Semlyen**, Life Fellow, IEEE, and **Reza Iravani**, Senior Member, IEEE

**Abstract**—Transmission lines with nonparallel conductors or significant sags and vertical structures, such as towers, can be viewed and modeled as nonuniform lines (NULs). The parameters of NULs are distance dependent. This paper presents a mathematical model for time domain simulation of electromagnetic transients in multiphase NULs taking into account the frequency dependence of the parameters. The model is based on the traveling wave phenomenon and accommodates any NUL geometry. In addition, the model can be interfaced with time domain programs such as the EMTP. The proposed methodology is validated by comparing the results with those obtained from a frequency domain model using the numerical Laplace Transform (LT), the method of characteristics (MC), and also with test results reported by other investigators.

**Index Terms**—Electromagnetic transients, frequency dependence, nonuniform line.

*Manuscript received June 6, 2001; revised July 5, 2002. This work was supported in part by the Science and Technology Council of Mexico (CONACYT) Project No. 34698-A and in part by the University of Toronto.*
*The authors are with the Department of Electrical and Computer Engineering, University of Toronto, Toronto, ON M5S 3G4 Canada (e-mail: abner@power.ele.utoronto.ca; adam.semlyen@utoronto.ca; iravani@ecf.utoronto.ca).*
*Digital Object Identifier 10.1109/TPWRD.2003.813877*

## I. INTRODUCTION
SIMULATION of electromagnetic transients in a transmission line is usually performed assuming that the conductors are parallel to ground, and thus, the parameters are uniform. There are however cases of nonuniform lines (NULs), where the line parameters have strong longitudinal variation. Examples are lines crossing rivers or entering substations and even towers may be considered in this category.

There have been several approaches for handling NULs. One is based on traveling waves and Bewley’s Lattice Diagram for single-phase lossless lines [1]. There also exist models for single-phase transmission lines for which parameters are assumed to vary exponentially; a frequency domain method is described in [2], and a time domain method in [3]. A model for towers is described in [4] for which the parameters are obtained from measurements.

Alternative models based on finite difference methods are used to solve the partial differential equations of the propagation phenomenon disregarding the frequency dependence of the parameters [5], [6].

In [7], a single-phase model is proposed in the frequency domain. In this model, a transmission line is represented as a two-port network and its transfer matrix is obtained from the multiplication of the chain matrices of the line’s subsegments. There exists also a multiphase frequency dependent model in which the NUL is subdivided and each subdivision is represented by a lossless uniform line [8]. References [9] and [10] also address the topic of modeling a NUL, assuming however constant line parameters.

Most of the methods mentioned before deal with a lossless single-phase line and a particular variation of the line parameters is considered. In this paper, a more general methodology for the time domain simulation of electromagnetic transients in NULs is presented. The proposed new approach overcomes the above mentioned limitations of existing methods. The methodology can be applied to multiphase lines where the frequency dependence of the parameters is taken into account. The proposed model has a continuous representation of the NUL and can be applied for any geometrical configuration, such as towers. In addition, the model can be interfaced with existing programs, for instance the EMTP.

## II. TERMINAL RELATIONS IN FREQUENCY DOMAIN FOR NUL
In the frequency domain, expression (1) represents the relation between voltages and currents at the two ends of the single-phase or the multiphase line of Fig. 1 [5], [11]
$$ (1) $$
where the matrix is numerically calculated by solving
$$ (2) $$
In (2), is the identity matrix, is the number of phases, and and are the impedance and the admittance matrices of the line calculated analytically or obtained from measurement. If and are calculated analytically, the matrix is obtained by chain multiplication of matrices for line segments. In the present work, the concept of complex depth is used to calculate parameters of lines and towers [12], [13].

Equation (1) contains the modal (eigenvalue/eigenvector) decomposition of the matrix. This gives the following relation between the forward and the backward waves and the propagation functions , in the forward and the backward directions
$$ (3) $$

Equation (3) relates variables of the traveling wave formulation. The transformation to phase domain quantities, valid for both ends of the line, is given by
$$ (4) $$

The relation between the forward and the backward propagation functions is
$$ (5) $$

The following inverse transformation matrix for (4) is defined
$$ (6) $$

Definitions for the characteristic admittances in the forward and the backward directions for (4) are

*Fig. 1. Notation and reference directions.*

*Fig. 2. Symmetrical, flat, three-phase NUL.*

*Fig. 3. Time domain simulation and experimental results for the line of Fig. 2.*

line (node in Fig. 1) must be taken into account together with numerical solution of the state-space approximations. As mentioned earlier, similar equations are derived for the backward direction and used for the sending end.