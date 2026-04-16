---
title: "Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models"
type: source
authors: ['未知']
year: 2023
journal: "IEEE Open Journal of Power Electronics;2023;4; ;10.1109/OJPEL.2023.3297449"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/32/Zhang 等 - 2023 - Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models.pdf"]
---

# Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models

**作者**: 
**年份**: 2023
**来源**: `32/Zhang 等 - 2023 - Real-Time HIL Emulation of DRM With Machine Learning Accelerated WBG Device Models.pdf`

## 摘要

The proliferation of artiﬁcial intelligence (AI) has opened up new avenues for the modeling of power electronics with ultra-fast transient responses, such as wide-bandgap (WBG) devices. This arti- cle highlights the signiﬁcance of ultra-fast transient device-level hardware emulation for the DC railway microgrid (DRM) in real-time. To this end, the proposed approach partitions the DRM power system by transmission line method (TLM) and employs gated recurrent unit (GRU) and electromagnetic transient (EMT) modeling techniques for system-level subsystems. Meanwhile, for WBG devices, gallium nitride (GaN) high electron mobility transistors (HEMT) and silicon carbide (SiC) insulated gate bipolar transistors (IGBT) are modeled using a novel physical feature neuron network (PFNN), which offers hig

## 核心贡献


- 提出物理特征神经网络模型，实现宽禁带器件纳秒级变步长高精度建模
- 采用传输线法对直流铁路微电网解耦，结合门控循环单元实现系统级并行仿真
- 构建基于FPGA的器件级机器学习与系统级电磁暂态混合实时硬件在环架构


## 使用的方法


- [[传输线法-tlm|传输线法(TLM)]]
- [[门控循环单元-gru|门控循环单元(GRU)]]
- [[电磁暂态-emt-建模|电磁暂态(EMT)建模]]
- [[物理特征神经网络-pfnn|物理特征神经网络(PFNN)]]
- [[fpga并行计算|FPGA并行计算]]
- [[硬件在环-hil-仿真|硬件在环(HIL)仿真]]


## 涉及的模型


- [[直流铁路微电网-drm|直流铁路微电网(DRM)]]
- [[氮化镓高电子迁移率晶体管-gan-hemt|氮化镓高电子迁移率晶体管(GaN HEMT)]]
- [[碳化硅绝缘栅双极型晶体管-sic-igbt|碳化硅绝缘栅双极型晶体管(SiC IGBT)]]
- [[宽禁带功率器件|宽禁带功率器件]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[硬件在环|硬件在环]]
- [[机器学习加速建模|机器学习加速建模]]
- [[变步长仿真|变步长仿真]]
- [[fpga并行架构|FPGA并行架构]]
- [[功率器件级建模|功率器件级建模]]


## 主要发现


- 新模型实现纳秒级变步长仿真，精度与商业离线软件结果高度一致
- 相比传统固定步长网络，新方法显著提升宽禁带器件超快暂态过程的计算效率
- 基于传输线解耦与FPGA并行架构，成功实现直流微电网系统级实时稳定运行


