---
title: "Optical Tolerance Analysis of the Multi-Beam Limb Viewing Instrument STEAMR"
type: source
authors: ['未知']
year: 2014
journal: "IEEE Transactions on Terahertz Science and Technology;2014;4;6;10.1109/TTHZ.2014.2361616"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/13&14/files/tec.2019.2939351.pdf.pdf"]
---

# Optical Tolerance Analysis of the Multi-Beam Limb Viewing Instrument STEAMR

**作者**: 
**年份**: 2014
**来源**: `13&14/files/tec.2019.2939351.pdf.pdf`

## 摘要

—In this paper, we report on an optical tolerance anal- ysis of the submillimeter atmospheric multi-beam limb sounder, STEAMR. Physical optics and ray-tracing methods were used to quantify and separate errors in beam pointing and distortion due to reﬂector misalignment and primary reﬂector surface deforma- tions. Simulations were performed concurrently with the manu- facturing of a multi-beam demonstrator of the relay optical system which shapes and images the beams to their corresponding receiver feed horns. Results from Monte Carlo simulations show that the inserts used for reﬂector mounting should be positioned with an overall accuracy better than 100 m ( 1/10 wavelength). Analyses of primary reﬂector surface deformations show that a deviation of magnitude 100 m can be tolerable before 

## 核心贡献


- 首次针对多像素光学系统开展机械公差分析，并将公差要求与制造工艺直接关联。
- 结合物理光学与光线追迹，量化分离反射镜失调与表面形变对波束指向的影响。
- 研制多波束中继光学演示样机，验证反射镜装配对准精度可控制在五十微米内。


## 使用的方法


- [[物理光学|物理光学]]
- [[光线追迹|光线追迹]]
- [[蒙特卡洛仿真|蒙特卡洛仿真]]
- [[公差分析|公差分析]]


## 涉及的模型


- [[steamr辐射计|STEAMR辐射计]]
- [[离轴ritchey-chrétien望远镜|离轴Ritchey-Chrétien望远镜]]
- [[中继光学反射镜组|中继光学反射镜组]]
- [[焦平面阵列|焦平面阵列]]
- [[线栅偏振器|线栅偏振器]]


## 相关主题


- [[光学公差分析|光学公差分析]]
- [[多波束成像|多波束成像]]
- [[亚毫米波大气探测|亚毫米波大气探测]]
- [[反射镜失调与表面形变|反射镜失调与表面形变]]
- [[仪器制造与装配验证|仪器制造与装配验证]]


## 主要发现


- 反射镜安装定位精度需优于一百微米，主镜表面形变运行中容差需小于三十微米。
- 焦平面附近光学元件对失调最敏感，该特性源于光束在此处的强离轴几何分布。
- 演示样机实测表明反射镜装配精度可达五十微米，有效验证了公差分析模型的正确性。



## 方法细节

### 方法概述

本文采用物理光学(Physical Optics, PO)与几何光线追迹(Ray Tracing)相结合的混合仿真方法，对亚毫米波多波束临边探测仪STEAMR进行系统级光学公差分析。通过蒙特卡洛统计方法量化反射镜失调（6自由度）和主反射镜表面形变对波束指向与畸变的影响。仿真与制造过程并行进行：利用GRASP软件基于物理光学和物理绕射理论(PTD)计算远场矢量方向图，使用ZEMAX进行高效光线追迹评估指向敏感性；对于表面形变，采用有限元法(FEM)模拟CFRP主镜在模具应力下的变形，并基于Zernike多项式描述彗差(coma)与像散(astigmatism)等光学像差。

### 数学公式


**公式1**: $$$Z_n^m(\rho,\theta) = R_n^m(\rho)\cos(m\theta)$$$

*Zernike多项式，用于描述主反射镜表面形变。其中$R_n^m(\rho)$为径向多项式，$n$为径向阶数，$m$为角向频率，用于表征彗差和像散等像差模式*


**公式2**: $$$\eta = \frac{\left|\iint_S \mathbf{E}_a \cdot \mathbf{E}_g^* \, dS\right|^2}{\iint_S |\mathbf{E}_a|^2 \, dS \cdot \iint_S |\mathbf{E}_g|^2 \, dS}$$$

