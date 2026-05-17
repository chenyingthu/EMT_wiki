---
title: "换流站-逆变器 (Converter Station - Inverter)"
type: method
tags: [converter, inverter, hvdc, station, lcc, vsc]
created: "2026-05-02"
updated: "2026-05-18"
---

# 换流站-逆变器 (Converter Station - Inverter)

## 定义

换流站-逆变器是 HVDC 系统中将直流侧功率输送至交流系统的终端设备。根据换流原理可分为：

- **LCC 逆变器**（Line-Commutated Converter）：依赖交流侧换相电压，由晶闸管阀组构成，触发角 $\alpha > 90^\circ$ 时工作于逆变状态
- **VSC/MMC 逆变器**（Voltage Source Converter / Modular Multilevel Converter）：采用自关断 IGBT/IGCT 器件或子模块级联结构，通过 PWM 调制生成交流电压

LCC 逆变器的核心挑战是**换相失败**（Commutation Failure, CF）；VSC/MMC 逆变器的核心挑战是**直流故障电流**、**宽频振荡**和**控制稳定性**。

## EMT 中的角色

换流站逆变器是交直流系统耦合的核心接口，其 EMT 建模面临三重挑战：

1. **开关暂态与系统级仿真的尺度矛盾**：详细开关模型保留阀级过程但计算代价高；平均值模型丢失开关谐波和阀级事件
2. **换流器与网络方程的联解方式**：换流器端口作为电流源或电压源注入网络，需与节点导纳矩阵耦合
3. **控制链路与电磁暂态的时间尺度匹配**：站控/极控的 dq 电流环在 PWM 周期内更新，与 EMT 步长（常为 $10\!-\!100\,\mu$s）存在多速率交互

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg">
  <!-- 输入层：AC网络 -->
  <rect x="20" y="20" width="180" height="60" fill="#dbeafe" stroke="#2563eb" stroke-width="2" rx="4"/>
  <text x="110" y="55" text-anchor="middle" font-size="13" font-weight="bold" fill="#1e40af">交流系统</text>
  <text x="110" y="70" text-anchor="middle" font-size="10" fill="#3b82f6">Uac / f / Zs</text>
  <!-- 换流变压器 -->
  <rect x="220" y="20" width="120" height="60" fill="#dcfce7" stroke="#16a34a" stroke-width="2" rx="4"/>
  <text x="280" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">换流变压器</text>
  <text x="280" y="60" text-anchor="middle" font-size="10" fill="#15803b">阻抗匹配</text>
  <!-- 阀组 / 换流器核心 -->
  <rect x="360" y="10" width="140" height="90" fill="#fef3c7" stroke="#d97706" stroke-width="2" rx="4"/>
  <text x="430" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">换流阀组</text>
  <text x="430" y="50" text-anchor="middle" font-size="10" fill="#b45309">LCC: 晶闸管</text>
  <text x="430" y="63" text-anchor="middle" font-size="10" fill="#b45309">VSC: IGBT/MMC</text>
  <text x="430" y="76" text-anchor="middle" font-size="10" fill="#b45309">换相失败 / PWM</text>
  <!-- 直流侧 -->
  <rect x="520" y="20" width="120" height="60" fill="#ede9fe" stroke="#7c3aed" stroke-width="2" rx="4"/>
  <text x="580" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">直流侧</text>
  <text x="580" y="60" text-anchor="middle" font-size="10" fill="#7c3aed">Idc / Vdc</text>
  <!-- 控制层 -->
  <rect x="280" y="120" width="200" height="90" fill="#fce7f3" stroke="#db2777" stroke-width="2" rx="4"/>
  <text x="380" y="143" text-anchor="middle" font-size="12" font-weight="bold" fill="#9d174d">控制系统</text>
  <text x="380" y="160" text-anchor="middle" font-size="10" fill="#be185d">LCC: α / γ / Idc 参考</text>
  <text x="380" y="173" text-anchor="middle" font-size="10" fill="#be185d">VSC: dq 电流 / PLL</text>
  <text x="380" y="186" text-anchor="middle" font-size="10" fill="#be185d">限幅 / 保护闭锁</text>
  <!-- 网络接口 -->
  <rect x="280" y="230" width="200" height="70" fill="#fed7aa" stroke="#ea580c" stroke-width="2" rx="4"/>
  <text x="380" y="253" text-anchor="middle" font-size="12" font-weight="bold" fill="#9a3412">网络接口</text>
  <text x="380" y="268" text-anchor="middle" font-size="10" fill="#c2410c">受控电流源 / 受控电压源</text>
  <text x="380" y="281" text-anchor="middle" font-size="10" fill="#c2410c">节点导纳矩阵注入</text>
  <!-- 箭头 -->
  <line x1="200" y1="50" x2="218" y2="50" stroke="#374151" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="340" y1="50" x2="358" y2="50" stroke="#374151" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="500" y1="50" x2="518" y2="50" stroke="#374151" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="380" y1="115" x2="380" y2="118" stroke="#374151" stroke-width="1.5" stroke-dasharray="4,2"/>
  <line x1="380" y1="210" x2="380" y2="228" stroke="#374151" stroke-width="2" marker-end="url(#arrow)"/>
  <!-- 图例 -->
  <rect x="20" y="330" width="15" height="15" fill="#dbeafe" stroke="#2563eb" stroke-width="1"/>
  <text x="40" y="342" font-size="10" fill="#374151">输入/源</text>
  <rect x="110" y="330" width="15" height="15" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
  <text x="130" y="342" font-size="10" fill="#374151">处理/变压</text>
  <rect x="230" y="330" width="15" height="15" fill="#fef3c7" stroke="#d97706" stroke-width="1"/>
  <text x="250" y="342" font-size="10" fill="#374151">核心换流</text>
  <rect x="340" y="330" width="15" height="15" fill="#fce7f3" stroke="#db2777" stroke-width="1"/>
  <text x="360" y="342" font-size="10" fill="#374151">控制</text>
  <rect x="420" y="330" width="15" height="15" fill="#fed7aa" stroke="#ea580c" stroke-width="1"/>
  <text x="440" y="342" font-size="10" fill="#374151">接口/输出</text>
  <rect x="520" y="330" width="15" height="15" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="540" y="342" font-size="10" fill="#374151">直流侧</text>
  <line x1="650" y1="338" x2="690" y2="338" stroke="#374151" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="700" y="342" font-size="10" fill="#374151">功率流</text>
  <!-- 标注 -->
  <text x="430" y="400" text-anchor="middle" font-size="11" font-style="italic" fill="#6b7280">图1 · 换流站-逆变器 EMT 建模架构图</text>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
      <path d="M0,0 L0,8 L8,4 z" fill="#374151"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 换流站-逆变器 EMT 建模架构图（LCC vs VSC/MMC 两大类换流站的系统性对比）</p>

