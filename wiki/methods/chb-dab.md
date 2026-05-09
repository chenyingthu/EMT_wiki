---
title: "Chb Dab"
type: method
tags: [chb-dab]
created: "2026-05-04"
updated: "2026-05-07"
---

# CHB-DAB

## 定义与边界

CHB-DAB 通常指级联 H 桥（CHB）与双有源桥（DAB）相关的隔离型 DC/DC 或电力电子变换单元组合。当前 Wiki 的主说明应收敛到 [[dual-active-bridge]]；本页作为 `chb-dab` 的短别名入口。

本页不把 CHB-DAB 扩展成多导体输电线路、频变大地回路或一般 EMT 求解方法页面。

## 核心机制

DAB 变换器通过原副边 H 桥之间移相角控制传输功率的大小和方向。在忽略变压器损耗和寄生电阻的条件下，传输功率方程为：

$$
P = \frac{n V_1 V_2 \phi (\pi - |\phi|)}{2\pi^2 f_s L_k}
$$

其中 $V_1$ 为原边 H 桥直流侧电压，$n V_2$ 为折算到原边的副边电压，$\phi$ 为原副边之间的移相角，$f_s$ 为开关频率，$L_k$ 为高频变压器的等效漏感。功率传输方向由 $\phi$ 的符号决定。

## 概念边界

- DAB 的相移控制、高频变压器漏感和双向 DC/DC 接口见 [[dual-active-bridge]]。
- 固态变压器或多桥电力电子变压器背景见 [[solid-state-transformer]] 和 [[pet]]。
- 设备控制与调制边界见 [[power-electronics-control]]、[[pwm-modulation]] 和 [[dc-dc-converter]]。
- 若页面需要讨论级联 H 桥本身，应绑定具体拓扑或来源，不在本别名页展开。

## 链接用法

已有文献或断链使用 `[[chb-dab]]` 时可保留链接到本页；新技术说明应优先链接 [[dual-active-bridge]]，并在需要时补充具体 source 页。

## 代表性来源

- [[dual-active-bridge]]：DAB 的主 canonical 页面。
- [[high-efficiency-modeling-of-multi-layer-cascaded-dual-active-bridge-dab-units-on]]：多层级 DAB 建模背景。
- [[simplified-emt-model-of-multiple-active-bridge-based-power-electronic-transforme]]：多有源桥/电力电子变压器简化 EMT 模型背景。

## 证据边界

本页不保留无来源公式、效率、功率密度、开关频率或实时性声明。CHB-DAB 的任何数值结论必须回到具体拓扑、调制方式、器件参数和来源页。
