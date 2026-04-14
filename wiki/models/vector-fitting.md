---
title: "矢量拟合"
type: model
tags: []
created: "2026-04-13"
---

# 矢量拟合

## 论文方法分析
> 基于 6 篇相关论文的深度内容分析生成
### 使用的方法/技术
| 方法/技术 | 使用次数 | 代表论文 |
|----------|---------|----------|| 并行计算技术 | 2 | Enhancing computation performance of rational approximation for freque |
| C语言底层线性代数实现 | 2 | Enhancing computation performance of rational approximation for freque |
| 有理函数逼近 | 2 | Rational approximation of frequency domain responses by vector fitting |
| 复数向量拟合(CVF) | 1 | Enhancing computation performance of rational approximation for freque |
| 向量拟合(VF) | 1 | Enhancing computation performance of rational approximation for freque |
| 有理逼近建模 | 1 | Enhancing computation performance of rational approximation for freque |
| 复数向量拟合 (CVF) | 1 | Enhancing computation performance of rational approximation for freque |
| 向量拟合 (VF) | 1 | Enhancing computation performance of rational approximation for freque |
| 有理逼近与频域实现 | 1 | Enhancing computation performance of rational approximation for freque |
| 模态矢量拟合(MVF) | 1 | Fast Realization of the Modal Vector Fitting |
| 带逆幅值加权的常规矢量拟合 | 1 | Fast Realization of the Modal Vector Fitting |
| 稀疏矩阵结构优化求解 | 1 | Fast Realization of the Modal Vector Fitting |
| 逐行对称留数识别 | 1 | Fast Realization of the Modal Vector Fitting |
| 有理函数/极点-留数建模 | 1 | Fast Realization of the Modal Vector Fitting |
| 向量拟合(Vector Fitting) | 1 | Rational approximation of frequency domain responses by vector fitting |
### 涉及的设备/模型
| 设备/模型 | 使用次数 |
|----------|----------|| 频率相关网络等值(FDNE) | 1 |
| 8端口网络模型 | 1 |
| 导纳/阻抗矩阵模型 | 1 |
| 频率相关网络等值 (FDNE) | 1 |
| 8端口网络等值模型 | 1 |
| 有理模型 (Rational Models) | 1 |
| 频率相关网络等效(FDNE) | 1 |
| 多端口导纳矩阵 | 1 |
| 极点-留数模型 | 1 |
| 状态空间模型 | 1 |
| 变压器 | 1 |
| 网络等值模型 | 1 |
| 频变电力系统组件 | 1 |
| Frequency-dependent network equivalents (FDNE) | 1 |
| High-frequency transformers | 1 |
### 验证方式分布
- **仿真/对比**: 2 篇
- **仿真与计算性能对比**: 1 篇
- **仿真**: 1 篇
- **仿真/实验**: 1 篇
- **仿真对比**: 1 篇
## 技术演进脉络
### 2004年 (1篇)
- **Rational approximation of frequency domain responses by vector fitting - Power D**
  - 💡 通过在向量拟合中引入复数起始极点，实现了对含密集谐振峰频域响应的高精度、通用有理函数逼近。
  - 提出了一种通用的频域响应有理函数逼近框架
  - 将向量拟合算法扩展至复数起始极点，解决了多谐振峰拟合难题
### 2009年 (1篇)
- **Fast Realization of the Modal Vector Fitting**
  - 💡 通过预计算初始极点、利用稀疏矩阵求解极点及逐行对称求解留数三步策略，实现了模态矢量拟合方法的高效计算，解决了高阻抗终端下小特征值建模误差放大与计算资源消耗大的问题。
  - 提出通过带逆幅值加权的常规矢量拟合预计算初始极点集，显著减少MVF迭代次数。
  - 利用稀疏矩阵结构仅求解关键未知数，实现极点识别步骤的高效计算。
### 2021年 (1篇)
- **Review and comparison of frequency-domain curve-fitting techniques: Vector fitti**
  - 💡 首次将四种主流频域曲线拟合技术与模型降阶方法结合进行系统性横向对比，为EMT仿真中宽频带等效建模提供了明确的方法选型与降阶指导。
  - 系统梳理并对比了VF、FpF、MPM和LM四种主流频域曲线拟合技术的基本理论与算法特性。
  - 通过三个典型算例定量评估了各方法在拟合精度与模型阶数方面的性能差异。
