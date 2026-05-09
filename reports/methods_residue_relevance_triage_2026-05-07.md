---
title: "Methods Residue Relevance Triage"
type: report
created: "2026-05-07"
scope: "wiki/methods pages with remaining substantive template residue after duplicate-convergence pass H"
---

# Methods Residue Relevance Triage

This triage changes the repair rule for the remaining `wiki/methods/` residue:
do not mechanically repair every page as a full method page. Remaining pages must
first be classified by EMT relevance and wiki value. Weakly related or generic
concepts should be collapsed into controlled entries or future merge targets, not
expanded.

Current scan basis:

- Remaining unprotected pages with substantive residue: 68.
- `protected` pages are excluded from ordinary shard work.
- Pages with only `high-value-link` marker noise are excluded from this triage.

## Tier A: EMT-Core, Keep But Converge

These pages name phenomena, components, modeling methods, or simulation modes
that are directly used in EMT studies. They should remain in the graph, but many
should be concise Chinese controlled entries pointing to canonical pages rather
than parallel full articles.

| Page | Rationale | Preferred action |
| --- | --- | --- |
| `wiki/methods/换相失败.md` | LCC-HVDC EMT phenomenon. | Controlled entry to `commutation-failure`, `concurrent-commutation-failure`, LCC/extinction-angle pages. |
| `wiki/methods/接地系统建模.md` | Grounding affects lightning and high-frequency EMT. | Controlled entry to grounding system model/topic pages. |
| `wiki/methods/新能源机组.md` | EMT studies of converter-based renewable units. | Controlled entry to renewable/IBR/wind/PV model pages. |
| `wiki/methods/时域电磁暂态仿真.md` | Direct EMT simulation term. | Controlled entry to `emt-simulation` and time-domain modeling pages. |
| `wiki/methods/晶闸管.md` | LCC/HVDC switching component. | Controlled component entry to thyristor/LCC pages. |
| `wiki/methods/晶闸管阀组.md` | LCC-HVDC valve group object. | Controlled entry to LCC/HVDC converter pages. |
| `wiki/methods/暂态过电压分析.md` | EMT overvoltage analysis. | Controlled entry to lightning/overvoltage/frequency-dependent line pages. |
| `wiki/methods/杆塔接地系统.md` | Lightning and tower-footing grounding EMT object. | Controlled entry to grounding and tower/line lightning pages. |
| `wiki/methods/特高压直流输电.md` | HVDC scenario and equipment context. | Controlled entry to HVDC/UHVDC pages. |
| `wiki/methods/电力电子变换器建模.md` | Core EMT modeling surface. | Controlled entry to power electronics modeling, inverter/converter model pages. |
| `wiki/methods/电力电子开关.md` | Switching-device modeling surface. | Controlled entry to switch modeling and power electronics pages. |
| `wiki/methods/电力电子换流器.md` | Converter EMT modeling object. | Controlled entry to converter/inverter/MMC pages. |
| `wiki/methods/电力电缆.md` | Cable EMT object. | Controlled entry to cable/frequency-dependent cable pages. |
| `wiki/methods/电报方程求解.md` | Transmission-line EMT mechanism. | Controlled entry to transmission-line theory and recursive convolution pages. |
| `wiki/methods/电磁暂态-emt-仿真.md` | Direct EMT alias. | Alias/control entry to `emt-simulation` and electromagnetic transient topic. |
| `wiki/methods/直流电容.md` | DC-link capacitor and converter EMT object. | Controlled entry to DC capacitor / converter energy-storage context. |
| `wiki/methods/直接接口技术.md` | Hybrid simulation interface method. | Controlled entry to `interface-technique` and hybrid simulation pages. |
| `wiki/methods/硬件在环-hil.md` | EMT real-time/HIL context. | Controlled entry to hardware-in-loop topic. |
| `wiki/methods/离散伴随支路等效.md` | EMT companion-circuit mechanism. | Controlled entry to companion-circuit / numerical integration pages. |
| `wiki/methods/网络等值技术.md` | EMT network equivalent modeling. | Controlled entry to network equivalent / FDNE pages. |
| `wiki/methods/背靠背变流器.md` | Converter topology in EMT studies. | Controlled entry to back-to-back converter/HVDC pages. |
| `wiki/methods/输电线路参数计算.md` | EMT line-parameter modeling. | Controlled entry to transmission line parameter / frequency-dependent line pages. |
| `wiki/methods/逆变器型资源-ibr.md` | Direct IBR alias. | Alias/control entry to `ibr` and inverter-based resource pages. |
| `wiki/methods/逆变器型资源.md` | Direct IBR Chinese term. | Alias/control entry to `ibr` and renewable/converter pages. |
| `wiki/methods/递归卷积.md` | Core line/cable EMT implementation method. | Controlled entry to `recursive-convolution`. |
| `wiki/methods/递归卷积法.md` | Duplicate Chinese term. | Alias to `递归卷积` / `recursive-convolution`. |
| `wiki/methods/阻抗特性分析.md` | EMT/control interaction and frequency-domain studies. | Controlled entry to impedance modeling / frequency-domain analysis. |
| `wiki/methods/阻抗稳定性分析.md` | Converter-grid EMT stability surface. | Controlled entry to impedance stability / harmonic interaction pages. |
| `wiki/methods/雷击感应电压.md` | Direct lightning EMT phenomenon. | Controlled entry to lightning-induced voltage topic. |
| `wiki/methods/频变电缆模型-fdcm.md` | Cable frequency-dependent model. | Controlled entry to frequency-dependent cable/cable model pages. |

