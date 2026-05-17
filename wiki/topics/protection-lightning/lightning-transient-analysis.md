---
title: "雷击暂态分析 (Lightning Transient Analysis)"
type: topic
tags: [lightning, transient, overvoltage, backflashover, shielding-failure, backflashover-rate, induced-lightning, emt]
created: "2026-05-04"
updated: "2026-05-17"
---

# 雷击暂态分析 (Lightning Transient Analysis)

## 定义与边界

雷击暂态分析是研究雷电放电对电力系统产生的电磁暂态过程的方法，涵盖直击雷（雷电直接击中线路或设备）和感应雷（雷云放电在附近线路感应过电压）两种主要形式。EMT仿真用于计算雷击引起的过电压波形、传播特征和绝缘闪络风险。

**边界限定**：本页面聚焦于雷击电磁暂态的**EMT建模方法**，不包括雷电物理机理（电荷分离、放电通道物理）或防雷装置（接闪器、避雷线）设计细节。相关防雷装置内容见[[surge-arrester-model]]和[[grounding-system-model]]。

**与相邻页面的区分**：
- [[lightning-induced-voltage]]：专注感应雷过电压的建模与计算
- [[insulator-string-model]]：绝缘子闪络判据（伏秒特性），不涉及雷电流注入
- [[grounding-system-model]]：杆塔接地与雷电流泄放的等效电路建模
- [[surge-arrester-model]]：避雷器保护特性与配合

## EMT中的作用

雷击暂态分析是输电线路绝缘配合的核心，其EMT仿真目标为：

1. **过电压计算**：确定雷击引起的线路和变电站过电压水平及其沿线路的传播分布
2. **绝缘闪络评估**：判断雷击过电压是否导致绝缘子闪络（反击/绕击）
3. **防雷设计优化**：评估避雷线屏蔽效果、接地电阻对接地电位升的影响
4. **保护配合**：避雷器配置与绝缘水平的协调（见[[surge-arrester-model]]）

**典型EMT分析场景**：
- 直击雷塔顶：雷电流注入杆塔，雷电流沿塔身流向接地系统，引起杆塔电位升高
- 感应雷过电压：雷电通道辐射电磁场在附近线路上耦合感应过电压（间接雷击）
- 多回线耦合：同塔多回线路的相互耦合影响（见[[transmission-line-model]]）

