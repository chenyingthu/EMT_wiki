---
title: "Frequency-Adaptive Power System Modeling for"
type: source
authors: ['未知']
year: 2009
journal: ""
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/19、20、21/EMT_task_20/TPWRS.2009.2016587.pdf.pdf"]
---

# Frequency-Adaptive Power System Modeling for

**作者**: 
**年份**: 2009
**来源**: `19、20、21/EMT_task_20/TPWRS.2009.2016587.pdf.pdf`

## 摘要

—A multiscale power system modeling methodology for the integrative simulation of electromagnetic and electromechan- ical transients is introduced, implemented and validated. It makes use of frequency-adaptive simulation of transients (FAST) in which the shift frequency appears as a new parameter in addition to the time step size. For fast electromagnetic transients, tracking of instantaneous waveforms as in the Electromagnetic Transients Program (EMTP) is performed. When slower electromechan- ical transients involving power oscillations prevail, the Fourier spectra of the waveforms are shifted by typically either 50 or 60 Hz to eliminate the ac carrier and enable envelope following as in phasor-based simulation. An algorithm for the automatic setting of both shift frequency and time step 

## 核心贡献


- 提出FAST多尺度建模方法，引入频移参数统一电磁与机电暂态仿真
- 构建变压器、同步机与线路的FAST伴随模型，桥接集中与分布参数
- 设计步长与频移频率二维自适应控制算法，实现暂态过程自动切换


## 使用的方法


- [[频率自适应仿真-fast|频率自适应仿真(FAST)]]
- [[动态相量法|动态相量法]]
- [[梯形积分法|梯形积分法]]
- [[伴随模型法|伴随模型法]]
- [[节点分析法|节点分析法]]
- [[解析信号处理|解析信号处理]]


## 涉及的模型


- [[变压器|变压器]]
- [[同步电机|同步电机]]
- [[输电线路|输电线路]]


## 相关主题


- [[多尺度仿真|多尺度仿真]]
- [[电磁暂态|电磁暂态]]
- [[机电暂态|机电暂态]]
- [[动态相量|动态相量]]
- [[频率自适应建模|频率自适应建模]]


## 主要发现


- BPA电网现场测试验证线路投切暂态精度，与EMTP结果高度吻合
- 频移设为载波频率时可大幅增大步长，高效跟踪机电暂态包络线
- 线路模型有效桥接集中与分布参数，准确复现稳态至行波的多尺度现象



## 方法细节

### 方法概述

该方法提出频率自适应暂态仿真(FAST)多尺度建模框架，通过引入频移频率(shift frequency)参数$f_s$与时间步长$\Delta t$构成二维自适应控制空间。核心在于利用希尔伯特变换将实信号转换为解析信号，通过频移操作$\tilde{x}_s(t) = \tilde{x}(t)e^{-j2\pi f_s t}$将带通信号频谱搬移至基带，从而消除载波(50/60Hz)实现包络跟踪。当$f_s=0$时退化为传统EMTP的瞬时信号跟踪模式；当$f_s=f_c$（载波频率）时转为动态相量模式跟踪机电暂态包络。采用梯形积分法构建伴随模型(companion model)，通过节点分析法(nodal admittance stamping)求解，实现电磁暂态（微秒级）与机电暂态（毫秒级）的统一仿真框架。

### 数学公式


**公式1**: $$\tilde{x}(t) = x(t) + j\mathcal{H}\{x(t)\}$$

*解析信号定义：通过希尔伯特变换将实信号$x(t)$转换为复平面解析信号，消除负频率分量*


**公式2**: $$\tilde{x}_s(t) = \tilde{x}(t)e^{-j2\pi f_s t}$$

*频移操作：将解析信号频谱平移$f_s$，当$f_s=f_c$时消除载波得到复包络*


**公式3**: $$\tilde{i}_L(t) = \frac{\Delta t}{2\tilde{L}}\tilde{u}_L(t) + \tilde{I}_L(t-\Delta t)$$

*电感伴随模型：频移后的梯形积分 companion model，其中$\tilde{I}_L$为历史电流项*


**公式4**: $$\tilde{L} = L \cdot \frac{j2\pi f_s \Delta t}{j2\pi f_s \Delta t + 2}$$

*频移等效电感：考虑频移频率后的复数等效电感值*


**公式5**: $$\epsilon = \frac{1 - (\frac{\pi (f-f_s) \Delta t}{2})^2}{1 + (\frac{\pi (f-f_s) \Delta t}{2})^2} - 1$$