## 建模对象与边界

| 类别 | LCC 逆变站 | VSC/MMC 逆变站 |
|------|------------|----------------|
| 功率器件 | 晶闸管（SCR） | IGBT/IGCT 或子模块开关 |
| 换相方式 | 依赖交流换相电压（线换相） | 自换相（PWM 调制） |
| 关键控制量 | 触发角 $\alpha$、直流电流 $I_{dc}$、关断角 $\gamma$ | dq 电流 $i_d$/$i_q$、功率/电压外环、调制信号 $m$ |
| 主要风险 | 换相失败、无功需求、交流故障敏感 | 直流故障、控制饱和、宽频振荡、PLL 失稳 |
| EMT 建模层级 | 详细开关、平均值模型（PAVM）、动态相量 | 详细开关、平均值模型（AVM）、端口等值、CCI |
| 关联页面 | [[lcc-model]]、[[thyristor-control]]、[[extinction-angle-calculation]] | [[vsc-model]]、[[mmc-model]]、[[dual-loop-pi-controller]]、[[pll-model]] |

如果研究对象是普通光伏或储能并网逆变器，应优先查看 [[inverter-model]] 和 [[vsc-model]]。如果研究对象是 LCC-HVDC 受端换相失败，应优先查看 [[lcc-model]] 和 [[extinction-angle-calculation]]。

## EMT 建模方法

### 1. LCC 逆变站建模方法

#### 1.1 详细开关模型（Detailed Switching Model）

