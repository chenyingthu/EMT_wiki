---
title: "灵敏度分析 (Sensitivity Analysis)"
type: method
tags: [sensitivity, analysis, parameter, stability, optimization, eigenvalue, participation-factor]
created: "2026-05-02"
---

# 灵敏度分析 (Sensitivity Analysis)

## 概述

灵敏度分析(Sensitivity Analysis)是研究系统输出或性能指标对参数变化的敏感程度的系统方法，在电力系统分析中广泛应用于参数优化、控制器设计、稳定性评估和规划决策。通过定量分析参数微小变化对系统行为的影响，灵敏度分析为系统优化和决策提供了重要的理论基础。

在电力系统领域，灵敏度分析涵盖特征值灵敏度、潮流灵敏度、电压灵敏度、稳定裕度灵敏度等多个方面，是电力系统规划、运行和控制中不可或缺的分析工具。

## 基本理论

### 灵敏度定义

**数学定义**:
对于系统 $y = f(x, p)$，输出 $y$ 对参数 $p$ 的灵敏度为：
$$S_p^y = \frac{\partial y}{\partial p}$$

**归一化灵敏度**:
无量纲形式便于比较：
$$\tilde{S}_p^y = \frac{p}{y}\frac{\partial y}{\partial p} = \frac{\partial y/y}{\partial p/p}$$
表示参数变化1%引起的输出变化百分比。

**多参数灵敏度**:
对于多参数系统，灵敏度为梯度向量：
$$\nabla_p y = \left[\frac{\partial y}{\partial p_1}, \frac{\partial y}{\partial p_2}, ..., \frac{\partial y}{\partial p_m}\right]^T$$

### 特征值灵敏度

**特征值问题**:
线性化系统的状态矩阵 $A$ 满足：
$$A u_i = \lambda_i u_i, \quad v_i^T A = \lambda_i v_i^T$$
其中 $\lambda_i$ 为特征值，$u_i$、$v_i$ 分别为右、左特征向量。

**特征值灵敏度公式**:
特征值对参数 $p$ 的灵敏度：
$$\frac{\partial \lambda_i}{\partial p} = \frac{v_i^T \frac{\partial A}{\partial p} u_i}{v_i^T u_i}$$

**特征向量灵敏度**:
$$\frac{\partial u_i}{\partial p} = \sum_{j \neq i} \frac{v_j^T \frac{\partial A}{\partial p} u_i}{(\lambda_i - \lambda_j)v_j^T u_j} u_j$$

### 参与因子

**定义**:
$$P_{ki} = |v_{ki} u_{ik}|$$
表示状态变量 $k$ 对模式 $i$ 的参与程度。

**归一化**:
$$p_{ki} = \frac{P_{ki}}{\sum_k P_{ki}}$$

**物理意义**:
- 大 $p_{ki}$: 状态 $k$ 强烈参与模式 $i$
- 用于识别振荡模式的主导变量
- 辅助控制器选址

## 灵敏度类型

### 静态灵敏度

**潮流灵敏度**:
功率方程线性化：
$$\begin{bmatrix} \Delta P \\ \Delta Q \end{bmatrix} = \begin{bmatrix} J_{P\theta} & J_{PV} \\ J_{Q\theta} & J_{QV} \end{bmatrix} \begin{bmatrix} \Delta \theta \\ \Delta V \end{bmatrix}$$

电压对无功灵敏度：
$$\frac{\partial V}{\partial Q} = J_{QV}^{-1}$$

**损耗灵敏度**:
网损对发电机出力的灵敏度：
$$\frac{\partial P_{loss}}{\partial P_{Gi}} = \sum_{k} 2P_k \frac{\partial P_k}{\partial P_{Gi}}$$
用于经济调度优化。

### 动态灵敏度

**特征值实部灵敏度**:
$$\frac{\partial \sigma_i}{\partial p} = Re\left(\frac{\partial \lambda_i}{\partial p}\right)$$
反映阻尼对参数的敏感程度。

**特征值虚部灵敏度**:
$$\frac{\partial \omega_i}{\partial p} = Im\left(\frac{\partial \lambda_i}{\partial p}\right)$$
反映频率对参数的敏感程度。

**稳定裕度灵敏度**:
临界切除时间(CCT)灵敏度：
$$\frac{\partial t_{crit}}{\partial p} = \lim_{\Delta p \to 0} \frac{t_{crit}(p+\Delta p) - t_{crit}(p)}{\Delta p}$$

### 电压灵敏度

