---
title: "Decision tree-based methodology for high impedance fault detection"
type: source
authors: ['Yong Sheng', 'S.M. Rovnyak']
year: 2004
journal: "IEEE Transactions on Power Delivery;2004;19;2;10.1109/TPWRD.2003.820418"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/12/Decision_tree-based_methodology_for_high_impedance_fault_detection.pdf"]
---

# Decision tree-based methodology for high impedance fault detection

**作者**: Yong Sheng, S.M. Rovnyak
**年份**: 2004
**来源**: `12/Decision_tree-based_methodology_for_high_impedance_fault_detection.pdf`

## 摘要

—This paper presents a high impedance fault (HIF) detection method based on decision trees (DTs). The features of HIF, which are the inputs of DTs, are those well-known ones, including current [in root mean square (rms)], magnitudes of the second, third, and fifth harmonics, and the phase of the third harmonics. The only measurements needed in the proposed method are the current signals sampled at 1920 Hz. It will reduce the cost of hardware compared with methods that use high sampling rates. A new HIF model is also used. The data of current signals are from the simulation of Electromagnetic Transients Program (EMTP). The DT algorithm trained can successfully distinguish the HIFs from most normal operations on simulation data, including switching loads, switching shunt capacitors, and load

## 核心贡献


- 提出基于决策树的高阻故障检测方法仅需1920Hz采样率即可实现降低硬件成本
- 构建含非线性电阻与随机直流源的新型高阻电弧模型提升电磁暂态仿真逼真度
- 结合EMTP仿真与CART算法实现高阻故障与常规操作暂态的精准区分


## 使用的方法


- [[决策树算法-cart|决策树算法(CART)]]
- [[快速傅里叶变换-fft|快速傅里叶变换(FFT)]]
- [[滑动窗口特征提取|滑动窗口特征提取]]
- [[emtp电磁暂态仿真|EMTP电磁暂态仿真]]
- [[bctran参数计算|BCTRAN参数计算]]


## 涉及的模型


- [[高阻故障-hif-电弧模型|高阻故障(HIF)电弧模型]]
- [[配电系统|配电系统]]
- [[变压器|变压器]]
- [[输电线路|输电线路]]
- [[并联电容器|并联电容器]]
- [[工业负荷|工业负荷]]


## 相关主题


- [[高阻故障检测|高阻故障检测]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[谐波分析|谐波分析]]
- [[继电保护|继电保护]]
- [[模式识别|模式识别]]
- [[配电系统暂态分析|配电系统暂态分析]]


## 主要发现


- 决策树算法在百例测试中成功区分高阻故障与负荷投切电容投切及变压器励磁涌流
- 仅依赖1920Hz采样电流信号提取谐波特征即可满足工程低成本部署需求
- 新型随机高阻模型生成的暂态电流波形与频谱特征与实际现场测量数据高度吻合



## 方法细节

### 方法概述

提出一种基于决策树（DT）的高阻故障（HIF）检测方法。该方法仅依赖标准馈线电流信号，采样率设定为1920 Hz（每周期32点），大幅降低硬件成本。通过1周期滑动窗口（步长1/8周期）对电流进行FFT分析，提取基波RMS值、第2/3/5次谐波幅值（经RMS归一化）及第3次谐波相位构成5维特征向量。采用CART算法离线训练45节点决策树，在线部署时结合低通滤波与特征提取。为抑制误动，设定“连续两次输出为1”的跳闸逻辑，并通过调整误分类代价（0→1代价为1→0的10倍）优化保护可靠性。该方案无需新增测量设备，可直接集成于现有微机保护控制器。

### 数学公式


**公式1**: $$$\mathbf{x} = \left[ I_{\text{rms}}, \frac{|I_2|}{I_{\text{rms}}}, \frac{|I_3|}{I_{\text{rms}}}, \frac{|I_5|}{I_{\text{rms}}}, \angle I_3 \right]$$$

*决策树输入特征向量，包含电流有效值及归一化的2、3、5次谐波幅值与3次谐波相位*


**公式2**: $$$V_{\text{dc}}^{(k)} = V_{\text{mean}} + \delta_k, \quad \delta_k \sim \mathcal{U}(-\Delta V, \Delta V)$$$

*HIF电弧模型中直流源电压每半周期随机变化的数学表达，用于模拟不同接地表面的动态特性*


**公式3**: $$$N_{\text{win}} = 32, \quad N_{\text{step}} = 4$$$

*滑动窗口采样点数与步长设置，对应1个周期窗口与1/8周期滑动间隔*


