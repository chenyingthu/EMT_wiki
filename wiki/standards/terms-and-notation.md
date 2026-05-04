---
title: "术语与符号规范 (Terms and Notation Standard)"
type: reference
tags: [standards, terminology, notation, consistency]
created: "2026-05-03"
---

# 术语与符号规范 (Terms and Notation Standard)

> 本规范用于统一 EMT Wiki 全站的专业术语、数学表达和概念体系。
> 所有页面在修订时应参照本规范，确保全站表达一致。

## 1. 核心术语对照表

### 1.1 方法类术语

| 规范术语 | 别名（废弃） | 英文 | 说明 |
|---------|------------|------|------|
| 节点分析法 | 节点法、节点分析 | Nodal Analysis | 以节点电压为未知量的求解方法 |
| 状态空间法 | 状态方程法 | State-Space Method | 以一阶微分方程组描述系统动态 |
| 伴随电路 | 伴随模型、Companion Circuit | Companion Circuit | 数值积分后的等效电路模型 |
| 梯形积分法 | 梯形法、Trapezoidal Rule | Trapezoidal Rule | 二阶A稳定积分方法 |
| 后向欧拉法 | 后向Euler、后退欧拉、Backward Euler | Backward Euler | 一阶L稳定积分方法 |
| 对角隐式Runge-Kutta法 | DIRK、DI-RK | Diagonally Implicit Runge-Kutta | 隐式多阶段积分方法 |
| 多速率方法 | 多步长方法 | Multirate Method | 不同子系统使用不同时间步长 |
| 平均值模型 | 平均模型 | Average-Value Model | 开关周期平均化建模 |
| 动态相量法 | 动态相量 | Dynamic Phasor | 复包络频谱搬移建模 |
| 矢量拟合 | 向量拟合、Vector Fitting | Vector Fitting | 频率响应的有理函数逼近 |
| 无源性强制 | 无源性约束 | Passivity Enforcement | 确保频变模型稳定性 |
| 恒导纳模型 | 固定导纳 | Constant Admittance Model | 避免导纳矩阵重构的技术 |
| 频变网络等值 | FDNE | Frequency-Dependent Network Equivalent | 宽频端口等值模型 |
| 模型降阶 | 降阶模型 | Model Order Reduction | 高维模型降维 |
| 刚性系统 |  stiff system | Stiff System | 时间常数差异大的系统 |
| 临界阻尼调整 | CDA | Critical Damping Adjustment | 事件点后切换积分方法 |
| 稀疏矩阵求解 | 稀疏求解 | Sparse Matrix Solver | 利用稀疏性的矩阵求解 |
| 牛顿迭代法 | 牛顿法 | Newton-Raphson Method | 非线性方程迭代求解 |
| 开关函数法 | 开关平均 | Switching Function | 电力电子开关的占空比建模 |
| 插值方法 | 插值 | Interpolation Method | 多速率仿真数据同步 |
| 离散化方法 | 离散化 | Discretization Method | 连续系统离散化 |
| 故障分析方法 | 故障分析 | Fault Analysis | 对称分量法、故障建模 |
| 谐波分析方法 | 谐波分析 | Harmonic Analysis | 傅里叶分析、THD |
| 小信号分析 | 线性化分析 | Small-Signal Analysis | 线性化、特征值分析 |
| 参数辨识 | 参数估计 | Parameter Identification | 从数据反推模型参数 |

### 1.2 模型类术语

