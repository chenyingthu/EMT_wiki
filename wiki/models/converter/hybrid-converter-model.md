---
title: "混合AC/DC变流器 (Hybrid AC/DC Converter)"
type: model
tags: [hybrid-converter, ac-dc, multiport, energy-router, solid-state-transformer, sst]
created: "2026-04-30"
updated: "2026-05-12"
---

# 混合AC/DC变流器 (Hybrid AC/DC Converter)


## 定义与概述

混合AC/DC变流器是新一代电力电子变压器和能量路由器的关键设备，能够同时处理交流（AC）和直流（DC）功率流，实现多端口能量管理、电压等级变换和电气隔离。在交直流混合配电网、数据中心、电动汽车充电站等场景中，混合变流器可显著提高系统效率和灵活性。本模型涵盖双有源桥（DAB）、级联H桥（CHB）、模块化多电平（MMC）混合拓扑，适用于交直流混合系统的EMT仿真。

## 1. 物理对象概述

### 1.1 功能与分类

**基本功能**：
- AC/DC双向功率变换
- 多端口能量路由
- 电压等级变换
- 电气隔离
- 功率因数校正

**混合变流器类型**:
| 类型 | 拓扑 | 功率等级 | 应用场景 |
|------|------|----------|----------|
| DAB型 | 双有源桥 | 100kW-10MW | 直流变压器 |
| CHB型 | 级联H桥 | 1-50MW | 中压直挂 |
| MMC型 | 模块化多电平 | 10MW-1GW | HVDC/柔直 |
| PET型 | 电力电子变压器 | 1-10MW | 配电网 |

### 1.2 端口结构

**三端口混合变流器**:
```
        HV AC (中高压交流)
            │
            ▼
    ┌───────────────┐
    │  AC/DC整流级  │
    │   (或逆变)    │
    └───────┬───────┘
            │ HV DC
            ▼
    ┌───────────────┐
    │   DC/DC隔离级  │
    │  (DAB或谐振)   │
    └───────┬───────┘
            │ LV DC
            ▼
    ┌───────────────┐
    │  DC/AC逆变级  │
    │              │
    └───────────────┘
            │
        LV AC (低压交流)
```

**多端口扩展**:
- AC端口：1个或多个
- DC端口：2个或多个电压等级
- 光伏/储能端口
- 电动汽车充电端口

### 1.3 运行激励

**功率流控制**：
- AC端口功率：$P_{AC}, Q_{AC}$
- DC端口功率：$P_{DC1}, P_{DC2}$
- 功率平衡：$\sum P_{in} = \sum P_{out} + P_{loss}$

**电压控制**：
- AC电压：幅值/频率
- DC电压：稳压或下垂

**工作模式**：
- AC整流模式
- AC逆变模式
- DC/DC变换模式
- 多端口功率路由

## 2. 物理模型与数学描述

### 2.1 双有源桥（DAB）

#### 2.1.1 基本拓扑

**全桥DAB**:
```
  V1     T1    L    T2     V2
──┬──   ┌──┐   │   ┌──┐   ──┬──
  │     │  │   │   │  │     │
──┴──   └──┘   │   └──┘   ──┴──
  n1:1        n2:1
```

**功率传输**:
$$P = \frac{n V_1 V_2}{2 f_s L} \cdot d \cdot (1-|d|)$$

其中：
- $d = \phi / \pi$ 为归一化移相角（$-1 \leq d \leq 1$）
- $f_s$：开关频率
- $L$：变压器漏感
- $n = n_2/n_1$：变比

**最优工作点**:
$$d_{opt} = 0.5 \Rightarrow P_{max} = \frac{n V_1 V_2}{8 f_s L}$$

#### 2.1.2 扩展拓扑

**双移相（DPS）**:
增加原副边内部移相，扩展ZVS范围。

**三移相（TPS）**:
原边、副边、原副边三个移相角，全范围ZVS。

### 2.2 级联H桥（CHB）

#### 2.2.1 单相CHB

