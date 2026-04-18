# Modeling of MMC-based STATCOM with embedded energy storage for the simulation of electromagnetic transients

Anton Stepanov a, *, Hani Saad b, Jean Mahseredjian c
a PGSTech, Montreal, QC, Canada
b ACDC Transient, Lyon, France
c Polytechnique Montreal, Canada

**Keywords:** Energy storage, Modeling, Modular multilevel converter, EMT, STATCOM

**Abstract**
The Delta-connected STATCOM is regarded as the most advantageous topology for STATCOMs based on the Modular Multilevel Converter (MMC) technology. Embedding energy storage devices into the MMCs has gained significant research interest in recent years. This paper focuses on modeling of MMC-based Delta-STATCOMs with embedded energy storage. A flexible modeling approach is proposed, which allows easy interfacing of various converter models with various energy storage device models. Four commonly used types of MMC models are applied to STATCOM modeling: detailed, detailed equivalent, arm equivalent, and average value. Supercapacitors and batteries are used as energy storage devices. Dynamic performances of the models are compared in transient simulation cases using EMTP.

## 1. Introduction
Modular multilevel converter (MMC) is a power electronic converter that generates AC voltages by inserting/bypassing the appropriate number of submodules (SMs). Each SMs represents one level of the resulting voltage waveform [1]. MMCs have several advantages over conventional 2- and 3-level voltage source converters, including easy scalability to high voltage levels, smoother AC voltage waveform, lower rate of change of voltage [2,3]. MMCs are used in many modern projects: HVDC systems [4,5], power quality improvement [6,7] and others [8,9].

Energy Storage (ES) devices allow to enhance network congestion management, to counteract the effects of intermittent power generation from renewable energy sources, provide grid frequency support, improve economic efficiency [9,10]. It has been concluded that MMCs with ES devices embedded within submodules are a promising solution to improve power quality [10–12]. Depending on the application requirements, the nominal power of the embedded energy storage may vary from partial (40% and lower) to full power of the converter, and its energy capacity likewise depends on the project requirements [10,11].

MMC-based STATCOMs can have single-star, double-star or delta topologies. Delta configuration with full-bridge (FB) SMs is considered in this paper since it has more advantages over other types [10,13].

Accurate models of various types of equipment are required to perform electromagnetic transient (EMT) simulations in the design and analysis of electrical systems. Owing to the structural complexity of MMCs, numerous nonlinear devices, and advanced control systems, many EMT models have been developed. They are generally divided into four groups [14–16]:
- **Detailed Model (DM):** represents nonlinear v-i characteristics of IGBTs. It is used to validate other models, to simulate SM internal faults, to analyze SM topologies etc.
- **Detailed Equivalent Model (DEM):** represents IGBTs as two-value resistances. Useful for the analysis of low-level controls such as capacitor balancing algorithms, modulation.
- **Arm Equivalent Model (AEM):** represents all SMs in each arm by a single equivalent circuit. Reduces computational time while keeping accuracy of internal variables such as circulating current and MMC internal energy.
- **Average Value Model (AVM):** represents all SMs in the converter as a single capacitor. Accelerates simulations while keeping accurate AC system dynamics, sufficiently accurate for transient stability studies.

Despite considerable research efforts in MMC modeling, the modeling of STATCOMs with embedded ES has not yet been widely researched. Some models have been proposed in [17,18], and [19], but only for the double-star configuration with half-bridge SMs and only using batteries as ES devices. Thus, the modeling of Delta-STATCOM configuration with FB SMs (Fig. 1) has not yet been discussed in the literature.

This paper aims to cover this gap by providing guidelines for EMT modeling of STATCOMs with energy storage using MMC technology, with a specific focus on Delta configuration. A comprehensive set of models with various types of embedded ES is presented. Plus, a generalized modeling approach for various ES device models and interfacing converter is proposed in this paper, describing how any two-port ES device model can work with any converter model.

The paper is organized as follows: Section 2 describes the converter topology and its control system, Section 3 describes the modeling principles of the ES and the converter, simulation results and analysis are given in Section 4.

## 2. 
- provide accurate control of the charging/discharging process;
- provide galvanic isolation if required.

The DC/DC converter must be bi-directional, since both charging and discharging processes are present. In this paper it is considered that the DC/DC converter is present.

### 2.4. Control system
The overview of the control system used in this paper is shown in Fig. 2. The main control system for the full-bridge MMC STATCOM in Delta configuration is taken from [23]. It employs the classical cascade structure. The active channel of the outer loop is responsible for the DC voltage control (which makes it the total energy control of the STATCOM), and the reactive channel is responsible for the AC voltage or reactive power output of the STATCOM. The outer loop generates reference signals for the inner current loop, which regulates the AC currents. The low-level control includes the calculation of the number of