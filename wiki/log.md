# EMT Wiki 日志

> 追加式记录，永不修改。每条以 `## [日期] 类型 | 标题` 开头。

## [2026-04-13] init | Wiki 初始化
- 创建目录结构：wiki/{topics,methods,models,entities,sources}, schema/, tools/
- 编写 schema/WIKI.md：定义 Wiki 结构、模板和工作流程
- 编写 tools/extract_metadata.py：PDF 元数据批量提取工具
- 提取全部 691 篇 PDF 元数据至 wiki/sources/metadata.json
- 创建概览页 wiki/overview.md
- 创建索引页 wiki/index.md
- 创建日志页 wiki/log.md
- 下一步：开始批量摄入各文件夹内容

## [2026-04-13] ingest | 文件夹 01 批量摄入
- 来源: EMT_Doc/01/ (21 篇论文)
- 创建来源页: 21
  a-guaranteed-passive-model-for-multi-port-frequency-dependent-network-equivalent.md, ahmed-等-a-computationally-efficient-continuous-model-for-the-modular-multilevel-.md, a-full-frequency-dependent-line-model-based-on-folded-line-equivalencing-and-lat.md, a-bridge-arm-module-based-fixed-admittance-adc-model-for-converters-in-emt-simul.md, chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas.md, untitled.md, a-bidirectional-interleaved-totem-pole-pfc-based-integrated-on-board-charger-for.md, huang-等-a-heterogeneous-multiscale-method-for-efficient-simulation-of-power-syst.md, a-flux-defined-pmsm-model-based-on-fea-results-for-real-time-emt-simulation.md, a-high-frequency-transformer-model-for-the-emtp-power-delivery-ieee-transactions.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 02 批量摄入（含标题修复）
- 来源: EMT_Doc/02/ (19 篇论文)
- 创建来源页: 27（含修复的 8 篇错误标题）
- 修复论文: Dennetière 2009 (EMTP-RV/FLUX3D), Hariri 2017 (PV集成), Jiang 2015 (多功串补), Kurokawa 2006 (线路参数), Morales 2023 (线缆参数), Rosołowski 1997 (距离保护), Shu 2018 (多速率MMC), Shu 2019 (多域联合仿真)
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 03 批量摄入（含标题修复）
- 来源: EMT_Doc/03/ (19 篇论文)
- 创建来源页: 19 → 修复 6 篇 DOI 风格文件名标题
- 修复论文: Mu 2014 (多速率EMT), Kong 2013 (后备保护), Noda 2012 (非线性EMT迭代), Xu 2015 (MMC建模综述), Shu 2018 (MMC多速率EMT), s0142 (频变线路效应)
- 同时修复: Guo 2021 (HVDC短路故障, 02文件夹误标题), Wang 2026 (新能源组件级建模, 01文件夹乱码)
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 04 批量摄入（含标题修复）
- 来源: EMT_Doc/04/ (21 篇论文)
- 创建来源页: 21 → 修复 9 篇错误标题 + 恢复 17 篇遗漏来源页
- 修复论文: Leal 2023 (Thévenin模域), Horton 2009 (电弧炉闪烁), Wang 2007 (电压暂态同步机), Moustafa 2012 (VSC-HVDC简化), Papagiannis 2005 (多层土壤线路效应), Lian 2010 (谐波潮流), Hussein 2013 (4型风电等值), Wu 2017 (磁滞变压器), Xu 2015 (MMC建模综述), Xiong 2024 (状态空间保持)
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] fix | 遗漏来源页恢复
- 自动扫描 folders 01-04，发现 17 篇缺失来源页并重建
- 从 PDF 第一页提取真实标题（替代 DOI 文件名）
- 总计 84 篇来源页 (01:21 + 02:22 + 03:20 + 04:21)

