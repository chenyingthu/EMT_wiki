---
title: "接地系统 (Grounding System)"
type: model
tags: [grounding, earthing, soil, frequency-dependent, step-voltage, touch-voltage]
created: "2026-04-29"
---

# 接地系统 (Grounding System)


```mermaid
graph TD
    subgraph Ncmp[接地系统 (Grounding System)]
        N0[**工作接地**: 系统中性点接地]
        N1[**保护接地**: 设备外壳接地]
        N2[**防雷接地**: 避雷针/线接地]
        N3[**信号接地**: 弱电系统接地]
    end
```


## 定义与概述

接地系统是电力系统安全运行的重要保障，提供故障电流通路、限制过电压、保障人身和设备安全。接地系统模型需要考虑土壤电阻率、接地极几何形状、频变特性等因素。本模型涵盖均匀土壤和分层土壤模型、接地电阻计算、跨步电压和接触电压分析、频变接地阻抗，适用于变电站接地网设计和雷电过电压分析。

## 1. 物理对象概述

### 1.1 功能与作用

接地系统是电力系统安全运行的重要保障：

**核心功能**：
- **故障电流疏散**：提供低阻抗路径，快速清除故障
- **过电压保护**：限制雷电和操作过电压
- **人身安全**：限制接触电压和跨步电压
- **设备保护**：提供等电位连接，防止地电位升高损坏设备
- **参考电位**：为控制和测量系统提供零电位参考

### 1.2 接地类型

| 类型 | 定义 | 应用场景 |
|------|------|---------|
| **工作接地** | 系统中性点接地 | 变压器中性点、发电机中性点 |
| **保护接地** | 设备外壳接地 | 开关柜、变压器外壳、杆塔 |
| **防雷接地** | 避雷针/线接地 | 变电站、线路杆塔 |
| **信号接地** | 弱电系统接地 | 通信、控制、测量系统 |

### 1.3 接地装置类型

**自然接地体**：
- 金属管道（水管、油管）
- 电缆金属外皮
- 建筑物钢筋

**人工接地体**：
- **垂直接地极**：钢管/角钢/铜棒，长度2.5-3m
- **水平接地极**：扁钢/圆钢，埋深0.6-0.8m
- **接地网**：变电站主接地网，网格5-10m
- **放射形接地**：线路杆塔，3-8根放射线

## 2. 物理模型与数学描述

### 2.1 接地电阻

**垂直接地极**（均匀土壤）：
$$
R = \frac{\rho}{2\pi L}\ln\frac{4L}{d}$$

**水平接地极**：
$$
R = \frac{\rho}{2\pi L}\ln\frac{L^2}{hd}$$

**接地网**：
$$
R = \frac{\rho}{4}\sqrt{\frac{\pi}{A}} + \frac{\rho}{L_{total}}$$

其中，$\rho$为土壤电阻率，$L$为接地极长度，$d$为等效直径，$h$为埋深，$A$为接地网面积。

### 2.2 跨步电压和接触电压

**跨步电压**（两脚间）：
$$
E_{step} = \frac{\rho I}{2\pi}\left(\frac{1}{x} - \frac{1}{x+s}\right)$$

**接触电压**（手脚间）：
$$
E_{touch} = \frac{\rho I}{2\pi}\left(\frac{1}{2x} + \frac{1}{D}\right)$$

其中，$s = 1m$为步距，$D$为接地网等效直径。

**安全限值**（IEEE 80）：
- 跨步电压：$E_{step} \leq \frac{116 + 0.7\rho_s}{\sqrt{t}}$
- 接触电压：$E_{touch} \leq \frac{116 + 1.5\rho_s}{\sqrt{t}}$

## 3. 频变特性

**接地阻抗频变**：
- 高频时：集肤效应显著，有效截面积减小
- 土壤频变：土壤介电常数和电导率随频率变化
- 接地阻抗：$Z_g(f) = R_g + j\omega L_g$

**时域模型**：
通过矢量拟合建立有理函数模型：
$$
Z_g(s) = R_0 + \sum_{k=1}^{N}\frac{R_k}{s - p_k}$$

## 4. 适用边界

**适用场景**：
- 变电站接地网设计
- 线路杆塔接地
- 雷电过电压分析
- 故障电流分布计算
- 人身安全评估

**模型限制**：
- 土壤均匀性假设
- 忽略化学腐蚀影响
- 季节性变化
- 接地极间互耦

## 代表性来源

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| A Accurate and Efficient Method for Transient Analysis of Substation Grounding System | 2021 | 提出基于复镜像法与矢量拟合的变电站接地系统暂态分析方法，实现宽频接地阻抗建模 |
| Frequency-Dependent Impedance of Grounding Systems | 2016 | 建立考虑土壤频变特性的接地系统频变阻抗模型，分析高频雷电流下的接地响应 |
| Earthed Systems Modeling for Power System Transient Analysis | 2009 | 开发适用于EMT仿真的接地系统多端口等值模型，处理大型接地网的计算效率问题 |

## 相关方法
- [[vector-fitting|矢量拟合]] - 接地阻抗频变拟合
- [[nodal-analysis|节点分析]] - 接地网节点分析
- [[state-space-method|状态空间法]] - 频变接地状态实现
- [[frequency-dependent-modeling|频率相关建模]] - 宽频接地建模
- [[numerical-integration|数值积分]] - 雷电响应仿真

## 相关模型
- [[cable-model|电缆模型]] - 电缆金属护套接地
- [[transformer-model|变压器模型]] - 变压器中性点接地
- [[transmission-line-model|输电线路模型]] - 杆塔接地
- [[surge-arrester-model|避雷器]] - 防雷接地

## 相关主题
- [[frequency-dependent-modeling]] - 频变接地建模
- [[harmonic-analysis]] - 接地谐波阻抗
- [[real-time-simulation]] - 接地系统实时仿真
- [[network-equivalent]] - 接地网等值

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
