# Electro-mechanical transient modeling of MMC based multi-terminal HVDC system with DC faults considered
Liang Xiao, Zheng Xu, Huangqing Xiao*, Zheren Zhang, Guoteng Wang, Yuzhe Xu
College of Electrical Engineering, Zhejiang University, Hangzhou, Zhejiang 310027, PR China

\* Corresponding author. E-mail address: xhqhz@zju.edu.cn (H. Xiao).

**Keywords:** DC fault simulation, Electro-mechanical transient model, Modular multilevel converter, Multi-terminal HVDC system, Transient stability

**Abstract:** Modeling different types of DC faults in modular multilevel converter based multi-terminal HVDC (MMC-MTDC) systems for transient stability analyses has not been well studied. In this paper, an improved electro-mechanical model of MMC-MTDC system which is feasible for a variety of DC fault simulations is proposed. Firstly, the improved MMC electro-mechanical model with a second-order DC side circuit is derived theoretically. Then a method based on preset DC fault information for studying the impacts of DC faults on the stability of large-scale AC/DC power systems is proposed, with which the DC faults can be handled efficiently without reconstructing the DC topology. Theoretical and simulation studies show that the DC-side equivalent circuit of the MMC should be established as a second-order circuit when DC faults are considered for transient stability studies. Simulations of various types of DC faults in the modified IEEE 39-bus system incorporating a four-terminal MMC-HVDC system are carried out on PSS/E for validating the proposed method.

## 1. Introduction
With the advancement and wide range application of power electronics technology [1–8], MMC-based multi-terminal HVDC (MTDC) systems have drawn more and more attention both from academic and industrial fields. Currently, the four-terminal MMC-based HVDC grid (Zhangbei Project) [9] adopting overhead lines is under construction in the North China Power Grid. Due to the high line fault rate, the impacts of various types of DC faults on the stability of power systems should be paid special attention. However, modeling different types of DC faults in MMC-MTDC systems for transient stability analyses has not been well studied. The goal of this paper is to provide a method for modeling an improved MMC-MTDC electro-mechanical model with DC faults considered, which is useful for transient stability studies of large-scale AC/DC systems.

Time-domain simulation method is widely used for transient stability study of large-scale AC/DC power systems [10]. The basic process is to solve the system differential-algebraic equations (DAEs) with appropriate numerical integration method, so as to obtain the dynamic response of the power system under a specific disturbance. Consequently, developing a computationally efficient and accurate model to describe the dynamic characteristic of an equipment is the prime work for transient stability study.

Researchers have developed plenty of MMC models for different application scenarios [11–16]. Extraordinarily, the CIGRE Working Group B4.57 released a guide for the development and usage of MMC models in the year 2014 [14]. According to its definition, there are seven types of MMC models, varying from the most complex Full Physics Based Models with detailed semiconductor devices to the computational efficient Average Value Models (AVM, Type 5) based on switching functions, etc. Among these models, the most widely used Detailed Equivalent Circuit Model (DECM, Type 4) was first proposed in [11]. The Type 4 DECM has the benefit of high efficiency as well as good accuracy but can only be implemented in electro-magnetic transient (EMT) tools. There are some common features in the Type 5 AVMs and Type 6 Electro-mechanical Models (also called Phasor Models, RMS Models, etc.), e.g. the large number of IGBTs are not explicitly modeled and their DC and AC side circuits are modeled as controlled current and voltage sources, thus both of them have the advantage of computational efficiency. However, harmonic contents from the modulation control are generally considered for the Type 5 AVMs [14]. The Type 6 Electro-mechanical Models are developed by neglecting all harmonics and are implemented in phasor-frame electro-mechanical simulation tools. Obviously, for long time range and large-scale power system transient stability studies, the Electro-mechanical Models are preferred to the EMT-type MMC models. This is because on one hand, in commonly used transient stability simulation tools (e.g. PSS/E), the AC networks are represented by complex phasors without considering any harmonics; on the other hand, the interactions of the MMCs with the host AC grids are dominated by the external dynamic characteristics rather than the internal dynamics of the MMCs.

The demand to analyze the stability of AC-MTDC systems has led to ongoing efforts in developing the MMC/VSC electro-mechanical model with DC faults considered [17–26]. A generalized dynamic VSC MTDC model valid for

| Symbol | Description |
|---|---|
| $C_{eq}$ | equivalent capacitance of the MMC |
| $C_{sm}$ | capacitance of the sub-module (SM) |
| $N$ | number of SM per arm |
| $i_{dcs}$ | controlled direct current source |
| $L_{arm}$, $R_{arm}$ | inductance and resistance of each arm |
| $L_t$, $R_t$ | inductance and resistance of transformer |
| $u_v$ | controlled AC voltage source |