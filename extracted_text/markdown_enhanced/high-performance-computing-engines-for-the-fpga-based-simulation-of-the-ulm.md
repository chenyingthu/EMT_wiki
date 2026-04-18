# High performance computing engines for the FPGA-based simulation of the ULM

Tarek Ould-Bachir$^{a,1,*}$, Hossein Chalangar$^{b,1}$, Keyhan Sheshyekani$^{b}$, Jean Mahseredjian$^{b}$

$^a$ Department of Computer Engineering and Software Engineering, Polytechnique Montréal, Montreal, Canada  
$^b$ Department of Electrical Engineering, Polytechnique Montréal, Montreal, Canada

**Keywords:** FPGA-Based simulation, Universal line model, Real-time simulation, Travelling-wave fault location

**Abstract:** This paper presents a design methodology for the FPGA-based simulation of the Universal Line Model (ULM). The proposed approach yields a higher computational performance compared to alternative implementations reported in the literature. Such performance allows the use of the FPGA model in real-time simulation applications or for the acceleration of offline EMT programs. A state-space approach is used to perform the time-domain simulation of the pole-residue form of the rational fitting of the characteristic admittance and propagation functions. The paper also discusses the appropriate scheduling of the ULM computations and proper management of the history terms that lead to an optimized hardware utilization, low latency response times, and higher computational performances using floating-point arithmetic.

## 1. Introduction

The Universal Line Model (ULM) [1] is a wide-band frequency-dependent model for lines and cables. The model includes full frequency dependency of the Transmission Line (TL) and cable parameters. The ULM with its various improvements [2–4] is currently recognized as being the most accurate wide-band model. The ability to run the ULM on FPGA is justified by various application requirements such as Hardware-in-the-Loop (HIL)-based testing of Travelling Wave Fault Locators (TWFLs). Modern TWFLs can locate a fault within a tower span ($\pm$ 300 m), but require 1 MHZ sampling rate to achieve such performance. Real-time simulators can indeed be used for providing a comprehensive test-bench for protection relays. Such a setup can be beneficial in the sense that it provides flexibility for selecting power system parameters as well as fault type and location while allowing the regeneration of real-time signals. Moreover, real-time simulators provide the possibility of in-situ testing of protection relays. However, for a HIL setup to function properly as a TWFL testbed, the simulated network necessitates a sub-microsecond time-step as well as accurate frequency-dependent line models [5].

CPU-based real-time simulation of the ULM have been shown to be rather computationally expensive for real-time simulation purposes because of the high fitting order of the lines [6], with simulation time-steps in the > 10 µs range. On the other hand, FPGA-based real-time implementations of the ULM have been proposed in the literature, but fail to reduce the simulation time-step below 1 µs. Recently, an FPGA-based implementation of the ULM for HIL-based testing of TWFLs has been proposed in [7]. The line model is based on the second-order realization of TL’s state-space equations [8] and achieves a time-step of 1.42 µs, while sustaining a clock frequency of 175 MHz.

To achieve a better performance, this work proceeds by increasing the clock frequency and deepening the pipeline to improving the computational performance. This however comes typically with a latency penalty. Hence, a thought-out rescheduling of the ULM equations is proposed to achieve more FLOPS at a lower latency. The real-time simulation of the ULM reported in this work can sustain a 250 MHz clock frequency and is shown to achieve a time-step as low as 200 ns, while offering proper accuracy for HIL-based TWFL testing.

The remainder of this paper is organized as follows. The theoretical background of the ULM is presented in Section 2. The proposed FPGA-based design methodology for an ULM simulator is discussed in Section 3. Section 4 elaborates on the test cases used to assess the performance of the FPGA model against EMTP [9] and discusses the footprint of the FPGA implementation as well as the computational accuracy resulting from the use of a non-standard floating-point (FP) format.

$$x_{Y_j c}(t + \Delta t) = \alpha_{j Y_c} x_{Y_j c}(t) + \beta_{j Y_c} v_k(t) \tag{8}$$

$$x_{i_{H,j}}(t + \Delta t) = \alpha_{i_{H,j}} x_{i_{H,j}}(t) + \beta_{i_{H,j}} \{ i_{rm}(t - \tau_i) + i_{rm}(t - \tau_i + \Delta t) \} \tag{9}$$

The time domain shunt and incident currents at the sending end $k$ are then obtained for the next time-point as follows:
$i_{\text{hist}}$

---
$^*$ Corresponding author.  
E-mail addresses: tarek.ould-bachir@polymtl.ca (T. Ould-Bachir), hossein.chalangar@polymtl.ca (H. Chalangar), keyhan.sheshyekani@polymtl.ca (K. Sheshyekani), jean.mahseredjian@polymtl.ca (J. Mahseredjian).  
$^1$ These authors contributed equally to this work.