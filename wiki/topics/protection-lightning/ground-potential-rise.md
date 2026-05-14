---
title: "地电位升 (Ground Potential Rise)"
type: topic
tags: [ground-potential-rise, gpr, grounding, lightning, fault-current]
created: "2026-05-02"
---

# 地电位升 (Ground Potential Rise)


```mermaid
graph TD
    subgraph Ncmp[地电位升 (Ground Potential Rise)]
        N0[0.1s: 1160V]
        N1[0.3s: 670V]
        N2[0.5s: 519V]
        N3[1.0s: 367V]
        N4[3.0s: 212V]
    end
```


## 核心原理详解

### 技术概述
地电位升是电力系统电磁暂态仿真领域的重要技术，对提高仿真精度和效率具有重要意义。

### 理论基础
该技术建立在严格的电磁场理论和电路分析基础之上，通过数学建模描述系统的动态行为。

### 核心机制
- **物理建模**：基于物理定律建立准确的数学模型
- **数值求解**：采用高效的数值算法求解系统方程
- **参数分析**：研究关键参数对系统性能的影响

### 技术优势
- 提高仿真精度和计算效率
- 支持复杂系统的详细分析
- 为工程设计和优化提供理论支撑

## 概述

地电位升(Ground Potential Rise, GPR)是指接地系统在故障电流或雷电流注入时，相对于远方大地的电位升高。GPR是电力系统接地设计的关键参数，直接影响人身安全、设备保护和通信系统干扰。

在电力系统暂态分析中，GPR是研究接地系统动态响应的核心指标。当变电站或发电厂发生接地故障时，故障电流通过接地网流入大地，由于土壤电阻的存在，接地网电位相对于远方零电位参考点升高，形成GPR。这种电位升会在接地网周围产生电位梯度，对站内外人员和设备构成安全威胁。

## 基本原理

### 产生机理

地电位升的产生机理源于电流在土壤中流动时产生的电压降。当电流$I$流入接地系统时，根据欧姆定律：

$$GPR = I \cdot R_g$$

其中：
- $I$: 接地故障电流或雷电流
- $R_g$: 接地系统的接地电阻

从电磁场理论角度分析，电流从接地导体注入土壤后，会在土壤中形成电流场。根据电流连续性方程和欧姆定律的微分形式：

$$\mathbf{J} = \sigma \mathbf{E}$$

其中$\mathbf{J}$为电流密度，$\sigma$为土壤电导率，$\mathbf{E}$为电场强度。电流场在土壤中的分布遵循拉普拉斯方程：

$$\nabla^2 \varphi = 0$$

接地电位升可以表示为从接地导体表面到无穷远处的线积分：

$$GPR = -\int_{\infty}^{S} \mathbf{E} \cdot d\mathbf{l} = \int_{\infty}^{S} \frac{\mathbf{J}}{\sigma} \cdot d\mathbf{l}$$

### 电流路径与分布

故障电流从接地点注入后，在土壤中呈半球形向外扩散。对于半球形接地极，等位面为同心半球面，电流密度随距离增加而减小：

$$J = \frac{I}{2\pi r^2}$$

电场强度分布为：

$$E = \frac{J}{\sigma} = \frac{\rho I}{2\pi r^2}$$

电位分布为：

$$\varphi(r) = \frac{\rho I}{2\pi r}$$

其中$\rho$为土壤电阻率，$r$为到接地点的距离。

对于实际接地网，电流分布更为复杂。接地网可视为由多段导体组成的网络，每段导体向周围土壤泄漏电流。总GPR为各段导体贡献的叠加：

$$GPR = \sum_{i=1}^{n} \int_{l_i} \frac{I_i \rho}{4\pi r_i} dl_i$$

### 电场分布特性

接地网周围的电场分布具有以下特性：

**近场区**（距离$r < r_{eq}$，$r_{eq}$为接地网等效半径）：
- 电场强度大，电位梯度陡
- 电位分布受接地网几何形状影响显著
- 等位线密集，跨步电压风险高

**远场区**（距离$r \gg r_{eq}$）：
- 电场强度近似按$1/r^2$衰减
- 电位分布趋近于半球形扩散模型
- 等位线稀疏，电位梯度小

