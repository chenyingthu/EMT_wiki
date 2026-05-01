# 参数辨识方法 (Parameter Identification)

## 定义与概述

参数辨识方法（Parameter Identification）是电力系统电磁暂态（EMT）仿真中从测量数据或仿真结果中提取模型参数的技术集合。与基于物理结构和材料属性的理论计算方法不同，参数辨识通过反演算法从可观测的电气量（电压、电流、功率等）中估计设备或网络的等效参数。在EMT领域，参数辨识广泛应用于变压器饱和特性提取、输电线路参数反演、频率相关网络等值（FDNE）建模、保护装置定值优化等场景，是解决"黑箱"设备建模、现场模型校准和宽频特性提取的核心技术手段。

## 1. 理论基础

### 1.1 辨识问题数学表述

**一般参数辨识模型**：
$$y(t) = f(u(t), \theta) + \epsilon(t)$$

其中：
- $y(t)$：系统输出（观测值）
- $u(t)$：系统输入（激励信号）
- $\theta$：待辨识参数向量
- $\epsilon(t)$：测量噪声

**优化目标**：
$$\min_\theta J(\theta) = \sum_{k=1}^{N} \|y_{meas}(t_k) - y_{sim}(t_k, \theta)\|^2$$

**最小二乘解**：
$$\hat{\theta} = (\Phi^T \Phi)^{-1} \Phi^T Y$$

其中$\Phi$为回归矩阵，$Y$为观测向量。

### 1.2 频域参数辨识

**传输线参数反演**：
基于单端开路/短路阻抗测量：
$$Z_{open} = Z_c \coth(\gamma l)$$
$$Z_{short} = Z_c \tanh(\gamma l)$$

**传播常数求解**：
$$\gamma = \frac{1}{l} \ln\left(\frac{1 + \sqrt{Z_{short}/Z_{open}}}{1 - \sqrt{Z_{short}/Z_{open}}}\right)$$

**单位长度参数重构**：
$$z = \gamma Z_c, \quad y = \frac{\gamma}{Z_c}$$

### 1.3 时域参数辨识

**变压器饱和曲线辨识**：
磁链-电流关系：
$$\psi(t) = \psi_R + \int V_{mag}(t) dt$$

其中铁芯电压：
$$V_{mag}(t) = V_{HV}(t) - L_{HV}\frac{dI}{dt} - R_{HV}I(t)$$

**饱和段拟合**：
对$\psi > \psi_{sat}$区域进行线性回归：
$$L_{sat} = \frac{\Delta \psi}{\Delta I_{mag}}$$

### 1.4 矢量拟合参数辨识

**FDNE有理函数拟合**：
$$Y(s) = \sum_{i=1}^{n} \frac{c_i}{s - a_i} + d + sh$$

**状态空间实现**：
$$Y(s) = C(sE - A)^{-1}B + D$$

**参数辨识流程**：
| 步骤 | 操作 | 输出 |
|------|------|------|
| 1 | 频率响应采样 | $Y(s_k), k=1,...,N$ |
| 2 | 极点初始定位 | 初始极点$a_i$ |
| 3 | 线性最小二乘 | 留数$c_i$、常数$d,h$ |
| 4 | 极点重定位 | 更新$a_i$ |
| 5 | 迭代收敛 | 最优参数集 |

## 2. EMT仿真应用

### 2.1 变压器饱和特性辨识

**现场投切暂态法**（2021 Canal）：

**原理**：利用变压器合闸暂态中至少一相未饱和的特性，从三相线电流中分离励磁电流。

**算法步骤**：
1. 采集投切暂态三相电压、电流（采样率≥5kHz）
2. 从线电流中扣除三角形绕组环流：$I_{mag,i} = J_i - I_{\delta}$
3. 计算励磁支路电压：$V_{mag} = V_{HV} - L_{HV}\frac{dJ}{dt} - R_{HV}J$
4. 积分得磁链：$\psi(t) = -\int V_{mag}(t)dt + C$
5. 用出厂空载试验校准积分常数$C$
6. 对$\psi > \psi_{sat}$区域线性拟合得饱和电感

