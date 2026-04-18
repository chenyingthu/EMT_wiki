## ±800kV 云广特高压直流控制方式的动态特性分析
**刘可真**$^{1,2}$，**束洪春**$^{1,2}$，**孙士云**$^{1,2}$，**司大军**$^3$，**张广斌**$^2$，**朱子钊**$^2$
（1．哈尔滨工业大学电气工程系，哈尔滨 150001；2．昆明理工大学电力工程学院，昆明 650051；3．云南电力科学研究院，昆明 650051）

## Analysis on Dynamic Characteristic of Control Mode for ±800kV Yun-Guang UHVDC
**LIU Ke-zhen**$^{1,2}$, **SHU Hong-chun**$^{1,2}$, **SUN Shi-yun**$^{1,2}$, **SI Da-jun**$^3$, **ZHANG Guang-bin**$^2$, **ZHU Zi-zhao**$^2$
(1. Department of Electrical Engineering, Harbin Institute of Technology, Harbin 150001, China; 2. Faculty of Electric Power Engineering, Kunming University of Science and Technology, Kunming 650051, China; 3. Yunnan Electric Power Research Institute, Kunming 650051, China)

**摘    要：** 云广±800kV 特高压直流输电系统建成之后，将形成远距离和大容量交、直流输电并列运行的电网格局，特高压直流的控制方式对电网的稳定性有重要影响。为此在电磁暂态仿真软件 EMTDC 中对±800 kV 云广直流双极运行下，整流侧分别采用定电流和定功率控制时，交流系统整流侧与逆变侧故障对直流系统的影响，直流控制系统与交流系统的响应过程进行了详细的计算分析，对两种控制方式下系统的动态特性进行了对比分析。结果表明，与整流侧采用定电流控制相比，定功率控制时，交流系统故障期间系统各电气量的变化较缓慢，故障清除后系统恢复过程中，直流电流的突增会导致短时换相失败，且故障后直流系统的恢复时间较长。
**关键词：** 特高压直流；定电流控制；定功率控制；动态特性；电磁暂态；换相失败
**中图分类号：** TM743  **文献标志码：** A  **文章编号：** 1003-6520（2010）01-0190-06

**Abstract:** When Yun-Guang ±800 kV ultra high voltage direct current (UHVDC) project is completed, a parallel AC/DC power system with long distance and heavy capacity will come out. And the UHVDC control mode has important influence on the power system stability. Consequently, Yun-Guang ±800 kV UHVDC bipolar model was established in EMTDC. The effect of AC system faults on the UHVDC transmission system in both constant current and constant power control modes and the response of UHVDC control system were computed and analyzed, respectively. Moreover, the dynamic characteristic of the AC/DC system in two control strategies was comparatively analyzed. The results show that, compared with the constant current mode, all the electrical variables change more slowly than in constant power mode during the power system fault. After the fault is cleared, a sudden increase of DC current may cause short time commutation failure. And the system needs more time to come back to normal operation.
**Key words:** UHVDC; constant current control; constant power control; dynamic characteristic; electromagnetic transient; commutation failure

**基金项目：** 国家自然科学基金（50977039；50847043；90610024；50467002；50347026）；云南省自然科学基金重点项目（2005F0005Z）；云南省自然科学基金（2008ZC016M）；云南省教育厅基金（07Y40615；08Y0058）。
**Project Supported by:** National Natural Science Foundation of China (50977039, 50847043, 90610024, 50467002, 50347026), Key Project of Yunnan Provincial Natural Science Foundation of China (2005F0005Z), Yunnan Provincial Natural Science Foundation of China (2008ZC016M), Foundation of Yunnan Province Education Bureau (07Y40615, 08Y0058).