接地网周围的电位分布可用以下经验公式近似：

$$\varphi(x) = GPR \cdot \left(1 - \frac{2}{\pi} \arctan\left(\frac{x}{h_{eff}}\right)\right)$$

其中$x$为距接地网边缘的水平距离，$h_{eff}$为等效深度参数，与接地网尺寸和埋深有关。

### 影响因素

- **接地电阻**: 接地电阻越小，相同故障电流下的GPR越低。接地电阻主要取决于接地网面积、导体尺寸、土壤电阻率等因素。

- **故障电流**: 故障电流幅值直接决定GPR大小。三相短路、单相接地故障、雷电冲击等不同工况下电流幅值差异很大。

- **土壤电阻率**: 高阻土壤（如岩石、干燥砂土）导致GPR显著升高。土壤电阻率受含水量、温度、化学成分等因素影响。

- **接地网面积**: 接地网面积越大，与土壤的接触面积越大，接地电阻越小，GPR相应降低。

- **土壤分层结构**: 多层土壤条件下，电流分布受各层电阻率差异影响，可能出现电流屏蔽效应或集聚效应。

## 计算方法

### 简单计算

#### 半球形接地极模型

对于简单近似，可采用半球形接地极模型。假设接地系统等效为半径$r$的半球，埋设于均匀土壤中：

$$GPR = \frac{\rho I}{2\pi r}$$

其中：
- $\rho$: 土壤电阻率（$\Omega \cdot m$）
- $r$: 等效半球半径（m）
- $I$: 注入电流（A）

等效半径可按下式估算：

$$r = \sqrt{\frac{A}{\pi}}$$

其中$A$为接地网面积。

#### 平板接地极模型

对于浅埋圆形平板，接地电阻计算公式为：

$$R_g = \frac{\rho}{4r} + \frac{\rho}{4\pi h} \ln\left(\frac{4h}{r}\right)$$

其中$h$为埋深。

#### 垂直接地极

单根垂直接地极的接地电阻：

$$R_g = \frac{\rho}{2\pi L} \left(\ln\left(\frac{4L}{d}\right) - 1\right)$$

其中$L$为接地极长度，$d$为等效直径。

### 详细计算

#### 接地网模型

对于复杂接地网，需要采用分段导体模型。将接地网分解为$n$段导体，每段导体看作一个电极单元。定义：

- 自导纳$Y_{ii}$：第$i$段导体流入单位电流时在本段产生的电位
- 互导纳$Y_{ij}$：第$j$段导体流入单位电流时在第$i$段产生的电位

接地网导纳矩阵为：

$$\mathbf{Y} = \begin{bmatrix} Y_{11} & Y_{12} & \cdots & Y_{1n} \\ Y_{21} & Y_{22} & \cdots & Y_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ Y_{n1} & Y_{n2} & \cdots & Y_{nn} \end{bmatrix}$$

电位-电流关系为：

$$\mathbf{\varphi} = \mathbf{Z} \cdot \mathbf{I} = \mathbf{Y}^{-1} \cdot \mathbf{I}$$

其中$\mathbf{Z}$为阻抗矩阵。

#### 互阻计算

两段导体之间的互阻可采用以下公式计算：

$$R_{ij} = \frac{\rho}{4\pi l_i l_j} \int_{l_i} \int_{l_j} \frac{1}{|\mathbf{r}_i - \mathbf{r}_j|} dl_i dl_j$$

对于平行导体，互阻有解析解；对于任意布置的导体，需要采用数值积分。

#### 电流分布计算

已知总注入电流$I_{total}$和电流分配系数$\alpha_i$，各导体电流为：

$$I_i = \alpha_i I_{total}$$

电流分配系数满足约束：

$$\sum_{i=1}^{n} \alpha_i = 1$$

根据接地网等电位假设，各段导体电位相等且等于GPR：

$$\varphi_i = GPR, \quad i = 1, 2, \ldots, n$$

通过求解线性方程组获得电流分布。

#### 电位分布计算

地表任意点$P(x, y)$的电位为各导体贡献的叠加：

