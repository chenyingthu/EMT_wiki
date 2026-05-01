---
title: "动态相量法 (Dynamic Phasor Method)"
type: method
tags: [dynamic-phasor, frequency-shift, emt-simulation, phasor-domain, multiscale-modeling]
created: "2026-04-30"
---

# 动态相量法 (Dynamic Phasor Method)

## 定义与概述

动态相量法是电磁暂态仿真中实现多时间尺度建模的核心方法，通过将时域信号分解为缓慢变化的幅值和相位分量（动态相量），在保证精度的前提下显著增大仿真步长。该方法基于频谱搬移原理，将高频交流信号转换为低频复包络，突破了传统EMT仿真受奈奎斯特采样定理限制的步长约束，特别适用于大规模交直流混联电网的高效仿真。

## 1. 理论基础

### 1.1 动态相量定义

**k阶动态相量**:
$$\langle x \rangle_k(t) = \frac{1}{T}\int_{t-T}^{t} x(\tau)e^{-jk\omega_s \tau} d\tau$$

其中：
- $T$: 滑动窗周期（通常取基频周期20ms）
- $\omega_s$: 基波角频率
- $k$: 谐波阶数
- $\langle x \rangle_k$: 第k阶动态相量（复数）

### 1.2 复数信号构造

**解析信号构造**:
$$x_S(t) = x(t) + j x_T(t)$$

**希尔伯特变换法**（最优）：
$$x_T(t) = \mathcal{H}\{x(t)\} = \frac{1}{\pi} \int_{-\infty}^{+\infty} \frac{x(\tau)}{t-\tau} d\tau$$

**微分变换法**（简化）：
$$x_T(t) = -\frac{1}{\omega_c}\frac{dx(t)}{dt}$$

**积分变换法**（替代）：
$$x_T(t) = \omega_c \int x(t)dt$$

### 1.3 移频变换

**复数移频变换**:
$$x_E(t) = x_S(t) e^{-j\omega_c t} = (x(t) + jx_T(t))e^{-j\omega_c t}$$

**实数矩阵形式**:
$$\begin{bmatrix} x_u(t) \\ x_v(t) \end{bmatrix} = \begin{bmatrix} \cos(\omega_c t) & \sin(\omega_c t) \\ -\sin(\omega_c t) & \cos(\omega_c t) \end{bmatrix} \begin{bmatrix} x(t) \\ x_T(t) \end{bmatrix}$$

其中：
- $x_u(t), x_v(t)$: 复包络的实部和虚部
- $\omega_c$: 中心角频率（基波角频率）

## 2. EMT仿真应用

### 2.1 移频电磁暂态模型

**移频微分方程**:
$$\frac{dx_E(t)}{dt} = f_E(t) - j\omega_c x_E(t)$$

**梯形积分离散化**:
$$\frac{x_E(t) - x_E(t-\Delta t)}{\Delta t} = \frac{f_E(t) + f_E(t-\Delta t)}{2} - j\omega_c \frac{x_E(t) + x_E(t-\Delta t)}{2}$$

**I型模型（复数形式）**:
- 直接求解n维复数节点电压方程
- 计算量小，内存访问局部性好
- 算术运算次数：$N_1 = 2nD + \frac{4n^3+12n^2+14n}{3}M + \frac{4n^3+12n^2+2n}{3}A$

**II型模型（矩阵形式）**:
- 求解2n维实数方程组
- 避免复数运算但计算量较大
- 算术运算次数：$N_2 = 2nD + \frac{8n^3+12n^2-2n}{3}M + \frac{8n^3+12n^2-2n}{3}A$

### 2.2 MMC动态相量建模

**基频动态相量（BFDP）**:
$$X_B(t) = \langle x \rangle_0(t) e^{-j\frac{2\pi}{T}(t-T+s)} + 2\sum_{k=1}^{+\infty} \langle x \rangle_k(t) e^{j(k-1)\frac{2\pi}{T}(t-T+s)}$$

**和/差分量解耦**:
- 和分量（s）：表征直流/共模动态
- 差分量（d）：表征交流/环流动态

**电容电压动态方程**:
$$\frac{d}{dt}V_{Cx}^{s,d} = \frac{1}{2NC_{SM}}(S_x^s i_x^{s,d} + S_x^d i_x^{s,d})$$

**桥臂电流动态方程**:
$$\frac{d}{dt}i_x^{s,d} = -\frac{1}{L}\left(\frac{1}{2}S_x^s V_{Cx}^{s,d} + \frac{1}{2}S_x^d V_{Cx}^{s,d} + R i_x^{s,d} \mp V_{dc}\right)$$

