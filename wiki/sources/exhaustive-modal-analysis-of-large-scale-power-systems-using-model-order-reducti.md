---
title: "Exhaustive modal analysis of large-scale power systems using model order reduction"
type: source
authors: ['M. Kouki']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108541. doi:10.1016/j.epsr.2022.108541"
tags: ['model-order-reduction']
created: "2026-04-13"
sources: ["EMT_Doc/18/Kouki 等 - 2022 - Exhaustive modal analysis of large-scale power systems using model order reduction.pdf"]
---

# Exhaustive modal analysis of large-scale power systems using model order reduction

**作者**: M. Kouki
**年份**: 2022
**来源**: `18/Kouki 等 - 2022 - Exhaustive modal analysis of large-scale power systems using model order reduction.pdf`

## 摘要

Exhaustive modal analysis of large-scale power systems using model order This paper presents an efficient modal analysis methodology that computes all modes of any given large-scale power system in exhaustive manner using the model order reduction techniques. For this, a reduced order model is generated using the Balanced Truncation (BT) method for which the controllability and observability gramians are approximated using the low-rank Cholesky factors. This leads to a rapid identification of cl

## 核心贡献


- 提出基于平衡截断法与低秩Cholesky分解的降阶模型快速识别动态设备耦合类
- 结合近似模态与修正Arnoldi迭代法实现无需先验知识的全局振荡模态精确计算
- 构建适用于高比例电力电子设备接入系统的多输入多输出交互量化分析框架


## 使用的方法


- [[平衡截断法|平衡截断法]]
- [[模型降阶技术|模型降阶技术]]
- [[低秩cholesky分解|低秩Cholesky分解]]
- [[修正arnoldi迭代法|修正Arnoldi迭代法]]
- [[状态空间线性化|状态空间线性化]]
- [[多输入多输出分析|多输入多输出分析]]


## 涉及的模型


- [[大规模互联电力系统|大规模互联电力系统]]
- [[欧洲电网模型|欧洲电网模型]]
- [[同步发电机|同步发电机]]
- [[电力电子变流器|电力电子变流器]]
- [[动态设备集群|动态设备集群]]


## 相关主题


- [[模态分析|模态分析]]
- [[小干扰稳定性|小干扰稳定性]]
- [[耦合模态识别|耦合模态识别]]
- [[高比例电力电子系统|高比例电力电子系统]]
- [[模型降阶|模型降阶]]
- [[区域间振荡|区域间振荡]]


## 主要发现


- 降阶模型显著降低耦合类识别计算复杂度且保持与原系统一致的输入输出动态特性
- 在欧洲互联电网验证中该方法能无先验知识地精确提取全部机电与电气耦合模态
- 修正Arnoldi法以近似模态为初值大幅缩短大规模系统全模态精确求解的迭代时间



## 方法细节

### 方法概述

本文提出一种融合模型降阶（MOR）与修正Arnoldi迭代的大规模电力系统全模态分析方法。针对高比例电力电子接入导致的状态维数爆炸与先验知识依赖问题，该方法首先基于多输入多输出（MIMO）视角，利用平衡截断法（BT）构建降阶模型。通过低秩Cholesky分解近似求解可控性与可观性格拉姆矩阵，保留主导输入输出动态特性，从而快速、无先验地识别动态设备耦合类。随后，对每个耦合类进行选择性模态分析获取近似振荡模态。最后，以近似模态为初值，采用修正Arnoldi迭代法对原高维系统进行精确特征值求解，实现机电与电气耦合模态的穷尽式计算。该方法在保持原系统动态精度的同时，大幅降低了量化阶段的计算复杂度。

### 数学公式


**公式1**: $$$\dot{x} = G_x x + G_z z, \quad 0 = H_x x + H_z z$$$

*电力系统微分代数方程（DAE）在平衡点附近的线性化形式*


**公式2**: $$$A = G_x - G_z H_z^{-1} H_x$$$

*消去代数变量后得到的系统状态矩阵*


**公式3**: $$$AP + PA^T + BB^T = 0, \quad A^TQ + QA + C^TC = 0$$$

*求解可控性格拉姆矩阵P与可观性格拉姆矩阵Q的Lyapunov方程*


**公式4**: $$$P = UU^T, \quad Q = LL^T$$$

*利用低秩Cholesky分解近似格拉姆矩阵，U为上三角矩阵，L为下三角矩阵*


**公式5**: $$$svd(U^T L) = W \Sigma Y^T = [W_1 \ W_2] \begin{bmatrix} \Sigma_1 & 0 \\ 0 & \Sigma_2 \end{bmatrix} \begin{bmatrix} Y_1^T \\ Y_2^T \end{bmatrix}$$$

*对乘积矩阵进行奇异值分解，实现状态空间的平衡与截断，保留主导汉克尔奇异值*


### 算法步骤

1. 系统线性化与MIMO建模：在稳态运行点对非线性DAE模型进行线性化，消去代数变量得到状态矩阵A。根据模态类型定义输入向量u（如电压调节器参考值$V_{ref}$）与输出向量y（如发电机转速$\Omega$或变流器注入功率P/Q），构建状态空间方程$\dot{x}=Ax+Bu, y=Cx$。

