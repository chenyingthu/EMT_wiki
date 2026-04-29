---
title: "EMT Wiki 索引"
type: index
created: 2026-04-13
updated: 2026-04-26
---

# EMT Wiki 索引

> 自动生成，每次 ingest 更新。

## 概览
- 总来源数：690 篇论文
- 已摄入：690 篇
- 已分析：690 篇 (100%)
- 来源页填充率：100% (核心贡献/使用的方法/涉及的模型/相关主题/主要发现 全部填充)
- 深度增强：682/682 (100%)
- 主题页：11
- 方法页：10
- 模型页：10
- 实体页：22
- 来源页：682 个活跃来源页

## 主题 (Topics)

| 页面 | 摘要 |
|------|------|
| [[co-simulation\|混合仿真]] | 机电-电磁暂态混合仿真、多速率、数模混合、频域-时域联合仿真 |
| [[real-time-simulation\|实时仿真]] | FPGA/RTDS/GPU实时仿真、硬件在环测试、时间步长约束 |
| [[dynamic-phasor\|动态相量法]] | 扩展频率范围的相量域建模、移位频率分析、宽频暂态 |
| [[parallel-computing\|并行计算]] | 空间分解、时间并行、GPU加速、多核并行 |
| [[frequency-dependent-modeling\|频率相关建模]] | 矢量拟合、频变参数、宽频阻抗建模、无源性 |
| [[network-equivalent\|网络等值]] | Ward/FDNE/Thevenin等值、参数辨识、大电网简化 |
| [[vsc-hvdc\|VSC-HVDC]] | 柔性直流输电、独立有功无功控制、多端直流 |
| [[ferroresonance\|铁磁谐振]] | 变压器非线性、铁磁谐振过电压、非线性磁化 |
| [[cable-modeling\|电缆建模]] | 地下/海底电缆、集肤效应、螺线管效应 |
| [[harmonic-analysis\|谐波分析]] | 谐波潮流、谐振频率分析、宽频暂态 |
| [[wind-farm-modeling\|风电场建模]] | DFIG/PMSG风机、等值聚合、大规模风电仿真 |

## 方法 (Methods)

| 页面 | 摘要 |
|------|------|
| [[vector-fitting\|矢量拟合]] | 频率响应的有理函数逼近算法 |
| [[average-value-model\|平均值模型]] | 换流器开关周期平均化建模 |
| [[nodal-analysis\|节点分析]] | EMTP标准求解框架、伴随电路法 |
| [[state-space-method\|状态空间法]] | 一阶微分方程组建模、矩阵指数法 |
| [[numerical-integration\|数值积分]] | 梯形法、Gear法、2S-DIRK等积分方法 |
| [[passivity-enforcement\|无源性强制]] | 确保频率相关模型稳定性的校正技术 |
| [[multirate-method\|多速率方法]] | 不同子系统不同时间步长的仿真方法 |
| [[fixed-admittance\|恒导纳模型]] | ADC模型，避免导纳矩阵重构 |
| [[interpolation-method\|插值方法]] | 多速率仿真数据同步、变步长中间值计算 |
| [[prony-analysis\|Prony分析]] | 指数信号分解、模态参数提取、系统辨识 |

## 模型 (Models)

| 页面 | 摘要 |
|------|------|
| [[mmc-model\|MMC]] | 模块化多电平换流器，HVDC主流拓扑 |
| [[transmission-line-model\|输电线路]] | Bergeron模型、频变线路、多导体线路 |
| [[transformer-model\|变压器]] | 磁滞、白盒、对偶电路、高频模型 |
| [[synchronous-machine-model\|同步电机]] | 相域/dq0/VBR模型、交叉磁化 |
| [[vsc-model\|VSC]] | 电压源换流器，两电平/三电平拓扑 |
| [[fdne-model\|FDNE]] | 频变网络等值，多端口宽频阻抗 |
| [[cable-model\|电缆]] | 地下/海底电缆，集肤效应，螺线管效应 |
| [[dfig-model\|DFIG]] | 双馈感应发电机，风电并网 |
| [[lcc-model\|LCC]] | 线路换相换流器，传统HVDC核心设备 |
| [[pmsm-model\|PMSM]] | 永磁同步电机，风力发电/电动汽车 |

## 实体 (Entities)