### 2.3 多频率分量处理

**傅里叶微分性质**:
$$\left\langle \frac{dx}{dt} \right\rangle_q = \frac{d\langle x \rangle_q}{dt} - jq\omega_s \langle x \rangle_q$$

**傅里叶乘积卷积性质**:
$$\langle xy \rangle_q = \sum_{i=-\infty}^{\infty} \langle x \rangle_{q-i} \langle y \rangle_i$$

## 3. 实现技术

### 3.1 复数信号构造算法

**算法步骤**:
1. 对原始电压/电流实信号$x(t)$应用数学变换$T(x)$生成正交信号$x_T(t)$
2. 构造复数信号$x_S(t) = x(t) + jx_T(t)$
3. 执行移频变换$x_E(t) = x_S(t)e^{-j\omega_c t}$
4. 建立移频微分方程并离散化求解

**构造方法对比**:
| 方法 | 负频率抑制 | 实现复杂度 | 精度 | 适用场景 |
|------|-----------|-----------|------|----------|
| 希尔伯特变换 | 完全消除 | 高（卷积运算） | 最高 | 高精度要求 |
| 微分变换 | 残留~5% | 低 | 中等 | 实时仿真 |
| 积分变换 | 残留~5% | 低 | 中等 | 快速估计 |

### 3.2 模型离散化策略

**I型模型（复数形式）优势**:
- 复数形式比矩阵形式快约2.4-2.6倍
- IEEE 9241节点系统：复数形式8.15s vs 矩阵形式21.59s
- 内存访问局部性更好，缓存命中率更高

**步长选择**:
- 传统EMT：$\Delta t < 1/(10f_{max})$
- 移频EMT：$\Delta t$ 可增大5-10倍
- 典型步长：50μs（传统10μs）

### 3.3 谐波阶数选择

**保留阶数与精度关系**:
| 保留谐波 | 幅值误差 | 相位误差 | 计算耗时增加 |
|----------|----------|----------|--------------|
| 基波(k=0) | <5% | <2° | 基准 |
| 基波+2次 | <2% | <1° | +15% |
| 基波+5次 | <0.5% | <0.3° | +50% |
| 基波+7次 | <0.3% | <0.2° | +80% |

## 4. 仿真软件实现

### 4.1 PSCAD/EMTDC实现

```fortran
! 移频变换模块
SUBROUTINE FREQUENCY_SHIFT(X_REAL, X_IMAG, OMEGA_C, T, X_SHIFTED)
    COMPLEX X_SHIFTED
    REAL X_REAL, X_IMAG, OMEGA_C, T
    
    ! 构造复数信号
    X_COMPLEX = CMPLX(X_REAL, X_IMAG)
    
    ! 移频变换
    X_SHIFTED = X_COMPLEX * CEXP(-CMPLX(0.0, OMEGA_C * T))
    
END SUBROUTINE

! 动态相量提取
SUBROUTINE DYNAMIC_PHASOR(X_TIME, OMEGA_S, K, T_WINDOW, PHASOR_K)
    COMPLEX PHASOR_K
    REAL X_TIME(*), OMEGA_S, T_WINDOW
    INTEGER K, N_STEPS
    
    PHASOR_K = CMPLX(0.0, 0.0)
    DT = T_WINDOW / N_STEPS
    
    DO I = 1, N_STEPS
        TAU = I * DT
        PHASOR_K = PHASOR_K + X_TIME(I) * CEXP(-CMPLX(0.0, K * OMEGA_S * TAU)) * DT
    END DO
    
    PHASOR_K = PHASOR_K / T_WINDOW
    
END SUBROUTINE
```

### 4.2 MATLAB实现

```matlab
classdef DynamicPhasorModel < handle
    properties
        omega_c         % 中心角频率
        T_window        % 滑动窗周期
        k_max           % 最大谐波阶数
        phasor_history  % 历史相量
    end
    
    methods
        function obj = DynamicPhasorModel(omega_c, T_window, k_max)
            obj.omega_c = omega_c;
            obj.T_window = T_window;
            obj.k_max = k_max;
            obj.phasor_history = cell(k_max+1, 1);
        end
        
        function x_analytic = hilbert_transform(obj, x_real)
            % 希尔伯特变换构造解析信号
            x_hilbert = hilbert(x_real);
            x_analytic = x_real + 1j * imag(x_hilbert);
        end
        
        function x_envelope = frequency_shift(obj, x_analytic, t)
            % 移频变换
            x_envelope = x_analytic * exp(-1j * obj.omega_c * t);
        end
        
        function phasor = extract_phasor(obj, x_time, k)
            % 提取k阶动态相量
            N = length(x_time);
            dt = obj.T_window / N;
            omega_k = k * obj.omega_c;
            
            phasor = 0;
            for i = 1:N
                tau = (i-1) * dt;
                phasor = phasor + x_time(i) * exp(-1j * omega_k * tau) * dt;
            end
            phasor = phasor / obj.T_window;
        end
        
        function x_reconstructed = reconstruct_signal(obj, phasors, t)
            % 信号重构
            x_reconstructed = real(phasors{1});
            for k = 1:obj.k_max
                x_reconstructed = x_reconstructed + ...
                    2 * real(phasors{k+1} * exp(1j * k * obj.omega_c * t));
            end
        end
    end
end
```