<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <!-- 定义 -->
  <rect x="10" y="10" width="200" height="50" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="42" text-anchor="middle" font-size="14" font-weight="bold" fill="#1e40af">雷电流源模型</text>
  <!-- 机制 -->
  <rect x="250" y="10" width="200" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="350" y="28" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">直击雷</text>
  <text x="350" y="44" text-anchor="middle" font-size="12" fill="#92400e">杆塔接地阻抗</text>
  <rect x="250" y="75" width="200" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="350" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">感应雷</text>
  <text x="350" y="109" text-anchor="middle" font-size="12" fill="#92400e">Rusck耦合模型</text>
  <rect x="250" y="140" width="200" height="50" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="350" y="158" text-anchor="middle" font-size="12" font-weight="bold" fill="#92400e">反击/绕击</text>
  <text x="350" y="174" text-anchor="middle" font-size="12" fill="#92400e">闪络判据(V-t)</text>
  <!-- 分析 -->
  <rect x="490" y="75" width="180" height="115" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="580" y="100" text-anchor="middle" font-size="12" font-weight="bold" fill="#166534">过电压传播</text>
  <text x="580" y="118" text-anchor="middle" font-size="11" fill="#166534">→ 线路波阻抗</text>
  <text x="580" y="132" text-anchor="middle" font-size="11" fill="#166534">→ 折射与反射</text>
  <text x="580" y="146" text-anchor="middle" font-size="11" fill="#166534">→ 绝缘子应力</text>
  <text x="580" y="160" text-anchor="middle" font-size="11" fill="#166534">→ 闪络/不闪络</text>
  <!-- 输出 -->
  <rect x="710" y="75" width="180" height="115" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
  <text x="800" y="100" text-anchor="middle" font-size="12" font-weight="bold" fill="#4c1d95">量化性能边界</text>
  <text x="800" y="118" text-anchor="middle" font-size="11" fill="#4c1d95">反击跳闸率</text>
  <text x="800" y="132" text-anchor="middle" font-size="11" fill="#4c1d95">绕击跳闸率</text>
  <text x="800" y="146" text-anchor="middle" font-size="11" fill="#4c1d95">最大过电压(kV)</text>
  <text x="800" y="160" text-anchor="middle" font-size="11" fill="#4c1d95">接地电位升(kV)</text>
  <!-- 箭头 -->
  <line x1="210" y1="35" x2="245" y2="35" stroke="#333" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="210" y1="100" x2="245" y2="100" stroke="#333" stroke-width="2"/>
  <line x1="210" y1="165" x2="245" y2="130" stroke="#333" stroke-width="2"/>
  <line x1="450" y1="100" x2="485" y2="132" stroke="#333" stroke-width="2"/>
  <line x1="670" y1="132" x2="705" y2="132" stroke="#333" stroke-width="2"/>
  <!-- 图例 -->
  <rect x="10" y="230" width="18" height="18" rx="3" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
  <text x="35" y="244" font-size="12" fill="#333">输入：雷电流源模型</text>
  <rect x="250" y="230" width="18" height="18" rx="3" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="275" y="244" font-size="12" fill="#333">处理：雷击机制</text>
  <rect x="490" y="230" width="18" height="18" rx="3" fill="#dcfce7" stroke="#16a34a" stroke-width="1.5"/>
  <text x="515" y="244" font-size="12" fill="#333">分析：过电压传播</text>
  <rect x="710" y="230" width="18" height="18" rx="3" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="735" y="244" font-size="12" fill="#333">输出：量化性能边界</text>
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#333"/>
    </marker>
  </defs>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · 雷击暂态分析EMT建模流程图</p>

## 主要分支与机制

### 1. 直击雷过电压

直击雷是雷电直接击中杆塔、避雷线或导线的场景。EMT建模的核心是**雷电流源模型**和**杆塔接地阻抗模型**。

#### 雷电流模型（Heidler模型）

Heidler模型是EMT程序中描述雷电流波形最广泛使用的解析模型：

$$i(t) = \frac{I_m}{\eta} \cdot \frac{(t/\tau_1)^{10}}{1 + (t/\tau_1)^{10}} \cdot e^{-t/\tau_2}$$

其中：$I_m$为峰值电流（kA），$\tau_1$为波前时间常数（μs），$\tau_2$为波尾时间常数（μs），$\eta$为峰值归一化因子。

**CIGRE推荐的Heidler参数**（用于标准雷电流波形）：

| 参数 | 首次雷击（10/350 μs） | 后续雷击（0.25/100 μs） |
|------|---------------------|----------------------|
| $I_m$ | 200 kA（极高架）~30 kA（配电） | 200 kA |
| $\tau_1$ | 10 μs | 0.25 μs |
| $\tau_2$ | 350 μs | 100 μs |
| $\eta$ | 约 0.93 | 约 0.95 |

**双指数模型的备选形式**：
$$i(t) = A \cdot I_m \cdot (e^{-t/\tau_1} - e^{-t/\tau_2})$$

IEEE Std. 1243-1997推荐使用双指数模型进行输电线路雷电性能估算。

#### 杆塔接地阻抗模型

当雷击塔顶时，雷电流沿杆塔流向接地系统，杆塔电位（接地电位升，GPR）为：

$$U_{GPR}(t) = R_g \cdot i(t) + L_t \cdot \frac{\mathrm{d}i(t)}{\mathrm{d}t}$$

其中$R_g$为接地电阻（Ω），$L_t$为杆塔等效电感（H）。