## [2026-04-13] ingest | 文件夹 05 批量摄入（含标题修复）
- 来源: EMT_Doc/05/ (21 篇论文)
- 创建来源页: 21 → 修复 3 篇错误标题 + 删除 1 篇重复
- 修复论文: Abusalah 2020 (稀疏矩阵加速EMT), Liu 2024 (油浸变压器温度自适应步长), Luo 2022 (直流配电谐振抑制)
- 去重: 1 篇重复论文 (accelerated frequency-dependent method, 同时存在于 1-s2.0-S0378 和 j.epsr DOI 文件)
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 06 批量摄入（含标题修复）
- 来源: EMT_Doc/06/ (16 篇论文)
- 创建来源页: 16 → 修复 3 篇错误标题
- 修复论文: Yang 2011 (永磁风机群等值聚合), TPWRD 2545922 (HVDC电缆温度场), Wideband Line/Cable建模 (HTML编码修复)
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 07&08 批量摄入（含标题修复）
- 来源: EMT_Doc/07&08/ (35 篇论文)
- 创建来源页: 35 → 修复 12 篇错误标题
- 修复论文: MMC增强平均值模型, Pantograph电弧模型, 高频白盒变压器, 低频GIC变压器, pi线路等值, 中国EMT仿真平台展望, EMTP截断误差分析, HVDC谐波传输, 中性点接地电阻, 云广UHVDC动态特性, 并联逆变器谐波, 混合线路电磁暂态
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 09 批量摄入（含标题修复）
- 来源: EMT_Doc/09/ (20 篇论文)
- 创建来源页: 20 → 修复 7 篇错误标题
- 修复论文: Cao 2006 (EMTP/UHV应用), Cao 2007 (EMTP-RV软件), AC-DC换流器平均值建模(HTML编码), pi电路电晕效应, 多芯变压器对偶电路, HVDC外环控制器参数, 小波熵保护
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 10 批量摄入（含标题修复）
- 来源: EMT_Doc/10/ (20 篇论文)
- 创建来源页: 20 → 修复 5 篇错误标题
- 修复论文: Guo 2020 (高频谐振特性), Sun 2014 (光机电磁暂态对比), Wang 2013 (直流低穿暂态对比), Li 2020 (容性限流器), Plumier 2016 (电磁暂态与相量联合仿真)
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 11 批量摄入（含标题修复）
- 来源: EMT_Doc/11/ (14 篇论文)
- 创建来源页: 14 → 修复 5 篇错误标题（期刊名替代论文名）
- 修复论文: 多虚拟同步机功率振荡抑制, 大电网仿真工具现状, 能量回馈型电力电子负载
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 12 批量摄入（含标题修复）
- 来源: EMT_Doc/12/ (13 篇论文)
- 创建来源页: 13 → 修复 5 篇错误标题（空标题/期刊名）
- 修复论文: 次同步控制互动阻尼(PV), 分布式光伏频率支撑, 模块化DAB直流变电站, 机电电磁混合仿真, IGBT详细建模
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 13&14 批量摄入（含标题修复）
- 来源: EMT_Doc/13&14/ (41 篇论文)
- 创建来源页: 41 → 修复 17 篇错误标题（空标题/期刊名/IEEE版权行）
- 修复论文: 距离保护频域辨识, 动态同步相量估计, LCC-HVDC动态平均化, RTDS-TSA混合仿真, 动态相量接口模型, 变压器对偶建模, 数字硬件EMU等
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 15 批量摄入（含标题修复）
- 来源: EMT_Doc/15/ (18 篇论文)
- 创建来源页: 18 → 修复 7 篇错误标题（IEEE版权行/期刊名/空标题）
- 修复论文: MMC高效建模, 超级电容储能仿真, CH-MMC快速仿真, 电力电子变压器加速仿真, 多端口频变网络等值
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 16 批量摄入（含标题修复）
- 来源: EMT_Doc/16/ (17 篇论文)
- 创建来源页: 17 → 修复 10 篇错误标题（空标题/期刊名），补建 2 篇遗漏页
- 修复论文: 级联H桥PET建模, UMEC Sen变压器, MMC-MTDC建模, STATCOM建模, 光伏解耦仿真, 直驱风电半隐式等
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 17 批量摄入（含标题修复）
- 来源: EMT_Doc/17/ (21 篇论文)
- 创建来源页: 21 → 修复 5 篇错误标题（期刊名替代论文名）
- 修复论文: VSC-MTDC机电电磁混合仿真, 水电风电混合仿真, MMC交直流混合仿真, 高铁牵引网建模, 机电电磁混合仿真方法
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 18 批量摄入（含标题修复）
- 来源: EMT_Doc/18/ (21 篇论文)
- 创建来源页: 21 → 修复 8 篇错误标题（期刊名/作者名/乱码）
- 修复论文: 频变模态域扩展, 快速电磁暂态仿真(Mu), 单相活动网络等值, 并联元件等值, 换相失败快速检测, 非隔离DC变压器
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 19、20、21 批量摄入（含标题修复）
- 来源: EMT_Doc/19、20、21/ (63 篇论文)
- 创建来源页: 63 → 修复 15 篇错误标题（期刊名/空标题/文件夹名替代）
- 修复论文: MMC高频振荡分析, 通用等值建模, 半波长暂态稳定, PMSG固定导纳建模, DC故障暂态模型, GPU并行算法等
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 22 批量摄入
- 来源: EMT_Doc/22/ (11 篇论文)
- 创建来源页: 11
  microsoft-word-small-signal-dynamic-phasor-3p-dab-for-sstfinal.md, impact-of-solenoid-effects-on-series-impedance-of-three-core-armoured-cables.md, hybrid-svc-vsc-modeling-approaches-for-hardware-in-the-loop-simulation.md, paper-title-use-style-paper-title.md, microsoft-word-small-signal-dynamic-phasor-3p-dab-for-sstfinal-22.md, high-speed-emt-modeling-of-mmcs-with-arbitrary-multiport-submodule-structures-us.md, impedance-based-stability-analysis-of-the-multi-terminal-cascaded-hybrid-hvdc-sy.md, hybrid-simulation-of-power-systems-with-svc-dynamic-phasor-model.md, hybrid-model-transient-stability-simulation-using-dynamic.md, hybrid-model-transient-stability-simulation-using-dynamic-22.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 23 批量摄入
