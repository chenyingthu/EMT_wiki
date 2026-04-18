---
title: "Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri"
type: source
authors: ['未知']
year: 2026
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Liu 等 - 2010 - Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri.pdf"]
---

# Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri

**作者**: 
**年份**: 2026
**来源**: `17/Liu 等 - 2010 - Electromechanical transientelectromagnetic transient hybrid simulation method considering asymmetri.pdf`

## 摘要

An effective solution of electromechanical transient and electromagnetic transient hybrid simulation was proposed, including interface selection, mutual equivalence methods between electromechanical transient and electro- magnetic transient network. It is able to deal with the situation that the positive and negative sequence parameters of equiva- lence circuit are different. Least square method was adopted to obtain three-sequence fundamental frequency current which indicated the influence of electromagnetic transiet simulation on the electromechanical network. The solution is demonstrated effective and feasible through several cases. Problems in hybrid simulation are solved when various faults (including symmetric and asymmetric faults) occur in electromechanical network. KEY WORDS: HVDC

## 核心贡献


- 提出机电与电磁混合仿真接口选取及双向诺顿等值交互方法，实现多端口耦合等效
- 提出基波负序补偿法处理等值电路正负序参数不等问题，有效消除稳态计算误差
- 采用最小二乘法提取三序基波电流，实现电磁暂态结果对机电网络的精确反馈


## 使用的方法


- [[混合仿真|混合仿真]]
- [[诺顿等值|诺顿等值]]
- [[补偿法|补偿法]]
- [[最小二乘法|最小二乘法]]
- [[序网-三相坐标变换|序网-三相坐标变换]]
- [[迭代交互求解|迭代交互求解]]


## 涉及的模型


- [[vsc-hvdc|VSC-HVDC]]
- [[换流器|换流器]]
- [[换流变压器|换流变压器]]
- [[同步发电机|同步发电机]]
- [[动态负荷|动态负荷]]
- [[交流电网|交流电网]]


## 相关主题


- [[机电-电磁混合仿真|机电-电磁混合仿真]]
- [[不对称故障|不对称故障]]
- [[网络等值|网络等值]]
- [[接口交互技术|接口交互技术]]
- [[正负序参数处理|正负序参数处理]]
- [[大规模电网仿真|大规模电网仿真]]


## 主要发现


- 正负序参数不等会导致导纳矩阵不对称，若不处理将引发显著的稳态功率计算误差
- 所提方案在对称与不对称故障下均能保持接口数据交互稳定，混合仿真结果准确可靠
- 经IEEE九节点及大电网验证，该方法兼顾局部电磁暂态精度与全网计算效率



## 方法细节

### 方法概述

提出一种机电-电磁暂态混合仿真架构，将电网划分为含HVDC等电力电子设备的电磁暂态子系统（微秒级步长）和含发电机/负荷的机电暂态子系统（周波级步长）。接口选在换流器交流母线。机电侧通过正、负、零三序诺顿等值向电磁侧提供边界条件，利用补偿法实现双向迭代交互。针对旋转电机导致等值电路正负序参数不等引发的导纳矩阵不对称问题，提出“基波负序电流补偿法”，将负序导纳强制替换为正序导纳，并附加补偿电流源修正误差。电磁侧向机电侧反馈时，采用最小二乘曲线拟合法从三相瞬时值中提取基波三序电流，避免故障期间电压过零导致的功率计算失效，实现跨时间尺度与模型精度的精确耦合。该方案有效解决了不对称故障下的接口数据交互稳定性问题。

### 数学公式


**公式1**: $$$U_F = U_F^0 + Z_T I_F$$$

*端口电压向量等于开路电压向量、端口等值阻抗矩阵与注入电流向量的线性叠加，用于补偿法正向求解*


**公式2**: $$$U_F^0 = U_F - Z_T I_F$$$

*根据当前端口电压和注入电流反推戴维南开路电压，用于机电-电磁迭代交互中的边界条件更新*


**公式3**: $$$Y_{eq}^{(1,2,0)} U^{(1,2,0)} = I_{eq}^{(1,2,0)} + I_{emt}^{(1,2,0)}$$$

*多端口三序诺顿等值网络方程，描述接口处三序电压、等值电流源与电磁侧注入电流的关系*


**公式4**: $$$Y_{eq}^{(a,b,c)} = S Y_{eq}^{(1,2,0)} S^{-1}$$$

*利用分块对角变换矩阵S将三序导纳阵转换为abc三相瞬时值导纳阵，实现序网模型到电磁暂态模型的映射*


**公式5**: $$$\Delta i_{diff-ij}^{(2)} = (y_{eqij}^{(2)} - y_{eqij}^{(1)})(u_i^{(2)} - u_j^{(2)})$$$

*基波负序补偿电流计算公式，用于修正因强制令负序导纳等于正序导纳而产生的稳态误差*


### 算法步骤

