---
title: "Interfacing real-time and offline power system simulation tools using UDP or FPGA systems"
type: source
authors: ['Christian Scheibe']
year: 2022
journal: "Electric Power Systems Research, 212 (2022) 108490. doi:10.1016/j.epsr.2022.108490"
tags: ['real-time', 'fpga']
created: "2026-04-13"
sources: ["EMT_Doc/24/Scheibe 等 - 2022 - Interfacing real-time and offline power system simulation tools using UDP or FPGA systems.pdf"]
---

# Interfacing real-time and offline power system simulation tools using UDP or FPGA systems

**作者**: Christian Scheibe
**年份**: 2022
**来源**: `24/Scheibe 等 - 2022 - Interfacing real-time and offline power system simulation tools using UDP or FPGA systems.pdf`

## 摘要

0378-7796/© 2022 Elsevier B.V. All rights reserved. Interfacing real-time and offline power system simulation tools using UDP or Christian Scheibe a,d,∗, Ananya Kuri a,d, Yuyao Feng c, Le Zhao c, Xuejun Xiong c, Piergiovanni La Seta a, Xiao Peng Liang b, Johannes Knödtel d, Philipp Holzinger d, Marc Reichenbach d, a Power Technologies International Siemens AG, Erlangen, Germany

## 核心贡献


- 提出RTDS与PSS/E的EMT-RMS混合仿真接口，实现实时与离线域高效互联。
- 设计基于UDP以太网与FPGA光纤的双架构接口，平衡通信延迟与硬件成本。
- 采用DFT相量提取与后向欧拉插值算法，解决多速率仿真步长匹配问题。


## 使用的方法


- [[混合仿真|混合仿真]]
- [[离散傅里叶变换|离散傅里叶变换]]
- [[正序变换|正序变换]]
- [[后向欧拉线性插值|后向欧拉线性插值]]
- [[多速率仿真|多速率仿真]]
- [[理想变压器模型|理想变压器模型]]
- [[udp通信|UDP通信]]
- [[aurora协议|Aurora协议]]


## 涉及的模型


- [[架空线路|架空线路]]
- [[电压源模型|电压源模型]]
- [[电流源模型|电流源模型]]
- [[正序网络等值|正序网络等值]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[离线仿真|离线仿真]]
- [[混合仿真|混合仿真]]
- [[电磁暂态与机电暂态接口|电磁暂态与机电暂态接口]]
- [[暂态稳定分析|暂态稳定分析]]
- [[数据通信协议|数据通信协议]]


## 主要发现


- UDP与FPGA接口均成功实现RTDS与PSS/E的稳定数据交互与混合仿真验证。
- 纯软件UDP方案部署灵活但延迟较高，FPGA硬件方案延迟更低且需额外设备。
- 相量变换与插值算法有效克服步长差异，在架空线路测试系统中验证了接口可行性。


