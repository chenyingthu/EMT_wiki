# DQ Admittance Model Extraction for IBRs via Gaussian Pulse Excitation
**Lingling Fan**, *Fellow, IEEE*, **Zhixin Miao**, *Senior Member, IEEE*, **Li Bao**, *Student Member, IEEE*, **Shahil Shah**, *Senior Member, IEEE*, and **Rahul H. Ramakrishna**, *Student Member, IEEE*

**Abstract**—While dq admittance models have shown to be very useful for stability analysis, extracting admittance models of inverter-based resources (IBRs) from the electromagnetic transient (EMT) simulation environment using frequency scans takes time. In this letter, a new perturbation method based on Gaussian pulses in combination with the system identification algorithms shows great promise for parametric dq admittance model extraction. We present the dq admittance model extracting method for a type-4 wind turbine. Challenges in implementing Gaussian pulse excitation are also pointed out. The extracted dq admittance model via the new method shows to have a high matching degree with the measurements obtained from frequency scans.

**Index Terms**—Inverter-based resources, admittance model, measurement.

Manuscript received 20 September 2022; revised 23 December 2022 and 2 February 2023; accepted 27 February 2023. Date of publication 13 March 2023; date of current version 24 April 2023. This work was supported in part by the U.S. Department of Energy SETO under Grant DE-EE-0008771, in part by the National Renewable Energy Laboratory, operated by Alliance for Sustainable Energy, LLC, for the U.S. Department of Energy (DOE) under Contract DE-AC36-08GO28308, and in part by National Science Foundation under Grants 2103480 and 1807974. Paper no. PESL-00247-2022. (Corresponding author: Lingling Fan.)

Lingling Fan, Zhixin Miao, Li Bao, and Rahul H. Ramakrishna are with the Department of Electrical Engineering, University of South Florida, Tampa, FL 33620 USA (e-mail: linglingfan@usf.edu; zmiao@usf.edu; libao@usf.edu; rahul12@usf.edu).
Shahil Shah is with the National Renewable Energy Laboratory, Golden, CO 80401 USA (e-mail: shahil.shah@nrel.gov).

## I. INTRODUCTION
While dq admittance models have shown to be very useful for stability analysis (see e.g. [1]), extracting admittance models of inverter-based resources (IBRs) from the electromagnetic transient (EMT) simulation environment using frequency scans takes time. The frequency scanning method may require hundreds of experiments. For each experiment, a sinusoidal perturbation with a given frequency is injected into an input portal and the measurements of the output portals are recorded and processed to extract the phasor of the harmonic component [2].

To speed up the process, alternative model extraction methods have been employed. In general, there are two categories of models that can be obtained from measurement data: non-parametric (Category 1) and parametric (Category 2) [3]. Non-parametric models can be time-domain impulse responses at discrete time points and frequency-domain responses at discrete frequency points. Frequency scans lead to non-parametric models. Parametric models include those expressed as transfer functions or state-space models. To obtain parametric models from non-parametric models, a data fitting procedure has to be carried out, as shown in [4], [5].

In Category 1, speeding up can be realized by use of multi-tone sinusoidal or chirp signal injection followed by the cross-correlation analysis [6], or the pseudo random binary signal (PRBS) injection followed by the cross-correlation analysis [7]. Note that for better outcomes, PRBS injection usually repeats sequences for several times. For example, in [8], five repetitions show to produce more accurate frequency responses from 0.06 to 10 rad/s with 200-s simulation data being used.

Compared to non-parametric models, parametric models have a unique advantage. They can be used directly for analysis and simulation. This feature also makes model validation very easy. After a model is obtained from a training data set, it can be used to simulate output responses for another data set. A high matching degree indicates the good quality of a model.

In Category 2, various system identification methods may be applied to extract input/output models. The authors have designed a dq admittance identification method using subspace methods in [9]. Two step response experiments are used to create two sets of output data, which were further converted to the Laplace domain expressions. Eventually, a dq admittance model in the Laplace domain can be found. This method has also been implemented to extract the dq admittance of a real-world 2.3-MW commercial battery inverter located in NREL’s Flatiron campus [5]. Experiment results show that step response experiment requires to have large enough perturbation to create output data and differentiate noise and signals. The voltage perturbation applied needs to be at 10% of the nominal voltage magnitude. Such step excitation changes the system operating conditions. Hence, impulse perturbations are preferred.

An ideal impulse injection is difficult to implement numerically. Instead, a Gaussian pulse can be used to emulate an ideal impulse. A Gaussian pulse does not have abrupt changes and has a continuous and smooth waveform.

In this letter, we present a new dq admittance extraction method based on Gaussian pulse excitation. Gaussian pulse excitation has been popularly used in physics [10]. The time-domain expression of a Gaussian pulse and its Fourier transform are as follows.

$$g(t) = \frac{1}{\sqrt{2\pi\sigma}} e^{-\frac{t^2}{2\sigma^2}}, \quad G(f) = e^{-\frac{1}{2}(2\pi\sigma f)^2}$$

They are shown in Fig. 1. It can be seen that the Fourier transform of a Gaussian pulse is also a Gaussian pulse in the frequency domain.