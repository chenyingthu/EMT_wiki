---
title: "Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for Faster-Than-SCADA Applications"
type: source
authors: ['未知']
year: 2021
journal: "IEEE Transactions on Power Systems;2021;36;3;10.1109/TPWRS.2020.3038850"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_19/tpwrs.2020.3038850.pdf.pdf"]
---

# Flexible Time-Stepping Dynamic Emulation of AC/DC Grid for Faster-Than-SCADA Applications

**作者**: 
**年份**: 2021
**来源**: `19、20、21/EMT_task_19/tpwrs.2020.3038850.pdf.pdf`

## 摘要

—Dynamic simulation of the integrated AC/DC grids playsacrucialroleintheenergycontrolcenter.Inthiswork,afaster than supervisory control and data acquisition (FT-SCADA) emu- lation based on ﬂexible time-stepping (FTS) algorithm is proposed for the energy control center to predict and mitigate the impacts after serious disturbances using ﬁeld-programmable gate arrays (FPGAs). To gain a high acceleration over SCADA/real-time, the FTS-based dynamic emulation is applied to the AC grid, which is the IEEE 118-bus system where a 9th-order synchronous ma- chine model is adopted. Meanwhile, the electromagnetic transient (EMT) emulation revealing the exact performance of the DC grid provides an insight into the impact on its AC counterpart. A power- voltage interface is inserted between the AC and DC

## 核心贡献


- 提出基于灵活步长的AC/DC协同仿真算法，实现超SCADA速度的动态预测
- 设计AC动态与DC电磁暂态混合架构，通过功率电压接口实现FPGA并行加速
- 采用显式RK4求解非线性微分代数方程，结合局部自适应步长提升硬件效率


## 使用的方法


- [[灵活步长算法|灵活步长算法]]
- [[四阶龙格库塔法|四阶龙格库塔法]]
- [[显式积分法|显式积分法]]
- [[fpga硬件并行仿真|FPGA硬件并行仿真]]
- [[emt-动态协同仿真|EMT-动态协同仿真]]
- [[功率-电压接口技术|功率-电压接口技术]]


## 涉及的模型


- [[ieee-118节点系统|IEEE 118节点系统]]
- [[9阶同步电机模型|9阶同步电机模型]]
- [[vsc-hvdc|VSC-HVDC]]
- [[交流输电网络|交流输电网络]]
- [[混合ac-dc电网|混合AC/DC电网]]


## 相关主题


- [[超scada仿真|超SCADA仿真]]
- [[实时仿真|实时仿真]]
- [[硬件仿真|硬件仿真]]
- [[并行计算|并行计算]]
- [[动态安全评估|动态安全评估]]
- [[交直流混合电网|交直流混合电网]]
- [[暂态稳定分析|暂态稳定分析]]
- [[预测控制|预测控制]]


## 主要发现


- 所提算法在IEEE 118节点系统中实现超SCADA 101倍以上的加速比
- 仿真结果与DSATools/TSAT离线工具对比验证了混合架构的高精度
- FPGA并行架构有效支撑严重扰动下电网状态的快速预测与预防控制决策