**统计处理**：
$$\bar{L}_{sat} \pm k\sigma\sqrt{1 + \frac{1}{n}}$$

**典型结果**：
| 参数 | 辨识值 | 厂家估算 | 误差修正 |
|------|--------|----------|----------|
| 饱和电感 | 0.833 H | 0.959 H | 高估15.1% |
| 95%置信区间 | ±6.3% | ±20% | 精度提升3倍 |

**工程意义**：饱和电感每高估10%，过电压约束低估约30%。

### 2.2 直流励磁现场测量法

**便携式直流测量**（2023 Velásquez）：

**核心思想**：用直流/低频激励代替高压交流试验，降低现场测试难度。

**技术优势对比**：
| 方法 | 测试电压 | 设备要求 | 测量时间 |
|------|----------|----------|----------|
| 传统交流法 | 1.2-1.4 p.u. (~504kV) | 高压大功率电源 | 数小时 |
| 直流励磁法 | 50-100 V | 便携式直流电阻测试仪 | ~5分钟 |

**测量流程**：
1. 施加正向直流电压，实时计算绕组电阻（1Hz）
2. 监测电阻变化率判断饱和状态
3. 自动极性反转捕获磁滞回线
4. T型等效电路分离铁芯电压
5. 积分计算磁链，建立$\psi-I$曲线

### 2.3 输电线路参数反演

**单端频域测量法**（2005 Kurokawa）：

**适用场景**：非均匀线路（弧垂、非平行导体、频变土壤电导率）

**突破点**：无需Carson/Pollaczek公式的均匀大地假设

**验证结果**：
- 频率范围：10 Hz ~ 10 kHz
- 与传统方法误差：<0.5%
- 波形畸变率降低：60%~80%

**限制条件**：需满足$\text{Im}(\gamma)l < \pi/2$以避免反双曲函数多值性

### 2.4 距离保护频域参数辨识

**故障距离估计**（2012 Griffiths）：

**问题转化**：将故障距离、过渡电阻、对侧等值参数作为未知量

**线性方程构建**：
$$sU_{mA}(s) = V(s)x_1 + I_{m0}(s)x_2 + sI_{m0}(s)x_3$$

**参数映射**：
$$p = x_1, \quad R_F = f(x_2, x_3), \quad L_{n0} = g(x_2, x_3)$$

**矩阵束算法**：提取暂态中基频与直流分量，避免DFT频谱泄漏

**性能对比**：
| 场景 | 传统阻抗法 | 微分方程法 | 本文算法 |
|------|------------|------------|----------|
| 50km远端故障 | -15.58% | -27.32% | +0.02% |
| 超越风险 | 高 | 极高 | 无 |

### 2.5 FDNE宽频等值参数辨识

**混合仿真接口建模**（2014 胡一中）：

**频域采样**：在1-2.5kHz范围获取边界导纳频率特性

**矢量拟合实现**：
```
步骤：
1. 简化网络获取导纳采样值
2. Vector Fitting求解极点、留数
3. 无源性校正（摄动留数矩阵特征根）
4. 状态空间离散化：I(t) = I_his + G_eq U(t)
5. RTDS用户自定义模型实现
```

**拟合精度**：
- 极点-留数模型阶数：n=10-20
- 频率范围：1-2500 Hz
- 幅值误差：<1%
- 相位误差：<5°

## 3. 实现技术

### 3.1 数值优化方法

**最小二乘算法**：
```python
def linear_least_squares(phi, y):
    """线性最小二乘参数估计"""
    theta = np.linalg.inv(phi.T @ phi) @ phi.T @ y
    return theta
```

**加权最小二乘**：
$$\hat{\theta} = (\Phi^T W \Phi)^{-1} \Phi^T W Y$$

