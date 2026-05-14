---
title: "储能变流器 (Energy Storage Converter)"
type: model
tags: [energy-storage, converter, bess, battery, grid-scale, frequency-regulation]
created: "2026-04-30"
updated: "2026-05-12"
---

# 储能变流器 (Energy Storage Converter)



## 定义与概述

储能变流器（Energy Storage Converter/PCS）是连接储能电池与电网的电力电子接口，实现电池直流电与交流电网之间的双向能量转换。随着可再生能源渗透率提高和电网灵活性需求增加，储能系统在调频、调峰、备用和黑启动等方面发挥着越来越重要的作用。本模型涵盖储能变流器拓扑、双向充放电控制、SOC管理、并网模式切换，适用于电网级储能系统的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- 双向AC/DC功率转换
- 电池充放电控制
- 有功/无功独立调节
- 并网/离网模式切换
- 黑启动能力

**储能变流器类型**:
| 类型 | 功率范围 | 电压等级 | 应用场景 |
|------|----------|----------|----------|
| 户用储能 | 3-20kW | 220/400V | 家庭光储 |
| 工商业储能 | 100kW-2MW | 400V-10kV | 削峰填谷 |
| 电网级储能 | 10-100MW | 35-220kV | 调频调峰 |
| 高压直挂 | 10-100MW | 10-35kV | 无需变压器 |

**电池类型配套**:
| 电池类型 | 特点 | 变流器要求 |
|----------|------|------------|
| 磷酸铁锂(LFP) | 安全、长寿命 | 标准双向PCS |
| 三元锂(NCM) | 高能量密度 | 高功率PCS |
| 钠离子 | 低成本 | 标准PCS |
| 液流电池 | 长时储能 | 低压大电流PCS |

### 1.2 系统结构

**典型储能系统架构**:
```
  ┌─────────────────────────────────────┐
  │           储能系统                   │
  │  ┌─────┐  ┌─────┐  ┌─────┐         │
  │  │电池 │──│ BMS │──│ PCS │──┬──→ 交流电网
  │  │模组 │  │     │  │     │  │     │
  │  └─────┘  └─────┘  └─────┘  │     │
  │      ↑         ↑        ↑    │     │
  │   SOC/电压   均衡     并离网  │     │
  │      管理    控制     切换    │     │
  │                               ↓     │
  │                          能量管理   │
  │                          (EMS)     │
  └─────────────────────────────────────┘
```

**两级式PCS**:
```
电池 ──→ DC/DC ──→ DC母线 ──→ DC/AC ──→ 交流
     (Buck-Boost)     (逆变)
```

**单级式PCS**:
```
电池 ──→ DC/AC ──→ 交流
  (直接逆变)
```

### 1.3 运行激励

**功率指令**：
- 有功功率：$P_{ref}$（充电为负，放电为正）
- 无功功率：$Q_{ref}$
- 功率限制：$|P| \leq P_{rated}$

**SOC约束**：
- SOC范围：10%-90%（安全运行区）
- SOC上限：充电功率限制
- SOC下限：放电功率限制

**电网条件**：
- 并网电压：额定±10%
- 频率：50/60Hz ±偏差
- 并网/离网切换

## 2. 物理模型与数学描述

### 2.1 主电路模型

#### 2.1.1 单级式拓扑

**两电平全桥逆变器**:
$$v_{inv} = m \cdot V_{bat}$$

其中 $m$ 为调制比。

**LC滤波器**:
$$L_f \frac{di_{inv}}{dt} = v_{inv} - v_c$$
$$C_f \frac{dv_c}{dt} = i_{inv} - i_g$$

#### 2.1.2 两级式拓扑

**DC/DC级（Buck-Boost）**:
$$V_{bus} = \frac{1}{1-d} V_{bat} \quad (Boost模式)$$
$$V_{bus} = d \cdot V_{bat} \quad (Buck模式)$$