$$\varphi_P = \sum_{i=1}^{n} I_i R_{iP}$$

其中$R_{iP}$为第$i$段导体到点$P$的互阻。

### 计算机仿真

#### CDEGS软件

`cdeg` - CDEGS（Current Distribution, Electromagnetic fields, Grounding and Soil structure）是专业的接地分析软件，包含以下模块：

- **RESAP**: 土壤电阻率分析和分层建模
- **FCDIST**: 故障电流分布计算
- **MALZ**: 接地网阻抗和电位分布分析
- **HIFREQ**: 高频接地阻抗分析

CDEGS采用矩量法求解积分方程，可处理复杂土壤分层结构和接地网几何。

#### EMT仿真

在[[emtp]]或[[pscad-emtdc]]中进行暂态GPR仿真时：

**接地网频域模型**:

$$Z_g(f) = R_g + j2\pi f L_g + \frac{1}{j2\pi f C_g}$$

其中$R_g$、$L_g$、$C_g$分别为接地网等效电阻、电感、电容。

**时域实现**:

采用有理函数拟合或矢量拟合方法，将频域阻抗转换为时域等效电路：

$$Z_g(s) = R_0 + \sum_{i=1}^{N} \frac{R_i}{s - p_i}$$

对应时域支路方程：

$$v(t) = R_0 i(t) + \sum_{i=1}^{N} v_i(t)$$

$$\frac{dv_i}{dt} = p_i v_i + R_i i$$

#### 有限元法

对于复杂几何和土壤结构，可采用有限元法求解：

**控制方程**:

$$-\nabla \cdot (\sigma \nabla \varphi) = 0$$

**边界条件**:
- 接地导体表面：等电位边界
- 远场边界：$\varphi = 0$（Dirichlet条件）或$\frac{\partial \varphi}{\partial n} = 0$（Neumann条件）

**离散形式**:

$$\mathbf{K} \cdot \mathbf{\varphi} = \mathbf{F}$$

其中$\mathbf{K}$为刚度矩阵，$\mathbf{F}$为源项向量。

## 安全限值

### 人身安全准则

#### 人体电流耐受

人体能够承受的电流取决于电流路径、幅值和持续时间。心室纤维性颤动阈值由以下公式描述：

$$I_b = \frac{0.116}{\sqrt{t}} \quad \text{(50kg人体)}$$

$$I_b = \frac{0.157}{\sqrt{t}} \quad \text{(70kg人体)}$$

其中$t$为电流持续时间（s），$I_b$为人体电流（A）。

#### 接触电压允许值

`touch-voltage` - 接触电压定义为人体同时接触接地设备和远处大地时承受的电压。

IEEE 80标准给出的接触电压允许值计算公式：

$$E_{touch} = \frac{0.116 \cdot (R_F + 1.5\rho_s)}{\sqrt{t}}$$

其中：
- $R_F$：人体电阻，通常取1000$\Omega$
- $\rho_s$：表层土壤电阻率
- $1.5\rho_s$：考虑鞋袜和脚电阻的等效电阻

#### 跨步电压允许值

`step-voltage` - 跨步电压定义为人体两脚站在不同电位点时的电压差。

跨步电压允许值：

$$E_{step} = \frac{0.116 \cdot (R_F + 6\rho_s)}{\sqrt{t}}$$

系数6来源于两脚串联时等效接触面积的变化。

#### 安全限值表

| 故障持续时间 | 接触电压限值(50kg) | 跨步电压限值(50kg) |
|-------------|-------------------|-------------------|
| 0.1s | 1160V | 3867V |
| 0.3s | 670V | 2233V |
| 0.5s | 519V | 1730V |
| 1.0s | 367V | 1223V |
| 3.0s | 212V | 707V |

### 设备保护要求

#### 二次设备耐压

二次设备（保护、测量、控制设备）对GPR的耐受能力有限。典型要求：

- 二次回路对地绝缘强度：2kV工频/1min
- 信号回路耐压：500V~1000V
- 通信接口耐压：通常<100V

当GPR超过设备耐压时，需要通过以下措施保护：

