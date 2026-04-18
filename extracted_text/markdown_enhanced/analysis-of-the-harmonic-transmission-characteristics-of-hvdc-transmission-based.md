# Ultra-Fast Millimeter Wave Beam Steering
Romain Bonjour, Matthew Singleton, Simon Arega Gebrewold, Yannick Salamin, Student Member, IEEE, Felix Christian Abrecht, Benedikt Baeuerle, Arne Josten, Pascal Leuchtmann, Christian Hafner, and Juerg Leuthold
*(Invited Paper)*

**Abstract—** In this paper, we demonstrate ultra-fast millimeter wave beam steering with settling times below 50 ps. A phased array antenna with two elements is employed to realize beam steering. The phased array feeder is implemented with a recently introduced time delay line that provides, at the same time, an ultra-fast tunability, broadband operation, and continuous tuning. Our implementation is used to perform symbol-by-symbol steering. In our demonstration, the beam direction is switched between two sequentially transmitted symbols toward two receivers placed 30° apart. We show the successful symbol-by-symbol steering for data streams as fast as 10 GBd. The suggested scheme shows that the ultra-fast beam steering is becoming practical and might ultimately enable novel high bit-rate multiple access schemes.

**Index Terms—** Ultra-fast beam steering, millimeter wave communication, microwave photonics, radio access network.

Manuscript received October 15, 2015; revised December 2, 2015; accepted December 7, 2015. Date of publication December 17, 2015; date of current version December 31, 2015. This work was supported by the European Union within the European Research Council (ERC) Advanced Grants through the Project ERC PLASILOR under Grant 670478. (Corresponding author: Romain Bonjour.)
The authors are with the Institute of Electromagnetic Fields, ETH Zurich, Zürich 8092, Switzerland (e-mail: rbonjour@ethz.ch; matthew.singleton@outlook.com; simon.gebrewold@ief.ee.ethz.ch; yannick.salamin@ief.ee.ethz.ch; felix.abrecht@ief.ee.ethz.ch; benedikt.baeuerle@ief.ee.ethz.ch; arne.josten@ief.ee.ethz.ch; pascal.leuchtmann@ief.ee.ethz.ch; christian.hafner@ief.ee.ethz.ch; juerg.leuthold@ief.ee.ethz.ch).

## I. INTRODUCTION
To meet the relentlessly growing bandwidth of wireless communication, moving carrier frequencies towards millimeter wave (mmW) is a promising path [1]–[3]. However, higher carrier frequencies experience higher free space path loss [4], increasing the total losses of the wireless link. This drawback can be compensated by using phased array antennas (PAAs) [5]. Besides providing higher reach and reduced crosstalk [6], PAAs enable beam steering in order to direct the energy to multiple users. Non-mechanical and thus fast beam steering is achieved by implementing active feeder networks (FNs) in front of the PAAs [7]. The FNs create and delay copies of the signal using true-time delays (TTDs). If the elements used to delay the signals are not ideal, beam squint will occur, i.e. different frequencies will be steered in different directions.

Millimeter wave PAA systems call for a large fractional bandwidth which makes implementation of TTDs in electronics difficult. Conversely, microwave photonics (MWP) where the signal processing is done relying on photonic technologies rather than electronics offers ample bandwidth. Several MWP PAA architectures have been proposed lately. Such devices could be based on spatial light modulators (SLM) [8]–[12], ring-resonators [13]–[18], switched delays [19], [20], semiconductor optical amplifier (SOA) [21], [22], gratings [17], [23]–[29], dispersive fibers [30]–[35] and tunable phase shifters [36]. While all these devices are optimized for specific applications, none provide large bandwidth, continuous tuneability, and low settling times as needed for ultra-fast beam steering.

In this paper, we demonstrate an ultra-fast beam steering concept relying on microwave photonics processing. The delay lines in the FN are based on a novel microwave photonics true-time delay scheme called Complementary Phase Shifted Spectra (CPSS) which we recently published in [37]. The advantages of ultra-fast beam steering are demonstrated with a proof-of-concept mmW radio-access network leveraging symbol-by-symbol steering. This technique enables highly flexible bandwidth allocation. Thanks to that, the cost and power consumption of the receiver electronics can be strongly reduced. The demonstration is performed for a transmitting antenna array but the same concept could be applied to receiving arrays in a similar way. Moreover, the proposed solution can be fully integrated on photonics platforms as it only relies on standard components such as couplers, waveguides, and phase modulators.

This paper is organized as follows. A short review on the main challenges in next generation mmW communication systems is provided in Section II. In Section III, we detailed the architecture of our ultra-fast beam steering scheme. The proof of concept demonstration with beam steering between 10 GBd symbols is described in Section IV. Finally, we draw our conclusions in Section V.

## II. CHALLENGES IN MILLIMETER WAVE COMMUNICATIONS
The use of mmW carrier frequencies for communication links brings a number of challenges that will be discussed in this section.

### A. Free Space Propagation Losses
Increasing the carrier frequency comes at the price of higher free space path losses [4]. The power budget in a wireless link can be derived from the Friis formula [38]
$$P_{\text{out}} - P_{\text{in}} = L + G_t + G_r + \text{FSPL}, \tag{1}$$
where $P_{\text{in}}$ and $P_{\text{out}}$ are the input and output power of the transmitting and receiving antenna, respectively,

TABLE I