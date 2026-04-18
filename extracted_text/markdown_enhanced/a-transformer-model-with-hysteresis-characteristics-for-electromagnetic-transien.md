## 考虑磁滞特性变压器 PSCAD/EMTDC 电磁暂态仿真建模方法及励磁差异性分析
吴嘉琪$^{1}$，李晓华$^{1}$，陈忠$^{2}$，丁晓兵$^{3}$，田庆$^{3}$
(1．华南理工大学电力学院，广东省 广州市 510640；2．中国南方电网有限责任公司超高压输电公司，广东省 广州市 510620；3．中国南方电网有限责任公司电力调度控制中心，广东省 广州市 510623)

### A Transformer Model With Hysteresis Characteristics for Electromagnetic Transients Based on PSCAD/EMTDC and Excitation Difference Analysis
WU Jiaqi$^{1}$, LI Xiaohua$^{1}$, CHEN Zhong$^{2}$, DING Xiaobing$^{3}$, TIAN Qing$^{3}$
(1. School of Electric Power, South China University of Technology, Guangzhou 510640, Guangdong Province, China; 2. Ultra-High Voltage Transmission Company of CSG, Guangzhou 510620, Guangdong Province, China; 3. Power Dispatching and Communication Center of CSG, Guangzhou 510623, Guangdong Province, China)

**ABSTRACT:** In order to research the inrush problems in HVDC transmission projects, a new three-phase transformer model with hysteresis characteristics of PSCAD/EMTDC was presented, which derives from ideas of the transformer model considering hysteresis characteristics in ATP-EMTP, in which it consists of Type96 and BCTRAN. This model added an excitation branch considering hysteresis characteristics based on the classical model. The hysteresis characteristics can be described effectively when using experimental data obtained. The simulation results show that the model reflects excitation characteristics well, and parameters are readily available, it’s easy for users to use it in PSCAD/EMTDC. It also studied the differences of excitation characteristics simulated by the hysteresis loop and the hysteresis midline, and it concluded that there is a consistency in respect of the inrush current peak in transient process if the hysteresis midline instead of the hysteresis loop to simulate the excitation characteristics of transformer cores, but the hysteresis loop has a greater impact on the transient process especially the harmonic characteristics of inrush current.

**KEY WORDS:** hysteresis loop; hysteresis midline; excitation characteristics; three-phase classical transformer model; ATP-EMTP; PSCAD/EMTDC; electromagnetic transient simulation

**摘要：** 为了研究高压直流输电中励磁涌流问题，该文结合 ATP-EMTP 电磁暂态仿真软件中描述铁心铁磁材料磁滞特性的非线性电感 Type96 以及 BCTRAN 共同建立考虑磁滞特性变压器模型思想，提出一种考虑磁滞特性变压器 PSCAD/EMTDC 电磁暂态仿真新模型。该模型在经典模型的基础上增加了考虑磁滞特性的励磁支路，利用试验获得的最大磁滞回线数据便可有效地反映变压器的磁滞特性，验证表明该模型能很好地反映变压器磁滞特性，且因参数易得，便于用户在 PSCAD/EMTDC 中仿真使用。同时也仿真研究利用磁滞回线和磁滞中线模拟变压器励磁特性的差异性，得出采用磁滞中线代替磁滞回线来模拟变压器铁心励磁特性在励磁涌流峰值上具有一致性，但磁滞回线对涌流稳态过程特别是谐波特性有较大影响。

**关键词：** 磁滞回线；磁滞中线；励磁特性；三相经典变压器模型；ATP-EMTP；PSCAD/EMTDC；电磁暂态仿真

基金项目：国家自然科学基金项目(51377059)。
Project Supported by the National Natural Science Foundation of China (51377059).

## 0 引言
高压直流输电系统一极投入运行时，其上的 Y/Y 和 Y/D 两台换流变将同时空载投入。在系统电压的励磁下，由于换流变内部非线性铁心因不同的初始电压而达到不同的饱和程度，往往会产生较大的励磁涌流，另一极换流变会出现复杂性和应涌流。此过程会对换流变内部结构产生强烈的冲击，同时因励磁涌流含有大量的非周期分量和高次谐波分量，导致电流互感器铁心严重饱和，产生不平衡暂态电流，引起换流变保护误动[1]。因此，研究换流变复杂性涌流特性及其抑制措施研究尤为必要，而其研究核心在于对换流变压器铁心励磁特性的精确建模。文献[2]采用 J-A 理论拟合磁滞回线，通过改良的艾杰文函数来拟合各向同性铁磁物质的理想磁化曲线，以磁畴壁位移思想为基础并根据能量损耗原理推导出磁滞回线方程，由于获取模型中 5 个参数的过程较为复杂，对实际工程不是很实用；文献[3]在经典 Preisach 模型的基础上修正完善了磁滞回线数学模型，但模型参数的确定较为困难，不太适用于实际工程；文献[4]采用修正的反正切函数描述未饱和时主区间内的两条极限磁滞回环，采用两条平行的直线段来描述饱和后主区间外的磁化曲线，只拟合了最大磁滞回线，未考虑其内部的次磁滞回线簇。

综合目前变压器模型研究现状，尚有两方面的问题需要进一步深入研究：
1）考虑磁滞特性变压器 PSCAD/EMTDC 电磁暂态模型。由于 PSCAD/EMTDC 中经典变压器模型不能较好地反映电力变压器的励磁特性真实状况，同时也考虑到，用于国内高压直流输电工程研究的基于 PSCAD/EMTDC 仿真平台的西门子、南瑞的所有直流控制保护模型中没有计及磁滞特性的变压器模型，因此建立考虑磁滞特性的变压器模型很有必要。
2）磁滞回线与磁滞中线模拟变压器励磁特性的差异性以及两种模拟方式在不同研究目的下的选取问题。通过了解两种模拟方式的异同点及各自的优缺点，以便后期研究针对不同的研究目的选取不同的变压器励磁特性模拟方式，目的性更强，研