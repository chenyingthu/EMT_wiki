---
title: "Detailed Switch Model"
type: model
tags: [switch-model, power-electronics, detailed-modeling, transient-analysis, igbt, mosfet, thyristor, diode, snubber-circuit]
created: "2026-05-02"
updated: "2026-05-03"
---

# Detailed Switch Model

## 模型定义 (Definition)

**详细开关模型（Detailed Switch Model）**是电磁暂态（EMT）仿真中用于精确描述电力电子开关器件动态行为的数学表示。该模型通过考虑开关器件的寄生参数、非线性特性和状态转换过程，实现对开关瞬态、损耗计算和电磁干扰（EMI）分析的精确仿真。

在EMT仿真框架下，详细开关模型通过以下核心要素描述开关行为：

- **双状态表示**: 开关在导通（ON）和关断（OFF）两种状态间切换
- **寄生元件建模**: 包含结电容、引线电感和导通电阻等寄生参数
- **非线性V-I特性**: 考虑器件电压-电流关系的非线性变化
- **开关动态过程**: 描述开通/关断过程中的电压、电流变化轨迹
- **损耗计算**: 量化导通损耗和开关损耗用于热设计

详细开关模型是电力电子系统EMT仿真的核心组件，用于分析功率变换器、电机驱动、新能源系统和高压直流（HVDC）输电系统中的开关瞬态行为。

### Importance in EMT Simulation

Power electronic switches operate in two distinct states (ON and OFF) with dramatically different electrical characteristics. During state transitions, switches exhibit complex nonlinear behavior including:

- **Finite switching times**: Real switches require microseconds to milliseconds to change state
- **Parasitic elements**: Capacitances, inductances, and resistances affect switching behavior
- **Nonlinear characteristics**: Device properties vary with voltage, current, and temperature
- **Switching losses**: Energy dissipation during transitions impacts thermal design
- **Electromagnetic interference**: Fast switching generates high-frequency transients

### Classification of Switch Models

Switch models in EMT simulation can be categorized by complexity level:

| Model Type | Complexity | Use Case |
|------------|------------|----------|
| Ideal switch | Low | Topology verification, fundamental frequency analysis |
| Resistance-based | Medium | Steady-state analysis, approximate loss calculation |
| Detailed physics-based | High | Switching transient analysis, EMI prediction, precise loss calculation |
| Behavioral models | Variable | Specific applications (thermal, aging, reliability) |

### EMT Simulation Challenges

EMT simulators face unique challenges with switch modeling:

1. **Topology changes**: Each switching event alters the system matrix
2. **Numerical stiffness**: Wide range of time constants (nanoseconds to seconds)
3. **Interpolation requirements**: Accurate switching instant detection
4. **Computational efficiency**: Frequent matrix refactorizations

---

## Ideal Switch Model

The ideal switch model represents the simplest abstraction for power electronic devices, suitable for preliminary analysis and topology verification.

### Mathematical Representation

```
ON State:  V = 0,  I = arbitrary (short circuit)
OFF State: I = 0,  V = arbitrary (open circuit)
```

The ideal switch is characterized by:
- Zero ON-state voltage drop
- Zero OFF-state leakage current
- Instantaneous switching (zero transition time)
- Infinite voltage and current handling capability

### Implementation in EMT

In nodal admittance matrix formulation:

$$Y_{switch} = \begin{cases}
\infty & \text{ON state (represented by large conductance } G_{on} = 10^6 \text{ S)} \\
0 & \text{OFF state (represented by small conductance } G_{off} = 10^{-6} \text{ S)}
\end{cases}$$

### Equivalent Circuit

```
    Terminal A
        |
    +---+---+
    |       |
   [Gsw]   Ideal
    |    Switch
    +---+---+
        |
    Terminal B
```

Where $G_{sw}$ represents the switch conductance.

### Advantages and Limitations

**Advantages:**
- Fastest simulation speed
- No convergence issues
- Suitable for fundamental frequency analysis
- Good for topology verification

