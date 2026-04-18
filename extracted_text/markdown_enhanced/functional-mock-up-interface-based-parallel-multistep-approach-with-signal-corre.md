# Functional Mock-Up Interface Based Parallel Multistep Approach With Signal Correction for Electromagnetic Transients Simulations

Ming Cai, Student Member, IEEE, Jean Mahseredjian, Fellow, IEEE, Ulas Karaagac, Member, IEEE, Ali El-Akoum, and Xiaopeng Fu, Member, IEEE

**Abstract**—This letter presents the latest improvements of a previously proposed parallel and multistep approach based on the functional mock-up interface standard for the simulation of electromagnetic transients. The improved approach extends the capacity of the original parallel asynchronous mode into accommodating the use of different time-steps in different decoupled subsystems. It also introduces a signal correction procedure using linear extrapolation in multistep simulations, greatly enhancing simulation flexibility, efficiency, and accuracy. Numerical examples are provided to demonstrate the computational advantages of the improved approach.

**Index Terms**—FMI, electromagnetic transients, parallel simulation, multistep simulation.

*Manuscript received December 19, 2018; accepted February 22, 2019. Date of publication March 4, 2019; date of current version April 17, 2019. This work was supported by the NSERC Industrial Chair. Paper no. PESL-00287-2018. (Corresponding author: Jean Mahseredjian.)*
*M. Cai and J. Mahseredjian are with Polytechnique Montréal, Montreal, QC H3T1J4, Canada (e-mail: ming.cai@polymtl.ca; jean.mahseredjian@polymtl.ca).*
*U. Karaagac is with The Hong Kong Polytechnic University, Hong Kong (e-mail: ulas.karaagac@polyu.edu.hk).*
*A. El-Akoum is with Électricité de France (EDF) Lab Paris-Saclay, Palaiseau 91120, France (e-mail: ali.el-akoum@edf.fr).*
*X. Fu is with Tianjin University, Tianjin 300072, China (e-mail: fuxiaopeng@tju.edu.cn).*

## I. INTRODUCTION

WITH the ever-growing popularity of Electromagnetic Transient (EMT) simulation tools [1]–[3] among utility engineers, the computing time reduction has become crucially important due to the constraint from numerical integration time-step as well as high accuracy models. In the meantime, state-of-the-art developments in HVDC systems and wind generation [4] have created more and more challenging cases for the studies of modern-day power systems, which also prompted computing time reduction to become a hot research topic.

Many techniques proposed over the years to improve computation speed in EMT-type solvers fall into two categories, which are parallel and multistep approaches (see references in [5]). Despite certain numerical advantages, the implementation of many of these techniques is limited by either the network decoupling interface, level of user intervention, or flexibility.

This letter proposes new developments that further enhance the performance of a previously proposed co-simulation-based parallel and multistep approach using the Functional Mock-Up Interface (FMI) standard [6] for EMT simulations with complex control systems [5]. In the improved approach, the computation capacity of the original parallel asynchronous mode is extended into accommodating the use of different time-steps in different subsystems decoupled in memory, greatly improving simulation flexibility and efficiency. Furthermore, a signal correction procedure based on linear extrapolation is introduced to achieve higher accuracy in a multistep simulation environment. Test cases studied in this letter demonstrate that the newly developed features have markedly upgraded the previously proposed approach [5] in terms of flexibility, efficiency and accuracy.

## II. IMPROVEMENTS ON AN FMI-BASED PARALLEL AND MULTISTEP APPROACH

### A. Parallel Multistep Asynchronous Mode

The synchronization scheme between master and slaves in the improved parallel multistep asynchronous mode is divided into three scenarios based on the comparison of master and slave time-steps, as are presented in Figs. 1, 2, and 3. The definitions of the terms in these figures can be found in [5].

The first scenario (Fig. 1) in which $\Delta t_{master} = \Delta t_{slave}$ was already implemented in [5].

In the second scenario where $\Delta t_{master} < \Delta t_{slave}$ (Fig. 2), after waiting for the slave to release SemMaster, the master keeps releasing SemMaster to itself if it lags behind the slave to catch up with the latter, and it releases SemSlave to the slave once it catches up such that both can execute their subsequent calculations simultaneously.

If $\Delta t_{master} > \Delta t_{slave}$ (third scenario), the master keeps releasing SemSlave to the slave for it to catch up if it lags behind. Once the slave catches up, the master releases SemSlave once more and both continue their subsequent calculations in parallel. Such an improved synchronization mechanism allows multiple time-steps to be employed in the parallel asynchronous mode, considerably enhancing simulation flexibility and efficiency.

**Fig. 1.** First synchronization scenario ($\Delta t_{master} = \Delta t_{slave}$) between master and slave in the parallel multistep asynchronous mode.

**Fig. 2.** Second synchronization scenario ($\Delta t_{master} < \Delta t_{slave}$) between master and slave in the parallel multistep asynchronous mode.

**Fig. 4.** Test benchmark.

| **TABLE I** |
| :--- |
| TEST CASE CO-SIMULATION MODE SCENARIOS |

Extrapolation on $y_{slave}$ is performed if the master keeps advancing and reading in the same data at $t = T$ as at $t = T - \Delta t_{slave}$.