# Improved Accuracy Average Value Models of Modular Multilevel Converters

A. Beddard, Member, IEEE, C. E. Sheridan, M. Barnes, Senior Member, IEEE, and T. C. Green, Senior Member, IEEE

**Abstract**—Modular multilevel converters (MMCs) have become the converter topology of choice for voltage-source converter–high-voltage direct-current systems. Excellent work has previously been conducted to develop much needed average value models (AVM) for these complex converters; however, there a number of limitations as highlighted in this paper. This paper builds on the existing models, proposing numerous modifications and resulting in an enhanced MMC-AVM, which is significantly more accurate and which can be used for a wider range of studies, including DC faults.

**Index Terms**—Average value model (AVM), electromagnetic transient (EMT) simulation, HVDC transmission, modular multilevel converter (MMC), voltage-source converter (VSC).

## I. INTRODUCTION

The demand for voltage-source converter (VSC) high-voltage direct-current (HVDC) transmission schemes has grown significantly in the last decade. This growth is mainly due to improvements in the voltage and current ratings of Insulated Gate Bipolar Transistors (IGBT) and the number of new VSC-HVDC applications such as the connection of offshore windfarms.

In 2010, the Trans Bay cable project became the first VSC-HVDC scheme to use Modular Multilevel Converter (MMC) technology. The MMC has many benefits in comparison to two or three level VSCs; chief among these is reduced converter losses. Today, the main HVDC manufacturers offer a VSC-HVDC solution which is based on MMC technology. Accurate and computational efficient models are therefore necessary for the development and understanding of these transmission systems [1]–[3].

There are many different types of MMC model and a number of them have been compared in several publications [4]–[9]. In order to accurately account for converter losses, semi-conductor physics models can be employed, however they are too complex to model an entire converter [1]. Full Detailed Models (FDM) which approximate the semi-conductors’ non-linear characteristics can however be used to model an entire MMC.

Traditional Detailed Models (TDM) represent the converter’s semi-conductors as a two-value resistance and have been shown to simulate faster than a FDM without an appreciable difference in the simulation results for the majority of studies [1]. The TDM is still however very inefficient due to the electrical connection of the MMCs components resulting in a large admittance matrix.

To address this issue, a more efficient model was proposed in [7]. This type of model, which is often referred to as a Detailed Equivalent Model (DEM), creates a Thevenin equivalent circuit for each converter arm and uses a nested fast and simultaneous solution method to significantly improve its efficiency [7]. The accuracy of this type of model has been verified in several publications [1], [8]. The disadvantage of DEM is that the Sub-Module (SM) components are not accessible to the user making this type of model unsuitable for studying internal converter faults. Variants of the DEM have also been proposed in [9]–[11].

The DEM model was simplified further in [6], [12], [13] by not considering each SM separately and therefore assuming that the all of the SM capacitor voltages are perfectly balanced. This simplification enables these types of models to simulate faster than a DEM. However, they cannot be used to study capacitor balancing controllers or variations in the individual SM capacitor voltages due to transient events.

Average Value Models (AVM) neglect the impact of capacitor ripple voltage in each arm of the converter by using a single DC side capacitance [4]–[6]. This enables the internal MMC controllers to be neglected which can improve efficiency further [6]. In addition to their efficiency, AVMs are often employed as their simplicity enables them to be implemented in a wide range of software packages and their accuracy is sufficient for many common power system studies.

One of the first and most widely used AVMs for MMC-HVDC applications was developed by Peralta et al. in [4]. This model represents the AC side of the converter with six voltage sources and the DC side with a single current source. This type of model is very efficient; however, it cannot accurately represent the blocked state of a MMC which means that it is generally unsuitable for DC fault studies. Xu et al. addressed this issue in [5] by incorporating diodes and switches in the AC side of the AVM and connecting the AC side to the DC side in the event of a DC side fault. The connection of the AC side of the AVM to the DC side also enables the offset in the converter voltages arising from a line-to-ground fault to be represented. However, this additional functionality comes with a 37% penalty in computational efficiency [5]. Furthermore, the need to connect the AC side and DC side of the AVM together during fault scenarios makes the implementation of this model challenging in some commonly used soft

Manuscript received August 25, 2015; revised December 1, 2015; accepted February 11, 2016. Date of publication May 4, 2016; date of current version September 21, 2016. This work was supported by the UK Engineering and Physical Science Research Council under, Grant: EPSRC EP/L021463/1. Paper no. TPWRD-01134-2015.R1.

A. Beddard is with The University of Manchester, Manchester, M13 9PL, U.K., and also with Imperial College London, London SW7 2AZ U.K. (e-mail: a.beddard@imperial.ac.uk).

C. E. Sheridan and T. C. Green are with Imperial College London, London SW7 2AZ, U.K. (e-mail: c.sheridan11@imperial.ac.uk; t.green@imperial.ac.uk).

M. Barnes is with The University of Manchester, Manchester, M13 9PL, U.K. (e-mail: mike.barnes@manchester.ac.uk).

Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org.

Digital Object Identifier 10.1109/TPWRD.2016.2535410