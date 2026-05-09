---
title: "Cross-Directory Convergence Triage"
type: report
created: "2026-05-08"
scope: "remaining unprotected wiki/methods residue after pass H, checked against models/topics/test-systems/sources"
---

# Cross-Directory Convergence Triage

This report supersedes a methods-only view of the remaining residue. The wiki is
a source-derived system with separate `sources/`, `methods/`, `models/`,
`topics/`, and `test-systems/` roles. A page left under `methods/` is not
automatically an EMT method. Many remaining pages are duplicate aliases,
model/object terms, topic/scenario terms, or generic support concepts.

Current repository shape:

- `wiki/sources/`: 682 source pages.
- `wiki/methods/`: 507 method-path pages.
- `wiki/models/`: 89 model pages.
- `wiki/topics/`: 90 topic pages.
- `wiki/test-systems/`: 22 test-system pages.
- Remaining unprotected `methods/` pages with substantive residue: 68.

## Directory Role Gate

Before editing any remaining `wiki/methods/` residue page, classify it by the
role it should play in the wiki:

| Target role | Use when | Action for a leftover `methods/` page |
| --- | --- | --- |
| method | Algorithm, numerical method, interface technique, signal-processing method, solver, or analysis procedure. | Keep as method only if it is not a duplicate of an existing canonical method page. |
| model | Device, component, physical object, converter, cable, grounding electrode, load, controller model. | Do not expand in `methods`; make a controlled entry pointing to `models/` or suggest future relocation. |
| topic | Research area, scenario class, stability phenomenon, EMT application domain. | Do not expand in `methods`; point to `topics/` synthesis page. |
| test-system | Named benchmark or system case. | Point to `test-systems/` if present; otherwise keep a controlled entry that explicitly says no benchmark owner exists. |
| source evidence | Paper-specific method name, year-author phrase, or claim from one existing source page. | Do not create source pages. Keep only a controlled entry that points to existing `sources/` evidence, or mark the evidence gap. |
| alias/disambiguation | Chinese synonym, acronym, overly broad phrase, or generic computation/control term. | Minimal controlled entry, no formulas, no performance claims, no broad tutorial. |

## Remaining Methods Pages By System Role

### A. Keep As Method-Oriented Controlled Entries

These can stay under `methods/`, but should still converge to existing canonical
pages when possible.

| Page | System role | Existing cross-directory anchors | Repair rule |
| --- | --- | --- | --- |
| `换相失败.md` | method/phenomenon entry | `methods/commutation-failure`, `methods/concurrent-commutation-failure`, LCC/HVDC source pages | Chinese controlled entry; no separate formulas beyond canonical page. |
| `数值积分算法.md` | method | `topics/numerical-integration-methods`, numerical-integration source pages | Controlled entry to numerical integration topic/methods. |
| `模态解耦.md` | method | modal transformation / modal-domain decoupling method pages | Controlled alias; avoid new line-model derivation. |
| `状态空间平均法.md` / `state-space-averaging.md` | duplicate method pages | canonical `methods/state-space-average-method`, dynamic-phasor/source pages | Delete duplicate pages after redirecting backlinks; do not keep parallel Chinese/English/method-suffix variants. |
| `直接接口技术.md` | method | `methods/interface-technique`, hybrid simulation topics/sources | Controlled entry; preserve hybrid-interface boundary. |
| `矢量拟合-vf.md` | method alias | `methods/vector-fitting`, vector-fitting sources | Alias only. |
| `离散傅里叶变换.md` | method support | frequency-domain topics and DFT/signal-processing methods | Controlled support entry, not a DSP tutorial. |
| `移频相量法.md` | method | `topics/shifted-frequency-analysis`, shifted-frequency source pages | Controlled entry to shifted-frequency analysis. |
| `递归卷积.md` | method | `methods/recursive-convolution`, line/cable sources | Keep as canonical or controlled method page. |
| `递归卷积法.md` | alias | `methods/recursive-convolution` | Alias to recursive convolution. |
| `非迭代求解.md` | method support | solver and companion-circuit pages | Controlled solver-strategy entry only. |
| `频域分析法.md` | method/topic bridge | `topics/frequency-domain-analysis`, frequency-domain sources | Controlled entry to topic, not broad tutorial. |
| `频域建模.md` | method/topic bridge | frequency-domain analysis, FDNE, vector fitting sources | Controlled entry with boundaries. |
| `频移技术.md` | method alias/support | `topics/shifted-frequency-analysis` | Controlled alias/support entry. |