## 0 引言
南方电网规划2009～2010年采用±800 kV、输送功率5000 MW 的特高压直流将云南水电送往广东。当云广±800 kV 特高压直流输电系统建成之后，将形成远距离和大容量交、直流输电并列运行的电网格局，其规模和复杂程度在国内外史无先例。因此，交流系统或特高压直流系统故障时交流系统与直流系统之间的相互影响及对电网的安全稳定的影响，成为倍受关注的问题［1-4］。而直流输电与交流输电相比，其最大的特点是直流输电拥有复杂而灵活的控制系统，可以快速、精确的调节电流、功率等，输电特性主要由其控制系统决定［5,6］。因此研究云广±800kV 特高压直流输电对云南电网暂态稳定的影响势必要考虑直流输电控制系统的作用［7］。目前广泛使用的中国电力科学研究院的 BPA、PSASP 和美国 PTI 公司的 PSS/E 等机电暂态仿真程序通常情况可以对直流双极闭锁这样的严重故障进行充分地计算和研究，但还存在一定的局限：由于在一系列假设条件下将直流系统作了简化与线性化，受其采用的直流模型限制，当需要考虑交流不对称故障对高压直流换相过程的影响及与直流控制系统性能密切相关的交流扰动后直流系统恢复等问题时，机电暂态仿真就不能给出足够准确的结果，因其不能描述换流阀的开通与关断的动态过程，不能真正反映直流输电控制系统的调节过程，不能确定什么故障可以造成直流闭锁，什么情况可以引起换相失败［8-11］。因此，在研究交直流的相互作用问题时，需要考虑直流换流器的详细模型，采用更精确的电磁暂态仿真模型是十分必要的［12-16］。

本文在电磁暂态仿真软件 EMTDC 中对±800 kV 云广直流双极运行下，整流侧分别采用定电流和定功率控制，交流系统整流侧与逆变侧故障对直流系统的影响以及直流输电线路故障时，直流控制系统与交流系统的响应过程进行了详细的计算分析。整流侧与逆变侧交流线路在不同位置发生不同类型故障时，计算了交流系统换流母线的电压、电流响应，直流系统电压、电流以及相关直流控制量的变化情况。

## 1 云广直流电磁暂态计算的模型
### 1.1 系统模型
云广直流输电工程西起云南楚雄州禄丰县，东至广东增城东部，电压等级为±800 kV，输电线路长度约1438km，输电功率为5GW，额定电流3125 kA，2009-06 建成 ±400 kV 或单极，2010 年建成 ±800kV。送端楚雄换流站通过2回500 kV 交流线路与云南主网500 kV 厂口变电站相连，小湾水电站和金桥水电站分别通过2回和2回500 kV 线路向楚雄站送电；受端换流站分别以2回500kV 交流出线接入增城、横沥和水乡变电站。

根据典型的直流输电模型，建立了如图1所示的云广直流双极电磁暂态模型。其包含的设备有：换流变压器、12脉换流器、交流侧滤波器、直流滤波器、平波电抗器、分布参数的直流输电线路等一次设备以及整流与逆变侧的二次直流系统的额定电压为800kV，每极直流线路的额定功率为2.5GW。

**图1 云广直流电磁暂态模型**
**Fig. 1 Electromagnetic transient model of Yun-Guang UHVDC system**

### 1.2 控制策略及参数
电压下降到一定程度时，转为定最小触发角运行，逆变侧采用定电流调节。当逆变侧交流母线电压下降到一定程度时，为防止换相失败，逆变侧采用定最小关断角 $\gamma_{\min} = 5^\circ$ 调节，而整流侧仍采用定电流调节。当逆变侧交流系统严重故障时，为防止连续换相失败，逆变侧迅速转为低压限流控制方式，同时整流侧也相应地转为低压限流控制方式。

整流侧定电流控制采用 PI 控制模式，比例增益为 $1.0989$，积分时间常数为 $0.01092\text{ s}$。逆变侧定电流控制比例增益为 $0.63$，积分时间常数为 $0.01524\text{ s}$。定关断角控制比例增益为 $0.7506$，积分时间常数为 $0.0544\text{ s}$。低压限流环节（VDCOL）特性参数如图2所示。图中，$I_{\text{dc,pu}}$、$U_{\text{dc,pu}}$ 分别为一极直流电流、电压的标么值（$I_{\text{dc,pu}}$ 的基准电流值为 $3125\text{ kA}$，$U_{\text{dc,pu}}$ 的基准电压值为 $800\text{ kV}$）。当 $0.4 < U_{\text{dc,pu}} < 0.9$ 时，$I_{\text{dc,pu}}$ 与 $U_{\text{dc,pu}}$ 呈 $0.9$ 倍比例关系。

**图2 VDCOL 特性曲线**
**Fig. 2 Characteristic curve of VDCOL**

2 不同控制方