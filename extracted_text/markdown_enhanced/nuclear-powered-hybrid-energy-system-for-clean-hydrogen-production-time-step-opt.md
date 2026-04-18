This article has been accepted for publication in IEEE Transactions on Energy Conversion. This is the author's version which has not been fully edited and content may change prior to final publication. Citation information: DOI 10.1109/TEC.2026.3658726

## Nuclear-Powered Hybrid Energy System for Clean Hydrogen Production: Time-Step-Optimized Real-Time Multi-Domain Hardware Emulation
**Weiran Chen**, Member, IEEE, **Xinyu Zhao**, Student Member, IEEE, and **Venkata Dinavahi**, Fellow, IEEE.

### Abstract
Increasing global emphasis on decarbonization and the proliferation of renewable energy, energy storage, and nuclear power is driving a surge of research interest into integrated sustainable energy modeling, simulation, operation and control. Traditional electromagnetic transient (EMT) methods typically discretize electrical networks using the trapezoidal rule. When coupled with the ordinary differential equations (ODEs) of other physical domains, however, the absolute stability region of the numerical integration scheme can shift, and discrepancies in time constants across subsystems further complicate integration of disparate models. While the demand for integrating EMT with multi-domain co-simulations is increasing, existing commercial EMT simulation tools either lack support for multi-domain physical coupling or are not specifically optimized for such hybrid simulations. To address this gap, this paper proposes a robust multiscale time-step estimation (RMTE) framework that enables real-time co-simulation of EMT networks and multi-domain subsystems. The framework includes a fast, efficient, and adaptive approach for selecting the optimal maximum time-step across heterogeneous physical domains. The proposed method is validated through a case study involving small modular reactors (SMRs), wind farm, photovoltaics (PV) and low-temperature proton exchange membrane (PEM) electrolysis for clean hydrogen production. Real-time hardware co-emulation is achieved on a field-programmable gate array (FPGA)-based platform. The results demonstrate significant improvements in simulation efficiency and execution time.

### Index Terms
Clean hydrogen, electromagnetic transients (EMT), field-programmable gate array (FPGA), hardware emulation, low-temperature electrolysis (LTE), multi-domain co-simulation, nuclear-renewable hybrid energy systems (N-RHES), photovoltaics (PV), proton exchange membrane (PEM), real-time systems, small modular reactor (SMR), wind farm.

### Nomenclature
| Symbol | Description |
| :--- | :--- |
| $A_E$ | Electrolyzer active area ($\text{cm}^2$). |
| $a_{H_2O}$ | Water activity. |
| $C$ | Constant. |
| $C_{wa}, C_{wc}$ | Water concentration in anode/cathode ($\text{mol/cm}^3$). |
| $C_i(t)$ | Delayed neutron density ($1/\text{cm}^3$). |
| $D_\omega$ | Water diffusion coefficient ($\text{cm}^2/\text{s}$). |
| $E$ | Open-circuit voltage (V). |
| $E_0$ | Standard electromotive force (V). |
| $F$ | Faraday constant (C/mol). |
| $F_{H_2,ci}, F_{H_2,co}$ | Cathode inlet/outlet hydrogen flow rate (mol/s). |
| $F_{H_2O,ai}, F_{H_2O,ao}$ | Anode inlet/outlet water flow rate (mol/s). |
| $F_{H_2O,ci}, F_{H_2O,co}$ | Cathode inlet/outlet water flow rate (mol/s). |
| $F_{H_2O,d}$ | Diffusive water molar flow rate (mol/s). |
| $F_{H_2O,eod}$ | Electro-osmotic water flux (mol/s). |
| $F_{O_2,ai}, F_{O_2,ao}$ | Anode oxygen flow rate (mol/s). |
| $F_{ia}, F_{ic}$ | Water vapor activity at anode/cathode. |
| $H_{2g}, O_{2g}$ | Cathode hydrogen/oxygen gas flow rate (mol/s). |
| $I_{in}$ | Input current (A). |
| $I_{loss}$ | Energy loss (W). |
| $i$ | Current density ($\text{A/cm}^2$). |
| $i_0$ | Exchange current density ($\text{A/cm}^2$). |
| $k_{ao}, k_{co}$ | Flow coefficients for anode/cathode pipes. |
| $M_{H_2O}$ | Molar mass of water (g/mol). |
| $M_{m,dry}$ | Molar mass of dry membrane (g/mol). |
| $M_{H_2}$ | Molar mass of hydrogen gas (g/mol). |
| $n$ | Number of cells. |
| $n(t)$ | Prompt neutron density ($1/\text{cm}^3$). |
| $n_d$ | Electro-osmotic drag coefficient. |
| $N_{H_2}$ | Net hydrogen production rate (mol/s). |
| $N_{H_2O,a}, N_{H_2O,c}$ | Net water change rate (mol/s). |
| $N_{O_2}$ | Net oxygen production rate (mol/s). |
| $P_a, P_c$ | Channel pressures (Pa). |
| $P_{ao}, P_{co}$ | Outlet pressures (Pa). |
| $P_{H_2}, P_{O_2}$ | Partial pressures (Pa). |
| $P_{H_2O,a}$ | Water partial pressure at anode (Pa). |
| $P_b$ | Hydrogen tank pressure (Pa). |
| $P_{bi}$ | Initial hydrogen tank pressure (Pa). |
| $R$ | Ideal gas constant (J/mol$\cdot$K). |
| $R_{el.ohm}$ | Membrane resistance ($\Omega\cdot\text{cm}^2$). |
| $T_{el}$ | Electrolyzer temperature (K). |
| $T_b$ | Hydrogen tank temperature (K). |
| $t_m$ | Membrane thickness (cm). |
| $V_a, V_c$ | Channel volumes ($\text{cm}^3$). |
| $V_h$ | Hydrogen tank volume (L). |
| $V_{el}$ | Electrolysis voltage (V). |
| $V_{el.act}$ | Activation overpotential (V). |
| $V_{el.ohm}$ | Ohmic overpotential (V). |

This work was supported in part by the Alberta Innovates, Mitacs, and Natural Science and Engineering Research Council of Canada (NSERC). (Corresponding author: Weiran Chen.) W. Chen, X. Zhao, and V. Dinavahi are