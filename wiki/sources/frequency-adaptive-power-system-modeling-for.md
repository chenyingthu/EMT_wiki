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


