## Hybrid Average Modeling of Three-Phase Dual Active Bridge Converters for Stability Analysis
Maxime Berger, Student Member, IEEE, Ilhan Kocar, Senior Member, IEEE, Handy Fortin-Blanchette, Member, IEEE, and Carl Lavertu, Member, IEEE

**Abstract—** The three-phase dual active bridge (3p-DAB) converter is widely addressed in emerging power systems applications such as solid-state transformer (SST), and dc microgrids. Its successful integration requires accurate modeling of its small-signal characteristics. Due to its dc-ac-dc structure, the DAB converter brings many challenges in small-signal modeling. The state-space averaging (SSA) has been the first proposed methodology to approximate the control-to-output, and line-to-output transfer functions of the 3p-DAB. However, as shown in this paper, SSA is not precise for the stability analysis of 3p-DAB converters. A generalized state-space averaging (GSSA) model based on the dynamic phasor concept is developed in this paper for the $Y\text{-}\Delta$ 3p-DAB. A hybrid SSA and GSSA model representation is then proposed for the evaluation of all the converter transfer functions. The developed models are validated with detailed time-domain switch-level simulations in an electromagnetic transient type (EMT-type) program. They are also used for the accelerated stability prediction in an EMT-type program.

**Index Terms—** Distributed resources, bidirectional converters, dc-dc conversion, dual active bridge, state-space averaging, generalized averaging, dynamic phasor, Electromagnetic Transients Program

## I. INTRODUCTION

Dual active bridge (DAB) isolated bidirectional dc-dc converters are widely considered as the central element in current and next-generation high-frequency-link power conversion systems [1]. Due to their high flexibility, DAB converters are proposed to be employed in many recent applications. The 3p-DAB converter provides many advantages over the 1p-DAB which is why it is favored in modern flexible dc-grids [9][10][12]. Due to its three-phase structure, the 3p-DAB (Fig. 1) also allows using different winding connections ($Y\text{-}Y$, $Y\text{-}\Delta$, and $\Delta\text{-}\Delta$). It is demonstrated in [13] that the $Y\text{-}\Delta$ transformer offers better performance in terms of stress on switches, transformer utilization, and filter capacitor requirements.

The integration of power electronics in ac- and dc-grids brings new challenges in terms of power system control and stability [14]-[16]. For this reason, this paper focuses on the development of accurate models of the 3p-DAB converter for stability analysis in dc-grid applications. Small- and large-signal analyses are widely used for stability assessment of power electronics-based systems [17]. Converter open-loop small-signal characteristics are generally defined by a set of standard transfer functions: the control-to-output transfer function $G_{vd}(s)$, line-to-output transfer function $G_{vg}(s)$, driving point $Z_D(s)$ and null driving point $Z_N(s)$ input impedances, and output impedance $Z_o(s)$. For the stability analysis of multiple converters interacting with other network components, it is also required to determine the closed loop small-signal characteristics of the converter such as the loop gain $T(s)$, and closed-loop input and output impedances [18].

```
Grid #1                                                                 Input Bridge                                                                 d                                                                 Output Bridge                                                                 io                                                                 Grid #2

vi      ii      S1      S3      S5      iR
        A       iA LA   M : 1   ia      S1’     S3’     S5’
        B       iB LB           a       ib      vo      R
                                b       Co
```