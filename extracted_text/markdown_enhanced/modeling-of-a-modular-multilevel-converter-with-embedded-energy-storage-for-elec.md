# Modeling of a Modular Multilevel Converter With Embedded Energy Storage for Electromagnetic Transient Simulations
Nuwan Herath, Student Member, IEEE, Shaahin Filizadeh, Senior Member, IEEE, and Mohammad Sedigh Toulabi, Senior Member, IEEE

**Abstract**—This paper proposes a detailed equivalent model for electromagnetic transient simulation of a modular multilevel converter with embedded battery energy storage in its submodules. The model offers an accuracy identical to that of a detailed switching model (DSM), while it markedly reduces the computational complexity of simulations. This is achieved by modeling each multivalve as a Thevenin equivalent considering the full dynamics of each constituent submodule, which results in a significant reduction in the number of switchable nodes in the converter model and hence the dimensions of the system’s admittance matrix. The paper presents the mathematical development of the model and validates it against detailed switching models through several case studies. Experimental results from a scaled-down laboratory setup are also presented for further verification.

**Index Terms**—Battery energy storage system (BESS), detailed equivalent model (DEM), electromagnetic transients (EMT) simulation, modular multilevel converter (MMC).

Manuscript received March 20, 2019; revised June 28, 2019; accepted August 22, 2019. Date of publication August 25, 2019; date of current version November 21, 2019. This work was supported in part by Natural Sciences and Engineering Research Council (NSERC) of Canada, in part by Manitoba Hydro, in part by the MITACS Accelerate Internship Program, and in part by the University of Manitoba. Paper no. TEC-00257-2019. (Corresponding author: Shaahin Filizadeh.)

N. Herath and S. Filizadeh are with the Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB R3T 5V6, Canada (e-mail: heratnmh@myumanitoba.ca; shaahin.filizadeh@umanitoba.ca).
M. S. Toulabi is with the Fiat Chrysler Automobiles (FCA) US LLC, Auburn Hills, MI 48326 USA (e-mail: toulabi@ieee.org).

## I. INTRODUCTION
Battery energy storage systems (BESS) have attracted a great deal of interest in the context of modern power systems, particularly in conjunction with the increasing penetration of renewables [1], [2]. Conventional BESS topologies comprise battery banks made with long strings of batteries, which are then connected in parallel. A DC-DC converter boosts up the battery bank voltage and maintains the common DC link voltage. Power conversion between the DC and AC sides is achieved using two- or three-level voltage source converters (VSC) [3] as shown in Fig. 1. This configuration does not provide high reliability (due to its non-modular nature) and does not readily facilitate usage of battery units that may be of different chemistries or at different stages of life-cycle. Additionally, the grid-side two- or three-level VSC exhibits high losses and harmonic contents.

**Fig. 1.** Conventional BESS.

An alternative BESS topology, based upon a modular multilevel converter (MMC) [4] is shown in Fig. 2. The converter consists of specialized sub-modules connected in series (SMs) in each converter arm (Fig. 3). Each SM consists of a small battery unit that is interfaced to the submodule capacitor using a bidirectional DC-DC converter [5]–[7]. The submodule capacitor may be inserted into or bypassed from the conduction path using the controlled switches Q3 and Q4. This topology benefits from the well-known qualities of an MMC including lower harmonics and losses, and integrates battery units for improved reliability via modularity.

**Fig. 2.** MMC structure.

**Fig. 3.** Topology of a SM with battery energy storage.

In this topology, each DC-DC converter can be used to control its SM capacitor voltage as well as the power flow to and from the SM battery [5], [6]. The work in [8] shows that dynamic power flow control can be achieved within this converter’s branches. Capabilities of an MMC with both regular SMs and SMs with energy storage are investigated in [7].

Significant hurdles exist on the way of computer simulation of an MMC with embedded energy storage using an electromagnetic transient (EMT) simulator. In EMT simulations the electrical circuit is represented as a network of admittances and current sources that represent each circuit element, and solved for node voltages at each time step. This process requires re-inversion of the network’s admittance matrix every time a switching event occurs [9]. The topological complexity and the large number of switching elements of an MMC with energy storage makes the admittance matrix large; high frequency operation of the DC-DC converters causes the admittance matrix to change very frequently. Therefore, EMT simulation of an MMC with energy storage SMs involves large admittance matrices that have to be reinverted at a high frequency, thereby causing a massive computational burden.

In this paper a detailed equivalent model (DEM) for an MMC multivalve with embedded energy storage is developed. A reference voltage waveform ($V_{\text{ref}}(t)$) with a modulation index ($m$) and a phase difference ($\delta$) relative to the point of common coupling (PCC) is generated using the outputs of a power ($P_{\text{AC}}$) and an AC voltage ($v_S$) controller as shown in Fig. 4. $P_{\text{AC,ref}}$ and $v_{S,\text{ref}}$ are the active power and AC voltage references. Direct (as shown) or decoupled controls may be used. The SMs may be inserted or bypassed within a multivalve using different techniques depending on $V_{\text{ref}}(t)$ [12]. Fig. 5 shows the firing pulse generation scheme for the multivalve using nearest level control (NLC) [13]. In Fig. 5 $I_{\text{MV}}$ is the current entering the multivalve and $\phi_{\text{PCC}}$ is the phase angle at PCC. The sorting method described in [14] is

**Fig. 4.** Direct controllers (a) AC power controller (b) AC voltage controller.

**Fig. 5.** NLC firing pulse generation.