**拓扑**:
```
Vdc ──→[H桥1]──[H桥2]──...──[H桥N]──→ Vac
        │       │          │
       C1      C2         CN
```

**输出电压**:
$$v_{ac} = \sum_{i=1}^{N} m_i \cdot v_{dc,i}$$

**电平数**:
- N个H桥：2N+1电平
- 三电平/五电平/七电平...

#### 2.2.2 三相CHB

**星形连接**:
- 每相N个H桥
- 三相独立控制
- 相间功率均衡

**三角形连接**:
- 线电压输出
- 相间耦合

### 2.3 电力电子变压器（PET）

#### 2.3.1 三级式PET

**输入级**：CHB整流
**隔离级**：DAB阵列
**输出级**：逆变器

**功率传输**:
$$P = \sum_{i=1}^{N} P_{DAB,i} = \sum_{i=1}^{N} \frac{n V_{dc,i} V_o}{2 f_s L} d_i (1-|d_i|)$$

#### 2.3.2 功率均衡控制

**相间功率均衡**:
$$d_a = d_0 + \Delta d_a$$
$$d_b = d_0 + \Delta d_b$$
$$d_c = d_0 + \Delta d_c$$

其中 $\Delta d$ 根据相间功率差调整。

## 3. EMT仿真模型

### 3.1 DAB离散化

**状态平均模型**:
$$\frac{d i_L}{dt} = \frac{v_1 - v_2/n}{L}$$

**离散化**:
$$i_L[k+1] = i_L[k] + \frac{T_s}{L}(v_1[k] - v_2[k]/n)$$

**功率计算**:
$$P[k] = v_1[k] \cdot i_{avg}[k]$$

### 3.2 CHB调制

**载波移相调制（CPS-PWM）**:
- 各H桥载波相位差：$360°/N$
- 等效开关频率：$N \cdot f_c$

**电压均衡控制**:
$$m_i = m_{ref} + \Delta m_i$$
$$\Delta m_i = K_{bal}(V_{ref} - V_{dc,i})$$

### 3.3 多端口功率管理

**功率分配**:
$$P_{AC} + P_{DC1} + P_{DC2} + P_{PV} + P_{ESS} = 0$$

**优先级控制**:
1. ESS充放电（根据SOC）
2. PV最大功率（MPPT）
3. AC/DC功率交换（根据需求）

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

**DAB控制**:
```fortran
! DAB移相控制
P_ERR = P_REF - P_MEAS
D_REF = KP_DAB * P_ERR + INTEGRAL_DAB
INTEGRAL_DAB = INTEGRAL_DAB + KI_DAB * DT * P_ERR

! 移相角限幅
D_REF = MAX(MIN(D_REF, D_MAX), -D_MAX)

! 产生PWM信号
PHI = D_REF * PI
PWM1 = SIGN(1.0, SIN(2*PI*FS*T))
PWM2 = SIGN(1.0, SIN(2*PI*FS*T + PHI))
```

**CHB电压均衡**:
```fortran
! 各模块电压均衡
DO I = 1, N
  V_ERR = V_REF - V_DC(I)
  DELTA_M(I) = K_BAL * V_ERR
  M(I) = M_REF + DELTA_M(I)
  
  ! 调制比限幅
  M(I) = MAX(MIN(M(I), 1.0), -1.0)
END DO
```

### 4.2 MATLAB/Simulink实现

**DAB模型**:
```matlab
function p = dab_model(v1, v2, d, params)
    % DAB功率传输方程
    n = params.n;
    fs = params.fs;
    L = params.L;
    
    % 功率传输
    p = n * v1 * v2 / (2 * fs * L) * d * (1 - abs(d));
end

function d = dab_controller(p_ref, p_meas, params)
    persistent integral
    if isempty(integral), integral = 0; end
    
    % PI控制
    e = p_ref - p_meas;
    d_unsat = params.Kp * e + integral;
    integral = integral + params.Ki * params.Ts * e;
    
    % 限幅
    d = max(min(d_unsat, params.d_max), -params.d_max);
end
```

