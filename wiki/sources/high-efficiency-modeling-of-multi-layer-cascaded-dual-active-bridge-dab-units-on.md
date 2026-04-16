---
title: "High Efficiency Modeling of Multi-Layer Cascaded Dual-Active-Bridge (DAB) Units on Real-time Simulator"
type: source
authors: ['未知']
year: 2024
journal: "2024 IEEE Power & Energy Society General Meeting (PESGM);2024; ; ;10.1109/PESGM51994.2024.10688518"
tags: ['real-time']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_21/Qi 等 - 2024 - High Efficiency Modeling of Multi-Layer Cascaded Dual-Active-Bridge (DAB) Units on Real-time Simulat.pdf"]
---

# High Efficiency Modeling of Multi-Layer Cascaded Dual-Active-Bridge (DAB) Units on Real-time Simulator

**作者**: 
**年份**: 2024
**来源**: `19、20、21/EMT_task_21/Qi 等 - 2024 - High Efficiency Modeling of Multi-Layer Cascaded Dual-Active-Bridge (DAB) Units on Real-time Simulat.pdf`

## 摘要

²0RGHOLQJ'XDO$FWLYH%ULGJH'$%WRSRORJLHVLQD UHDOWLPHVLPXODWRUSUHVHQWVFKDOOHQJHGXHWRWKHKLJKVZLWFKLQJ IUHTXHQF\ DQG WKH VXEVWDQWLDO QXPEHU RI VXEPRGXOHV 7KLV UHTXLUHVERWKWKHILULQJSXOVHV¶SUHFLVLRQDQGKLJKVSHHGPDWUL[ FRPSXWDWLRQ,QWKLVSDSHUDQDJJUHJDWHGPRGHOLVSURSRVHGIRU DW\SLFDO'XDO$FWLYH%ULGJH'$%FLUFXLWXVLQJWKHVWDWHVSDFH FLUFXLWDSSURDFK,WDFFXUDWHO\LPSOHPHQWVWKHGXW\F\FOHRIWKH ILULQJ SXOVHV DQG FRQVHTXHQWO\ HQKDQFHV DFFXUDF\ 7KH WZR + EULGJH FRQYHUWHUV DQG WKH DF WUDQVIRUPHU ZLWK WKH EORFNLQJ FDSDFLWRUV DUH FRQVROLGDWHG LQWR D VLQJOHXQLW 7R DGGUHVV VFHQDULRV LQYROYLQJ PXOWLOHYHO FDVFDGHG '$% XQLWV ZLWK LQSXW VHULHVRXWSXWSDUDOOHO,623WKHPXOWLSOHVLQJOHXQLWEORFNVDUH IXUWKHU SDF

## 核心贡献


- 提出基于状态空间的DAB聚合模型，整合H桥与变压器并隐藏内部节点。
- 开发级联ISOP拓扑多层聚合模型，仅暴露直流节点，大幅缩减导纳矩阵规模。
- 结合UCM与IFP技术实现占空级精确触发，有效抑制高频开关下的直流偏磁。


## 使用的方法


- [[状态空间电路法|状态空间电路法]]
- [[通用换流器模型-ucm|通用换流器模型(UCM)]]
- [[改进触发脉冲法-ifp|改进触发脉冲法(IFP)]]
- [[描述符状态空间建模|描述符状态空间建模]]
- [[阀状态预测算法|阀状态预测算法]]
- [[聚合建模技术|聚合建模技术]]


## 涉及的模型


- [[双有源桥-dab|双有源桥(DAB)]]
- [[h桥换流器|H桥换流器]]
- [[交流变压器|交流变压器]]
- [[直流隔直电容|直流隔直电容]]
- [[isop级联dab单元|ISOP级联DAB单元]]
- [[电力电子变压器-pet|电力电子变压器(PET)]]


## 相关主题


- [[实时仿真|实时仿真]]
- [[电磁暂态仿真|电磁暂态仿真]]
- [[高频开关建模|高频开关建模]]
- [[电力电子聚合建模|电力电子聚合建模]]
- [[节点导纳矩阵优化|节点导纳矩阵优化]]
- [[直流偏磁抑制|直流偏磁抑制]]


## 主要发现


- 聚合模型显著节省电气节点与历史项计算时间，降低实时仿真硬件资源占用。
- 仿真步长可降至1至2微秒，支持高达100kHz开关频率的精确实时建模。
- 稳态与暂态仿真结果与详细单单元模型高度一致，验证了聚合方法的准确性。