| 规范术语 | 别名（废弃） | 英文 | 说明 |
|---------|------------|------|------|
| 模块化多电平换流器 | MMC | Modular Multilevel Converter | HVDC主流拓扑 |
| 电压源换流器 | VSC | Voltage Source Converter | 两电平/三电平换流器 |
| 线路换相换流器 | LCC | Line-Commutated Converter | 传统HVDC核心设备 |
| 双馈感应发电机 | DFIG | Doubly-Fed Induction Generator | 风电主流机型 |
| 永磁同步发电机 | PMSM | Permanent Magnet Synchronous Machine | 直驱风力发电 |
| 输电线路模型 | 线路模型 | Transmission Line Model | Bergeron模型、频变线路 |
| 变压器模型 | 变压器 | Transformer Model | 磁滞、白盒、对偶电路 |
| 同步电机模型 | 同步机 | Synchronous Machine Model | 相域/dq0/VBR模型 |
| 感应电机模型 | 异步电机 | Induction Machine Model | 鼠笼/绕线式 |
| 电缆模型 | 电缆 | Cable Model | 地下/海底电缆 |
| 锁相环 | PLL | Phase-Locked Loop | 电网同步 |
| 下垂控制 | Droop Control | Droop Control | P-f/Q-V下垂 |
| 矢量控制 | 磁场定向控制、FOC | Vector Control / FOC | 磁场定向控制 |
| PWM调制器 | 脉宽调制 | PWM Modulator | 脉宽调制 |
| PI控制器 | 比例积分控制器 | PI Controller | 比例-积分控制器 |
| 避雷器 | 浪涌保护器 | Surge Arrester | ZnO避雷器 |
| 接地系统 | 接地网 | Grounding System | 接地网、频变土壤 |
| 负荷模型 | 负载模型 | Load Model | ZIP负荷、感应电机负荷 |
| 开关模型 | 开关 | Switch Model | 电力电子开关 |
| 二极管模型 | 二极管 | Diode Model | 功率二极管 |
| IGBT模型 | IGBT | IGBT Model | 绝缘栅双极晶体管 |
| 电容模型 | 电容 | Capacitor Model | 储能元件 |
| 电感模型 | 电感 | Inductor Model | 感性元件 |
| 电阻模型 | 电阻 | Resistor Model | 无源电阻 |
| 换流变压器 | 阀侧变压器 | Converter Transformer | HVDC专用变压器 |
| 多端直流电网 | MTDC | Multi-Terminal DC Grid | 多端直流 |
| 电力电子变压器 | PET、SST | Power Electronic Transformer | 固态变压器 |
| 电池储能系统 | BESS | Battery Energy Storage System | 锂电池储能 |
| 光伏系统 | PV系统 | PV System | 光伏阵列+逆变器 |
| 感应机模型 | 异步机 | Induction Machine | 感应电机 |

### 1.3 主题类术语

| 规范术语 | 别名（废弃） | 英文 | 说明 |
|---------|------------|------|------|
| 电磁暂态 | EMT | Electromagnetic Transient | 微秒级电磁过程 |
| 机电暂态 | RMS仿真 | Electromechanical Transient | 毫秒-秒级机电过程 |
| 混合仿真 | 联合仿真 | Co-Simulation | 多方法/多平台联合 |
| 实时仿真 | 在线仿真 | Real-Time Simulation | FPGA/RTDS/GPU实时 |
| 硬件在环仿真 | HIL | Hardware-in-the-Loop | 硬件在环测试 |
| 并行计算 | 分布式计算 | Parallel Computing | 空间/时间并行 |
| 频率相关建模 | 频变参数 | Frequency-Dependent Modeling | 集肤效应、大地回路 |
| 网络等值 | 网络简化 | Network Equivalent | Ward/FDNE/戴维南等值 |
| 铁磁谐振 | 铁谐 | Ferroresonance | 非线性磁谐振 |
| 开关暂态 | 操作过电压 | Switching Transient | 断路器操作 |
| 雷电过电压 | 雷击过电压 | Lightning Overvoltage | 直击雷、感应雷 |
| 谐波分析 | 谐波的 | Harmonic Analysis | 傅里叶、THD |
| 宽频振荡 | 次同步振荡 | Wideband Oscillation | SSO/SSCI |
| 模型验证 | 模型校验 | Model Verification | CIGRE/IEEE基准 |
| 仿真实践 | 工程指南 | Simulation Practice | 方法选择、步长 |

## 2. 数学符号规范

### 2.1 通用符号

| 符号 | 含义 | 使用示例 |
|------|------|---------|
| $t$ | 连续时间 | $v(t)$ |
| $\Delta t$ | 时间步长 | $x_{n+1} = x_n + \Delta t \cdot f$ |
| $n$ | 时间步索引 | $x_n$ 表示第 $n$ 步的值 |
| $\mathbf{x}$ | 状态向量（粗体） | $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}\mathbf{u}$ |
| $\mathbf{v}$ | 节点电压向量（粗体） | $\mathbf{Y}\mathbf{v} = \mathbf{i}$ |
| $\mathbf{i}$ | 电流向量（粗体） | $\mathbf{i} = \mathbf{Y}\mathbf{v}$ |
| $\mathbf{A}$ | 系统矩阵（大写粗体） | 状态矩阵 |
| $\mathbf{Y}$ | 导纳矩阵（大写粗体） | 节点导纳矩阵 |
| $A$ | 标量或普通矩阵（非粗体） | 特征值 $A_i$ |

### 2.2 时间步约定

