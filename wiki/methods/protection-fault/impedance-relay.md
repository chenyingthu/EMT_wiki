---
title: "阻抗继电器 (Impedance Relay)"
type: method
tags: [impedance-relay, distance-protection, relay, fault-detection, zone-protection, r-x-plane, mho-relay, quadrilateral-relay]
created: "2026-05-02"
updated: "2026-05-16"
---

# 阻抗继电器 (Impedance Relay)

## 定义

阻抗继电器是距离保护系统中的核心测量与判别元件，通过提取保护安装处的电压、电流相量构造视在阻抗 $Z_m = R_m + jX_m$，并判断该阻抗是否落入预设的动作特性域（Characteristic Plane），从而确定故障是否位于保护区内。

在电磁暂态程序（EMT）仿真中，阻抗继电器模型需要与[[protection-relay-modeling]]的测量链路（互感器模型→采样→滤波→相量提取→阻抗估计→动作判据）联接，形成完整的"系统暂态→互感器变换→继电器算法处理→保护决策反馈→系统状态更新"闭环仿真结构（[[protection-system-representation-in-the-electromagnetic-transients-program-power]]）。

基本阻抗测量方程：

$$
Z_m = \frac{\dot{V}_m}{\dot{I}_m} = \frac{V_R + jV_I}{I_R + jI_I}
$$

展开为实部与虚部：

$$
R_m = \frac{V_R I_R + V_I I_I}{I_R^2 + I_I^2}, \quad X_m = \frac{V_I I_R - V_R I_I}{I_R^2 + I_I^2}
$$

## EMT中的角色

阻抗继电器在 EMT 仿真中有三重角色：

**1. 保护算法的物理验证载体**：继电器看到的不是稳态正弦量，而是含直流偏移、行波反射和互感器暂态误差的故障暂态波形。EMT 仿真能把这些非理想条件施加给保护算法，验证其在暂态早期（通常为故障后几个毫秒）的动作可靠性。

**2. 保护-电网闭环交互的研究工具**：当继电器输出跳闸信号后，EMT 据此改变电力系统拓扑（断开断路器），使后续时步的电气量反映保护动作后的网络状态，从而研究故障、跳闸与后续过电压的级联交互效应。

**3. 测量链路各环节的量化评估平台**：通过 EMT 中的 CT/CVT 模型，可以定量评估互感器暂态响应、采样率限制和滤波算法对阻抗测量精度的影响。

关键挑战体现在四个方面：

- **过渡电阻影响**：高阻接地故障时，测量阻抗轨迹向电阻方向偏移，可能导致保护拒动或超越动作
- **负荷阻抗干扰**：重负荷长线路的负荷阻抗可能与动作区边界重叠，需要负荷限制特性
- **系统振荡判别**：振荡期间视在阻抗缓慢穿越动作区，必须与短路故障突变量区分
- **互感器暂态误差**：CT 饱和和 CVT 暂态传变误差直接影响继电器输入量的精度

## 核心机制

### 阻抗测量原理

阻抗继电器通过故障回路的电压、电流相量计算视在阻抗。根据故障类型选择不同的测量方程：

**相间故障**（BC 相间故障为例）：

