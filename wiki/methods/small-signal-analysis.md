# 小信号分析方法 (Small-Signal Analysis)

## 定义与概述

小信号分析方法（Small-Signal Analysis）是电力系统稳定性研究的核心技术，通过在稳态运行点附近对非线性系统进行线性化，建立状态空间模型，进而分析系统在小扰动下的动态响应特性。该方法基于李雅普诺夫线性化理论，将复杂的非线性微分代数方程（DAE）转化为线性时不变（LTI）系统，利用特征值分析、参与因子、模态分析等工具，揭示系统振荡模式、阻尼特性、稳定性裕度以及关键影响因素。在新能源大规模接入、交直流混联电网背景下，小信号分析对于理解系统弱阻尼振荡、次同步振荡（SSO）、宽频振荡等问题具有不可替代的作用。

## 1. 理论基础

### 1.1 线性化原理

**非线性系统状态方程**：
$$\dot{x} = f(x, u)$$
$$y = g(x, u)$$

其中$x \in \mathbb{R}^n$为状态变量，$u \in \mathbb{R}^m$为输入，$y \in \mathbb{R}^p$为输出。

**稳态运行点**：
$$0 = f(x_0, u_0)$$
$$y_0 = g(x_0, u_0)$$

**泰勒展开线性化**：
$$\Delta \dot{x} = A\Delta x + B\Delta u$$
$$\Delta y = C\Delta x + D\Delta u$$

其中雅可比矩阵：
$$A = \left.\frac{\partial f}{\partial x}\right|_{(x_0,u_0)}, \quad B = \left.\frac{\partial f}{\partial u}\right|_{(x_0,u_0)}$$
$$C = \left.\frac{\partial g}{\partial x}\right|_{(x_0,u_0)}, \quad D = \left.\frac{\partial g}{\partial u}\right|_{(x_0,u_0)}$$

**小信号假设**：
$$\|x - x_0\| \ll 1, \quad \|u - u_0\| \ll 1$$

### 1.2 特征值分析

**特征值问题**：
$$A v_i = \lambda_i v_i$$
$$w_i^T A = \lambda_i w_i^T$$

其中：
- $\lambda_i = \sigma_i \pm j\omega_i$：第$i$个特征值
- $v_i$：右特征向量（模态形状）
- $w_i$：左特征向量

**稳定性判据**：
| 特征值位置 | 稳定性 | 物理意义 |
|------------|--------|----------|
| $\sigma_i < 0$ | 稳定 | 扰动衰减 |
| $\sigma_i > 0$ | 不稳定 | 扰动发散 |
| $\sigma_i = 0$ | 临界稳定 | 等幅振荡 |

**阻尼比**：
$$\zeta_i = \frac{-\sigma_i}{\sqrt{\sigma_i^2 + \omega_i^2}} = \cos(\theta_i)$$

| 阻尼比 | 稳定性等级 | 典型现象 |
|--------|------------|----------|
| $\zeta > 0.3$ | 良好 | 快速收敛 |
| $0.1 < \zeta < 0.3$ | 弱阻尼 | 缓慢衰减振荡 |
| $\zeta < 0.1$ | 极差 | 持续振荡 |
| $\zeta < 0$ | 负阻尼 | 振荡发散 |

**振荡频率**：
$$f_i = \frac{\omega_i}{2\pi}$$

**典型振荡模式**：
| 频率范围 | 模式类型 | 主要参与元件 |
|----------|----------|--------------|
| 0.1-2.0 Hz | 机电振荡 | 发电机转子 |
| 2-10 Hz | 控制模式 | 励磁/调速系统 |
| 10-50 Hz | 次同步振荡 | 串联补偿/换流器 |
| 50-500 Hz | 高频谐振 | 电力电子/电缆 |

### 1.3 参与因子分析

**参与因子定义**：
$$p_{ki} = w_{ki} \cdot v_{ik}$$

其中$w_{ki}$为左特征向量第$k$个元素，$v_{ik}$为右特征向量第$i$个元素。

**归一化参与因子**：
$$p_{ki}^{norm} = \frac{|p_{ki}|}{\sum_{j=1}^{n}|p_{ji}|} \times 100\%$$

**物理意义**：
- 状态变量$k$对模态$i$的参与程度
- 识别主导状态变量和关键元件

