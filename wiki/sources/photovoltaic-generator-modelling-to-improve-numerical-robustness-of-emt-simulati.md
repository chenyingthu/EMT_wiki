---
title: "Photovoltaic generator modelling to improve numerical robustness of EMT simulation"
type: source
authors: ['Anna', 'Rita', 'Di', 'Fazio']
year: 2011
journal: "Electric Power Systems Research, 83 (2011) 136-143. 10.1016/j.epsr.2011.10.013"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/31/j.epsr.2011.10.013.pdf.pdf"]
---

# Photovoltaic generator modelling to improve numerical robustness of EMT simulation

**作者**: Anna, Rita, Di 等
**年份**: 2011
**来源**: `31/j.epsr.2011.10.013.pdf.pdf`

## 摘要

1. Introduction When PV systems are included into the power system sim- ulation, the non-linearities present in the PV generator models In recent years the growing concern for environment preserva- require special attention. On one side, they cannot be neglected tion has caused a wide spreading o...

## 核心贡献


- 提出扩展线性系统技术将光伏非线性方程嵌入线性网络消除单步延迟引发的数值失稳
- 构建收敛性分析框架从数学层面证明新方法相比传统分离求解法的稳定性显著提升


## 使用的方法


- [[基本线性系统技术-blst|基本线性系统技术(BLST)]]
- [[扩展线性系统技术-elst|扩展线性系统技术(ELST)]]
- [[收敛性分析|收敛性分析]]
- [[节点分析法|节点分析法]]


## 涉及的模型


- [[光伏发电机|光伏发电机]]
- [[单二极管等效电路|单二极管等效电路]]
- [[ieee标准测试系统|IEEE标准测试系统]]
- [[并网逆变器|并网逆变器]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[数值稳定性|数值稳定性]]
- [[光伏系统建模|光伏系统建模]]
- [[局部阴影效应|局部阴影效应]]
- [[分布式发电|分布式发电]]


## 主要发现


- 扩展线性系统技术有效克服了传统方法在局部阴影或多二极管模型下的数值发散问题
- IEEE标准系统仿真验证表明新方法在电气故障与局部阴影工况下均能保持收敛稳定



## 方法细节

### 方法概述

论文提出扩展线性系统技术(ELST)以解决基本线性系统技术(BLST)在EMT仿真中的数值不稳定性问题。BLST将光伏发电机的非线性方程与电力系统线性方程分离求解，使用前一时步的电压值计算当前电流，引入单步延迟导致数值失稳，特别是在局部遮阴、多类型阵列或多电平逆变器接口等需使用多个单二极管等效电路的场景。ELST的核心思想是在保持计算效率的同时，通过将光伏模型在当前工作点的线性化表示（等效电导并联等效电流源）嵌入线性网络方程，消除单步延迟引起的误差，从而显著提高数值稳健性。

### 数学公式


**公式1**: $$$I_i(V_i) = I_g - I_o(e^{\beta V_i/a} - 1)$$$

*理想单二极管PV模型方程，描述光生电流$I_g$与二极管电流$I_d$的关系，其中$I_o$为反向饱和电流，$a$为理想因子，$\beta$为热电压倒数*


**公式2**: $$$\beta(T) = \frac{q}{M_s k T}$$$

*热电压倒数定义，$q$为电子电荷(1.60217646e-19 C)，$k$为玻尔兹曼常数(1.3806503e-23 J/K)，$M_s$为串联电池数，$T$为结温*


**公式3**: $$$I(V) = I_g - I_o(e^{\beta(V+R_s I)/a} - 1) - \frac{V+R_s I}{R_p}$$$

*实际PV模块单二极管等效电路方程，考虑串联电阻$R_s$和并联电阻$R_p$的非线性隐式方程，描述端电流$I$与端电压$V$的关系*


**公式4**: $$$a_{gen} = a, \quad I_{g,gen} = N_p I_g, \quad I_{o,gen} = N_p I_o$$$

*PV发电机参数缩放关系（部分），$N_p$为并联阵列数，$N_s$为串联模块数*


**公式5**: $$$R_{s,gen} = \frac{N_s}{N_p}R_s, \quad R_{p,gen} = \frac{N_s}{N_p}R_p, \quad \beta_{gen} = \frac{\beta}{N_s}$$$

*PV发电机等效电阻和热电压参数缩放关系，用于将模块级参数转换为发电机级参数*


**公式6**: $$$I_{linearized} = I_{eq} + G_{eq}V$$$

*ELST中光伏模型的线性化表示形式，$G_{eq}$为等效电导，$I_{eq}$为等效电流源，通过在当前工作点求导获得*


### 算法步骤

1. 初始化：设定仿真时步$\Delta t$，获取PV模块参数($I_g$, $I_o$, $a$, $R_s$, $R_p$)，根据阵列配置计算发电机级参数

2. BLST步骤（基线方法）：(1) 在第k步，利用前一步电压$V(k-1)$代入非线性方程计算$I(k)$；(2) 将$I(k)$作为理想电流源注入线性网络；(3) 求解线性系统$YV(k)=I_{inj}$获得当前步电压；(4) 存储$V(k)$供下一步使用

3. ELST步骤（改进方法）：(1) 在第k步，首先使用$V(k-1)$评估非线性方程并计算当前工作点的导数$\partial I/\partial V$；(2) 构建线性化等效电路：等效电导$G_{eq} = -\partial I/\partial V$（取负因为电流注入方向），等效电流源$I_{eq} = I(V(k-1)) - G_{eq}V(k-1)$；(3) 将$G_{eq}$并入节点导纳矩阵，$I_{eq}$并入注入电流向量；(4) 求解扩展的线性系统获得$V(k)$；(5) 更新状态并进入下一步

