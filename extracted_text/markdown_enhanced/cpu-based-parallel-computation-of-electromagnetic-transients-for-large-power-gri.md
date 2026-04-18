# CPU based parallel computation of electromagnetic transients for large power grids

**A. Abusalah**^a, **O. Saad**^b, **J. Mahseredjian**^a,*, **U. Karaagac**^c, **L. Gerin-Lajoie**^b, **I. Kocar**^a

^a Ecole Polytechnique Montreal, Quebec H3C 3A7, Canada  
^b IREQ, Hydro-Québec, Varennes, Quebec, J3X 1S1, Canada  
^c Hong Kong Polytechnic University, Hung Hom, Hong Kong  

**Keywords:** Electromagnetic transient, Modified-augmented-nodal-analysis, KLU, Sparse matrix solver

**Abstract:** This paper presents the implementation of a parallel sparse matrix solver for improving the computational speed of an electromagnetic transients (EMTs) simulation software. The new method is established on the KLU sparse matrix solver which is suitable for circuit based simulation methods The solver is programmed using parallelization through automatic detection of sparse matrix submatrices separated by the natural decoupling available in transmission line/cable models. The proposed approach is demonstrated in an EMT-type software that uses a fully iterative solution method for all nonlinear models. Furthermore, it is demonstrated for realistic large scale grids.

## 1. Introduction

Computation time is a crucial parameter in the simulation of power system electromagnetic transients (EMTs). This aspect is becoming increasingly important with modern power systems that include the integration of wind generators, HVDC transmission links and various other devices. Moreover, due to the much superior accuracy of the circuit-based approach in EMT computation methods, there is a trend to extend its application to the simulation of electromechanical transients for the same grid data set. This could require modeling very large scale networks. EMT computations with such a network are presented and compared in Ref. [1].

It is possible to improve the computational performance for off-line EMT-type solvers by programming more efficient solution methods and models, but such research does not allow to achieve significant gains due to the inherent algorithms for circuit based modeling. Other approaches for improving performance include multiple time-step (multi-rate) solutions [2], waveform relaxation [3,4], combinations of different time-frame methods [5] and interfacing with frequency dependent network equivalents [5,6]. The main difficulty with such methods is generalization, automation and control of accuracy. The industrial grade implementation of such methods into existing EMT-type software poses major challenges.

A direct approach for off-line EMT-type computational speed improvement is the application of parallelization. This is supported by the fact that the current trend in the computing industry is to deliver parallel computers rather than faster processor units.

The parallelization approach is researched in many publications [7,8] and has been initially applied in real-time simulation tools [9–11]. Off-line methods have been proposed in Refs. [12,13] and other publications. Network tearing for parallelization without any loss of accuracy is based on the natural time delay formed by distributed parameter transmission line (or cable) models. It is also possible to avoid approximations using other tearing techniques, such as in Ref. [14], when transmission line models are not present in a given network. In addition to CPU based parallelization, work has been done using other technologies, such as GPU [15].

An important difficulty in several references presented above, such as Ref. [13], is that user intervention is required to decide on parallelization tasks, interfacing procedures or selection of equivalents. Some real-time simulators [9] are capable of automatic task scheduling, but they are not based on the sparse-matrix solution approach researched in this paper.

The objective in this paper is to present shared memory CPU based parallelization on conventional multi-core computers. The objective is also to avoid any user intervention in the parallelization process. The presented work targets the upgrading of existing sparse matrix based solvers. Network tearing for parallelization is based on the natural decoupling delay caused by distributed parameter transmission line models. There are no approximations in the proposed approach.

This paper demonstrates the application of a new sparse matrix solver for an existing EMT-type simulation tool (EMTP [16]) for improving computational performance through automatic parallelization. Another distinctive contribution in this paper is that parallelization is applied for a fully iterative solver. All nonlinear models are solved simultaneously using the Newton method. The iterations are essential for delivering highest accuracy, but the iterative process creates supplementary computational burden.

The contributions of this paper are tested on a new version of the very large scale Hydro-Quebec grid benchmark initially presented in