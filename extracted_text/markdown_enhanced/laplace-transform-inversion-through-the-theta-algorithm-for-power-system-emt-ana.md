# Laplace transform inversion through the theta algorithm for power-system EMT analysis

L.J. Castañón$^{a,*}$, J.L. Naredo$^{a}$, J.R. Zuluaga$^{a}$, E. Bañuelos-Cabral$^{b}$, Pablo Gómez$^{c}$

$^{a}$ Cinvestav Guadalajara, Mexico  
$^{b}$ Universidad de Guadalajara, CUCEI, Mexico  
$^{c}$ Western Michigan University, United States  

* Corresponding author. E-mail address: lorenzo.castanon@cinvestav.mx (L.J. Castañón).

**Keywords:** Electromagnetic transients, Frequency-domain, Laplace transform, Padé approximants, Shanks transformation, Epsilon algorithm, Theta algorithm

**Abstract:** Laplace transform analysis of electromagnetic power system transients generally is based on a technique in which the Laplace inversion integral is truncated with a suitable data window. This technique, being referred to as WNLT, is appropriate for most practical cases. Nevertheless, it results inadequate for certain R&D tasks. This paper presents a new technique for numerical Laplace inversion that does not require truncation with a data window; it instead uses Brezinski’s theta algorithm to account for the infinite range of the Laplace inversion integral. As opposed to the WNLT, the new technique guarantees consistent and high accuracy levels at low computational costs. Finally, the new technique is applied to the transient analysis of a power-system network. Its results compare favorably well with those from the PSCAD/EMTDC program.

## 1. Introduction

The analysis and simulation of electromagnetic transients (EMTs) are essential for the design and the safe and reliable operation of electric power systems (PS). These activities are usually carried out using time domain (TD) methods based on EMTP methodologies (ATP, PSCAD/EMTDC, EMTP-RV, etc.) [1,2]. Nevertheless, for many years, progress in EMT analysis has been driven by advances in frequency-domain (FD) analysis. At this respect, a key player among power-system specialists has been the Windowed Numerical Laplace Transform (WNLT) [6,7]. The WNLT has been adopted both, as an R&D tool and as a reference method to assess time-domain methods, models, and results [3, 4, 5].

The WNLT discretizes the Laplace inversion integral converting it to an infinite sum that is then truncated for numerical evaluation [2,6]. The errors due to this truncation are decreased by applying a suitable data window [2,6,7,8,9,10]. Typical accuracies delivered by the WNLT are within the range of $10^{-3}$ and $10^{-6}$, which is appropriate for most practical situations. Until recently, the WNLT had responded well to the needs of PS-EMT specialists. However, sustained progress in this field is pushing the WNLT beyond its limits. Therefore, new and more advanced tools are needed to support progress in EMT analysis. This paper demonstrates the limitations of the WNLT and has as its main objective the introduction of a new FD tool that is more accurate and reliable than the WNLT. Although the new method is primarily intended as an R&D tool, the general community of PS-EMT specialists may also benefit from its use.

One limitation of the WNLT is that its accuracy is not fixed; that is, if any parameter of a signal to be inverted is modified, the resulting precision changes. Another limitation is that the maximum precision offered by the WNLT is $10^{-9}$ and this is attained at a very high computational cost; that is, it requires a high number of spectral samples, in the order of $2^{20}$ (1,048,576). An application of the WNLT requiring a guaranteed accuracy of $10^{-9}$ or better is the delay identification and extraction from a frequency-domain function prior to applying a rational fit [11,23]. A poor delay extraction can result in rational fits of an unnecessary high order and with increased possibilities of being non-passive.

Other methods to invert numerically the Laplace transform do not truncate the integration range; instead, these methods use extrapolation techniques to approximate sums of infinite series; these are referred to as sum-acceleration methods and offer high and fixed accuracies with a moderate number of samples and, in consequence, with moderate computational cost. These methods have not been extensively applied to PS-EMT analysis. If anything, only to small networks with single-phase lines with constant parameters [12]. Previously, the authors of this paper have presented one of these methods, the QD algorithm [13].

This paper presents a new numerical inversion technique for the Laplace transform that is based on Brezinski’s Theta algorithm [14,15] to accelerate the convergence of infinite sums. To the best of these authors’ knowledge, this is the first application of Brezinski’s Theta algorithm in the inversion of the Laplace transform, as well as in the analysis of power-system EMTs. This paper shows that the Theta algorithm far exceeds the limitations of the WNLT at a moderate computational cost.

## 2. Numerical treatment of the Laplace transform

Let $f(t)$ represent a time-domain signal and $F(s)$ its corresponding Laplace transform, both are related by the Laplace inversion integral:
$$ \int_{c-j\infty}^{c+j\infty} $$

$$ f(n\Delta t) + \epsilon_{al} = \frac{2e^{cn\Delta t}}{\Delta t} \text{Re} \left\{ \frac{1}{N} \sum_{k=0}^{\infty} F(c + jk\Delta\omega) e^{j2\pi nk/N} \right\} \quad (9) $$

with $n = 0, 1, 2, \dots, N - 1$.

For the sake of clarity, the following notation is now adopted:
$$ f_n = f(n\Delta t) $$
and $F_k = F(c + jk\Delta\omega)$.

The evaluation of (9) requires truncating the summation at its right-hand-side to a finite number of terms $M$:
$$ f_n + \epsilon_{al} = \frac{2e^{cn\Delta t}}{\Delta t} \text{Re} \left\{ \frac{1}{N} \sum_{k=0}^{M-1} F_k e^{j2\pi nk/N} \right\} $$