- 来源: EMT_Doc/23/ (15 篇论文)
- 创建来源页: 15
  improved-accuracy-average-value-models-of-modular-multilevel-converters.md, implementation-of-modal-domain-transmission-line-models-in-the-atp-software.md, improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f.md, improving-numerical-efficiency-of-frequency-dependent-transmission-line-models-f-23.md, inaccuracies-due-to-the-frequency-warping-in-simulation-of-electrical-systems-us.md, improving-emt-simulations-using-frequency-shifted-rational-approximations.md, improvement-of-numerical-stability-for-the.md, improvement-of-numerical-stability-for-the-computation-of-transients-in-lines-an.md, improved-methods-for-optimization-of-power-systems-with-renewable-generation-usi.md, improved-control-systems-simulation-in-the-emtp-through-compensation.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 24 批量摄入
- 来源: EMT_Doc/24/ (11 篇论文)
- 创建来源页: 11
  influence-of-a-lossy-ground-on-the-lightning-performance-of-overhead-transmissio.md, initializing-emt-models-of-grid-forming-vscs-in-mtdc-systems.md, interfacing-factor-based-white-box-transformer.md, interfacing-techniques-for-transient-stability.md, wwwelseviercomlocateepsr.md, integrating-dynamic-soil-ionization-models-in-emtp-for-time-domain-simulation-of.md, influence-of-approximate-internal-impedance-formula-on-half-wavelength-transmiss.md, interfacing-real-time-and-offline-power-system-simulation-tools-using-udp-or-fpg.md, interfacing-techniques-for-transient-stability-24.md, interface-displacement-and-mapping-equivalence-based-hybrid-simulation-for-hvacd.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 25 批量摄入
- 来源: EMT_Doc/25/ (20 篇论文)
- 创建来源页: 20
  laplace-transform-inversion-through-the-theta-algorithm-for-power-system-emt-ana.md, machine-learning-reinforced-massively-parallel-transient-simulation-for-large-sc.md, lightning-induced-voltage-analysis-on-a-three-phase-compact-distribution-line-co.md, loewner-matrix-approach-for-modelling-fdnes-of-power-systems.md, key-technologies-and-prospects-for-electromagnetic-transient-parallel-simulation.md, lessons-learned-in-porting-offline-large-scale-power-system-simulation-to-real-t.md, interpolation-for-power-electronic-circuit-simulation-revisited-with-matrix-expo.md, massively-parallel-modeling-of-battery-energy-storage-systems-for-acdc-grid-high.md, power-system-technology.md, massively-parallel-implementation-of-ac-machine.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 26 批量摄入