**统一使用 $n$ 作为时间步索引**：
- $x_n$：第 $n$ 步的值（当前步）
- $x_{n+1}$：第 $n+1$ 步的值（下一步）
- $x_{n-1}$：第 $n-1$ 步的值（上上步）

**不推荐使用 $k$ 作为时间步索引**（$k$ 用于其他含义，如求和索引、极点索引）。

### 2.3 矩阵与向量

- **矩阵**：大写粗体 $\mathbf{A}$、$\mathbf{Y}$、$\mathbf{G}$
- **向量**：小写粗体 $\mathbf{x}$、$\mathbf{v}$、$\mathbf{i}$、$\mathbf{u}$
- **标量**：小写斜体 $x$、$v$、$i$、$L$、$C$、$R$
- **矩阵元素**：$A_{ij}$（不粗体）

### 2.4 导纳与电导

- **导纳/电导**：$G$（统一用 $G$，不混用 $Y$ 表示单个导纳）
- **导纳矩阵**：$\mathbf{Y}$ 或 $\mathbf{G}_{sys}$
- **等效电导**：$G_{eq}$
- **电纳**：$B$

### 2.5 历史源（伴随电路）

- **历史电流源**：$I_{hist}$ 或 $I_{eq}$
- **历史电压源**：$V_{hist}$ 或 $E_{eq}$
- **上一时刻**：用 $(t-\Delta t)$ 或下标 $(n-1)$ 表示

## 3. 命名约定

### 3.1 文件名

- 全部小写
- 空格用连字符 `-`
- 缩写用小写：`fdne`、`mmc`、`vsc`、`pll`
- 长名称用连字符连接：`nodal-analysis`、`state-space-method`

### 3.2 Wikilink

- **目标页存在时**：使用 `[[link-name]]` 格式
- **需要显示文本时**：使用 `[[link-name|显示文本]]` 格式
- **显示文本统一用中文**：`[[nodal-analysis|节点分析法]]`
- **不存在的页面**：不使用 wikilink，改为纯文本

### 3.3 术语首次出现

首次出现时统一格式：`中文术语（English Term）`，例如：
- 节点分析法（Nodal Analysis）
- 状态空间法（State-Space Method）
- 伴随电路（Companion Circuit）

后续出现时只用中文术语，不再重复英文。

## 4. 内容结构规范

### 4.1 页面基本结构

每个页面应包含以下章节（按顺序）：

1. **概述**：定义、作用、在EMT中的地位
2. **核心原理**：数学推导、公式、算法步骤
3. **适用边界**：适用场景、不适用场景、注意事项
4. **技术演进脉络**（可选）：关键时间节点
5. **关键发现汇总**（可选）：重要结论
6. **相关方法/模型/主题**：wikilink 交叉引用
7. **来源论文**：支撑文献列表

### 4.2 深度增强标记

深度增强内容使用HTML注释标记：

```markdown
<!-- deep-enrich:start -->
## 深度增强内容
...
<!-- deep-enrich:end -->
```

**注意**：只替换标记内的内容，保留标记外的手动编辑。

### 4.3 表格规范

- 所有表格使用 Markdown 表格格式
- 表头与数据间用 `|---|` 分隔
- 统一使用 `$...$` 行内公式，不使用 `$$...$$` 块级公式（除非公式特别长）
- 多行公式使用 `aligned` 环境

## 5. 语言风格规范

### 5.1 中文表达

- 使用简体中文
- 专业术语使用规范中文译名
- 避免口语化表达
- 句子简洁，避免过长复合句

### 5.2 英文术语

- 首次出现时标注英文
- 此后正文只用中文
- 公式中的变量可使用英文符号（标准数学符号）
- 不翻译标准缩写：EMT、HVDC、MMC、VSC、PLL、PI、PWM

### 5.3 禁止使用的词汇

- " magnificent "、" blazingly fast "、" 100% secure " 等营销用语
- 没有证据支持的百分比或指标
- " 显然 "、" 容易证明 " 等跳过推导的表述

## 6. 修订检查清单

修订页面时，逐项检查：

- [ ] 术语是否使用规范名称（参照第1节）
- [ ] 符号是否与规范一致（参照第2节）
- [ ] 文件名和 wikilink 是否符合命名约定（参照第3节）
- [ ] 页面结构是否完整（参照第4节）
- [ ] 公式格式是否统一（行内 `$...$`，块级 `aligned`）
- [ ] 中文表达是否规范（参照第5节）
- [ ] 交叉引用是否指向存在的页面
- [ ] 数值结果是否有来源或标注"据方法推断"

---

*本规范于 2026-05-03 创建，后续修订时应同步更新。*
