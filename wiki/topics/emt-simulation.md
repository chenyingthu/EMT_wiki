---
title: "EMT Simulation (电磁暂态仿真)"
type: topic
tags: [emt, electromagnetic-transient, time-domain, simulation, power-system]
created: "2026-05-02"
---

# EMT Simulation (电磁暂态仿真)

## 概述

电磁暂态(EMT)仿真是电力系统分析的重要工具，通过求解描述网络动态行为的微分方程组，模拟电力系统在各种扰动下的暂态过程。EMT仿真能够详细模拟电力电子开关动作、故障暂态、雷电冲击等快速电磁过程，时间尺度从微秒到数秒。

## 基本原理

### 数学基础
EMT仿真基于以下基本方程：
- **基尔霍夫定律**: KCL和KVL
- **元件特性**: 电阻、电感、电容的微分方程
- **电磁耦合**: 变压器、线路的耦合关系

状态方程形式：
$$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$$
$$\mathbf{y} = \mathbf{C}\mathbf{x} + \mathbf{D}\mathbf{u}$$

### 数值积分
- [[trapezoidal-rule]] - 梯形法则
- [[backward-euler]] - 后向欧拉
- [[numerical-integration]] - 数值积分
- 步长: 微秒级到毫秒级

### 求解方法
- **节点导纳法**: [[nodal-admittance-matrix]]
- **状态空间法**: [[state-space-method]]
- **混合法**: 结合两者优势

## 建模特点

### 详细程度
- **开关器件**: IGBT、晶闸管详细模型
- [[ideal-switch-model]] - 理想开关
- [[detailed-switch-model]] - 详细开关
- **分布参数**: 输电线路行波模型
- [[transmission-line-model]] - 线路模型

### 非线性处理
- **饱和**: 变压器磁饱和
- [[magnetic-saturation-modeling]] - 磁饱和
- **电弧**: 断路器电弧模型
- `arcing-model` - 电弧模型

### 控制系统
- **详细控制**: 控制器完整实现
- `control-system-modeling` - 控制系统
- **采样**: 离散时间控制
- `discrete-control` - 离散控制

## 时间尺度

### EMT范围
- **雷电**: 微秒级(μs)
- **开关**: 毫秒级(ms)
- **故障**: 周波级(10-100ms)
- **机电**: 百毫秒到秒级

### 与机电暂态对比
| 特性 | EMT | 机电暂态 |
|------|-----|----------|
| 时间步长 | μs-ms | ms-10ms |
| 网络模型 | 三相详细 | 正序简化 |
| 电机模型 | 详细 | 经典/简化 |
| 开关 | 详细 | 平均值 |
| 计算量 | 大 | 小 |

### 混合仿真
- [[hybrid-simulation]] - 混合仿真
- [[co-simulation]] - 联合仿真
- **接口**: EMT-机电暂态接口

## 主要应用

### 过电压分析
- **操作过电压**: 开关操作
- [[switching-transient]] - 开关过电压
- **雷电过电压**: 雷击影响
- [[lightning-overvoltage]] - 雷电过电压
- **谐振过电压**: 系统谐振
- [[analysis-and-mitigation-of-subsynchronous-resonance-in-series-compensated-wind-p]] - 谐振

### 电力电子
- **换流器**: VSC、LCC、MMC
- [[vsc-model]] - VSC换流器
- [[mmc-model]] - MMC换流器
- **FACTS**: SVC、STATCOM
- [[facts]] - 灵活交流输电

### 继电保护
- **保护测试**: 保护定值验证
- `relay-testing` - 保护测试
- **故障分析**: 复杂故障
- [[fault-analysis]] - 故障分析

### 可再生能源
- **风机**: 全功率/双馈
- [[real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp]] - 风力发电机
- **光伏**: 逆变器控制
- `pv-model` - 光伏模型

## 商业软件

### PSCAD/EMTDC
- **特点**: 图形化、易用
- **元件库**: 丰富的元件库
- **自定义**: Fortran/C自定义模型
- **应用**: 学术研究、工业

### EMTP-RV
- **特点**: 工业标准
- **功能**: 全面的分析功能
- **模型**: 高精度模型
- **应用**: 工程咨询、规划

### MATLAB/Simulink
- **特点**: 灵活、可扩展
- **Simscape**: 物理建模
- **仿真**: 多领域联合
- **应用**: 研究、教学

### RTDS
- **特点**: 实时仿真
- [[real-time-simulation]] - 实时仿真
- **HIL**: 硬件在环测试
- [[hil-simulation]] - 硬件在环

## 建模要点

### 数据准备
- **网络数据**: 线路参数、变压器
- **设备数据**: 发电机、负荷
- **控制数据**: 控制器参数

### 步长选择
- **稳定性**: 满足数值稳定
- **精度**: 足够精度
- **效率**: 计算效率
- **原则**: 最小时间常数的1/10

### 初始条件
- [[steady-state-initialization]] - 稳态初始化
- **潮流**: 基于潮流结果
- **快照**: 保存/加载状态

## 结果分析

### 波形分析
- **时域波形**: 电压、电流波形
- **FFT分析**: 频谱分析
- `fft-analysis` - FFT分析
- **谐波**: 谐波含量

### 统计量
- **峰值**: 最大过电压
- **有效值**: RMS值
- **能量**: 能量累积

### 可视化
- **动画**: 电压分布动画
- `visualization` - 可视化
- **3D**: 三维场分布

## 并行计算
- [[parallel-computing]] - 并行计算
- [[gpu-parallel-acceleration]] - GPU加速
- **分网**: 网络分区并行
- **实时**: 实时仿真

## 发展趋势
- **大规模**: 万节点级系统
- [[large-scale-system-simulation]] - 大规模仿真
- **实时仿真**: 硬件在环
- [[real-time-simulation]] - 实时仿真
- **云仿真**: 云端计算资源

## 相关主题
- [[electromagnetic-transient]] - 电磁暂态
- [[lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t]] - 电力系统仿真
- [[lightning-transient-analysis]] - 暂态分析
- [[coupling-model-for-time-domain-analysis-of-nonparallel-overhead-wires-and-buried]] - 时域分析

## 来源论文

参见 [[index]] 获取更多EMT仿真相关文献。