## 5. 典型参数参考

| 应用场景 | 中心频率 | 仿真步长 | 保留谐波 | 加速比 | 精度 |
|----------|----------|----------|----------|--------|------|
| 交流输电系统 | 50/60 Hz | 50-100 μs | 基波+3次 | 5-10倍 | 误差<1% |
| MMC-HVDC | 50 Hz | 50 μs | 基波+7次 | 15-25倍 | 误差<0.5% |
| 风电并网 | 50 Hz | 100 μs | 基波+5次 | 10-20倍 | 误差<2% |
| 大规模电网 | 50 Hz | 200 μs | 基波 | 50-100倍 | 误差<5% |

## 相关方法
- [[switching-function|开关函数法]] - 与动态相量结合使用
- [[average-value-model|平均值模型]] - 动态相量的低阶近似
- [[numerical-integration|数值积分]] - 移频模型离散化
- [[thevenin-norton-equivalent|戴维南-诺顿等效]] - 移频等效电路
- [[discretization-methods|离散化方法]] - 复数域离散化技术

## 相关模型
- [[mmc-model|MMC模型]] - 基频动态相量在MMC建模中的应用
- [[vsc-model|VSC模型]] - 移频变换在VSC建模中的应用
- [[transmission-line-model|输电线路模型]] - 移频传输线模型实现
- [[synchronous-machine-model|同步电机模型]] - 动态相量电机模型
- [[dfig-model|DFIG模型]] - 风机变流器移频建模

## 相关主题
- [[real-time-simulation|实时仿真]] - 动态相量加速实时仿真技术
- [[multirate-method|多速率方法]] - 多时间尺度仿真协调
- [[harmonic-analysis|谐波分析]] - 动态相量谐波提取方法
- [[frequency-dependent-modeling|频率相关建模]] - 频域建模方法

## 7. 适用边界与限制

### 7.1 适用条件
- **带限信号**: 信号频谱集中，带宽远小于中心频率
- **缓变幅值**: 信号幅值/相位变化远慢于载波周期
- **已知中心频率**: 系统基波频率明确且稳定
- **周期性稳态**: 适用于稳态或准稳态分析

### 7.2 失效边界
- **宽频暂态**: 故障引起的高频分量（>10次谐波）
- **强非线性**: 铁磁饱和、电弧等非线性现象
- **快速切换**: 保护动作、开关操作等瞬态过程
- **频率偏移**: 系统频率大幅偏移额定值

### 7.3 精度边界
| 应用场景 | 幅值误差 | 相位误差 | 暂态误差 | 适用频段 |
|----------|---------|---------|----------|----------|
| 稳态运行 | <0.5% | <0.3° | - | 基波+7次 |
| 功率阶跃 | <2% | <1° | <5% | 基波+5次 |
| 故障暂态 | <5% | <2° | <15% | 基波+3次 |
| 机电振荡 | <1% | <0.5° | <3% | 基波 |

## 8. 来源论文

| 论文 | 年份 | 核心贡献 |
|------|------|----------|
| 电力系统移频电磁暂态仿真原理及应用综述 | 2022 | 系统梳理移频仿真三大关键技术，比较三种复数信号构造方法 |
| A Dynamic Phasor Model of an MMC with Extended Frequency Range for EMT Simulations | 2018 | 基频动态相量BFDP，计算效率提升15-25倍，精度<0.5% |
| 模块化多电平换流器时间尺度变换建模和仿真 | 2022 | 时间尺度变换与动态相量结合，仿真速度提升206倍 |
| 一种用于LCC-HVDC系统小干扰稳定性分析的改进动态相量模型 | 2022 | 改进动态相量用于小干扰稳定性分析 |

---

*本页面基于Karpathy LLM Wiki Pattern构建，内容来自682篇EMT领域学术文献的深度分析*