**参与因子应用**：
```
模态i分析：
1. 计算所有状态变量的p_ki
2. 排序找出最大参与因子
3. 识别主导元件（发电机/控制器/换流器）
4. 指导控制器参数整定
```

## 2. EMT仿真应用

### 2.1 换流器线性化建模

**LCC换流器线性化**（2026 贺永杰）：

换流器状态方程：
$$\dot{x}_{conv} = f_{conv}(x_{conv}, V_{ac}, I_{dc}, \alpha, \gamma)$$

线性化后39阶状态矩阵：
$$A_{sys} = \begin{bmatrix} A_{rect} & A_{couple} \\ A_{couple}^T & A_{inv} \end{bmatrix}$$

**改进动态相量模型**：
- 传统准稳态模型：换相线性近似，幅值误差~1%
- 改进正弦模型：考虑阀电流正弦变化，幅值误差<0.2%

**特征值分析结果**：
| 模态 | 频率(Hz) | 阻尼比 | 主导状态 | 物理意义 |
|------|----------|--------|----------|----------|
| 1 | 0.8 | 0.15 | $\Delta I_d$, $\Delta\alpha$ | 直流电流控制 |
| 2 | 5.2 | 0.08 | $\Delta\theta_{PLL}$ | PLL相位 |
| 3 | 12.5 | 0.05 | $\Delta V_{dc}$, $\Delta\gamma$ | 直流电压/关断角 |

### 2.2 VSC小信号稳定性

**VSC状态空间模型**：
$$\begin{bmatrix} \Delta \dot{i}_d \\ \Delta \dot{i}_q \end{bmatrix} = \begin{bmatrix} -R/L & \omega \\ -\omega & -R/L \end{bmatrix} \begin{bmatrix} \Delta i_d \\ \Delta i_q \end{bmatrix} + \begin{bmatrix} 1/L & 0 \\ 0 & 1/L \end{bmatrix} \begin{bmatrix} \Delta v_d \\ \Delta v_q \end{bmatrix}$$

**电流环PI控制线性化**：
$$\Delta v_d^{ref} = (K_p + \frac{K_i}{s})(\Delta i_d^{ref} - \Delta i_d) - \omega L \Delta i_q$$

**锁相环（PLL）线性化**：
$$\Delta \dot{\theta} = K_{p,PLL}\Delta v_q + K_{i,PLL}\int \Delta v_q dt$$

**弱电网稳定性问题**：
短路比（SCR）降低导致：
- 谐振频率降低
- 阻尼变弱
- 可能产生负阻尼

**临界SCR**：
| 控制策略 | 临界SCR | 稳定裕度 |
|----------|---------|----------|
| 电流控制 | 1.5-2.0 | 较小 |
| 电压控制 | 2.0-3.0 | 中等 |
| 虚拟同步机 | 1.0-1.5 | 较大 |

### 2.3 次同步振荡（SSO）分析

**SSO类型**：
| 类型 | 频率范围 | 机理 | 典型场景 |
|------|----------|------|----------|
| **IGE** | 10-50 Hz | 感应发电机效应 | 串补线路 |
| **TI** | 10-50 Hz | 转矩相互作用 | 多机系统 |
| **SSR** | 15-45 Hz | 扭转相互作用 | 汽轮机组 |
| **SSTI** | 10-100 Hz | 次同步控制相互作用 | HVDC/VSC |

**HVDC引起的SSO**（SSTI）：
- 换流器控制产生负阻尼
- 频率：10-50 Hz
- 影响：轴系疲劳、保护误动

**特征值分析**：
```
汽轮机组轴系模型：
- 多质块弹簧系统
- 6-8个扭转模态
- 第一模态~15 Hz
- 与电气系统耦合
```

### 2.4 风电场小信号分析

**DFIG小信号模型**：

电气状态：转子电流$i_{dr}, i_{qr}$，直流电压$V_{dc}$
机械状态：转速$\omega_r$，轴系角度$\delta$

**关键振荡模式**：
| 模态 | 频率 | 阻尼 | 影响因素 |
|------|------|------|----------|
| 转子电气 | 5-20 Hz | 中 | RSC控制参数 |
| 直流电压 | 1-5 Hz | 弱 | GSC控制/电容 |
| 转速控制 | 0.1-1 Hz | 强 | 转速环带宽 |
| 轴系扭转 | 1-3 Hz | 极弱 | 传动链柔性 |

