---
title: "能量函数法 (Energy Function Method)"
type: method
tags: [energy-function, direct-method, stability, lyapunov, transient, direct-analysis]
created: "2026-05-02"
---

# 能量函数法 (Energy Function Method)

## 概述

能量函数法(Energy Function Method)是电力系统暂态稳定性分析的直接法(Direct Method)之一，由Aylett于1958年首次提出，后经许多学者发展完善。该方法通过构造系统的李雅普诺夫函数(能量函数)来直接判断系统的稳定性，无需进行时域仿真计算整个摇摆曲线，能够显著提高暂态稳定性分析的效率，特别适合在线安全评估和大量故障场景的筛选。

能量函数法的基本思想是将电力系统类比为力学系统，系统的总能量由动能和势能组成。当故障后的系统总能量小于临界能量时，系统是稳定的；反之则不稳定。这种方法避免了逐次积分求解微分方程，计算速度快，但结果可能偏于保守。

## 基本原理

### 能量函数构造

**保守系统能量**:
对于经典模型的多机系统，总能量函数为：
$$W(\delta, \omega) = W_k(\omega) + W_p(\delta)$$
其中 $W_k$ 为动能，$W_p$ 为势能。

**动能**:
$$W_k = \frac{1}{2} \sum_{i=1}^{n} M_i \omega_i^2$$
$M_i$ 为发电机惯性常数，$\omega_i$ 为转速偏差。

**势能**:
$$W_p = -\sum_{i=1}^{n} P_{mi}(\delta_i - \delta_i^s) - \sum_{i<j} V_i V_j B_{ij}(\cos\delta_{ij} - \cos\delta_{ij}^s)$$
其中：
- $P_{mi}$: 机械功率
- $\delta_i^s$: 稳态功角
- $V_i, V_j$: 节点电压
- $B_{ij}$: 节点导纳虚部
- $\delta_{ij} = \delta_i - \delta_j$: 功角差

**能量变化率**:
$$\frac{dW}{dt} = \sum_{i=1}^{n} (P_{mi} - P_{ei}) \omega_i - D_i \omega_i^2$$
对于无损系统，$\frac{dW}{dt} = 0$，能量守恒。

### 稳定判据

**基本判据**:
故障切除时刻的系统能量：
$$W_{cl} = W(\delta_{cl}, \omega_{cl})$$

临界能量：
$$W_{cr} = W(\delta_{u}, 0)$$
$\delta_u$ 为不稳定平衡点(UEP)功角。

**稳定性条件**:
$$W_{cl} < W_{cr} \Rightarrow \text{稳定}$$
$$W_{cl} > W_{cr} \Rightarrow \text{不稳定}$$

**稳定裕度**:
$$\Delta W = W_{cr} - W_{cl}$$
$$\eta = \frac{\Delta W}{W_{cl}} \times 100\%$$

### 不稳定平衡点(UEP)

**定义**:
系统动态方程的平衡点：
$$\dot{\delta} = 0, \quad \dot{\omega} = 0$$

**类型**:
- 稳定平衡点(SEP): $\delta_s$，系统稳态运行点
- 不稳定平衡点(UEP): $\delta_u$，势能鞍点

**UEP求解**:
$$P_{mi} = P_{ei} = \sum_{j=1}^{n} V_i V_j B_{ij} \sin\delta_{ij}$$

**最近UEP**:
与故障后轨迹最接近的UEP决定临界能量。

## 能量函数类型

### 经典模型能量函数

**两机系统**:
$$W = \frac{1}{2} M_{eq} \omega^2 - P_m (\delta - \delta_s) - P_{max}(\cos\delta - \cos\delta_s)$$
其中等效惯性：
$$M_{eq} = \frac{M_1 M_2}{M_1 + M_2}$$

**多机系统**:
以COI(惯性中心)为参考：
$$\delta_{COI} = \frac{\sum M_i \delta_i}{\sum M_i}, \quad \omega_{COI} = \frac{\sum M_i \omega_i}{\sum M_i}$$