**Schroeder等(2018)的关键发现**：传统EMT程序将接地系统简化为恒定电阻$R_g$，但雷电流含有丰富的高频分量（DC~MHz），此时：
- **接地阻抗的宽频特性**：接地电极在高频下的阻抗不再等于直流接地电阻，而是一个宽频复阻抗
- **土壤参数频变效应**：土壤电阻率$\rho$和介电常数$\varepsilon_r$均随频率变化（所谓"土壤频变模型"）
- **量化影响**：考虑土壤频变特性后，接地脉冲阻抗峰值降低，首次雷击时GPR最大降幅约27.1%（Schroeder等2018, Table 5）
- **对反击跳闸率的间接影响**：GPR降低会减小绝缘子串两端电压，从而降低反击跳闸率

**频变土壤的EMT建模方法**（Schroeder等2018）：
- 采用Vector Fitting技术将接地电极的宽频阻抗响应拟合为有理函数模型
- 将拟合结果转换为等效EMT电路（π型等效或诺顿等效电流源）
- 在EMTP/ATP中通过时域递归卷积实现频变接地模型

#### 杆塔波过程模型

雷击杆塔时，雷电通道与杆塔构成复合传输线系统。杆塔电位不仅取决于接地阻抗，还取决于雷电流在杆塔体内的传播。Yin等(2023)提出：

**分叉结构杆塔的简化等效电路**：
- 多段分割法建模下导线（down-lead），考虑互感和寄生电容
- 建议将杆塔下导线简化为集中参数分段传输线

$$Z_{tower}(\omega) = Z_0 \cdot \frac{\sinh(\gamma h)}{\sinh(\gamma h) + \frac{Z_0}{Z_g}(\omega) \cdot \cosh(\gamma h)}$$

其中$Z_0$为杆塔波阻抗，$\gamma$为传播常数，$h$为塔高，$Z_g(\omega)$为接地频变阻抗。

### 2. 感应雷过电压

感应雷（indirect lightning / induced lightning）是雷云放电在附近输电线路上通过电磁耦合感应过电压。Rusck(1958)提出了经典理论：

#### Rusck模型

**单根导线上的感应过电压**（Rusck 1958年原始公式）：

$$U_i(h, y, t) = \frac{Z_0 \cdot I_0 \cdot h}{y} \cdot \frac{1}{\sqrt{1 + (v \cdot t / 2y)^2}} \cdot \frac{1}{\sqrt{1 + (v \cdot t / 2y)^2}} \cdot e^{-t/\tau_2}$$

化简后时域形式：

$$U_i(h, y, t) = \frac{30 \cdot I_0 \cdot h}{y^2} \cdot \frac{v \cdot t}{(1 + (vt/2y)^2)^{3/2}} \quad \text{(波形近似)}$$

其中：$Z_0 \approx 60 \ln(2h/r)$为线路波阻抗（Ω），$h$为导线对地高度（m），$y$为雷击点与线路的水平距离（m），$v$为光速。

**De Conti等(2020)的扩展**：Rusck原始公式适用于单根导线，实际配电线路为三相结构。紧凑型配电线路的感应雷分析需考虑：
- 相间耦合效应（三相导线的相互耦合）
- 频变传输线模型（Marti模型或有限差分时域FDTD方法）
- 土壤损耗对感应过电压幅值的影响（损耗增大时感应电压衰减）

**Mashayekhi和Kordi(2013)的快速算法**：
- 采用混合时频宏模型框架（mixed time-frequency macro-model）
- 通过追踪雷电-传输线系统的传递函数极点与留数来构建端口型等效
- 避免了逐点FDTD计算，计算效率显著提升

### 3. 反击与绕击机制

#### 反击（Backflashover）

反击是雷击杆塔或避雷线后，雷电流沿塔身流向接地系统，引起绝缘子串两端电压超过其闪络强度而发生的闪络。

**反击过程**：
1. 雷击塔顶/避雷线 → 雷电流$i(t)$注入杆塔
2. 杆塔电位升高：$U_{tower}(t) = R_g \cdot i(t) + L_t \cdot \mathrm{d}i(t)/\mathrm{d}t$
3. 绝缘子电压：$U_{ins}(t) \approx U_{tower}(t) - U_{phase}(t)$
4. 当$U_{ins}(t) > U_{flashover}(t)$（伏秒特性曲线）时发生反击闪络

