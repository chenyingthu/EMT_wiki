---
title: "最近电平调制 (Nearest Level Modulation)"
type: method
tags: [nearest-level-modulation, nlm, mmc, modulation, voltage-balancing]
created: "2026-05-05"
updated: "2026-05-10"
---

# 最近电平调制 (Nearest Level Modulation)

## 1. 定义与边界

最近电平调制（Nearest Level Modulation, NLM），又称最近电平逼近控制（Nearest Level Control, NLC），是多电平换流器（尤其是MMC）中最常用的调制方法之一。其基本思想是：根据参考电压选择最接近的可用离散电平，确定当前步每个桥臂应投入的子模块数量，再结合电容电压排序或均衡逻辑决定具体哪些子模块投入/切除。

NLM 与载波移相调制（CPS-PWM）的核心区别在于：NLM 在每个控制周期直接计算投入数量，不依赖高频载波比较，因而等效开关频率较低，适合子模块数量较多（通常 N>=20）的应用场景。

**边界声明**: 本页聚焦 NLM 的调制原理、等效建模方法及其与电容电压均衡的耦合。不讨论动态相量、多速率求解或频移方法等与 NLM 无直接关联的仿真技术。

## 2. EMT 仿真中的作用

在 EMT 仿真中，NLM 涉及三个相互关联的环节：

1. **电平映射**: 将连续参考电压（由上层控制器生成）映射为离散的桥臂投入子模块数 $n_{on}(t)$。
2. **子模块选择**: 根据 $n_{on}(t)$ 和电容电压均衡策略，从桥臂中选出应投入的具体子模块。
3. **等效建模**: 在大规模系统中，NLM 的离散开关细节可通过连续等效模型替代，以换取仿真步长的放宽和计算效率的大幅提升。

NLM 的性能直接影响 MMC 的输出电压谐波含量、电容电压波动以及控制系统的动态响应时间。

## 3. 关键原理与算法

### 3.1 电平映射

参考电压 $v_{ref}$ 到投入数的映射采用取整函数：

$$n_{on} = \text{round}\left(\frac{v_{ref}}{V_c^{avg}}\right)$$

其中 $V_c^{avg}$ 为桥臂子模块电容电压平均值（或额定值 $V_{dc}/N$）。取整引入的量化误差随子模块数 $N$ 增大而减小。

### 3.2 电容电压均衡策略

NLM 必须与电压均衡算法配合，否则电容电压将发散。主流的均衡策略有三类：

**策略 A — 全量排序法**（传统）：每步对所有 $N$ 个子模块的电容电压排序。复杂度 $O(N \log N)$，在 $N$ 较大时计算负担重 [Xu 2015]。

**策略 B — 平均比较法** [Yu 2014]：计算桥臂电容电压算术平均值 $V_{avg} = (1/N)\sum V_{c,i}$，将各 SM 电压与 $V_{avg}$ 逐一比较：
- 充电时（$i_{arm}>0$）优先投入低于平均值的子模块
- 放电时（$i_{arm}<0$）优先投入高于平均值的子模块
- 通过两个调节变量设置滞环带，控制等效开关频率
复杂度降至 $O(N)$，约 5000 倍仿真加速 [Yu 2014]。

**策略 C — 双向堆排序法** [Lian 2022]：利用 NLC 只需确定 $n_{on}$ 个极值的特点，构建规模为 $K = \min(n_{on}, N-n_{on})$ 的堆。复杂度 $O(K \log K)$，最坏情况（$n_{on}=N/2$）不超过 $N/2$。

### 3.3 NLM 等效连续模型

Zhao 2023 提出将 NLM 的离散调制过程等效为连续模型，核心思想是将每个子模块的等效占空比 $d_{eq}$ 分解为：

$$d_{eq} = d_{stable} + d_{fluctuation}$$

- $d_{stable}$: 由 MMC 主控制系统的调制波直接生成，负责形成桥臂基波电压
- $d_{fluctuation}$: 通过为每个子模块独立配置直流电压闭环控制器自动产生，负责电容电压的动态均衡

该模型避免了 NLM 的载波比较与实时排序计算，可在 PSCAD/EMTDC 中用离散元件搭建，无需额外编程 [Zhao 2023]。

### 3.4 灵活切换离散化

Lian 2022 提出用参数 $\alpha$ 控制离散化方法：$\alpha=0$ 为隐式梯形法（高精度），$\alpha=1$ 为后退欧拉法（避免网络突变时的数值振荡）。当检测到桥臂投入子模块数变化时自动切换为后退欧拉法，结构稳定时恢复梯形法。

## 4. 关键公式

