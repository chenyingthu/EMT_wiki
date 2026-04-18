---
title: "Modelling of Single-Phase Nonuniform Transmission Lines in Electromagnetic Transient Simulations - Power Delivery, IEEE Transactions on"
type: source
authors: ['IEEE']
year: 2004
journal: ""
tags: ['transmission-line']
created: "2026-04-13"
sources: ["EMT_Doc/27&28/Modelling of single-phase nonuniform transmission lines in electromagnetic transient simulations.pdf"]
---

# Modelling of Single-Phase Nonuniform Transmission Lines in Electromagnetic Transient Simulations - Power Delivery, IEEE Transactions on

**作者**: IEEE
**年份**: 2004
**来源**: `27&28/Modelling of single-phase nonuniform transmission lines in electromagnetic transient simulations.pdf`

## 摘要

An exponential single-phase line model is introduced to represent nonuniform transmission lines, When the line parameters are assumed to vary exponentially, a set of two- port equations can be formed in the frequency domain, which contain frequency-dependent functions. These func- tions are then synthesized with rational functions of the minimum-phase-shift type. Utilizing a fast recursive con- volution technique, the time-domain equations of the pro- posed model reduce to a form similar to those in Bergeron's method. Thus, the model is compatible with general elec- tromagnetic transients programs such as the EMTP El]. Time-domain simulations with the proposed model show good agreement with published experimental results, and with those produced by a cascade multi-section model, where the 

## 核心贡献


- 提出基于参数指数变化假设的单相非均匀线路频域二端口模型
- 采用最小相移型有理函数综合频变特性，实现时域快速递归卷积
- 推导出类Bergeron形式的时域等效电路，可直接兼容EMTP程序


## 使用的方法


- [[有理函数综合|有理函数综合]]
- [[快速递归卷积|快速递归卷积]]
- [[transmission-line-model|Bergeron线路模型]]
- [[频域二端口建模|频域二端口建模]]


## 涉及的模型


- [[单相非均匀输电线路|单相非均匀输电线路]]
- [[指数变化线路模型|指数变化线路模型]]
- [[级联多段均匀线路模型|级联多段均匀线路模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关建模|频率相关建模]]
- [[时域行波仿真|时域行波仿真]]
- [[emtp兼容建模|EMTP兼容建模]]


## 主要发现


- 时域仿真结果与已发表实验数据高度吻合，验证了模型准确性
- 模型计算结果与级联多段均匀线路模型一致，且计算效率更高
- 有理函数综合的幅频与相频特性曲线与精确解几乎完全重合



## 方法细节

### 方法概述

该论文提出了一种基于指数参数变化的单相非均匀传输线建模方法。核心思想是假设线路的单位长度串联阻抗$Z(x)$和并联导纳$Y(x)$沿线路长度呈指数变化，即$L(x)=L_0e^{qx}$和$C(x)=C_0e^{-qx}$。在此假设下，频域波动方程可解析求解，得到包含频变函数（特征阻抗$Z_c$和传播函数$A$）的二端口方程。通过最小相移型有理函数（实数负极点和零点）对这些频变函数进行有理函数综合（rational function synthesis），然后利用快速递归卷积技术（fast recursive convolution）将频域卷积转换为时域指数函数求和，最终推导出与Bergeron方法形式相似的时域等效电路方程，实现与EMTP等电磁暂态仿真程序的兼容。

### 数学公式


**公式1**: $$$-\frac{dV}{dx} = Z(x)I$$$

*频域传输线电压方程，V和I为电压电流相量，Z(x)为空间相关的单位长度串联阻抗*


**公式2**: $$$-\frac{dI}{dx} = Y(x)V$$$

*频域传输线电流方程，Y(x)为空间相关的单位长度并联导纳*


**公式3**: $$$Z(x) = j\omega L_0 e^{qx}$$$

*指数变化串联阻抗，L0为x=0处电感值，q为指数变化系数*


**公式4**: $$$Y(x) = j\omega C_0 e^{-qx}$$$

*指数变化并联导纳，C0为x=0处电容值，变化方向与阻抗相反以保持波速恒定*


**公式5**: $$$\frac{d^2V}{dx^2} - q\frac{dV}{dx} - \frac{\omega^2}{c^2}V = 0$$$

*非均匀线波动方程，其中$c=1/\sqrt{L_0C_0}$为波速*


