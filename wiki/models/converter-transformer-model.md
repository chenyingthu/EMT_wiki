---
title: "换流变压器 (Converter Transformer)"
type: model
tags: [converter-transformer, hvdc, transformer, valve-side, saturation]
created: "2026-04-29"
---

# 换流变压器 (Converter Transformer)

## 1. 物理对象概述

### 1.1 功能与作用

换流变压器是高压直流输电(HVDC)系统的核心设备之一，承担以下关键功能：

- **电压变换**：将交流电网电压变换为换流阀所需的工作电压（通常网侧500kV，阀侧200-300kV）
- **电气隔离**：实现交流系统与直流系统的电气隔离，提供阀侧套管绝缘
- **短路阻抗**：通过漏抗限制阀侧短路电流，保护换流阀
- **相位变换**：在12脉动换流器中提供30°相位差，消除5、7次特征谐波
- **调压功能**：通过有载调压分接头(OLTC)调节阀侧电压，优化触发角

### 1.2 结构特点

换流变压器与普通电力变压器相比，具有显著不同的结构特征：

| 结构特征 | 换流变压器 | 普通电力变压器 |
|---------|-----------|--------------|
| **阀侧套管** | 需承受直流电压叠加交流电压，采用直流套管 | 仅需承受交流电压 |
| **绝缘设计** | 需考虑直流偏磁和谐波损耗 | 工频绝缘设计 |
| **谐波负载** | 承受大量谐波电流（6脉动：12.5-15% THD） | 主要为工频负载 |
| **直流偏磁** | 需承受由触发不对称引起的直流偏磁 | 无直流偏磁问题 |
| **短路阻抗** | 通常15-18%（较高，限制短路电流） | 通常10-12% |
| **分接头范围** | ±10%～±20%，级数多 | 通常为±10% |

### 1.3 运行激励

换流变压器承受的电气激励具有显著的非正弦特征：

**网侧激励**：
- 电压：正弦交流，谐波含量通常<5%
- 频率：50/60 Hz基波
- 电流：含谐波分量，取决于换流器运行模式

**阀侧激励**：
- 电压：准方波（6脉动）或12脉动波形，含特征谐波
- 直流偏置：由触发角不对称引起的直流分量
- 谐波：6k±1次特征谐波（6脉动），12k±1次（12脉动）

**特殊激励条件**：
- 换相失败时的暂态过电压
- 直流系统故障时的过电流
- 谐波共振条件

## 2. 物理模型与数学描述

### 2.1 基本电磁方程

换流变压器遵循麦克斯韦电磁场方程组，在准静态近似下可表示为：

**磁路方程**：
$$
\nabla \times \mathbf{H} = \mathbf{J}, \quad \nabla \cdot \mathbf{B} = 0
$$

**本构关系**：
$$
\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M}) = \mu_0 \mu_r \mathbf{H}
$$

其中磁化强度 $\mathbf{M}$ 与磁场强度 $\mathbf{H}$ 的非线性关系由磁化曲线描述。

### 2.2 集总参数等效电路

#### 2.2.1 单相T型等效电路

对于单相变压器，采用T型等效电路：

$$
\begin{cases}
v_1 = R_1 i_1 + L_{l1} \frac{di_1}{dt} + \frac{d\psi_m}{dt} \\
v_2 = R_2 i_2 + L_{l2} \frac{di_2}{dt} + \frac{d\psi_m}{dt} \\
\psi_m = f_m(i_1 + i_2) \quad \text{(非线性磁化曲线)}
\end{cases}
$$

其中：
- $R_1, R_2$：原/副边绕组电阻
- $L_{l1}, L_{l2}$：漏感
- $\psi_m$：主磁链
- $f_m(\cdot)$：非线性磁化函数

#### 2.2.2 三相组式变压器模型

三相组式变压器（三台单相组成）各相独立，相域方程为：

$$
\mathbf{v}_{abc} = \mathbf{R} \mathbf{i}_{abc} + \mathbf{L}_l \frac{d\mathbf{i}_{abc}}{dt} + \frac{d\mathbf{\psi}_{m,abc}}{dt}
$$

