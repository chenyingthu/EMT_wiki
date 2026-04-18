# Co-simulation of electrical networks by interfacing EMT and dynamic-phasor simulators

K. Mudunkotuwa$^a$, S. Filizadeh$^{b,*}$

$^a$ Electranix Corp., Winnipeg, MB R3Y 1P6, Canada  
$^b$ Department of Electrical and Computer Engineering, University of Manitoba, Winnipeg, MB, R3T 5V6, Canada

**Abstract**  
The paper presents a hybrid co-simulator comprising EMT and dynamic phasor-based simulators. The EMT simulator models portion(s) of the network wherein fast transients are prevalent and detailed modeling is necessary. The dynamic phasor solver models the rest of the network using extended-frequency Fourier components. Specialized algorithms are developed and presented to accurately map instantaneous EMT and counterpart dynamic phasor samples. Interfacing requirements for co-simulation using different time-steps in the two solvers are also discussed along with implications on accuracy and numerical stability. The paper demonstrates the developed co-simulation algorithm using an example of the IEEE three-phase 118-bus network in which a wind farm is included. The wind farm and the network in its vicinity are modeled in the PSCAD/EMTDC electromagnetic transient simulator, and are interfaced to the rest of the system modeled in a dynamic phasor-based solver. The paper demonstrates the accuracy of the proposed co-simulation for a range of time-step ratios of the two solvers, and also reports the substantial computational time savings obtained using the hybrid simulator.

**Keywords:** Co-simulation, Electromagnetic transient simulation, Dynamic phasors, Interfacing

☆ This manuscript is a significantly extended version of a conference paper presented at IPST 2017.  
☆☆ This work was supported in part by the University of Manitoba, and in part by the Natural Sciences and Engineering Research Council (NSERC) of Canada.  
* Corresponding author. E-mail addresses: km@electranix.com (K. Mudunkotuwa), shaahin.filizadeh@umanitoba.ca (S. Filizadeh).

## 1. Introduction

Electromagnetic transient (EMT) simulation of large electrical networks is a challenging task due to the inherent computational intensity of EMT models and solution methods. EMT simulation of fast transients, e.g., switching events of high-power electronic converters, is particularly cumbersome as it needs small simulation time-steps to accurately capture high-frequency components. This leads to large computational burden. In a conventional EMT simulator the entire network is simulated with a small time-step, even though fast transients may only be confined to small portions where faults occur or fast-acting systems such as power-electronic converters exist. This limitation has led to the use of EMT solvers primarily for studies of moderately small networks. With the proliferation of switching converters in modern power systems, it is increasingly necessary to use EMT simulations for larger systems to the extent that the required computational resources have nearly always outpaced the computing power of contemporary computers.

Several methods have been proposed to extend the applicability of EMT simulators in the study of large and complex power systems. Simplifications to individual component models and systems, which is widely applied to high-frequency power electronic converters and is referred to as averaging, is one such method [1,2,3]. Alternatively, dynamic equivalents represent a portion of a large network by aggregating several components in a reduced-order model to relieve the computational intensity of simulation of the whole network [4–6]. Dynamic equivalents often yield substantial reduction in the number of nodes to be included in the system’s equivalent admittance matrix, which in turn relieves matrix inversion and computation tasks. In both the averaged-value and dynamic equivalent modeling approaches, a single EMT simulator will solve the entire network containing regular EMT-type and averaged or dynamic equivalent models.

Co-simulation is another approach to enable EMT-type simulation of a large network. Co-simulation is based upon an interface established between an EMT simulator and another solver. The two simulators will each solve a distinct portion of the large network under consideration concurrently. The core benefit of co-simulation is that it allows better matching between the constituent simulators and the properties of the network subsections they simulate. For example, portions of the network wherein fast transients may be reasonably ignored will be assigned to and solved by a simulator with less computational demand than an EMT solver.

Since constituent simulators may not necessarily simulate networks in the same domain (i.e., time or frequency), simulated waveform samples need to be properly transferred from one simulator to another; this requires specific mapping algorithms to ensure

$$x(t - T + s) = x_0(t) + 2 \text{Re} \left( \sum_{h=1}^{+\infty} x_h(t) e^{j h \frac{2\pi}{T} (t - T + s)} \right) \tag{3}$$

Therefore, it is seen that the dynamic phasor corresponding to the $h$-th harmonic component is $2 x_h(t)$, which shows the time-varying