**公式6**: $$$\lambda_1 = \frac{q}{2} + \sqrt{(\frac{q}{2})^2 - (\frac{\omega}{c})^2}$$$

*特征方程的第一个根*


**公式7**: $$$\lambda_2 = \frac{q}{2} - \sqrt{(\frac{q}{2})^2 - (\frac{\omega}{c})^2}$$$

*特征方程的第二个根*


**公式8**: $$$[V_k + Z_{ck}(0)I_k]A = V_m + Z_{cm}(0)I_m$$$

*频域二端口传输方程，A为传播函数，Z_ck和Z_cm为两端特征阻抗*


**公式9**: $$$Z_{ck}(\omega) = \frac{j\omega L_0}{\lambda_2}$$$

*节点k处特征阻抗频域表达式*


**公式10**: $$$Z_{cm}(\omega) = \frac{j\omega L_0 e^{ql}}{\lambda_2}$$$

*节点m处特征阻抗频域表达式（l为线路长度）*


**公式11**: $$$[v_k(t) + z_{ck}(t) * i_k(t)] * a(t) = v_m(t) - z_{cm}(t) * i_m(t)$$$

*时域卷积形式方程，*表示卷积运算*


**公式12**: $$$v_m(t) = Z_{meq}i_m(t) + e_{h-m}(t)$$$

*类Bergeron形式的时域等效电路方程，Z_meq为等效阻抗，e_h-m为历史电压源*


**公式13**: $$$q = -\frac{1}{l}\ln\frac{Z_{highm}}{Z_{highk}}$$$

*指数变化系数计算公式，由两端高频特征阻抗确定*


### 算法步骤

1. 假设线路参数沿长度指数变化：根据线路两端的高频特征阻抗$Z_{highk}$和$Z_{highm}$，计算指数变化系数$q = -\frac{1}{l}\ln(Z_{highm}/Z_{highk})$

2. 建立频域波动方程：将$Z(x)=j\omega L_0 e^{qx}$和$Y(x)=j\omega C_0 e^{-qx}$代入传输线方程，得到二阶微分方程$\frac{d^2V}{dx^2} - q\frac{dV}{dx} - \frac{\omega^2}{c^2}V = 0$

3. 求解特征根：计算$\lambda_{1,2} = \frac{q}{2} \pm \sqrt{(\frac{q}{2})^2 - (\frac{\omega}{c})^2}$，得到电压通解$V(x) = C_1e^{\lambda_1 x} + C_2e^{\lambda_2 x}$

4. 推导二端口方程：应用边界条件$x=0$和$x=l$，建立两端电压电流关系$[V_k + Z_{ck}I_k]A = V_m + Z_{cm}I_m$，其中$A=e^{\lambda_1 l}$为传播函数

5. 有理函数综合：使用最小相移型有理函数（实数负极点和零点）分别综合特征阻抗$Z_{ck}(\omega)$、$Z_{cm}(\omega)$和传播函数$A(\omega)$的频变特性

6. 逆傅里叶变换：将综合后的频域有理函数转换为时域指数函数之和，得到$z_{ck}(t)$、$z_{cm}(t)$和$a(t)$的时域表达式，其中$a(t)$包含传播时延

7. 快速递归卷积：利用递归卷积算法计算时域卷积积分$z(t)*i(t)$，避免每一步长都进行完整卷积计算，提高计算效率

8. 构建Bergeron等效电路：将卷积结果整理为$v_m(t) = Z_{meq}i_m(t) + e_{h-m}(t)$形式，其中历史项$e_{h-m}(t)$由前一时间步的电压电流值递归计算得到

9. 双向建模：对从m到k的反向传输，使用$q'=-q$重新计算特征根和特征阻抗，建立反向传输方程$v_k(t) = Z_{keq}i_k(t) + e_{h-k}(t)$

10. EMTP接口实现：将等效电路以诺顿等效形式（电流源并联电阻）接口到EMTP等电磁暂态程序中


### 关键参数

- **line_length**: 50 m（示例线路长度）

- **Z_high_k**: 220 Ω（节点k处高频特征阻抗）

- **Z_high_m**: 150 Ω（节点m处高频特征阻抗）

- **q**: -0.00766（从k到m方向的指数变化系数，计算公式$q = -\frac{1}{50}\ln\frac{150}{220}$）

- **q_reverse**: 0.00766（从m到k方向的指数变化系数，数值相反）

- **L_0**: x=0处单位长度电感（具体数值未在摘录中给出）

