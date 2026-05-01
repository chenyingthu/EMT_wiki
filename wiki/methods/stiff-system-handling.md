# 刚性系统处理 (Stiff System Handling)

## 定义与概述

刚性系统（Stiff System）是指同时包含多个时间尺度差异极大的动态过程的微分方程系统。在电力系统EMT仿真中，刚性表现为：电力电子开关暂态（ns-μs级）、电磁暂态（μs-ms级）、机电暂态（ms-s级）共存于同一系统。刚性比（Stiffness Ratio）可达$10^6$甚至更高，导致显式积分方法需要极小步长才能保持稳定，计算效率极低。刚性系统处理技术通过隐式积分、自动变步长、混合积分等策略，在保证稳定性的同时最大化仿真步长，是含电力电子设备电网仿真的核心技术挑战。

## 1. 理论基础

### 1.1 刚性系统的数学定义

**测试方程**:
$$\dot{x} = \lambda x, \quad \text{Re}(\lambda) < 0$$

**刚性比定义**:
$$S = \frac{\max|\text{Re}(\lambda_i)|}{\min|\text{Re}(\lambda_i)|}$$

| 刚性等级 | 刚性比范围 | 典型场景 |
|----------|-----------|----------|
| 非刚性 | $S < 10$ | 纯交流网络 |
| 中等刚性 | $10 \leq S < 10^3$ | 含FACTS的交流系统 |
| 强刚性 | $10^3 \leq S < 10^6$ | HVDC换流站 |
| 极强刚性 | $S \geq 10^6$ | MMC子模块+控制系统 |

### 1.2 电力系统刚性来源

**多时间尺度耦合**:
```
时间尺度层级：
├── 电力电子开关：ns-μs (10^-9-10^-6 s)
├── 电磁暂态：μs-ms (10^-6-10^-3 s)
├── 控制动态：ms-10ms (10^-3-10^-2 s)
├── 转子动态：10ms-s (10^-2-10^0 s)
└── 慢变过程：s-min (10^0-10^2 s)
```

**典型刚性场景**:
| 场景 | 快动态 | 慢动态 | 刚性比 |
|------|--------|--------|--------|
| MMC换流器 | 子模块电容充放电 (μs) | 外环功率控制 (ms) | $10^3-10^4$ |
| HVDC换相 | 换流阀关断 (μs) | 直流线路放电 (ms) | $10^2-10^3$ |
| DFIG风机 | 变流器电流环 (ms) | 机械转速 (s) | $10^2-10^3$ |
| 系统故障 | 故障电流上升 (μs) | 保护动作 (ms) | $10^2-10^4$ |

### 1.3 显式方法的局限性

**稳定性约束**:
对于前向欧拉法，稳定条件要求：
$$|1 + h\lambda| < 1 \Rightarrow h < \frac{2}{|\lambda_{\max}|}$$

**步长限制示例**:
- 系统特征值：$\lambda_{\max} = 10^6$ (对应1μs时间常数)
- 显式方法最大步长：$h < 2\mu$s
- 仿真10ms暂态需要>5,000步

**效率问题**: 为满足稳定性，步长远小于精度需求，导致"过采样"。

### 1.4 隐式方法的优势

**后向欧拉（BE）稳定区域**:
$$rac{x_{n+1} - x_n}{h} = f(x_{n+1}) \Rightarrow x_{n+1} = \frac{x_n}{1 - h\lambda}$$

稳定性条件：$|1 - h\lambda| > 1$，对所有$\text{Re}(\lambda) < 0$均成立。

**A稳定性**: 方法在整个左半平面稳定，步长不受快动态限制。

**L稳定性**: 对$\lambda \to -\infty$，$x_{n+1} \to 0$，完全抑制高频分量。

| 方法 | A稳定 | L稳定 | 精度阶数 |
|------|-------|-------|---------|
| 前向欧拉 | ✗ | ✗ | 1阶 |
| 后向欧拉 | ✓ | ✓ | 1阶 |
| 梯形法 | ✓ | ✗ | 2阶 |
| 2S-DIRK | ✓ | 可调 | 2阶 |
| Gear法 | ✓ | ✓ | 2-6阶 |

## 2. EMT仿真应用

### 2.1 刚性问题的识别

