# Use of efficient task allocation algorithm for parallel real-time EMT simulation

Boris Bruned, Pierre Rault, Sébastien Dennetière, Ian Menezes Martins

^a^ RTE - Réseau de Transport d'Electricité, 69330 Jonage, France
^b^ RTE - Réseau de Transport d'Electricité, 92800 Puteaux, Paris – La Défense, France

**Keywords:** Graph partitioning, Hardware-in-the-loop, Optimization, Parallel simulation, Real-time simulation, Task allocation problem

**Abstract**
Real-time EMT (Electromagnetic Transients) simulation relies on multi-cores computers to accelerate the simulation through parallelization. It also increases simulation accuracy by allowing a lower time step. First, the network has to be split into several tasks using a separation technique. Then, each task has to be allocated/mapped to a processor. This paper focuses on this problem which can be formulated as a TAP (Task Allocation Problem). To find optimal task allocation, operational research techniques can be used. Heuristics such as graph partitioning allow getting fast solutions. Their performances are asserted with very large networks and real-time simulator architectures, both from TSO (Transmission System Operator) grids. Exact resolution methods are used to verify solution quality. The validation of each task mapping strategy is done through a real EMT case study which involves real-time Hardware-in-the-Loop simulation.

## 1. Introduction

The need for real-time EMT simulation has increased with the development of power electronic devices in the transmission network related to the high penetration of wind power farms and High Voltage Direct Current (HVDC) links. Since 2011, the French TSO, RTE, has created his own real-time laboratory SMARTE to study interaction between these new power devices. Hardware-In-the-Loop simulation, which connects a real-time simulator to a replica of the on-site control system, allows performing accurate EMT studies close to on-field phenomena. Otherwise, the utility of replicas is various from maintenance activities to real-time event studies which have occurred on the network [1]. To improve accuracy, detailed networks are used for EMT simulation [2] although interesting network reduction methods based on frequency equivalent [3,4] help in certain cases to accelerate the simulation.

To cope with large networks, real-time EMT tools take advantage of the parallelization offered by multicore computers used as real-time simulators [2]. Indeed, in the real-time environment, it will accelerate the simulation but above all, it will respect the time constraints to be able to interact with a hardware device such as a control replica. The parallelization is automatically performed in two steps. First, the network is separated into several tasks. Then, each network task is mapped to the simulator's processors before starting the parallel simulation. The stability of a real-time simulation depends strongly on the result of this task mapping. Indeed, if the time step is not respected after the mapping, overruns can be a source of numerical instabilities.

Previous works [2,5] have demonstrated the efficiency of graph partitioning algorithms [6] on some Software-in-the-Loop (SIL) examples. However, no full study has been done to assess performance on industrial cases and the optimality of found solutions. For the first time, this paper proposes a detailed analysis of the use of graph partitioning algorithms in EMT simulation in terms of performance and quality of the solution found. After formulating the Task Allocation Problem (TAP) [7] and presenting heuristic techniques, very large realistic network instances are tested with real architectures to verify algorithms’ performance. Then, a deep analysis of the whole graph partitioning algorithm allows understanding its advantages and limits. Hyper parameter tuning helps to improve real-time performance. Additionally, exact solutions from a linear programming formulation are first used in this paper to assert the quality of solutions found from the graph partitioning algorithms. Lastly, in complement to previous SIL examples, a Hardware-in-the-Loop (HIL) set-up of a three-terminal HVDC grid with DC Circuit Breakers validates the efficiency of the task allocation algorithm and discussed the mapping strategy.

All proposed algorithms have been tested on the real-time EMT tools HYPERSIM [8] which proposes a fully –automatic network parallelization.

## 2. Task allocation problem

That means choosing the branch that locally minimizes the communications.

### 2.1. Task separation

The first step of parallelization is to split the network into several tasks which will be run in parallel on several cores. Two main separation techniques are used for the split.

The first one relies on a decoupling element such as power lines. If the propagation delay is greater than the simulation time step, tasks can be separated through the lines. The line delay allows transmitting

### 2.3.2. Graph partitioning

The second method is based on graph partitioning techniques [6]. These heuristics are commonly used to automatically parallelize EMT simulations [5,17,18]. The goal of the algorithm is to map a “Source Graph”, SG, to a “Target Graph”, TG. It consists of partitioning the former and then mapping the resulting subsets of source vertices to a