**反击跳闸率**（IEEE Std. 1243）：

$$N_{bf} = N_g \cdot L \cdot \eta_{bf} \cdot P_{bf}$$

其中：$N_g$为地闪密度（次/km²/年），$L$为线路长度（km），$\eta_{bf}$为反击闪络率，$P_{bf}$为建弧率。

#### 绕击（Shielding Failure）

绕击是雷电绕过避雷线屏蔽直接击中导线的现象。

**电气几何模型（EGM）**：

绕击暴露距离（导线暴露区域的临界击距）：

$$r_c = 8 \cdot I^{0.65} \quad \text{（m，平原地区）}$$

避雷线保护距离：

$$r_g = 8 \cdot I^{0.65} \cdot k_g$$

其中$k_g$为地形系数（山区$k_g < 1$，平原$k_g = 1$）。

当$I < I_{critical}$（临界保护电流）时，雷电绕过避雷线击中导线。

**绕击跳闸率**：

$$N_{sf} = N_g \cdot L \cdot \eta_{sf} \cdot P_{sf}$$

## 形式化表达

### 雷击跳闸率综合计算

$$N = N_g \cdot L \cdot (\eta_{bf} \cdot P_{bf} + \eta_{sf} \cdot P_{sf})$$

其中各参数定义如上。

### 线路波阻抗与传播

对于均匀单导线线路，特性阻抗为：

$$Z_c = \frac{1}{2\pi} \sqrt{\frac{\mu_0}{\varepsilon_0}} \ln\frac{2h}{r} \approx 60 \ln\frac{2h}{r} \quad \text{(Ω)}$$

其中$h$为导线对地高度，$r$为导线半径。

**波过程**：雷击过电压沿线路传播，遇到阻抗不连续点（杆塔、换位塔、分支线路）产生折射和反射。

### 接地脉冲阻抗的频变特性

**Portela频变土壤模型**（Schroeder等2018引用）：

$$\rho(\omega) = \rho_0 \cdot \left[1 + k \cdot \left(\frac{\omega}{\omega_0}\right)^n\right]$$

**通用土壤模型的阻抗表达式**（K.S. Smith & Longmire Universal Soil Model）：

$$Z_g(\omega) = \frac{\rho}{\sqrt{\varepsilon_r(\omega)}} \cdot \frac{\Gamma(\omega)}{2\pi h} \cdot \coth(\gamma h)$$

频变效应使高频下接地阻抗降低，从而减少GPR峰值。

### 波形相关电晕模型（Jiang 2024）

**电晕电荷动态方程**（临界体积法）：

$$Q(t) = Q_0 \cdot \left[1 - e^{-(t - t_0)/\tau_{relax}}\right] \cdot u(t - t_0)$$

其中$t_0$为起晕延时，$\tau_{relax}$为电离弛豫时间常数，$u(t)$为单位阶跃函数。

**电晕电容**（时变）：

$$C_{corona}(t) = C_0 + \frac{Q(t)}{U(t)}$$

Jiang等(2024)在PSCAD/EMTDC中实现了波形相关电晕模型，发现：波形越缓（波前时间越长），电晕衰减越显著；波前时间从5 μs增至20 μs时，过电压峰值衰减约15%~25%。

## 关键技术挑战

### 挑战1：接地阻抗的宽频建模

**问题描述**：雷电流频谱从DC延伸至数MHz，而土壤电阻率$\rho$和介电常数$\varepsilon_r$均随频率变化（高频下$\rho$降低、$\varepsilon_r$升高），传统的恒定电阻接地模型无法捕捉这一效应。

**EMT建模方法**：
- **等效电路法**：将接地电极的宽频阻抗响应用Vector Fitting拟合成有理函数，再转化为EMT程序可用的等效电路（Schroeder等2018）
- **时域递归卷积法**：在时域中使用递归卷积积分直接计算频变接地响应