### 2022年 (1篇)
- **Transient Analysis on Multiphase Transmission Line Above Lossy Ground Combining **
  - 💡 将矢量拟合技术与考虑频变土壤参数的Nakagawa模型相结合，有效提升了ATP工具中多相架空线路雷击暂态仿真的计算精度。
  - 系统对比了Bode法与矢量拟合技术在JMarti模型中逼近特征阻抗和传播矩阵的精度与性能。
  - 深入分析了Nakagawa方法与Carson方法在考虑频变土壤参数时对线路暂态响应的影响差异。
### 2024年 (2篇)
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 首次将CVF引入FDNE矩阵综合并结合并行C语言底层实现，在保持高精度的同时大幅提升了计算效率与软件独立性。
  - 首次将复数向量拟合(CVF)应用于FDNE导纳/阻抗矩阵综合，突破了传统算法必须满足复共轭极点配对的限制。
  - 开发了基于C语言与底层线性代数库的并行化VF/CVF算法实现，彻底摆脱了对MATLAB等商业软件的依赖。
- **Enhancing computation performance of rational approximation for frequency-depend**
  - 💡 将复数向量拟合引入FDNE导纳矩阵综合，并结合并行化C语言底层实现，构建了无商业软件依赖的高性能有理逼近计算框架。
  - 首次将复数向量拟合（CVF）应用于导纳/阻抗矩阵综合，消除了传统VF对复共轭极点的强制约束。
  - 开发了基于C语言和底层线性代数库的VF与CVF并行化实现，彻底摆脱了对MATLAB等商业软件的依赖。
## 关键发现汇总
- [2004] **Rational approximation of frequency domain responses by vect**: 复数起始极点策略成功克服了原实数极点方法在多谐振峰场景下的失效问题
- [2004] **Rational approximation of frequency domain responses by vect**: 在人工构造数据、实测变压器频响及网络等值模型中均实现了高精度拟合
- [2004] **Rational approximation of frequency domain responses by vect**: 将频域响应转化为低阶有理函数，大幅提升了时域EMT仿真的计算效率
- [2009] **Fast Realization of the Modal Vector Fitting**: 所提快速实现方法在保证小特征值精确表示的同时，大幅降低了计算时间和内存消耗。
- [2009] **Fast Realization of the Modal Vector Fitting**: 在频率相关网络等效（FDNE）建模算例中验证了该方法的高效性与准确性。
- [2021] **Review and comparison of frequency-domain curve-fitting tech**: VF及其改进算法在多数宽频带场景下拟合精度最优，但为满足误差指标常需较高的模型阶数。
- [2021] **Review and comparison of frequency-domain curve-fitting tech**: MPM和LM作为非迭代方法避免了初始极点选择难题，但在复杂频段拟合中易产生冗余阶数。
- [2021] **Review and comparison of frequency-domain curve-fitting tech**: 结合MOR技术可在几乎不损失精度的前提下显著压缩状态空间模型阶数，有效提升EMT仿真计算速度。
- [2022] **Transient Analysis on Multiphase Transmission Line Above Los**: 矢量拟合技术在逼近特征阻抗和传播矩阵时的精度显著优于传统Bode法。
- [2022] **Transient Analysis on Multiphase Transmission Line Above Los**: 采用Nakagawa方法计算的暂态电压峰值较Carson方法明显降低，且在高电阻率土壤中差异更为显著。
- [2024] **Enhancing computation performance of rational approximation **: 并行化C语言实现显著加速了有理逼近过程，有效处理了具有大量峰谷特征的复杂频率响应。
- [2024] **Enhancing computation performance of rational approximation **: CVF算法在取消共轭极点约束的情况下仍能保证FDNE建模的精度与数值稳定性。
- [2024] **Enhancing computation performance of rational approximation **: 所提算法的计算性能随模型阶数、端口数和频率样本量的变化表现出良好的可扩展性与效率优势。
- [2024] **Enhancing computation performance of rational approximation **: 并行化C语言实现显著提升了有理逼近的计算效率，大幅缩短了大规模FDNE的拟合耗时。
- [2024] **Enhancing computation performance of rational approximation **: CVF方法成功处理了具有大量频域峰谷的8端口FDNE，且无需进行复共轭极点配对。
- [2024] **Enhancing computation performance of rational approximation **: 算法计算性能随模型阶数、端口数及频率样本量的变化表现出良好的可扩展性与稳定性。
