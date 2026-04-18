# Dynamic Performance of Embedded HVDC with Frequency Control Strategy
**Jicheng Yu**, Student Member, IEEE  
**Mengjia Xiao**, Student Member, IEEE  
School of Electrical, Computer and Energy Engineering, Arizona State University, Tempe, Arizona, USA  
jichengy@asu.edu  
**George G. Karady**, Life Fellow, IEEE  
School of Electrical, Computer and Energy Engineering, Arizona State University, Tempe, Arizona, USA  

**Abstract**—An embedded HVDC system is a HVDC link connected in parallel with an AC transmission line or a mashed AC system. This paper proposes a control strategy cooperating with conventional $d-q$ vector control for embedded HVDC system. The novel control method employs frequency features at two terminal stations to eliminate power oscillation. Dynamic simulation models are constructed in PSCAD platform to compare the transient stability of the proposed strategy with the conventional $d-q$ vector control. According to the simulation results, the average Critical Clearing Time after contingencies is improved by 22.93% when equipped with the proposed frequency control method.

**Index Terms**—Embedded HVDC; VSC-HVDC; dynamic performance; transient stability; power oscillation

## I. INTRODUCTION
Since the growing challenges in AC network development, the demand for a more reliable and affordable power delivery drives an increasing construction of HVDC links within the AC system [1]. The HVDC transmission system has many advantages, such as a high efficiency in long distance, bulk-power transmission, a reliable asynchronous connection and practices in submarine cable crossings [2]. The applications of HVDC transmission system can be categorized in three aspects according to how a HVDC integrates within a power system; HVDC interconnection, HVDC segmentation and embedded HVDC system [3].

The HVDC interconnection refers to a HVDC link which connects two isolated AC networks [4]. The HVDC segmentation is applied to decompose a large AC network into several small segments, where the HVDC links are responsible for the power transmission among the segments [3]. The embedded HVDC system is first defined by the International Council on Large Electric Systems (CIGRÉ): “an embedded HVDC system is a DC link with at least two ends being physically connected within a single synchronous AC network.” [5]

The basic configuration of the embedded HVDC system is depicted in Fig 1. In the diagram, the AC power system 1, AC power system 2 and the AC interconnection can be considered as a single synchronous AC network. The AC interconnection can either be a long transmission line or a meshed AC power system, which is an equivalent AC network that may consist of generators, lines and loads. Between the two AC power systems in the diagram, a VSC-HVDC is constructed in parallel with the AC interconnection. Compared to conventional HVDC system, the connection method of embedded HVDC between the two AC systems is paralleled AC and HVDC transmission, rather than HVDC transmission alone.

The embedded HVDC system employs the VSC-HVDC techniques. The VSC stands for voltage source convertors, which utilize transistors, such as IGBT and GTO as switching valves [2]. Compared with the last generation HVDC, which is a thyristor valves and line-commutated convertor based technology, the VSC-HVDC system is able to reduce harmonics, to eliminate requirements of reactive power and to control the power flow [6].

**Fig. 1.** The basic topology of embedded HVDC system paralleling with an equivalent AC interconnection.

Instead of analyzing the internal properties of HVDC transmission systems, the authors of [7] compared the embedded HVDC system with pure AC and pure DC links by using Simplified Southern and Eastern Australian Power System, in which the voltage stability and transient stability are tested. According to the results from [7], the embedded HVDC link exerts worst voltage stability among three cases. Reference [8] has similar results that embedded HVDC link is weak in voltage stability due to the weak tie-line in the network. However, the simulations in [8] also illustrate that the transient stability can be improved when the embedded HVDC link is applied.

Both HVDC systems studied in [7] and [8] perform as interconnections which are applied with conventional $d-q$ vector controls. Unlike operating as a HVDC interconnection, in the embedded HVDC system, the frequencies on all DC terminals are synchronous since the HVDC works within the same AC network.

In this paper, a frequency control strategy is introduced in the embedded HVDC system, cooperating with the conventional $d-q$ vector control. The theoretical study and operational mechanism of conventional $d-q$ vector control and frequency control are explained in Part II. In Part III. Dynamic models of VSC-HVDC embedded in IEEE 4-machine, 6-bus power system are constructed in PSCAD program. Two scenarios are categorized according to the VSC control strategy. In Scenario I, the conventional $d-q$ vector control method is applied on the system model, and in Scenario II, the system is modelled with the $d-q$ vector control with the proposed frequency control strategy. Under each scenario, the system dynamic performance, including dynamic stability and power oscillation attenuation, is simulated in PSCAD. In the respect of dynamic stability, the Critical Clearing Time (CCT) is calculated

### B. Optimal Control of Embedded VSC-HVDC in AC network
In the embedded HVDC, since the AC interconnection line connects the two terminal buses, the frequency of the power going into the rectifier and that out of the inverter have the same frequency. By using this equal frequency condition, a frequency control method is proposed for the embedded VSC-HVDC system.

In Fig. 2, as the VSC-HVDC link operates in parallel with a long AC transmission line or network, the total active power leaving Bus2, denoted as $P_{\text{Bus 2}}$, is the sum of the active power transmitted on AC and DC links.
$$P_{\text{Bus 2}} = P_{\text{dc 2}} + P_{\text{ac 12}} \tag{1}$$
where $P_{\text{dc 2}}$ and $P_{\text{ac 12}}$ represent the power flowing out of the