- 来源: EMT_Doc/26/ (21 篇论文)
- 创建来源页: 21
  modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati.md, mitigation-of-subsynchronous-interactions-in-hybrid-acdc-grid-with-renewable-ene.md, modeling-of-cross-magnetization-effects-in-saturated-synchronous-machines-for-el.md, modal-domain-based-modeling-of-parallel.md, measurement-based-frequency-dependent-model-of-a-hvdc-transformer-for-electromag.md, modeling-of-a-modular-multilevel-converter-with-embedded-energy-storage-for-elec.md, modeling-a-mixed-residential-commercial-load-for-simulations-involving-large-dis.md, modeling-method-for-dfig-based-wind-farm-in-high-efficiency-real-time-electromag.md, modeling-and-application-of-dq-sequence-dynamic-phasors-under-unbalanced-ac-cond.md, modelica-based-simulation-of-electromagnetic-transients-using-dynao-current-stat.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 27&28 批量摄入
- 来源: EMT_Doc/27&28/ (40 篇论文)
- 创建来源页: 40
  msemt-an-advanced-modelica-library-for-power-system-electromagnetic-transient-st.md, mtof-a-novel-fpga-based-emt-toolbox-in-matlab.md, modeling-of-mmc-based-statcom-with-embedded-energy-storage-for-the-simulation-of.md, modeling-of-inductive-constant-power-load-for-electromagnetic-transient-simulati-27&28.md, modeling-of-overhead-transmission-lines-for-trapped-charge-discharge-rate-studie.md, modeling-synchronous-voltage-source-converters-in-transmission-system-planning-s.md, university-of-manitoba.md, modelling-of-circuit-breakers-in-the-electromagnetic-transients-program-power-sy.md, modelling-of-electromagnetic-transients-in-multi-unit-high-voltage-circuit-break.md, modelling-of-single-phase-nonuniform-transmission-lines-in-electromagnetic-trans.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 29 批量摄入
- 来源: EMT_Doc/29/ (10 篇论文)
- 创建来源页: 10
  nuclear-powered-hybrid-energy-system-for-clean-hydrogen-production-time-step-opt.md, numerically-efficient-average-value-model-for-voltage-source-converters-in-nodal.md, numerical-integration-by-the-2-stage-diagonally.md, 未知论文.md, 未知论文-29.md, 未知论文-29.md, on-site-measurement-of-the-hysteresis-curve-for-improved-modelling-of-transforme.md, on-a-new-approach-for-the-simulation-of-transients.md, on-fixed-point-iterations-for-the-solution-of-control-equations-in-power-systems.md, electric-power-automation-equipment-29.md
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 30 批量摄入
- 来源: EMT_Doc/30/ (13 篇论文)
- 创建来源页: 13
  parallel-in-time-simulation-algorithm-for-power-electronics-mmc-hvdc-system.md, optimized-high-frequency-white-box-transformer-model-for-implementation-in-atp-e.md, parallelization-of-emt-simulations-for-integration-of-inverter-based-resources.md, microsoft-word-parallel-emt-simulation-based-on-shared-memory-architecture-compu.md, paraemt-an-open-source-parallelizable-and-hpc-compatible-emt-simulator-for-large.md, parallel-massive-thread-electromagnetic-transient-simulation-on-gpu.md, parallelization-of-mmc-detailed-equivalent-model.md, parallel-computation-of-power-system-emts-through-polyphase-qmf-filter-banks.md, optimization-of-numerical-integration-methods-for-the-simulation-of-dynamic-phas.md, parallel-in-time-object-oriented-electromagnetic-transient-simulation-of-power-s.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 31 批量摄入
- 来源: EMT_Doc/31/ (16 篇论文)
- 创建来源页: 16
  power-converter-simulation-module-connected-to-the-emtp-power-systems-ieee-trans.md, partial-refactorization-techniques-for-electromagnetic-transient-simulations.md, passivity-enforcement-of-wideband-model-through-a-new-and-full-perturbation-form.md, phase-domain-model-of-twelve-phase-synchronous-machine-for-emtp-type-simulation.md, portal-analysis-approach-used-for-the-efficient-electromagnetic-transient-emt-si.md, performance-evaluation-of-communication-fabrics-for-offline-parallel-electromagn.md, passivity-enforcement-for-transmission-line-models.md, parametric-study-of-transient-electromagnetic-fields.md, partitioned-fitting-and-dc-correction-for-the-simulation-of-electromagnetic-tran.md, potential-risk-of-failures-in-switching-ehv-shunt-reactors.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 32 批量摄入