**Limitations:**
- Cannot calculate switching losses
- No switching transient analysis
- Cannot predict voltage/current spikes
- Inaccurate for high-frequency analysis

### Applications

- Initial topology verification
- Control system design
- Harmonic analysis at switching frequency
- Educational purposes

See also: [[ideal-switch-model]], [[average-value-model]]

---

## Resistance-Based Switch Model

The resistance-based switch model represents devices using state-dependent resistances, providing a compromise between simulation speed and accuracy.

### Model Structure

$$R_{sw}(t) = \begin{cases}
R_{on} & \text{when switch is ON} \\
R_{off} & \text{when switch is OFF} \\
R_{transition}(t) & \text{during switching}
\end{cases}$$

### Typical Parameter Values

| Device Type | $R_{on}$ (mΩ) | $R_{off}$ (MΩ) | $V_{rated}$ (V) |
|-------------|---------------|----------------|-----------------|
| Low-power MOSFET | 10-100 | 1-10 | 20-200 |
| High-power MOSFET | 1-20 | 1-10 | 200-1000 |
| IGBT | 1-10 | 0.1-1 | 600-6500 |
| Power Diode | 0.5-5 | 1-10 | 100-8000 |
| Thyristor/SCR | 0.1-2 | 1-10 | 200-8000 |

### Conductance Representation

For numerical stability, EMT programs often use conductance:

$$G_{sw} = \frac{1}{R_{sw}}$$

During switching transitions:

$$G_{sw}(t) = G_{on} + (G_{off} - G_{on}) \cdot f(t)$$

Where $f(t)$ is a transition function:
- Linear: $f(t) = \frac{t - t_0}{t_{sw}}$
- Exponential: $f(t) = 1 - e^{-\frac{t-t_0}{\tau}}$

### Equivalent Circuit

```
    Terminal A
        |
    +---+---+
    |       |
   [Rsw]   |
    |       |
    +---+---+
        |
    Terminal B
```

### State Transition Logic

```
IF (Gate Signal = HIGH AND t ≥ t_trigger):
    State = ON
    Rsw = Ron
ELSE IF (Gate Signal = LOW AND t ≥ t_trigger):
    State = OFF
    Rsw = Roff
ELSE:
    Rsw = interpolate(Ron, Roff, t_transition)
```

### Loss Calculation

Conduction losses:

$$P_{cond} = I_{rms}^2 \cdot R_{on}$$

Total switch losses (approximate):

$$P_{total} = P_{cond} + E_{sw} \cdot f_{sw}$$

Where $E_{sw}$ is switching energy and $f_{sw}$ is switching frequency.

---

## Inductance/Capacitance Based Models

Detailed switch models incorporate parasitic inductances and capacitances to accurately capture switching transients and high-frequency behavior.

### Parasitic Capacitance Models

Power semiconductor devices exhibit parasitic capacitances that significantly affect high-frequency switching:

#### MOSFET Capacitance Model

```
         D (Drain)
          |
    +-----+-----+
    |           |
   Cgd         Cds
    |           |
    +     S     |
    |     |     |
   Cgs    +-----+
    |     |
    G     +---- Body Diode
   (Gate) |
          |
         S (Source)
```

**Capacitance definitions:**
- $C_{iss} = C_{gs} + C_{gd}$ (input capacitance)
- $C_{oss} = C_{ds} + C_{gd}$ (output capacitance)
- $C_{rss} = C_{gd}$ (reverse transfer capacitance)

#### IGBT Capacitance Model

```
         C (Collector)
          |
    +-----+-----+
    |           |
   Cgc         Cce
    |           |
    +     E     |
    |     |     |
   Cge    +-----+
    |     |
    G     |
   (Gate) |
          |
         E (Emitter)
```

**Typical capacitance values:**

| Device | $C_{iss}$ (nF) | $C_{oss}$ (nF) | $C_{rss}$ (pF) |
|--------|----------------|----------------|----------------|
| Small MOSFET | 0.5-2 | 0.1-0.5 | 50-200 |
| Large MOSFET | 5-50 | 1-10 | 200-1000 |
| IGBT (600V) | 1-10 | 0.5-2 | 50-500 |
| IGBT (1200V) | 2-20 | 1-5 | 100-1000 |