**宽频振荡问题**：
- 频率：5-1000 Hz
- 机理：变流器控制+电网阻抗
- 影响因素：PLL带宽、电流环参数、电网强度

### 2.5 交直流混联系统

**多馈入系统特征**：
- 直流间相互作用
- 交直流耦合振荡
- 电压/功率交互影响

**多馈入短路比（MISCR）**：
$$\text{MISCR}_i = \frac{S_{ac,i}}{P_{dc,i} + \sum_{j \neq i} G_{ij}P_{dc,j}}$$

**稳定性判据**：
- MISCR > 3：强系统，稳定
- 2 < MISCR < 3：弱系统，需注意
- MISCR < 2：极弱系统，高风险

## 3. 实现技术

### 3.1 数值线性化方法

**解析线性化**：
- 手工推导雅可比矩阵
- 适用于简单系统
- 精度高，但工作量大

**数值微分线性化**：
```python
def numerical_linearization(f, x0, u0, dx=1e-6):
    n = len(x0)
    A = np.zeros((n, n))
    
    for j in range(n):
        x_plus = x0.copy()
        x_plus[j] += dx
        x_minus = x0.copy()
        x_minus[j] -= dx
        
        f_plus = f(x_plus, u0)
        f_minus = f(x_minus, u0)
        
        A[:, j] = (f_plus - f_minus) / (2*dx)
    
    return A
```

**自动微分线性化**（MATLAB/Simulink）：
```matlab
% 创建状态空间模型
sys = linearize('model_name', op_point);

% 提取A矩阵
A = sys.A;

% 特征值计算
eigenvalues = eig(A);
```

### 3.2 特征值计算算法

**QR算法**：
- 标准特征值算法
- 适合稠密矩阵
- 计算复杂度$O(n^3)$

**Arnoldi算法**（稀疏矩阵）：
- Krylov子空间方法
- 计算部分特征值（主导模态）
- 适合大规模系统

**选择算法**：
| 系统规模 | 矩阵类型 | 推荐算法 |
|----------|----------|----------|
| n < 100 | 稠密 | QR |
| 100 < n < 1000 | 稀疏 | Arnoldi |
| n > 1000 | 稀疏 | 块Arnoldi |

### 3.3 灵敏度分析

**特征值灵敏度**：
$$\frac{\partial \lambda_i}{\partial p} = w_i^T \frac{\partial A}{\partial p} v_i$$

**应用**：
- 识别关键参数
- 指导控制器设计
- 优化系统性能

**阻尼灵敏度**：
$$\frac{\partial \zeta_i}{\partial K_p} = \frac{\partial \zeta_i}{\partial \lambda_i} \cdot \frac{\partial \lambda_i}{\partial K_p}$$

用于PI参数整定。

## 4. 仿真软件实现

### 4.1 MATLAB/Simulink实现

**线性化工具箱**：
```matlab
% 定义操作点
op = operpoint('model_name');

% 线性化
sys = linearize('model_name', op);

% 提取状态空间
A = sys.A;
B = sys.B;
C = sys.C;
D = sys.D;

% 特征值分析
eig_val = eig(A);
damping = -real(eig_val) ./ abs(eig_val);
freq = imag(eig_val) / (2*pi);

% 参与因子计算
[V, D] = eig(A);
[W, ~] = eig(A');
for i = 1:length(eig_val)
    PF(:, i) = abs(W(:, i) .* V(:, i));
    PF(:, i) = PF(:, i) / sum(PF(:, i)) * 100;
end
```

**模态分析工具**：
```matlab
% 绘制根轨迹
pzmap(sys);

% 阻尼比-频率图
damp(sys);

% 模态参与因子图
bar(PF(:, mode_idx));
xlabel('State Variable');
ylabel('Participation Factor (%)');
```

### 4.2 PSD-BPA/小干扰稳定程序

**计算流程**：
```
1. 潮流计算（确定运行点）
2. 建立状态矩阵
3. 特征值计算
4. 阻尼比筛选
5. 参与因子分析
6. 灵敏度分析
7. 输出报告
```

**输出结果**：
- 弱阻尼振荡模式列表
- 参与因子排序
- 灵敏度矩阵
- 调整建议

### 4.3 与EMT仿真联合

**验证流程**：
```
1. 小信号分析预测不稳定模式
2. EMT仿真验证
   - 施加小扰动（1-5%）
   - 观察振荡响应
   - FFT分析频率
3. 对比分析
   - 频率误差<5%
   - 阻尼比误差<10%
```

