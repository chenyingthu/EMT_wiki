---
title: "DSOGI锁相环电磁暂态建模方法 (DSOGI-PLL)"
type: method
tags: [dsogi-pll, phase-locked-loop, sogi, synchronization, grid-following]
created: "2026-05-10"
updated: "2026-05-12"
---

# DSOGI锁相环电磁暂态建模方法 (DSOGI-PLL)

## 1. 物理背景与工程需求

并网逆变器(GFL)的同步精度直接决定其功率注入和故障穿越行为的正确性。在平衡且无谐波的理想电网中,同步旋转坐标系锁相环(SRF-PLL)能以简单结构实现高精度相位跟踪。然而,当电网发生不对称故障(产生负序分量)、谐波畸变(THD>3%)或频率扰动时,SRF-PLL的单一dq变换会同时受正序和负序分量调制,导致相位估计中出现二倍频振荡;低通滤波器虽然可以抑制振荡,却会牺牲暂态响应速度。

DSOGI-PLL(双二阶广义积分器锁相环)解决这一矛盾的核心思路是:在电网同步的路径中引入正交信号发生器(QSG)和正序分量计算器(PSC),先从不平衡/畸变的三相电压中提取基波正序分量,再将该正序分量送入SRF-PLL环路完成相位锁定。由此,DSOGI-PLL将同步解耦为正序提取和相位跟踪两个独立环节,在不平衡和谐波条件下仍能获得无纹波的同步相位。工程需求包括:(1)弱电网(SCR<3)中三相电压严重不平衡时的可靠同步;(2)谐波畸变(5%-10%THD)下不依赖大量滤波器即可维持精度;(3)故障穿越期间快速、准确的相位估计,以免逆变器控制因错误相位失稳。

## 2. 数学描述

### 2.1 二阶广义积分器(SOGI)

SOGI是DSOGI-PLL的核心滤波组件,生成与输入电压同相(v')和正交(qv')的信号。其传递函数为:

$$D(s) = \frac{v'(s)}{v(s)} = \frac{k\omega_0 s}{s^2 + k\omega_0 s + \omega_0^2}, \quad Q(s) = \frac{qv'(s)}{v(s)} = \frac{k\omega_0^2}{s^2 + k\omega_0 s + \omega_0^2}$$

其中$\omega_0$为谐振频率(由PLL锁定频率反馈更新),$k$为阻尼系数。D(s)是带通滤波器(BPF),在$\omega_0$处增益为1、相移0;Q(s)是低通滤波器(LPF),在$\omega_0$处增益为1、相移-90度。典型取值$k=1.414$(对应阻尼比$\xi=0.7$),在带宽与选择性之间取折中。

SOGI的时域状态方程可写为:
$$\frac{d}{dt}\begin{bmatrix} v' \\ qv' \end{bmatrix} = \begin{bmatrix} -k\omega_0 & -\omega_0 \\ \omega_0 & 0 \end{bmatrix} \begin{bmatrix} v' \\ qv' \end{bmatrix} + \begin{bmatrix} k\omega_0 \\ 0 \end{bmatrix} v$$

### 2.2 双SOGI与正序提取

将三相电压$v_{abc}$经Clarke变换得到$v_{\alpha\beta}$,分别送入两个独立SOGI(一个用于$\alpha$轴,一个用于$\beta$轴),得到四路信号$v'_\alpha, qv'_\alpha, v'_\beta, qv'_\beta$。正序分量计算器(PSC)按如下公式提取基波正序:

$$\begin{bmatrix} v_{\alpha}^+ \\ v_{\beta}^+ \end{bmatrix} = \frac{1}{2} \begin{bmatrix} 1 & -e^{j\pi/2} \\ e^{j\pi/2} & 1 \end{bmatrix} \begin{bmatrix} v'_{\alpha} \\ v'_{\beta} \end{bmatrix} = \frac{1}{2} \begin{bmatrix} v'_\alpha - qv'_\beta \\ qv'_\alpha + v'_\beta \end{bmatrix}$$

式中的$-e^{j\pi/2}$和$e^{j\pi/2}$分别对应滞后和超前90度操作,由SOGI生成的$qv'$信号自然提供。这一组合可完全消除负序分量,在不平衡条件下获得纯净正序。

### 2.3 正序到相位锁定

正序分量$v_{\alpha\beta}^+$经Park变换转到$dq$坐标系:
$$\begin{bmatrix} V_d \\ V_q \end{bmatrix} = \begin{bmatrix} \cos\hat{\theta} & \sin\hat{\theta} \\ -\sin\hat{\theta} & \cos\hat{\theta} \end{bmatrix} \begin{bmatrix} v_{\alpha}^+ \\ v_{\beta}^+ \end{bmatrix}$$