- **C_0**: x=0处单位长度电容（具体数值未在摘录中给出）

- **c**: $1/\sqrt{L_0C_0}$波速



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 特征阻抗$Z_{ck}$频域综合 | 幅频特性和相频特性在$10^2$至$10^6$Hz范围内，有理函数综合结果与精确函数几乎完全重合（图3和图4），幅值误差小于视觉分辨精度（<1%），相位拟合精度高 | 与传统的高频近似方法[4]相比，在全频段内（包括低频）均保持高精度，而非仅在高频有效 |

| 传播函数$A$频域综合 | 幅值和相位综合曲线（图5和图6）与精确函数对比，拟合精度合理，轨迹追踪精确 | 优于级联多段模型在段数较少时的近似误差 |

| 传播函数$a(t)$时域验证 | 通过逆傅里叶变换得到的时域传播函数$a(t)$（图7），综合结果与精确曲线几乎完全相同（practically identical），验证了有理函数综合的时域精度 | 与精确解的时域误差可忽略不计 |

| 指数线路时域仿真 | 50m长指数线路（220Ω至150Ω）的暂态仿真结果与级联多段均匀线路模型结果一致，且计算效率更高 | 比级联多段模型计算速度更快（无需划分多段），同时保持相同精度 |

| 实验验证 | 时域仿真结果与已发表的实验数据（published experimental results）高度吻合 | 验证了模型的工程实用性和准确性 |



## 量化发现

- 指数变化系数$q$的计算精度：对于50m长、阻抗从220Ω变到150Ω的线路，$q = -0.00766$（精确到小数点后5位）
- 特征阻抗有理函数综合：在$10^2$-$10^6$Hz频率范围内，综合函数与精确函数的幅值偏差<1%，相位偏差<5°（根据图3-4目视估计）
- 传播时延：传播函数$a(t)$的时延近似等于最快频率分量沿线传播时间，即$\tau \approx l/c$
- 计算效率：相比级联多段均匀线路模型（cascade multi-section model），所提模型无需将线路划分为多个短段，减少了状态变量数量，计算速度提升显著（具体倍数未给出，但强调'fast'）
- 波速恒定：尽管线路参数$L(x)$和$C(x)$随位置变化，但乘积$L(x)C(x)=L_0C_0$为常数，因此波速$c=1/\sqrt{L_0C_0}$沿线路保持恒定
- 阻抗变化范围：示例中线路特征阻抗从220Ω指数变化到150Ω，变化比例为1.47:1


## 关键公式

### 指数线频域二端口方程

$$$[V_k + Z_{ck}(0)I_k]A = V_m + Z_{cm}(0)I_m$$$

*描述单相指数非均匀线两端电压电流关系，是模型的核心频域表达式，其中$A=e^{\lambda_1 l}$为传播函数，$Z_{ck}$和$Z_{cm}$为两端特征阻抗*

### 类Bergeron时域等效方程

$$$v_m(t) = Z_{meq}i_m(t) + e_{h-m}(t)$$$

*经过快速递归卷积后得到的时域形式，与EMTP中Bergeron线路模型格式兼容，便于程序实现，其中$e_{h-m}(t)$为历史电压源*

### 指数线波动方程

$$$\frac{d^2V}{dx^2} - q\frac{dV}{dx} - \frac{\omega^2}{c^2}V = 0$$$

*假设参数指数变化后得到的二阶常微分方程，是推导二端口方程的基础，其中$q$为指数变化系数，$c$为恒定波速*



## 验证详情

- **验证方式**: 多维度验证：1) 频域对比（精确函数vs有理函数综合结果）；2) 时域对比（逆傅里叶变换验证传播函数）；3) 与级联多段均匀线路模型对比；4) 与已发表的实验结果对比
- **测试系统**: 单相50m长指数非均匀输电线路，特征阻抗从220Ω（送端）指数变化到150Ω（受端），用于模拟输电线路塔的行波传播
- **仿真工具**: EMTP（电磁暂态程序）兼容接口，使用快速递归卷积算法和有理函数综合工具
- **验证结果**: 所提模型在频域和时域均表现出高精度：特征阻抗和传播函数的有理函数综合曲线与精确解几乎完全重合；时域传播函数$a(t)$与精确解几乎相同（practically identical）；与级联多段模型结果一致但计算效率更高；与已发表实验数据高度吻合。模型成功实现了非均匀传输线在EMTP中的高效精确仿真。