*相对误差公式：建模电感相对于真实电感的误差，取决于信号频率$f$、频移$f_s$和步长$\Delta t$*


**公式6**: $$\text{Re}(j\omega) > 0$$

*稳定性条件：梯形积分法在FAST中的绝对稳定性判据，对步长无上界限制*


**公式7**: $$\begin{bmatrix} \tilde{i}_1 \\ \tilde{i}_2 \end{bmatrix} = \begin{bmatrix} \frac{1}{Z} & -\frac{1}{nZ} \\ -\frac{1}{nZ} & \frac{1}{n^2Z} \end{bmatrix} \begin{bmatrix} \tilde{u}_1 \\ \tilde{u}_2 \end{bmatrix} + \begin{bmatrix} \tilde{I}_1 \\ \tilde{I}_2 \end{bmatrix}$$

*变压器伴随模型矩阵形式：包含变比$n$和漏阻抗$Z$的二维节点导纳矩阵*


### 算法步骤

1. 信号预处理：将实电压/电流信号$x(t)$通过希尔伯特变换构建解析信号$\tilde{x}(t) = x(t) + j\hat{x}(t)$，其中虚部为正交分量

2. 自适应频移设置：根据暂态类型自动选择$f_s$——电磁暂态（行波、开关操作）设$f_s=0$；机电暂态（功率振荡）设$f_s=f_c$（50或60Hz）

3. 频域搬移：对解析信号执行复数调制$\tilde{x}_s(t) = \tilde{x}(t)e^{-j2\pi f_s t}$，将带通信号转换为低通包络信号

4. 伴随模型构建：应用梯形积分法建立各元件FAST伴随模型。对电感：计算等效复阻抗$\tilde{Z}_L = \frac{2\tilde{L}}{\Delta t}$，构建包含历史电流源的诺顿等效电路

5. 系统矩阵组装：采用节点分析法(stamping)将各元件伴随模型贡献叠加至系统导纳矩阵$\mathbf{Y}$和注入电流向量$\mathbf{J}$

6. 复数域求解：求解线性方程组$\mathbf{Y}\tilde{\mathbf{u}} = \mathbf{J}$得到频移后的节点电压相量$\tilde{\mathbf{u}}$

7. 反变换与更新：通过$\tilde{x}(t) = \tilde{x}_s(t)e^{j2\pi f_s t}$恢复自然坐标系下的量，并更新历史项$\tilde{I}_L(t-\Delta t)$用于下一时步

8. 二维自适应控制：监测波形局部频率含量，若检测到高频电磁暂态则减小$\Delta t$并设$f_s=0$；若进入稳态或机电振荡则增大$\Delta t$并设$f_s=f_c$


### 关键参数

- **$\Delta t$**: 时间步长，电磁暂态模式典型值1-100$\mu$s，机电暂态模式可增至1-10ms

- **$f_s$**: 频移频率，典型值为0Hz（EMTP模式）或50/60Hz（动态相量模式）

- **$\tilde{L}$**: 频移等效电感，复数域表示，$\tilde{L} = L \cdot \frac{j2\pi f_s \Delta t}{j2\pi f_s \Delta t + 2}$

- **$f_c$**: 载波频率，电力系统通常为50Hz或60Hz

- **$n$**: 变压器变比，用于构建变压器伴随模型矩阵

- **$\tau$**: 线路传播时间，$\tau = l\sqrt{LC}$，用于分布参数线路模型



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| BPA现场试验——线路投切与恢复暂态 | 在邦纳维尔电力管理局(BPA)实际电网进行的 staged field test 中，仿真线路 energization 和 recovery 暂态过程。FAST模型准确复现了现场测量的过电压波形，包括行波传播和反射过程。在电磁暂态阶段($f_s=0$)捕捉到微秒级波头，在后续机电暂态阶段自动切换至$f_s=60$Hz模式跟踪包络线 | 与现场测量数据高度吻合，验证了模型从分布参数行波现象到集中参数机电振荡的多尺度建模能力 |

| 四机两区系统机电暂态对比 | 在IEEE标准四机两区测试系统中，模拟功率振荡和扰动响应。当设置$f_s=60$Hz消除载波后，可使用大步长$\Delta t$（毫秒级）高效跟踪电压电流包络线，而传统EMTP需保持微秒级步长以分辨60Hz载波 | 与EMTP型仿真器结果一致，但在机电暂态阶段仿真效率显著提升（步长可增大两个数量级），同时保持包络跟踪精度误差<1% |