**量化数据**：忽略土壤频变特性时，GPR峰值被系统性高估，首次雷击时高估幅度最大约27.1%（Schroeder等2018, Table 5）；对绝缘子过电压的影响相对较小（约数个百分点）。

### 挑战2：电晕效应对过电压传播的影响

**问题描述**：当导线表面电场超过空气电离临界值时，电晕放电产生空间电荷，改变线路的有效电容和波阻抗，导致冲击波在传播过程中发生衰减、畸变和波形转换（波前变缓、峰值降低）。

**EMT建模方法**（Jiang等2024）：
- 采用临界体积法计算起晕延时：$t_0 = \tau_{ionization} \cdot \ln(E_{max}/E_{crit})$
- 考虑电离弛豫过程：$\tau_{relax}$影响空间电荷建立速度
- 非迭代算法：将非线性电晕电容嵌入EMT程序，避免迭代求解

**量化数据**：波前时间5 μs→20 μs时，过电压峰值衰减15%~25%（Jiang等2024，PSCAD验证工况）。

### 挑战3：感应雷耦合模型的计算效率

**问题描述**：计算雷电通道辐射电磁场对线路上每一点的感应电压，传统有限差分时域（FDTD）方法计算量极大（需要沿线逐点采样并迭代）。

**EMT建模方法**（Mashayekhi和Kordi 2013）：
- **混合时频宏模型**：提取雷电-传输线系统的传递函数$H(\omega)$的极点$p_k$和留数$R_k$
- **时域实现**：$U(t) = \sum_{k} R_k \cdot e^{p_k t}$（指数和形式），避免FDTD逐点迭代
- 计算效率比FDTD方法提升约一个数量级

### 挑战4：分叉结构杆塔的精确建模

**问题描述**：实际EHV/UHV杆塔具有复杂的分叉结构（横担、地线支柱、绝缘子挂点），"单根分布参数杆塔"简化模型无法描述雷击偏置点时绝缘子电压的左右不对称性。

**EMT建模方法**（Yin等2023）：
- **多段分割下导线模型**：将横担和地线支柱分别建模，考虑各段间互感和寄生电容
- **简化经验公式**：基于格子图法（lattice diagram method）推导分叉结构的简化等效电路
- **量化精度**：简化模型与完整FDTD结果对比，最大误差<8%（Yin等2023, Aalborg大学测试塔）

### 挑战5：土壤电离对冲击接地阻抗的影响

**问题描述**：高幅值雷电流（>10 kA）流入接地极时，接地极周围土壤发生电离，电离区的等效电阻率降低，导致接地阻抗在暂态过程中从高值非线性降低到低值（冲击电离效应）。

**EMT建模方法**：
- **两区域土壤电离模型**：电离区内电阻率$\rho_i = \rho_0 / \chi$（$\chi$为电离系数），电离区边界由电场临界值$E_c$确定
- **迭代求解**：在每个时步根据电流密度判断电离边界位置，再计算等效阻抗

**关键参数**：土壤临界电离梯度$E_c \approx 300 \sim 500$ kV/m（取决于土壤类型和湿度）。

## 量化性能边界

基于多个来源论文的实验和仿真数据：

| 指标 | 典型范围 | 代表数据来源 |
|------|---------|-------------|
| 反击GPR峰值 | 100 kV ~ 1000 kV（取决于$I_m$和$R_g$） | Schroeder等2018：138 kV线路，GPR峰值365 kV（30 kA雷电流） |
| 土壤频变导致的GPR降幅 | 约15%~27%（首次雷击） | Schroeder等2018：最大27.1%（Portela公式） |
| 电晕导致的过电压峰值衰减 | 10%~25%（取决于波前时间） | Jiang等2024：波前5→20 μs，峰值衰减15%~25% |
| 感应雷过电压幅值 | 10 kV ~ 500 kV | Rusck 1958，De Conti等2020：15 kV紧凑线路，感应电压峰值约120 kV |
| 杆塔波阻抗 | 100 Ω ~ 300 Ω（取决于塔型） | Yin等2023：76 m双回路塔，等效波阻抗约150 Ω |
| 建弧率（工频续流） | 0.5 ~ 0.9（取决于绝缘子类型） | IEEE Std. 1243 |
| 地闪密度$N_g$ | 1 ~ 40 次/km²/年（地区差异极大） | IEEE Std. 1243 |