**DC/AC级**:
$$v_g = m \cdot V_{bus}$$

### 2.2 SOC模型

**SOC定义**:
$$SOC(t) = SOC_0 + \frac{1}{C_{rated}} \int_0^t \eta \cdot i_{bat}(\tau) d\tau$$

**离散形式**:
$$SOC[k+1] = SOC[k] + \frac{\eta \cdot P_{bat}[k] \cdot T_s}{C_{rated} \cdot V_{bat}}$$

**充放电效率**:
$$\eta = \begin{cases}
\eta_{ch}, & P_{bat} > 0 \text{ (充电)} \\
1/\eta_{dis}, & P_{bat} < 0 \text{ (放电)}
\end{cases}$$

**功率限幅（基于SOC）**:
$$P_{max,dis} = P_{rated} \cdot \min\left(1, \frac{SOC - SOC_{min}}{SOC_{safe} - SOC_{min}}\right)$$
$$P_{max,ch} = P_{rated} \cdot \min\left(1, \frac{SOC_{max} - SOC}{SOC_{max} - SOC_{safe}}\right)$$

### 2.3 充放电控制策略

#### 2.3.1 恒流恒压(CC-CV)

**充电过程**:
1. 恒流阶段：$I_{ch} = I_{CC}$（至80-90% SOC）
2. 恒压阶段：$V_{ch} = V_{CV}$（至100% SOC）
3. 涓流阶段：小电流补足

**电流指令**:
$$i_{bat}^* = \begin{cases}
I_{CC}, & V_{bat} < V_{CV} \\
I_{CV}, & V_{bat} \geq V_{CV}
\end{cases}$$

#### 2.3.2 电网支撑控制

**一次调频**:
$$P_{ref} = P_0 + K_f \cdot \Delta f$$

**虚拟惯量**:
$$P_{ref} = P_0 - 2H \frac{d\Delta f}{dt}$$

**AGC跟踪**:
$$P_{ref} = P_{AGC}$$

### 2.4 并网控制

**跟网型(GFL)模式**:
- 使用PLL跟踪电网
- 电流源控制模式
- 适用于强电网

**构网型(GFM)模式**:
- 自主建立电压
- 电压源控制模式
- 适用于弱电网/孤岛

## 3. EMT仿真模型

### 3.1 电池模型接口

**等效电路模型**:
$$V_{bat} = V_{oc}(SOC) - R_{int}(SOC, T) \cdot I_{bat}$$

**功率约束**:
$$P_{PCS} = P_{bat} \cdot \eta_{PCS} - P_{loss}$$

### 3.2 SOC管理

**实时SOC计算**:
```
if charging:
    SOC = SOC + P_ch * eta_ch * dt / E_rated
else if discharging:
    SOC = SOC - P_dis / eta_dis * dt / E_rated
```

**SOC限功率**:
```
if SOC > SOC_max:
    P_ch = 0  # 禁止充电
if SOC < SOC_min:
    P_dis = 0  # 禁止放电
```

### 3.3 并离网切换

**并网→离网**:
1. 检测电网故障
2. 断开并网开关
3. 切换至GFM模式
4. 建立电压频率

**离网→并网**:
1. PLL同步
2. 电压幅值/相位匹配
3. 闭合并网开关
4. 切换至GFL模式

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**SOC管理**:
```fortran
! SOC计算
IF (P_BAT > 0) THEN  ! 充电
  SOC = SOC + P_BAT * ETA_CH * DT / E_RATED
ELSE  ! 放电
  SOC = SOC + P_BAT / ETA_DIS * DT / E_RATED
END IF

! SOC限幅
SOC = MAX(MIN(SOC, SOC_MAX), SOC_MIN)

! 功率限幅
IF (SOC > SOC_MAX_SOFT) THEN
  P_MAX_CH = P_RATED * (SOC_MAX - SOC) / (SOC_MAX - SOC_MAX_SOFT)
ELSE
  P_MAX_CH = P_RATED
END IF

IF (SOC < SOC_MIN_SOFT) THEN
  P_MAX_DIS = P_RATED * (SOC - SOC_MIN) / (SOC_MIN_SOFT - SOC_MIN)
ELSE
  P_MAX_DIS = P_RATED
END IF
```