- 来源: EMT_Doc/32/ (17 篇论文)
- 创建来源页: 17
  real-time-digital-simulator-of-the-electromagnetic-transients-of-power-transmiss.md, protection-system-representation-in-the-electromagnetic-transients-program-power.md, real-time-fpga-rtds-co-simulator-for-power-systems.md, real-time-simulation-of-hybrid-modular-multilevel-converters-using-shifted-phaso.md, real-time-simulation-for-detailed-wind-turbine-model-based-on-heterogeneous-comp.md, real-time-simulation-of-power-system-electromagnetic-transients-on-fpga-using-ad.md, 未知论文-32.md, rational-approximation-of-frequency-domain-responses-by-vector-fitting-power-del.md, real-time-hil-emulation-of-drm-with-machine-learning-accelerated-wbg-device-mode.md, proximity-effect-in-fast-transient-simulations-of-an-underground-transmission-ca.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 33 批量摄入
- 来源: EMT_Doc/33/ (14 篇论文)
- 创建来源页: 14
  realization-of-rational-models-for-tower-footing-grounding-systems.md, real-time-simulation-with-an-industrial-dccb-controller-in-a-hvdc-grid.md, review-and-comparison-of-frequency-domain-curve-fitting-techniques-vector-fittin.md, reduced-order-dynamic-model-of-modular.md, reduced-order-and-simultaneous-solution-of-power-and-control-system-equations-in.md, real-time-transient-simulation-based-on-a-robust.md, 中-国-电-机-工-程-学-报-33.md, power-system-technology-33.md, 第45-卷-第6-期-电力系统保护与控制-vol45-no6.md, power-system-technology-33.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 34 批量摄入
- 来源: EMT_Doc/34/ (15 篇论文)
- 创建来源页: 15
  rmsx002b-augmenting-the-traditional-circuit-model-to-capture-pll-instability.md, revisiting-dynamic-phasors-and-their-efficacy-in-simulating-electric-circuits.md, 未知论文.md, sfa-emt-hybrid-simulation-of-power-systems-application-to-hvdc-systems.md, shifted-frequency-analysis-based-faster-than-real-time-simulation-of-power-syste.md, shooting-method-based-modular-multilevel-converter-initialization-for-electromag.md, shifted-frequency-analysis-emtp-multirate-simulation-of-power-systems.md, saturable-reactor-hysteresis-model-based-on-jilesatherton-formulation-for-ferror.md, robust-passivity-enforcement-scheme-for.md, 中-国-电-机-工-程-学-报.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 35 批量摄入
- 来源: EMT_Doc/35/ (15 篇论文)
- 创建来源页: 15
  sparse-solver-application-for-parallel-real-time-electromagnetic-transient-simul.md, splitting-state-space-method-for-converter-integrated-power-systems-emt-simulati.md, simulation-of-electromagnetic-transients-with-a-family-of-implicit-multi-step-os.md, stability-assessment-of-multi-rate-electromagnetic-transient-simulations.md, spurious-power-losses-in-modular-multilevel-converter-arm-equivalent-model.md, 未知论文-35.md, stability-evaluation-of-interpolation-extrapolation-and-numerical-oscillation-da.md, csee-journal-of-power-and-energy-systems-vol-11-no-3-may-2025.md, spurious-power-and-its-elimination-in-modular-multilevel-converter-models.md, simulation-of-electromagnetic-transients-with-modelica-accuracy-and-performance-.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 36 批量摄入
- 来源: EMT_Doc/36/ (12 篇论文)
- 创建来源页: 12
  suppression-of-numerical-oscillations-in-the-emtp-power-systems-power-systems-ie.md, state-equation-approximation-of-transfer-matrices-and-its-application-to-the-pha.md, structure-preserving-aggregation-method-for-doubly-fed-induction-generators-in-w.md, study-of-a-numerical-integration-method-using-the-compact-scheme-for-electromagn.md, stability-improved-network-partition-based-on-a-small-step-synthesis-model-for-e.md, supplementary-techniques-for-2s-dirk-based-emt-simulations.md, power-system-technology-36.md, 中-国-电-机-工-程-学-报-36.md, 电力系统电磁暂态实时仿真中并行算法的研究.md, 考虑死区特性的全桥型mmc状态空间平均化建模方法.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 37 批量摄入