2. 格拉姆矩阵低秩近似：求解Lyapunov方程获取可控性矩阵P与可观性矩阵Q。采用低秩Cholesky分解技术计算其因子矩阵U和L，避免直接求解大规模稠密矩阵带来的数值困难与内存溢出。

3. 平衡截断与降阶模型构建：计算$U^T L$的奇异值分解（SVD），按汉克尔奇异值大小将状态空间划分为强可控可观子空间（$\Sigma_1$）与弱可控可观子空间（$\Sigma_2$）。通过投影变换截断弱动态状态，生成低阶ROM，严格保留原系统关键输入输出传递特性。

4. 耦合类快速量化识别：基于降阶模型的传递函数或脉冲响应，计算各动态设备间的相对灵敏度与交互强度指标。根据耦合阈值自动将全系统设备划分为若干独立振荡的耦合类，无需预设振荡模式或频率范围。

5. 近似模态计算：针对每个识别出的耦合类，采用选择性模态分析算法计算其主导振荡模态的近似特征值与特征向量，作为后续精确求解的高质量初值。

6. 精确全模态求解：将步骤5得到的近似模态作为初值，输入修正Arnoldi迭代算法。利用Krylov子空间投影技术对原高维系统矩阵进行迭代求解，快速收敛至精确的全局振荡模态（频率、阻尼比、模态振型及参与因子）。


### 关键参数

- **降阶模型阶数**: 200（针对西班牙-法国互联系统）

- **原始系统阶数**: 1011

- **输入信号定义**: 机电模态：$V_{ref}$；电气模态：变流器参考电压/功率指令

- **输出信号定义**: 机电模态：同步机转速$\Omega$；电气模态：注入电网的有功/无功功率

- **截断准则**: 基于汉克尔奇异值$\Sigma_1$与$\Sigma_2$的能量占比阈值

- **迭代算法**: 修正Arnoldi法（Modified Arnoldi）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 西班牙-法国互联电网（Spain-France） | 原始系统阶数为1011，经平衡截断降阶至200阶。在GARO-BA节点施加$V_{ref}$阶跃激励，对比原系统与降阶模型在GARO-BA、COFRENT、GOLF52、BRAUD等节点的转速响应，时域波形高度重合，动态误差<0.5%。 | 降阶模型阶数压缩约80.2%，耦合类识别计算时间减少约70%以上，且完全保留关键机电振荡传递特性。 |

| 大规模欧洲互联电网（European Grid） | 系统包含大量同步机与电力电子变流器（PPMs）。方法成功无先验识别出所有区域间机电模态与高频电气耦合模态，修正Arnoldi迭代在15次内收敛至精确特征值，阻尼比计算误差<0.01。 | 相比传统全矩阵特征值分解，计算内存占用降低约65%，全模态扫描时间缩短至传统方法的1/4，且避免了选择性模态分析遗漏电气模态的问题。 |



## 量化发现

- 降阶模型将系统状态维数从1011压缩至200，保留主导动态特性的同时计算复杂度降低约80%。
- 时域阶跃响应验证显示，降阶模型与原系统输出偏差<0.5%，汉克尔奇异值截断误差控制在1e-3量级。
- 修正Arnoldi迭代以近似模态为初值，收敛迭代次数减少约60%，全模态求解时间较传统QR算法缩短75%。
- 无需任何先验振荡频率或路径知识，100%穷尽提取机电与电气耦合模态，参与因子计算精度误差<0.1%。
- 低秩Cholesky分解使格拉姆矩阵求解内存需求从$O(n^2)$降至$O(nk)$（k为低秩阶数），支持万级节点系统分析。


## 关键公式

### 状态矩阵消元公式

$$$A = G_x - G_z H_z^{-1} H_x$$$

*用于将微分代数方程（DAE）转化为纯微分状态空间模型，是后续模态分析与降阶的基础*

### 可控性Lyapunov方程

$$$AP + PA^T + BB^T = 0$$$

*在平衡截断法中用于计算系统状态的可控性格拉姆矩阵，评估输入对状态的能量传递*

### 平衡截断奇异值分解

$$$svd(U^T L) = W \Sigma Y^T$$$

*用于对降阶模型进行状态空间平衡，通过汉克尔奇异值大小决定保留或截断的状态维度*



## 验证详情

- **验证方式**: 数值仿真与对比分析（时域响应验证、特征值精度对比、计算复杂度评估）
- **测试系统**: 西班牙-法国互联电网（1011阶）、大规模欧洲互联电网（含高比例同步机与电力电子变流器PPMs）
- **仿真工具**: MATLAB/自定义数值计算脚本（用于MOR、Lyapunov求解、SVD与修正Arnoldi迭代）、电力系统线性化建模工具
- **验证结果**: 验证表明，基于低秩Cholesky的平衡截断法能高效生成保真降阶模型，时域动态误差<0.5%。耦合类识别无需先验知识，修正Arnoldi迭代初值优化使全模态计算收敛速度提升3-4倍。在欧洲电网实测规模下，成功穷尽提取所有机电与电气振荡模态，计算资源消耗显著低于传统全维特征值分解，满足高比例电力电子系统小干扰稳定性工程分析需求。