**PV曲线灵敏度**:
鼻点处的电压对负荷灵敏度：
$$\frac{\partial V_{nose}}{\partial P_L} = -\infty$$
表示电压崩溃的临界性。

**Q-V灵敏度**:
$$S_{QV} = \frac{\partial Q}{\partial V}$$
用于电压稳定评估：
- $S_{QV} > 0$: 稳定
- $S_{QV} = 0$: 临界点
- $S_{QV} < 0$: 不稳定

**模态分析**:
降阶雅可比矩阵的特征值分析：
$$J_R = -J_{QV} + J_{Q\theta}J_{P\theta}^{-1}J_{PV}$$
最小特征值对应电压崩溃模式。

## 计算方法

### 解析法

**直接求导法**:
对于显式函数 $y = f(p)$，直接解析求导。

**伴随网络法**:
引入伴随变量：
$$\lambda^T = \frac{\partial y}{\partial x}$$
灵敏度：
$$\frac{dy}{dp} = \frac{\partial y}{\partial p} + \lambda^T \frac{\partial f}{\partial p}$$

**隐函数微分**:
对于 $F(x, p) = 0$：
$$\frac{\partial F}{\partial x}\frac{dx}{dp} + \frac{\partial F}{\partial p} = 0$$
$$\frac{dx}{dp} = -\left(\frac{\partial F}{\partial x}\right)^{-1}\frac{\partial F}{\partial p}$$

### 数值法

**有限差分法**:
前向差分：
$$\frac{dy}{dp} \approx \frac{y(p+\Delta p) - y(p)}{\Delta p}$$

中心差分(更高精度)：
$$\frac{dy}{dp} \approx \frac{y(p+\Delta p) - y(p-\Delta p)}{2\Delta p}$$

**扰动法**:
小扰动分析：
$$\frac{dy}{dp} = \lim_{\Delta p \to 0} \frac{\Delta y}{\Delta p}$$

**步长选择**:
- 太小：数值误差大
- 太大：截断误差大
- 最优：$\Delta p \approx \sqrt{\varepsilon_{mach}} \cdot p$

### 蒙特卡洛法

**统计灵敏度**:
参数随机采样，分析输出统计特性：
$$\sigma_y^2 \approx \sum_i \left(\frac{\partial y}{\partial p_i}\right)^2 \sigma_{p_i}^2$$

**全局灵敏度**:
Sobol指数：
$$S_i = \frac{Var_{p_i}(E_{p_{-i}}[y|p_i])}{Var(y)}$$
衡量参数 $p_i$ 对输出方差的贡献。

## 电力系统应用

### 控制器设计

**PSS参数优化**:
特征值对PSS增益灵敏度：
$$\frac{\partial \lambda}{\partial K_{PSS}} = v^T \frac{\partial A}{\partial K_{PSS}} u$$
用于阻尼优化。

**FACTS选址定容**:
- 电压灵敏度确定最佳安装位置
- 稳定灵敏度确定最佳容量
- 多目标优化考虑经济性和技术性

**HVDC附加控制**:
阻尼对直流功率调制的灵敏度指导控制器设计。

### 稳定评估

**暂态稳定灵敏度**:
CCT对参数灵敏度：
$$\frac{\partial t_c}{\partial p} > 0 \Rightarrow \text{增加}p\text{提高稳定性}$$

**小扰动稳定灵敏度**:
阻尼比灵敏度：
$$\frac{\partial \xi}{\partial p} = \frac{\partial}{\partial p}\left(-\frac{\sigma}{\sqrt{\sigma^2+\omega^2}}\right)$$

**电压稳定灵敏度**:
负荷裕度灵敏度：
$$\frac{\partial MW_{margin}}{\partial Q_{shunt}}$$
指导无功补偿配置。

### 规划分析

**线路投资灵敏度**:
网损减少值对新建线路的灵敏度：
$$\frac{\partial P_{loss}}{\partial x_{line}}$$
评估线路投资效益。

**发电机选址**:
电压支撑灵敏度：
$$\frac{\partial V}{\partial Q_G}$$
确定最佳发电位置。

**可靠性灵敏度**:
系统可靠性指标对元件参数的灵敏度，识别薄弱环节。

### 运行优化

**经济调度**:
边际成本灵敏度：
$$\frac{\partial C_{total}}{\partial P_{Gi}} = \lambda$$

**安全约束调度**:
稳定裕度对发电出力的灵敏度约束：
$$\frac{\partial Margin}{\partial P_G} \Delta P_G \geq \Delta Margin_{req}$$

