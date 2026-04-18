# Evaluation of the impact of different frequency dependent soil models on lightning overvoltages

Marco Aurélio O. Schroeder $^{a,*}$, Maria Teresa Correia de Barros $^{b}$, Antonio C.S. Lima $^{c}$, Márcio M. Afonso $^{d}$, Rodolfo A.R. Moura $^{a,c}$

$^{a}$ Universidade Federal de São João del-Rei, UFSJ, São João del-Rei, Brazil
$^{b}$ Instituto Superior Técnico, Universidade de Lisboa, Portugal
$^{c}$ Universidade Federal do Rio de Janeiro, COPPE/UFRJ, Rio de Janeiro, Brazil
$^{d}$ Centro Federal de Educação Tecnológica de Minas Gerais, CEFET-MG, Belo Horizonte, Brazil

**Article Info**
Received 15 February 2017
Received in revised form 22 August 2017
Accepted 17 September 2017
Available online 23 October 2017

**Abstract**
This work assesses the inﬂuence of including the wideband behaviour of grounding systems in EMT-type programs on evaluation of transients resulting from direct lightning strikes to transmission lines. The grounding frequency behaviour is determined by using an accurate electromagnetic model and included in EMTP/ATP by means of an equivalent circuit derived from Vector Fitting technique. Furthermore, the impact of the frequency dependence of soil parameters on the lightning performance of transmission lines is addressed. It was found that representing the tower-footing grounding by a simple resistance can lead to signiﬁcant errors in terms of grounding potential rise. However, for the overvoltages that appear across the insulator strings, the representation of the grounding system by a simple resistance leads to results whose accuracy is similar to those obtained using more complex representations which consider the wideband behaviour. Also, it was shown that the frequency dependence of soil parameters leads to a reduction of the grounding impulse impedance and causes a decrease of the backﬂashover rates, improving the lightning performance of transmission lines. In addition, the effect of considering the variation of soil parameters with frequency is more intense in the ground potential rise than in the overvoltages in the insulator strings.

**Keywords:**
Lightning performance of transmission lines
Wideband modeling of grounding
EMT-type programs
Frequency dependence of soil parameters

## 1. Introduction

Direct lightning strikes are a frequent cause of transmission line outages. As well detailed in Ref. [1], when a stroke hits a tower, a portion of the current travels down the tower and the remainder portion goes through the shield wires. The tower current ﬂows to earth at the tower base through the grounding system. The resultant voltage wave reﬂected back up to the tower top depends directly on the value of the footing impedance encountered by the current. A sufﬁciently high voltage may stress the insulator strings and result in backﬂashover. According to Ref. [1]: “Since the tower voltage is highly dependent on the footing impedance, it follows that footing impedance is an extremely important factor in determining lightning performance”.

The overvoltages on transmission lines yielded by direct lightning strikes are usually computed by using simpliﬁed analytical approaches or by simulations using full electromagnetic models or EMT-type programs [1–9]. The use of simpliﬁed analytical approaches should be avoided, since they consider certain assumptions that could lead to errors in estimating the lightning performance of transmission lines. The use of full electromagnetic models, although they provide the most accurate results, has the drawback of being very computational time consuming. On the other hand, the widespread EMT-type programs have several models of the electrical system components that allow in most cases a sufﬁcient accurate analysis of the lightning overvoltages propagation along transmission lines. However, EMT-type programs usually do not have accurate models to represent the lightning response of grounding, including its wideband behaviour.

As already mentioned, the grounding system is an extremely important component in determining lightning performance of transmission lines [10]. Nevertheless, in most evaluations considering simpliﬁed approaches or EMT-type programs, the grounding is represented by a simple resistance [1–6,11–13]. Such representation disregards some effects that arise when the grounding is subjected to lightning currents, for instance, capacitive and inductive effects along with propagation phenomena [11,14]. Also, even when more elaborate models are used for grounding representation, the frequency depende

**Table 1**
Coefﬁcient $a_n$ for the universal soil model [21]—see Eqs. (5) and (6).

| N | $a_n$ | N | $a_n$ | N | $a_n$ |
|---|---|---|---|---|---|
| 1 | $3,4 \times 10^6$ | 6 | $1,33 \times 10^2$ | 11 | $9,8 \times 10^{-1}$ |
| 2 | $2,74 \times 10^5$ | 7 | $2,72 \times 10^1$ | 12 | $3,92 \times 10^{-1}$ |
| 3 | $2,58 \times 10^4$ | 8 | $1,25 \times 10^1$ | 13 | $1,73 \times 10^{-1}$ |

$^{*}$ Corresponding author.
E-mail addresses: schroeder@ufsj.edu.br (M.A.O. Schroeder), teresa.correiadebarros@tecnico.ulisboa.pt (M.T.C. de Barros), acsl@dee.ufrj.br (A.C.S. Lima), marciomatias@des.cefetmg.br (M.M. Afonso), moura@ufsj.edu.br (R.A.R. Moura).