**数值振荡特征**:
- 梯形法在非连续点（开关动作、故障）后产生高频振荡
- 振荡频率：$\omega \approx 2/\Delta t$
- 振荡不衰减（梯形法非L稳定）

**刚性诊断指标**:
| 指标 | 计算公式 | 临界值 |
|------|----------|--------|
| 刚性比 | $S = |\lambda_{\max}|/|\lambda_{\min}|$ | >100 |
| 雅可比条件数 | $\kappa(J) = \sigma_{\max}/\sigma_{\min}$ | >1e6 |
| 局部截断误差比 | $\text{LTE}_{\text{fast}}/\text{LTE}_{\text{slow}}$ | >10 |

### 2.2 临界阻尼调整（CDA）

**问题**: 梯形法在开关事件后产生数值振荡。

**解决方案**: 在间断点后使用后向欧拉法两步。

**算法流程**:
```
正常仿真：梯形法 → 梯形法 → 梯形法
            ↓
开关事件：检测到不连续
            ↓
事件后：  后向欧拉 → 后向欧拉 → 梯形法
```

**效果**: 完全消除数值振荡，保持2阶精度（仅局部降阶）。

**实现细节**:
- 第一步（BE）：$x_{n+1} = x_n + h \cdot f(x_{n+1})$
- 第二步（BE）：$x_{n+2} = x_{n+1} + h \cdot f(x_{n+2})$
- 后续（TR）：$x_{n+3} = x_{n+2} + \frac{h}{2}[f_{n+2} + f_{n+3}]$

### 2.3 Gear多步法

**一般形式**:
$$\sum_{j=0}^{k} \alpha_j x_{n+j} = h \beta_k f(x_{n+k})$$

**阶数选择**:
| 阶数 | 稳定性 | 适用场景 |
|------|--------|----------|
| 1阶 | L稳定 | 强刚性，允许低精度 |
| 2阶 | A稳定 | 中等刚性，平衡精度稳定性 |
| 3阶 | 刚性稳定 | 弱刚性，高精度需求 |
| 4-6阶 | 刚性稳定 | 平滑动态，高精度 |

**变阶变步长策略**:
- 误差大/刚性增强 → 降阶+减小步长
- 误差小/刚性减弱 → 升阶+增大步长

### 2.4 混合积分策略

**多速率分区**:
将刚性系统按时间尺度分区：

```
┌──────────────────────────────────────┐
│  慢变子系统（大时间步长）              │
│  方法：梯形法/Gear法（高阶）           │
│  步长：h_slow = 10·h_fast             │
├──────────────────────────────────────┤
│  快变子系统（小时间步长）              │
│  方法：后向欧拉/2S-DIRK（L稳定）       │
│  步长：h_fast                         │
└──────────────────────────────────────┘
```

**插值接口**:
慢变系统输出插值到快变系统时间步：
$$u_{fast}(t) = u_{slow}(t_n) + \frac{t - t_n}{h_{slow}}(u_{slow}(t_{n+1}) - u_{slow}(t_n))$$

### 2.5 DIRK方法应用

**2S-DIRK（两阶段对角隐式龙格-库塔）**:

阶段1：
$$x_{n+\gamma} = x_n + \gamma h f(x_{n+\gamma})$$

阶段2：
$$x_{n+1} = x_n + (1-\gamma)h f(x_{n+\gamma}) + \gamma h f(x_{n+1})$$

其中$\gamma = 1 - \frac{\sqrt{2}}{2} \approx 0.293$确保L稳定。

**优势**: 每个阶段只需一次LU分解（对角结构），计算效率高于完全隐式方法。

## 3. 实现技术

### 3.1 自动变步长控制

**误差估计**:
$$\text{LTE} = \|x_{n+1}^{(p)} - x_{n+1}^{(p+1)}\|$$

或使用嵌入式方法：
$$\text{LTE} = \|x_{n+1} - \hat{x}_{n+1}\|$$

**步长调整**:
$$h_{new} = h_{old} \cdot \left(\frac{\epsilon}{\text{LTE}}\right)^{1/(p+1)}$$

其中$p$为方法阶数，$\epsilon$为容差。

**刚性检测**:
当连续多步需要减小步长<10%时，判定系统进入刚性区域，切换至隐式方法。

### 3.2 牛顿迭代求解

**隐式方程**:
$$x_{n+1} = x_n + h \beta f(x_{n+1})$$