- **隔离变压器**：阻断地电位传导路径
- **光隔离器**：实现电气隔离
- **浪涌保护器**：限制过电压幅值
- **屏蔽电缆**：减少电磁感应

#### 通信设备保护

通信设备对GPR尤为敏感。变电站与通信站之间的地电位差可能损坏通信设备。

保护措施包括：

- **光缆替代**：采用光纤通信消除地电位影响
- **隔离变压器**：用于音频和数据通信线路
- **中和变压器**：用于同轴电缆系统
- **气体放电管**：提供过电压保护

#### 绝缘配合

[[insulation-coordination]] - 绝缘配合确保设备绝缘水平与系统过电压相匹配。

变电站设备绝缘水平应满足：

$$BIL > k_s \cdot GPR_{max}$$

其中：
- $BIL$：基本冲击绝缘水平
- $k_s$：安全系数，通常取1.2~1.5
- $GPR_{max}$：最大预期GPR

## 暂态GPR分析

### 雷电GPR

[[lightning-overvoltage]] - [[lightning-transient-analysis]]

雷电注入接地系统时产生的暂态GPR具有幅值高、持续时间短的特点。

#### 冲击接地阻抗

冲击接地阻抗与工频接地电阻不同，主要差异源于：

- **土壤电离**：高电场强度下土壤击穿，等效电阻率降低
- **电感效应**：高频下接地导体电感不可忽略
- **电容效应**：快速暂态下电容电流贡献显著

冲击接地阻抗的频域表达式：

$$Z_{impulse}(s) = R_g + sL_g + \frac{1}{sC_g}$$

#### 火花效应

当电流密度超过土壤击穿阈值时，发生土壤电离：

$$E_{crit} \approx 300 \text{~} 1000 \text{ kV/m}$$

电离导致接地极等效半径增大：

$$r_{eff} = r_0 \sqrt{1 + \frac{\rho I}{2\pi r_0^2 E_{crit}}}$$

等效半径增大使冲击接地阻抗降低：

$$R_{impulse} = \frac{\rho}{2\pi r_{eff}}$$

#### 雷电GPR计算

雷电GPR峰值可表示为：

$$GPR_{max} = \eta \cdot I_{peak} \cdot R_{impulse}$$

其中：
- $I_{peak}$：雷电流峰值
- $\eta$：衰减系数，考虑引线电感和接地体电感的影响
- $R_{impulse}$：冲击接地阻抗

### 故障GPR

`ground-fault` - [[ac-fault-transient-analysis]]

工频接地故障产生的GPR持续时间较长，热效应显著。

#### 工频故障电流

单相接地故障电流：

$$I_f = \frac{3V_{ph}}{Z_1 + Z_2 + Z_0 + 3R_g}$$

其中$Z_1$、$Z_2$、$Z_0$分别为正序、负序、零序阻抗。

#### 故障持续时间

故障持续时间取决于保护动作时间：

$$t_{clear} = t_{relay} + t_{breaker}$$

其中：
- $t_{relay}$：继电器动作时间（通常20~100ms）
- $t_{breaker}$：断路器开断时间（通常50~100ms）

#### 热稳定校验

接地导体应能承受故障电流的热效应：

$$I_f^2 \cdot t_{clear} \leq I_{thermal}^2 \cdot t_{rated}$$

其中$I_{thermal}$为导体热稳定电流。

### 暂态测量

#### 暂态测量系统

高速暂态GPR测量需要：

- **宽带分压器**：带宽>10MHz
- **高速示波器**：采样率>100MS/s
- **光纤隔离**：消除地电位对测量系统的影响

#### 测量方法

**电流注入法**：
- 使用冲击电流发生器产生标准波形的注入电流
- 测量接地网电位响应
- 计算冲击接地阻抗

**自然雷电测量**：
- 在雷电季节记录自然雷击数据
- 获取真实的雷电GPR波形
- 统计分析雷电参数

## 降低GPR的措施

### 降低接地电阻

[[grounding-system]]

#### 扩大接地网面积

接地电阻与接地网面积近似关系：

$$R_g \approx \frac{\rho}{4}\sqrt{\frac{\pi}{A}} + \frac{\rho}{L_{total}}$$