| 公式 | 含义 | 来源 |
|------|------|------|
| $n_{on} = \text{round}(v_{ref}/V_c^{avg})$ | 参考电压→投入数映射 | NLM 基本定义 |
| $V_{avg} = (1/N)\sum V_{c,i}$ | 桥臂平均电容电压 | [Yu 2014] |
| $d_{eq} = d_{stable} + d_{fluctuation}$ | NLM 等效占空比分解 | [Zhao 2023] |
| $v_{sm,i} = S_i v_{c,i} + v_{sw,i}$ | 子模块输出电压合成 | [Yu 2014] |
| $v_{arm} = \sum_{i=1}^{N} v_{sm,i}$ | 桥臂输出电压求和 | [Yu 2014] |
| $v_c(t) = v_c(t-\Delta t) + \frac{\Delta t}{2C}[i_c(t)+i_c(t-\Delta t)]$ | 梯形法电容更新 | [Yu 2014, Lian 2022] |
| $C \cdot \frac{u_C(t)-u_C(t-\Delta t)}{\Delta t} = \frac{(1+\alpha)i_C(t)+(1-\alpha)i_C(t-\Delta t)}{2}$ | 灵活切换离散化 | [Lian 2022] |
| $\Delta u_c(t) = i_{arm}(t)\cdot T_s / C$（投入时） | 后退欧拉电容增量 | [Xu 2015] |

## 5. 与相关方法的关系

- **[[pwm-modulation]]**: PWM/SPWM 使用高频载波比较，适合子模块数少的换流器；NLM 适合子模块数多的 MMC，等效开关频率低、谐波特性不同。
- **[[half-bridge-submodule]] / [[fbsm]]**: 子模块拓扑决定可用的电平集合，NLM 的输出电平数 = N+1（半桥）或 2N+1（全桥）。
- **[[mbsm]]**: 统一子模块表示中需将 NLM 组织为插入指数或等效电平。
- **[[mmc-model]]**: NLM 是 MMC 详细模型、戴维南等效模型和平均值模型的调制背景。
- **[[circulating-current-suppression]]**: NLM 的投入数变化影响桥臂电流中的二倍频环流分量。
- **[[average-value-model]]**: AVM 使用平均开关函数替代 NLM 过程，牺牲子模块电压细节换取系统级效率。

## 6. 适用边界与失效模式

### 适用条件
- 子模块数 N >= 20（通常建议 N >= 40 以获得可接受的谐波性能）
- 对等效开关频率要求较低的应用（如 HVDC、STATCOM 等大容量低频场景）
- 系统级 EMT 仿真中需要保留子模块电容动态但可容忍 ms 级步长

### 失效边界
- N < 10 时电平数过少，输出电压谐波畸变严重，应使用 PWM 调制
- 故障、闭锁或极端暂态中，NLM 的简化等效模型可能不足以代表所有开关细节 [Zhao 2023]
- 纯 NLM 等效连续模型不适合：开关应力分析、器件损耗评估、EMI 研究 [Yu 2014]
- 不同论文中“等效 NLM 模型”的近似范围和适用步长差异很大，不能泛化（Zhao 2023 支持 1-5ms 步长，而详细 NLM 需 μs 级步长）

### 关键假设
- 电容电压基本均衡是前提 — 若散布过大，仅靠 NLM 的最近电平选择不足以维持平衡
- 等效连续模型假设子模块间参数一致（电容值 $C$、导通电阻 $R_{on}$ 相同）

## 7. 代表性来源与数值证据

### 数值证据汇总

| 来源 | 关键数值 | 方法核心 |
|------|---------|---------|
| [Zhao 2023] | 步长 1-5ms, 0-500Hz 误差 <0.5%, 电容偏差 <±2%, 15-40x 加速 | 占空比分解 + 电压闭环 |
| [Yu 2014] | ~5000x 加速, 5s 暂态从 1 周→分钟, O(N) 复杂度 | 平均比较替代全排序 |
| [Lian 2022] | 导纳矩阵 11→5 阶 (54.5%), O(K log K) 堆排序, 灵活切换 | 双向堆排序 + 灵活离散 |
| [Xu 2015] | N=200 时 15-20x 加速, 梯形法比后退欧拉精度高 0.2-0.4% | Thevenin 等效 + 分组排序 |

### 代表论文

- **[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-]**: Zhao 2023, 提出基于电压闭环的 NLM 连续等效模型
- **[fast-voltage-balancing-control-and-fast]**: Yu 2014, 平均比较电压均衡 + 快速数值仿真模型
- **[a-review-of-efficient-modeling-methods-for-modular-multilevel-converters]**: Xu 2015, 综述 MMC 建模中 NLM/I 的等效方法
- **[模块化多电平换流器的高效电磁暂态仿真方法研究]**: Lian 2022, 双向堆排序 + 灵活切换提升 NLC 仿真效率

## 来源论文

| 论文 | 年份 |
|------|------|
| [[fast-voltage-balancing-control-and-fast|Fast Voltage-Balancing Control and Fast Numerical Simulation]] | 2014 |
| [[mmc-mtdc系统的电磁-机电暂态建模与实时仿真分析|MMC-MTDC系统的电磁-机电暂态建模与实时仿真分析]] | 2022 |
| [[equivalent-model-of-nearest-level-modulation-for-fast-electromagnetic-transient-|Equivalent model of nearest level modulation for fast electr]] | 2023 |