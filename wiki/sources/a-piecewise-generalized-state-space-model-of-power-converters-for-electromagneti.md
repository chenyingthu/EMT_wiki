---
title: "A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien"
type: source
year: 2022
journal: ""
created: "2026-04-13"
sources: ["EMT_Doc/03/Wang 等 - 2019 - A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien.pdf"]
---

# A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien

**年份**: 2022
**来源**: `03/Wang 等 - 2019 - A Piecewise Generalized State Space Model of Power Converters for Electromagnetic Transient Efficien.pdf`

## 摘要

Common averaging methods were studied for modeling the grid-connected converter in new energy domain to balance the accuracy and efficiency in electromagnetic transient simulation. A piecewise generalized state space averaging (P-GSSA) method was proposed for converters with the large-scale new energy connected to grid. The piecewise technique was applied to generalized state space averaging (GSSA) model of the converters in this method, which combines the time slot with similar operating characteristic together to study. And multi time scale modeling was successfully achieved in the grid-connected converter of new energy domain. An example was simulated according to the P-GSSA model proposed in this paper, and the simulation results show that the model can adapt to the efficient simulatio

## 核心贡献


- 提出分段广义状态空间平均法，融合分段技术与广义状态空间平均模型
- 设计基于幅值预测的分段策略，合并动作特性一致的开关周期实现变步长
- 构建多时间尺度变流器模型，有效兼顾电磁暂态仿真精度与计算效率


## 使用的方法


- [[广义状态空间平均法|广义状态空间平均法]]
- [[分段状态空间平均法|分段状态空间平均法]]
- [[傅里叶级数展开|傅里叶级数展开]]
- [[变步长建模|变步长建模]]
- [[多时间尺度建模|多时间尺度建模]]


## 涉及的模型


- [[并网变流器|并网变流器]]
- [[三相pwm逆变器|三相PWM逆变器]]
- [[光伏系统|光伏系统]]
- [[变流器开关详细模型|变流器开关详细模型]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[新能源并网|新能源并网]]
- [[变流器建模|变流器建模]]
- [[高效仿真|高效仿真]]
- [[谐波分析|谐波分析]]


## 主要发现


- 分段模型能精确反映变流器电磁暂态特性，有效计及高频分量与谐波影响
- 仿真验证表明该模型在保持高精度的同时显著提升计算效率，优于传统平均法
- 自适应分段策略成功实现多时间尺度仿真，适用于大规模新能源并网场景



## 方法细节

### 方法概述

分段广义状态空间平均法（P-GSSA）是一种面向电磁暂态高效仿真的变流器建模方法。该方法将分段技术与广义状态空间平均法有机结合，核心思想是根据开关函数占空比的方差阈值，将动作特性一致（具有“近周期性”）的多个开关周期合并为一个时间分段，实现变步长与多时间尺度建模。在每个分段区间内，对状态变量进行傅里叶级数展开，保留低阶系数以重构电气量，从而精确计及高频分量与谐波影响。该方法通过动态调整分段长度（稳态2~3个周期，暂态1个周期）和傅里叶展开阶数，在保证微秒级电磁暂态仿真精度的同时，显著降低微分方程求解次数，有效平衡了大规模新能源并网变流器仿真的精度与计算效率。

### 数学公式


**公式1**: $$$$S_i = \begin{cases} 1, & v_m > v_c \\ 0, & v_m \le v_c \end{cases}$$$$

*PWM开关函数定义，通过比较调制波与载波确定各相开关状态*


**公式2**: $$$$d_i = \frac{1}{T_s} \int_{t-T_s}^{t} S_i(\tau) d\tau$$$$

*周期性开关函数占空比计算，用于表征单个开关周期内的平均导通比例*


**公式3**: $$$$\frac{d}{dt} x_k(t) = f(x(t), u(t))_k(t) - jk\omega x_k(t)$$$$

*广义状态空间平均法核心方程，利用傅里叶微分性质建立频域状态微分方程*


**公式4**: $$$$\dot{y}(t) = \sum_{q=-\infty}^{\infty} \left[ A_0 y(t)_q + b_0 + \sum_{i=1}^{m} (A_i y(t)_q + b_i) D_i(t) \right]$$$$

*分段广义状态空间平均模型最终状态方程，在分段区间内联合求解各阶傅里叶系数*


**公式5**: $$$$\sigma = \max \frac{|x_P - x_D|}{x_D}$$$$

*模型相对误差计算公式，用于对比P-GSSA模型与详细开关模型的偏差*


### 算法步骤

1. 初始化仿真参数：设定总仿真时长T、占空比方差限值ε1、状态变量误差限值ε2及最大傅里叶阶数q_max（通常≤10）。

2. 计算开关动作时刻：根据正弦调制波vm与三角载波vc的实时比较，确定各相开关函数Si的导通时刻tp与关断时刻tf。

3. 动态分段判定：从当前时刻起，连续计算r个开关周期的占空比方差σr。若σr < ε1，判定为具有“近周期性”，将r个周期合并为当前分段Tn；否则结束当前分段，以单个周期作为新分段起点。

4. 工况突变处理：若检测到运行工况改变（如电网故障、控制策略切换），立即终止当前分段，将突变时刻后的时间重置为单开关周期分段，并更新分段计数n。