扩大接地网面积可有效降低接地电阻。当面积扩大为原来的4倍时，接地电阻约降低50%。

#### 深埋接地

利用深层低阻土壤：

- 垂直接地极深入地下水位
- 深井接地（深度可达100m以上）
- 适用于表层土壤电阻率高的情况

深井接地电阻：

$$R_{well} = \frac{\rho}{2\pi L} \ln\left(\frac{2L}{d}\right)$$

#### 降阻剂

化学降阻剂改善土壤导电性：

- **膨润土**：天然粘土矿物
- **导电混凝土**：掺入导电材料的混凝土
- **电解离子接地极**：持续释放电解质

降阻效果：

$$\rho_{eff} = \frac{\rho}{1 + k \cdot C}$$

其中$C$为降阻剂浓度，$k$为系数。

#### 外部接地极

将接地网与外部低阻区域连接：

- **水下接地**：利用河流、湖泊
- **远方接地**：通过电缆连接远处接地网
- **共用接地**：多站共用接地系统

### 均衡电位

#### 均压带设计

在接地网上方铺设均压带（碎石层或沥青层）：

- **碎石层**：提高表层电阻率，减小接触电流
- **厚度**：通常10~15cm
- **电阻率要求**：$\rho_s > 3000 \Omega \cdot m$

均压带效果：

$$E_{touch,eff} = E_{touch} \cdot \frac{\rho_s}{\rho_s + 1.5\rho}$$

#### 等电位连接

将所有设备外壳、金属构件与接地网可靠连接：

- **等电位母排**：主接地母线
- **分支连接**：各设备接地引线
- **连接要求**：低阻抗、可靠连接

#### 区域隔离

在高GPR区域与低电位区域之间设置隔离：

- **绝缘隔离**：通信线路绝缘段
- **物理隔离**：保持安全距离
- **时间隔离**：故障期间切断敏感回路

### 转移电位

#### 远距离电位转移

通过金属导体将电位转移到远处：

- **架空地线**：将故障电流分流到远端
- **电缆金属护套**：提供低阻抗并联路径
- **接地导体**：连接相邻接地网

转移电位计算：

$$GPR_{remote} = GPR_{local} \cdot \frac{Z_{transfer}}{Z_{transfer} + Z_{remote}}$$

#### 通信线路保护

保护通信线路免受转移电位影响：

- **光缆替代**：消除金属导体
- **隔离变压器**：阻断工频电流
- **中和变压器**：平衡对地阻抗

#### 管道电位控制

金属管道受GPR影响可能产生：

- **腐蚀**：直流电流导致电化学腐蚀
- **安全**：管道与地之间高电压

保护措施：

- **绝缘接头**：隔离管道与接地网
- **排流装置**：提供低阻抗泄放路径
- **阴极保护**：补偿腐蚀电流

## 与EMT仿真的结合

### 接地网建模

[[grounding-system-modeling]]

#### 分布参数模型

将接地网划分为多个单元，每个单元用集总参数表示：

- **自阻抗**：$Z_{ii} = R_{ii} + \mathrm{j}\omega L_{ii}$
- **互阻抗**：$Z_{ij} = R_{ij} + \mathrm{j}\omega L_{ij}$
- **对地导纳**：$Y_{i0} = G_{i0} + \mathrm{j}\omega C_{i0}$

导体分段原则：

- 每段长度：$\Delta l < \lambda/10$，$\lambda$为最小波长
- 对于50Hz工频：$\Delta l < 60$km
- 对于雷电波（1$\mu$s上升沿）：$\Delta l < 30$m

#### 频变特性

高频下接地阻抗呈感性：

$$Z_g(f) = R_g \sqrt{1 + \left(\frac{f}{f_c}\right)^2}$$

其中$f_c$为特征频率，取决于接地网尺寸和土壤参数。

#### 土壤分层模型

多层土壤的等效电阻率：

$$\rho_{eq} = \frac{\sum_{i=1}^{n} \rho_i h_i}{\sum_{i=1}^{n} h_i}$$

对于两层土壤，采用镜像法计算：