**一次调频**:
```fortran
! 频率偏差
DELTA_F = F_MEAS - F_NOM

! 调频功率
P_FREQ = -KF * DELTA_F

! 总功率指令
P_REF = P_BASE + P_FREQ + P_AGC

! 限幅
P_REF = MAX(MIN(P_REF, P_MAX_DIS), -P_MAX_CH)
```

### 4.2 MATLAB/Simulink实现

**储能控制器**:
```matlab
function [p_ref, soc_out] = energy_storage_controller(...
    soc_in, p_agc, delta_f, mode, params)
    persistent soc
    if isempty(soc), soc = soc_in; end
    
    % SOC功率限幅
    if soc > params.soc_max_soft
        p_max_ch = params.p_rated * (params.soc_max - soc) / ...
                   (params.soc_max - params.soc_max_soft);
    else
        p_max_ch = params.p_rated;
    end
    
    if soc < params.soc_min_soft
        p_max_dis = params.p_rated * (soc - params.soc_min) / ...
                    (params.soc_min_soft - params.soc_min);
    else
        p_max_dis = params.p_rated;
    end
    
    % 根据模式计算功率
    switch mode
        case 'AGC'
            p_ref = p_agc;
        case 'Frequency'
            p_ref = -params.kf * delta_f;
        case 'PeakShaving'
            p_ref = calculate_peak_shave(load_profile);
        otherwise
            p_ref = 0;
    end
    
    % 功率限幅
    p_ref = max(min(p_ref, p_max_dis), -p_max_ch);
    
    % SOC更新
    if p_ref > 0  % 放电
        soc = soc - p_ref / params.eta_dis * params.dt / params.e_rated;
    else  % 充电
        soc = soc - p_ref * params.eta_ch * params.dt / params.e_rated;
    end
    soc = max(min(soc, params.soc_max), params.soc_min);
    soc_out = soc;
end
```

## 5. 典型参数参考

### 5.1 电网级储能参数

| 参数 | 户用 | 工商业 | 电网级 |
|------|------|--------|--------|
| 功率 | 5-20kW | 100kW-2MW | 10-100MW |
| 容量 | 10-50kWh | 200kWh-10MWh | 20-400MWh |
| 放电时长 | 2-4h | 2-6h | 2-4h |
| 响应时间 | <1s | <500ms | <100ms |
| 效率 | 85-92% | 88-94% | 90-95% |

### 5.2 SOC管理参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| SOC_min | 10-20% | 放电下限 |
| SOC_max | 80-95% | 充电上限 |
| SOC_safe | 15-90% | 正常运行区 |
| 充放电效率 | 90-95% | 往返效率85-90% |

### 5.3 调频参数

| 参数 | 一次调频 | 二次调频(AGC) |
|------|----------|---------------|
| 响应时间 | <2s | <1min |
| 调频系数 | 3-5% | 可调 |
| 功率范围 | ±100% | ±100% |
| 持续时间 | 15-30min | 持续 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[bess-model|电池储能系统]] - 电池侧建模
- [[gfl-inverter-model|跟网型变流器]] - 并网控制
- [[gfm-inverter-model|构网型变流器]] - 孤岛控制
- [[pi-controller-model|PI控制器]] - 功率环控制

### 6.2 相关方法
- [[droop-control-model|下垂控制]] - 功率均分
- [[numerical-integration|数值积分]] - SOC计算

### 6.3 相关主题
- 一次调频 - 频率支撑
- AGC调频 - 自动发电控制
- 削峰填谷 - 能量套利
- 黑启动 - 应急支撑