5. 分段内傅里叶展开与求解：在分段区间Tn内，对状态变量进行傅里叶级数展开，选取初始阶数q=0，利用傅里叶变换的微分与卷积性质建立分段广义状态空间微分方程组并数值求解。

6. 误差校验与阶数自适应：计算当前阶数下的状态变量相对误差σ。若σ > ε2且q < q_max，则令q=q+1重新求解；若满足精度则输出该分段结果，若超过q_max仍不满足则标记为求解错误。

7. 循环迭代推进：重复步骤3至6，直至累计分段时间覆盖全部仿真时长T，完成多时间尺度变步长电磁暂态仿真。


### 关键参数

- **占空比方差阈值(ε1)**: 用于判定连续开关周期是否具有近周期性，决定分段合并长度

- **状态变量误差限值(ε2)**: 用于校验傅里叶展开阶数是否满足工程精度要求

- **最大傅里叶阶数(q_max)**: 通常不超过10，控制模型复杂度与计算量，超限则判定求解错误

- **分段长度策略**: 稳态工况一般为2~3个开关周期，暂态工况强制为1个开关周期

- **仿真步长设置**: 详细模型固定为开关周期的1/100，P-GSSA模型采用变步长（步长等于当前分段长度）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 稳态工况不同开关频率测试 | 在0~0.2s稳态运行下，开关频率分别设为1、2、5、10kHz。分段数随频率线性增加（100至989段），最大相对误差从5.7003%降至1.3166%。 | 相比详细模型，P-GSSA在10kHz下误差仅1.3166%，但计算步长大幅延长，仿真耗时从119.673s降至95.354s，效率提升约20.3%。 |

| 暂态工况（电压跌落）测试 | 0.2~0.4s期间电网电压幅值从0.4kV跌落至0.15kV（0.21s发生，0.26s恢复）。暂态期间强制单周期分段，分段数达1243段，最大相对误差为0.4913%（10kHz）。 | 暂态误差略高于稳态，但波形高度吻合。P-GSSA模型准确捕捉了电压跌落瞬间的高频暂态响应，误差控制在0.5%以内。 |

| 光伏系统三相短路及低压穿越测试 | 0.2s发生三相短路（电压跌落70%，持续0.15s）。未采用低穿控制时并网电流峰值超额定值2.5倍；采用无功注入低穿策略后，电流幅值被抑制在0.9~1.1倍标幺值之间。 | P-GSSA模型完整复现了故障穿越全过程，全程误差始终小于5%，验证了其在复杂控制策略与严重故障下的适用性。 |



## 量化发现

- 开关频率从1kHz升至10kHz时，稳态最大相对误差从5.7003%降至1.3166%，暂态误差从4.0820%降至0.4913%，误差与开关周期Ts大致成正比。
- 在3秒仿真时长下，P-GSSA模型相比详细开关模型计算耗时降低20%以上（10kHz工况下从119.673s降至95.354s）。
- 光伏系统三相短路故障期间，采用无功注入低穿策略可将并网电流峰值从>2.5倍额定值有效抑制至0.9~1.1倍标幺值。
- 傅里叶展开阶数q通常取0~3即可满足工程精度要求，超过10阶将导致计算量剧增且易触发求解错误判定。
- 模型分段数与开关频率呈正相关，稳态工况分段长度可达2~3个周期，暂态工况自动收缩至1个周期，实现动态变步长。


## 关键公式

### 分段广义状态空间平均模型状态方程

$$$$\dot{y}(t) = \sum_{q=-\infty}^{\infty} \left[ A_0 y(t)_q + b_0 + \sum_{i=1}^{m} (A_i y(t)_q + b_i) D_i(t) \right]$$$$

*在任意分段区间Tn内使用，联合求解各阶傅里叶系数以重构含高频谐波的电磁暂态状态变量*

### 分段区间占空比平均化公式

$$$$D_i(\tau) = \begin{cases} \int_{k}^{k+1} S_i(\tau) d\tau, & \tau \in [k, k+1) \\ \frac{1}{L_s/T_n - N} \int_{N}^{L_s/T_n} S_i(\tau) d\tau, & \tau \in [N, L_s/T_n] \end{cases}$$$$

*用于将多个近周期开关动作合并计算，实现变步长建模，是分段技术的核心数学表达*

### 模型相对误差校验公式

$$$$\sigma = \max \frac{|x_P - x_D|}{x_D}$$$$

*在误差分析模块中使用，用于动态判定当前傅里叶展开阶数是否满足预设精度ε2，指导阶数自适应调整*



## 验证详情

- **验证方式**: 数值仿真对比分析（P-GSSA模型 vs 详细开关模型）
- **测试系统**: 三相PWM DC/AC逆变器、小型光伏并网发电系统（含低压穿越控制策略）
- **仿真工具**: MATLAB/Simulink（基于S函数搭建P-GSSA模型，详细模型采用标准开关器件库）
- **验证结果**: 仿真波形在稳态、电压跌落及三相短路故障下均高度吻合。最大相对误差严格控制在5%以内，计算耗时降低超20%。验证了该模型在兼顾微秒级电磁暂态精度与大规模新能源并网仿真效率方面的有效性与工程实用性。