### B. Model/Object Terms Misplaced In Methods

These are mainly devices, components, physical objects, or model objects. Do not
write them as independent method articles.

| Page | Better system role | Existing anchors | Repair rule |
| --- | --- | --- | --- |
| `接地系统建模.md` | model/topic | `models/grounding-system-model`, `topics/grounding-system`, grounding sources | Controlled entry to model/topic. |
| `新能源机组.md` | model/topic | `topics/renewable-energy-units`, `topics/renewable-energy-integration`, renewable sources | Controlled entry to renewable/IBR model/topic pages. |
| `晶闸管.md` | model/object | `methods/thyristor-control`, LCC/HVDC sources | Minimal component entry; do not expand device physics. |
| `晶闸管阀组.md` | model/object | LCC/HVDC converter sources | Controlled object entry; consider future model page if evidence supports. |
| `杆塔接地系统.md` | model/object | grounding model/topic, tower-footing grounding sources | Controlled entry to grounding model/topic. |
| `水平接地极.md` | model/object | grounding model/topic, grounding electrode sources | Controlled object entry or future merge into grounding model. |
| `电力电子变换器建模.md` | model/method bridge | `models/power-electronics-modeling`, `topics/power-electronics` | Controlled entry to model page. |
| `电力电子开关.md` | model/object | switch modeling and power electronics pages | Controlled object entry. |
| `电力电子换流器.md` | model/object | converter/inverter/MMC model pages | Controlled object entry. |
| `电力电缆.md` | model/object | `models/cable-model`, `topics/cable-modeling`, cable sources | Controlled entry to model/topic. |
| `直流电容.md` | model/object | `models/capacitor-model`, converter/MMC sources | Controlled object entry. |
| `电容电感储能元件.md` | model/object | capacitor/lumped RLC model context | Minimal controlled entry; no generic circuit tutorial. |
| `绝缘子串.md` | model/object | `models/insulator-string-model`, lightning/insulation sources | Controlled entry to model page. |
| `背靠背变流器.md` | model/object | back-to-back HVDC/converter pages | Controlled entry to converter/HVDC pages. |
| `逆变器型资源-ibr.md` | model/topic alias | `methods/ibr`, IBR source pages | Alias/control entry to IBR and model/topic pages. |
| `逆变器型资源.md` | model/topic alias | `methods/ibr`, IBR source pages | Alias/control entry to IBR and model/topic pages. |
| `非线性分段线性元件.md` | model/method support | piecewise-linear and nonlinear/switch modeling pages | Controlled entry; no standalone model expansion. |
| `频变电缆模型-fdcm.md` | model | cable/frequency-dependent cable pages | Controlled entry to cable model/topic. |

### C. Topic/Scenario Terms Misplaced In Methods

These are broad research directions, scenarios, or system-study contexts. They
should point to `topics/`, not become method pages.