磁化特性：
$$\psi_{m,k} = f_m(i_{m,k}), \quad k = a, b, c$$

### 2.3 磁饱和模型

#### 2.3.1 磁化曲线表示

换流变压器铁芯饱和特性通常采用以下数学模型：

**双曲正切模型**：
$$B = \frac{2B_s}{\pi} \arctan\left(\frac{\pi H}{2H_s}\right)$$

**指数模型**：
$$B = B_s \left(1 - e^{-\alpha H}\right) + \mu_0 H$$

**分段线性模型**（便于EMT实现）：
$$\psi_m = \begin{cases}
L_{m0} i_m, & |i_m| \leq I_{knee} \\
\psi_{knee} + L_{sat}(i_m - I_{knee}) \cdot \text{sgn}(i_m), & |i_m| > I_{knee}
\end{cases}$$

其中$\psi_{knee} = L_{m0} I_{knee}$为膝点磁链。

#### 2.3.2 考虑谐波的磁滞模型

对于精确的铁芯损耗计算，需考虑磁滞回线：

**Preisach模型**：
$$B(t) = \iint_{\alpha \geq \beta} \mu(\alpha, \beta) \gamma_{\alpha\beta}[H(t)] d\alpha d\beta$$

**Jiles-Atherton模型**：
$$\frac{dM}{dH} = \frac{M_{an}(H_{eff}) - M}{k - \alpha (M_{an}(H_{eff}) - M)}$$

### 2.4 直流偏磁模型

换流变压器在不对称触发条件下会承受直流偏磁，磁链方程为：

$$\psi_m(t) = \psi_{DC} + \psi_{AC} \sin(\omega t)$$

其中直流偏磁分量：
$$\psi_{DC} = \frac{1}{T} \int_0^T v_{valve}(t) dt \cdot \frac{1}{R_{DC}}$$

饱和引起的励磁电流峰值：
$$I_{exc,peak} = \frac{\psi_{DC} + \psi_{AC}}{L_{sat}}$$

### 2.5 绕组漏磁与杂散损耗

绕组漏磁场分布：
$$B_{leak}(r) = \frac{\mu_0 N I}{h_w} \left(1 - \frac{r}{r_{out} - r_{in}}\right)$$

杂散损耗计算：
$$P_{eddy} = \frac{\pi^2 f^2 B_{leak}^2 t^2}{6\rho} \cdot V_{cond}$$

## 3. EMT仿真模型

### 3.1 详细三相模型 (Detailed Three-Phase Model)

#### 3.1.1 相域饱和变压器模型

适用于相域EMT仿真器（如EMTP、PSCAD），每个铁芯支路独立建模：

**电路结构**：
- 网侧/阀侧三相绕组
- 各相铁芯磁化支路（非线性电感）
- 零序磁通路径（三相三柱式/三相五柱式/组式）

**非线性电感实现**：
$$i_{exc} = f_{sat}^{-1}(\lambda) = \frac{\lambda}{L_m} + I_{nl} \left(\frac{\lambda}{\lambda_{nl}}\right)^n$$

其中$\lambda = N \cdot \phi$为磁链。

**饱和特性参数化**：
| 参数 | 典型值 | 说明 |
|------|--------|------|
| 膝点电压 | 1.15-1.25 p.u. | 额定频率下 |
| 空载电流 | 0.3-0.6% | 额定电流百分比 |
| 饱和区斜率 | 0.05-0.1 p.u. | 相对于不饱和区 |
| 磁滞回线宽度 | 10-20% | 峰峰电压比 |

#### 3.1.2 数值实现

**伴随电路法**：
将非线性电感在时域离散化：
$$i(t) = G_{eq} v(t) + I_{hist}$$

其中等效导纳：
$$G_{eq} = \frac{\Delta t}{2L_{eq}(\lambda)}$$

**迭代求解**：
每个时步需迭代求解非线性方程：
$$F(\lambda) = \lambda - L_m \cdot f_{sat}(i_{tot}) = 0$$

### 3.2 UMEC通用变压器模型

UMEC (Unified Magnetic Equivalent Circuit) 模型适用于任意铁芯拓扑：