- 来源: EMT_Doc/37/ (18 篇论文)
- 创建来源页: 18
  time-domain-modeling-of-external-systems-for-electromagnetic-transients-programs.md, three-phase-transformer-modelling-for-fast-electromagnetic-transient-studies-pow.md, switch-averaged-frequency-domain-simulation-of-photovoltaic-systems.md, the-fdload-model-for-accurate-frequency-dynamics-in-the-sfa-emt-simulator.md, the-impact-of-frame-transformations-on-power-system-emt-simulation.md, csee-journal-of-power-and-energy-systems-vol-8-no-2-march-2022.md, the-use-of-averaged-value-model-of-modular.md, the-use-of-averaged-value-model-of-modular-37.md, 未知论文-37.md, three-phase-adaptive-auto-reclosing-for-single-outgoing-line-of-wind-farm-based-.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 38 批量摄入
- 来源: EMT_Doc/38/ (10 篇论文)
- 创建来源页: 10
  tower-foot-grounding-model-for-emt-programs-based-on-transmission-line-theory-an.md, time-domain-modeling-of-a-subsea-buried-cable.md, transient-analysis-on-multiphase-transmission-line-above-lossy-ground-combining-.md, time-domain-coupling-model-for-nonparallel-frequency-dependent-overhead-multicon.md, time-domain-modeling-of-transmission-line-crossing-using-electromagnetic-scatter.md, time-domain-implementation-of-damping-factor-white-box-transformer-model-for-inc.md, transient-electromagnetic-power-compensationbased-adaptive-inertia-control-strat.md, time-delay-estimation-through-all-pass-functions-for-ulm-line-and-cable-models.md, 未知论文-38.md, coalitional-games-for-joint-co-tier-and-cross-tier-cooperative-spectrum-sharing-.md
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 39 批量摄入
- 来源: EMT_Doc/39/ (13 篇论文)
- 创建来源页: 13
  transmission-line-modeling-with-explicit-grounding-representation.md, using-tacs-functions-within-empt-to-teach-protective-relaying-fundamentals-power.md, wwwelseviercomlocateepsr.md, use-of-efficient-task-allocation-algorithm-for-parallel-real-time-emt-simulation.md, using-the-exact-equivalent-x03c0-circuit-of-transmission-lines-for-electromagnet.md, universal-decoupled-equivalent-circuit-models-of-solid-state-transformer-for-acc.md, unified-mana-based-load-flow-for-multi-frequency-hybrid-acdc-multi-microgrids.md, type-3-wind-turbine-generator-model-with-generic-high-level-control-for-electrom.md, ehv-ac-cables-and-hvdc-links-are-planned-on-the-french.md, transmission-line-model-for-variable-step-size-simulation-algorithms.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] ingest | 文件夹 40 批量摄入
- 来源: EMT_Doc/40/ (19 篇论文)
- 创建来源页: 19
  zfunction-convolution-in-ehv.md, z-tool-frequency-domain-characterization-of-emt-models-for-small-signal-stabilit.md, wideband-model-based-on-constant-transformation-matrix-and-rational-krylov-fitti.md, wave-function-and-multiscale-modeling-of-mmc-hvdc-system-for-wide-frequency-tran.md, validation-of-frequency-dependent.md, 中-国-电-机-工-程-学-报-40.md, 中-国-电-机-工-程-学-报-40.md, power-system-technology-40.md, 中-国-电-机-工-程-学-报-40.md, 中-国-电-机-工-程-学-报-40.md...
- 主题/方法/模型页: 待分析后创建

## [2026-04-13] analyze | LLM 分析 & Wiki 页面创建
- 分析 690 篇来源页，识别共同主题、方法、模型和实体
- 创建主题页 (6): 混合仿真、实时仿真、动态相量法、并行计算、频率相关建模、网络等值
- 创建方法页 (8): 矢量拟合、平均值模型、节点分析、状态空间法、数值积分、无源性强制、多速率方法、恒导纳模型
- 创建模型页 (9): MMC、输电线路、变压器、同步电机、VSC、FDNE、电缆、DFIG
- 创建实体页 (8): PSCAD/EMTDC、EMTP/EMTP-RV、ATP-EMTP、RTDS、Polytechnique Montreal、University of Manitoba、Manitoba Hydro
- 更新 index.md：反映全部 31 个新页面和 100% 摄入覆盖率
- 下一步：填充各来源页的"核心贡献"/"使用的方法"/"涉及的模型"等分析内容