1. 初始化或网络变更时，从机电暂态全网三序导纳阵中剔除电磁暂态子系统贡献，形成独立机电网络。

2. 在新机电网络各端口依次注入单位电流，计算全网节点电压响应，构建多端口等值阻抗矩阵$Z_T$。

3. 提取当前迭代步的端口电压向量$U_F$，结合上一步电磁侧注入电流$I_F$，利用公式$U_F^0 = U_F - Z_T I_F$计算戴维南开路电压。

4. 将$U_F^0$与$Z_T$作为边界条件传递给电磁暂态程序，驱动其进行微秒级详细仿真，计算出新端口注入电流$I_F$。

5. 利用补偿公式$U_F = U_F^0 + Z_T I_F$修正机电侧全网节点电压，完成机电网络状态更新。

6. 将机电侧输出的三序诺顿等值参数通过变换矩阵$S$转换为abc三相瞬时值模型，并入电磁侧网络方程求解。

7. 若检测到正负序导纳不等，应用基波负序电流补偿法计算$\Delta i_{diff-ij}^{(2)}$，作为附加电流源注入支路，消除导纳不对称误差。

8. 电磁侧单步仿真结束后，截取半个周波长度的接口母线三相瞬时数据，采用最小二乘法拟合提取基波正、负、零序电流，作为恒流源注入机电侧网络，进入下一机电步长迭代。


### 关键参数

- **接口位置**: 换流器交流终端母线

- **机电暂态步长**: 周波级（通常10~20ms）

- **电磁暂态步长**: 微秒级（通常10~50μs）

- **最小二乘拟合窗口**: 半个周波数据长度

- **适用短路比条件**: 有效短路比>5（强交流系统）

- **坐标变换矩阵维度**: $(3m) \times (3m)$分块对角阵（m为接口母线数）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| IEEE 9节点系统稳态验证 | 未处理正负序不等时，母线1线路有功计算值为50.27MW（基准62.10MW），无功为40.24Mvar（基准29.10Mvar）。采用基波负序补偿法后，有功计算值升至62.09MW，无功降至29.14Mvar。 | 补偿法使有功误差从19.0%降至0.016%，无功误差从38.1%降至1.37%，稳态精度与PSD潮流程序完全一致。 |

| 2015年川电特高压直流送出系统不对称故障动态仿真 | 0s复龙站附近三相短路，0.1s单相拒动，0.34s后备保护动作。混合仿真准确捕捉直流电压跌落至-400kV、电流波动及功率振荡过程，三相交流电压波形畸变与恢复轨迹清晰。 | 动态响应曲线与PSCAD全电磁暂态基准高度重合，无接口数据发散或数值振荡，验证了不对称故障下的接口稳定性。 |



## 量化发现

- 基波负序电流补偿法将稳态功率计算最大误差从19.0%降低至0.016%以内
- 最小二乘法仅需半个周波数据即可完成基波提取，相比DFT整周波需求，在频率偏移和故障暂态期间精度显著提升
- 三序至abc相变换采用分块对角阵解耦计算，将$(3m)\times(3m)$大矩阵运算降维为m个$3\times3$小矩阵运算，大幅提升计算效率
- 混合仿真在有效短路比>5的强交流系统接口处，波形畸变误差可忽略，满足工程精度要求


## 关键公式

### 基波负序电流补偿公式

$$$\Delta i_{diff-ij}^{(2)} = (y_{eqij}^{(2)} - y_{eqij}^{(1)})(u_i^{(2)} - u_j^{(2)})$$$

*处理等值电路正负序参数不等导致的导纳矩阵不对称问题，附加补偿电流源修正稳态误差*

### 序网-三相坐标变换公式

$$$Y_{eq}^{(a,b,c)} = S Y_{eq}^{(1,2,0)} S^{-1}$$$

*将机电侧三序诺顿等值导纳转换为电磁侧abc三相瞬时值模型，实现跨模型接口耦合*

### 端口开路电压反推公式

$$$U_F^0 = U_F - Z_T I_F$$$

*机电-电磁迭代交互过程中，根据当前端口电压和注入电流动态更新戴维南等值电压源*



## 验证详情

- **验证方式**: 对比仿真验证（稳态潮流对比+动态故障波形对比）
- **测试系统**: IEEE 9节点测试系统；2015年四川电网特高压直流送出实际系统（含向家坝-上海、溪洛渡-浙西、溪洛渡-湖南三回直流）
- **仿真工具**: PSD-BPA（机电暂态程序）、PSCAD/EMTDC（电磁暂态程序）、自主开发混合仿真接口平台
- **验证结果**: 稳态下补偿法消除正负序参数差异引起的功率计算偏差（误差<0.02%）；动态不对称故障下，混合仿真直流电压/电流/功率响应曲线与全电磁暂态基准高度一致，验证了接口交互算法、负序补偿法及最小二乘反馈机制的有效性与工程可行性。