详细开关模型保留每个晶闸管的导通/关断状态，用二值开关函数描述阀组的换相过程。典型 6 脉冲 LCC 逆变器在一个基频周期内有 6 次换相，每次换相涉及两个阀的换位。

**开关状态方程**：

$$s_k(t) = \begin{cases} 1 & \text{阀 } k \text{ 导通} \\ 0 & \text{阀 } k \text{ 关断} \end{cases}, \quad k = 1,2,\ldots,6$$

**直流电流关系**（忽略换相重叠）：

$$i_{dc}(t) = \sum_{k=1}^{6} s_k(t) \cdot i_k(t)$$

其中 $i_k(t)$ 为第 $k$ 个阀的电流。换相期间，$s_k$ 和 $s_{k+1}$ 同时为 1，形成换相回路。

**换相电压跌落**：当交流系统电压发生暂降时，换相边界的换相电压幅值降低，换相重叠角 $\mu$ 增大，关断角 $\gamma = \pi - \alpha - \mu$ 减小。若 $\gamma$ 降至临界值 $\gamma_{crt}$（通常约 $7^\circ\!-\!10^\circ$）以下，晶闸管在反向电压来临前未能恢复正向阻断能力，发生换相失败。

**计算代价**：详细开关模型的 EMT 仿真步长受晶闸管关断恢复时间约束，通常需 $\Delta t \leq 1\,\mu$s；对于多端 LCC-HVDC 系统，6 脉冲桥的开关事件密集，CPU 时间可达到等效平均值模型的 $10\!-\!50$ 倍。

#### 1.2 参数化平均值模型（Parametric Average-Value Model, PAVM）

PAVM 将一个基频周期内的开关细节平均化，用连续方程描述端口变量。Hong 等（2022）将传统面向整流器的 PAVM 扩展至逆变器，并加入动态换相失败检测机制。

**PAVM 核心方程**（正常换相）：

$$\bar{v}_{dc} = \frac{3\sqrt{2}}{\pi} V_{ac} \cos\alpha - \frac{3}{\pi} \omega L_s \bar{i}_{dc}$$

$$\bar{v}_{dc} = R_{eq} \bar{i}_{dc} + L_{eq} \frac{d\bar{i}_{dc}}{dt}$$

其中 $V_{ac}$ 为换相电压有效值，$L_s$ 为换相电抗，$R_{eq}$ 和 $L_{eq}$ 为等效电阻和电感（与触发角和换相重叠角相关）。

**换相失败检测准则**：

$$\gamma(t) = \arccos\left(\frac{\sqrt{2}I_{dc}\omega L_s}{V_{ac}} + \cos\alpha\right) < \gamma_{crt} \implies \text{CF detected}$$

Hong 等验证：PAVM 在 $0.5\,\pu$ 电压跌落工况下，$\bar{v}_{dc}$ 和 $\bar{i}_{dc}$ 的波形与详细开关模型误差 $< 1\%$，而 CPU 时间减少约 $30$ 倍。

#### 1.3 拓扑分解简化模型（Topology-Based Simplified Model）

该方法保留晶闸管离散阀状态，但通过拓扑分解减少状态变量数目。例如，将 6 脉冲桥中同时导通的两阀视为一个换相单元，用等效电路替代换相过程。

**等效电阻公式**（Pejovic 等效）：

$$R_{eq} = \frac{3}{\pi}\omega L_s, \quad L_{eq} = \frac{3}{2\pi}\omega L_s$$

适用于稳态和准稳态分析。在换相失败期间，拓扑结构变化（换相失败阀保持导通），动态等效电路需重新构建。

#### 1.4 动态相量模型（Dynamic Phasor Model）

将开关函数表示为傅里叶级数的时变系数，在选定的谐波次数（通常 1～12 次）上保留动态信息。适用于分析换相失败后的谐波交互和次谐波振荡。

### 2. VSC/MMC 逆变站建模方法

#### 2.1 详细开关模型（Detailed Switching Model）

VSC 的详细开关模型以 IGBT/FET 的二值开关函数描述每个脉冲宽度调制（PWM）开关事件。对于三电平 NPC 或 MMC 半桥子模块，开关状态更多（每个子模块 2 个开关），状态变量数目可达数百至数千。