**预防控制**:
基于灵敏度计算控制量：
$$\Delta u = S^+ \Delta y_{desired}$$
其中 $S^+$ 为灵敏度矩阵的伪逆。

## 灵敏度矩阵计算

### 状态空间形式

**线性系统**:
$$\dot{x} = Ax + Bu$$
$$y = Cx + Du$$

**输出对参数灵敏度**:
$$\frac{\partial y}{\partial p} = C\frac{\partial x}{\partial p} + \frac{\partial C}{\partial p}x$$

**状态灵敏度方程**:
$$\frac{d}{dt}\left(\frac{\partial x}{\partial p}\right) = A\frac{\partial x}{\partial p} + \frac{\partial A}{\partial p}x$$

### 伴随系统法

**伴随方程**:
$$\dot{\lambda} = -A^T\lambda - C^T$$
反向积分求解。

**灵敏度计算**:
$$\frac{\partial y}{\partial p} = \int_0^T \lambda^T \frac{\partial A}{\partial p} x dt$$

**优势**:
- 单次计算得到对所有参数的灵敏度
- 适合多参数系统
- 计算效率高

### 稀疏技术

**稀疏矩阵处理**:
利用电力系统矩阵稀疏性，高效计算：
$$\frac{\partial x}{\partial p} = -J^{-1}\frac{\partial F}{\partial p}$$

**稀疏向量法**:
仅计算感兴趣的灵敏度，避免完整矩阵求逆。

## 特殊灵敏度分析

### 结构保留灵敏度

**结构保留模型**:
保留网络结构的模型：
$$M\ddot{\delta} + D\dot{\delta} + f(\delta) = 0$$

**灵敏度特点**:
- 考虑网络拓扑影响
- 负荷模型详细
- 计算复杂度高

### 概率灵敏度

**随机灵敏度**:
考虑参数不确定性：
$$E\left[\frac{\partial y}{\partial p}\right], \quad Var\left(\frac{\partial y}{\partial p}\right)$$

**场景分析**:
多场景下灵敏度统计特性。

### 时变灵敏度

**轨迹灵敏度**:
时变系统灵敏度：
$$\frac{\partial x(t)}{\partial p} = \int_0^t \Phi(t, \tau) \frac{\partial f}{\partial p} d\tau$$
其中 $\Phi$ 为状态转移矩阵。

## 工具与实现

### 商业软件

**PSS/E**:
- 特征值分析模块
- 参与因子计算
- 灵敏度分析工具

**PowerFactory**:
- 模态分析
- 灵敏度计算
- 优化模块集成

**MATLAB**:
- Control System Toolbox
- 特征值计算
- 灵敏度函数

### 编程实现

**Python示例**:
```python
import numpy as np
from scipy.linalg import eig

# 计算特征值灵敏度
def eigenvalue_sensitivity(A, dA_dp, u, v):
    lam = v.T @ A @ u / (v.T @ u)
    dlam_dp = (v.T @ dA_dp @ u) / (v.T @ u)
    return lam, dlam_dp
```

**稀疏矩阵优化**:
利用scipy.sparse处理大规模系统。

## 局限性与注意事项

### 线性化局限

**适用范围**:
- 小扰动假设
- 非线性系统需分段线性化
- 大扰动后灵敏度变化

**准确性**:
灵敏度仅在工作点附近有效，远离线性化点误差增大。

### 计算挑战

**计算量**:
- 多参数系统计算量大
- 需要多次重复求解
- 大规模系统存储需求

**数值问题**:
- 重特征值问题
- 病态矩阵
- 数值稳定性

### 应用限制

**灵敏度悖论**:
高灵敏度参数往往难以控制，低灵敏度参数易于控制但效果有限。

**多目标冲突**:
不同目标函数的灵敏度可能冲突，需要折衷。

## 相关方法

- [[modal-analysis]] - 模态分析: 基于特征值的系统动态特性分析
- [[eigenvalue-analysis]] - 特征值分析: 系统稳定性特征值计算
- [[emt-model-boundary-determination-using-floquet-theory-based-participation-factor]] - 参与因子: 状态变量与振荡模式的关联
- [[numerical-damping-optimization]] - 优化方法: 基于灵敏度的系统优化
- [[small-signal-stability]] - 小扰动稳定: 灵敏度分析主要应用场景

## 来源论文

参见 [[index.md]] 获取更多灵敏度分析相关文献。
