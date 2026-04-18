## 考虑不对称故障影响的多馈入直流系统换相失败快速判别方法
张彦涛，邱丽萍*，施浩波，韩奕，李新年，姜懿郎
(电网安全与节能国家重点实验室(中国电力科学研究院)，北京市 海淀区 100192)

## Fast Detection Method of Commutation Failure in Multi Infeed DC System Considering the Effect of Unbalanced Fault
ZHANG Yantao, QIU Liping*, SHI Haobo, HAN Yi, LI Xinnian, JIANG Yilang
(State Key Laboratory of Power Grid Safety and Energy Conservation (China Electric Power Research Institute), Haidian District, Beijing 100192, China)

**ABSTRACT:** The dynamic characteristics of HVDC transmission have a serious impact on the overall power system stability, and that has become the most severe challenge in the multi infeed DC system. The correct identification of commutation failure when unbalanced faults occurred in AC system is of great significance, especially in the stability transient simulation with a quasi steady state DC model. This paper proposed a fast identification criterion to access commutation failure risk, based on the commutation equation of inverter valve, considering the effect of negative sequence voltage components on commutation voltage angle offset during unbalanced fault. The criterion can easily be used in the current HVDC quasi steady state model. The accuracy and effectiveness of the proposed method were verified by comparison with the results of electromechanical and electromagnetic hybrid simulation.

**KEY WORDS:** HVDC; commutation failure; electro-mechanical transient; negative sequence voltage; unbalanced fault; electromechanical and electromagnetic transient hybrid simulation

**摘要：** 多直流馈入系统中直流输电的动态特性对系统整体稳定性的影响成为突出问题。提高交流系统不对称故障时直流准稳态模型对换相失败情况识别的准确度，对于提高系统分析精度具有重要意义。该文从逆变器换流阀的换流方程出发，考虑不对称故障时负序电压分量对换相电压角度偏移的影响，提出一种换相失败风险的快速识别判据。该判据在目前的高压直流准稳态模型基础上稍加修改即可实现。通过与机电–电磁混合仿真结果的比较，验证了文中方法的准确性与有效性。

**关键词：** 高压直流输电；换相失败；机电暂态；负序电压分量；不对称故障；机电–电磁混合仿真

基金项目：国家电网公司科技项目(XT71-15-053)。
Project Supported by Project of State Grid Corporation of China (XT71-15-053).

## 0 引言
换相失败已经成为威胁多直流馈入系统安全稳定运行的主要风险因素[1-2]，特别是多回直流连续换相失败[3-6]，将会导致受端地区大规模功率缺额，对系统安全造成巨大影响。受端电网直流换相失败时，送端交流系统产生的冗余功率涌动与转移，同样可能会造成系统失稳[7]。软件仿真仍然是目前进行电力系统安全性分析的主要手段。在暂态仿真中能否准确模拟直流换相失败过程及其影响，成为直接关系到系统分析结论准确性的关键问题，因而长期以来一直是高压直流输电技术的重要研究内容之一[8-11]。

电磁暂态仿真方法[12-15]可以详细模拟换流阀的换相过程以及直流输电系统控制器的调节作用，因而在交直流系统的仿真分析中其准确性得到广泛认可。基于电磁暂态仿真分析方法的研究及直流工程运行实践表明，受到交流系统故障影响的直流输电系统首次换相失败难以避免[16]，因而在换相失败方面其研究的重点在于如何准确预测换相失败条件，通过改进控制器特性使直流系统尽量避免连续换相失败[16-18]，保证直流系统顺利恢复。

在机电暂态仿真中，由于无法详细模拟直流系统换流阀的暂态过程，截至目前仍采用基于三相对称正序电压推导出的准稳态方程作为其仿真模型[19]。准稳态模型无法准确模拟换相失败过程，也无法准确判断换相失败发生的条件，在实际仿真中只是根据经验将正序电压跌落幅度或根据准稳态方程计算出的关断角作为判据[20]，因而在发生不对称故障时其模拟准确度不佳。目前基于准稳态模型开展的多直流换相失败风险研究多集中于对称故障条件下通过多直流馈入安全指标进行综合评估[21-26]，难以实现特定不对称故障的换相失败识别。

为了弥补机电暂态在直流输电系统方面的不足，同时又能够适用于大规模电网的仿真分析，近年来机电–电磁混合仿真[27]方法得到大力发展，并取得一系列研究成果，其仿真精度也得到实际系统案例的验证[28]。由于混合仿真中电磁暂态仿真部分的规模及其初始化问题尚未得到彻底解决，以及混合仿真速度方面的原因，尚不能满足目前大量方式计算应用的要求。

鉴于目前提高机电暂态仿真中换相失败条件的判别准确性仍有很高的实用价值，本文提出一种考虑不对称故障情况下产生的负序电压分量影响的直流系统换相失败快速判别方法。该方法可以考虑负序电压分量引起的换相电压过零点偏移的影响，因而可提高不对称故障时换相失败条件的判别精度。将本文所提方法结合 PSD-BPA 机电暂态仿真软件，针对我国华东多直流馈入系统进行了大量

**图1** 单 12 脉动直流输电逆变侧示意图
**Fig. 1** Diagram of single 12 pulse DC transmission system

所示序号依次开通和关断。由于平波电抗以及直流线路电感的稳流作用，且换相过程通常时间较短，因而可假定在换相期间，直流电流 $I_d$ 保持恒定，在换流器进行阀间换相时，仅是将该电流由一个阀切换至另一个阀。因而可将直流电流等效为恒定电流源，逆变侧在换相瞬间的等效电路可简化为图 2。