锁相误差由反正切计算(Ranasinghe 2024):
$$\theta_{err} = \tan^{-1}\left(\frac{V_q}{V_d}\right)$$

替代传统SRF-PLL的$V_q$直接反馈,消除电压幅值波动对环路增益的非线性耦合。误差信号经PI控制器生成角频率偏差:
$$\Delta\omega = K_p \theta_{err} + K_i \int \theta_{err} dt$$

最终相位由积分得到:
$$\hat{\theta} = \int (\omega_0 + \Delta\omega) dt$$

### 2.4 开环传递函数

DSOGI-PLL的开环传递函数(Ranasinghe 2024)为:
$$G_{ol}(s) = \left(\frac{K_p s + K_i}{s}\right) \left(\frac{\omega_p}{\omega_p + s}\right) \frac{1}{s}$$

其中第一项为PI控制器,第二项为低通滤波(截止频率$\omega_p$),第三项为积分器。闭环特征方程:
$$s^3 + \omega_p s^2 + K_p\omega_p s + K_i\omega_p = 0$$

PI参数与目标阻尼比$\xi$和自然频率$\omega_n$的关系可通过系数匹配获得:
$$\omega_p = 2\xi\omega_n + A, \quad A\omega_n^2 = K_i\omega_p, \quad \omega_n^2 + 2\xi\omega_n A = \omega_p K_p$$

## 3. 计算模型与离散化

### 3.1 SOGI的离散化

SOGI需要连续时间或离散时间实现。在EMT仿真(步长$\Delta t=50\mu s$)中,可采用双线性变换(Tustin)将SOGI传递函数离散化。对D(s)应用$s = \frac{2}{\Delta t}\frac{z-1}{z+1}$:

$$D(z) = \frac{k\omega_0 \cdot \frac{2}{\Delta t}\frac{z-1}{z+1}}{\left(\frac{2}{\Delta t}\frac{z-1}{z+1}\right)^2 + k\omega_0\left(\frac{2}{\Delta t}\frac{z-1}{z+1}\right) + \omega_0^2}$$

化简后可写为二阶IIR滤波器形式。离散化精度取决于$\Delta t$与$\omega_0$的比值:当$\Delta t \ll 1/\omega_0$时(典型工况$\Delta t=50\mu s$, $\omega_0=2\pi\cdot 60\approx 377$ rad/s,比值<0.02),双线性变换引入的频率翘曲可忽略。

### 3.2 数字实现流程

每个仿真步长$t_n$执行:

1. **Clarke变换**: $v_\alpha, v_\beta \gets v_{abc}(t_n)$
2. **SOGI滤波**: 对$v_\alpha$和$v_\beta$分别执行离散化SOGI更新,使用上一时刻频率估计$\hat{\omega}(t_{n-1})$作为$\omega_0$,得到$v'_\alpha, qv'_\alpha, v'_\beta, qv'_\beta$
3. **正序提取**: $v^+_\alpha = (v'_\alpha - qv'_\beta)/2$, $v^+_\beta = (qv'_\alpha + v'_\beta)/2$
4. **Park变换**: 使用当前相位估计$\hat{\theta}(t_{n-1})$将$v^+_{\alpha\beta}$转到$dq$,计算$\theta_{err}$
5. **PI更新**: $\Delta\omega(t_n) = K_p\theta_{err} + K_i \cdot$累积积分
6. **相位更新**: $\hat{\theta}(t_n) = \hat{\theta}(t_{n-1}) + \Delta t \cdot (\omega_0 + \Delta\omega(t_n))$
7. **频率反馈**: 将$\hat{\omega}(t_n) = \omega_0 + \Delta\omega(t_n)$作为下一时刻SOGI的谐振频率

## 4. 实现方法与算法细节

### 4.1 PLL方法对比

| 特性 | SRF-PLL | DSOGI-PLL | 改进DSOGI-PLL(Ranasinghe 2024) |
|------|---------|------------|-------------------------------|
| 正序提取 | 无(受负序直接干扰) | 双SOGI+PSC完整提取 | 同DSOGI |
| 相位误差计算 | 直接$V_q$反馈 | $\tan^{-1}(V_q/V_d)$ | 同DSOGI |
| 谐波抑制 | 需额外LPF | SOGI内置带通滤波 | 同DSOGI |
| 频率反馈 | 无 | SOGI使用PLL估计频率 | 暂态检测后冻结SOGI频率 |
| 带宽调整 | 固定 | 固定 | 自适应5x缩放 |
| 不对称故障调节时间 | 含二倍频振荡 | 无纹波 | 约0.016s(-60% vs DSOGI) |
| 90度相位跳变调节时间 | 含大幅超调 | 约0.15s | 约0.03s(-80%) |
| SCR下限 | >3.0(弱网敏感) | 约2.3 | 约1.0 |
| 稳态THD抑制(4%THD) | 误差较大 | RMSE约0.0078 rad | RMSE约0.0063 rad |
| 计算复杂度 | 低 | 中(2个IIR + PSC) | 中高(增加暂态检测+BW调度) |