**磁等效电路**：
将变压器磁路表示为磁阻网络：
$$\mathcal{R}_{total} = \mathcal{R}_{core} + \mathcal{R}_{gap} + \mathcal{R}_{leak}$$

**支路磁通方程**：
$$\Phi_j = \frac{\mathcal{F}_j}{\mathcal{R}_j}, \quad \mathcal{F}_j = N i_j$$

**与电路耦合**：
$$\mathbf{v} = N \frac{d\mathbf{\Phi}}{dt}$$

### 3.3 饱和变压器模型 (BCTRAN)

基于短路阻抗和饱和曲线参数的简化模型：

**等效电路参数**：
| 参数 | 计算方法 |
|------|---------|
| $R_1, R_2$ | 负载损耗试验 |
| $X_1, X_2$ | 短路阻抗 $\times$ 绕组匝比 |
| $X_m$ | 空载电流试验 |
| 饱和曲线 | 空载电压-电流特性 |

**BCTRAN格式**（EMTP标准）：
```
TRANSFORMER
1WINDING  R1=0.002  X1=0.08
2WINDING  R2=0.001  X2=0.08  RATIO=0.6
SATURATION  FLUX=1.2  CURRENT=0.01  SLOPE=0.1
```

### 3.4 多端口等效模型

对于换流变压器与换流阀的联合仿真，采用多端口FDNE等效：

**端口定义**：
- 端口1-3：网侧ABC三相
- 端口4-6：阀侧ABC三相

**频变导纳矩阵**：
$$\mathbf{Y}(s) = \sum_{k=1}^{N} \frac{\mathbf{R}_k}{s - p_k} + \mathbf{D} + s\mathbf{E}$$

适用于高频谐波分析和雷电过电压研究。

### 3.5 考虑谐波的平均值模型

用于系统级谐波潮流分析：

**谐波等效阻抗**：
$$Z_h = R_{DC} + j h X_{leak}, \quad h = 1, 5, 7, 11, 13, ...$$

**谐波电流分配**：
$$I_{h,AC} = I_{h,DC} \cdot \frac{Z_{h,filter}}{Z_{h,filter} + Z_{h,transformer}}$$

## 4. 仿真软件实现

### 4.1 EMTP/ATP实现

**SATURABLE TRANSFORMER元件**：
```
TRANSFORMER THREEPHASE
1WINDING BUS1A BUS1B BUS1C  R=0.002  X=0.08
2WINDING BUS2A BUS2B BUS2C  R=0.001  X=0.08  RATIO=0.6
SATURATION FLUX=[1.0,1.15,1.3,1.5]  CURRENT=[0.001,0.005,0.02,0.1]
```

**BCTRAN元件**：
基于铭牌参数自动计算等效电路，支持三相/单相、双绕组/三绕组。

**XFORMER元件**：
基于几何参数的物理模型，需要铁芯尺寸、绕组匝数等信息。

### 4.2 PSCAD/EMTDC实现

**UMEC变压器模型**：
- 支持三相三柱/五柱/组式铁芯
- 可设置各相独立饱和特性
- 支持零序磁通建模

**经典变压器模型**：
- 理想变压器+漏抗+励磁支路
- 非线性励磁电感通过Type-96/98实现

**接口配置**：
```fortran
! PSCAD变压器模型接口
SUBROUTINE TRANSFORMER(T,DT,VD,CD,XD,SD,ND,NS,INPUT,OUTPUT)
  ! T: 当前时间
  ! DT: 时间步长
  ! VD: 节点电压数组
  ! CD: 支路电流数组
  ! 返回OUTPUT: 注入电流
END SUBROUTINE
```

### 4.3 MATLAB/Simulink实现

**Simscape Electrical模型**：
- Three-Phase Transformer (Two Windings)
- Saturable Transformer
- 支持磁滞和饱和

**Simulink实现**：
```matlab
% 饱和变压器模型
function [v1, v2] = saturated_transformer(i1, i2, lambda)
    % 非线性磁化特性
    im = (i1 + i2 * N2/N1);
    if abs(lambda) < lambda_knee
        lambda = Lm * im;
    else
        lambda = lambda_knee + Lsat * (im - im_knee);
    end
    
    % 电压计算
    v1 = R1*i1 + Ll1*di1/dt + dlambda/dt;
    v2 = R2*i2 + Ll2*di2/dt + dlambda/dt * N2/N1;
end
```

