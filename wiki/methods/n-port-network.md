---
title: "N 端口网络方法 (N-Port Network)"
type: method
tags: [n-port-network, fdne, network-equivalent, multi-port, reduction]
created: "2026-05-05"
updated: "2026-05-06"
---

# N 端口网络方法 (N-Port Network)

## 定义与边界

N 端口网络方法是用多个电气端口来描述外部网络、设备集群或等值子系统的建模路线。它常用于频变网络等值、多端口诺顿/戴维南等值以及大型系统降阶。重点是“保留多个外部接口的端口行为”，而不是某个具体的 MMC 子模块公式。

## EMT 中的作用

在 EMT 研究中，N 端口网络方法主要用于：

- 表达大型网络的多端口频变等值；
- 为系统分区、协同仿真和外部网络缩减提供接口模型；
- 在保持端口行为的同时减少内部状态规模。

## 常见关注点

- 端口数量增加后外部接口行为的保真度；
- 频域拟合如何落回时域实现；
- 多端口等值的无源性和稳定性；
- 在系统分区或协同仿真中如何使用端口边界。

## 关键公式

多端口网络最基本的端口关系可写为：

$$
\mathbf{I}(s)=\mathbf{Y}(s)\mathbf{V}(s)
$$

其中 $\mathbf{Y}(s)$ 为多端口导纳矩阵。不同方法的关键差异在于 $\mathbf{Y}(s)$ 如何由原始网络导出、拟合和时域实现。

## 与相关方法的关系

- [[network-equivalent]]：等值建模总入口。
- [[fdne-model]]：频变网络等值背景。
- [[norton-equivalent]]：端口等值的基础形式。
- [[power-system-network]]：系统级网络背景。
- [[passivity-enforcement]]：多端口等值无源性背景。

## 代表性来源

- [[multi-port-frequency-dependent-network-equivalents-for-the-emtp-power-delivery-i]]：多端口 FDNE 背景。
- [[efficient-implementation-of-multi-port-frequency-dependent-network-equivalents-f]]：多端口频变网络等值的实现背景。
- [[a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent]]：无源性和端口等值背景。

## 证据边界

本页不写无来源拟合阶数、速度提升或统一端口数结论，必须绑定具体网络和拟合条件。

## 开放问题

- 当前页尚未继续拆分“多端口频变等值”和“更一般的 N 端口抽象网络”之间的边界。
- 端口保真度与模型阶数之间的取舍，后续仍需结合具体拟合方法展开。
