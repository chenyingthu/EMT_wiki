## Expanding the measuring range via S-parameters in a EHV voltage transformer modelling for reliable GIS VFT simulations
Gustavo H.C. Oliveira *, Lucas P.R.K. Ihlenfeld, Lucas F.M. Rodrigues, Angélica C.O. Rocha, Diogo J.D.E. Santo
a Department of Electrical Engineering, Federal University of Paraná (UFPR), Brazil
b ATG, Brazil
c Jirau Energia, Brazil

## Abstract
The customary approach to modelling voltage transformers (VT) at gas insulate substations (GIS) subject to Very Fast Transients Overvoltages (VFTOs) consists of using a capacitive element. However, this simplistic approach is unable to reproduce characteristic resonances and predict how transients propagate to the VT’s secondary winding. Multiport black-box passive rational models built upon frequency-domain measurements are instrumental to overcome these challenges. The adoption of S-Parameters is an alternative to black-box approaches based on Y-Parameters so as to consistently expand the measurement frequency range which is required to accurately capture the dynamics involved in VFTO phenomena up to 50 MHz at GIS facilities. We validate our results using an strategy that entails measuring, modeling and simulation upon a multiport extra-high voltage (EHV) VT. The proposed approach using S-Parameters leads to increased accuracy compared with the customary approaches using Y-Parameters or capacitive elements.
We build two models estimated upon distinct frequency ranges to highlight the importance of extending the measurements into the MHz range so that time-domain simulations better reproduce VFTO characteristics. The black-box VT model thus obtained is incorporated into an actual 500 kV GIS model for transient simulations enabling the analysis of transient propagation between primary and secondary windings.

## Keywords
Extra high voltage equipment, Frequency-domain measurement, Gas insulated substation, Rational models, S-parameters, Very fast transient overvoltages, Voltage transformer

## 1. Introduction
Gas-insulated substations (GIS) have grown in number around the globe in the last decades owing to several advantages over the traditional air-insulated counter-part, these advantages include smaller space requirements, higher safety levels, simpler maintenance and commissioning, et cetera. The growing number of both planned and operational GIS brings such issues to the forefront of research on power systems. Conversely, GIS are more susceptible to Very Fast Transient Overvoltages (VFTO), as a consequence of its intrinsic physical properties [1–3].

As demonstrated in the literature, GIS are prone to VFTO during disconnector or circuit-breaker operations, see [1,2,4–8]. Essentially, several restrikes appear as a circuit-breaker operates in switching action to either establish or interrupt the current flow. These high frequency strikes constitute the root cause of VFTO at GIS.

In essence, VFTO are electromagnetic transients characterized by signals with very short rise times (1 to 50 MHz) and tail with lower (30 to 300 kHz) frequency content [1,9]. Classification for transients in electric power systems [9] prescribes the VFTO frequency range from 100 kHz to 50 MHz, and associate it with transients originating from disconnector switching and faults at GIS. As they propagate through the GIS, these transients can damage high-voltage equipment [10,11]. As far as Instrument Transformers are concerned, according to the standard [12], immunity tests are recommended whenever frequency components beyond 1 MHz exist so that their impact on control circuits be properly assessed.

Reliable VFTO simulations at GIS require therefore models endowed with wide-band capabilities. In transient simulations, Voltage Transformers are traditionally described as a simple one-port capacitive element [1,9] which is a simplistic description incapable of reproducing all resonances that fully characterize the actual equipment.

On the other hand, multiport black-box rational models extracted over a wide frequency band [13–18], come as an appropriate alternative to improve the modelling process in so long as the system’s dynamic behaviour as well as its interaction with surrounding substation be accurately modelled for transient overvoltages simulations.

Besides, it is also known that the transformer ratio is frequency-dependent. Therefore, this dynamics can be understood and correctly simulated provided a reliable wide-band model be available. Still comparing with a single one-port capacitive model for VTs, the ability to describe transient overvoltages in both transformer windings requires a multiport approach, thus permitting the analysis of the impact overvoltages have on circuit protection/control and its associated digital apparatus. Some accounts in the literature suggest that control better reproduce VFTO characteristics.

The second gap is addressed by incorporating the estimated multiport EHV VT model into an actual 500 kV GIS model for transient simulations so that the transient propagation from primary to secondary is accounted for and both can be simulated and analyzed. This transient propagation from one winding to another cannot be accounted for using the traditional capacitive model.

The paper is structured into 6 Sections. This introductory Section 2 sets out the notation whereas Section 3 introduces the proposed methodology that is applied to an actual EHV-VT equipment in Section 3.1. In