**递推最小二乘**（在线辨识）：
$$K_k = P_{k-1}\phi_k(1 + \phi_k^T P_{k-1}\phi_k)^{-1}$$
$$\hat{\theta}_k = \hat{\theta}_{k-1} + K_k(y_k - \phi_k^T\hat{\theta}_{k-1})$$
$$P_k = (I - K_k\phi_k^T)P_{k-1}$$

### 3.2 频域辨识算法

**矩阵束算法**（Matrix Pencil）：
构建Hankel矩阵：
$$Y = \begin{bmatrix} y(0) & y(1) & \cdots & y(L) \\ y(1) & y(2) & \cdots & y(L+1) \\ \vdots & \vdots & \ddots & \vdots \\ y(N-L) & y(N-L+1) & \cdots & y(N) \end{bmatrix}$$

SVD分解提取信号子空间，求解极点与留数。

**Prony分析**：
$$y(k) = \sum_{m=1}^{M} R_m z_m^k$$

用于暂态信号模态参数提取。

### 3.3 数据预处理

**滤波处理**：
- 低通滤波：消除高频噪声
-  notch滤波：消除工频干扰

**积分漂移校正**：
$$\psi(t) = \int_0^t V(\tau)d\tau - \frac{t}{T}\int_0^T V(\tau)d\tau$$

**归一化处理**：
$$x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}$$

## 4. 仿真软件实现

### 4.1 MATLAB实现

**变压器饱和曲线辨识**：
```matlab
% 磁链积分
psi = cumtrapz(t, V_mag);

% 去漂移
psi = psi - mean(psi);

% 饱和段拟合
idx_sat = psi > psi_sat;
p = polyfit(I_mag(idx_sat), psi(idx_sat), 1);
L_sat = p(1);
```

**矢量拟合参数辨识**：
```matlab
% 使用Vector Fitting工具箱
[poles, residues, d, h] = vectfit3(Y, s, init_poles);

% 状态空间转换
[A,B,C,D] = ss_from_pr(poles, residues, d, h);
```

### 4.2 Python实现

**传输线参数反演**：
```python
import numpy as np

def line_parameter_inversion(Z_open, Z_short, l):
    """基于开短路阻抗反演线路参数"""
    X = np.sqrt(Z_short / Z_open)
    gamma = np.log((1 + X) / (1 - X)) / l
    Zc = np.sqrt(Z_open * Z_short)
    z = gamma * Zc
    y = gamma / Zc
    return z, y
```

**最小二乘拟合**：
```python
def ls_fit(phi, y, weights=None):
    if weights is None:
        theta = np.linalg.lstsq(phi, y, rcond=None)[0]
    else:
        W = np.diag(weights)
        theta = np.linalg.inv(phi.T @ W @ phi) @ phi.T @ W @ y
    return theta
```

### 4.3 EMTP/PSCAD实现

**FDNE参数辨识流程**：
```fortran
! 频率响应计算
DO f = f_min, f_max, df
    CALL calc_admittance(Y(f), network, f)
END DO

! 矢量拟合
CALL vector_fitting(Y, poles, residues, d, h, order)

! 无源性检查
CALL passivity_check(poles, residues, d, h, is_passive)
IF (.NOT. is_passive) THEN
    CALL passivity_enforcement(poles, residues, d, h)
END IF
```

## 5. 典型参数参考

### 5.1 辨识精度指标

| 应用场景 | 参数类型 | 典型精度 | 置信水平 |
|----------|----------|----------|----------|
| 变压器饱和电感 | 电感值 | ±5-10% | 95% |
| 输电线路参数 | R,L,C | <0.5% | 全频段 |
| FDNE有理拟合 | Y(s) | <1% | 1-2.5kHz |
| 故障距离估计 | 距离 | <1% | 线性方程 |
| 磁滞回线 | $\psi-I$ | 1-3% | 波形对比 |

### 5.2 采样要求

| 辨识对象 | 采样率 | 数据窗长 | 窗函数 |
|----------|--------|----------|--------|
| 变压器饱和 | ≥5kHz | 1-2个周波 | 矩形 |
| 线路参数 | 频域扫描 | 全频段 | - |
| 暂态信号 | ≥10kHz | 10-20ms | Hanning |
| 磁滞回线 | 1Hz | 完整循环 | - |

