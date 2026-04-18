University of Manitoba Department of Electrical & Computer Engineering

# Modeling of LCC-HVDC Systems Using Dynamic Phasors

Mehdi Daryabak, Student Member, IEEE

Dept. Electrical & Computer Engineering

University of Manitoba

umdaryab@cc.umanitoba.ca

High‐voltage direct current (HVDC) transmission systems play an important role in modern power networks. HVDC is considered to be a suitable option for such applications as transmission via underground/submarine cables, linking ac systems with unequal frequencies, integration of energy sources such as hydropower, and long‐ distance transmission. Although a new breed of HVDC systems using voltage‐source converters (VSC) is also developed, the majority of existing HVDC systems are based on the conventional line‐commutated converters (LCC). LCC‐HVDC schemes offer the benefits of a mature technology and are available in much larger ratings than the currently available VSC‐HVDC systems.

Electromagnetic transient (EMT) simulation programs, in which high‐fidelity models of transmission systems and power electronic converters are available, have been extensively used for analysis and design of HVDC schemes. Despite its accuracy in representing the fast switching dynamics of converters, an EMT simulator may indeed be excessively detailed for the study of interconnected networks with embedded HVDC, particularly when low‐ frequency dynamics of the network are of interest. For such cases simulation of the switching transients, which are often small in magnitude, adds unnecessary computational complexity. Dynamic average modeling aims to develop low‐intensity models that represent the slow dynamics of power‐electronic based systems by neglecting the switching transients.

This research presents an average‐value model for an LCC‐HVDC system using dynamic phasors. Dynamic phasors use the quasi‐periodic switching nature of a power electronic converter, for which voltages and currents can be represented using time‐varying Fourier coefficients. Dynamic phasor modeling retains the low‐frequency dynamic characteristics of a power system without having to model the high‐frequency transients caused by the operation of power‐electronic switches and converters. Additionally, a dynamic phasor model can be easily augmented to account for harmonic components, if so needed.

Dynamic phasors have been successfully used in modeling and analysis of electrical machines, power system dynamics and faults, FACTS devices, sub‐synchronous resonance (SSR), dc‐dc converters, multi‐converter dc systems, and multi‐converter ac systems. Special studies including real‐time and repetitive simulations can benefit from the reduction in computational intensity offered by dynamic phasor modeling. This research extends the use of dynamic phasors to modeling of large‐excursion transients of LCC‐HVDC systems, caused by control actions or faults. The reduced simulation intensity of the model resulting from its neglecting switching transients makes it particularly useful in the study of large‐signal, low‐frequency transients, or in repetitive simulations when time saving over EMT simulations become significant.

ADVISOR: Dr. Shaahin Filizadeh