### Parasitic Inductance Models

Stray inductances in the switching loop cause voltage overshoot:

$$V_{overshoot} = L_{stray} \cdot \frac{di}{dt}$$

**Sources of stray inductance:**
- Package inductance: $L_{pkg}$ = 5-50 nH
- PCB trace inductance: $L_{pcb}$ = 10-100 nH
- Connection inductance: $L_{conn}$ = 5-30 nH
- Busbar inductance: $L_{bus}$ = 20-200 nH

Total loop inductance:

$$L_{loop} = L_{pkg} + 2L_{pcb} + 2L_{conn} + L_{bus}$$

### Complete LC Switch Model

```
        Terminal 1
            |
    +-------+-------+
    |       |       |
   Lstray  Cds     Ron
    |       |       |
    +---+---+   +---+
        |           |
       Cgd         |
        |           |
    +---+---+       |
    |       |       |
    G     Rg      Terminal 2
  (Gate)   |
            |
           GND (reference)
```

### Mathematical Model

The complete switch model with parasitics:

$$V_{ds}(t) = V_{dc} - L_{loop} \frac{di_d}{dt} - R_{on} \cdot i_d$$

$$i_d(t) = C_{oss} \frac{dV_{ds}}{dt} + \frac{V_{ds}}{R_{off}}$$

Gate circuit equation:

$$V_g = R_g \cdot i_g + L_g \frac{di_g}{dt} + V_{gs}$$

$$i_g = C_{iss} \frac{dV_{gs}}{dt} - C_{gd} \frac{dV_{ds}}{dt}$$

---

## Diode and Thyristor Models

Diodes and thyristors (SCRs) are fundamental power electronic devices with unique modeling requirements.

### Power Diode Models

#### Static Characteristic

The diode static I-V characteristic follows the Shockley equation:

$$I_D = I_s \left( e^{\frac{qV_D}{nkT}} - 1 \right)$$

Where:
- $I_s$: Reverse saturation current
- $n$: Ideality factor (1-2)
- $k$: Boltzmann constant
- $T$: Junction temperature
- $q$: Electron charge

For power diodes at high currents, the on-state characteristic includes resistive drop:

$$V_D = V_{to} + R_d \cdot I_D$$

Where:
- $V_{to}$: Threshold voltage (0.5-1.5 V)
- $R_d$: Dynamic resistance (0.1-100 mΩ)

#### Reverse Recovery Model

Diodes exhibit reverse recovery when switching from forward to reverse conduction:

```
Current
   |
IF |     +----+   <-- Forward current
   |    /      \
   |   /        \
   +--+          +--------+
   |  |          |        \
   |  |          |         \
-IR |  +----------+          +----> Time
   |    trr
   |
```

Reverse recovery parameters:
- $t_{rr}$: Reverse recovery time (10 ns - 10 μs)
- $Q_{rr}$: Reverse recovery charge
- $I_{RM}$: Peak reverse recovery current
- $di/dt$: Rate of current commutation

$$Q_{rr} = \frac{1}{2} \cdot I_{RM} \cdot t_{rr}$$

#### Diode EMT Model

```
    Anode
       |
    +--+--+
    |     |
  [Rd]   [Cd]
    |     |
    +--+--+--[Lrr]--+
       |            |
      [Vto]      [Roff]
       |            |
    +--+------------+
       |
    Cathode
```

See also: [[diode-model]], [[power-electronics]]

### Thyristor (SCR) Models

#### Static Characteristics

Thyristor operation states:
- **Forward blocking**: High impedance until $V_{AK} > V_{BO}$ (breakover voltage)
- **Forward conducting**: Low impedance after triggering
- **Reverse blocking**: High impedance for reverse voltage

Static I-V model:

$$I_A = \begin{cases}
0 & V_{AK} < V_{to} \text{ (blocking)} \\
\frac{V_{AK} - V_{to}}{R_{on}} & \text{conducting}
\end{cases}$$

