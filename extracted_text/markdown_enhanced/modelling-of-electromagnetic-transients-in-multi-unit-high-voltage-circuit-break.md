# Modelling of electromagnetic transients in multi-unit high-voltage circuit-breakers
Antoine Mailhot a, *, Ryszard Pater a, Sébastien Poirier a, Jean Mahseredjian b, René Doche c
a Institut de recherche d’Hydro-Québec (IREQ), Varennes, Canada
b Polytechnique Montréal, Montréal, Canada
c Hydro-Québec, Montréal, Canada

**Keywords:** Circuit-breakers, Electromagnetic transients, Grading capacitors, Multi-unit, Switching transients

**Abstract:** High-voltage (HV) circuit-breakers (CBs) often consist of several making and breaking units (MBUs) in series. A multi-unit circuit-breaker EMTP® model is proposed to analyse the effects of non-simultaneity between MBUs of the same pole. The model allows for simulations of high-frequency voltage and current transients during opening or closing operations. The simulations include the non-simultaneity of MBUs of the same pole or differences in dielectric withstand characteristics for vacuum circuit-breakers (VCBs) and SF6 CBs. According to simulation results, the maximum non-simultaneity of MBUs of the same pole, as permitted per international standards, can lead to multiple re-ignitions during opening or excessive overvoltages during closing operations. These phenomena are rarely simulated with conventional CB models. The simulations also highlight the important challenges facing high-voltage VCB design due to the inherent characteristics of vacuum bottle technology. The proposed models serve as useful tools for understanding and studying the effect of multi-unit CBs in various system studies and advanced diagnostics.

## 1. Introduction
A high-voltage (HV) circuit-breaker (CB) is a mechanical switching device used in transmission grids, capable of making and breaking currents under normal and abnormal circuit conditions. Amongst other functions, the HV CB ensures the reliability of a transmission grid. CB currents can be normal load currents, capacitive or inductive currents or short-circuit currents. The main functions of a HV circuit-breaker are as follows:
- Connect or isolate parts of the electrical grid by making or breaking load currents [1]
- In the open position, maintain excellent insulating properties to ensure dielectric strength [1]
- In the closed position, maintain excellent conductive properties, with a contact resistance of the order of a few tens of microohms, to avoid heat loss or damage [1]
- Interrupt a short-circuit current, as per the rated characteristics of the device (ranging from 40 kA to 80 kA, depending on the case [2])
- Establish a short-circuit current according to the rated characteristics of the device [2]

Many HV CB technologies exist, such as oil, air, sulphur hexafluoride (SF6) and vacuum circuit-breakers (VCB). The last two categories are the most common today. The VCBs are mainly applied for voltages below 145 kV, but efforts are being made to apply this technology to higher voltages. Moreover, recent research has focused on alternative media to replace SF6, the most prominent greenhouse gas (GHG) [3].

HV CBs above 245 kV are often composed of several making and breaking units (MBUs) in series per pole. The term MBU is defined in IEC 62271-100 [2]. MBUs are also called “interrupter units.” The grading capacitors installed in parallel with MBUs allow the uniform voltage distribution between the units [4].

In the Electromagnetic Transients Program (EMTP®), the basic model of a CB is an ideal switch that makes the current instantaneously and breaks it at a zero crossing [5]. A more complete model of CB is available, which integrates the transient recovery voltage (TRV) envelope [6].

Mayr and Avdonin arc models are available in EMTP® [7-9]. However, Mayr and Avdonin electric arc models require a considerable number of parameters to accurately simulate current quenching. These non-linear models of the arc necessitate precise and challenging determination of physical parameters to simulate various dielectric media such as oil, air, SF6, vacuum, and alternative gases as well as different contact geometries. Avdonin and Mayr models are not usually used in CB operation analysis and simulation.

Electromagnetic phenomena occurring during CB operation, such as prestrike, restrike or re-ignition, involve interactions between different MBUs. Reference [10] details a CB diagnostic method using the measurement of transient electromagnetic emissions (TEEs) occurring during CB operation. This diagnostic tool, which is particularly useful for multiple MBU (multi-unit) CBs, allows the detection of prestrikes, restrikes or re-ignitions in individual units. As an example, multiple prestrikes in one MBU during a closing operation of an SF6 CB were observed [11].

The work in [12] studied the effects of very fast transient phenomena including lightning impulse on an assembly of several pairs of contacts in series, showing the complexity of such a system. Their conclusion underlines the challenges related to the multi-contact breakdown voltage modelling, depending on the streamer integral, volume-time criteria and precise modelling of contact geometry.

In this manuscript, we propose novel multi-unit electromagnetic transient (EMT) simulation models that integrate both thermal and does not address the impact for CBs with multiple units. The authors of

*Fig. 1. Voltage transients caused by mechanical non-simultaneity in CB with two MBUs.*