**CHB调制**:
```matlab
function v_out = chb_modulation(v_dc, m, N)
    % CHB输出电压
    v_out = 0;
    for i = 1:N
        v_out = v_out + sign(m(i)) * v_dc(i);
    end
end
```

## 5. 典型参数参考

### 5.1 DAB参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 开关频率 | 10-50kHz | IGBT/SiC |
| 变压器变比 | 1:1 至 4:1 | 电压匹配 |
| 漏感 | 5-50μH | 功率传输 |
| 效率 | 96-99% | 全范围 |
| 功率密度 | 1-5kW/L | 体积功率 |

### 5.2 CHB参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| H桥数 | 5-20/相 | 电压等级 |
| 模块电压 | 800-1500V | DC电容 |
| 开关频率 | 0.5-2kHz | 模块频率 |
| 等效频率 | 5-40kHz | CPS-PWM |
| 效率 | 97-99% | 高压应用 |

### 5.3 PET参数

| 参数 | 配电级 | 输电级 |
|------|--------|--------|
| 功率 | 1-10MW | 10-100MW |
| 输入电压 | 10-35kV | 110-500kV |
| 输出电压 | 400V-1kV | 10-35kV |
| 效率 | 95-97% | 96-98% |
| 体积 | 1/10传统 | 1/5传统 |

## 6. 相关主题与链接

### 6.1 相关模型
- [[pet-sst-model|电力电子变压器]] - SST详细模型
- 双有源桥 - DAB变换器
- [[mmc-model|MMC模型]] - 高压应用
- [[vsc-model|VSC模型]] - AC/DC变换

### 6.2 相关方法
- [[average-value-model|平均值模型]] - DAB建模
- [[multirate-method|多速率方法]] - 不同开关频率

### 6.3 相关主题
- 能量路由器 - 多端口管理
- 交直流配电网 - 混合系统
- 固态变压器 - 未来电网

## 7. 适用边界与限制

### 7.1 适用条件
- **功率范围**：kW至GW级
- **电压等级**：低压至超高压
- **频率范围**：50/60Hz或DC
- **开关频率**：取决于器件

### 7.2 模型限制
- **损耗模型**：简化导通/开关损耗
- **热模型**：未考虑温度影响
- **保护逻辑**：简化过流保护
- **多机协调**：并联均流未建模

### 7.3 量化性能边界

混合 AC/DC 变流器 EMT 建模的精度取决于模型简化策略和拓扑类型。以下汇总可引用的量化数据：

**平均值模型精度**：Li (2025) 在固态变压器（SST）场景下验证了开关函数平均值模型，与详细开关模型相比误差小于 0.5%。Xu (2025) 对级联 H 桥 DAB 采用广义状态空间平均（GSSA）模型，在保留低频动态特性的同时显著降低计算复杂度。

**多速率仿真加速**：Wang (2025) 采用多速率方法对 CHB-DAB 进行 EMT 仿真，整体加速比达 10-20 倍，精度损失在可接受范围内。Gao (2022) 基于 Kron 消去法对电力电子变压器进行模型降阶，加速 10-100 倍。Li (2026) 采用 ImEx-Gear 混合积分方法实现 PET 仿真加速达 171 倍。

**实时仿真实现**：Qi (2024) 在实时仿真器中实现了双有源桥（DAB）的聚合模型，结合插值前推（IFP）方法，实现 FPGA 上的亚微秒级步长实时仿真。Berger (2018) 采用 GSSA 对 DAB 进行建模验证，证明平均值方法在保留关键动态特性的前提下可实现显著加速。

**数据缺口声明**：混合 AC/DC 变流器的 EMT 建模精度评估高度依赖具体拓扑（DAB、CHB、MMC、PET）和控制策略。不同建模方法（开关函数平均值、GSSA、多速率）在同一测试基准下的对比数据不足。建议用户根据具体应用场景选择合适的模型保真度。

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
