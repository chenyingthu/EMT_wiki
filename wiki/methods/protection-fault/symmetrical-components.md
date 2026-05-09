---
title: "对称分量法 (Symmetrical Components)"
type: method
tags: [symmetrical-components, sequence, unbalanced, fault-analysis, fortescue]
created: "2026-05-02"
---

# 对称分量法 (Symmetrical Components)


```mermaid
graph TD
    subgraph Ncmp[对称分量法 (Symmetrical Components)]
        N0[零序 $X_0$: 三相同相]
        N1[正序 $X_1$: a-b-c 正相序]
        N2[负序 $X_2$: a-c-b 反相序]
    end
```


## 定义与边界

对称分量法是 Fortescue 变换在三相交流系统中的应用：任意一组三相复相量可唯一分解为零序、正序和负序三组对称相量。它是一种线性代数分解，不是完整故障模型，也不自动给出设备参数、保护动作或 EMT 暂态波形。

本页负责数学定义和物理解释。使用流程见 [[sequence-component-method]]；序网构建见 [[sequence-network-model]]；直接相域建模见 [[phase-domain-modeling]]。

## 数学定义

令 $a=e^{j120^\circ}$，满足

$$
a^3=1,\qquad 1+a+a^2=0.
$$

相量到序量的变换为

$$
\begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix}
=\frac{1}{3}
\begin{bmatrix}
1 & 1 & 1 \\
1 & a & a^2 \\
1 & a^2 & a
\end{bmatrix}
\begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix}.
$$

反变换为

$$
\begin{bmatrix} X_a \\ X_b \\ X_c \end{bmatrix}
=
\begin{bmatrix}
1 & 1 & 1 \\
1 & a^2 & a \\
1 & a & a^2
\end{bmatrix}
\begin{bmatrix} X_0 \\ X_1 \\ X_2 \end{bmatrix}.
$$

因此

$$
X_a=X_0+X_1+X_2,
$$

$$
X_b=X_0+a^2X_1+aX_2,
$$

$$
X_c=X_0+aX_1+a^2X_2.
$$

## 分量含义

| 分量 | 相序关系 | 常见物理解释 | 边界 |
|---|---|---|---|
| 零序 $X_0$ | 三相同相 | 接地通道、中性点位移、共模分量 | 是否流通取决于回路 |
| 正序 $X_1$ | a-b-c 正相序 | 正常基波运行和正向旋转磁场 | 不代表全部暂态能量 |
| 负序 $X_2$ | a-c-b 反相序 | 不平衡、反向旋转磁场、负序保护量 | 对旋转电机可能引起额外转子效应 |

对称分量的“正序”“负序”是相量基底定义。若研究的是瞬时波形中的正负序，需要说明如何从 EMT 数据中提取基频相量或解析信号。

## 与功率和阻抗的关系

若电压和电流都用相同序分量约定表示，复功率可分解为各序贡献的和：

$$
S=3(V_0I_0^*+V_1I_1^*+V_2I_2^*).
$$

该式依赖相量稳态和一致的共轭约定。保护、设备发热和稳定性分析不应只看这个代数式，还要考虑时间积分、负序热容量、控制限流和故障持续时间等外部条件。

序阻抗 $Z_0$、$Z_1$、$Z_2$ 不是由变换矩阵自动给出，而来自设备和网络模型。线路、变压器、发电机和接地系统的序阻抗需要单独建模或查证。

## EMT 中的作用

对称分量在 EMT wiki 中主要作为桥接概念：

- 从三相波形或相量中构造不平衡指标。
- 解释保护装置使用的零序和负序测量量。
- 把经典短路计算与相域 EMT 故障仿真联系起来。
- 为动态相量、dq-sequence 或多参考系方法提供分量定义。

它不应被写成相域 EMT 的替代品。EMT 波形中包含衰减直流、谐波、开关纹波和高频行波时，单一基频序分量只能描述其中一个投影。

## 适用边界与失败模式

- 只适用于三相集合；多导体线路、电缆护套、地线和多绕组设备需要扩展矩阵或相域模型。
- 对非线性饱和、电弧、断续接触和电力电子限流，只做序分量分解不能得到真实动态。
- 零序电流是否存在不能只由 $X_0$ 非零判断，还要看外部回路和变压器连接。
- 负序对旋转电机的影响需要设备模型，不应只用负序相量大小直接推断热风险。
- 把“基频相量序分量”和“瞬时序分量”混写，会造成证据边界不清。

## 代表性证据

[[fault-analysis]] 可作为不平衡故障中使用对称分量的上位方法入口，但它也明确区分了序网相量计算与 EMT 相域故障注入。[[dynamic-phasor]] 和 [[complex-differential-equation-solving]] 可作为把序分量、旋转坐标和包络变量结合的相关入口；这些方法需要额外定义窗口和频率参考。

## 与相关页面的关系

- [[sequence-component-method]]：把本页变换用于不平衡分析的步骤。
- [[sequence-network-model]]：把序阻抗组织成故障计算网络。
- [[coordinate-transformation]]：坐标变换总览。
- [[dq-transformation]]：同步旋转坐标，与序分量可组合但不是同一分解。
- [[phase-domain-modeling]]：不通过序分解而直接求解 abc 耦合。
- [[unbalanced-fault-analysis]]：不平衡故障应用场景。

## 修订与证据使用注意事项

新增内容应区分数学恒等式、工程参数和论文算例。数学变换可直接给出；设备序阻抗、保护限值、热容量和故障电流数值必须绑定来源和工况。

## 来源论文

| 论文 | 年份 |
|------|------|
| [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym|A new distance relaying algorithm based on complex different]] | 2004 |
| [[fast-detection-method-of-commutation-failure-based-on-multi-infeed-interaction-f|Fast Detection Method of Commutation Failure Based on Multi-]] | 2023 |
