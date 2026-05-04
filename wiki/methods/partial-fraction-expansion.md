---
title: "部分分式展开 (Partial Fraction Expansion)"
type: method
tags: [partial-fraction, residue, laplace-transform, transfer-function, rational-function]
created: "2026-05-02"
---

# 部分分式展开 (Partial Fraction Expansion)

## 定义与边界

部分分式展开把有理函数表示为极点、留数和直接项的和。对 EMT 而言，它是频域有理模型进入时域递推、状态空间实现和模态解释的桥梁，常与[[vector-fitting]]、[[wideband-modeling]]、[[frequency-dependent-modeling]]和[[passivity-enforcement]]配合使用。

本页讨论极点-留数表示和实现边界。它不是频域曲线拟合算法本身，也不自动保证拟合模型无源、稳定或适合实时仿真。

## EMT 中的作用

频率相关线路、变压器、接地网络和外部网络等值常以采样频率响应给出。若将端口响应拟合为有理函数，部分分式形式可把卷积核写为指数项，使 EMT 时域实现避免每步全历史卷积。

典型用途包括：

- 将导纳、阻抗或传播函数写为极点-留数模型。
- 从传递函数提取时域指数响应和振荡模式。
- 将有理函数转换为状态空间模型或递归卷积。
- 在[[modal-analysis]]中解释输入输出通道对某个模态的留数。

## 核心形式

对有理函数

$$
F(s)=\frac{N(s)}{D(s)},
$$

若分母有互异极点 $p_i$，可写为

$$
F(s)=d+s e+\sum_{i=1}^{n}\frac{k_i}{s-p_i}.
$$

其中 $k_i$ 是留数，$d$ 和 $e$ 分别描述直接项和高频比例项。对单极点，

$$
k_i=\lim_{s\to p_i}(s-p_i)F(s)=\frac{N(p_i)}{D'(p_i)}.
$$

若 $p$ 是 $m$ 阶重极点，

$$
F(s)=\sum_{j=1}^{m}\frac{k_j}{(s-p)^j}+R(s),
$$

其中留数需通过导数公式或线性方程求得。工程实现中应谨慎处理近重根，因为数值上“相近极点”和“精确重极点”的行为不同。

## 时域解释

基本对应关系为

$$
\mathcal{L}^{-1}\left\{\frac{k}{s-p}\right\}=k e^{pt}.
$$

若 $p=\sigma+j\omega$ 且实值系统存在共轭项，则一对极点在时域形成衰减或增长振荡。$\sigma<0$ 表示该指数项衰减，$\sigma>0$ 表示增长；但端口模型是否可接入网络还要检查无源性、因果性和数值离散化。

对 EMT 递归卷积，连续指数核在步长 $\Delta t$ 下通常转化为递推系数，例如

$$
z_{i,k}=a_i z_{i,k-1}+b_i u_k,\quad a_i\approx e^{p_i\Delta t}.
$$

具体 $b_i$ 取决于积分规则、输入保持假设和软件实现。

## 工作流

1. 获得有理函数：来自解析传递函数、[[vector-fitting]]、频域扫描或网络等值。
2. 分离直接项：若分子阶次不低于分母阶次，先做多项式除法。
3. 求极点：计算 $D(s)$ 的根或读取拟合算法输出的极点。
4. 求留数：对单极点用留数公式，对多端口或近重极点用线性最小二乘。
5. 组合共轭项：实值时域模型应保持共轭对一致。
6. 生成时域实现：转换为状态空间、递归卷积或 companion-like 历史项。
7. 验证：检查频域拟合误差、时域波形、稳定极点、无源性和步长敏感性。

## 变体

| 变体 | 机制 | 适用场景 | 风险 |
|---|---|---|---|
| 标量部分分式 | 单输入单输出有理函数 | 传递函数、单端口阻抗 | 高阶多项式根可能病态 |
| 多端口公共极点 | 多个矩阵元素共享极点，留数为矩阵 | FDNE、宽频线路和变压器 | 留数矩阵需满足对称性和无源性要求 |
| 状态空间实现 | 把极点-留数转换为一阶状态 | EMT 时域求解 | 状态缩放影响条件数 |
| 递归卷积实现 | 把指数核转为历史递推 | 频变线路和网络等值 | 步长和积分规则影响误差 |
| 模态展开 | 按特征模式或极点解释响应 | 振荡模式识别 | 留数小不代表状态不重要 |

## 适用边界与失败模式

- 相近极点会导致留数很大且互相抵消，时域实现可能对舍入误差敏感。
- 拟合误差在频域可接受，不代表接入网络后无源或稳定。
- 不稳定极点若来自物理负阻尼、拟合噪声或数值伪影，需要分别解释，不能简单删除。
- 多端口模型的每个矩阵元素单独拟合可能破坏对称性和互易性。
- 直接把单篇算例的拟合精度、阶数或频带写成通用经验值不符合证据纪律。

## 代表性证据

- [[rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del]] 支撑“极点-留数有理函数可用于频域响应近似”的经典 VF 路线；其中数值效果应绑定原文频响、阶数和频带。
- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]] 支撑多端口频率相关网络等值需要极点-留数或状态空间实现；不能据此保证所有端口模型自动无源。
- [[partitioned-fitting-and-dc-correction-in-transmission-linecable-models-for-wideb]] 支撑线路/电缆宽频拟合中 DC 修正和分区拟合的重要性；属于具体方法证据。

## 与相关页面的关系

- [[vector-fitting]]：常见的极点和留数识别方法。
- [[least-squares-method]]：固定极点后的留数识别通常是线性最小二乘问题。
- [[passivity-enforcement]]：检查和修正接入网络后的能量一致性。
- [[frequency-dependent-line-model]]：使用有理近似实现频变线路。
- [[companion-model]]：解释 EMT 历史项和离散时域接口。
- [[numerical-laplace-transform]]：提供频域与时域转换的另一类数值路线。
