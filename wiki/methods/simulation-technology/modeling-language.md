---
title: "建模语言 (Modeling Language)"
type: method
tags: [modeling, language, modelica, cim, description, equation-based, object-oriented, declarative, netlist, fmi]
created: "2026-05-02"
updated: "2026-05-19"
---

# 建模语言 (Modeling Language)

## 定义与边界

建模语言（Modeling Language）是在仿真工具、模型库或数据交换流程中描述元件、拓扑、参数、方程和接口的形式化表达。它可以是方程式语言、图形框图语言、网表格式、数据交换标准或工具内置脚本语言。

在 EMT Wiki 中，建模语言页面关注"模型如何被表达和交换"，不直接评价某个工具的求解器性能，也不把语言能力等同于模型已被验证。一个模型用 Modelica、CIM、EMTP 卡片、PSCAD 自定义模块或 MATLAB/Simulink 框图表达，只说明它有了可被工具读取的形式；其 EMT 可信度仍取决于方程、参数、初始化、求解器设置和验证证据。

## EMT 中的角色

建模语言在 EMT 工作流中主要承担四类任务：

- **结构描述**：定义节点、支路、端口、控制模块和层级组件。
- **方程描述**：写出元件伏安关系、状态方程、控制方程或事件逻辑。
- **数据交换**：在规划、潮流、机电暂态、EMT 和资产系统之间传递拓扑与参数。
- **自动化生成**：从模板、参数表或图形模型生成仿真输入文件、代码或网表。

这些任务的风险不同。结构描述可能丢失控制细节；方程描述可能与目标求解器的离散化不一致；数据交换可能发生单位、坐标系或设备语义错配；自动生成流程可能生成语法正确但物理边界错误的模型。

## 五类建模语言体系

### 方程式语言（Equation-Based Languages）

方程式语言以变量和方程为核心，适合描述多物理域系统和可复用组件。例如电阻元件可写成：

```modelica
model Resistor
  parameter Real R;
  Real v;
  Real i;
equation
  v = R * i;
end Resistor;
```

这种表达强调物理关系而不是求解顺序。用于 EMT 时，需要进一步说明连接器方向、参考节点、状态选择、事件处理和目标工具如何离散这些方程。

#### Modelica 语言体系

