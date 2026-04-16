---
title: "EMU-traction network modeling of high speed railway and electromagnetic transient influence consider"
type: source
authors: ['未知']
year: 2025
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/17/Song和Liu - 2018 - EMU-traction network modeling of high speed railway and electromagnetic transient influence consider.pdf"]
---

# EMU-traction network modeling of high speed railway and electromagnetic transient influence consider

**作者**: 
**年份**: 2025
**来源**: `17/Song和Liu - 2018 - EMU-traction network modeling of high speed railway and electromagnetic transient influence consider.pdf`

## 摘要

摘要: 针对高铁弓网燃弧造成的电磁暂态现象，基于多导体传输线( MTL) 理论对计及弓网二次燃弧的牵引网 回路进行车－网建模仿真研究。推导高铁全并联自耦变压器( AT) 供电方式下牵引网MTL 链式集总π 型网 络矩阵参数; 根据CＲH2 型动车组结构参数，结合动车组实际运行过程中车体、钢轨、牵引网三者之间的相对 位置分布及电气参数关系，在MATLAB /Simulink 上建立精确的高速铁路车－网链式参数仿真模型。以二次 Project supported by the Joint Funds of the National Natural Sci-

## 核心贡献


- 推导全并联AT供电下牵引网MTL链式集总π型网络矩阵参数，实现多导体耦合精确建模
- 结合CRH2车体结构与轮对分布，建立计及相对位置的高铁车网链式参数仿真模型
- 引入Habedank等效电弧模型，实现弓网一次及二次燃弧电磁暂态过程的动态仿真


## 使用的方法


- [[多导体传输线-mtl-理论|多导体传输线(MTL)理论]]
- [[链式集总π型网络参数推导|链式集总π型网络参数推导]]
- [[dubanton复镜像法|Dubanton复镜像法]]
- [[habedank等效电弧模型|Habedank等效电弧模型]]
- [[快速傅里叶变换-fft-分析|快速傅里叶变换(FFT)分析]]
- [[matlab-simulink仿真|MATLAB/Simulink仿真]]


## 涉及的模型


- [[牵引网-多导体传输线|牵引网(多导体传输线)]]
- [[crh2型动车组|CRH2型动车组]]
- [[自耦变压器-at-供电系统|自耦变压器(AT)供电系统]]
- [[弓网离线电弧模型|弓网离线电弧模型]]
- [[钢轨与接地回流系统|钢轨与接地回流系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[弓网燃弧分析|弓网燃弧分析]]
- [[牵引网建模|牵引网建模]]
- [[谐波与过电压分析|谐波与过电压分析]]
- [[动车组接地回流|动车组接地回流]]
- [[高速铁路供电系统|高速铁路供电系统]]


## 主要发现


- 二次燃弧使牵引网电压谐波总畸变率由1.52%升至9.55%，畸变显著加剧
- 二次燃弧在动车受流处引发高达95kV的暂态过电压，并沿线路两侧逐渐衰减
- 多次燃弧导致畸变电压在车网回路中叠加振荡，严重威胁牵引网及车载设备安全