### 仿真工具
| 页面 | 摘要 |
|------|------|
| [[pscad-emtdc]] | 曼尼托巴大学开发的EMT仿真软件 |
| [[emtp]] | 经典EMT程序，EMTP-RV版本 |
| [[atp-emtp]] | EMTP开源免费版本 |
| [[rtds]] | 实时数字仿真器，HIL测试 |
| [[matlab-simulink]] | MATLAB/Simulink控制设计与代码生成平台 |
| [[cloudpss]] | CloudPSS云仿真平台，清华大学研发，国产EMT工具 |
| [[adpss]] | ADPSS国产电力系统仿真软件，中国电科院研发 |
| [[psmodel]] | PSModel国产超大规模电网仿真平台，国家电网研发 |
| [[comsol]] | 多物理场有限元仿真软件，变压器/电缆建模 |
| [[ansys]] | ANSYS/Maxwell电磁场有限元分析工具 |

### 机构
| 页面 | 摘要 |
|------|------|
| [[polytechnique-montreal]] | 蒙特利尔理工学院，EMTP-RV开发 |
| [[university-manitoba]] | 曼尼托巴大学，PSCAD/EMTDC开发 |
| [[manitoba-hydro]] | 曼尼托巴水电国际，PSCAD商业化 |
| [[tsinghua-university]] | 清华大学，MMC-HVDC与新能源研究重镇 |
| [[china-epri]] | 中国电力科学研究院，特高压直流与新能源仿真 |
| [[abb]] | ABB集团，HVDC技术先驱与设备制造商 |
| [[siemens]] | 西门子，HVDC Plus®技术与电力电子 |

### 学者
| 页面 | 摘要 |
|------|------|
| [[gole]] | A.M. Gole，曼尼托巴大学，PSCAD/EMTDC核心开发者 |
| [[mahseredjian]] | Jean Mahseredjian，蒙特利尔理工学院，EMTP-RV核心开发者 |
| [[bjorn-gustavsen]] | Bjørn Gustavsen，SINTEF，矢量拟合算法创始人 |
| [[adam-semlyen]] | Adam Semlyen，多伦多大学，电磁暂态理论先驱 |

### 标准组织
| 页面 | 摘要 |
|------|------|
| [[ieee]] | IEEE，电力系统标准制定与期刊发表（351次提及） |
| [[cigre]] | CIGRE，国际大电网委员会，技术报告权威（28次提及） |

## 来源 (Sources)

_共 690 篇活跃来源，另有 11 个重复来源指针，详见下方按文件夹分组_

### 按文件夹分组

| 文件夹 | 论文数 | 已摄入 | 状态 |
|--------|--------|--------|------|
| EMT_Doc/01 | 21 | 21 | ✅ |
| EMT_Doc/02 | 19 | 19 | ✅ |
| EMT_Doc/03 | 19 | 19 | ✅ |
| EMT_Doc/04 | 21 | 21 | ✅ |
| EMT_Doc/05 | 21 | 21 | ✅ |
| EMT_Doc/06 | 16 | 16 | ✅ |
| EMT_Doc/07&08 | 35 | 35 | ✅ |
| EMT_Doc/09 | 20 | 20 | ✅ |
| EMT_Doc/10 | 20 | 20 | ✅ |
| EMT_Doc/11 | 14 | 14 | ✅ |
| EMT_Doc/12 | 13 | 13 | ✅ |
| EMT_Doc/13&14 | 41 | 41 | ✅ |
| EMT_Doc/15 | 19 | 19 | ✅ |
| EMT_Doc/16 | 17 | 17 | ✅ |
| EMT_Doc/17 | 21 | 21 | ✅ |
| EMT_Doc/18 | 21 | 21 | ✅ |
| EMT_Doc/19、20、21 | 63 | 63 | ✅ |
| EMT_Doc/22 | 11 | 11 | ✅ |
| EMT_Doc/23 | 15 | 15 | ✅ |
| EMT_Doc/24 | 11 | 11 | ✅ |
| EMT_Doc/25 | 20 | 20 | ✅ |
| EMT_Doc/26 | 21 | 21 | ✅ |
| EMT_Doc/27&28 | 40 | 40 | ✅ |
| EMT_Doc/29 | 10 | 10 | ✅ |
| EMT_Doc/30 | 13 | 13 | ✅ |
| EMT_Doc/31 | 16 | 16 | ✅ |
| EMT_Doc/32 | 17 | 17 | ✅ |
| EMT_Doc/33 | 14 | 14 | ✅ |
| EMT_Doc/34 | 15 | 15 | ✅ |
| EMT_Doc/35 | 15 | 15 | ✅ |
| EMT_Doc/36 | 12 | 12 | ✅ |
| EMT_Doc/37 | 18 | 18 | ✅ |
| EMT_Doc/38 | 10 | 10 | ✅ |
| EMT_Doc/39 | 13 | 13 | ✅ |
| EMT_Doc/40 | 19 | 19 | ✅ |
| **总计** | **690** | **690** | **100%** |