Modelica 是电力系统 EMT 领域最重要的方程式语言，其核心特征是**声明式、面向对象、方程导向**的非因果建模范式[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。

**Modelica 编译器的工作流程**（以 MSEMT 库为例）：

1. **扁平化（Flattening）**：展开所有继承类和子组件层次结构，将 connect 语句转换为等式约束，输出完整隐式 DAE 系统：

$$F(x, \dot{x}, y, t) = 0$$

其中 $x$ 为微分变量（状态），$y$ 为代数变量，$t$ 为时间。

2. **结构分析与匹配（Structural Analysis）**：构建结构 Jacobian 矩阵，分析各方程对变量及其导数的依赖关系，识别微分变量和代数变量[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]：

$$\frac{partial F}{partial dot{x}} cdot dot{x} + frac{partial F}{partial x} cdot x + frac{partial F}{partial y} cdot y = 0$$

3. **BLT 分块排序（Block Lower Triangular）**：应用 Tarjan 强连通分量算法将方程系统分解为块下三角形式，将大问题分解为可顺序求解的独立子块。联立求解的方程维度可降低至原规模的 **10-30%**（取决于网络拓扑稀疏性）[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。

4. **撕裂算法（Tearing）**：针对 BLT 排序后仍存在的大型代数环，智能选择撕裂变量将环打破，将非线性系统求解维度显著降低[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。

5. **指标约简（Index Reduction）**：使用 Pantelides 算法将高阶 DAE（index > 1）转换为 index-1 形式，确保系统可解性[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。

6. **代码生成与数值积分**：生成高效 C 语言求解代码，链接 DASSL 或 IDA 求解器，采用变阶（1-5 阶）变步长 BDF 积分处理刚性系统[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。

**Modelica 的 EMT 加速优化**：针对大规模输电线路模型，Masoom 等（2022）提出基于空间数据局部性的优化策略[[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-]]。其核心思想是将 $n$ 条三相输电线路合并为"线路块模型"，将端电压、电流及历史电流变量重构为长度为 $3n$ 的一维数组：

- 宽频（WB）线路块：CPU 时间从 9682 s 降至 6117 s（**提速 1.58 倍**），DAE 方程数减少 19.9%
- 恒定参数（CP）线路块：CPU 时间从 374.3 s 降至 215.7 s（**提速 1.74 倍**），DAE 方程数减少 17.8%

对 CP 线路，通过 Modelica external 接口调用向量化 C 函数处理延迟历史，替代大量标量 `delay()` 调用[[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-]]。

**混合 C++/Modelica 架构**：Dynaωo 平台采用虚拟方程预编译策略——在编译阶段临时添加虚构方程（如电流方程）使非方阵模型可编译，编译后移除生成预编译库[[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat]]。该方法：

- 在 230 kV 变电站背对背电容器组投切测试中，成功分辨 **340 Hz 低频振荡、8220 Hz 高频振荡和 27.26 kHz 超高频分量**
- IDA 求解器容差 1e-6，与 EMTP 参考结果误差 < 0.1%[[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat]]

#### Julia 语言体系

Julia 作为通用高级语言，同样可用于 EMT 仿真平台开发。JSEMT 平台采用改进增广节点分析法（MANA）[[a-julia-based-simulation-platform-for-power-system-transients]]：

$$mathbf{A}mathbf{x} = mathbf{b}$$

扩展形式为：

$$begin{bmatrix} mathbf{Y}_n & mathbf{A}_c \ mathdr {A}_r & mathbf{A}_d end{bmatrix} begin{bmatrix} mathbf{V}_n \ mathdr {I}_x end{bmatrix} = begin{bmatrix} mathbf{I}_n \ mathdr {V}_x end{bmatrix}$$

其中 $mathbf{Y}_n$ 为经典节点导纳矩阵，$mathbf{A}_c, mathbf{A}_r, mathbf{A}_d$ 为增广部分[[a-julia-based-simulation-platform-for-power-system-transients]]。

JSEMT v4 在 IEEE 39 节点系统上单核计算时间 **2.42 s**，与商业软件 EMTP® 的 **2.10 s** 相当（性能比 1.15:1）；在 3704 节点放大网络上达 **26.54 s** vs EMTP® 的 23.04 s[[a-julia-based-simulation-platform-for-power-system-transients]]。

关键优化手段包括 KLU 稀疏矩阵求解器的符号分解缓存与数值重因式分解（**9.18 倍提速**从 v1 到 v4），以及基于输电线路解耦的子网络并行策略（**5 核加速 5.73 倍**）[[a-julia-based-simulation-platform-for-power-system-transients]]。

### 图形框图语言（Block Diagram Languages）

图形框图语言以信号流和控制逻辑为核心，适合描述控制器和系统级结构。典型代表包括 MATLAB/Simulink 的模块图和 PSCAD 的自定义控制模块。其 EMT 建模核心是**离散化控制方程与 PWM 采样链路**，将模拟控制器转化为离散时步执行逻辑。

图形框图语言的 EMT 局限在于：框图保留的是系统级信号连接，不一定保留底层电路拓扑——当控制器与电力电子开关紧密耦合时，框图层的等效离散化误差难以在 EMT 精度要求下被忽略。

### 网表与卡片格式（Netlist / Card Formats）

EMTP 卡片、ATP MODELS/TACS、PSCAD 自定义代码、SPICE 网表和 MATEMTP 属于工具相关网表表达[[a-julia-based-simulation-platform-for-power-system-transients]]。其优势是贴近目标仿真器的求解架构，缺点是跨工具迁移时语义容易变化。

**MANA 框架**（Modified Augmented Nodal Analysis）是网表类语言的核心数学基础[[a-julia-based-simulation-platform-for-power-system-transients]]：将所有元件（RLC 支路、开关、同步电机等）的微分方程用梯形积分法离散为诺顿等效电路，组装为稀疏线性系统 $mathbf{A}mathbf{x} = mathbf{b}$ 后统一求解。

SPICE 网表的本构关系可写为[[a-julia-based-simulation-platform-for-power-system-transients]]：

$$mathbf{Y}_n mathbf{V}_n = mathbf{I}_n$$

其中 $mathbf{Y}_n$ 为节点导纳矩阵，$mathbf{V}_n$ 为节点电压向量，$mathbf{I}_n$ 为注入电流向量。

若页面声称"模型可跨平台复用"，应说明复用的是拓扑、参数、控制逻辑、离散方程还是完整可运行工程文件。只有文件能被导入，不代表波形或数值稳定性等价。

### 数据交换标准（Data Exchange Standards）

Common Information Model（CIM）标准面向电网对象、资产、拓扑和运行数据交换[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。它适合传递线路、变压器、开关、母线、量测和网络层级关系，但不自动提供 EMT 所需的全部高频参数、控制器细节、开关插值设置或非线性元件动态。

CIM 类数据作为 EMT 模型构建输入时，通常还需要补充[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]：

- 频率相关线路/电缆参数（宽频建模数据）
- 变压器饱和、磁滞或宽频模型参数
- 电力电子控制器和保护逻辑（控制框图或参数集）
- 初始条件、事件时刻和仿真步长

**FMI（Functional Mock-up Interface）** 标准支持不同仿真工具之间的模型交换[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。FMI 采用标准化的残差函数接口和 Jacobian 矩阵接口，使 Modelica 模型可与传统 EMTP 类求解器联合仿真，实现声明式建模与高性能数值计算的分离[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。

### 工具脚本与 API（Tool Scripts / APIs）

工具内置脚本语言（如 PSCAD 自定义模块、MATLAB Function、ATP MODELS/TACS）适合参数扫描和自动化建模。其 EMT 建模核心是**自动化脚本生成批量算例或后处理流程**，而非元件本构关系的直接表达。

## 分类与变体对比表

| 类型 | 表达重点 | EMT 使用价值 | 主要风险 |
|------|----------|--------------|----------|
| 方程式建模语言 | 物理方程、连接器、组件复用 | 适合多物理域和模型库组织 | 事件、初值和离散化需与 EMT 求解器对齐 |
| 图形框图语言 | 控制逻辑、信号流、模块组合 | 适合控制器和系统级搭建 | 框图不一定保留底层电路语义 |
| 网表/卡片格式 | 节点、支路、元件参数 | 适合电路拓扑和批处理输入 | 复杂控制和非线性模型迁移困难 |
| 数据交换标准 | 资产、拓扑、运行数据 | 适合从电网数据生成基础模型 | EMT 高频参数和控制细节常缺失 |
| 工具脚本/API | 自动化建模、运行、后处理 | 适合参数扫描和回归测试 | API 可变，版本和许可需核查 |

## 关键技术挑战

### 方程与求解器的对齐挑战

声明式建模语言（如 Modelica）的核心矛盾在于：用户书写的物理方程是连续时间形式，而 EMT 求解器最终需要在离散时间步上求解代数方程组[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]。关键挑战包括[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]：

- **微分指标问题**：高阶 DAE（index > 1）不能直接送入 BDF 求解器，需通过 Pantelides 算法约简至 index-1
- **事件定位精度**：开关操作等不连续点的时间定位精度取决于求解器步长控制容差（通常 $10^{-6}$ 秒量级）[[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]]
- **代数环撕裂**：大型网络常形成数百至数千维的代数环，需智能选择撕裂变量以平衡稀疏性与收敛性

### 大规模系统的计算效率挑战

- **稀疏矩阵重复求解**：网络拓扑不变时，每次时步重复符号分析成本高昂，需采用符号分解缓存+数值重因式分解策略[[a-julia-based-simulation-platform-for-power-system-transients]]
- **内存访问局部性**：大量分散的线路对象导致缓存命中率低；可通过"线路块模型"批量组织同类变量[[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-]]
- **非线性元件迭代收敛**：分段线性化方法需牛顿-拉夫逊迭代确定工作点，边界附近可能出现数值振荡[[a-julia-based-simulation-platform-for-power-system-transients]]

### 跨工具迁移的语义等价性挑战

- **坐标系与相序差异**：Park 变换、dq 坐标与相域变量的参考坐标系必须一致
- **步长与积分方法匹配**：同一网表在 EMTP（梯形法）和 Modelica IDA（BDF 变阶）中可能产生不同数值阻尼特性
- **开关事件处理机制**：梯形法的"数值振荡"问题与 BDF 的事件根查找机制不可互换

## 量化性能边界

| 平台/方法 | 测试系统 | 性能指标 | 对比基线 |
|-----------|----------|----------|----------|
| MSEMT (Modelica) | IEEE 39 节点 | DAE 维度降至原规模 10-30% | 声明式建模 vs 过程式 EMTP |
| Modelica WB 线路块 | IEEE 39 节点 (34 条线路) | CPU 9682s→6117s（**1.58× 加速**） | 原始 Modelica 分散线路 |
| Modelica CP 线路块 | IEEE 39 节点 (34 条线路) | CPU 374.3s→215.7s（**1.74× 加速**） | 原始 Modelica 分散线路 |
| Dynaωo 混合架构 | 230 kV 电容器组投切 | 误差 < 0.1%，分辨 340 Hz–27.26 kHz | EMTP 固定步长 10 μs |
| JSEMT v4 (Julia) | IEEE 39 节点 (357 节点) | CPU 2.42s，性能比 1.15:1 | EMTP® 2.10s |
| JSEMT v4 (Julia) | 3704 节点 (10× 放大) | CPU 26.54s | EMTP® 23.04s |
| JSEMT 子网络并行 | 3704 节点 | **5 核 5.73× 加速** | 单核 865.07s |

## 适用边界与选择指南

**适用场景：**

- 需要在多个工具、模型库或数据系统之间传递拓扑和参数 → 选择数据交换标准（CIM/FMI）
- 需要批量生成 EMT 算例或做参数扫描 → 选择工具脚本/API
- 需要把控制器、设备模型和网络模型拆成可维护组件 → 选择方程式语言（Modelica）
- 已有明确网表格式的算例批量处理 → 选择网表/卡片格式

**失败模式：**

- 只转换拓扑和额定参数，却声称完整 EMT 模型已迁移
- 忽略单位、标幺基值、坐标系、相序和参考方向
- 把机电暂态或潮流模型直接当作 EMT 可用模型
- 自动生成文件语法正确，但缺少初始化、开关事件和控制采样设置
- 页面列出某语言或标准名称，却没有说明它在论文中承担的是数据交换、模型表达还是代码生成角色

## 相关页面

- [[netlist-import-export]]：关注拓扑和元件参数的文本化交换，是建模语言的一个具体分支
- [[automatic-code-generation]]：可从建模语言或模板生成目标工具代码，但需要验证生成模型的语义等价性
- [[co-simulation]]：建模语言可描述各子系统，协同仿真还需要时间同步和接口调度
- [[simulation-tools-status]]：工具页应说明工具能力证据，不能把某语言支持直接等同于工具适用性
- [[model-compatibility-layer]]：关注跨格式模型迁移中的接口兼容性问题

## 来源论文

- [[msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st]] — Masoom 等 2022：Modelica 声明式 EMT 框架 MSEMT，方程与求解器解耦，BLT/Pantelides 算法，精度与 EMTP 对齐
- [[acceleration-of-electromagnetic-transient-simulations-in-modelica-using-spatial-]] — Masoom 等 2022：Modelica 空间局部性优化，线路块模型，WB 线路 1.58× / CP 线路 1.74× 加速
- [[modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat]] — Masoom 等 2021：Dynaωo 混合 C++/Modelica 架构，虚拟方程预编译，IDA 求解器，340 Hz–27.26 kHz 多频段分辨
- [[a-julia-based-simulation-platform-for-power-system-transients]] — Naidjate 等 2025：Julia 平台 JSEMT，MANA 网络方程，KLU + 重因式分解，9.18× 加速比，子网络并行 5.73×（5 核）