## [2026-04-13] analyze | 规则分析 699 篇来源页
- 编写 tools/analyze_sources.py：基于标题关键词和 frontmatter 标签的规则分析
- 映射 40+ 标题关键词和 30+ 标签到现有分类体系（8方法、8模型、6主题）
- 处理 699 篇来源页，成功 649 篇，跳过 50 篇（无摘要）
- 自动填充：核心贡献、使用的方法、涉及的模型、相关主题、主要发现
- 生成中文摘要和贡献描述，支持 wikilink 自动链接
- 下一步：继续处理未处理的文件夹，完善来源页分析

## [2026-04-13] backrefs | 构建分类页来源论文引用
- 编写 tools/build_backrefs.py：自动收集来源页 wikilink 引用
- 更新 21 个主题/方法/模型页，添加"来源论文"章节
- 总计 565 条论文引用，23 个唯一 wikilink
- 引用最多的页面：transmission-line-model (56), mmc-model (73), real-time-simulation (52), frequency-dependent-modeling (52), parallel-computing (48)
- 下一步：继续处理未处理的文件夹

## [2026-04-14] expand | 补全 11 个缺失分类页
- 模型页 (2): lcc-model, pmsm-model
- 主题页 (5): vsc-hvdc, ferroresonance, cable-modeling, harmonic-analysis, wind-farm-modeling
- 方法页 (2): interpolation-method, prony-analysis
- 实体页 (2): gole (A.M. Gole, 曼尼托巴大学), mahseredjian (Jean Mahseredjian, 蒙特利尔理工学院)
- 分类页总数: 29 → 40
- 未解析 wikilink: 11 → 0 (全部解析)
- 更新 tools/build_backrefs.py：新增页面纳入自动构建

## [2026-04-14] llm-deep | LLM 深度内容分析 — 11 个分类页
- 编写 tools/deep_analyze_taxonomy.py：PDF 文本提取 → LLM 结构化分析 → checkpoint 保存
- 编写 tools/generate_enriched_page.py：从分析结果生成富化分类页（方法对比表、设备统计、验证分布、技术演进、关键发现）
- 已完成深度分析的分类页（11 页，共 494 篇论文）：
  | 页面 | 论文数 | 行数 |
  |------|--------|------|
  | mmc-model | 73 | 539 |
  | transmission-line-model | 56 | 463 |
  | transformer-model | 44 | 407 |
  | real-time-simulation | 52 | 339 |
  | frequency-dependent-modeling | 52 | 326 |
  | parallel-computing | 48 | 302 |
  | cable-model | 28 | 296 |
  | co-simulation | 46 | 287 |
  | dynamic-phasor | 37 | 251 |
  | vsc-model | 19 | 167+ |
  | dfig-model | 18 | 158+ |
  | average-value-model | 13 | 148+ |
- 分析工具支持 16 种分类 wikilink
- 论文 LLM 分析成功率: 486/486 = 100%
- 下一步：继续增强剩余分类页（synchronous-machine-model, fdne-model, 各方法页等）

## [2026-04-14] llm-deep | LLM 深度内容分析 — 第二批 6 个分类页
- 完成剩余 taxonomy 页面的 LLM 深度分析（6 页，共 25 篇论文）：
  | 页面 | 论文数 | 行数 |
  |------|--------|------|
  | synchronous-machine-model | 11 | 216 |
  | state-space-method | 8 | 108+ |
  | vector-fitting | 6 | 98+ |
  | numerical-integration | 5 | 88+ |
  | lcc-model | 4 | 67+ |
  | pmsm-model | 1 | 27+ |
- 在 deep_analyze_taxonomy.py 中新增 lcc-model 和 pmsm-model taxonomy 定义
- 所有 18 个分类页已完成 LLM 深度分析，累计 519 篇论文
- 论文 LLM 分析成功率: 519/519 = 100%
- 所有页面已提交并推送到 GitHub (chenyingthu/EMT_wiki.git)
