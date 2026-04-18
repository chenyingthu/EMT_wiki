# Lightning-induced voltage analysis on a three-phase compact distribution line considering different line models

**Alberto De Conti**^a,*, **Osis E.S. Leal**^b,c, **Alex C. Silva**^b

^a LRC – Lightning Research Center / Department of Electrical Engineering, UFMG – Federal University of Minas Gerais, Av. Antônio Carlos, 6627, Pampulha, 31.270-901, Belo Horizonte, MG, Brazil  
^b PPGEE – Graduate Program of Electrical Engineering, UFMG – Federal University of Minas Gerais, Av. Antônio Carlos, 6627, Pampulha, 31.270-901, Belo Horizonte, MG, Brazil  
^c UTFPR – Federal University of Technology – Paraná, Via do Conhecimento, km 1, 85.503-390, Pato Branco, PR, Brazil  

\* Corresponding author.  
E-mail address: conti@cpdee.ufmg.br (A. De Conti).

**Keywords:** Lightning-induced voltages, Electromagnetic transients, Compact distribution lines, Transmission line models

**Abstract:** This paper discusses the simulation of lightning-induced voltages on a three-phase compact distribution line considering either a first order finite-difference time-domain solution of telegrapher's equations or a version of Marti's transmission line model extended to include the influence of external electromagnetic fields, named EMD model. The validity of both models is first demonstrated by means of comparisons with lightning-induced voltages measured in rocket-triggered lightning experiments. It is then shown that the EMD model can be used in the simulation of lightning-induced voltages on compact distribution lines provided special attention is given to the model fitting in the modal domain, regardless if complex or real poles are used. Results obtained with the vector fitting technique are seen to be more reliable than those obtained using Bode's asymptotic method, which must be used with caution in the modeling of compact distribution lines. The obtained results are relevant because compact distribution lines contain both bare and covered conductors, which is likely to pose difficulties to the simulation of transients with transmission line models based on modal-domain theory.

## 1. Introduction

Several countries have been using compact distribution lines to reduce faults due to contact with tree branches, reduce clearances and increase the number of circuits sharing the same pole [1,2]. Fig. 1 illustrates a 15-kV class compact distribution line used in Brazil. A polymeric spacer holds the three phase conductors, labeled A, B, and C in Fig. 1, which are covered with an insulating layer that is usually made of cross-linked polyethylene (XLPE) or high-density polyethylene (HDPE) [3–5]. The spacer is supported by a bare steel cable, known as messenger (M), which is connected to the neutral conductor (N) at every grounding point.

Compact distribution lines such as the one of Fig. 1 have been experiencing a reduced number of outages compared to conventional lines installed in the same region [6]. This can be in part explained by the relative immunity of compact lines to high-impedance faults, but also by the increase of their impulse withstand voltage due to the use of covered conductors [3–5] and the reduction of lightning-induced overvoltage levels due to the shielding effect associated with the presence of two periodically-grounded conductors [7,8].

Despite the increasing use of compact distribution lines, the number of studies dedicated to characterize their transient performance is relatively scarce [7–10]. Recently, it was investigated whether the modal-domain transmission line model proposed by Marti [11] could be used for simulating transient phenomena on compact distribution lines [12]. This was motivated by the presence of both bare and covered conductors, which changes the per-unit-length parameters such that the application of this model could become unfavorable due to the larger variation of the associated eigenvectors. Despite such concern, it was shown that Marti's model is able to perform relatively well in the simulation of switching transients in compact distribution lines provided that special attention is given to the fitting of the model parameters [12]. However, it is not clear if similar results would be obtained for other types of transient phenomena.

This paper extends the analysis presented in Ref. [12] by investigating whether Marti's model can be successfully used in the calculation of lightning-induced voltages on a three-phase compact distribution line. For such, the solution method proposed in Ref. [13] is used. To check the validity of the results, a direct phase-domain solution of telegrapher's equations based on the finite-difference time-

**Table 2**  
Conductor details.

| Conductor | Core radius (mm) | External radius (mm) | εr | DC Resistance (Ω/km) |
|---|---|---|---|---|
| A, B, C | 4.10 | 7.10 | 2.3 | 0.822 |
| M | 4.75 | 4.75 | – | 4.5239 |
| N | 3.72 | | | |