**时域验证**：
```matlab
% EMT仿真结果
t = emt_results.time;
v = emt_results.voltage;

% Prony分析
[poles, residues] = prony(v, t, order);

% 提取模态参数
freq_emt = imag(poles) / (2*pi);
damp_emt = -real(poles) ./ abs(poles);
```

## 5. 典型参数参考

### 5.1 稳定性裕度指标

| 指标 | 计算公式 | 合格标准 | 优良标准 |
|------|----------|----------|----------|
| **阻尼比** | $\zeta$ | >0.03 | >0.05 |
| **振荡频率** | $f$ | - | 避开谐振 |
| **稳定裕度** | $\sigma$ | <0 | - |
| **参与因子** | $p$ | >10% | - |

### 5.2 控制器参数影响

| 控制器 | 参数 | 对低频模态 | 对高频模态 |
|--------|------|------------|------------|
| **励磁系统** | $K_A$ | 强影响 | 弱影响 |
| **PSS** | $K_{PSS}$ | 显著改善阻尼 | 基本无影响 |
| **电流环** | $K_{p,i}$ | 弱影响 | 显著影响频率 |
| **PLL** | $K_{p,PLL}$ | 影响稳定性 | 影响谐振 |

## 6. 相关主题与链接

### 6.1 相关方法
- [[state-space-method|状态空间法]] - 小信号建模基础
- [[state-space-method|状态空间法]] - 模态分析核心
- [[prony-analysis|Prony分析]] - 时域模态辨识
- 频域分析 - 频响分析

### 6.2 相关模型
- [[synchronous-machine-model|同步电机]] - 机电振荡主导
- [[vsc-model|VSC]] - 电力电子振荡
- [[pll-model|锁相环]] - 控制模式主导
- [[dfig-model|DFIG]] - 次同步振荡

### 6.3 相关主题
- 电压稳定分析 - 综合稳定性分析
- 振荡分析 - 宽频振荡
- [[wind-farm-modeling|风电场建模]] - 弱电网稳定性

## 7. 适用边界与限制

### 7.1 适用条件

**小信号分析有效场景**：
- 小扰动稳定性评估
- 控制器参数整定
- 振荡模式识别
- 稳定性裕度评估

**必须满足的条件**：
- 扰动足够小（<5%额定值）
- 系统可线性化
- 雅可比矩阵存在

### 7.2 失效边界

**不适用场景**：
- 大扰动暂态（故障/切机）
- 强非线性系统
- 开关动作瞬间
- 混沌/分岔现象

**线性化失效信号**：
- 雅可比矩阵奇异
- 特征值对参数极度敏感
- 时域响应非线性明显

### 7.3 精度边界

| 误差来源 | 典型误差 | 缓解方法 |
|----------|----------|----------|
| 线性化误差 | 5-10% | 高阶项补偿 |
| 数值误差 | 1-3% | 精细微分步长 |
| 模型误差 | 10-20% | 详细建模 |
| 参数误差 | 5-15% | 参数辨识 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Power System Stability and Control (Kundur) | 1994 | 小信号分析经典教材，特征值/参与因子理论 |
| 一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型 | 2026 | LCC线性化建模，39阶状态矩阵，改进正弦模型误差<0.2% |
| Small-signal stability analysis of VSC-HVDC | 2015 | VSC小信号建模，PLL稳定性，弱电网分析 |
| Subsynchronous oscillations in power systems | 2018 | SSO机理分析，HVDC引起的SSTI |
| DFIG small-signal modeling and stability | 2012 | 双馈风机小信号模型，轴系扭转分析 |

## 相关模型

- [[synchronous-machine-model|同步电机模型]] - 机电振荡分析的主导模型
- [[vsc-model|VSC模型]] - 电力电子振荡稳定性分析
- [[pll-model|锁相环模型]] - 控制模式振荡的关键元件
- [[dfig-model|DFIG模型]] - 次同步振荡分析对象
- [[mmc-model|MMC模型]] - 多电平换流器小信号建模

## 相关主题

- 电力系统稳定性 - 小信号稳定性的应用背景
- 振荡分析 - 宽频振荡机理研究
- [[wind-farm-modeling|风电场建模]] - 弱电网稳定性分析
- [[state-space-method|状态空间法]] - 小信号建模的数学基础

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*