### 算法步骤

1. 信号采集与预处理：以1920 Hz采样率获取馈线三相电流，通过数字或模拟低通滤波器滤除高频噪声与白噪声干扰。

2. 滑动窗口划分：将连续电流信号划分为长度为32个采样点（1个工频周期）的滑动窗口，每次计算后窗口向前滑动4个采样点（1/8周期）。

3. 频域特征提取：对每个窗口内的电流数据执行快速傅里叶变换（FFT），计算基波RMS值、第2/3/5次谐波幅值及第3次谐波相位，并将谐波幅值除以当前窗口RMS值完成归一化。

4. 决策树分类推理：将提取的5维特征向量输入离线训练好的CART决策树（45个节点），算法输出二分类结果（0表示正常，1表示HIF）。

5. 跳闸逻辑判定：采用连续确认机制，仅当决策树连续两次输出为1时，才判定发生高阻故障并触发保护动作，以此容忍单次分类波动并降低误动率。


### 关键参数

- **采样率**: 1920 Hz (32点/周期)

- **滑动窗口长度**: 1个周期 (32点)

- **滑动步长**: 1/8周期 (4点)

- **特征维度**: 5维 (RMS, 2/3/5次谐波幅值, 3次谐波相位)

- **决策树节点数**: 45

- **误分类代价比**: 10:1 (0→1代价是1→0的10倍)

- **跳闸确认阈值**: 连续2个周期输出为1



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 100个综合测试事件（25个HIF故障，75个正常操作） | 在总计5700个测试样本中，算法实现100%分类准确率。所有25个HIF事件均在故障发生后2个周期内被准确识别，75个正常操作事件（含负荷投切、电容投切、变压器励磁涌流）在8个周期监测窗口内零误动。 | 相比文献中依赖高频采样（>10 kHz）或复杂神经网络的方案，本方法在保持100%检测率的同时，将硬件采样成本降低至1/5以上，且训练与在线推理速度显著提升。 |

| 不同接地表面与导体状态HIF仿真 | 通过随机调整HIF模型直流源均值（1000~5000 V）与标准差，模拟沥青、沙地、草地等不同接地条件及导线落地/未落地状态，决策树均能稳定提取谐波特征并正确分类。 | 传统基于固定阈值或单一谐波的方法在多变接地条件下易失效，本方法通过CART自动划分超平面，对非线性与随机性电弧的鲁棒性提升显著。 |



## 量化发现

- 采样率仅需1920 Hz（每周期32点），远低于同类研究中常见的10 kHz以上高频采样要求。
- 决策树在线执行时间可忽略不计，主要计算耗时集中于FFT特征提取。
- 误分类代价比设置为10:1，使正常状态误判为故障的概率被严格压制。
- 训练集规模达468个事件共26676个样本，测试集为100个事件共5700个样本。
- 故障检测响应时间≤2个周期（60 Hz系统下约33.3 ms）。
- 测试集分类准确率达100%，正常工况误动率为0%，漏报率为0%。


## 关键公式

### HIF特征向量构建公式

$$$\mathbf{x} = \left[ I_{\text{rms}}, \frac{|I_2|}{I_{\text{rms}}}, \frac{|I_3|}{I_{\text{rms}}}, \frac{|I_5|}{I_{\text{rms}}}, \angle I_3 \right]$$$

*用于将时域电流信号转换为决策树可处理的5维归一化频域特征，消除负荷波动对幅值绝对值的影响*

### HIF电弧随机直流源模型

$$$V_{\text{dc}}^{(k)} = V_{\text{mean}} + \delta_k$$$

*在EMTP仿真中每半周期随机更新直流源幅值，以逼近真实电弧的非线性、不对称与动态随机特性*



## 验证详情

- **验证方式**: 电磁暂态仿真（EMTP）结合离线机器学习训练与测试
- **测试系统**: 138/12.5-kV变电站配电系统，含50km无限大电源输电线路、4条架空馈线，HIF设置于5km馈线末端，带工业负荷（1800 kVar并联电容，功率因数0.8滞后）
- **仿真工具**: EMTP（含MCAT接口导出MATLAB格式）、C++（随机事件生成与直流源时序控制）、MATLAB（FFT与数据预处理）、CART软件（决策树训练与验证）
- **验证结果**: 在涵盖负荷投切、电容器投切、变压器空载励磁涌流及不同接地表面特性的100个测试事件中，算法实现100%分类准确率，HIF检测延迟≤2周期，正常操作零误报，验证了低采样率下决策树方案的工程可行性与高可靠性。