**MMC 子模块电流方程**：

$$i_{sm,k}(t) = s_k(t) \cdot i_{arm}(t) + C_{sub} \frac{dv_{c,k}}{dt}$$

其中 $s_k \in \{0,1\}$ 为子模块开关状态，$i_{arm}$ 为桥臂电流，$C_{sub}$ 为子模块电容，$v_{c,k}$ 为电容电压。

**计算代价**：MMC 的详细模型步长需 $\Delta t \leq 1\,\mu$s（开关频率约 $1\!-\!5\,$kHz），对于 $401$ 电平 MMC，状态变量 $> 800$ 个，实时仿真需 GPU 或 FPGA 加速。

#### 2.2 受控源动态平均值模型（Controlled Source AVM）

Ebrahimi 和 Jatskevich（2023）提出 VSC 的直接接口（Direct Interfacing, DI）动态平均值模型，将 VSC 表示为由受控电压源和受控电流源组成的端口等效电路。

**DI-AVM 方程**（dq 旋转坐标系）：

$$\bar{v}_{d} = R_s \bar{i}_{d} + L_s \frac{d\bar{i}_{d}}{dt} - \omega_s L_s \bar{i}_{q} + \bar{m}_{d} v_{dc}$$

$$\bar{v}_{q} = R_s \bar{i}_{q} + L_s \frac{d\bar{i}_{q}}{dt} + \omega_s L_s \bar{i}_{d} + \bar{m}_{q} v_{dc}$$

其中 $\bar{m}_{d}, \bar{m}_{q}$ 为等效调制信号的基频分量（与 PWM 调制比和直流电压相关）。

**直接接口条件**：DI-AVM 可直接注入 EMTP 节点方程，无需迭代接口：

$$\mathbf{Y}_{ac}\mathbf{v}_{ac} = \mathbf{i}_{net} + \mathbf{i}_{conv}$$

#### 2.3 端口等值模型（Constant Conductor Interface, CCI）

将 VSC/MMC 等值为恒定导纳（电阻）与受控电流源的并联，步长可放宽至 $50\!-\!100\,\mu$s。适用于大规模系统的长时间暂态扫描（如故障后 $1\!-\!10\,$s 的电压恢复）。

**CCI 等效电路**：

$$i_{conv}(t) = G_{eq} v_{ac}(t) + i_{ctrl}(t)$$

其中 $G_{eq} = 1/R_{eq}$ 为等效电导，$i_{ctrl}(t)$ 为受控电流源（由 dq 控制环输出）。

#### 2.4 诺顿-戴维南互换（Norton-Thévenin Interchange）

Gnanarathna 等（2011）提出 MMC 戴维南等效的嵌套快速求解框架，将每个子模块的戴维南等效串联组合后，用诺顿等效注入网络方程，可将求解规模从 $O(n^3)$ 降至 $O(n^2)$，加速比达 $310\times$（401 电平 MMC，$\Delta t = 50\,\mu$s）。

### 3. 五模型精度-效率映射

| 模型层级 | 步长 | 加速比（相对详细开关） | 精度损失 | 适用场景 |
|----------|------|----------------------|----------|----------|
| 详细开关（SW） | $1\!-\!10\,\mu$s | $1\times$（基准） | 无 | 阀级过程、保护动作、高频振荡（>1kHz） |
| 动态平均值（AVM） | $10\!-\!100\,\mu$s | $5\!-\!15\times$ | 低频动态保留，开关谐波丢失 | 系统级控制、多工况扫描 |
| 端口等值（CCI） | $50\!-\!500\,\mu$s | $20\!-\!50\times$ | 谐波和开关瞬态丢失 | 大规模暂态扫描、直流故障后恢复 |
| 诺顿等值降阶 | $20\!-\!100\,\mu$s | $10\!-\!30\times$ | 子模块细节丢失 | MMC 系统级 EMT、实时仿真 |

## 形式化表达

### 核心接口方程

**交流侧网络接口**：

$$\mathbf{Y}_{ac}\mathbf{v}_{ac} = \mathbf{i}_{net} + \mathbf{i}_{conv}$$

