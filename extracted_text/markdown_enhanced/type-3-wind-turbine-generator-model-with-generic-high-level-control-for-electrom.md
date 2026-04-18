# Type-3 wind turbine generator model with generic high-level control for electromagnetic transient simulations

Anton Stepanov $^{a,*}$, Hossein Ashourian $^{a}$, Henry Gras $^{a}$, Jean Mahseredjian $^{b}$

$^{a}$ PGSTech, Montreal, QC, Canada
$^{b}$ Polytechnique Montreal, Canada

**Keywords:** EMT simulation, DFIG, IBR, Modeling, WECC, Wind turbine

**Abstract:** Electromagnetic transient (EMT) simulations are instrumental in providing researchers and engineers with detailed data about the dynamic behavior of power grids, necessary for analysis, planning, and risk mitigation. Such simulation studies become even more relevant with the increased number of inverter-based resources integrated into the grid. To achieve reliable simulation results, accurate and accessible models are needed, since existing generic models do not always provide accurate transient response, especially during fast transients. This paper proposes a model for the type-3 wind turbine generator, otherwise known as doubly-fed induction generator (DFIG), that combines the benefits of the generic wind turbine model developed by the Western Electricity Coordinating Council (WECC), with the extra accuracy of a detailed electrical model for the DFIG. WECC models are widely used by planners in their phasor-domain model databases. The proposed WECC-DFIG model is designed to be used in EMT-type software, and due its inheritance of the high-level control system, it can reuse control settings from an existing WECC model without re-tuning. It improves accuracy during transients, such as balanced and unbalanced faults.

## 1. Introduction

A considerable proportion of existing and currently installed wind parks are based on type-3 wind turbine generators (WTGs), also called doubly-fed induction generators (DFIG) [1–4]. A typical DFIG wind turbine system is shown in Fig. 1.

Significant efforts have been made in the last decades in the development of various inverter-based resources (IBRs), including DFIG wind turbine models with various levels of detail and field of applications, including protection studies, electromagnetic transient simulations (EMT) studies, frequency domain modeling and more [5–9].

Specifically in the area of EMT simulations, various WTGs models have been proposed in the literature, focusing on different aspects, ranging from the detailed representation of mechanical systems and associated controls [10,11], numerical efficiency [12,13], to real-time modeling and WTG emulators [14,15]. Despite possible simplifications, such models typically provide a high level of detail at the expense of increased computational burden.

One of the most widely used generic models is the model developed by the Western Electricity Coordinating Council, referred to in this paper as the WECC model [16,17]. A similar generic model has been developed by the IEC [18,19]. These models are often used by electrical power system planners in phasor-domain simulations. They do not accurately represent fast transients, especially during non-nominal operating conditions, such as operation under partial load or unbalanced conditions. This is due to the fact that the mechanical, electrical and control system representations in these models are greatly simplified. The DFIG model, for example, is represented by a full converter. However, they result in faster simulations and have increased ease of use due to the reduced amount of detail, unified design, and well-developed documentation. Despite initially being proposed for phasor-domain simulations, such simplified generic models are also used in EMT simulation software packages [17,20,21].

To obtain an EMT model of their grid, it is not uncommon for transmission system operators to transpose an existing grid, which may already contain numerous generic IBR models with project-specific parameters, from an RMS simulation software to EMT. However, directly replacing such IBR models by the default detailed models from the EMT simulation software libraries can become quite challenging and time-consuming. It is due to the fact that they would often have a different control structure compared to their RMS counterparts, thus requiring re-tuning. Implementing manufacturer-specific detailed models may not be possible due to the lack of available data or confidentiality issues [9,22]. The choice is therefore often made to keep the generic IBR models in the EMT grid, which can lead to reducing the accuracy of simulation results, especially in simulation studies involving weak grids and/or unbalanced faults [9].

This paper proposes a DFIG wind turbine model that combines the interface and high-level controls of a generic model (such the WECC model), and the accurac

Fig. 1. DFIG wind turbine.
Fig. 3. GSC control system of a DFIG turbine.
Fig. 4. Mechanical control system of a DFIG turbine.