---
title: "Retinal Area Detector From Scanning Laser Ophthalmoscope (SLO) Images for Diagnosing Retinal Diseases"
type: source
authors: ['未知']
year: 2015
journal: "IEEE Journal of Biomedical and Health Informatics;2015;19;4;10.1109/JBHI.2014.2352271"
tags: ['emt']
created: "2026-04-13"
sources: ["EMT_Doc/04/ACCESS.2020.2983356.pdf.pdf"]
---

# Retinal Area Detector From Scanning Laser Ophthalmoscope (SLO) Images for Diagnosing Retinal Diseases

**作者**: 
**年份**: 2015
**来源**: `04/ACCESS.2020.2983356.pdf.pdf`

## 摘要

—Scanning laser ophthalmoscopes (SLOs) can be used for early detection of retinal diseases. With the advent of latest screening technology, the advantage of using SLO is its wide ﬁeld of view, which can image a large part of the retina for better diag- nosis of the retinal diseases. On the other hand, during the imaging process, artefacts such as eyelashes and eyelids are also imaged along with the retinal area. This brings a big challenge on how to exclude these artefacts. In this paper, we propose a novel approach to automatically extract out true retinal area from an SLO image based on image processing and machine learning approaches. To reduce the complexity of image processing tasks and provide a convenient primitive image pattern, we have grouped pixels into different regions based o

## 核心贡献



- 提出一种基于图像处理和机器学习的方法，自动从SLO图像中提取真实视网膜区域
- 利用超像素分组降低图像处理复杂度，提取纹理与结构特征以区分视网膜区域与伪影

## 使用的方法

- [[图像处理|图像处理]]
- [[机器学习|机器学习]]
- [[超像素分割|超像素分割]]
- [[特征提取与选择|特征提取与选择]]
- [[分类算法|分类算法]]

## 涉及的模型

- [[扫描激光检眼镜-slo-成像系统|扫描激光检眼镜(SLO)成像系统]]
- [[视网膜区域|视网膜区域]]
- [[眼部伪影-睫毛-眼睑等|眼部伪影（睫毛、眼睑等）]]

## 相关主题

- [[医学图像分析|医学图像分析]]
- [[视网膜疾病诊断|视网膜疾病诊断]]
- [[图像伪影去除|图像伪影去除]]
- [[自动化图像分割|自动化图像分割]]

## 主要发现



- 该方法能有效排除睫毛、眼睑等成像伪影，整体分类准确率达到92%
- 去除伪影可提升视网膜疾病特征的自动检测效率，并支持多视角图像配准

## 方法细节

### 方法概述

本文提出了一种基于图像处理和机器学习的自动视网膜区域提取框架，用于从扫描激光检眼镜(SLO)图像中区分真实视网膜区域与伪影（如睫毛、眼睑）。该方法采用三阶段架构：训练阶段、测试评估阶段和部署阶段。核心创新在于使用超像素(SLIC算法)将像素分组为区域，以降低图像处理复杂度并生成便于处理的图像基元。系统提取纹理、灰度梯度和区域结构特征，通过特征选择算法筛选最相关特征，最终构建二分类器实现视网膜区域与伪影的自动判别。

### 数学公式


**公式1**: $$$I_{norm} = \left(\frac{I}{255}\right)^{\gamma}$$$

*Gamma校正公式，用于图像预处理阶段将图像强度值归一化到特定范围。其中I为原始图像强度值，γ为Gamma系数，Inorm为归一化后的图像强度。*


### 算法步骤

1. 图像数据整合：将SLO图像数据与人工标注的真实视网膜区域边界进行集成，建立训练集和测试集

2. 图像预处理：对图像进行强度归一化处理，将图像均值调整至目标值μtarget=80，并应用Gamma校正公式调整对比度

3. 超像素生成：采用简单线性迭代聚类(SLIC)算法将图像分割为约5000个超像素区域，基于区域大小和紧致度进行像素分组，平衡计算稳定性与预测精度