*功率耦合系数，评估馈源喇叭口径场$\mathbf{E}_a$与基模高斯分布$\mathbf{E}_g$的匹配程度，文中要求该值$>98\%$*


**公式3**: $$$\sigma = \frac{UT + LT}{2}$$$

*蒙特卡洛仿真中扰动的标准差定义，$UT$和$LT$分别为上、下容差限（文中设$UT=LT$），扰动限制在$\pm\sigma$范围内（变量设为2）*


**公式4**: $$$\Theta_{point} = \arctan\left(\frac{\Delta y}{f_{eff}}\right)$$$

*指向误差角计算，$\Delta y$为光线在焦平面上的横向偏移，$f_{eff}$为系统等效焦距，用于评估反射镜失调导致的波束指向偏差*


### 算法步骤

1. 建立完整光学链模型：包含离轴Ritchey-Chrétien望远镜（M1-M2，CFRP材料）、6个铝制中继反射镜（M3-M6）、线栅偏振器(WGP)和两块焦平面阵列(FPA)，定义各反射镜局部坐标系并全局对齐于笛卡尔坐标系

2. 定义扰动参数：对每个反射镜的6个自由度（3维平移+3维旋转）施加随机扰动，安装接口采用三点球窝关节(ball-socket joints)模型，旋转失调幅度随反射镜尺寸线性缩放

3. 生成蒙特卡洛样本：从准随机正态分布（均值0，标准差$\sigma$）生成随机失调量，通过变量约束（设为2）将扰动限制在$\pm\sigma$范围内，总计生成3000个扰动系统样本

4. 指向误差快速评估：使用ZEMAX光线追迹，对每个样本的7条特征光线进行追迹，计算远场指向偏差，单批次10个样本约40分钟（4核处理器）

5. 波束畸变精确计算：对关键样本使用GRASP物理光学引擎，计算主反射镜远场矢量方向图，积分第一零值内立体角得到波束效率，评估方位向折叠方向图(ACAP)和极化平面倾斜误差

6. 表面形变专项分析：基于SolidWorks FEM模拟CFRP主镜（1.6m×0.8m）在模具应力下的变形，固定两点、第三点施力生成点云数据导入GRASP；同时叠加Zernike多项式描述的彗差和像散（幅值变化至100$\mu$m）评估光学性能退化

7. 统计分析与容差反演：基于3000次仿真结果统计指向误差与波束畸变的分布，确定满足垂直指向知识精度<10m和FWHM知识精度优于-26dB的机械容差限


### 关键参数

- **工作频率**: 323–357 GHz（中心频率约340 GHz，对应波长$\lambda\approx0.88$ mm）

- **波束数量**: 14个极化交织波束（7+7，通过WGP分离，极化方向$\pm45^{\circ}$）

- **主反射镜尺寸**: 1.6 m $\times$ 0.8 m（离轴非球面，CFRP材料）

- **蒙特卡洛样本数**: 3000次扰动系统

- **光线追迹配置**: 每系统7条特征光线，10系统批量处理耗时$\sim$40分钟

- **物理光学计算耗时**: 单波束单频点$\sim$12分钟，总计超过24天（3000系统）

- **安装方式**: 三点球窝关节定位，反射镜通过金属球与插座接口连接

- **观测距离**: 3325 km（临边探测模式，指向误差对应地面轨迹偏差）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 反射镜安装插入件定位精度蒙特卡洛分析 | 统计结果显示，为保证光学性能，反射镜安装插入件的整体定位精度需优于100 $\mu$m（约$\lambda/10$）。该容差适用于发射前的装配阶段，确保14个波束的相对指向满足R1-R4要求 | 该容差比传统单波束微波遥感器（通常要求$\lambda/20\sim\lambda/50$）更宽松，但针对多波束相对指向要求进行了优化，通过蒙特卡洛统计验证了可制造性 |