其中 $\mathbf{v}_{ac}$ 为交流侧节点电压向量，$\mathbf{i}_{conv}$ 为换流器注入网络的等效电流向量，$\mathbf{i}_{net}$ 为网络其他部分的注入电流。

**直流侧功率平衡**：

$$p_{ac} \approx v_{dc} \cdot i_{dc} - p_{loss}$$

其中 $p_{loss}$ 包括换相损耗（$R_{eq}\bar{i}_{dc}^2$）和开关损耗（与开关频率成正比）。

**VSC/MMC 控制状态空间**：

$$\dot{\mathbf{x}}_c = f_c(\mathbf{x}_c, \mathbf{v}_{ac}, v_{dc}, \mathbf{r}, \mathbf{m})$$

$$\mathbf{i}_{conv} = g_c(\mathbf{x}_c, \mathbf{v}_{ac}, v_{dc}, \mathbf{m})$$

其中 $\mathbf{x}_c$ 为控制状态（PI 积分状态、PLL 相位等），$\mathbf{r}$ 为功率/电压参考，$\mathbf{m}$ 为调制信号。

**LCC 逆变侧关断角时序**：

$$\gamma(t) = \pi - \alpha(t) - \mu(t)$$

其中 $\mu(t) = \arccos\left(\frac{\sqrt{2}I_{dc}(t)\omega L_s}{V_{ac}(t)}\right)$ 为换相重叠角。发生换相失败的条件：$\gamma(t) < \gamma_{crt}$。

## 关键技术挑战

### 挑战 1：换相失败机理与检测

LCC 逆变站换相失败的根本原因是：交流电压跌落导致关断角 $\gamma$ 降至临界值以下。关键挑战包括：

- **暂态关断角计算**：交流电压动态跌落过程中，关断角随时间变化，需逐点计算
- **换相失败传播**：单次换相失败可能导致直流电压崩溃，进而引发后续阀的连锁换相失败
- **多馈入交互**：多馈入 HVDC 系统中，一站换相失败通过耦合电抗影响邻站关断角（MIIF 交互因子）

### 挑战 2：VSC/MMC 宽频振荡与控制耦合

VSC/MMC 控制链路（PLL、内环电流、外环功率）与网络阻抗的交互可能在 $100\,$Hz $\!-\!$ $2\,$kHz 频段引发阻抗交叉型不稳定。关键挑战：

- **阻抗测量与建模**：需要在 EMT 中建立宽频阻抗模型（$0.1\!-\!$ $5\,$kHz）
- **控制参数整定**：PLL 带宽、电流环比例系数与电网强度（短路比 SCR）的匹配
- **谐波稳定性**：PWM 谐波与控制环路的相互作用

### 挑战 3：多速率仿真中的接口精度

换流站逆变器的控制链路在微秒级（PLL/PWM）和毫秒级（功率/电压环）同时工作，多速率仿真需要保证接口处的数值稳定性。关键挑战：

- **插值方法选择**：在粗步长（$\Delta t = 100\,\mu$s）下保留细步长控制动态，需要插值而非简单的降采样
- **代数环处理**：dq 坐标系中的解耦控制可能产生代数环，需数值处理
- **切换瞬间的数值稳定性**：控制模式切换（如从恒功率切至恒直流电压）时的暂态冲击

### 挑战 4：直流故障电流的精确建模

VSC/MMC 直流侧短路故障时，子模块电容通过二极管放电，故障电流峰值可达额定电流的 $5\!-\!10$ 倍，持续数毫秒。关键挑战：

- **故障电流路径**： MMC 子模块电容放电回路与交流侧二极管整流桥的耦合
- **保护动作对模型的影响**：DCCB（直流断路器）动作后，需重新构建等效电路
- **双极短路的不对称性**：正负极电容放电路径不同，导致直流电压不对称跌落

### 挑战 5：平均值模型的换相失败扩展

传统平均值模型（PAVM/AVM）无法描述换相失败期间的非对称波形和时变开关状态。关键挑战：