### 4.2 改进DSOGI-PLL的关键增强

Ranasinghe(2024)在标准DSOGI-PLL基础上增加了三个改进:

**(a) 反正切线性化**: 用$\theta_{err} = \tan^{-1}(V_q/V_d)$替代直接$V_q$反馈。在SRF-PLL中,$V_q$的增益随$V_d$(即电压幅值)变化;低电压(如故障时)会使环路增益大幅降低,减缓同步。反正切使误差信号标准化为角度,不依赖幅值。

**(b) 暂态频率冻结**: 监测PLL估计频率的变化率$d\hat{\omega}/dt$。当检测到突变超过阈值时,锁存DSOGI中使用的$\omega_0$至当前值,保持冻结时间$T_{fz}=0.1$s。此举切断"扰动导致频率估计偏移导致SOGI谐振频率偏离导致滤波失真导致更大同步误差"的正反馈链。

**(c) 自适应带宽**: 实时计算$|\theta_{err}|$,当超过阈值$\varepsilon=0.1$rad时,目标穿越频率$\omega_c$从标称值62rad/s提升至5倍(310rad/s),并根据闭环特征方程系数匹配重新计算Kp和Ki。当误差衰减至阈值以下后,带宽线性恢复至标称值,避免稳态下对谐波和噪声的过度放大。

### 4.3 标称参数示例(Ranasinghe 2024, 60Hz系统)

| 参数 | 符号 | 标称值 | 暂态值 |
|------|------|-------|--------|
| SOGI阻尼系数 | k | 1.414 | 不变 |
| 标称穿越频率 | $\omega_c$ | 62 rad/s | 310 rad/s(5x) |
| PI比例系数 | $K_p$ | 57.1 | 重算 |
| PI积分系数 | $K_i$ | 1660.1 | 重算 |
| 目标阻尼比 | $\xi$ | 0.7 | 0.7 |
| 相位误差阈值 | $\varepsilon$ | — | 0.1 rad |
| 频率冻结时间 | $T_{fz}$ | — | 0.1 s |

## 5. 适用边界与失效模式

### 适用条件(valid_when)
- 不平衡电网(不对称故障)条件下的GFM/GFL逆变器同步
- 谐波畸变环境(THD 3%-10%)下的正序分量提取
- 弱电网(SCR 1.0-3.0)中需要可靠锁相的并网逆变器EMT仿真
- 跟网型IBR等效模型的同步模块(如Luchini 2023中ATP实现)
- 频率扰动(频率斜坡不大于7Hz/s)下的快速相位恢复

### 失效边界(invalid_when)
- 超弱电网(SCR<1.0): DSOGI-PLL自身结构仍可能失稳(改进PLL已将极限扩至SCR=1.0)
- 极高频扰动(>10Hz/s频率变化): 频率冻结的时间常数Tfz可能不适合
- 构网型(GFM)逆变器控制: GFM自身建立电压频率,不需要PLL同步
- 器件级开关瞬态仿真: DSOGI-PLL是平均化同步模型,不涉及开关事件
- 硬件在环(HIL)实时仿真: 本文改进PLL仅在50us步长的PSCAD中验证

### 关键假设(assumptions)
- SOGI阻尼系数k=1.414(对应阻尼比0.7)为固定值(据Ranasinghe 2024)
- 频率冻结时间Tfz=0.1s对多数电力系统暂态适用;更短的暂态(如<0.05s)可能需要调整
- 带宽自适应切换的阈值0.1rad针对本文测试系统整定;对其他应用可能需要重新校准
- 正序提取假设三相电路不带零序分量(仅考虑正序和负序)

### 证据缺口(evidence_gaps)
- Ranasinghe 2024改进DSOGI-PLL仅在PSCAD/EMTDC中完成仿真验证,无硬件实验或HIL测试数据
- 自适应带宽的5倍放大系数的通用性未在多种控制结构下验证
- 频率冻结机制的鲁棒性在持续频率漂移(如孤岛微电网)场景下的表现未见报道
- 改进PLL在不同逆变器控制(如虚拟同步机、下垂控制)接口下的兼容性数据缺失

## 6. 应用案例

### 案例1: 弱电网光伏逆变器的改进DSOGI-PLL验证