$$R_g = \frac{\rho_1}{4\pi r} + \frac{\rho_1}{4\pi} \sum_{n=1}^{\infty} K^n \left(\frac{1}{r_n^+} - \frac{1}{r_n^-}\right)$$

其中$K = (\rho_2 - \rho_1)/(\rho_2 + \rho_1)$为反射系数。

### 故障仿真

#### 故障电流模型

在[[ac-fault-transient-analysis]]仿真中，接地故障模型：

$$I_f(t) = \sqrt{2}I_{rms}\left[\sin(\omega t + \phi) - \sin(\phi)e^{-t/\tau}\right]$$

其中：
- $I_{rms}$：故障电流有效值
- $\phi$：故障合闸角
- $\tau$：直流衰减时间常数

#### 电位分布计算

EMT仿真输出各节点电压后，地表电位分布：

$$\varphi(x, y, t) = \sum_{i} I_i(t) \cdot R_i(x, y)$$

#### 跨步电压和接触电压提取

仿真后处理计算：

$$E_{step}(t) = \varphi(x_1, y_1, t) - \varphi(x_2, y_2, t)$$

$$E_{touch}(t) = \varphi_{equipment}(t) - \varphi(x_{hand}, y_{hand}, t)$$

### 雷电仿真

`transient-ground-impedance`

#### 雷电流模型

常用双指数波形：

$$i(t) = I_{peak} \left(e^{-\alpha t} - e^{-\beta t}\right)$$

参数：
- 标准雷电波：$\alpha = 1.4 \times 10^4$ s$^{-1}$，$\beta = 4.6 \times 10^6$ s$^{-1}$
- 对应1.2/50$\mu$s波形

#### 非线性接地模型

考虑土壤电离的非线性电阻：

$$R(I) = \frac{R_0}{\sqrt{1 + (I/I_{crit})^n}}$$

其中：
- $R_0$：小电流时的接地电阻
- $I_{crit}$：电离起始电流
- $n$：非线性系数，通常取2~4

#### 雷电暂态分析流程

1. 建立接地网EMT模型
2. 设置雷电流注入点
3. 运行暂态仿真
4. 提取GPR波形
5. 分析峰值、波形、能量

## 多站点影响分析

### 站间GPR

#### 输电线路影响

故障时，两变电站通过输电线路耦合：

- **地线传导**：架空地线提供低阻抗路径
- **电容耦合**：线路对地电容形成分压
- **互感耦合**：零序电流产生互感电压

站间电位差：

$$\Delta GPR = GPR_1 - GPR_2 = I_g \cdot (Z_{g1} - Z_{g2})$$

其中$I_g$为经地线传输的电流。

#### 地线分流

架空地线可显著降低GPR：

$$GPR_{eff} = GPR_0 \cdot \frac{R_g}{R_g + Z_{gw}}$$

其中$Z_{gw}$为地线等效阻抗。

### 通信干扰

#### 感应干扰

故障电流产生的磁场在通信线路上感应电压：

$$V_{ind} = \mathrm{j}\omega M \cdot I_f \cdot l$$

其中：
- $M$：互感系数
- $l$：平行长度

#### 传导干扰

地电位差直接传导到通信线路：

$$V_{con} = GPR_1 - GPR_2$$

#### 保护措施

- **光缆通信**：根本消除电磁感应
- **屏蔽电缆**：减少感应耦合
- **接地排流**：提供低阻抗泄放路径

## 测量方法

### 现场测量

`fall-of-potential` - `high-voltage-measurement`

#### 电位降法

测量接地电阻的经典方法：

1. 在接地网注入测试电流$I_{test}$
2. 测量电位探针电压$V$
3. 计算接地电阻：$R_g = V/I_{test}$

电位探针位置：

- 远离接地网：距离$d \geq 5\sqrt{A}$
- 避开电流极影响区
- 等位线平坦区域

#### 夹钳法

不断开接地连接的情况下测量：

- 适用于多点接地系统
- 测量并联支路电流
- 需要已知部分支路电阻

原理：

$$R_x = \frac{V_{clamp}}{I_{injected}} \cdot \frac{R_{known}}{R_{known} + R_x}$$

#### 异频测量