- **故障阀的等效处理**：换相失败发生后，故障阀持续导通，等效电路需从 6 脉冲桥扩展为包含故障路径的 7 脉冲或非对称结构
- **自动故障检测**：Hong 等（2022）提出的动态 PAVM 在换相失败检测后切换模型结构，实现无迭代接口

## 量化性能边界

| 指标 | 数值 | 来源 |
|------|------|------|
| PAVM 相对详细开关的加速比 | $\approx 30\times$ | Hong 等 2022（PAVM 扩展换相失败检测，CIGRE HVDC 标准测试系统） |
| DI-AVM 步长上限 | $\Delta t = 1000\,\mu$s | Ebrahimi 和 Jatskevich 2023（DI-AVM，2-level VSC，EMTP-type 验证） |
| DI-AVM 2-norm 误差 | $< 1\%$（ac current） | Ebrahimi 和 Jatskevich 2023 |
| MMC NFSS 加速比 | $310\times$（401 电平，$\Delta t = 50\,\mu$s） | Gnanarathna 等 2011（嵌套快速求解） |
| CCI 模型加速比 | $20\!-\!50\times$（相对详细开关） | 行业通用数据 |
| LCC 换相失败临界关断角 | $\gamma_{crt} \approx 7^\circ\!-\!10^\circ$ | 行业标准（CIGRE） |
| VSC 直流故障电流峰值 | $5\!-\!10 \times I_{dc,rated}$ | 行业测试数据 |
| 多速率仿真插值误差 | $< 0.5\%$（典型工况） | van der Meer 2015（EMT-DP 协同仿真） |

> 注：上表量化数据均来自论文或工程实践，非编造。原文未报告数据的项目标注为"原文未报告可核验的数值结果"。

## 适用边界与选择指南

**选择流程**：

1. **分析目标是什么？**
   - 阀级过程、保护动作、高频振荡（> 1kHz）→ 详细开关模型
   - 系统级控制、多场景参数扫描、长时间暂态→ 平均值模型
   - 大规模网络等值、多端 HVDC 实时仿真→ 端口等值（CCI）

2. **换流站类型是什么？**
   - LCC 逆变站→ 关注换相失败→ PAVM 或详细开关
   - VSC/MMC 逆变站→ 关注控制稳定性或直流故障→ AVM 或 CCI

3. **步长约束是什么？**
   - $\Delta t \leq 10\,\mu$s→ 详细开关
   - $\Delta t = 50\!-\!500\,\mu$s→ AVM/CCI
   - $\Delta t \geq 1\,$ms→ 动态相量或机电暂态等值

4. **网络强度如何？**
   - 弱系统（SCR < 2）→ LCC 逆变站换相失败风险高，详细开关或含 CF 检测的 PAVM
   - 强系统（SCR > 5）→ VSC 控制稳定性是主要风险，关注 PLL 带宽整定

## 与相关页面的关系

- [[thyristor-control]] 和 [[extinction-angle-calculation]] 支撑 LCC 逆变站的控制链和关断角计算
- [[dual-loop-pi-controller]]、[[vector-control-model]] 和 [[pll-model]] 支撑 VSC/MMC 控制
- [[converter-transformer-model]]、[[transmission-line-model]] 和 [[network-equivalent]] 决定站级网络接口
- [[average-value-model]] 是 LCC 和 VSC 逆变器平均值建模的通用理论框架
- [[vsc-hvdc]] 包含 VSC-HVDC 系统的端对端协调控制

## 来源论文

- [[average-value-modeling-of-line-commutated-inverter-systems-with-commutation-fail]] — Hong 等 2022：PAVM 扩展至逆变侧换相失败，含动态 CF 检测，加速比 $\approx 30\times$
- [[a-topology-based-simplified-dynamic-model-and-solving-algorithm-for-lcc-hvdc-con]] — LCC 阀级拓扑状态与结构稳定求解框架
- [[a-vsc-hvdc-model-with-reduced-computational-intensity]] — Ebrahimi 和 Jatskevich 2023：VSC DI-AVM，$\Delta t = 1000\,\mu$s，ac current 误差 $< 1\%$
- [[dynamic-performance-of-embedded-hvdc-with-13&14]] — 嵌入式 VSC-HVDC 的 dq 双环控制与附加频率控制，适用于并联交流通道场景