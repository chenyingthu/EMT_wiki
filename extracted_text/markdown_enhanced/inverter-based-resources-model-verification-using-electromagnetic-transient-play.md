## Inverter-Based Resources Model Verification Using Electromagnetic Transient Playback Simulation

Haoyuan "Harry" Sun 1, 2, Qiang "Frankie" Zhang 2, Xiaochuan Luo 2, Zachary Serritella 2, David Hussey 2, Bradley Marszalkowski 2

1. Department of EECS, The University of Tennessee at Knoxville, Knoxville, Tennessee, USA
2. ISO New England, Holyoke, Massachusetts, USA

Emails: hsun19@vols.utk.edu, {qzhang, xluo, zserritella, dhussey, bmarszalkowski}@iso-ne.com

## Abstract
The rapidly increasing penetration of Inverter-Based Resources into modern power systems creates an urgent need for accurate modeling, specifically in the EMT domain. In the US, model accuracy is the Generation Owners' responsibility. However, there are movements in the wider industry to require verification of EMT models. NERC has a number of SAR projects open for MOD-26, FAC-02, MOD-32, and TPL-001 to include EMT models. IEEE P2800.2 also requires EMT models to be verified in conformance with IEEE 2800. Therefore, a general approach to benchmark IBR EMT model accuracy is needed. This paper proposes a full IBR EMT model verification solution together with two initialization techniques. Both simulated data and real Point-On-Wave data were used in the study to test the proposed approach. The results demonstrate that EMT playback is an efficient and effective model verification solution. This paper also introduces the PSCAD playback module and GUI tool that ISO New England developed.

**Index Terms**—Playback, Inverter-based resources (IBRs), model verification, electromagnetic transient (EMT) simulation, PSCAD.

## I. Introduction
Transient (EMT) models are thus leveraged for their more accurate representation of the IBR's transient behaviors. For example, the Electric Reliability Council of Texas (ERCOT) used instantaneous voltage playback as part of their EMT model-vetting tools [5] [6].

New England is in the process of integrating GWs of renewable generation into the current pool, the vast majority being IBRs. To ensure reliability, a full EMT model verification solution and necessary tools were developed to facilitate this process. We also proposed two key techniques that enable the proposed solution: an IBR model ramp-up technique and an IBR terminal bus initialization technique. To our knowledge, this is the first time such a solution has been presented and used in practice.

This paper is organized as follows: Section II introduces the playback solution and proposes two key techniques in the process. Section III introduces the PSCAD playback module and GUI tool developed at ISO-NE. Section IV presents the results from playing back simulated data and real field data. Finally, Section V concludes the paper.