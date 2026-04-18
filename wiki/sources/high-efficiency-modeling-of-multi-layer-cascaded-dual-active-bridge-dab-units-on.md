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



## 方法细节

### 方法概述

本文提出一种面向实时仿真器的多层级联双有源桥（DAB）高效聚合建模方法。针对高频开关与子模块数量庞大导致的节点爆炸与计算瓶颈，采用两阶段聚合策略：第一阶段基于状态空间电路法，将单个DAB单元的两个H桥、交流变压器及直流隔直电容整合为单一模块，将所有交流侧节点隐藏为内部节点；第二阶段针对输入串联输出并联（ISOP）拓扑，将多个单单元模块进一步打包为多层聚合模型，仅对外暴露直流侧节点，大幅缩减网络导纳矩阵规模。结合通用换流器模型（UCM）与改进触发脉冲法（IFP），在单个仿真步长内对开关状态进行占空比平均值等效，实现精确触发，有效抑制高频下的直流偏磁，同时避免传统插值法带来的双倍CPU开销，满足实时性约束。

### 数学公式


**公式1**: $$L_t \frac{di}{dt} + R_t i = V_{md}(V_{P1}, V_{N1}, S_I) - V_f - V_{cap}$$

*DAB左侧H桥回路状态方程，描述电感电流动态与中点电压、互感电压及隔直电容电压的关系*


**公式2**: $$C_{cap} \frac{dV_{cap}}{dt} = i$$

*直流隔直电容电压动态方程，用于计算电容充放电过程及预测电流方向*


### 算法步骤

1. 初始化仿真步长与网络状态，接收外部控制器下发的触发脉冲信号，记录当前正负直流母线电压（V_P1, V_N1）及互感电压V_f。

2. 采用改进触发脉冲法（IFP），在单个仿真步长内不假设开关状态恒定，而是根据脉冲实际占空比计算该步长内的平均导通状态，生成等效开关矩阵。

3. 启动阀状态预测算法：系统遍历所有可能的开关组合状态（如'1001'等），代入描述符状态空间方程进行前向预测计算。

4. 基于状态方程求解流经隔直电容的预测电流方向，并与当前阀体实际物理导通方向进行交叉校验。

5. 若预测电流方向与阀导通方向一致，则确认该开关组合为有效物理状态；若不一致，则剔除该组合并更新等效开关矩阵。

6. 将校验后的等效开关状态代入外部网络导纳矩阵，计算历史项与节点电压，完成当前步长求解并输出至下一时刻循环。


### 关键参数

- **最小仿真步长**: 1.0 μs

- **支持最高开关频率**: 100 kHz

- **RSCAD子步节点限制**: 传统环境限制为60个节点

- **单单元对外暴露节点**: 仅4个直流侧节点（交流侧全隐藏）

- **级联拓扑类型**: 输入串联输出并联(ISOP)



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 高频稳态与暂态工况对比 | 在100 kHz开关频率与1.0 μs步长下，聚合模型与详细电力电子变压器（PET）模型波形高度吻合，变压器电流直流偏置分量被有效抑制至<0.1%，电压纹波误差<0.5%。 | 相比传统单单元模型，网络节点数量减少约80%，历史项计算时间降低超60%，在相同硬件资源下实现更高频实时仿真。 |

| 极小步长触发精度验证 | 在1.0 μs极小步长下，传统非UCM模型因离散触发不精确导致交流变压器电流产生显著直流偏移（峰值偏移>5%），UCM+IFP聚合模型偏移量稳定在0.05%以内。 | 精度达到离线插值法水平，但CPU计算开销未增加，彻底消除数值振荡，满足实时控制器硬件在环（HIL）测试要求。 |



## 量化发现

- 仿真步长可压缩至1.0 μs，支持最高100 kHz开关频率的实时电磁暂态仿真。
- 聚合模型将每个DAB单元对外暴露的节点从10个（6交流+4直流）缩减至仅4个直流节点，网络导纳矩阵规模下降超60%。
- 突破RSCAD子步环境60个节点的硬件限制，支持大规模级联拓扑实时运行，计算资源消耗降低约70%。
- UCM+IFP技术使高频开关下的变压器电流直流偏置误差控制在0.1%以内，消除传统离散触发导致的数值振荡。


## 关键公式

### DAB单单元状态空间主方程

$$L_t \frac{di}{dt} + R_t i = V_{md}(V_{P1}, V_{N1}, S_I) - V_f - V_{cap}$$

*用于在单个仿真步长内预测电感电流与电容电压动态，支撑阀状态预测算法与IFP平均等效计算*



## 验证详情

- **验证方式**: 对比仿真验证（聚合模型 vs 详细电力电子变压器PET模型）
- **测试系统**: 含前端AC-DC换流器与多层级联ISOP-DAB单元的电力电子变压器系统
- **仿真工具**: RTDS Technologies实时仿真平台（RSCAD环境）
- **验证结果**: 在稳态运行与暂态扰动工况下，聚合模型的电压、电流波形与详细模型高度一致，直流偏磁现象被有效消除，计算资源消耗大幅降低，验证了模型在百kHz级高频开关下的实时仿真精度与效率。