**牛顿迭代**:
$$J^{(k)} \Delta x^{(k)} = -F(x^{(k)})$$

其中：
- $F(x) = x - x_n - h\beta f(x) = 0$
- $J = I - h\beta \frac{\partial f}{\partial x}$（雅可比矩阵）

**简化牛顿法**:
固定雅可比矩阵（仅每步或数步更新一次）：
$$J_0 \Delta x^{(k)} = -F(x^{(k)})$$

减少LU分解次数，适用于弱非线性系统。

### 3.3 预处理技术

**雅可比矩阵预处理**:
对于大规模系统，求解$J \Delta x = -F$代价高昂。

**不完全LU预处理（ILU）**:
$$M = \tilde{L}\tilde{U} \approx J$$

预处理后的系统：
$$M^{-1}J \Delta x = -M^{-1}F$$

条件数改善，迭代收敛加速。

### 3.4 电力电子特殊处理

**开关事件检测**:
```python
def detect_switching(v_threshold, i_threshold):
    """检测开关事件并触发处理方法"""
    for switch in switches:
        if switch.voltage > v_threshold or switch.current > i_threshold:
            # 1. 插值找到精确开关时刻
            t_exact = interpolate_crossing(t_prev, t_now)
            
            # 2. 回退到上一时刻
            rollback_state(t_prev)
            
            # 3. 使用小步长到精确时刻
            step(t_exact - t_prev, method='BE')
            
            # 4. 切换开关状态
            switch.toggle()
            
            # 5. 执行临界阻尼调整
            step(h, method='BE')  # 第一步BE
            step(h, method='BE')  # 第二步BE
            
            # 6. 恢复正常积分
            step(h, method='TR')  # 后续梯形法
```

## 4. 仿真软件实现

### 4.1 EMTP-RV实现

```fortran
! EMTP刚性处理核心
SUBROUTINE STIFF_SOLVER(X, T, H, TOL, METHOD)
    REAL X(*), T, H, TOL
    INTEGER METHOD
    
    ! 刚性检测
    IF (METHOD .EQ. AUTO) THEN
        STIFFNESS = ESTIMATE_STIFFNESS(X, JACOBIAN)
        IF (STIFFNESS > STIFF_THRESHOLD) THEN
            METHOD = GEAR
            ORDER = 2
        ELSE
            METHOD = TRAPEZOIDAL
        ENDIF
    ENDIF
    
    ! 变步长控制
    ERROR = ESTIMATE_ERROR(X, X_PREV, METHOD)
    IF (ERROR > TOL) THEN
        H = 0.5 * H  ! 减小步长重算
        RETURN
    ELSEIF (ERROR < 0.1*TOL) THEN
        H = MIN(2.0*H, H_MAX)  ! 增大步长
    ENDIF
    
    ! 积分步推进
    SELECT CASE(METHOD)
        CASE(TRAPEZOIDAL)
            CALL TRAPEZOIDAL_STEP(X, T, H)
        CASE(BACKWARD_EULER)
            CALL BE_STEP(X, T, H)
        CASE(GEAR)
            CALL GEAR_STEP(X, T, H, ORDER)
        CASE(DIRK)
            CALL DIRK_STEP(X, T, H)
    END SELECT
END SUBROUTINE
```

### 4.2 PSCAD实现

**CDA自动触发**:
- 检测开关状态变化
- 自动在事件后插入两步BE
- 无需用户干预

**多方法选择**:
- 标准模式：梯形法（默认）
- 刚性模式：2S-DIRK（可配置）
- 自动模式：根据刚性检测切换

### 4.3 MATLAB/Simulink实现

```matlab
% ode15s：专为刚性系统设计的变阶变步长求解器
options = odeset('RelTol', 1e-4, 'AbsTol', 1e-6, ...
                 'MaxStep', 1e-4, ...
                 'Jacobian', @jacobian_func, ...
                 'BDF', 'on');  % 启用Gear方法

[t, y] = ode15s(@power_system_model, [0 0.1], y0, options);
```

**ode23tb**：TR-BDF2组合方法
- 第一阶段：梯形法（TR）
- 第二阶段：2阶后向微分公式（BDF2）
- 兼具精度与稳定性

## 5. 典型参数参考

