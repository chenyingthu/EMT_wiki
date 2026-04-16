---
title: "A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation"
type: source
year: 2023
journal: "IEEE Transactions on Power Delivery;2023;38;1;10.1109/TPWRD.2022.3181445"
created: "2026-04-13"
sources: ["EMT_Doc/04/Leal和Conti - 2023 - A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation.pdf"]
---

# A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation

**年份**: 2023
**来源**: `04/Leal和Conti - 2023 - A Thévenin-Type Version of the Extended Modal-Domain Model for Lightning-Induced Voltage Calculation.pdf`

## 摘要

—In this paper, a new procedure is proposed for de- termining the external current sources required for evaluating lightning-induced voltages on overhead lines with the extended- modal domain (EMD) model. Unlike the original model, in which the calculation of the inducing current sources depends on the ﬁtting of the characteristic admittance of the line, in the proposed procedure this calculation is performed using the characteristic impedance of the line. This signiﬁcantly simpliﬁes the use of the EMD model because now all parameters can be readily obtained from the built-in ﬁtting tool that is usually available in electro- magnetic transient programs to derive the parameters of Marti’s transmission line model. The validity of the proposed procedure is demonstrated through examples that i

## 核心贡献


- 提出基于特征阻抗拟合的雷击感应电压计算方法，替代原特征导纳拟合流程。
- 将外部电磁场激励等效为戴维南型电流源，直接复用EMT软件内置线路拟合参数。
- 推导扩展模态域模型感应电流源的时域递归卷积算法，简化多导体线路建模。


## 使用的方法


- [[矢量拟合|矢量拟合]]
- [[戴维南等效变换|戴维南等效变换]]
- [[递归卷积算法|递归卷积算法]]
- [[模态域变换|模态域变换]]
- [[有理函数逼近|有理函数逼近]]


## 涉及的模型


- [[marti输电线路模型|Marti输电线路模型]]
- [[扩展模态域模型|扩展模态域模型]]
- [[多导体架空线路|多导体架空线路]]
- [[配电变压器|配电变压器]]
- [[避雷器|避雷器]]


## 相关主题


- [[雷击感应电压|雷击感应电压]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[频率相关线路建模|频率相关线路建模]]
- [[外部电磁场耦合|外部电磁场耦合]]
- [[配电线路过电压|配电线路过电压]]


## 主要发现


- 验证了基于特征阻抗的新方法在计算架空配电线路雷击感应电压时具有高精度。
- 新方法可直接调用EMT软件内置拟合参数，免除了用户独立编写拟合代码的需求。
- 在含变压器、避雷器及多点接地的复杂网络中，仿真波形与基准结果高度吻合。