相对变量：
$$\tilde{\delta}_i = \delta_i - \delta_{COI}, \quad \tilde{\omega}_i = \omega_i - \omega_{COI}$$

### 结构保留模型

**保留网络结构**:
考虑负荷母线和传输网络：
$$W_p = W_p^{gen} + W_p^{load} + W_p^{network}$$

**负荷模型**:
考虑电压相关负荷：
$$P_L = P_{L0} \left(\frac{V}{V_0}\right)^{\alpha}, \quad Q_L = Q_{L0} \left(\frac{V}{V_0}\right)^{\beta}$$

**势能分量**:
- 发电机势能
- 负荷势能
- 传输线储能

### 复杂模型能量函数

**考虑励磁系统**:
$$W = W_{mech} + W_{field}$$
其中励磁能量：
$$W_{field} = \frac{1}{2} L_{fd} i_{fd}^2$$

**考虑调速系统**:
增加原动机-调速器能量项。

**考虑PSS**:
增加阻尼能量项。

## 临界能量计算

### 最近UEP方法

**方法步骤**:
1. 求解所有UEP
2. 计算每个UEP的势能
3. 最近UEP为势能最小者
4. $W_{cr} = W_p(\delta_{closest})$

**局限性**:
可能过于保守，实际轨迹未必到达最近UEP。

### 相关UEP方法

**主导UEP**:
与故障类型相关的UEP：
$$\delta_{controlling} = f(\text{fault location, type})$$

**确定方法**:
- 故障后持续故障轨迹法
- 模式分析
- 经验法则

### 势能边界表面(PEBS)方法

**基本思想**:
在势能表面上寻找最小势能路径。

**算法**:
1. 从SEP出发，沿梯度方向搜索
2. 找到势能极大值点
3. 该点即为临界状态

**势能梯度**:
$$\nabla W_p = \frac{\partial W_p}{\partial \delta}$$

**优势**:
避免求解所有UEP，计算效率高。

### BCU方法

**边界控制法(Boundary of stability region based Controlling Unstable equilibrium point)**:
结合时域仿真和能量函数。

**步骤**:
1. 短时域仿真(3-5周期)
2. 确定主导模式
3. 找到相关UEP
4. 计算临界能量

**特点**:
- 速度快
- 精度高
- 适合在线应用

## 扩展方法

### 扩展等面积准则(EEAC)

**基本思想**:
将多机系统等效为单机无穷大系统：
$$M_{eq} \frac{d^2\delta_{eq}}{dt^2} = P_{m,eq} - P_{e,eq}$$

**等面积准则**:
加速面积 = 减速面积：
$$\int_{\delta_0}^{\delta_c} (P_m - P_e^{fault}) d\delta = \int_{\delta_c}^{\delta_{max}} (P_e^{post} - P_m) d\delta$$

**稳定裕度**:
$$\eta = \frac{A_{decel} - A_{accel}}{A_{accel}}$$

### SIME方法

**单机等效(Single Machine Equivalent)**:
动态识别主导机群。

**步骤**:
1. 时域仿真识别失稳机群
2. 将系统分为临界机群和剩余机群
3. 等效为两机系统
4. 应用等面积准则

**优势**:
- 可处理首摆和多摆稳定
- 适合复杂故障
- 精度高

### 混合方法

**时域仿真+能量函数**:
- 短时域仿真获取初始轨迹
- 能量函数评估稳定性
- 结合两者优势

**逐步积分**:
在关键时段小步长积分，其他时段大步长。

## 电力系统应用

### 暂态稳定评估

**快速筛选**:
大量故障场景快速筛选：
- 稳定故障: 快速通过
- 临界故障: 详细分析
- 不稳定故障: 立即识别

**在线应用**:
- 安全评估
- 预警系统
- 预防控制

### 临界切除时间计算

**迭代法**:
1. 假设CCT
2. 计算切除时刻能量
3. 与临界能量比较
4. 调整CCT

