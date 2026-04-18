# Development of high frequency (Supraharmonic) models of small-scale (< 5 kW), single-phase, grid-tied PV inverters based on laboratory experiments

Dilini Darmawardana$^{a,*}$, Sarath Perera$^{a}$, Jan Meyer$^{b}$, Duane Robinson$^{a}$, Upuli Jayatunga$^{c}$, Sean Elphick$^{a}$

$^{a}$ University of Wollongong, Wollongong, NSW, Australia  
$^{b}$ Technische Universitaet Dresden, Dresden, Germany  
$^{c}$ University of Moratuwa, Moratuwa, Sri Lanka  

$^{*}$ Corresponding author. E-mail addresses: dhd971@uowmail.edu.au, dilihansi.27@gmail.com (D. Darmawardana).

**Keywords:** High frequency emissions, Supraharmonics, PV inverters, High frequency models

**Abstract:** There is a growth of high frequency (HF) emissions in the range of $2\text{--}150 \text{ kHz}$ (also known as Supraharmonics) in electricity distribution networks, primarily due to the increasing number and capacity of AC grid connected equipment having power electronic interfaces. Although PV inverters are a major HF source in electricity distribution networks, PV inverter models that are suitable for HF emission studies are yet to be developed. To this end, a generic method that can be used to develop HF models of small-scale ($< 5 \text{ kW}$), grid-tied, single-phase PV inverters using a black box approach is presented in this paper. Accordingly, HF models of three PV inverters that are commonly used in domestic and commercial installations are developed assuming standard network conditions. It is shown that these HF models are capable of successfully capturing the HF performance of the selected PV inverters under a wide range of operating conditions. The outcomes of this work are expected to broaden the knowledge pertaining to the HF emissions in the frequency range considered.

## 1. Introduction

High frequency (HF) emissions (also referred to as "supraharmonics") are an emerging power quality concern in low voltage electrical distribution networks. These emissions comprise of currents/voltages in the range of $2\text{--}150 \text{ kHz}$, superimposed on the fundamental frequency waveform, originating from power electronic (PE) interfaces and power line carrier (PLC) communication systems [1,2]. Malfunction and/or reduction of lifetime of grid connected equipment, audio noise generation, resonance and disturbance to PLC communication can be identified as the most prominent consequences of HF emissions [3–7]. While HF emissions caused by PLC communication are regulated by EN 50065-1, HF emissions from PE equipment are not properly controlled by any international standards, except for CISPR 15 and CISPR 14-1 that specify the emission limits of lighting equipment and induction cookers in the range of $9\text{--}150 \text{ kHz}$ [8–10]. However, several international standardising organisations such as IEC and IEEE have identified the importance of controlling the HF emissions from PE equipment. The attention paid to HF emissions, for example, is evident from the recent release of IEC 61000-2-2:2002+A1:2017+A2:2018 standard specifying the compatibility levels in the frequency range of $2\text{--}150 \text{ kHz}$ for public low voltage networks [11]. However, inadequacy in the knowledge pertaining to the behaviour of HF sources under different network conditions remains a main challenge when standardising work is considered.

Among many HF sources, such as electric vehicle chargers and small-scale storage converters, solar photovoltaic (PV) inverters are prominent in low voltage distribution networks. Several studies have investigated the behaviour of HF emissions from small ($< 5 \text{ kW}$), grid-tied, single-phase PV inverters under different conditions [3,4,12,13]. While there are time domain models (white box models) for PV inverters developed for the low frequency range, their validity in the range $2\text{--}150 \text{ kHz}$ has not been verified to date [5]. Even for the low frequency range, developing a white box model requires in-depth knowledge of the internal circuitry and control systems which are not usually disclosed by the inverter manufacturers. Further, the process is complex and time consuming. The most essential drawback of such an approach is that a HF model developed as such is applicable only to a very specific type of PV inverters, if not a single inverter. Therefore, a black box approach is more suitable in developing models of PV inverters for HF studies. However, no such models are available in the literature to date.

In this paper, HF models of three commercially available, small-scale ($< 5 \text{ kW}$), grid-tied, single-phase PV inverters that are commonly used in domestic and commercial installations are developed using a novel method employing controlled laboratory experiments, optimisation and curve/surface fitting. The paper gives a literature review (Section 2) that is followed by an overview of the proposed models (Section 3). The step-by-step model development process (Section 4) and the proposed HF models of the three PV inverters considered (Section 5) are described together with an error analysis and a model validation (Section 6). Next, an application study using the developed HF models (Section 7) is presen

- $V_{\text{grid}}$: grid voltage
- $M$: modulation index
- $f$: grid frequency
- $t$: time
- $J_{2n-1}$: Bessel function of order $2n-1$
- $f_s$: switching frequency

In (1), the 1st term represents the desired output voltage whereas the 2nd term represents the unwanted HF components. These HF components are a consequence of the pulsed output voltage resulting from the PWM switching operation of the inverter. As can be seen in (1), HF emissions from single-phase inverters occur as groups (side-