| 场景 | 刚性比 | 推荐方法 | 典型步长 | 注意事项 |
|------|--------|----------|----------|----------|
| 纯交流网络 | <10 | 梯形法 | 50-100μs | 标准设置 |
| HVDC换流站 | 10^2-10^3 | 梯形+CDA | 20-50μs | 开关处自动切换BE |
| MMC详细模型 | 10^3-10^4 | 2S-DIRK/Gear | 10-20μs | 高阶方法可能不稳定 |
| 系统级故障 | 10^2-10^4 | 变步长BE | 自适应 | 故障时步长自动减小 |
| 实时仿真 | 不定 | 固定步长BE | 固定50μs | 牺牲精度保实时性 |

## 6. 相关主题与链接

### 6.1 相关方法
- [[numerical-integration|数值积分]] - 刚性处理的基础方法
- [[multirate-method|多速率方法]] - 分区处理不同时间尺度
- [[fixed-admittance|恒导纳模型]] - 避免开关引起的刚性突变
- [[sparse-matrix-solver|稀疏矩阵求解]] - 隐式方法的线性方程求解
- [[fpga-real-time-simulation|FPGA实时仿真]] - 固定步长刚性处理

### 6.2 相关模型
- [[mmc-model|MMC模型]] - 强刚性系统典型代表
- [[vsc-model|VSC模型]] - 高频开关引入刚性
- [[dfig-model|DFIG模型]] - 机电-电磁多时间尺度

### 6.3 相关主题
- [[real-time-simulation|实时仿真]] - 实时约束下的刚性处理
- 数值稳定性 - 刚性处理的理论基础
- [[switching-function|开关函数法]] - 减少刚性影响的建模方法

## 7. 适用边界与限制

### 7.1 适用条件
- **多时间尺度系统**: 刚性比>100，快动态和慢动态共存
- **数值振荡**: 梯形法产生持续高频振荡
- **稳定性需求**: 大步长下仍需保持稳定
- **精度平衡**: 允许局部降阶以换取稳定性

### 7.2 失效边界
- **极强刚性**: $S > 10^8$时，即使是隐式方法也需极小步长
- **高度非线性**: 雅可比矩阵变化剧烈，简化牛顿法失效
- **不连续频繁**: 开关频率过高（>10kHz），CDA切换开销大
- **实时约束**: 隐式迭代无法满足固定步长要求

### 7.3 精度边界
| 方法 | 稳态误差 | 暂态误差 | 数值阻尼 |
|------|---------|---------|----------|
| 梯形法 | $O(h^2)$ | $O(h^2)$ | 无（振荡） |
| 后向欧拉 | $O(h)$ | $O(h)$ | 强 |
| Gear(2阶) | $O(h^2)$ | $O(h^2)$ | 中等 |
| 2S-DIRK | $O(h^2)$ | $O(h^2)$ | 可调 |

**权衡**: 高阶方法精度高但稳定性差；L稳定方法无振荡但引入数值阻尼。

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Numerical integration methods for stiff ODEs in power systems | 1994 | 电力系统刚性ODE数值积分方法综述 |
| A multirate EMT co-simulation of large AC and MMC-based MTDC | 2020 | 多速率协同仿真处理MMC刚性 |
| 基于矩阵对角化的电磁暂态时间并行计算方法 | 2023 | 刚性系统时间并行算法 |
| 计及电容过渡过程的双钳位型MMC电磁暂态高效仿真 | 2022 | MMC刚性处理与高效仿真 |
| Gear, C.W.: Numerical Initial Value Problems in ODE | 1971 | Gear方法原始文献，刚性系统经典算法 |
| Alexander, R.: Diagonally Implicit Runge-Kutta Methods | 1977 | DIRK方法原始文献 |

## 相关模型

- [[mmc-model|MMC模型]] - 强刚性系统典型代表，含多时间尺度动态
- [[vsc-model|VSC模型]] - 高频开关引入刚性
- [[dfig-model|DFIG模型]] - 机电-电磁多时间尺度系统
- [[lcc-model|LCC模型]] - 晶闸管换流器刚性特性
- [[igbt-model|IGBT模型]] - 高频开关器件刚性处理

## 相关主题

- [[real-time-simulation|实时仿真]] - 实时约束下的刚性处理方法
- 刚性系统处理 - 数值稳定性理论基础
- [[switching-function|开关函数法]] - 减少刚性影响的建模方法
- 电力电子 - 刚性系统的主要来源

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*