#### Dynamic Characteristics

**Turn-on process:**
- Delay time ($t_d$): 0.1-2 μs
- Rise time ($t_r$): 0.1-1 μs
- Spread time ($t_p$): 1-50 μs (plasma spreading)

**Turn-off process:**
- Reverse recovery similar to diode
- Gate recovery time
- Forward blocking recovery

$$t_q = t_{rr} + t_{gr}$$

Where $t_q$ is the turn-off time (5-500 μs depending on device rating).

#### Gate Triggering Model

Thyristor triggering condition:

$$I_G > I_{GT} \quad \text{AND} \quad V_{AK} > V_{to} \quad \text{AND} \quad t_{pulse} > t_{min}$$

Where:
- $I_{GT}$: Gate trigger current (1-200 mA)
- $V_{GT}$: Gate trigger voltage (0.5-2 V)
- $t_{pulse}$: Gate pulse width

#### Snubber Requirements

Thyristors require RC snubbers for:
- $dv/dt$ protection: $\frac{dv}{dt} < \left(\frac{dv}{dt}\right)_{max}$
- Voltage spike suppression

$$R_{snubber} \approx \sqrt{\frac{L_s}{C_s}}$$

See also: [[thyristor-control]], [[thyristor-control]], [[power-electronics]]

---

## IGBT and MOSFET Models

### MOSFET Models

#### Static Model

MOSFET operation regions:

**Cutoff Region** ($V_{GS} < V_{th}$):
$$I_D = 0$$

**Linear Region** ($V_{GS} > V_{th}$, $V_{DS} < V_{GS} - V_{th}$):
$$I_D = \mu C_{ox} \frac{W}{L} \left[ (V_{GS} - V_{th})V_{DS} - \frac{V_{DS}^2}{2} \right]$$

**Saturation Region** ($V_{GS} > V_{th}$, $V_{DS} \geq V_{GS} - V_{th}$):
$$I_D = \frac{1}{2} \mu C_{ox} \frac{W}{L} (V_{GS} - V_{th})^2 (1 + \lambda V_{DS})$$

For power MOSFETs in on-state:

$$R_{DS(on)} = \frac{1}{\mu C_{ox} \frac{W}{L} (V_{GS} - V_{th})}$$

#### Temperature Dependence

$$R_{DS(on)}(T) = R_{DS(on)}(25°C) \cdot [1 + \alpha (T - 25)]$$

Where $\alpha \approx 0.007 /°C$ for silicon MOSFETs.

#### Gate Charge Model

Total gate charge:

$$Q_g = Q_{gs} + Q_{gd} + Q_{ov}$$

Where:
- $Q_{gs}$: Gate-source charge
- $Q_{gd}$: Gate-drain (Miller) charge
- $Q_{ov}$: Overcharge

Gate voltage during switching:

$$V_{gs}(t) = V_{drive} \left( 1 - e^{-\frac{t}{R_g C_{iss}}} \right)$$

### IGBT Models

#### Static Characteristics

IGBT combines MOSFET input characteristics with bipolar output:

**Transfer characteristic:**
$$I_C = \begin{cases}
0 & V_{GE} < V_{GE(th)} \\
K(V_{GE} - V_{GE(th)})^2 & V_{GE} > V_{GE(th)}
\end{cases}$$

**Output characteristic:**
$$V_{CE} = V_{CE(sat)} = V_{to} + \frac{I_C}{g_m}$$

Where:
- $V_{to}$: Threshold voltage (0.5-1.0 V)
- $g_m$: Transconductance

Typical on-state voltage: 1.5-3.5 V at rated current.

#### IGBT Capacitances

| Capacitance | Definition | Typical Range |
|-------------|------------|---------------|
| $C_{ies}$ | $C_{ge} + C_{gc}$ | 1-20 nF |
| $C_{oes}$ | $C_{ce} + C_{gc}$ | 0.5-5 nF |
| $C_{res}$ | $C_{gc}$ | 0.1-1 nF |

#### Switching Characteristics