### 5.3 算法选择指南

| 问题类型 | 推荐算法 | 理由 |
|----------|----------|------|
| 线性参数 | 最小二乘 | 解析解，计算快 |
| 非线性参数 | Levenberg-Marquardt | 收敛性好 |
| 暂态模态 | 矩阵束/Prony | 频率分辨率高 |
| 频域拟合 | 矢量拟合 | 稳定，精度高 |
| 在线辨识 | 递推最小二乘 | 实时更新 |

## 6. 相关主题与链接

### 6.1 相关方法
- [[vector-fitting|矢量拟合]] - FDNE参数辨识核心算法
- [[prony-analysis|Prony分析]] - 暂态信号模态参数提取
- [[frequency-dependent-modeling|频率相关建模]] - 频域参数辨识基础
- [[state-space-method|状态空间法]] - FDNE状态空间实现

### 6.2 相关模型
- [[transformer-model|变压器模型]] - 饱和特性建模
- [[transmission-line-model|输电线路模型]] - 线路参数建模
- [[fdne-model|FDNE模型]] - 宽频网络等值
- [[circuit-breaker-model|断路器模型]] - 电弧参数辨识

### 6.3 相关主题
- [[network-equivalent|网络等值]] - 参数辨识应用背景
- [[real-time-simulation|实时仿真]] - 在线参数辨识
- 现场测试 - 参数辨识数据来源
- 模型验证 - 辨识结果校核

## 7. 适用边界与限制

### 7.1 适用条件

**参数辨识有效场景**：
- 有可观测的输入输出数据
- 模型结构已知或可选择
- 参数可辨识（观测矩阵满秩）
- 信噪比足够高

**数据质量要求**：
- 采样率满足奈奎斯特准则
- 激励信号充分激励所有模态
- 数据长度覆盖主要动态过程

### 7.2 失效边界

**不适用场景**：
- 模型结构未知且无法假设
- 观测数据严重缺失
- 参数不可辨识（共线性）
- 强非线性系统（需分段线性化）

**数值问题**：
- 条件数过大导致病态
- 局部极小值（非凸优化）
- 积分漂移（时域积分）

### 7.3 精度边界

| 误差来源 | 典型误差 | 缓解方法 |
|----------|----------|----------|
| 测量噪声 | 1-5% | 滤波、加权最小二乘 |
| 模型误差 | 5-15% | 模型结构选择、残差分析 |
| 数值误差 | 0.1-1% | 双精度、正则化 |
| 截断误差 | 1-3% | 增加拟合阶数 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| Determination of saturation curve from transient measurements | 2021 | 变压器饱和曲线现场辨识，投切暂态利用 |
| On-site measurement of hysteresis curve using DC excitation | 2023 | 直流励磁法现场测量磁滞曲线 |
| New procedure to derive transmission-line parameters | 2005 | 单端频域测量反演线路参数 |
| Distance protection based on parameter identification | 2012 | 频域参数辨识用于故障测距 |
| RTDS-TSA hybrid simulation with FDNE | 2014 | FDNE宽频等值参数辨识与实现 |
| Wideband CVT model using scattering parameters | 2024 | 散射参数辨识用于CVT宽频建模 |

## 相关模型

- [[transformer-model|变压器模型]] - 饱和特性参数辨识的核心对象
- [[transmission-line-model|输电线路模型]] - 线路参数频域辨识
- [[fdne-model|FDNE模型]] - 宽频网络等值参数辨识
- [[circuit-breaker-model|断路器模型]] - 电弧参数辨识应用
- [[cable-model|电缆模型]] - 电缆参数现场辨识

## 相关主题

- [[network-equivalent|网络等值]] - 参数辨识在网络等值中的应用背景
- [[real-time-simulation|实时仿真]] - 在线参数辨识技术
- 现场测试 - 参数辨识数据来源与方法
- 模型验证 - 辨识结果校核与验证

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*