| Page | Better system role | Existing anchors | Repair rule |
| --- | --- | --- | --- |
| `控制系统.md` | topic/model support | control models, VSC/PLL/control sources | Controlled disambiguation; not general control theory. |
| `控制系统建模.md` | topic/model support | controller model pages and control-system sources | Controlled entry to models/methods. |
| `时域建模.md` | topic | `topics/time-domain-modeling`, time-domain sources | Controlled entry to topic. |
| `时域电磁暂态仿真.md` | topic/method alias | EMT simulation and time-domain topics | Controlled entry to EMT/time-domain topics. |
| `暂态稳定仿真.md` | topic | `topics/transient-stability-analysis`, hybrid simulation sources | Boundary entry; mainly electromechanical except hybrid EMT use. |
| `暂态过电压分析.md` | topic | `topics/lightning-overvoltage`, `topics/grounding-lightning-overvoltage` | Controlled entry to overvoltage topics. |
| `机电-电磁混合仿真技术.md` | topic/method bridge | `topics/electromechanical-electromagnetic-hybrid-simulation`, `topics/hybrid-simulation` | Controlled entry to topic/interface pages. |
| `机电暂态仿真技术.md` | topic | `topics/electromechanical-transient` | Boundary entry; do not expand in methods. |
| `机电暂态模型.md` | topic/model | `models/electromechanical-model`, `topics/electromechanical-transient` | Controlled entry to model/topic. |
| `混合仿真建模.md` | topic/method bridge | `topics/hybrid-simulation`, hybrid simulation sources | Controlled entry to topic/interface pages. |
| `特高压直流输电.md` | topic/scenario | HVDC/UHVDC topics and sources | Controlled scenario/topic entry. |
| `电磁暂态-emt-仿真.md` | topic alias | `topics/electromagnetic-transient`, EMT simulation pages | Alias/control entry. |
| `硬件在环-hil.md` | topic | `topics/hardware-in-loop` | Controlled alias to topic. |
| `阻抗特性分析.md` | topic/method bridge | impedance sources, frequency-domain topic | Controlled entry to impedance/frequency-domain pages. |
| `阻抗稳定性分析.md` | topic/method bridge | impedance-based stability sources | Controlled entry; avoid unsupported stability claims. |
| `雷击感应电压.md` | topic/phenomenon | `topics/lightning-induced-voltage`, lightning sources | Controlled entry to topic. |

### D. Generic Support Terms: Do Not Expand

These are not EMT-domain pages in their own right. Keep only if backlinks need a
disambiguation page; otherwise they are candidates for merge/removal after
backlinks are redirected.

| Page | Why not a standalone EMT method | Preferred convergence |
| --- | --- | --- |
| `数值效率优化.md` | Generic performance phrase. | Point to fast-system simulation, sparse solver, parallel computing. |
| `有限元法.md` | Generic field solver. | Alias to finite-element method; mention EMT only as component-detail support. |
| `正负序分解法.md` | Generic sequence-analysis tool. | Controlled entry to power-quality/control/fault-analysis contexts. |
| `浮点运算.md` | Generic computer arithmetic; current content is template pollution. | Minimal entry or merge into numerical solver implementation notes. |
| `混合求解架构.md` | Generic solver architecture phrase. | Controlled entry to solver/co-simulation pages. |
| `混合灵敏度优化.md` | Generic optimization/control phrase. | Keep only if existing `sources/` pages support the exact EMT use; otherwise unresolved controlled entry. |
| `灵活分组聚类.md` | Generic clustering phrase. | Merge/alias to coherency clustering/network equivalent if backlinks require. |
| `状态变量仿真.md` | Generic state-space phrase. | Controlled entry to state-space modeling/numerical integration. |
| `电压均衡控制.md` | MMC/control subtopic, not broad method. | Alias to MMC capacitor balancing/control sources. |
| `电容电压均衡.md` | Duplicate voltage-balancing phrase. | Merge/alias to voltage balancing. |
| `硬件加速.md` | Generic computing term. | Controlled entry to HIL/FPGA/real-time acceleration. |
| `解析信号.md` | Generic signal-processing concept. | Alias only if needed for shifted-frequency/dynamic phasor links. |
| `解析信号构造.md` | Generic signal-processing process. | Merge/alias to analytic signal. |
| `计算加速.md` | Generic computing phrase. | Merge into fast-system-simulation/hardware acceleration. |
| `闭式近似公式.md` | Generic mathematical phrase. | Source-bound unresolved entry only. |

## Revised Execution Rule

For the remaining residue, the first edit decision is not "how do we improve
this methods page?" but "which part of the wiki system already owns this
concept?"

1. Check `models/`, `topics/`, `test-systems/`, and existing `sources/` before editing.
2. If a non-method page already owns the concept, make the `methods/` page a
   short controlled entry or merge recommendation.
3. Do not add new pages while cleaning residue, including new `sources/` pages.
4. Do not expand generic Tier D concepts.
5. Registry entries should record the target role: method, model, topic, source,
   or alias/disambiguation.
