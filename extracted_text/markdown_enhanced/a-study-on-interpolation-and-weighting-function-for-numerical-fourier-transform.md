# A study on interpolation and weighting function for numerical Fourier transform
Xi Shi a, *, Akihiro Ametani a, Aniruddha M. Gole a
a Department of Electrical and Computer Engineering, University of Manitoba, MB R3T 2N2, Canada

**Keywords:**
Numerical Fourier transform
Weighting function
Interpolation
Gibbs oscillation

**Abstract**
In order to mitigate the Gibbs oscillation, a very simple and effective linear mid-point interpolation method is proposed. The relationship between proposed linear mid-point interpolation in time domain and window function in numerical inverse Fourier transform is also investigated in this paper. It is proved that the linear mid-point interpolation in time domain is equivalent to the cosine window function defined as $G_{\cos}(\omega) = \cos\left(\frac{\pi \omega}{2 \omega_{\max}}\right)$, where $\omega_{\max}$ is the maximum angular frequency used in the transform. Furthermore, the cosine window function and sinc window function (also known as sigma-factor) show the similar characteristic. A weighting order $n$, which is originally defined as the power to which the window function is raised, can also be applied to the interpolation method when $n$ is an integer. The $n$th-time interpolation is equivalent to applying the window function $[G_{\cos}(\omega)]^n$ in frequency domain.

## 1. Introduction
Gibbs phenomenon describes the large overshoot and oscillations of the Fourier series at the jump discontinuity, which was first discovered by Henry Wilbraham in 1848 [1]. It was widely believed the oscillation was due to the flaws of the device when re-synthesize the Fourier series. In 1899, Gibbs published a description of the overshoot at the point of discontinuity in [2]. In 1906, a mathematical analysis was given by Maxime Bocher [3]. It’s found out that the overshoot does not die out with the increase of the Fourier terms, but the span can be shortened, while the height of the overshoot remains the same.

In order to alleviate the oscillation, various methods were used, including Fejér summation [4] or Riesz summation [5], sigma-approximation [6], discrete wavelet transform with Haar basis functions [7],etc. In this paper, a very simple, easy-to-use, after computation method is proposed to effectively mitigate Gibbs oscillation.

In Section 2, the cause of the Gibbs phenomenon and the sinc window approach have been reviewed. In Section 3, the linear mid-point interpolation method is introduced; the proof of the equivalence of the linear mid-point interpolation method and cosine window is given; the effect on Gibbs oscillation suppression is compared with sinc window method. In Section 4, the weighting order is applied to linear mid-point interpolation method. In Section 5, the proposed approach is used in the switching surge simulation. The findings are concluded and summarized in Section 6.

## 2. Gibbs phenomenon and sinc window
To get the time domain response, inverse Fourier transform can be applied to the frequency domain functions [8, 9],
$$ f(t) = \frac{1}{\pi} \int_{0}^{\infty} F(\omega)\exp(j\omega t)d\omega \quad (1) $$
where $F(j\omega)$ is the frequency domain function to be evaluated. When (1) is evaluated numerically, the integration range $[0, \infty]$ must be substituted by a finite range $[0, \omega_{\max}]$ with sufficiently large $\omega_{\max}$ as in (2).
$$ f(t) = \frac{1}{\pi} \int_{0}^{\omega_{\max}} F(\omega)\exp(j\omega t)d\omega \quad (2) $$
When the frequency domain function is numerically evaluated, the integration range is abruptly chopped at a certain frequency $\omega_{\max}$. As a result, the original signal $F(\omega)$ can be seen to be multiplied by a “brick-wall” window function $G(\omega)$. From the signal processing view, the window function $G(\omega)$ can be seen as an ideal low-pass/high-cut filter. The window function $G(\omega)$ is defined in (3) and is illustrated in Fig. 1.
$$ G(\omega) = \begin{cases} 1 & 0 \le \omega \le \omega_{\max} \\ 0 & \text{else} \end{cases} \quad (3) $$
This ideal rectangular window function $G(\omega)$ in the frequency domain corresponds to the sinc function $g(t)$ (also called the "sampling function") in the time domain. $g(t)$ is defined in (4) and is illustrated in Fig. 2.
$$ \begin{aligned} g(t) &= \mathcal{F}^{-1}(G(\omega)) \\ &= \frac{\omega_{\max}}{\pi} \frac{\sin(\omega_{\max} t)}{\omega_{\max} t} \\ &= \frac{\omega_{\max}}{\pi} \text{sinc}(\omega_{\max} t) \quad (4) \end{aligned} $$
where $\mathcal{F}^{-1}$ denotes inverse Fourier transform. With $f_{\max} = 10^7$ Hz ($\omega_{\max} = 2\pi \times 10^7$ rad/s), the sinc function in the time domain is as shown in Fig. 2.

The product in frequency domain $F(\omega)G(\omega)$ is equal to convolution in the time domain $f(t) * g(t)$. The oscillations of the sinc function $g(t)$ causes the ripples in the output result. Imagine $f(t)$ is a step function which jumps from 0 to 1 at $t = 0$ s, then the convolut