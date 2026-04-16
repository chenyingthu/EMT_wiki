---
title: "An open-source parallel EMT simulation framework"
type: source
authors: ['Min Xiong']
year: 2024
journal: "Electric Power Systems Research, 235 (2024) 110734. doi:10.1016/j.epsr.2024.110734"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/07&08/Xiong et al. - 2024 - An open-source parallel EMT simulation framework.pdf"]
---

# An open-source parallel EMT simulation framework

**作者**: Min Xiong
**年份**: 2024
**来源**: `07&08/Xiong et al. - 2024 - An open-source parallel EMT simulation framework.pdf`

## 摘要

Min Xiong a,b, Bin Wang c, Deepthi Vaidhynathan a, Jonathan Maack a, Matthew J. Reynolds a, Andy Hoke a, Kai Sun b, Deepak Ramasubramanian d, Vishal Verma d, Jin Tan a,* a National Renewable Energy Laboratory, Golden, CO, 80401, USA b University of Tennessee, Knoxville, TN, 37996, USA c University of Texas at San Antonio, San Antonio, TX, 78249, USA

## 核心贡献


- 开发开源Python电磁暂态仿真框架，支持跨平台运行与模块化扩展
- 采用BBD矩阵分解与MPI技术，实现网络方程自动化并行求解
- 集成Numba即时编译与PSSE潮流初始化，显著提升计算效率


## 使用的方法


- [[节点分析法|节点分析法]]
- [[梯形积分法|梯形积分法]]
- [[加边块对角矩阵分解|加边块对角矩阵分解]]
- [[mpi并行计算|MPI并行计算]]
- [[numba即时编译|Numba即时编译]]
- [[人工阻尼电阻|人工阻尼电阻]]


## 涉及的模型


- [[逆变器型资源-ibr|逆变器型资源(IBR)]]
- [[同步电机|同步电机]]
- [[输电线路|输电线路]]
- [[变压器|变压器]]
- [[故障模型|故障模型]]
- [[标准测试系统|标准测试系统]]


## 相关主题


- [[电磁暂态仿真|电磁暂态仿真]]
- [[并行计算|并行计算]]
- [[开源仿真框架|开源仿真框架]]
- [[大规模电力系统|大规模电力系统]]
- [[逆变器型资源并网|逆变器型资源并网]]
- [[高性能计算|高性能计算]]
- [[系统稳定性分析|系统稳定性分析]]


## 主要发现


- BBD并行算法有效突破大规模网络求解瓶颈，显著缩短仿真耗时
- Numba即时编译大幅优化Python循环计算，提升框架运行效率
- 多算例验证表明框架在保持仿真精度的同时具备优异并行加速比


