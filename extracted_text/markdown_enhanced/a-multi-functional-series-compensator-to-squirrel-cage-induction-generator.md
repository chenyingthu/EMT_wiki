## 适用于鼠笼异步发电机的多功能串联补偿器
姜飞，涂春鸣，帅智康，侯尊，刘子维，郭祺
（国家电能变换与控制工程技术研究中心（湖南大学），湖南省长沙市 410082）

### A Multi-Functional Series Compensator to Squirrel Cage Induction Generator
JIANG Fei, TU Chunming, SHUAI Zhikang, HOU Zun, LIU Ziwei, GUO Qi
(National Electric Power Conversion and Control Engineering Technology Research Center (Hunan University), Changsha 410082, Hunan Province, China)

**ABSTRACT.** To enhance low-voltage ride through (LVRT) capability of squirrel cage induction generator (SCIG), a multi-functional series compensator (MFSC) is proposed. MFSC is connected in series with SCIG stator to grid connection point. MFSC has multiple functions, such as LVRT capability improvement of wind farm during faults, fast voltage recovery at point of common coupling after faults and fault-current limiting. By analyzing SCIG working mechanism, mathematic models of MFSC are established under different modes. In addition, control strategies and operational algorithm for different modes are provided. Control strategies of thyristors are presented briefly. Finally, effectiveness of multiple functions of MFSC is verified with PSCAD/EMTDC simulation.
**KEY WORDS:** squirrel cage induction generator; multi-function; series compensator; LVRT

**摘要：** 为改善鼠笼型异步风电机（squirrel cage induction generator, SCIG）的低电压穿越能力，提出了一种适用于SCIG的多功能串联补偿器（multi-functional series compensator, MFSC）。MFSC可连接于风机定子与并网点之间，能够实现风电场低电压穿越、故障后风机并网点电压快速恢复、系统短路故障限流等多种功能。通过分析电网故障下的SCIG风机工作特性，给出了MFSC功能实现的数学模型；重点介绍了MFSC的不同功能控制策略、多模式切换流程及新增晶闸管控制短路支路优化控制策略。采用PSCAD/EMTDC软件建立了仿真系统，仿真结果验证了MFSC多种功能应用的有效性。
**关键词：** 鼠笼型异步风电机；多功能；串联补偿器；低电压穿越
**DOI:** 10.13335/j.1000-3673.pst.2015.12.010
**基金项目：** 国家自然科学基金项目（51377051）。

## 0 引言
近年来，随着风电装机容量在电力系统所占比重不断增大[1]，并网风电机组与系统的交互影响不容忽视[2]。统计发现，已建成的风电场中还存在着大量较早投产的异步风机，这些机组生产时并未考虑低电压穿越（low-voltage ride through, LVRT）技术[3-4]。为保障电网安全稳定运行，国家电监会明确规定风电场必须进行LVRT改造[5]。
常用风电机组中永磁直驱同步发电机和双馈异步风电机均可通过改进变换器控制或简单自身拓扑结构实现LVRT功能。但鼠笼异步发电机（squirrel cage induction generator, SCIG）由于定子侧直接与电网连接，缺乏对转矩和转速的有效控制，系统故障产生的电磁转矩波动将对风机齿轮箱等机械部件造成冲击[5]；其在故障消除后的系统电压恢复过程中需吸收大量无功，引起机端出口电压进一步降低[6]，所导致的发电机转子转速飞升是此类机组脱网的主要原因。
国内外学者对于SCIG型风机的低电压穿越技术已经有较多研究。传统桨距控制调节可减少输入机械功率，限制转速上升[7]。但变桨距调节缓慢，对于风电机组故障穿越作用有限，且转速上升使得电机吸收无功增大，将导致电网电压恶化[8]。静止无功补偿器（static var compensator, SVC）、静止同步补偿器（static synchronous compensator, STATCOM）、超级电容等[9-11]在电压跌落期间投入运行，可为故障期间的风电机组提供无功支持，有助于实现LVRT功能。文献[12]表明同容量STATCOM在维持节点电压、暂稳定极限及阻尼效果上明显优于SVC，但故障期间的低电压限制了无功补偿能力发挥，且在短路容量较大的系统中无功补偿效果并不理想。动态电压调节器（dynamic voltage restorer, DVR）串联于风电机组与电网之间，能够保持机端电压恒定；但正常运行时的器件损耗不容忽视，尤其故障期间系统快速上升的短路电流易造成功率器件损坏[6,13]，且直流侧需安装耗能元件，如卸荷电阻。通过串、并联制动电阻可有效改善风电场稳定性[14]。串联制动电阻（series braking resistors, SBR）作用发挥依赖电流大小而非电压大小，其在低电压环境下机端电压恢复、机组暂态稳定性能力更加突出[15-17]；但制动电阻切入时间受开关动作时间限制，过晚切除也可能导致电阻箱发热严重，缩短设备寿命。
考虑到单种技术提高风电机组LVRT能力的局限性，联合补偿方法将成为一个研究方向。文献[18]提出了采用可控硅串联补偿器（thyristor controlled series compensator, TCSC）和SVC的联合补偿技术，仿真表明此方案相比于单个设备具有更好效果。文献[4]提出一种串联限流电抗的无功补偿方案，可实现电压跌落时维持机端电压相对恒定和无功电流注入功能；但该方案中电抗器投切可能产生较大冲击，对风机本身将产生不良影响。文献[19]提出了采用电容器与静止无功补偿器构成混合无功补偿系统。以上联合补偿策略一定程度上提高了笼型异步风机暂态稳定性，但补偿方案涉及新增设备及多个...

$$P = \frac{U^2 (R_r/s)}{(R_s + R_r/s)^2 + (X_s + X_r)^2} \tag{1}$$
其中，转差率 $s$ 为
$$s = \frac{\omega_s - \omega_r}{\omega_s} \tag{2}$$
$$Q = \frac{U^2 (X_s + X_r)}{(R_s + R_r/s)^2 + (X_s + X_r)^2} \tag{3}$$
由式（1）—（3）可知，考虑到发电方式下 $s<0$，因此异步风机输出的有功功率为正、无功功率为负。

### 1.1 故障期间分析
当电网发生故障后，风机并网点电压迅速降低，将使得SCIG型风机产生电磁转矩与机械转矩不平衡。由于风机转子运动方程
$$J \frac{d\omega_r}{dt} = T_m - T_e \tag{4}$$
式中：$T_m$ 为机械转矩；$T_e$ 为电磁转矩；$J$ 为发电机旋转模块的转动惯量；$\omega_r$ 为转子机械速度。电磁转矩可表示为
$$T_e = \frac{p U^2 (R_r/s)}{\omega_s \left[ (R_s + R_r/s)^2 + (X_s + X_r)^2 \right]} \tag{5}$$