**Turn-on sequence:**
1. Turn-on delay ($t_{d(on)}$): Gate voltage rises to threshold
2. Current rise ($t_{ri}$): Collector current rises
3. Voltage fall ($t_{fv}$): Collector voltage falls

$$t_{on} = t_{d(on)} + t_{ri} + t_{fv}$$

**Turn-off sequence:**
1. Turn-off delay ($t_{d(off)}$): Gate voltage falls
2. Voltage rise ($t_{rv}$): Collector voltage rises
3. Current fall with tail ($t_{fi} + t_{tail}$)

$$t_{off} = t_{d(off)} + t_{rv} + t_{fi} + t_{tail}$$

**Tail current phenomenon:**

$$I_{tail}(t) = I_{tail0} \cdot e^{-\frac{t}{\tau_{tail}}}$$

Where $\tau_{tail}$ = 0.1-2 μs, causing significant turn-off losses.

#### Switching Energy

$$E_{on} = \int_0^{t_{on}} v_{ce}(t) \cdot i_c(t) dt$$

$$E_{off} = \int_0^{t_{off}} v_{ce}(t) \cdot i_c(t) dt$$

$$P_{sw} = f_{sw} \cdot (E_{on} + E_{off})$$

See also: [[igbt-model]], [[power-electronics]], [[average-value-model]]

---

## Switching Dynamics

### Turn-On Dynamics

#### MOSFET Turn-On Process

The turn-on process consists of distinct phases:

**Phase 1: Turn-on delay ($t_0$ to $t_1$)**
- Gate voltage rises from 0 to threshold $V_{th}$
- No drain current flows
- Duration: $t_{d(on)}$

$$t_{d(on)} = -R_g C_{iss} \ln\left(1 - \frac{V_{th}}{V_{drive}}\right)$$

**Phase 2: Current rise ($t_1$ to $t_2$)**
- Gate voltage rises above threshold
- Drain current rises to load current $I_L$
- Drain voltage remains at $V_{dc}$
- Duration: $t_{ri}$

**Phase 3: Miller plateau ($t_2$ to $t_3$)**
- Gate voltage constant at Miller voltage $V_{gp}$
- Drain voltage falls rapidly
- Gate current charges $C_{gd}$
- Duration: $t_{fv}$

$$t_{fv} = \frac{R_g \cdot Q_{gd}}{V_{drive} - V_{gp}}$$

**Phase 4: Fully on ($t_3$ onward)**
- Gate voltage rises to $V_{drive}$
- $V_{DS} = I_L \cdot R_{DS(on)}$

#### IGBT Turn-On Characteristics

IGBT turn-on follows similar phases but with bipolar current contribution:

```
Vge    |          +-------+
       |         /         \
       |        /           \
       |       /             +-------+
       |      /  Miller
       +-----+   Plateau
       t0   t1  t2         t3

Ic     |                +-------+
       |              /
       |            /
       |          /
       |        /
       +-------+----------
              t2

Vce    |              +-------+
       |            /
       |          /
       |        /
       |      /
       +-----+------------
            t2
```

### Turn-Off Dynamics

#### MOSFET Turn-Off Process

**Phase 1: Turn-off delay ($t_0$ to $t_1$)**
- Gate voltage falls from $V_{drive}$ to $V_{gp}$
- Current and voltage unchanged
- Duration: $t_{d(off)}$

**Phase 2: Voltage rise ($t_1$ to $t_2$)**
- Gate voltage at Miller plateau
- Drain voltage rises to $V_{dc}$
- Current constant at $I_L$
- Duration: $t_{rv}$

**Phase 3: Current fall ($t_2$ to $t_3$)**
- Gate voltage falls below threshold
- Drain current falls to zero
- Duration: $t_{fi}$

**Phase 4: Gate discharge ($t_3$ onward)**
- Gate fully discharged
- Device in blocking state

#### IGBT Turn-Off with Tail Current

IGBT turn-off includes a characteristic tail current:

```
Ic     +-------+
       |       \
       |        \
       |         \
       |          +----+    <-- Tail current
       |          |    \
       |          |     +---
       +----------+
       t0         t1  t2  t3

Vce    +          +-------+
       |        /
       |      /
       |    /
       |  /
       +-
```

Tail current loss:

$$E_{tail} = \int_{t_2}^{t_3} V_{dc} \cdot I_{tail}(t) dt$$

### Switching Loss Analysis

Total switching losses depend on:
- DC bus voltage ($V_{dc}$)
- Load current ($I_L$)
- Gate resistance ($R_g$)
- Junction temperature ($T_j$)

$$E_{sw} \propto V_{dc} \cdot I_L \cdot t_{sw}$$

Temperature effect on switching:

$$E_{sw}(T_j) = E_{sw}(25°C) \cdot [1 + \beta (T_j - 25)]$$

Where $\beta$ = 0.003-0.01/°C for IGBTs.

---

## Snubber Circuits

### Purpose of Snubbers

Snubber circuits serve critical functions:
- Limit $dv/dt$ during turn-off
- Limit $di/dt$ during turn-on
- Reduce switching losses
- Suppress voltage transients
- Prevent false triggering

### RC Snubber

#### Circuit Configuration

```
        +----[Rs]----+----+
        |            |    |
        |           [Cs] [Switch]
        |            |    |
       Vdc           +----+----+
        |                 |
        +-----------------+
```

#### Design Equations

Snubber capacitance for $dv/dt$ control:

$$C_s \geq \frac{I_{load}}{\left(\frac{dv}{dt}\right)_{max}}$$

Snubber resistance for damping:

$$R_s = \sqrt{\frac{L_{loop}}{C_s}}$$

Where $L_{loop}$ is the stray inductance in the commutation loop.

Power dissipation in snubber:

$$P_{Rs} = \frac{1}{2} C_s V_{dc}^2 f_{sw}$$

### RCD Snubber

#### Circuit Configuration

```
        +----+----+
        |    |    |
       [Rs] [Cs] [Switch]
        |    |    |
        +----+    |
        |         |
       [Diode]    |
        |         |
        +---------+----+
```

#### Advantages

- Reduced snubber loss compared to RC
- Better voltage clamping
- Faster recovery

Energy stored in capacitor:

$$E_{Cs} = \frac{1}{2} C_s (V_{peak}^2 - V_{dc}^2)$$

### Turn-Off Snubber (Polarized)

```
        +----[Ls]----+----+
        |            |    |
       [Ds]       [Switch]
        |            |
        +------------+----+
```

Inductor limits $di/dt$:

$$L_s \geq \frac{V_{dc}}{\left(\frac{di}{dt}\right)_{max}}}$$

### Undeland Snubber

For DC-DC converters, the Undeland snubber provides:
- Energy recovery
- Reduced losses
- Compact design

```
        +----[Lr]----+----+----+
        |            |    |    |
       [Cr]       [Dr1]  |  [Switch]
        |            |    |    |
        +-----+------+    |    |
              |      [Dr2]|    |
             [Ds]     |   |    |
              |       +---+    |
        +-----+------+---------+
```

### Snubber Design Procedure

1. **Measure or estimate** stray inductance $L_{loop}$
2. **Determine maximum allowed** $dv/dt$ from datasheet
3. **Calculate** $C_s = \frac{I_{load}}{(dv/dt)_{max}}$
4. **Select** $R_s = \sqrt{\frac{L_{loop}}{C_s}}$ (typically 1-100 Ω)
5. **Verify power rating**: $P_{Rs} = \frac{1}{2} C_s V_{dc}^2 f_{sw}$
6. **Check component ratings** for voltage and current

---

## Numerical Issues and Solutions

### Challenges in EMT Simulation

#### Topology Change Problems

Each switching event changes the system admittance matrix:

$$Y(t) \cdot V(t) = I(t)$$

Frequent switching causes:
- Matrix refactorization overhead
- Numerical noise accumulation
- Convergence issues

#### Stiffness Issues

Switch models create widely varying time constants:

$$\tau_{min} = R_{on} \cdot C_{parasitic} \approx 10^{-9} \text{ s}$$
$$\tau_{max} = \frac{L_{load}}{R_{load}} \approx 10^{-3} \text{ s}$$

Stiffness ratio:

$$S = \frac{\tau_{max}}{\tau_{min}} = 10^6 \text{ or higher}$$

#### Switching Instant Detection

Fixed time-step simulation misses exact switching instants:

```
Time step:  |-----|-----|-----|-----|-----|
Switching:       X
                |-- Error --|
```

Interpolation error:

$$\Delta t = t_{actual} - t_{detected}$$

### Solutions

#### Interpolation Techniques

**Linear interpolation** for switching instant:

$$t_{switch} = t_n + \Delta t \cdot \frac{V_{ref} - V(t_n)}{V(t_{n+1}) - V(t_n)}$$

**Backtracking algorithm**:
1. Detect threshold crossing at $t_{n+1}$
2. Interpolate to find $t_{switch}$
3. Reject step to $t_n$
4. Advance to $t_{switch}$ with reduced step
5. Apply switching
6. Continue from $t_{switch}$

#### Variable Time-Step Methods

Adaptive step control:

$$\Delta t_{new} = \Delta t_{current} \cdot \min\left(\sqrt{\frac{\epsilon}{error}}, 2\right)$$

Switching-forced step reduction:

$$\Delta t = \min(\Delta t_{calculated}, t_{next_switch} - t_{current})$$

#### Numerical Oscillation Suppression

**Critical damping adjustment (CDA)**:
- Use trapezoidal rule for smooth intervals
- Switch to backward Euler at discontinuities
- Prevents numerical oscillations

**Artificial damping**:

$$G_{damping} = \frac{C_{eq}}{\Delta t}$$

#### Compensated Source Models

Instead of changing matrix structure, use voltage/current sources:

```
    +----+----+
    |    |    |
   [G]  [I] [Switch Model]
    |    |    |
    +----+----+
```

Where $I$ is a compensation current source.

#### Multi-Rate Simulation

Different time steps for different subsystems:
- Slow subsystem: Power network ($\Delta t_{slow}$ = 50-500 μs)
- Fast subsystem: Switching devices ($\Delta t_{fast}$ = 0.1-1 μs)

Interface via interpolation or state-space modeling.

### Best Practices for EMT Switch Modeling

1. **Use appropriate conductance values**:
   - $G_{on}$ = $10^6$ - $10^{12}$ S (avoid numerical overflow)
   - $G_{off}$ = $10^{-12}$ - $10^{-6}$ S

2. **Implement interpolation** for accurate switching

3. **Set minimum time steps** based on switching frequency:

$$\Delta t_{min} < \frac{1}{100 \cdot f_{sw}}$$

4. **Monitor convergence** with diagnostic output

5. **Use snubbers** when appropriate for stability

---

## Related Models and Cross-References

### Related Switch Models

- [[ideal-switch-model]] - Zero-resistance instantaneous switching
- [[average-value-model]] - Fundamental frequency equivalent
- [[igbt-model]] - Detailed IGBT semiconductor physics
- `mosfet-model` - MOSFET-specific characteristics
- [[thyristor-control]] - SCR and TRIAC models

### Related Power Electronics Models

- [[power-electronics]] - General power electronics framework
- [[thyristor-control]] - Firing angle control and commutation
- [[hybrid-converter-model]] - AC-DC and DC-AC converter topologies
- [[inverter-model]] - DC-AC inverter modeling
- `rectifier-model` - AC-DC rectifier modeling

### Related System Models

- [[mmc-model]] - Modular Multilevel Converter switch modeling
- [[vsc-model]] - Voltage Source Converter
- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] - High Voltage DC transmission
- `motor-drive-model` - Variable speed drive systems
- `renewable-energy-model` - Solar and wind power conversion

### Related Analysis Methods

- [[lightning-transient-analysis]] - EMT simulation techniques
- [[harmonic-analysis]] - Frequency domain effects of switching
- `thermal-model` - Switching loss and thermal management
- `emc-model` - Electromagnetic compatibility analysis