## 适用边界与选择指南

### 适用条件

- 雷电流参数（峰值$I_m$、波前时间$\tau_1$、波尾时间$\tau_2$）服从对数正态分布，可基于统计分布随机抽取
- 土壤电阻率已知，用于接地计算（建议取雷电高频下的等效值，而非直流值）
- 线路参数（波阻抗、衰减系数）准确，建模为均匀传输线或频变传输线
- 绝缘子伏秒特性曲线已知

### 失效边界

| 场景 | 失效原因 | 建议 |
|------|---------|------|
| 高土壤电阻率地区（$\rho > 1000 \Omega \cdot m$） | 位移电流和频变效应不可忽略，Carson大地返回公式可能产生显著误差 | 使用Schroeder等2018的频变土壤模型 |
| 多回线同塔 | 线间耦合改变各回线雷电分布，需多导体传输线模型 | 采用完整的模域多导体模型（见[[transmission-line-model]]） |
| 城市配电网（复杂电磁环境） | 建筑物屏蔽效应难以精确建模，感应雷计算误差增大 | 现场实测标定或二维FDTD全波计算 |
| 特高压线路（$\ge 500$ kV） | 杆塔结构复杂（高度>60 m），波过程需分布参数模型 | Yin等2023分叉杆塔模型或多段分布参数杆塔 |
| 绝缘子老化 | 老化绝缘子闪络电压降低，实测值与标准值偏差可达±20% | 使用实际伏秒特性曲线而非标准曲线 |

### 模型选择决策

| 场景 | 推荐模型 | 说明 |
|------|---------|------|
| 配电线路（< 35 kV）直击雷 | Heidler + 恒定接地电阻 | 接地系统简单，频变效应相对次要 |
| 高压/超高压线路反击分析 | Heidler + 频变接地模型（Vector Fitting） | 接地阻抗宽频特性主导反击风险 |
| 感应雷过电压计算 | Rusck模型（或De Conti 2020扩展公式） | 三相线路需考虑相间耦合 |
| 电晕主导的过电压传播（> 345 kV） | 波形相关电晕模型（Jiang 2024） | 导线表面电场超过临界值时 |
| 分叉结构杆塔 | Yin等2023分段下导线模型 | 横担结构不对称时 |
| 土壤电离主导 | Portela双区域模型 | 雷电流峰值>10 kA时 |

## 相关模型

- [[transmission-line-model]] — 输电线路波过程建模基础
- [[insulator-string-model]] — 绝缘子闪络模型（伏秒特性）
- [[grounding-system-model]] — 接地系统建模与接地阻抗计算
- [[surge-arrester-model]] — 避雷器保护特性与配合
- [[waveform-propagation]] — 雷电冲击波的传播与衰减特性
- [[vsc-model]] — 换流器建模（涉及雷电过电压对电力电子设备的影响）

## 来源论文

以下论文为本文提供了关键建模方法和量化数据：

- **Jiang等 2024** — 波形相关电晕模型（PSCAD/EMTDC）：电晕电荷动态方程、起晕延时计算、非迭代算法
- **Schroeder等 2018** — 频变土壤对接地过电压的影响：接地宽频阻抗Vector Fitting、GPR降幅量化（最大27.1%）
- **De Conti等 2020** — 紧凑配电线路感应雷分析：Rusck模型的扩展验证、三相模域模型
- **Mashayekhi和Kordi 2013** — 感应电压快速算法：混合时频宏模型、极点留数提取
- **Yin等 2023** — 分叉结构杆塔冲击响应：多段分割下导线模型、简化经验公式
- **Rusck 1958** — 感应雷过电压原始理论公式