$$
Z_{\phi\phi'} = \frac{V_\phi - V_{\phi'}}{I_\phi - I_{\phi'}}
$$

**单相接地故障**（A 相接地为例，需零序补偿）：

$$
Z_\phi = \frac{V_\phi}{I_\phi + k_0 I_0}, \quad k_0 = \frac{Z_{0L} - Z_{1L}}{3 Z_{1L}}
$$

其中 $k_0$ 为零序补偿系数，$Z_{0L}$ 和 $Z_{1L}$ 分别为线路零序和正序阻抗。

**阻抗轨迹的影响因素**：

- **过渡电阻 $R_F$**：使测量阻抗的电阻分量增大，轨迹向 $+R$ 方向偏移
- **助增电流**：相邻线路故障电流流入，使本端测量阻抗偏小（欠范围）
- **外汲电流**：相邻线路从本端网络汲取电流，使本端测量阻抗偏大（超范围）
- **平行线路互感**：零序互感压降叠加于故障相电压，改变零序阻抗测量值
- **CT 饱和**：使电流测量值偏小，导致阻抗轨迹向原点偏移
- **CVT 暂态**：电压测量含低频衰减分量，导致阻抗在暂态期间振荡

### 动作特性

阻抗继电器的动作域（Characteristic）在 R-X 平面上呈现不同几何形状，代表不同的保护整定思想：

| 特性类型 | 几何形状 | 方向性 | 适用场景 | 主要局限 |
|---------|---------|--------|---------|---------|
| 全阻抗圆 | 圆（圆心在原点） | 无，需单独方向元件 | 短线路、保护Ⅰ段 | 受负荷阻抗影响大 |
| Mho（方向圆） | 圆（过原点） | 自带方向 | 距离保护主保护 | 难处理大过渡电阻 |
| 偏移Mho | 圆（原点偏移至第Ⅰ、Ⅲ象限） | 可覆盖正反向 | 启动元件、后备保护 | 动作区较大可能超范围 |
| 四边形/多边形 | 四边形 | 可设方向线 | 过渡电阻较大场景 | 整定参数多，配合复杂 |
| 阻抗梯度 | 直线（电抗线+电阻线） | 需方向判别 | 串补线路 | 依赖精确参数 |

动作域的统一判据形式为：

$$
f(R_m, X_m, \theta_{\text{pol}}, s_{\text{block}}) > 0
$$

其中 $\theta_{\text{pol}}$ 为极化量（提供方向参考），$s_{\text{block}}$ 为闭锁状态（系统振荡闭锁、电压开放闭锁等）。

**阻抗平面的分区**：R-X 平面被特性边界划分为：
- **动作区**（Inside）：阻抗落入此区域则继电器动作
- **闭锁区**（Outside）：阻抗在保护区外，继电器不动作
- **延时区**（Restraint/Time-delayed）：需要配合延时才动作

### 动作特性参数整定

保护范围通常以线路正序阻抗的百分比表示：

$$
Z_{\text{set}} = k \cdot Z_{1L} \quad (0.8 \leq k \leq 1.2)
$$

对于 Mho 特性，阻抗圆半径整定为 $Z_{\text{set}}$；对于四边形特性，电抗边界整定为 $X_{\text{set}} = 0.85 Z_{1L}$，电阻边界整定为 $R_{\text{set}} = 0.2 Z_{1L} \sim 0.3 Z_{1L}$。

### 阻抗继电器的数字实现链路

数字阻抗继电器在 EMT 中的实现链路为：

```
故障电压/电流采样
    ↓
抗混叠滤波（通常为低通，截止频率 ≤ fs/2）
    ↓
相量提取（DFT/滑动DFT/傅里叶滤波/矩阵束算法）
    ↓
零序补偿（接地故障）
    ↓
阻抗计算 Z_m = V_m / I_m
    ↓
动作域判别（R-X平面坐标比较）
    ↓
延时与配合逻辑
    ↓
跳闸/闭锁决策
```

## EMT建模方法

在 EMT 仿真中进行阻抗继电器建模，需要考虑以下五个环节的数学建模：

### 方法1：理想变压器接口（恒定采样）

最简单的接口方式，将继电器视为保护安装处的电压、电流直接读取点：

$$
\dot{V}_m(k) = v_{\text{bus}}(k \Delta t), \quad \dot{I}_m(k) = i_{\text{line}}(k \Delta t)
$$

**特点**：无建模误差，但忽略互感器暂态，适用于暂态研究初期验证。

**适用场景**：继电器算法本身的研究、动作特性验证、采样率影响分析。

### 方法2：CT/CVT 暂态模型接口

引入实际互感器的传变特性模型：

**电流互感器（CT）暂态模型**：

$$
i_s(t) = \frac{N_2}{N_1} i_p(t) + L_m \frac{d}{dt}\left(\frac{i_p(t)}{N_{1}}\right) + R_c i_p(t)
$$

或使用等效二阶模型模拟铁芯饱和效应：

$$
v_s(t) = R_s i_s(t) + L_s \frac{di_s(t)}{dt}, \quad L_s = f(i_s, \text{B-H})
$$

**电容式电压互感器（CVT）暂态模型**：

CVT 由电容分压、补偿电抗和电磁单元组成，其暂态响应包含：

- **工频稳态响应**：精度较高（0.5%~1%）
- **暂态响应误差**：故障初期电压突变时，CVT 输出存在低频衰减分量（约几赫兹），持续时间可达数十毫秒

简化 CVT 传递函数模型：

$$
H(s) = \frac{\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}
$$

其中 $\omega_0$ 为工频谐振角频率，$\zeta$ 为阻尼系数。

### 方法3：相量提取算法建模

阻抗继电器的核心是相量估计算法，不同算法在精度、速度和抗干扰性之间有不同权衡：

**全波傅里叶滤波（FWF）**：

$$
\dot{I} = \frac{2}{N}\sum_{k=0}^{N-1} i(k) e^{-j2\pi k/N}
$$

**滑动傅里叶滤波（SWF）**：

每新来一点采样，窗内数据右移一位：

$$
\dot{I}(m) = \frac{2}{N}\sum_{k=0}^{N-1} i(m-N+k) e^{-j2\pi k/N}
$$

**短窗傅里叶滤波**：

窗长取半个周波（60 Hz 系统为 8.33 ms @ 1 kHz），用短窗傅里叶滤波得到对称分量后，组装复数瞬时等效故障回路，求解复数微分方程得到正序阻抗（[[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]]）。

**矩阵束算法（Matrix Pencil）**：

对含直流偏移的故障暂态采样序列 $i(k)$ 做矩阵束分析：

$$
i(k) = \sum_{i=1}^{M} A_i e^{\sigma_i k \Delta t} \cos(\omega_i k \Delta t + \phi_i)
$$

从中提取基频分量和直流衰减分量，再计算相量（[[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide]]）。

### 方法4：参数辨识阻抗估计

将阻抗估计转化为故障网络参数辨识问题：

对于 R-L 线路模型的单相接地故障，设故障距离为 $p$（单位 p.u.）、过渡电阻为 $R_F$、对侧零序等效电感为 $L_{n0}$，故障回路方程为：

$$
sU_m(s) = p Z_{1L} I_m(s) + R_F I_{m0}(s) + s L_{n0} I_{m0}(s)
$$

在频域化为线性方程，求解得到三个系数后映射回物理参数（[[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide]]）。

### 方法5：故障阻抗轨迹预测与补偿

针对过渡电阻对阻抗轨迹的影响，有以下建模思路：

**故障电阻补偿**：

将测量阻抗投影到线路阻抗线方向，消除过渡电阻的纯电阻分量影响：

$$
Z_{\text{projected}} = \frac{\text{Re}(Z_m \cdot Z_{1L}^*)}{|Z_{1L}|^2} Z_{1L}
$$

**并行线路零序互感补偿**：

对于平行线路，将零序互感压降显式纳入故障回路方程（[[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel]]）：

$$
V = p(I \cdot Z_{1L} + I_{0P} \cdot Z_{0M}) + I_F \cdot R_F
$$

其中 $I_{0P}$ 为平行线路零序电流，需表示为故障距离 $p$ 的线性函数。

## 量化性能边界

阻抗继电器的性能边界与故障类型、过渡电阻、系统阻抗和整定参数密切相关。以下数据来自仿真验证（原文未全部报告可逐项核验的数值结果，此处标注来源）：

| 工况 | 故障类型 | 过渡电阻 | 误差范围 | 来源 |
|------|---------|---------|---------|------|
| 远端高阻接地 | 单相接地（A-G） | 50~100 Ω | 计算距离系统性偏小（可能导致超越） | [[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide]] |
| 并行线路远端高阻故障 | 单相接地（A-G） | 50~100 Ω | 需并行线路零序互感补偿才能准确 | [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] |
| 双回线路 | 单相接地（A-G） | 0~30 Ω | 未补偿互感时误差可达 5%~15% | [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel]] |
| 近端三相故障 | 三相（ABC） | 0 Ω | 方向判别需记忆电压或交叉极化 | [[protection-system-representation-in-the-electromagnetic-transients-program-power]] |

**采样率对阻抗测量的影响**：

- 采样率 $\geq 960$ Hz（60 Hz 系统每周波 16 点）：基频相量误差 $< 5%$
- 采样率 $= 1920$ Hz：低次谐波（2/3/5 次）提取误差 $< 3%$（[[decision-tree-based-methodology-for-high-impedance-fault-detection]]）
- 短窗傅里叶（8 点窗）相对全波傅里叶（16 点窗）：动作速度提升约 50%，但相量精度降低

**动作速度**：

- 基于短窗傅里叶+复数微分方程的阻抗估计：故障后 $0.5 \sim 1$ 周波（$8 \sim 16$ ms @ 60 Hz）可得可信阻抗值
- 基于全波傅里叶的相量阻抗估计：故障后 $1 \sim 1.5$ 周波（$16 \sim 25$ ms @ 60 Hz）动作
- 矩阵束算法：故障后 $0.5$ 周波即可提取基频相量，但需额外计算开销

**EMT 仿真中的计算开销**：

| 组件 | 计算复杂度 | 说明 |
|------|---------|------|
| CT/CVT 暂态模型 | $O(1)$ per step | 二阶等效模型或查表 |
| FWF 相量提取 | $O(N)$ per sample | N = 周波采样点数 |
| 滑动 FWF | $O(1)$ per new sample | 递推实现 |
| 矩阵束算法 | $O(N^2)$ per window | SVD 分解 |
| 阻抗轨迹判别 | $O(1)$ | 坐标比较 |

## 关键技术挑战

### 挑战1：过渡电阻对保护范围的影响

过渡电阻 $R_F$（包括故障点接地电阻、电弧电阻）会使测量阻抗的电阻分量增大：

$$
Z_m = \frac{V_\phi}{I_\phi + k_0 I_0} \approx \frac{Z_{1L} \cdot I_\phi + R_F \cdot I_F}{I_\phi + k_0 I_0}
$$

当 $R_F$ 较大时，$Z_m$ 的轨迹向 $+R$ 方向偏移，导致：

- **超越动作**：故障位于下一级线路首端，但测量阻抗落入本级动作区
- **拒动**：重负荷长线路末端故障，测量阻抗恰好落在动作区边缘

**应对思路**：在 EMT 验证时使用高阻故障（如 50~100 Ω）测试，观察阻抗轨迹是否越出保护范围。

### 挑战2：系统振荡与短路故障的区分

系统振荡时，等效电源电势相角差 $\delta$ 缓慢变化，导致测量阻抗沿一条轨迹（振荡阻抗轨迹）穿越 R-X 平面。该轨迹可能穿过保护的动作区而被误判为故障。

**区分判据**：

- **$\Delta Z / \Delta t$ 判据**：故障时阻抗突变（$dZ/dt$ 大），振荡时阻抗缓变（$dZ/dt$ 小）
- **$\Delta V / \Delta I$ 判据**：短路时电压突降而电流突升，振荡时电压和电流同步变化
- **记忆电压极化**：利用故障前的电压相位作为参考，故障后电压相位突变，而振荡时电压相位缓变

### 挑战3：零序网络不确定性与互感补偿

平行线路的零序互感补偿面临两个不确定性：

1. **对端零序电流不可直接测量**：需通过故障距离和零序网络拓扑推算
2. **零序参数准确度**：线路零序阻抗受土壤电阻率、地线配置、频率依赖性影响

对于并行线路，可将零序电流表示为故障距离的线性函数 $I_{0P} = m \cdot p + q$（$p, q$ 由零序网络拓扑决定），代入故障回路方程后直接求解，无需直接测量健康平行线电流（[[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel]]）。

### 挑战4：CT/CVT 暂态误差对测量精度的影响

**CT 暂态饱和**：故障电流中含大量直流偏移分量，使 CT 铁芯快速饱和，二次电流瞬时传变误差可超过 10%，导致阻抗轨迹向原点方向偏移。

**CVT 暂态传变**：CVT 在故障后数毫秒内存在低频衰减分量（频率约 $2 \sim 5$ Hz），导致电压相量在暂态期间幅值偏小、相位偏移，从而使阻抗轨迹在 R-X 平面上振荡。

**量化影响**（据 [[protection-system-representation-in-the-electromagnetic-transients-program-power]]）：原文未给出具体量化数据，但 CT/CVT 模型并入 EMTP 的研究范式表明，EMT 仿真中引入互感器模型后，保护算法的动作边界确实需要针对暂态误差进行修正。

### 挑战5：高阻抗故障检测

高阻抗故障（HIF）的电流幅值接近负荷扰动水平，传统的低阻抗继电器难以检测。HIF 检测需要利用弧光非线性产生的低频谐波特征（2/3/5 次谐波幅值和 3 次谐波相位），结合数据驱动方法（如 CART 决策树）进行分类（[[decision-tree-based-methodology-for-high-impedance-fault-detection]]）。

检测特征工程：

| 特征 | 物理含义 | 检测依据 |
|------|---------|---------|
| 基波 RMS | 故障或操作导致的电流水平 | 故障时通常突升 |
| 2 次谐波幅值（归一化） | 弧光不对称性 | HIF 燃弧不对称时较大 |
| 3 次谐波幅值（归一化） | 弧光非线性 | HIF 时较大 |
| 5 次谐波幅值（归一化） | 弧光非线性 | HIF 时较大 |
| 3 次谐波相位 | 区分同幅值不同波形 | 弧光相位特征 |

## 适用边界与选择指南

### 阻抗继电器选型决策

| 工况 | 推荐特性 | 理由 |
|------|---------|------|
| 短线路（$< 50$ km）、过渡电阻小 | 全阻抗圆 | 结构简单，方向性由外部判别 |
| 中长线路、过渡电阻中等 | Mho（方向圆） | 自带方向性，兼顾过渡电阻 |
| 串补线路、大过渡电阻 | 四边形/多边形 | 可分别设置电抗线和电阻边界 |
| 启动元件或后备保护 | 偏移 Mho | 可覆盖正反向故障 |
| 需要精确测距 | 阻抗梯度（电抗线） | 测距与保护功能分离 |

### EMT 建模方法选择

| 仿真目标 | 推荐建模层次 | 方法 |
|---------|------------|------|
| 继电器动作特性验证 | 理想接口 | 方法1（恒定采样） |
| 测量链路精度分析 | 完整测量链路 | 方法2（CT/CVT）+ 方法3（相量提取） |
| 保护-电网闭环交互 | 完整链路 + 断路器反馈 | 方法2 + 方法3 + 动作逻辑 |
| 高阻故障与谐波分析 | 谐波特征提取 | 方法3（矩阵束）+ 方法5（参数辨识） |
| 并行线路保护验证 | 零序互感补偿 | 方法4（参数辨识）+ 方法5（互感补偿） |

### 不适用场景

阻抗继电器在以下场景需要专门验证或改进：

- **高阻故障**（$R_F > 100$ Ω）：阻抗轨迹与动作区边界重叠，需要 HIF 检测算法
- **串补线路**：串联电容使线路阻抗呈非线性（容性段），需要防止区外故障超越
- **新能源并网系统**：电力电子换流器限流模式和构网/跟网模式切换导致故障电流形态与同步发电机不同，阻抗轨迹可能由控制器限流主导
- **多端 DC 网络**：MMC 和 DAB 型 DC/DC 换流器在故障初期的高频阻抗受控制策略影响，需要高频距离保护方法（[[distance-protection-scheme-for-dc-distribution-systems-based-on-the-high-frequen]]）

## 相关方法与模型

- [[distance-protection]] — 距离保护的上层方法页，包含分区逻辑和保护配合
- [[digital-distance-protection]] — 数字实现中的采样、滤波和参数估计算法
- [[distance-relay]] — 距离继电器设备/元件描述页
- [[impedance-measurement]] — 阻抗测量的通用概念和算法
- [[fault-impedance-model]] — 故障阻抗建模及其对测量阻抗的影响
- [[symmetrical-components]] — 对称分量法（阻抗测量的序分量基础）
- [[sequence-component-method]] — 序分量方法在故障分析中的应用
- [[protection-relay-modeling]] — 保护继电器的 EMT 通用建模框架
- [[equivalent-fault-loop]] — 等值故障回路（阻抗测量的物理基础）

## 来源论文

- [[a-new-distance-relaying-algorithm-based-on-complex-differential-equation-for-sym]] — 提出短窗傅里叶滤波+复数微分方程的阻抗估计方法，支持并行线路高阻故障检测，验证工具为 EMTP
- [[a-novel-distance-protection-algorithm-in-frequency-domain-based-on-parameter-ide]] — 提出频域线性参数辨识阻抗法，R-L 线路模型，含矩阵束算法提取基频分量，防超越设计
- [[protection-system-representation-in-the-electromagnetic-transients-program-power]] — 建立 EMTP 中 CT/CVT 模型、继电器算法接口和断路器反馈的完整闭环仿真架构
- [[decision-tree-based-methodology-for-high-impedance-fault-detection]] — 利用 CART 决策树和馈线电流低次谐波特征进行 HIF 检测，采样率 1920 Hz，EMTP 仿真验证
- [[double-ended-fault-locating-method-for-parallel-lines-without-measuring-parallel]] — 提出并行线路零序互感补偿的相量测距方法，无需测量健康平行线电流
- [[distance-protection-scheme-for-dc-distribution-systems-based-on-the-high-frequen]] — 面向柔性直流配电的单端高频距离保护，利用换流器高频恒定阻抗建模