| 变压器励磁涌流仿真 | 利用FAST变压器伴随模型（理想变压器+漏感+磁化支路）仿真合闸涌流，在$f_s=0$模式下准确捕捉非周期分量和高次谐波 | 与EMTP仿真结果偏差<0.5%，验证了伴随模型在频移条件下的数值精度 |



## 量化发现

- 当频移频率$f_s$等于信号频率$f$时，电感建模相对误差$\epsilon = 0$，此时允许使用最大时间步长而保持精度
- 频移设为载波频率（50或60Hz）时，AC载波被完全消除，仿真可仅跟踪复包络，步长$\Delta t$可从微秒级（EMTP模式）增大至毫秒级（动态相量模式），效率提升约100-1000倍
- 梯形积分法在FAST框架下具有绝对稳定性，稳定性条件为$\text{Re}(j\omega) > 0$，对时间步长$\Delta t$不存在上界限制（区别于传统EMTP的临界稳定限制）
- 误差公式$\epsilon = \frac{1-(\frac{\pi(f-f_s)\Delta t}{2})^2}{1+(\frac{\pi(f-f_s)\Delta t}{2})^2} - 1$表明，通过调整$f_s$使$(f-f_s)\rightarrow 0$，可将建模误差降至接近零，同时允许$\Delta t$显著增大
- 线路模型通过d'Alembert解和线性插值技术，在$\Delta t > \tau$（传播时间）时仍能保持数值稳定性，有效桥接集中参数与分布参数仿真
- 在BPA现场试验中，线路投切过电压峰值仿真结果与实测值偏差<2%，波头到达时间误差<1$\mu$s


## 关键公式

### 解析信号构造

$$\tilde{x}(t) = x(t) + j\mathcal{H}\{x(t)\}$$

*通过希尔伯特变换将实信号转换为复解析信号，消除负频率分量，为频移操作做准备*

### 频率自适应平移

$$\tilde{x}_s(t) = \tilde{x}(t)e^{-j2\pi f_s t}$$

*核心创新：通过复指数调制将信号频谱平移$f_s$，实现从瞬时信号($f_s=0$)到动态相量($f_s=f_c$)的连续过渡*

### FAST电感伴随模型

$$\tilde{i}_L(t) = \frac{\Delta t}{2\tilde{L}}\tilde{u}_L(t) + \tilde{i}_L(t-\Delta t) - \frac{\Delta t}{2\tilde{L}}\tilde{u}_L(t-\Delta t)$$

*基于梯形积分法的频移域companion model，其中$\tilde{L}$为频移等效电感，用于节点分析法的矩阵组装*

### 建模相对误差

$$\epsilon = \frac{1 - (\frac{\pi (f-f_s) \Delta t}{2})^2}{1 + (\frac{\pi (f-f_s) \Delta t}{2})^2} - 1$$

*量化分析频移频率选择对精度的影响，指导二维自适应控制算法中$f_s$的自动设置*

### 绝对稳定性判据

$$\text{Re}(j\omega) > 0$$

*证明FAST使用梯形积分法时对任意步长$\Delta t$和频移$f_s$组合均保持稳定，为多尺度仿真提供理论基础*



## 验证详情

- **验证方式**: 双重验证：与BPA实际电网现场试验数据对比，以及与商业EMTP型仿真器（如PSCAD/EMTDC）进行背靠背仿真对比
- **测试系统**: 1) BPA实际500kV电网：包含线路投切、故障清除和恢复暂态；2) 标准四机两区Kundur系统：用于机电暂态和功角稳定性验证；3) 单端供电变压器系统：用于励磁涌流验证
- **仿真工具**: 自主开发的FAST仿真平台，与EMTP-type simulator（提及EMTP/SPICE算法作为基准）进行精度对比，使用MATLAB进行后处理分析
- **验证结果**: 现场试验验证表明，FAST能准确复现线路 energization 的过电压波形（峰值误差<2%，时延误差<1$\mu$s），包括行波传播和反射细节。与EMTP对比显示，在电磁暂态阶段($f_s=0$)两者精度相当；在机电暂态阶段通过自动切换至$f_s=60$Hz模式，可在保持包络精度（误差<1%）的同时将步长增大100倍以上，显著提升计算效率。线路模型成功桥接微秒级行波现象和毫秒级功率振荡，验证了多尺度建模的有效性。
