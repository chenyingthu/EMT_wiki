# Review and comparison of frequency-domain curve-fitting techniques: Vector fitting, frequency-partitioning fitting, matrix pencil method and loewner matrix
**B. Salarieh** *, **H.M.J. De Silva**  
*Manitoba Hydro International Ltd, Winnipeg, MB R3P 1A3, Canada*

**Keywords:** Frequency dependent network equivalent, Matrix pencil method, Loewner matrix, Vector fitting, Frequency-partitioning fitting, Model order reduction

**Abstract**  
It is a well-known practice to approximate the frequency-domain response of an electrical component or a subsystem with rational functions for electromagnetic transient (EMT) simulations of power systems. There are a variety of curve-fitting methods developed over time that offer different levels of accuracy, speed, and complexity. In some cases, the order of rational function may get very large to meet specified error criteria. Model order reduction (MOR) methods can be used to decrease the order of the function without a considerable deterioration of the approximation error. This paper presents a thorough review and comparison of the most popular curve-fitting methods, namely, the vector fitting (VF) method along with its later developments, the frequency-partitioning fitting (FpF) methods, matrix pencil method (MPM) and loewner matrix (LM) fitting technique. First, the fundamental theories of each one are briefly reviewed. Then, their accuracy and fitting order are compared together through three case studies. Lastly, the application of two different MOR methods to the resulted rational function is investigated.

☆ Paper submitted to the International Conference on Power Systems Transients (IPST2021) in Belo Horizonte, Brazil June 6–10, 2021.  
* Corresponding author.  
E-mail addresses: bsalarieh@mhi.ca (B. Salarieh), jeewantha@mhi.ca (H.M.J. De Silva).  
https://doi.org/10.1016/j.epsr.2021.107254  
Received 27 November 2020; Received in revised form 21 March 2021; Accepted 7 April 2021  
Available online 18 April 2021  
0378-7796/© 2021 Elsevier B.V. All rights reserved.

## 1. Introduction
The electromagnetic transient simulation of power systems requires accurate modeling of system components, including their wideband frequency characteristics. Once the frequency-domain behavior seen from the terminals is known, the modeling is based on fitting a rational function to the frequency-domain characteristics, which can be in the form of admittance ($Y$), impedance ($Z$), or scattering ($S$) parameters. This way, an efficient time-domain simulation is possible using the recursive convolution [1]. There are several applications for rational fitting in time-domain studies, such as wideband modeling of frequency-dependent network equivalents (FDNE) [2,3], high-frequency transformer modeling [4], and modeling of transmission lines [5]. The vector fitting (VF) technique [6], is robust and widely applied in EMT studies. There were enhancements of VF proposed later, known as relaxed vector fitting (RVF) [7] and modal vector fitting (MVF) [8]. Another approach is the frequency-partitioning fitting (FpF) [9–11] that overcomes the ill-conditioned equations occurring on wideband responses by subdividing the frequency range of interest into several partitions and applying rational fitting to each subrange.

Alternative techniques were proposed later, such as matrix pencil method (MPM) [12] and loewner matrix [13]. These techniques have advantages such as being non-iterative, and not requiring an initial pole set. Once the rational function approximation is obtained in the forms of poles and residues, there are two postprocessing steps that perturb the model parameters. The first one is due to the passivity requirement of rational models to guarantee a stable time-domain simulation [14]. Moreover, the large number of components in a power system requires reducing the order of state-space model of the components for an efficient time-domain simulation, while maintaining the accuracy of the original model.

In this paper, following a complete review of VF, FpF, MPM, and LM, these techniques are compared together in regard to the fitting order and accuracy through three case studies. Furthermore, the application of two different MOR methods to the models obtained by these techniques is investigated. Since non of the mentioned techniques guarantee a stable model, the passivity analysis is not covered in this paper.

## 2. Review of curve-fitting techniques
The purpose of curve-fitting techniques is to approximate the frequency response of a linear time invariant (LTI) system, $F(s)$ with a rational function of the following form
$$ F(s) = \sum_{n=1}^{N} \frac{R_n}{s - p_n} + D + sE \tag{1} $$
where $s = j\omega$, and $N$ is the number of poles including the real and complex-conjugate poles. Identification of (1) is called rational fitting and different methods of calculating its parameters are described as follows.

### 2.1.2. Fast modal vector fitting (FMVF)
With the application of VF, some properties of a system may be approximated with higher accuracy than others. As an example, when fitting the elements of an admittance matrix $Y$ that has both large and small elements, the elements of higher magnitude are fitted with more accuracy than the small elements, depending on the error criterion. The resulting model does not necessarily provide a good fit for the impedance $Z = Y^{-1}$ matrix. To have an accurate model with arbitrary terminal conditions, modal vector fitting (MVF) is introduced, where the focus is on accurate representation of eigenvalues (modes) instead of matrix elements [8]. Let’s consider a multiport system characterized by its admittance matrix $Y$. First, we diagonalize this matrix by a transformation matrix $T$ and