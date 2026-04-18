## Lightning transient response of bifurcation structure pylon and its empirical expression with high accuracy

Kai Yin a, Mohammad Ghomi a, Hanchi Zhang a, Claus Leth Bak a, Filipe Faria da Silva a, Qian Wang a, b, *
a Department of Energy, Aalborg University, Aalborg 9220, Denmark
b School of Automation, Wuhan University of Technology, Wuhan 430070, China

* Corresponding author. E-mail address: qiw@whut.edu.cn (Q. Wang).

### Keywords
Composite pylon, Lightning protection, Bifurcation structure, Backflashover rate, Lattice diagram method

### Abstract
This paper studies the transient responses to a lightning surge terminating on towers with a bifurcation structure and presents new empirical formulas for estimating the respective lightning performance. The multi-stage segmentation is adopted for down-lead modeling, and mutual coupling and parasitic capacitance are considered. By discussing the influence degree of these factors, we propose a simplified down-lead system for formula expression. These formulas are derived from the lattice diagram method, and the original lattice diagram method recommended by CIGRE is also compared. Taking the simulation results as standard, the results derived from the proposed method show a good match with the simulation values, due to the consideration of the down-lead bifurcation configuration. The critical current ($I_c$) at the full range of front time is obtained, and the errors for the Y-shaped pylon by the new method are much less than that of the CIGRE method when the lightning front time is in the 97.5 % confidence interval. Finally, the Monte Carlo method is employed to verify the superiority of the new empirical formulas.

## 1. Introduction
The European Network of Transmission System Operators for Electricity (ENTSO-E) [1] reported an increasing demand for energy and cross-border transmission combined with multiple ways will be implemented to meet electricity demand and delivery to climate treaty [2]. For the cross-border transmission line to be built, projects place more and more emphasis on the environmental impact, not merely on electrical performance, as well as costs, which has given birth to various forms of alternative towers to traditional lattice towers. Fig. 1 shows several typically novel towers for electricity transmission [3,6]. One of those towers’ distinguishing features is that the unibody cross-arms form a bifurcation configuration to support and carry three-phase conductors replacing the suspended insulators in traditional towers [2]. This design makes pylons have a more compact pattern and smaller footprints, which means less right-of-way [7]. Furthermore, the components of the tower are easy to assemble and transport, and the construction period and cost are greatly reduced [7]. From the perspective of lightning protection, lower height and narrow width of towers will decrease the probability of being struck by lightning [8]. Therefore, these novel kinds of transmission pylons are promising candidates for the next generation of towers [4,9]. Up to now, some tower prototypes are under trial stage and construction. For example, the ‘T’ shaped pylon has been built at the UK National Grid’s training academy at Eakring, Nottinghamshire [6].

Of particular concern is that the novel pylons are different from the traditional towers in many aspects. Firstly, regarding the lightning transient model of towers, this kind of novel pylons possesses the bifurcation configuration, and the electromagnetic coupling effect between two cross-arms should be taken into consideration. Secondly, for compact composite towers such as Fig. 1 (a) and (c), when the down-lead going through cross-arms as the ground method [10], the relative spatial position of down-lead and phase conductors is very close, enlarging the stray capacitance among the conductors [11]. Thirdly, pylons with a Y-shape have inclined cross-arms and down-leads, and there is no existing model to express its surge impedance. Meanwhile, the down-leads are mainly wrapped by fiber-reinforced polymer (FRP), and silicon rubber, which further increases the complexity of the expression of the surge impedance.

## Table 1
Parameters of Y composite pylon.

| Parameter | Y pylon |
|---|---|
| Tower height $h_t$ [m] | 22.5 |
| Upper conductor (AiN) height [m] | 21.1 |
| Middle conductor (BiN) height [m] | 19.3 |
| Lower conductor (CiN) height [m] | 17.5 |
| Shielding distance [m] | 20.78 |
| Tower base radius [m] | 1.5 |
| Radius of conductors and wires $r$ [m] | 0.0175 |
| Distances between shield wire to conductor [m] | 2.8 |