4. 特征生成：针对每个超像素提取三类特征：(1)纹理特征（基于红绿通道的多尺度高斯模糊）；(2)灰度梯度特征；(3)区域结构特征。蓝色通道因值为零被忽略

5. 特征选择：从大量特征集中筛选与分类最相关的特征子集，降低特征维度以提高分类器计算效率

6. 分类器构建：基于选定特征和人工标注标签构建二分类器，训练模型区分视网膜区域与伪影类别

7. 测试评估：对测试集图像进行自动标注，将分类结果与人工标注进行比对计算分类准确率

8. 部署应用：将训练好的模型用于新图像的视网膜区域自动提取，排除睫毛、眼睑等伪影干扰


### 关键参数

- **超像素数量**: 5000个（在计算稳定性与预测精度之间的折中选择）

- **预处理目标均值**: μtarget = 80（可视化优化设定值）

- **Gamma校正系数**: γ（根据具体图像调整）

- **特征提取通道**: 红色和绿色通道（蓝色通道设置为零，不参与特征计算）

- **高斯模糊尺度**: 多尺度平滑尺度（Multi-scale Gaussian blurring scales）



## 仿真结果

### 仿真测试

| 测试场景 | 结果描述 | 对比基线 |

|---------|---------|----------|

| 视网膜区域与伪影分类性能评估 | 在包含健康及患病视网膜图像的数据集上进行测试，分类器整体准确率达到92%。实验评估了特征选择前后分类器的性能差异，验证特征降维可有效提升计算效率同时保持较高精度 | 相比逐像素处理方法，基于超像素的区域处理方法显著降低了计算复杂度，特征向量生成效率与超像素数量(5000)成线性关系而非与图像像素总数相关 |

| 超像素分割效果验证 | 对比分水岭算法与SLIC算法，SLIC在区域紧致度和边界贴合度方面表现更优，且超像素数量可控（固定为5000），避免了分水岭算法在伪影区域生成过多碎片的问题 | 分水岭方法在伪影区域易产生过量超像素，而SLIC方法保持区域数量恒定，计算效率提升约20-30% |



## 量化发现

- 分类器整体准确率达到92%，基于选定特征子集的分类性能与完整特征集相当但计算时间显著减少
- 超像素数量设定为5000，此为计算稳定性与预测精度之间的最优折中值
- 图像预处理阶段将目标均值设定为80，适用于SLO图像可视化优化
- 特征提取基于红绿双通道多尺度高斯模糊，蓝色通道因SLO成像特性置零处理
- 数据集包含健康及患病视网膜图像，验证了方法在不同病理状态下的鲁棒性
- 超像素尺寸远大于像素级处理，特征向量维度降低为原像素数量的约1/1000（假设图像分辨率为数千万像素）


## 关键公式

### Gamma校正归一化公式

$$$I_{norm} = \left(\frac{I}{255}\right)^{\gamma}$$$

*用于图像预处理阶段，将SLO图像强度值归一化到标准范围，消除图像间光照强度差异，为后续超像素生成和特征提取提供统一的输入数据分布*



## 验证详情

- **验证方式**: 实验评估与对比验证（基于人工标注金标准）
- **测试系统**: Optos plc制造的扫描激光检眼镜(SLO)成像系统获取的宽视野(200°)视网膜图像数据集，包含健康及患病（多种视网膜疾病）病例
- **仿真工具**: 简单线性迭代聚类(SLIC)超像素算法、多尺度高斯滤波、基于纹理/灰度/结构的特征提取算法、特征选择算法（如PLS或SVM-based）、二分类器（具体分类器类型未明确说明，可能为SVM或PLS）
- **验证结果**: 所提框架在测试集上达到92%的分类准确率，能有效区分视网膜区域与睫毛、眼睑等伪影。超像素方法较像素级处理显著降低计算复杂度，特征选择进一步提升了分类效率。预处理的Gamma校正有效解决了SLO图像光照不均问题，为后续自动疾病特征检测和多视角图像配准提供了可靠的预处理基础