## Tier B: EMT-Supporting, Do Not Expand

These are mathematically or computationally useful for EMT, but not EMT-specific.
They should not become broad standalone method articles. Keep as short controlled
entries only when they help disambiguate wiki links.

| Page | Rationale | Preferred action |
| --- | --- | --- |
| `wiki/methods/控制系统.md` | Generic control term, only relevant via EMT model interfaces. | Controlled entry to control-system, VSC control, PLL, power electronics control. |
| `wiki/methods/控制系统建模.md` | Generic control modeling term. | Controlled entry; avoid broad control-theory article. |
| `wiki/methods/数值效率优化.md` | Generic numerical-performance term. | Controlled entry to fast simulation / sparse solver / parallel computing. |
| `wiki/methods/数值积分算法.md` | Supporting EMT numerics. | Controlled entry to numerical integration methods. |
| `wiki/methods/时域建模.md` | Broad modeling term, relevant to EMT but not specific. | Controlled entry to time-domain modeling/EMT simulation. |
| `wiki/methods/暂态稳定仿真.md` | Primarily electromechanical; EMT only via hybrid simulation. | Controlled boundary entry to transient stability and hybrid simulation. |
| `wiki/methods/有限元法.md` | Field solver method, support for detailed component models. | Controlled entry to finite-element method; do not expand into FEM tutorial. |
| `wiki/methods/机电-电磁混合仿真技术.md` | Hybrid EMT/electromechanical workflow. | Controlled entry to hybrid simulation pages. |
| `wiki/methods/机电暂态仿真技术.md` | Electromechanical side, not EMT core. | Controlled boundary entry; avoid expansion. |
| `wiki/methods/机电暂态模型.md` | Electromechanical model side. | Controlled boundary entry to electromechanical model/topic. |
| `wiki/methods/模态解耦.md` | Mathematical line/model decomposition support. | Controlled entry to modal-domain decoupling and modal transformation. |
| `wiki/methods/次同步谐振.md` | Stability phenomenon that may use EMT studies. | Controlled entry to SSR/stability pages. |
| `wiki/methods/正负序分解法.md` | Sequence analysis support. | Controlled entry to sequence/signal/control pages. |
| `wiki/methods/混合仿真建模.md` | Broad hybrid-simulation support. | Controlled entry to hybrid simulation / interface pages. |
| `wiki/methods/混合求解架构.md` | Solver architecture, support not core domain. | Controlled entry to solver/co-simulation/sparse solver pages. |
| `wiki/methods/状态变量仿真.md` | Generic state-space simulation phrase. | Controlled entry to state-space modeling / EMT integration boundary. |
| `wiki/methods/状态空间平均法.md` / `wiki/methods/state-space-averaging.md` | Duplicate pages for an existing method. | Delete after redirecting backlinks to `state-space-average-method`; do not keep parallel variants. |
| `wiki/methods/电压均衡控制.md` | MMC/capacitor balancing support. | Controlled entry to MMC/submodule capacitor balancing pages. |
| `wiki/methods/电容电压均衡.md` | Duplicate of voltage balancing. | Alias/control entry; consider merge with voltage balancing. |
| `wiki/methods/电容电感储能元件.md` | Generic circuit element term. | Controlled entry to lumped RLC / energy storage element context. |
| `wiki/methods/矢量拟合-vf.md` | Supporting rational approximation method. | Alias to vector fitting; no new article. |
| `wiki/methods/硬件加速.md` | Generic computing support. | Controlled entry to FPGA/HIL/real-time acceleration; no broad hardware article. |
| `wiki/methods/离散傅里叶变换.md` | Generic signal-processing support. | Controlled entry to DFT/frequency-domain analysis. |
| `wiki/methods/移频相量法.md` | EMT-supporting shifted-frequency method. | Controlled entry to shifted-frequency analysis / dynamic phasor. |
| `wiki/methods/非线性分段线性元件.md` | EMT component approximation support. | Controlled entry to piecewise-linear and switch/nonlinear modeling. |
| `wiki/methods/非迭代求解.md` | Solver strategy support. | Controlled entry to non-iterative solver / companion-circuit boundary. |
| `wiki/methods/频域分析法.md` | Broad but common support analysis. | Controlled entry to frequency-domain analysis. |
| `wiki/methods/频域建模.md` | Broad modeling term. | Controlled entry to frequency-domain modeling / FDNE / vector fitting. |
| `wiki/methods/频移技术.md` | Supporting signal/model transformation. | Controlled entry to shifted-frequency analysis. |

