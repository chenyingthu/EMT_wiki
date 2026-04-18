# Frequency-Dependent Transmission Line Modeling Utilizing Transposed Conditions
**Bjørn Gustavsen, Member, IEEE**

**Abstract**—Existing phase domain transmission line models are capable of producing highly accurate results for both overhead lines and underground cables. This paper introduces a hybrid line model which gives substantial savings in computation time without loss of accuracy, when one or more circuits of a transmission system are treated as continuously transposed. This is achieved by means of a constant transformation matrix in combination with a reduced-size phase domain line model and a number of single-phase (modal) line models. The calculated examples demonstrate a potential speed increase over a full phase domain model between three and four. If none of the circuits are transposed, the line model degenerates into a full phase domain line model.

This paper proposes a new transmission line model (hybrid line) which utilizes the properties of the near diagonal system to obtain a line model with high computational efficiency, without compromising on accuracy. This is achieved by formulating the line model in terms of a constant transformation matrix, modes, and a (small) phase block which takes into account the coupling between circuits. The resulting model can be applied to any combination of transposed and untransposed circuits, of any geometry.

**Index Terms**—Electromagnetic transients, multicircuit overhead lines, transmission line modeling, transposed circuits.

## I. INTRODUCTION
TRADITIONALLY, frequency-dependent transmission line models have been formulated using frequency-dependent modes and a transformation matrix which is assumed to be constant and real [1], [2]. The usage of modes leads to efficient time domain simulations, but the neglected frequency dependence of the transformation matrix can lead to errors in the simulation result.

With the introduction of phase domain line models [3]–[6] the transformation matrix is not needed and highly accurate simulations can be achieved for both overhead lines and underground cables. However, the usage of phase domain quantities instead of modal domain quantities leads to slower simulations.

When overhead lines are transposed, the user of an EMTP-type program will in principle have to subdivide the line into sections and explicitly introduce the transpositions. However, some of these programs have options for specifying that a circuit be “continuously transposed,” which is less accurate but very convenient from a practical point of view. The continuously transposed option has the effect of introducing unbalancing in the series impedance and shunt admittance matrix which define the line system. For multicircuit overhead lines it has been shown [7] that subsequent application of an appropriate constant transformation matrix will lead to a system with diagonal elements and a few off-diagonal elements which reflect the zero sequence coupling between the circuits.

For transposed double-circuit lines with vertical symmetry, it is possible to take into account the zero sequence coupling using a constant transformation matrix [8], but this approach is only an approximation for general line configurations as the zero sequence coupling is in general frequency dependent.

The author is with SINTEF Energy Research, N-7465 Trondheim, Norway (e-mail: bjorn.gustavsen@energy.sintef.no).

## II. TRANSMISSION LINE EQUATIONS
### A. Approach
A multiconductor transmission line can be described in the frequency domain in terms of a series impedance matrix and a shunt admittance matrix

$$ \tag{1} $$
$$ \tag{2} $$

where $\mathbf{Z}$ and $\mathbf{Y}$ are symmetrical, square matrices.

Assume that the conductors have been numbered such that the conductors within each circuit have contiguous phase numbers. As a result, $\mathbf{Z}$, of a multicircuit overhead line can be subdivided into a number of $3 \times 3$ blocks. Blocks on the diagonal represent the circuit self impedance while the off-diagonal blocks represent mutual coupling between circuits.

Treating a circuit as continuously transposed implies that all conductors within the circuit get the same coupling to any other conductor outside the circuit. This leads to a modification of the elements of $\mathbf{Z}$ and $\mathbf{Y}$ by an averaging process according to the following rules.

1. Diagonal blocks of untransposed circuits are left unchanged.
2. Diagonal blocks of transposed circuits are modified by averaging the diagonal elements, and by averaging the off-diagonal elements [7].
3. The rows of off-diagonal blocks representing coupling from a transposed circuit to an untransposed circuit are modified by averaging the elements within each row.
4. The columns of off-diagonal blocks representing coupling from an untransposed circuit to a transposed circuit are modified by averaging the elements within each column.
5. Off-diagonal blocks representing coupling between two untransposed circuits are left unchanged.
6. Off-diagonal blocks representing coupling between two transposed circuits are modified by averaging the elements within the block [7].

This approach is fully general; it applies to any number of untransposed and transposed circuits, with any numbering of the phases. For a system of transposed circuits and untransposed circuits, we get modes and a phase block of dimension .