## Frequency-dependent multiconductor line model based on the Bergeron method
Pablo Torrez Caballero $^a$, Eduardo C. Marques Costa $^b$, Sérgio Kurokawa $^{a,*}$
$^a$ Universidade Estadual Paulista—UNESP, Faculdade de Engenharia de Ilha Solteira—FEIS, Departamento de Engenharia Elétrica, Ilha Solteira, SP, Brazil
$^b$ Universidade de São Paulo—USP, Escola Politécnica, Departamento de Engenharia de Energia e Automação Elétricas—PEA, São Paulo, SP, Brazil

* Corresponding author. Tel.:+55 1130915152.
E-mail addresses: pablotorrezcaballero@gmail.com (P.T. Caballero), educosta@pea.usp.com (E.C.M. Costa), kurokawa@dee.feis.unesp.br (S. Kurokawa).

**Article history:**
Received 5 March 2015
Received in revised form 16 May 2015
Accepted 23 May 2015
Available online 27 June 2015

**Keywords:**
Electromagnetic transients
Transmission line modeling
Vector fitting
Time-domain analysis

**Abstract**
A new multiconductor transmission line model is proposed based on the method of characteristics. The conventional Bergeron model is characterized by the line representation using constant lumped parameters. The novel content of this paper is the inclusion of the frequency effect in the longitudinal parameters by fitting techniques and three-phase representation of the Bergeron line model. This new feature enables to extend the application of the Bergeron method for simulation of electromagnetic transient in three-phase systems, considering fast and impulsive transients composed of a wide range of frequencies.

## 1. Introduction
The method of the characteristics, or Bergeron method, was initially applied to solve hydraulic systems and after for electrical problems in electromagnetic propagation through a lossless wave guide [1]. At the same time, end of the 1960s and beginning of the 1970s, two important researches on transmission line modeling—TLM were published. The first work was published by A. Budner, which described a two-phase transmission line modeled by a two-port circuit in the frequency-domain. The time-domain currents and voltages at the sending and receiving ends of the two-phase line were calculated using inverse transforms and convolutions [2]. The second important research described the inclusion of the line losses in the Bergeron model using lumped resistances in the equivalent line circuit [3]. The main difference of the two methods is that the Budner’s model is based on the representation of the distributed characteristics of the line parameters in the frequency domain whereas the Bergeron line model is a time-domain representation based on lumped circuits without inverse transforms and convolutions. Surely that at the same time there were other important contemporary studies, such as the papers published by H. W. Dommel on the Electromagnetic Transient Program (EMTP) [4]. However, the two prior references are more important specifically for the line model proposed in this research.

An effective evolution in TLM was verified in the 1980s with the great improvement of the computational resources and processing power [5,6]. The well-established line model of J. Marti, available in various programs derived from the EMTP, was published in 1982 [7]. This paper introduced in the technical literature on TLM the concept of synthesis of the line parameters, i.e., the frequency-dependent characteristic impedance of the line was represented in the time domain as an equivalent circuit composed of resistances and capacitances. Thus, the inverse transforms and convolution used in the first frequency-dependent line models were not more necessary for time-domain transient simulations [2]. At the same period, the Bergeron line model with losses was integrated to tool boxes of power systems available in several simulation programs derived from the EMTP [6].

In the 1990s, important researches were published improving the multiconductor representation of transmission lines and new methods for inclusion of the frequency effect in the line parameters, directly in the time domain, were also included in the TLM literature. The multiphase representation of transmission lines was carried out using modal decoupling, i.e., each phase of a transmission line was decoupled as an independent propagation mode [8]. Thus, there are no mutual parameters in the modal domain and each propagation mode can be considered as a single-phase transmission line. At the same period, fitting techniques were proposed to include the frequency effect on the line longitudinal parameters directly in the time domain. The premise of the technique

**Fig. 1.** Bergeron circuit considering the line losses.

**Fig. 2.** Time-domain fitting of the line longitudinal parameters.

The characteristic impedance $Z_0$ and the propagation time $\tau$, from the sending end to the receiving end of the line, are constant and expressed as:
$$Z_0 = \sqrt{\frac{L'}{C'}}; \quad \tau = \frac{l}{v} = l\sqrt{L'C'}$$