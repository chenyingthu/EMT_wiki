## Mode Domain Multiphase Transmission Line Model Use in Transient Studies

**M. C. Tavares**, **J. Pissolato**, **C. M. Portela**  
UNICAMP - State University of Campinas, COPPE - Federal University of Rio de Janeiro  
Campinas, Rio de Janeiro.  
e-mail: cristina@dsce.fee.unicamp.br, e-mail: portela@vishnu.coep.ufrj.br  
BRAZIL

**Abstract** - This paper presents a new model to represent multiphase transmission lines in transient studies, including the frequency dependence of longitudinal parameters. The model uses the exact modes, for ideally transposed lines, and "quasi-modes" for non-transposed lines. For the latter it is necessary to have a vertical symmetry plane. The frequency dependence is represented with synthetic circuits, with one $\pi$-circuit for each mode. The transformation matrix used for the entire frequency range is the Clarke's one and as it is a real matrix it is modeled through ideal transformers. The model is described for three-phase lines and double three-phase lines.  
An application of the methodology is presented for a 440 kV single three-phase transmission line where it is made mode analysis, statistical energization and frequency scan analysis. The simulations are performed in EMTP with the proposed model and with a frequency dependent EMTP line model, the Semlyen one, supposing the line transposed and non-transposed.

**Keywords**: Transmission line model, frequency dependence, mode domain, transformation matrix, EMTP.

## I. INTRODUCTION

One of the main difficulties when dealing with transient simulation studies in a digital simulator program like EMTP [1] is the correct representation of transmission lines. The EMTP works in the time domain and the network elements are generally represented by their phase quantities. Nevertheless, the transmission line parameters, namely the longitudinal parameters, varies with distance and frequency.  
The former can be well represented through the hyperbolic function in the distributed parameter model or through $\pi$-circuits. To model the frequency dependence it is more complex, for the impedance matrix varies with frequency. As a program like EMTP works in time domain, the frequency dependence of an element is not a straight model.  
It is proposed then model the lines by their modes and deal with several uncoupled cascade of $\pi$-circuits representing the modes. Each mode circuit can have its frequency dependence fully described through synthetic circuits.  
However, there is the transformation matrix, that makes the link between phase and mode domain, which also varies with frequency. In the present model it is proposed to use Clarke transformation matrix as the unique transformation matrix for the entire frequency range. As Clarke matrix is a real one, all its elements are real, it can be represented in EMTP through ideal transformers. This model can be applied to ideally transposed lines, transposed in short distance compared with a quarter of wave length, or non-transposed lines with a vertical symmetry plane. For the former this is an exact solution and for non-transposed lines this is a very good approximation, as shown.  
The theory is described for a three-phase and a double three-phase line, but can also be applied for dc-lines and six-phase lines. [2]  
The methodology is exemplified with a 440 kV single three-phase transmission line and it is made a validation with an established frequency dependent EMTP line model, the Semlyen method incorporated in EMTP [3]. The line is supposed both transposed and non-transposed. First the modes are analyzed, supposing a step in the generation end. Then a transient phenomena is studied, the line energization. A statistical energization is performed and the worst case is reproduced. To conclude, a frequency scan analysis is done, pointing out the differences between the two models.

PE-430-PWRD-0-04-1998 A paper recommended and approved by the IEEE Transmission and Distribution Committee of the IEEE Power Engineering Society for publication in the IEEE Transactions on Power Delivery. Manuscript submitted August 11, 1997; made available for printing April 24, 1998.

## II. THREE-PHASE TRANSMISSION LINE MODEL

The proposed model is described for a three-phase transmission line. The first step is to transform the line parameters from phase domain to mode domain. This is done using Clarke transformation matrix, as shown. Later the transformation matrix itself is included in EMTP, to make the link between the network represented in phase domain and the line represented in mode domain. This is described in detail at the next items.

### 2.1 Mode Domain

Suppose a three-phase transmission line with the ground wires already reduced, as shown in Fig. 1. Note that this line has a vertical symmetry plane. With this symmetry for non-transposed line, as is shown below, Clarke components separate two groups of modes, $\alpha$ (exact mode), and other two modes represented by $\beta$-$0$ components. However even if the non-transposed line has not this symmetry plane the model will still give a good approximation.

$$Z_\alpha = \frac{1}{3}(2A + B - 4D + F) \tag{5}$$

$$Z_\beta = B - F \tag{6}$$

$$Z_{\beta 0} = Z_{0\beta} = -((A - E) + (D - F)) \tag{7}$$