# A Time-Domain AC Electric Arc Furnace Model for Flicker Planning Studies
Randy Horton, Senior Member, IEEE, Timothy A. Haskew, Senior Member, IEEE, and Reuben F. Burch IV, Senior Member, IEEE

**Abstract**—A time-domain model of an AC electric arc furnace (EAF) was developed for power system (flicker) planning studies. The proposed model was implemented in the Electro Magnetic Transient Program (EMTP), and it focuses on the behavior of the EAF during the early stages of the melt cycle, thus providing an accurate prediction of the short term flicker created by the EAF, specifically $P_{st99\%}$. The primary advantages of the proposed model over existing models are: 1) it uses system data that is readily available to the planning engineer; 2) it is a three phase model and can accurately model imbalance and predict flicker at the point of common coupling (PCC) as well as remote buses in the power system; and 3) its accuracy has been verified using synchronized flicker measurements of an actual EAF. Existing time-domain EAF models that are used in flicker planning studies require measurement or statistical data that is difficult to obtain during the planning stages of a project. Frequency domain methods are a popular means of estimating the flicker created by an EAF; however, when these methods are used in flicker planning studies, the operational uncertainty of the EAF introduces error into the calculations. Also, in many cases, frequency domain methods struggle to accurately predict the flicker level at buses remote from the PCC. Thus, a time-domain EAF model which can accurately predict $P_{st99\%}$ at points of interest and uses readily available system information is needed. The following paper describes such an EAF model. Validation of the proposed model is performed by comparing simulation results with flicker measurements of an actual EAF that were time synchronized using global positioning systems (GPS).

**Index Terms**—Flicker, flicker measurement, flicker transfer coefficient, furnaces, power quality.

Manuscript received April 29, 2008; revised August 21, 2008. First published March 27, 2009; current version published June 24, 2009. Paper no. TPWRD-00303-2008.
Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.
R. Horton and R. F. Burch IV are with the Alabama Power Company, Birmingham, AL 35291 USA (e-mail: jorhorto@southernco.com).
T. A. Haskew is with the University of Auburn, Auburn, AL 35291 USA.
Digital Object Identifier 10.1109/TPWRD.2008.2007021

## I. INTRODUCTION
LARGE electric arc furnaces (EAFs) have become a popular means of producing high-quality steel in the U.S. The ability to precisely control the temperature and chemistry of the batch make EAFs an ideal choice for producing high-grade steel that is used in the petroleum and automobile industry. Since both of these industries are on the rise, more and more EAFs are being planned and constructed.

EAFs consume wildly varying amounts of real and reactive power; consequently, they create an enormous amount of flicker. Because of this, it is paramount that a flicker planning study be conducted whenever a traditional system planning (e.g., load flow) study is performed to determine serviceability of the load. IEC 61000-3-7 [7] and IEEE 1453 [1] provide flicker planning criteria that should be used to assess serviceability of flicker producing loads such as EAFs.

The two criteria that are used in [1] and [7] to determine flicker severity and assess its impact on the system are $P_{st}$ and $P_{lt}$. $P_{st}$ is the so called “short term” flicker; $P_{lt}$ is referred to as “long term” flicker. $P_{st}$ is based on a 10 minute measurement interval, while, $P_{lt}$ is based on a two hour time interval. It is well recognized that infrequent high values of $P_{st}$ are not detrimental to power quality, and typically the value that is exceeded 1% of the time (i.e., $P_{st99\%}$) is used instead of the maximum value based on a measurement period of at least one week [7].

The amount of flicker created by the load (e.g., EAF) must be known via calculation or direct measurement before the planning criteria provided in [1] and [7] can be applied. This is an arduous task for several reasons when EAF installations are being evaluated. Direct measurement of a future EAF installation is not possible. When loads such as chipper mills, hammer mills, etc. are evaluated, flicker measurements made of a similar sized mill at another location in the system can be used to estimate the flicker at the proposed location (assuming the system impedance is known at both locations) [7]. However, because system parameters greatly affect the operation of an EAF, flicker measurements made at a similar sized EAF installation can not be used to estimate the flicker level at a proposed site. Thus, whenever flicker planning studies are conducted for future EAF installations, the flicker level must be calculated using either frequency domain or time-domain methods. The following is a discussion of some of the more popular methods.

### A. Frequency Domain Methods
The most popular frequency domain method used to estimate the flicker created by EAFs is provided in [8]. According to [8], the flicker created by an EAF can be estimated using (1)
$$P_{st99\%} = C \frac{S_{sc}}{S_{sys}} \quad (1)$$
where,
- $P_{st99\%}$: flicker level that has a 1% probability of being exceeded;
- $C$: characteristic emission coefficient for $P_{st99\%}$, ranging from 48 to 85 (generally 75 is used);
- $S_{sc}$: short-circuit level at the furnace electrodes;
- $S_{sys}$: short-circuit level of the system at the PCC.

Methods of simulating the time variation of the arc include sinusoidal