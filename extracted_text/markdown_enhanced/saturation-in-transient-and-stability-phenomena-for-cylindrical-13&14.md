# Effect of Reactance Saturation on Transient and Stability for Cylindrical Synchronous Machine
Daisuke Hiramatsu*, Yoichi Uemura*, Masashi Kobayashi*, Mikio Kakiuchi*, Ken Nagakura*, Toru Otaka*, Ken Nagasaka**

**Abstract--** This paper presents the influence of reactance saturation in transient and stability phenomena for cylindrical synchronous machine. For this purpose the authors have examined various equivalent circuit models using electromagnetic transients program (EMTP-ATP).
**Index Terms—** turbine generator, flux saturation, operational-impedance, EMTP

*D.Hiramatsu,Y.Uemura,K.Tsujikawa,M.Kobayashi,M.Kakiuchi,K.Nagakura, T.Ueda,H.Hosaka, and T.Otaka are with Toshiba Corporation 2-4 Suehiro-cho, Tsurumi-ku, Yokohama 230-0045 Japan.
** K. Nagasaka is with Tokyo University of Agriculture and Technology, 2-24-16 Nakamachi Koganei Tokyo 184-8588 Japan.

## I. INTRODUCTION
Turbine generators are extensively used for power generation since many years ago. The capacity of single unit is significantly increasing to catch up with the growing demand for power in recent years. We have manufactured and delivered 2-pole 900,000 to 1,200,000kVA-class generator units to customers in Japan and abroad.

Authors are looking for equivalent circuit with enhanced accuracy to estimate the transients of the larger capacity units. The Park model(1) shown in Fig. 1 is generally used as an equivalent circuit model for evaluating the synchronous machines [1]. The Park model is a linear model assuming constant reactance in the equivalent circuit. However reactance varies with permeability or magnetic saturation. There is another Park model(2) (Fig. 2) which considers the magnetic saturation and, further, reactance $x'_q$ of the quadrature axis (hereafter called $q$-axis) in the transient region, which is often omitted in the conventional equivalent circuits. This Park model is useful for estimating the load rejection characteristics of cylindrical generators with good accuracy.[2] [3] [4] The authors have studied the effect of $x'_q$, and gained new knowledge.

Generator reactance varies in momentarily changing transients due to the effect of saturation. This state is analyzed in the AC frequency range considering saturation, but no report has been published on transient phenomena and transient stability considering the transient DC components. By returning to the starting point, we studied the effect of reactance magnetic saturation and $x'_q$ on various transient phenomena and transient stability from the following points of view.

As equivalent circuit elements,
(1) Saturation value is applied as the constant value
(2) Magnetic saturation is considered for $d$- and $q$-axis armature reaction reactance, to represent the momentary changes
(3) Like analysis program (EMTP-ATP), magnetic saturation is polyline-approximated to represent the momentary changes.

We have studied the above cases, and the result is reported below.

```
       $R_a$     $x_l$                                   $R_a$     $x_l$
                      $x_{fd}$      $x_{kd}$                                  $x_{kq}$
          $x_{ad}$                                         $x_{aq}$
                     $R_{fd}$      $R_{kd}$                                   $R_{kq}$
           $d$ axis                                  $q$ axis
Fig.1. Park model(1)
```

```
       $R_a$      $x_l$                                   $R_a$      $x_l$
                      $x_{fd}$ $x_{kd}$                                $x_{fq}$
               $k$ $x_{ad}$
                                                                                      $x_{kq}$
                                                                         $k$ $x_{aq}$
                     $R_{fd}$ $R_{kd}$                                $R_{fq}$ $R_{kq}$
           $d$ axis                             $q$ axis
Fig.2.Park Model (2):with flux saturation and $x'_q$
```

## II. ANALYTICAL MODEL
The structure of the rotor of a large-capacity turbine generator is shown in Fig. 3. As seen from the figure, the rotor has a solid core and electric current flows on the shaft surfaces and wedges in a transient.

Fig. 3 also shows the analytical model used in the present study. The model system is assumed to be connected to an infinite bus. In this paper, two model cylindrical type generators with a solid rotor (500,000 and 800,000 kVA-class) are used. We have done the analysis considering AVR and PSS (power system stabilizer).

```
Wedge
External Impedance
Field Winding
Infinite Bus
Rotor Shaft
Mechanical Input
Fig.3. Generator Model (Rotor Construction and Analytical Model)
```

## III. VARIABLE REACTANCE WITH MAGNETIC SATURATION
### A. Saturated and Unsaturated Reactance
Reactance is used in the analysis of steady-state and transient characteristics of a synchronous machine. Reactance measured in the area where the effect of saturation appears (normally rated voltage) is called saturated reactance.

Figs. 4 and 5 show the flux distribution and magnetic saturation characteristics of the model generator (500,000kVA class cylindrical solid core rotor). By these two figures, we estimating load rejection characteristics of cylindrical generators with good accuracy[2][3][4].