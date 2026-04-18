# Enhancements to Terminal Duality-based models for three-phase multi-limb multi-winding transformers

Meysam Ahmadi*, Ali Dehkordi, Yi Zhang  
RTDS Technologies Inc., Winnipeg, Canada

**Keywords:** Terminal Duality Method, EMT model for three-phase multi-limb multi-winding transformers, Zero-sequence impedance

**Abstract:** This paper introduces an enhanced electromagnetic transient (EMT) model for three-phase multi-limb multi-winding transformers based on the Terminal Duality Method (TDM). The proposed model improves accuracy by incorporating zero-sequence path inductances, specifically for three-limb transformers, which are formulated for the first time. A closed-form formula is developed to precisely calculate the zero-sequence path inductance, ensuring that the transformer’s open-circuit zero-sequence impedance aligns with the user-provided value. Additionally, the inductances of the yoke sections beneath the winding stacks are considered by distributing the yoke inductances across each winding. Furthermore, a stabilization technique is implemented for nonlinear inductive cutsets by introducing a reference node to represent the tank voltage. The proposed model is implemented in RSCAD-RTDS and validated through extensive simulations and comparative studies, demonstrating its effectiveness and accuracy.

I This article is part of a Special issue entitled: ‘IPST 2025’ published in Electric Power Systems Research.  
II Paper submitted to the International Conference on Power Systems Transients (IPST2025) in Guadalajara, Mexico, June 8–12, 2025.  
* Corresponding author. E-mail address: meysam.ahmadi@ametek.com (M. Ahmadi).

## 1. Introduction

The electromagnetic transient (EMT) modeling of three-phase transformers is a cornerstone of power system analysis, providing insights into critical phenomena such as inrush currents, short circuits, and harmonic generation [1–5]. Among the diverse methodologies available for transformer modeling, the Terminal Duality Method (TDM) has gained prominence due to its ability to construct equivalent circuit models with high accuracy and computational efficiency [6–9]. This approach effectively translates the magnetic behavior of the transformer core into an equivalent electrical circuit by leveraging the principles of duality, which captures the fundamental relationships between magnetic flux, reluctance, and winding currents [6].

Transformer modeling remains complex, especially for multi-limb transformers, due to intricate core-limb interactions. TDM simplifies this by relying on manufacturer-provided parameters – such as magnetizing characteristics, core aspect ratios, and test data – rather than core dimensions or material properties. The incorporation of the Normalized Core Concept (NCC) further enhances TDM by improving core-limb interaction modeling and capturing nonlinearities like saturation and hysteresis [6,10–12].

Accurate zero-sequence impedance representation is critical for three-limb transformers, widely used in distributed generation (DG) interconnections due to cost-effectiveness [4]. Their core structure results in significantly different zero-sequence impedance compared to five-limb or shell-type transformers. Ignoring this can lead to inaccuracies in fault analysis and unbalanced operating conditions, compromising EMT simulations.

Prior works, such as [6], acknowledge that existing three-limb TDM models cannot handle unbalanced voltage applications. This highlights the need for models incorporating zero-sequence path inductances to fully capture transformer behavior under unbalanced conditions.

This paper presents an enhanced TDM-based model for multi-limb transformers, including zero-sequence path inductances with a closed-form calculation, allowing users to specify arbitrary zero-sequence impedance values. This improvement enhances applicability to real-world unbalanced conditions. Additionally, the yoke inductance can be distributed based on the winding stack-to-yoke length ratio.

Another enhancement corrects an error in the phase connections of the [6] model from the PSCAD library. To mitigate numerical chatter from nonlinear inductive cutsets, the tank node voltage is designated as the reference point.

The proposed model is implemented in RSCAD-RTDS and validated through cross-EMT verification against a similar PSCAD model. The validation includes open-circuit, short-circuit, excitation, inrush current studies, and an open-phase case scenario. However, experimental validation is left for future work.

This paper is organized as follows: Section 2 covers the normalized core concept. Section 3 derives the electric dual for multi-limb transformers, focusing on zero-sequence paths and numerical chatter mitigation. Section 4 presents validation results, and Section 5 concludes.

where in (7), $\delta = (3K_r^2 + 6K_r + 4)K_{ro}^2 + (6K + 8)K + 4$. The yoke and outer limb reactances of 3-limb, 4-limb, and 5-limb transformers can be obtained from $X_{lmb}$ using (3) and (4).

It should be mentioned that this work introduces the concept of distributed yoke inductances, which will be discussed in subsequent