Ranasinghe等(2024)在PSCAD/EMTDC中构建了替换同步发电机的IEEE 9节点系统,其接入光伏逆变器在SCR约1.8的弱电网中运行。采用改进DSOGI-PLL后,在不对称故障下相位调节时间从0.040s降至0.016s(降幅60%),超调从0.272rad降至0.113rad(降幅58.5%);在90度相位跳变下调节时间从0.15s降至0.03s(降幅80%)。频率跟踪RMSE在暂态区间内从2.16Hz降至0.001Hz(降幅99.95%),稳定运行SCR极限从2.3扩展至1.0(提升56.5%)。

### 案例2: ATP/ATPDraw中DSOGI-PLL作为同步模块

Luchini(2023)在ATP/ATPDraw中实现跟网型IBR等效时域模型,提供DSOGI-PLL和LPF-PLL两种同步模块选项。DSOGI-PLL在电网电压畸变条件下可有效抑制谐波干扰,保障同步相位精度。该等效模型在故障条件下平均电流误差约2.33%,仿真时间较全开关基准模型减少约70%。

### 案例3: DSOGI-PLL在GFL逆变器EMT仿真中的角色

在系统级EMT仿真中,DSOGI-PLL通常作为跟网型逆变器完整模型的组成部分。其输出相位用于:坐标变换(将电流控制从abc转到dq)、功率计算(计算P、Q与指令误差)和故障穿越逻辑(判断电压幅值和相位跳变量)。DSOGI-PLL的精度直接决定了电流控制的方向是否正确,在不平衡故障时尤其关键——相位误差过大会使Vd和Vq的控制耦合失配,导致电流超调和功率振荡。

## 7. 量化性能边界

**Ranasinghe 2024 改进DSOGI-PLL（自适应带宽+频率冻结）**:
- 在PSCAD/EMTDC中构建替换同步发电机的IEEE 9节点系统，光伏逆变器在SCR≈1.8弱电网中运行
- 不对称故障下相位调节时间从0.040s降至0.016s（降幅60%），超调从0.272rad降至0.113rad（降幅58.5%）
- 90度相位跳变下调节时间从0.15s降至0.03s（降幅80%）
- 频率跟踪RMSE在暂态区间内从2.16Hz降至0.001Hz（降幅99.95%）
- 稳定运行SCR极限从2.3扩展至1.0（提升56.5%）
- 数据缺口：仅在PSCAD/EMTDC中完成仿真验证，无硬件实验或HIL测试数据

**Luchini 2023 ATP/ATPDraw GFL等效模型（DSOGI-PLL同步）**:
- 在ATP/ATPDraw中实现跟网型IBR等效时域模型，提供DSOGI-PLL和LPF-PLL两种同步模块
- 故障条件下平均电流误差约2.33%
- 仿真时间较全开关基准模型减少约70%
- DSOGI-PLL在电网电压畸变条件下可有效抑制谐波干扰
- 数据缺口：等效模型精度仅在故障条件下验证，稳态谐波工况下的误差未单独报告

**数据缺口声明**：DSOGI-PLL的量化性能数据主要来自离线EMT仿真平台（PSCAD/EMTDC、ATP），实时硬件平台下的性能数据缺失。不同改进DSOGI-PLL方案（自适应带宽/频率冻结/并联SOGI等）间的横向对比缺乏统一基准系统和标准化测试工况。Ranasinghe 2024改进PLL在不同逆变器控制（虚拟同步机、下垂控制）接口下的兼容性数据未见报道。

## 8. 延伸阅读

### 方法相关
- [[srf-pll]]: SRF-PLL基准结构,与DSOGI-PLL对比理解正序提取的必要性
- [[phase-locked-loop]]: PLL总体分类和通用概念
- [[dq-transformation]]: Park变换和Clarke变换的数学基础

### 模型相关
- [[gfl-inverter-model]]: 跟网型逆变器模型,DSOGI-PLL是其同步环节
- [[grid-connected-inverter]]: 并网逆变器整体模型
- [[pv-power-plant]]: 光伏电站模型,典型DSOGI-PLL应用场景

### 控制相关
- [[grid-forming-control]]: 构网型控制,不依赖PLL同步
- [[fault-ride-through]]: 故障穿越控制,依赖PLL的相位估计

### 代表性来源
- [[advanced-dsogi-pll-with-adaptive-bandwidth|Ranasinghe 2024 - 改进型DSOGI-PLL自适应带宽]]
- [[equivalent-grid-following-inverter-model-atp|Luchini 2023 - ATP中跟网型逆变器等效模型(DSOGI-PLL同步)]]

---

*本页面遵循学术严谨性原则，所有技术细节均基于同行评议的学术文献。*
