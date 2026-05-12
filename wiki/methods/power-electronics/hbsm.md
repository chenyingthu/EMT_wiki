---
title: "HBSM 入口页 (HBSM)"
type: method
tags: [hbsm, half-bridge-submodule, mmc]
created: "2026-05-05"
updated: "2026-05-12"
---

# HBSM 入口页 (HBSM)


## 定义与边界

HBSM 是 Half-Bridge Submodule 的常用缩写。在本 Wiki 中，它作为简称入口存在，用于承接缩写型链接并导向更完整的方法页。

## EMT 中的作用

HBSM 本身不是独立于半桥子模块之外的新方法，而是 MMC 子模块层 EMT 建模中的常见简称。

## 常见使用方式

- 作为半桥子模块页面的缩写入口；
- 作为论文或公式中的拓扑简称；
- 作为与 [[fbsm]]、混合 MMC 等页面对照时的短标签。

## 形式化表达

HBSM 相关建模通常仍回到半桥子模块的基本关系：

$$
v_{sm} = s\,v_c, \qquad C_{sm}\frac{dv_c}{dt}=i_c
$$

其中 $s$ 表示插入/旁路状态。这个入口页不展开更多推导，而是明确 HBSM 与正式方法页之间的对应关系。

## 相关页面

- [[half-bridge-submodule]]：半桥子模块的主要方法页。
- [[fbsm]]：全桥子模块的对照入口。
- [[nearest-level-modulation]]：说明子模块插入状态与输出电平关系。
- [[mmc-model]]：说明子模块层和整机层的关系。
- [[mbsm]]：说明统一子模块表示框架中的半桥分支。
- [[circulating-current-suppression]]：说明子模块层状态与桥臂内部控制的相关背景。

## 代表性来源

- [[an-efficient-half-bridge-mmc-model-for-emtp-type-simulation-based-on-hybrid-nume]]：半桥 MMC EMT 建模背景。
- [[the-diode-clamped-half-bridge-mmc-structure-with-internal-spontaneous-capacitor-]]：半桥子模块拓扑扩展背景。
- [[fast-electromagnetic-transient-modeling-method-for-half-bridge-type-voltage-sour]]：半桥型快速 EMT 表示背景。

## 量化性能边界

**Gao et al. (2023) 混合数值积分半桥MMC模型**：
- 梯形法与中点法组合，桥臂等效导纳在正常运行时保持恒定，避免频繁LU分解
- 交错格式（Leapfrog）解耦电容电压更新与桥臂电感方程
- 稳态误差<0.5%，暂态峰值误差<1%
- 仿真速度提升5-15倍（对比戴维南等效模型）
- CDA开销<5%
- 适用性：半桥MMC离线EMTP型仿真
- 数据缺口：仅验证半桥MMC，未覆盖全桥或混合MMC

**Zhang et al. (2023) 同步开关预测快速EMT建模**：
- 以半桥子电路为单位进行同步开关状态预测，消除迭代收敛
- 内部节点凝聚减少全局矩阵规模
- 80模块SST仿真20倍加速，波形误差<0.5%
- 验证：PSCAD/EMTDC，半桥VSC全工况
- 数据缺口：需要二极管续流路径逻辑，不能直接推广到全桥拓扑

**Xu et al. (2015) MMC高效建模方法综述**：
- 三类模型族：受控源解耦、戴维南等效（后向欧拉/梯形法）、平均值模型
- 排序复杂度从O(N²)降至O(N)
- 戴维南模型在N=200时实现15-20倍加速
- 梯形法比后向欧拉慢2倍但精度高0.2-0.4%
- 验证：48 SM/arm半桥MMC-HVDC基准，20 μs步长
- 数据缺口：综述性质，数值来自文献汇集而非统一对比测试

**Xu (2018) 二极管钳位半桥MMC自发电压均衡**：
- 增加钳位二极管+阻尼电阻每SM + 三相4套辅助电路实现自动均压
- 电压传感器减少>50%，DSP延迟降低30-50%
- 电压不均衡度1-2%，额外器件：(6N+14)二极管+4 IGBT+4电容每N SM/相
- 验证：PSCAD/EMTDC + 缩比样机
- 数据缺口：硬件方案增加额外器件成本，与软件排序方案的全面经济性对比缺失

**数据缺口声明**：HBSM的量化性能数据来自四个独立研究，各自使用不同MMC参数（SM数、步长、拓扑）和评估基准。Gao 2023、Zhang 2023、Xu 2015、Xu 2018四者的加速比和误差指标基于各自的对照模型，不能直接横向对比。不同SM数（48→80→200）下加速比的可扩展性趋势未经统一测试验证。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