### 4.4 实时仿真器(RTDS)实现

**大时间步长模型**：
- 基于频率相关等效的简化模型
- 适用于系统级实时仿真（步长50-100μs）

**详细模型**：
- 需要较小步长（10-20μs）
- 配合GPC卡实现多处理器并行

**硬件接口**：
- 模拟量输出：阀侧电压、电流
- 数字量输入：分接头位置、保护信号

## 5. 典型参数参考

### 5.1 ±800kV/8000MW换流变压器参数

| 参数 | 网侧(Y) | 阀侧(Δ) | 单位 |
|------|--------|--------|------|
| 额定电压 | 525 | 210 | kV |
| 额定容量 | 1200 | 1200 | MVA |
| 短路阻抗 | 16 | 16 | % |
| 空载损耗 | 300 | 300 | kW |
| 负载损耗 | 2500 | 2500 | kW |
| 空载电流 | 0.4 | 0.4 | % |

**饱和特性**：
- 膝点电压：1.2 p.u.
- 空载电流@1.0 p.u.：0.3%
- 空载电流@1.3 p.u.：5%

### 5.2 12脉动换流变压器组

**网侧绕组**：
- YY变压器：相位移0°
- YΔ变压器：相位移30°

**阀侧绕组**：
- 双绕组结构
- 绝缘水平：LIWV 650kV

**分接头范围**：±15%，每级1.25%

### 5.3 仿真模型参数设置

**详细模型步长建议**：
| 仿真类型 | 推荐步长 | 原因 |
|---------|---------|------|
| 铁磁谐振分析 | 1-10 μs | 捕捉饱和非线性 |
| 雷电过电压 | 10-20 ns | 波头陡峭 |
| 操作过电压 | 10-50 μs | 中等频率 |
| 系统级暂态 | 50-100 μs | 效率优先 |

**收敛参数**：
- 最大迭代次数：10-20次
- 残差容差：1e-6 p.u.
- 松弛因子：0.5-0.8（饱和区域）

### 5.4 模型选择指南

| 应用场景 | 推荐模型 | 理由 |
|---------|---------|------|
| 铁磁谐振研究 | UMEC详细模型 | 精确饱和特性 |
| 换相失败分析 | BCTRAN模型 | 计算效率 |
| 雷电过电压 | 多端口FDNE | 宽频特性 |
| 系统级稳定性 | 平均值模型 | 大步长可行 |
| 实时仿真 | 简化等效 | 实时性要求 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[transformer-model|变压器模型]] - 通用变压器建模方法
- [[mmc-model|MMC模型]] - 换流阀详细模型
- [[vsc-model|VSC模型]] - 电压源换流器模型
- [[lcc-model|LCC模型]] - 线路换相换流器模型

### 6.2 相关方法
- [[vector-fitting|矢量拟合]] - 频变参数辨识
- [[fixed-admittance|恒导纳模型]] - 高效变压器仿真
- [[state-space-method|状态空间法]] - 变压器状态空间实现

### 6.3 相关主题
- [[vsc-hvdc|VSC-HVDC]] - 柔性直流输电系统
- [[ferroresonance|铁磁谐振]] - 变压器铁磁谐振现象
- [[harmonic-analysis|谐波分析]] - 换流变压器谐波负载

## 7. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| [[measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag|Measurement-based frequency dependent model of a HVDC transformer]] | 2019 | 基于测量的HVDC变压器频变模型，5Hz-10MHz |
| [[a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions|A high frequency transformer model for the EMTP]] | 2001 | 高频变压器模型，适用于电磁暂态 |
| [[electromagnetic-transient-modeling-and-simulation-of-large-power-systems-emt-sim|Electromagnetic Transient Modeling of Large Power Systems]] | 2025 | 大规模系统EMT建模，含变压器详细模型 |

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自EMT领域学术文献的深度分析*