## Tier C: Weak Or Generic, Prefer Merge Or Minimal Alias

These pages are weakly EMT-specific or too generic for a methods taxonomy. Do not
expand them. They should either become minimal disambiguation entries, be merged
into a canonical page, or eventually be removed from navigation after backlinks
are redirected.

| Page | Why weak | Preferred action |
| --- | --- | --- |
| `wiki/methods/浮点运算.md` | Generic computer arithmetic; current content is wrong pasted EMT boilerplate. | Minimal controlled entry to numerical precision / solver implementation, or merge into numerical solver discussion. |
| `wiki/methods/混合灵敏度优化.md` | Generic optimization/control phrase; no clear EMT canonical target. | Keep only if a source-backed EMT use exists; otherwise unresolved controlled entry. |
| `wiki/methods/灵活分组聚类.md` | Generic clustering phrase; not EMT-specific unless tied to equivalencing. | Merge/alias to coherency clustering or network equivalent if used. |
| `wiki/methods/水平接地极.md` | Component/object detail, not method; may belong under grounding model/topic. | Controlled object entry or merge into grounding-system pages. |
| `wiki/methods/绝缘子串.md` | Physical object, not method; relevant only for lightning/insulation studies. | Controlled object entry to insulator string model / lightning transient pages. |
| `wiki/methods/解析信号.md` | Generic signal-processing concept. | Alias to analytic-signal / shifted-frequency analysis only if backlinks need it. |
| `wiki/methods/解析信号构造.md` | Generic signal-processing process. | Merge/alias to analytic signal; do not expand. |
| `wiki/methods/计算加速.md` | Generic computing phrase. | Merge into fast-system-simulation/hardware acceleration; do not expand. |
| `wiki/methods/闭式近似公式.md` | Generic mathematical phrase; EMT relevance depends on existing source evidence. | Minimal unresolved entry only; do not create or imply new source pages. |

## Execution Rule For Remaining Work

1. Check the tier before editing.
2. For Tier A, preserve EMT semantics but still avoid duplicate full pages when a
   canonical page exists.
3. For Tier B, keep only boundary, links, and evidence constraints; do not add
   formulas or broad tutorials.
4. For Tier C, do not expand. Prefer alias, merge recommendation, or unresolved
   controlled entry.
5. Do not create new `sources/` pages; the source layer is fixed and can only be
   referenced as existing evidence.
6. After each batch, update `wiki/standards/page-revision-registry.md` and keep
   strict audit at zero.