---

## Summary

Detailed switch modeling in EMT simulation requires careful consideration of:

1. **Model fidelity**: Trade-off between accuracy and computational cost
2. **Parasitic elements**: Capacitances and inductances affecting switching behavior
3. **Numerical stability**: Proper handling of topology changes and stiffness
4. **Switching dynamics**: Accurate representation of turn-on and turn-off processes
5. **Loss calculation**: Conduction and switching losses for thermal design
6. **Snubber circuits**: Protection and stress reduction techniques

The appropriate model selection depends on the analysis objectives:
- **System-level studies**: Ideal or resistance-based models
- **Device-level studies**: Detailed physics-based models with parasitics
- **Control design**: Average-value or behavioral models

See also: [[power-electronics]], [[average-value-model]], [[igbt-model]], [[thyristor-control]]

---

## 适用边界 (Applicable Boundaries)

### 适用场景

| 应用场景 | 推荐模型 | 说明 |
|---------|---------|------|
| 系统级拓扑验证 | 理想开关模型 | 快速验证电路拓扑正确性 |
| 稳态损耗估算 | 电阻式模型 | 计算导通损耗和效率 |
| 开关瞬态分析 | 详细物理模型 | 分析dv/dt、di/dt、过电压 |
| EMI/EMC预测 | 含寄生参数模型 | 高频振荡和电磁干扰分析 |
| 热设计验证 | 损耗模型+热网络 | 结温计算和散热设计 |
| 控制策略验证 | 平均值模型 | 忽略开关细节，关注控制性能 |

### 不适用场景

- **纳秒级开关过程**: 当需要分析开关瞬间的详细物理过程（如载流子动态），需用器件级仿真（SPICE）
- **长期老化评估**: 开关寿命预测需考虑材料退化，超出EMT模型范围
- **多物理场耦合**: 电热磁机械强耦合场景需用有限元分析
- **超高频应用**: 射频功率电子（>100MHz）需用微波电路仿真工具

### 关键假设

1. **集总参数假设**: 开关内部电磁场视为集总参数，忽略空间分布效应
2. **准静态近似**: 开关状态变化时间尺度远大于电磁波波长传播时间
3. **温度恒定**: 除非显式耦合热模型，否则假设结温恒定
4. **理想连接**: 开关与外部电路的连接视为理想导线

### 精度边界

| 模型类型 | 电压精度 | 电流精度 | 开关损耗精度 | 适用频率 |
|---------|---------|---------|-------------|---------|
| 理想开关 | N/A | N/A | 无法计算 | DC~kHz |
| 电阻式 | ±10% | ±5% | ±20% | DC~10kHz |
| 详细物理 | ±2% | ±1% | ±5% | DC~1MHz |
| 行为模型 | ±5% | ±3% | ±10% | DC~100kHz |

### 计算效率边界

- **理想开关**: 最快，适合大规模系统（1000+开关）
- **电阻式**: 中等，适合中等规模系统（100-1000开关）
- **详细模型**: 最慢，适合小规模详细分析（<100开关）
- **混合建模**: 不同部分采用不同精度，平衡效率与精度

---

## 代表性来源 (Representative Sources)

### 经典文献

| 文献 | 年份 | 核心贡献 |
|------|------|---------|
| Dommel, "Digital Computer Solution of Electromagnetic Transients" | 1969 | 提出EMT梯形积分框架，奠定开关建模数值基础 |
| Mohan et al., "Power Electronics: Converters, Applications, and Design" | 1989 | 电力电子开关建模经典教材 |

### 开关建模方法论

- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] - VSC-HVDC简化建模与计算强度优化
- [[average-value-model]] - 开关周期平均化建模方法
- [[igbt-model]] - IGBT详细物理建模与参数提取

### 应用案例研究

- 高压直流输电换流阀开关建模
- 新能源并网逆变器开关瞬态分析
- 电机驱动系统PWM开关损耗计算

---

*本文档为EMT Wiki知识库的一部分，内容基于IEEE标准及EMT领域学术文献整理。*