**直接计算**:
$$CCT = f^{-1}(W_{cr})$$
其中 $f$ 为故障期间能量增长函数。

### 稳定裕度分析

**裕度排序**:
按 $\Delta W$ 排序故障严重性：
$$Ranking: \Delta W_1 > \Delta W_2 > ... > \Delta W_n$$

**灵敏度分析**:
裕度对参数的灵敏度：
$$\frac{\partial \eta}{\partial p} = \frac{\partial}{\partial p}\left(\frac{W_{cr} - W_{cl}}{W_{cl}}\right)$$

### 安全约束调度

**优化模型**:
$$\min C(P_G)$$
$$s.t. \quad W_{cl}(P_G) \leq W_{cr} - \Delta W_{margin}$$

**预防控制**:
调整发电出力提高稳定裕度。

## 局限性与改进

### 主要局限

**模型简化**:
- 经典模型假设
- 忽略阻尼
- 恒定电压

**保守性**:
- 结果偏于保守
- 稳定裕度估计偏小
- 可能误判临界情况

**多摆稳定**:
- 主要适用于首摆稳定
- 多摆问题分析困难
- 摇摆失稳难以识别

**复杂故障**:
- 复杂故障序列
- 多重故障
- 保护动作协调

### 改进方向

**模型改进**:
- 详细发电机模型
- 考虑负荷特性
- 网络结构保留

**方法改进**:
- 混合方法
- 自适应方法
- 机器学习方法

**应用扩展**:
- 电压稳定
- 频率稳定
- 小扰动稳定

## 工具与实现

### 商业软件

**TSAT**:
- 暂态稳定分析工具
- 直接法实现
- EEAC方法

**PowerFactory**:
- 能量函数模块
- 稳定裕度计算
- 在线应用

**Siemens PTI**:
- PSS/E直接法模块
- 大规模系统支持

### 编程实现

**MATLAB实现**:
```matlab
% 计算能量函数
function W = energy_function(delta, omega, M, Pm, V, B, delta_s)
    % 动能
    Wk = 0.5 * sum(M .* omega.^2);
    
    % 势能
    n = length(delta);
    Wp = 0;
    for i = 1:n
        Wp = Wp - Pm(i) * (delta(i) - delta_s(i));
        for j = i+1:n
            Wp = Wp - V(i)*V(j)*B(i,j)*(cos(delta(i)-delta(j)) - cos(delta_s(i)-delta_s(j)));
        end
    end
    
    W = Wk + Wp;
end
```

**Python实现**:
利用NumPy/SciPy实现能量函数计算。

## 验证与测试

### 简单系统测试

**单机无穷大**:
$$W = \frac{1}{2}M\omega^2 - P_m(\delta - \delta_s) - P_{max}(\cos\delta - \cos\delta_s)$$
与等面积准则对比验证。

**两机系统**:
解析验证能量守恒。

### 实际系统测试

**与详细仿真对比**:
以时域仿真结果为基准：
- 稳定/不稳定判断一致性
- CCT计算误差
- 裕度估计准确性

**统计评估**:
大量故障场景的准确率：
$$Accuracy = \frac{N_{correct}}{N_{total}} \times 100\%$$

### IEEE测试系统

**IEEE 9机系统**:
标准测试验证方法有效性。

**IEEE 39机系统**:
中等规模系统验证。

**大规模系统**:
100机以上系统应用测试。

## 相关方法

- [[transient-stability-analysis]] - 暂态稳定性分析: 一般暂态稳定分析方法
- [[equal-area-criterion]] - 等面积准则: 单机系统稳定判据
- `direct-method` - 直接法: 不通过时域仿真的稳定分析方法
- `lyapunov-stability` - 李雅普诺夫稳定性: 能量函数理论基础
- [[eeac]] - 扩展等面积准则: 多机等效方法
- [[time-domain-simulation]] - 时域仿真: 与直接法对比的仿真方法

## 来源论文

参见 [[index.md]] 获取更多能量函数法相关文献。
