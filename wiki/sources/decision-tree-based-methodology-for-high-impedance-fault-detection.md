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