| 主反射镜表面形变容差分析 | 发射前（地面状态）可容忍100 $\mu$m量级的表面偏差；在轨运行期间，由于热环境变化和结构松弛，表面形变需严格控制在30 $\mu$m以内 | 运行中容差(30$\mu$m)比发射前(100$\mu$m)严格3.3倍，反映出发射载荷与在轨热稳定性的不同约束，确保在UT/LS区域大气参数反演精度 |

| 中继光学系统敏感度梯度分析 | 焦平面阵列(FPA)附近的光学元件（M5-M6）对失调最敏感，这是由于光束在此处具有强离轴几何特性（off-axis nature），导致小位移引起大指向误差 | 敏感度随光学元件与焦平面距离减小而显著增加，FPA附近元件的敏感度比望远镜主镜(M1-M2)高约1-2个数量级，因此FPA采用整体单块加工以避免内部失调 |

| 多波束演示样机机械验证 | 实际制造的中继光学演示样机（含FPA及两个反射镜M5-M6）经后装配机械测量，证实反射镜对准精度可达50 $\mu$m以内，优于仿真提出的100 $\mu$m容差要求 | 实测50$\mu$m比仿真容差收紧50%，验证了容差分析模型的保守性和正确性，证明铝制反射镜通过精密加工可实现所需精度 |



## 量化发现

- 反射镜安装定位精度硬性指标：优于100 $\mu$m（$< \lambda/10$ @ 340 GHz）
- 主反射镜在轨运行表面形变容差：峰谷值<30 $\mu$m（约$\lambda/30$）
- 指向知识精度要求：垂直方向<10 m（对应角度精度约3 $\mu$rad @ 3325 km）
- FWHM波束大小知识精度：优于-26 dB（对应相对误差<5%，满足反演算法要求）
- 馈源与高斯基模耦合效率：>98%（采用基模高斯近似计算远场）
- 蒙特卡洛仿真规模：3000次扰动系统，覆盖6自由度$\times$6反射镜=36维扰动空间
- 计算效率：光线追迹评估3000系统约需200 CPU小时，物理光学抽样验证约需600 CPU小时
- 实测对准精度：50 $\mu$m（演示样机），比仿真容差收紧50%，验证了制造工艺能力
- 波束分布：两组7波束，极化方向$\pm45^{\circ}$，垂直分离1.5 km和2.0 km（地面轨迹）


## 关键公式

### 反射镜安装容差限

$$$\Delta z_{RMS} < \frac{\lambda}{10} \approx 100~\mu\text{m}$$$

*基于蒙特卡洛统计结果（3000次扰动），确定反射镜插入件定位的均方根误差需小于波长的1/10，这是保证14波束相对指向精度的关键机械指标*

### Zernike表面形变模型

$$$W(\rho,\theta) = \sum_{n,m} \alpha_n^m Z_n^m(\rho,\theta)$$$

*用于描述主反射镜在制造应力（模具应变）和热载荷下的表面偏差，其中主要考虑彗差($Z_3^{\pm1}$)和像散($Z_2^{\pm2}$)项，系数$\alpha_n^m$幅值分析至100$\mu$m*



## 验证详情

- **验证方式**: 实验验证与仿真对比（硬件在环验证）
- **测试系统**: STEAMR中继光学多波束演示样机，包含焦平面阵列(FPA，整体铝制微加工)和两个铝制离轴反射镜（M5-M6），采用与飞行件相同的CFRP安装背板和三点球窝关节定位结构
- **仿真工具**: GRASP 9（物理光学仿真，PO/PTD混合算法）、ZEMAX（序列光线追迹）、SolidWorks Simulation（FEM形变分析）、高精度三坐标测量机（CMM，后装配机械测量）
- **验证结果**: 演示样机机械测量证实反射镜对准精度<50$\mu$m，验证了蒙特卡洛仿真提出的<100$\mu$m容差要求的正确性和保守性。FPA单件加工精度验证了作为整体单元可不考虑内部失调的假设。仿真与制造并行工程方法成功将光学要求转化为可实现的机械加工精度（~50$\mu$m量级），确认CFRP和铝制结构能满足亚毫米波光学公差要求
