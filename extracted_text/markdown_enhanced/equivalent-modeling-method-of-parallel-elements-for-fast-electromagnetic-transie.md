## 电力电子变压器电磁暂态并行仿真等效建模方法
孙昱昊，许建中
（新能源电力系统国家重点实验室(华北电力大学)，北京市 昌平区 102206）

## Equivalent Modeling Method of Parallel Electromagnetic Transient Simulation for Power Electronic Transformer
SUN Yuhao, XU Jianzhong
(State Key Laboratory of Alternate Electrical Power System With Renewable Energy Sources (North China Electric Power University), Changping District, Beijing 102206, China)

**ABSTRACT:** Power electronic transformer (PET) has the characteristics of modularity, multiple nodes, and high frequency. However, the inefficient electromagnetic transient simulation (EMT) of its detailed model poses an urgent need for simulation acceleration. In this paper, starting from speeding up the model and improving the CPU computation efficiency, an equivalent modeling method of parallel electromagnetic transient simulation for the power electronic transformer is proposed. Taking the cascaded H-bridge type power electronic transformer (CHB-PET) as an example, the theoretical derivation and simulation verification are carried out. Firstly, on the condition that an admittance is fixed, the power module (PM) is divided into circuits of different admittance units. Secondly, from the perspective of the loaded two ports, it is deduced that the H-bridge element contains only 2 equivalent admittances, which can be simplified as a two-value admittance unit. By prestoring the admittance parameters of each unit and calculating the port short-circuit current with the superposition theorem, the PM Norton equivalent circuit parameters are quickly obtained and aggregated to form a CHB-PET serial equivalent model. Finally, a parallel simulation framework is constructed in combination with the high parallelism of the model. Through simulation verification on the PSCAD/EMTDC, the result shows that the model highly fits the detailed model under various working conditions with the maximum error as less than 3%. When the number of the single-phase modules is 48, the optimal parallel equivalent model is able to achieve a simulation speedup over the detailed model by more than 10000 times.

**KEY WORDS:** power electronic transformer; cascaded H-bridge; admittance unit prestorage; parallel equivalent modelling; multithreaded parallel computing

**摘要：** 电力电子变压器(power electronic transformer，PET)具有模块化、多节点、频率高的特点，其详细模型的电磁暂态仿真(electromagnetic transient，EMT)效率低下，仿真提速需求迫切。从模型自身提速与提高 CPU 计算效率两方面入手，提出了 PET 电磁暂态并行仿真等效建模方法，并以级联 H 桥型 PET(cascaded H-bridge type power electronic transformer，CHB-PET)为例进行了理论推导与仿真验证。首先，以导纳是否可定为标准，将功率模块(power module，PM)划分为不同导纳单元电路的组合；其次，从有载二端口的角度出发，推导出 H 桥单元对外仅含 2 种等效导纳，可简化为二值导纳单元；将各单元的导纳参数预存，利用叠加定理求取端口短路电流，即可快速获取 PM 诺顿等效电路参数，聚合形成 CHB-PET 串行等效模型；最后，结合该模型的高度并行性构建了并行仿真框架。在 PSCAD/EMTDC 中进行仿真验证，该模型实现了对详细模型的多工况高度拟合，最大误差小于 3%。当单相模块数为 48 时，最佳并行等效模型可实现对详细模型 10000 多倍的仿真提速。

**关键词：** 电力电子变压器；级联 H 桥型；导纳单元预存；并行等效建模；多线程并行计算

DOI：10.13335/j.1000-3673.pst.2022.0432

基金项目：北京市自然科学基金项目(3222059)。
Project Supported by Natural Science Foundation of Beijing Municipality (3222059)．

## 0 引言
电力电子变压器(power electronic transformer，PET)因兼具多端口电能汇集与综合功率调控等功能，已逐渐成为大规模交直流混联和新能源并网的关键设备[1-5]。目前国内外针对 PET 的控制器设计、性能优化、样机研发和示范工程建设方兴未艾，总体呈现电压等级、容量不断提高，功率端口与拓扑结构日渐灵活，工作频率不断上升的趋势[6-11]。

为准确反映 PET 高频开关动作引起的瞬态过程，电磁暂态(electromagnetic transient，EMT)仿真已成为辅助样机参数设计、性能测试等方面的重要工具。但是，由于 PET 高矩阵阶数和小仿真步长的特点，基于分立元器件的 EMT 详细仿真模型面临大量高阶矩阵的重构与求逆运算，仿真效率极低，严重影响了研究效率[5,12]。

针对上述问题，目前已有较多学者开展了关于 PET 电磁暂态加速仿真方法的研究，主要呈现两大趋势。一方面，着重提高模型自身求解速率，即从数学原理或等效机制出发，提高模型串行解算速率，但在仿真精度制约下，串行速率将趋于极值；另一方面，关注模型的并行性以提高计算机计算效率，最大限度挖掘处理器计算潜力，从而实现仿真提速。

在串行提速方面，文献[13-15]建立了 PET 平均值模型，可实现高速率仿真，但忽略了换流器内部特性，仿真工况受到限制，使得应用场景受限。文献[16]基于 RT-LAB 开发了 PET 纳秒级实时仿真模型，利用 L/C 等效电路模拟电力电子开关获取定导纳模型，但其本质上仍是一种详细模型，需占用大量仿真资源，且仿真时会产生虚拟功率，仿真精度较差。文献[17-19]采用变压器端口解耦思路建立了通用的 PET 串行等效模型，利用嵌套快速同时求解法降低系统节点数，有明显提速效果。但由于导纳不定，消去过程中每步长须进行矩阵求逆更新导纳值，模块数较多时会影响仿真效率。

探索并行性方面，文献[20-22]提出基于 Bergeron 线路模型的电气网络接口(electric network interface，ENI)技术，实现了不同子系统的并行仿真，但受限于电路结构，该方法仅适用于含传输线侧并联(input-series-output-parallel，ISOP)方式连接而成。单个 PM 由输入侧的 AC/DC 变换器以及含高频隔离变压器的双有源桥(dual active bridge，DAB)型 DC/DC 变换器组成，可实现 AC-DC-AC-DC 四级电能变换。PM 输出侧可直接接入直流负载，或通过 DC/AC 换流器接入交流负载。

**图 1 CHB-PET 系统示意图**
*Fig. 1 Schematic diagram of CHB-PET system*

### 1.1.1 PM 伴随电路形成
针对上述 PM 电路，可采用文献[17]的方法，对 IGBT-二极管开关组电路采用二值电阻等值，电容元件与高频隔离变压器采用梯形积分法(trapezoidal rule，TR)离散化，可得到 PM 伴随电路如图 2 所示，其中的参数由式(1)计算获得。

```
UAUHB1           FAUC1         UAUHB2             FAUT              UAUHB3      FAUC2
                                 -GT12
GA3 GA1                   GH1 GH3               GT12                GL3 GL1
         jC1      GC1             jT1   GT11 GT22       jT2              GC2   jC2
GA4 GA2                GH2 GH4               GT12                GL4 GL2
                                 -GT12
```

**图 2 PM 伴随电路**