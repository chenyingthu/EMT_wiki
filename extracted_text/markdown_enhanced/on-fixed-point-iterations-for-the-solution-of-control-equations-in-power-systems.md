# On fixed-point iterations for the solution of control equations in power systems transients

**C.F. Mugombozi** a,b,∗, **J. Mahseredjian** a, **O. Saad** b  
a Ecole Polytechnique de Montréal, Canada  
b IREQ/Hydro-Quebec, Montréal, Canada  

∗ Corresponding author at: École Polytechnique de Montréal, C.P. 6079 succ. Centre-ville, Montréal, Québec, Canada H3C 3A7. Tel.: +1 450 652 8313.  
E-mail addresses: chuma-francis.mugombozi@polymtl.ca, mugombozi.chuma-francis@ireq.ca (C.F. Mugombozi), jeanm@polymtl.ca (J. Mahseredjian), saad.omar@ireq.ca (O. Saad).

**Article history:**  
Received 14 November 2013  
Received in revised form 12 March 2014  
Accepted 31 March 2014  
Available online xxx  

**Abstract**  
This paper contributes toward the establishment of a formal analysis method of control system equations solved through fixed-point iterations. The success of fixed-point iterations relies on contraction properties of the function to be iterated. A convergence criterion is presented and accuracy is not sacrificed over gain in computational performance.  
The presented algorithms are illustrated in EMTP-RV for practical control systems used in wind power generation and for a user defined model case. Limitations and performances are discussed in relation to the Newton method.

**Keywords:**  
Control system equations, Fixed-point iterations, Coates graph, Feedback interconnection, EMTP, Nonlinear equations

## 1. Introduction
AN iterative Newton method for the solution of control system equations in electromagnetic transient (EMT) type simulation methods has been proposed in [1]. Although it represents a robust and systematic approach, there are some feedback based control systems that can be also solved using the much simpler and sometimes more efficient fixed-point (FP) method. The efficiency level of the FP method can be very high since it only sequentially evaluates the control blocks and does not require time-consuming linearization procedures and matrix formulations required in the Newton method. The difficulty is in the determination of whether or not the FP method can converge for a given case, before it is actually undertaken.

Moreover, in some classes of control system equations, the model loops may lead to algebraic constraints. In such cases, the basic sequential evaluation of blocks is not applicable. Different approaches can be undertaken to reformulate models in order to apply a sequential solution. The approach proposed in [2] consists of breaking algebraic loops. This approach is acceptable when the loop is artificial, i.e. when it can be eliminated without compromising the physical behavior of the model. Specific tools are dedicated to achieve such elimination [3]. However, some cases require algebraic constraints that cannot be easily eliminated. A possible solution consists in re-organizing blocks to eliminate algebraic loops while still maintaining functionality, but as pointed out in [3], this may become prohibitively difficult.

Loop-breaking is valid for some classes of control system equations, but it was proven that it may fail for others, for instance, when nonlinear (NL) blocks appear in the feedback path [1]. A highly accurate algorithm should handle algebraic loops by solving a set of NL control equations simultaneously while maintaining computational performance, but this is not usually the case and iterative solutions may require longer computing times.

It is proposed in this paper to analyze control system equations to formally display the contractive properties of loop paths. The success of the FP method relies on contraction properties of the iterated function [4–7]. It is proposed, in this paper, to study the iterated functions by analyzing the Jacobian matrix in association with the isolated variables representing the feedback loop path. Graph theory techniques are used for that purpose. The consideration of such properties may widen the usage of FP methods. When the convergence criterion is established, solution accuracy is not sacrificed over reduction in computing time. Additional iterations permit achieving convergence for a predefined tolerance.

This paper contributes to the establishment of a formal analysis method of control system equations which permits safe usage of the FP method.

The analysis proposed in this paper is illustrated for the simulation of practical control systems in the study of power system transients. The test cases are for wind power generation and user defined model equations for an electrical machine.

## 2. Theoretical background
f1
f3 f4 f5 f8 f9
Input u +_ PROD ++ ++ f 6 300 f7 f10 f2 c f11 600