4. 收敛性监控：在每个时步检查残差$|V(k) - V(k-1)| < \epsilon$，若未收敛可迭代或减小步长


### 关键参数

- **q**: 1.60217646e-19 C (电子电荷)

- **k**: 1.3806503e-23 J/K (玻尔兹曼常数)

- **T**: p-n结温度 (K)

- **Ms**: 串联光伏电池数

- **a**: 二极管理想因子 (1-2)

- **Ig**: 光生电流 (A)，与辐照度$G$成正比

- **Io**: 二极管反向饱和电流 (A)，与温度$T$相关

- **Rs**: 串联电阻 (Ω)

- **Rp**: 并联/旁路电阻 (Ω)

- **Np**: 并联阵列数量

- **Ns**: 串联模块数量

- **beta_gen**: 发电机级热电压倒数，$\beta/N_s$

- **Rs_gen**: 发电机级串联电阻，$N_s/N_p \cdot R_s$

- **step_delay**: 单步延迟$\Delta t$导致的代数环误差



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 局部遮阴条件(partial shading) | PV发电机部分阵列处于不同辐照度条件，需用多个单二极管等效电路建模，导致传统BLST方法出现数值发散 | ELST在相同遮阴模式下保持数值稳定，而BLST在遮阴突变时失效 |

| 多电平逆变器接口 | PV发电机通过中性点箝位(NPC)或级联H桥等多电平逆变器并网，需多个独立PV模型分别连接至不同直流母线 | ELST成功处理多直流端口非线性耦合，BLST因多模块间数值耦合失稳 |

| 电气故障瞬态 | IEEE基准系统中发生短路或电压骤降故障，测试PV系统在电网扰动下的暂态响应 | ELST在故障期间及故障清除后均保持收敛，BLST在电压急剧变化时迭代发散 |

| 计算效率验证 | 对比完全迭代求解法（如PSpice/Matlab）、BLST和ELST的计算时间 | ELST计算负担与BLST相当（线性系统复杂度），比完全迭代法快 orders of magnitude，仅比纯线性系统增加有限的矩阵重构开销 |



## 量化发现

- 单步延迟误差：BLST引入的时延误差与仿真步长$\Delta t$和电压变化率$dV/dt$成正比，在遮阴突变或故障时$dV/dt$极大导致误差不可接受
- 参数缩放比例：发电机级串联电阻$R_{s,gen} = (N_s/N_p)R_s$，并联电阻$R_{p,gen} = (N_s/N_p)R_p$，光生电流$I_{g,gen} = N_p I_g$
- 计算复杂度：ELST每时步仅需一次线性系统求解（与BLST相同），导数计算解析进行，不增加迭代次数
- 收敛半径：理论分析证明ELST的收敛域显著大于BLST，在光伏特性曲线斜率突变区（局部遮阴多峰值）仍能保证局部收敛
- 数值稳定性：ELST通过将非线性特性以电导形式嵌入导纳矩阵，有效阻尼了BLST中存在的代数环振荡，阻尼比改善与$G_{eq}$的引入直接相关


## 关键公式

### 单二极管PV模型隐式方程

$$$I(V) = I_g - I_o(e^{\beta(V+R_s I)/a} - 1) - \frac{V+R_s I}{R_p}$$$

*描述实际PV模块的I-V特性，用于计算工作点电流和构建ELST的线性化模型*

### ELST等效电导（隐式微分）

$$$G_{eq} = \left.\frac{\partial I}{\partial V}\right|_{V(k-1)} = -\frac{\beta I_o}{a}e^{\beta(V+R_s I)/a}\left(1 + R_s\frac{\partial I}{\partial V}\right) - \frac{1}{R_p}\left(1 + R_s\frac{\partial I}{\partial V}\right)$$$

*在ELST中计算当前工作点的动态电导，用于构建伴随模型并入节点导纳矩阵*

### ELST扩展节点方程

$$$\begin{bmatrix} Y_{sys} + G_{eq} & -G_{eq} \\ -G_{eq} & G_{eq} \end{bmatrix} \begin{bmatrix} V_{bus} \\ V_{pv} \end{bmatrix} = \begin{bmatrix} I_{sources} \\ I_{eq} \end{bmatrix}$$$

*将光伏线性化模型并入电力系统节点分析方程，$Y_{sys}$为网络导纳矩阵，$G_{eq}$为PV等效电导*



## 验证详情

- **验证方式**: 数值仿真验证与收敛性理论分析相结合。通过构建收敛性数学框架，证明ELST相比BLST具有更大的稳定域；通过PSCAD/EMTDC时域仿真验证理论结果
- **测试系统**: 1) 简单测试系统：用于验证理论分析；2) IEEE标准配电系统基准（具体为IEEE benchmark distribution system），含多台PV发电机并网
- **仿真工具**: PSCAD/EMTDC（电磁暂态仿真软件），用于实现BLST和ELST算法并对比验证
- **验证结果**: 仿真验证了在局部遮阴（PV特性出现多峰值）、电网故障（电压骤降）及多电平逆变器接口（多直流母线耦合）三种严苛工况下，ELST均保持数值稳定收敛，而BLST在相同条件下出现数值发散或收敛失败。计算效率方面，ELST保持了与BLST相当的线性计算复杂度，远高于全牛顿迭代法的非线性求解效率
