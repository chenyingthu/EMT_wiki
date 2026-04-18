# A Binary Frequency-Region Partitioning Algorithm for the Identification of a Multiphase Network Equivalent for EMT Studies
Taku Noda, Member, IEEE

**Abstract**—Previously, a method for identifying a multiphase network equivalent for electromagnetic transient calculations using partitioned frequency response has been proposed. The method accurately and robustly identifies an equivalent of the target network by dividing its frequency response into sections, but no specific algorithm for the frequency-region partitioning has been proposed. To make the entire identification process automatic, this letter proposes a binary partitioning algorithm.

**Index Terms**—Electromagnetic transient analysis, equivalent circuits, frequency response, interconnected power systems, power system modeling, power system simulation.

## I. INTRODUCTION
ELECTROMAGNETIC TRANSIENT (EMT) simulations have become crucial for the design and operation of a power system. For reducing the computational burden, it is often desirable to replace a large part of a power system far from the source of a transient with a reduced-order network equivalent. Obtaining a network equivalent of an apparatus, such as a transformer, whose equivalent circuit is not obvious but its frequency response is available by measurement, is also desirable. To these ends, a method for identifying a multiphase network equivalent for EMT calculations utilizing partitioned frequency response has been proposed [1]. The method divides the frequency response of the target network into sections, and by applying enhanced rational fitting to each section, it accurately and robustly identifies equivalent poles of the target and, thus, a network equivalent. However, no specific algorithm for the frequency-region partitioning has been proposed. To make the entire identification process automatic, this technical letter proposes a binary algorithm of frequency-region partitioning for the identification method.

## II. REVIEW OF THE IDENTIFICATION METHOD
The identification method proposed in [1] assumes that the frequency response of the target network is given in the form of an $N$-by-$N$ transfer function matrix $\mathbf{H}$ defined at discrete angular frequencies $\omega_k$. If the input to the network is the voltages of the terminals and the output is their currents, $\mathbf{H}$ is an admittance matrix. The identification method first identifies the poles $p_m$ by the frequency response of $\text{tr}(\mathbf{H})$ (i.e., the matrix trace of $\mathbf{H}$). In this pole identification process, the frequency response is divided into sections and enhanced rational fitting is applied to each section. Since the frequency range of each section is limited, the terms in the rational function do not cause ill conditioning in the fitting process. The residue matrices of size $N \times N$ can be identified by a least-squares method using the entire frequency response with the known poles. Finally, we obtain the matrix partial fraction expansion (MPFE) model

$$ \text{(1)} $$

of the target network, where $\mathbf{D}$ is a constant $N$-by-$N$ matrix.

## III. BINARY PARTITIONING ALGORITHM
### A. Algorithm
The bandwidth of each frequency section in the pole identification process should be narrow enough so that the $M$ terms in the rational function do not cause ill conditioning in the least-squares fitting process. However, ill conditioning comes not only from the bandwidth but also from the shape of the frequency response in the section. Thus, explicitly calculating an appropriate bandwidth would be difficult.

The proposed binary partitioning algorithm is based on a trial-and-error process. First, the rational fitting for the pole identification is applied to the entire frequency region without partitioning. If the rational fitting achieves specified accuracy, the pole identification is completed. Otherwise, the frequency region is divided into two sections and the same procedure is recursively applied to both sections. The subdivision is repeated until all subsections achieve specified accuracy. The algorithmic description of the proposed binary partitioning is shown in Table I. In this way, it is ensured that all poles are identified within specified accuracy.

| **TABLE I** |
| :--- |
| PROPOSED BINARY PARTITIONING ALGORITHM |

### B. Treatment of Boundary
In the algorithm description above, how a section is divided into two subsections is not mentioned. Since two neighboring subsections should not identify (share) the same poles, the boundary of two subsections should be placed at a local minimum of the magnitude of $\mathbf{H}$. Therefore, the following procedure is used. First, the boundary is placed at the midpoint of the frequency section of interest ("current section" in Table I). Starting from the midpoint, the closest local minimum is searched for. This search can be coded by a simple loop with a comparison of values. If a local minimum is found within a distance from the midpoint closer than the half the bandwidth of the section, then the boundary is moved to the local minimum. Otherwise, (if a local minimum is not found nearby), the boundary remains at the midpoint.

## IV. NUMERICAL EXAMPLE
Fig. 1 is the test network.

**Fig. 1.** Test network.

**Fig. 2.** Result of the pole identification process with the result of frequency-region partitioning by the proposed binary algorithm.

**Fig. 3.** Identification result for some elements of the admittance matrix. (a) The (1,1) element is shown. (b) The (1,2) element is shown.

*Manuscript received August 29, 2006. Paper no. PESL-00062-2006.*  
*The author is with the Electric Power Engineering Research Laboratory, Central Research Institute of Electric Power Industry (CRIEPI), Kanagawa 240-0196, Japan (e-mail: takunoda@ieee.org).*