## 7. 适用边界与限制

### 7.1 适用条件
- **SOC范围**：10%-90%
- **功率范围**：额定功率
- **温度范围**：0-40°C（最佳）
- **循环寿命**：考虑老化降额

### 7.2 模型限制
- **电池老化**：未建模容量衰减
- **温度影响**：简化温度模型
- **多机协调**：SOC均衡未建模
- **保护逻辑**：简化故障保护

## 量化性能边界

**PCS 拓扑与效率**（Wang 2025、Lin 2023）：
- MMC-BESS 中 IDEM 模型在稳态、暂态和故障工况下仿真误差 < 1%（Wang 2025）
- 加速算法将多阀臂等效为三节点戴维南电路，单步长运算减少 50%-70%，仿真速度较 DSM 提升 10 倍以上（Wang 2025）
- CPU-GPU 异构架构在多 BESS 系统中实现加速比 > 200 倍（Lin 2023）
- 仿真步长 10-50 μs（EMT），多速率耦合降低计算冗余（Lin 2023）

**DC-DC 变换器谐振抑制**（Luo 2022）：
- Buck 模式下系统自然串联谐振频率理论值 118 Hz，阻抗模型误差 < 2.5%
- 支撑电容 > 0.5 mF 时在 100 Hz 以上呈无源电容特性
- 有源阻尼控制器增益须满足上限约束，否则在 50-100 Hz 产生负电阻区域

**构网型 PCS 黑启动**（Nguyen 2021）：
- 光储混合黑启动全过程 18 s（7 步），稳态电压误差 < 1%
- 母线电压恢复时间 < 0.2 s
- 最大负荷阶跃 120.2 MW + 42.3 Mvar，构网逆变器成功支撑

**FPGA 超实时 BESS 仿真**（Cao 2023）：
- FPGA 实现 51 倍超实时加速，步长达到亚微秒级

**数据缺口声明**：储能变流器在不同功率等级（kW 至 MW 级）和不同拓扑（单级式/两级式/MMC 嵌入式）下的效率-损耗建模数据缺乏系统公开对比。PCS 在不同电池类型（LFP/NCM/LTO）下的阻抗特性和控制参数整定缺乏统一基准。多 PCS 并联运行时 SOC 均衡控制策略的动态响应和稳态误差的定量数据不足。构网型 PCS 在弱电网（SCR < 2）下的暂态稳定边界缺乏系统验证。

## 相关方法
- [[numerical-integration|数值积分]] - SOC计算与离散控制
- [[state-space-method|状态空间法]] - 变流器状态分析
- [[average-value-model|平均值模型]] - 系统级简化
- [[droop-control-model|下垂控制模型]] - 一次调频功率控制

## 相关模型
- [[bess-model|电池储能系统]] - 电池侧详细模型
- [[gfl-inverter-model|跟网型变流器]] - 并网控制策略
- [[gfm-inverter-model|构网型变流器]] - 孤岛控制策略
- [[pi-controller-model|PI控制器]] - 功率环与电流环
- [[pll-model|锁相环]] - 并网同步

## 相关主题
- 频率调节 - 一次/二次调频
- 黑启动 - 应急支撑能力
- 微电网 - 并离网切换
- 削峰填谷 - 能量套利

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*

## 来源论文

| 论文 | 年份 |
|------|------|
| [[modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec|Modeling of a Modular Multilevel Converter With Embedded Ene]] | 2019 |
| [[average-value-model-for-a-modular-multilevel-converter-with-embedded-storage|Average-Value Model for a Modular Multilevel Converter With ]] | 2021 |
| [[electromechanical-transient-modelling-and-application-of-modular-multilevel-conv|Electromechanical transient modelling and application of mod]] | 2021 |
| [[active-damping-control-and-parameter-calculation-for-resonance-suppression-in-dc-distribution|Active Damping Control and Parameter Calculation for Resonan]] | 2022 |