采用非工频（如128Hz）测试信号：

- 避免工频干扰
- 提高信噪比
- 适用于变电站强电磁环境

### 暂态测量

#### 冲击电流测试

使用冲击电流发生器：

- 电流幅值：100A~10kA
- 波形：8/20$\mu$s或10/350$\mu$s
- 测量冲击接地阻抗

#### 高速数据采集

暂态GPR测量要求：

- 采样率：>10MS/s
- 带宽：>5MHz
- 分辨率：>12bit

#### 光纤隔离测量

消除地电位对测量设备的影响：

- **有源光纤探头**：信号数字化后传输
- **无源光纤探头**：利用电光效应
- **隔离度**：>100dB

## 标准规范

### IEEE 80标准

IEEE Std 80《IEEE Guide for Safety in AC Substation Grounding》是变电站接地设计的主要标准。

#### 主要内容

- 人身安全准则（接触电压、跨步电压限值）
- 接地网设计方法
- 接地电阻计算
- 电位分布计算
- 测量方法

#### 设计流程

1. 确定最大接地故障电流
2. 计算接地电阻
3. 计算GPR
4. 校核接触电压和跨步电压
5. 必要时修改设计

#### 安全电压限值

IEEE 80-2013采用的简化公式：

$$E_{touch70} = \frac{0.157 \cdot C_s \cdot (1000 + 1.5C_s\rho_s)}{\sqrt{t_s}}$$

$$E_{step70} = \frac{0.157 \cdot C_s \cdot (1000 + 6C_s\rho_s)}{\sqrt{t_s}}$$

其中$C_s$为表层衰减系数：

$$C_s = 1 - \frac{0.09(1 - \rho/\rho_s)}{2h_s + 0.09}$$

### IEC 61936标准

IEC 61936-1《Power installations exceeding 1 kV a.c.》规定了电力装置的接地要求。

#### 主要规定

- 接地电阻一般要求：<2$\Omega$（大接地电流系统）
- 接地导体截面要求
- 连接和焊接要求
- 测量和验证要求

#### 与IEEE 80的差异

- 采用不同的安全电压限值计算方法
- 考虑不同的体重假设
- 欧洲标准更注重风险评估

### 其他相关标准

- **IEEE 81**: 接地系统测量指南
- **IEEE 837**: 变电站接地连接标准
- **IEC 62305**: 雷电防护
- **GB/T 50065**: 中国交流电气装置接地设计规范

## 相关主题

- [[grounding-system]] - 接地系统
- `touch-voltage` - 接触电压
- `step-voltage` - 跨步电压
- [[earth-return-impedance]] - 地回路阻抗
- [[grounding-system-modeling]] - 接地系统建模
- [[ac-fault-transient-analysis]] - 故障暂态
- [[lightning-transient-analysis]] - 雷电暂态分析
- [[lightning-overvoltage]] - 雷电过电压
- `ground-fault` - 接地故障
- `transient-ground-impedance` - 暂态接地阻抗
- [[insulation-coordination]] - 绝缘配合
- `safety-criteria` - 安全标准
- `fall-of-potential` - 电位降法
- `high-voltage-measurement` - 高压测量
- `cdeg` - CDEGS软件
- [[emtp]] - EMTP仿真

## 来源论文

| 论文 | 年份 |
|------|------|
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[ground-potential-rise-in-wind-farms-due-to-direct-lightning|Ground Potential Rise in Wind Farms due to Direct Lightning]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |
## 来源论文

| 论文 | 年份 |
|------|------|
| [[evaluation-of-the-impact-of-different-transmission-line-models-on-electromagneti|Evaluation of the impact of different transmission line mode]] | 2018 |
| [[computation-of-ground-potential-rise-and-grounding-impedance-of-simple-arrangeme|Computation of ground potential rise and grounding impedance]] | 2021 |
| [[ground-potential-rise-in-wind-farms-due-to-direct-lightning|Ground Potential Rise in Wind Farms due to Direct Lightning]] | 2021 |
| [[performance-of-the-recursive-methods-applied-to-compute-the-transient-responses-|Performance of the recursive methods applied to compute the ]] | 2021 |