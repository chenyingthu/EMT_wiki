#!/usr/bin/env python3
"""
修复简化/缩写链接到完整页面名
"""

import re
import json
from pathlib import Path
from collections import defaultdict, Counter

WIKI_DIR = Path("/home/chenying/researches/EMT_LLM_Wiki/wiki")
SOURCES_DIR = WIKI_DIR / "sources"

# 简化名称到完整页面名的映射
ABBREV_TO_FULL = {
    # Topics
    'real-time': 'topics/real-time-simulation',
    'parallel': 'topics/parallel-computing',
    'transmission-line': 'topics/transmission-line-modeling',
    'state-space': 'methods/state-space-method',
    'frequency-dependent': 'topics/frequency-dependent-modeling',
    'hvdc': 'topics/vsc-hvdc',
    'wind-farm': 'topics/wind-farm-modeling',
    'transformer': 'topics/transformer-modeling',
    'mmc': 'models/mmc-model',
    'harmonic': 'topics/harmonic-analysis',
    'synchronous-machine': 'models/synchronous-machine-model',
    'passivity': 'methods/passivity-enforcement',
    'network-partitioning': 'topics/multirate-and-network-partitioning',
    'vsc': 'models/vsc-model',
    'fdne': 'models/fdne-model',
    'phase-domain-model': 'topics/phase-domain-modeling',
    'cable': 'topics/cable-modeling',
    'multirate': 'methods/multirate-method',
    'switching-function-method': 'methods/switching-function',
    'transient-stability': 'topics/transient-stability-analysis',
    'numerical-stability': 'topics/numerical-stability',
    'network-equivalent': 'topics/network-equivalent',
    'thevenin-norton-equivalent': 'methods/thevenin-norton-equivalent',
    'average-value-model': 'methods/average-value-model',
    'model-order-reduction': 'topics/model-order-reduction',
    'hil-simulation': 'topics/hil-simulation',
    'mtdc': 'models/mtdc-model',
    'large-scale-grid-simulation': 'topics/large-scale-grid-simulation',
    'fpga-real-time-simulation': 'topics/fpga-real-time-simulation',
    'bergeron-model': 'methods/bergeron-model',
    'modal-transformation': 'methods/modal-transformation',
    'vector-fitting': 'methods/vector-fitting',
    'co-simulation': 'topics/co-simulation',
    'dynamic-phasor': 'topics/dynamic-phasor',
    'emt': 'topics/emt-mathematical-foundation',
    'nodal-analysis': 'methods/nodal-analysis',
    'numerical-integration': 'methods/numerical-integration',
    'vsc-hvdc': 'topics/vsc-hvdc',
    'lcc': 'models/lcc-model',
    'dfig': 'models/dfig-model',
    'pmsm': 'models/pmsm-model',
    'induction-machine': 'models/induction-machine-model',
    'converter-transformer': 'models/converter-transformer-model',
    'pi-controller': 'methods/pi-controller',
    'pll': 'methods/pll-model',
    'distance-protection': 'methods/distance-protection',
    'differential-protection': 'models/differential-protection',
    'state-space-average-method': 'methods/state-space-average-method',
    'companion-circuit': 'methods/companion-circuit',
    'switching-function': 'methods/switching-function',
    'frequency-domain-modeling': 'topics/frequency-dependent-modeling',
    'electromechanical-electromagnetic-hybrid': 'topics/electromechanical-electromagnetic-hybrid-simulation',
    'ferroresonance': 'topics/ferroresonance',
    'lightning': 'topics/lightning-overvoltage',
    'grounding': 'topics/grounding-lightning-overvoltage',
    'wideband-modeling': 'topics/wideband-modeling',
    'switching-transient': 'topics/switching-transient',
    'microgrid': 'topics/microgrid-distribution-network',
    'load-modeling': 'topics/load-and-dg-modeling',
    'bess': 'models/bess-model',
    'solid-state-transformer': 'models/pet-sst-model',
    'gfl-inverter': 'models/gfl-inverter-model',
    'gfm-inverter': 'models/gfm-inverter-model',
    'igbt': 'models/igbt-model',
    'diode': 'models/diode-model',
    'thyristor': 'models/thyristor-model',
    'capacitor': 'models/capacitor-model',
    'inductor': 'models/inductor-model',
    'resistor': 'models/resistor-model',
    'circuit-breaker': 'models/circuit-breaker-model',
    'emi-filter': 'models/emi-filter-model',
    'grounding-system': 'models/grounding-system-model',
    'fault-impedance': 'models/fault-impedance-model',
    'droop-control': 'models/droop-control-model',
    'distance-relay': 'models/distance-relay',
    'energy-storage-converter': 'models/energy-storage-converter-model',
    'hybrid-converter': 'models/hybrid-converter-model',
    'coordinate-transformation': 'methods/coordinate-transformation',
    'park-transformation': 'methods/coordinate-transformation',
    'clarke-transformation': 'methods/coordinate-transformation',
    'dq-transformation': 'methods/coordinate-transformation',
    'abc-dq-transformation': 'methods/coordinate-transformation',
    'discretization': 'methods/discretization-methods',
    'trapezoidal-rule': 'methods/numerical-integration',
    'backward-euler': 'methods/numerical-integration',
    'gear-method': 'methods/numerical-integration',
    'interpolation': 'methods/interpolation-method',
    'linear-interpolation': 'methods/interpolation-method',
    'quadratic-interpolation': 'methods/interpolation-method',
    'dae-solver': 'methods/dae-solvers',
    'sparse-solver': 'methods/sparse-solver',
    'klu': 'methods/sparse-direct-solver-klu-mklu',
    'umfpack': 'methods/sparse-solver',
    'gmres': 'methods/iterative-solver',
    'bicgstab': 'methods/iterative-solver',
    'cg': 'methods/iterative-solver',
    'preconditioner': 'methods/preconditioning-techniques',
    'ilu': 'methods/preconditioning-techniques',
    'incomplete-lu': 'methods/preconditioning-techniques',
    'jacobian': 'methods/jacobian-computation',
    'newton-raphson': 'methods/newton-raphson-method',
    'fixed-point-iteration': 'methods/fixed-point-iteration',
    'explicit-integration': 'methods/explicit-integration',
    'implicit-integration': 'methods/implicit-integration',
    'partitioned-method': 'methods/partitioned-integration',
    'multirate-integration': 'methods/multirate-method',
    'subcycling': 'methods/subcycling-technique',
    'latency-insertion': 'methods/latency-insertion',
    'transmission-line-model': 'models/transmission-line-model',
    'cable-model': 'models/cable-model',
    'frequency-dependent-line': 'models/frequency-dependent-line-model',
    'fd-line': 'models/frequency-dependent-line-model',
    'wideband-line': 'models/wideband-line-model',
    'universal-line': 'models/universal-line-model',
    'marti-model': 'models/marti-line-model',
    'semlyen-model': 'models/semlyen-line-model',
    'noda-model': 'models/noda-line-model',
    'phase-domain-line': 'models/phase-domain-line-model',
    'modal-domain-line': 'models/modal-domain-line-model',
    'constant-parameter-line': 'models/constant-parameter-line-model',
    'distributed-parameter': 'methods/distributed-parameter-line',
    'lumped-parameter': 'methods/lumped-parameter-model',
    'pi-section': 'methods/pi-section-model',
    'bergeron': 'methods/bergeron-model',
    'single-phase-line': 'methods/single-phase-line-model',
    'three-phase-line': 'methods/balanced-three-phase-line',
    'transposed-line': 'methods/transposed-three-phase-line',
    'untransposed-line': 'methods/untransposed-line-model',
    'mutual-coupling': 'methods/mutual-coupling-model',
    'skin-effect': 'methods/skin-effect-modeling',
    'ground-return': 'methods/ground-return-model',
    'carson': 'methods/carson-ground-return',
    'pollaczek': 'methods/pollaczek-ground-return',
    'complex-depth': 'methods/complex-ground-return',
    'frequency-dependent-soil': 'methods/frequency-dependent-soil-model',
    'corona': 'methods/corona-model',
    'arc-model': 'methods/arc-model',
    'ideal-switch': 'methods/ideal-switch-model',
    '开关模型': 'methods/switch-modeling',
    'valve-model': 'models/thyristor-model',
    'igbt-model': 'models/igbt-model',
    'diode-model': 'models/diode-model',
    'thyristor-model': 'models/thyristor-model',
    'gto': 'models/gto-model',
    'mosfet': 'models/mosfet-model',
    '理想变压器': 'methods/ideal-transformer-equivalent',
    '饱和变压器': 'methods/saturation-transformer-model',
    'multi-winding-transformer': 'models/multi-winding-transformer',
    'three-phase-transformer': 'models/three-phase-transformer-model',
    'shell-form-transformer': 'models/shell-form-transformer',
    'core-form-transformer': 'models/core-form-transformer',
    'bctran': 'methods/bctran-transformer-model',
    'hybrid-transformer': 'models/hybrid-transformer-model',
    'unified-magnetic-equivalent-circuit': 'models/umec-transformer',
    'duality-based-model': 'models/duality-transformer-model',
    'topology-based-model': 'models/topology-transformer-model',
    'detailed-transformer': 'models/detailed-transformer-model',
    'saturable-core': 'methods/saturable-core-model',
    'hysteresis': 'methods/hysteresis-modeling',
    'preisach': 'methods/preisach-model',
    'jiles-atherton': 'methods/jiles-atherton-model',
    'virgin-curve': 'methods/virgin-curve-model',
    'inrush-current': 'methods/inrush-current-analysis',
    'ferroresonance-analysis': 'topics/ferroresonance',
    'geomagnetic-disturbance': 'methods/gic-analysis',
    'gic': 'methods/gic-analysis',
    'dc-offset': 'methods/dc-offset-modeling',
    'synchronous-generator': 'models/synchronous-machine-model',
    'round-rotor': 'models/round-rotor-machine',
    'salient-pole': 'models/salient-pole-machine',
    'v-curve': 'methods/v-curve-analysis',
    'capability-curve': 'methods/capability-curve',
    'swing-equation': 'methods/swing-equation',
    'equal-area-criterion': 'methods/equal-area-criterion',
    'transient-stability': 'topics/transient-stability-analysis',
    'small-signal-stability': 'topics/small-signal-stability',
    'voltage-stability': 'topics/voltage-stability',
    'frequency-stability': 'topics/frequency-stability',
    'excitation-system': 'methods/excitation-system',
    'avr': 'methods/excitation-system',
    'pss': 'methods/power-system-stabilizer',
    'governor': 'methods/turbine-governor-model',
    'turbine-model': 'methods/turbine-governor-model',
    'hydro-turbine': 'methods/hydro-turbine-model',
    'steam-turbine': 'methods/steam-turbine-model',
    'gas-turbine': 'methods/gas-turbine-model',
    'wind-turbine': 'methods/wind-turbine-model',
    'pitch-control': 'methods/pitch-control-system',
    'maximum-power-point-tracking': 'methods/mppt-control',
    'mppt': 'methods/mppt-control',
    'crowbar': 'methods/crowbar-protection',
    'chopper': 'methods/dc-chopper-model',
    'braking-resistor': 'methods/braking-resistor',
    'series-compensation': 'methods/series-compensation',
    'shunt-compensation': 'methods/shunt-compensation',
    'svc': 'models/svc-model',
    'statcom': 'models/statcom-model',
    'tcsc': 'models/tcsc-model',
    'upfc': 'models/upfc-model',
    'ipfc': 'models/ipfc-model',
    'facts': 'topics/facts-modeling',
    'custom-power': 'topics/custom-power-device',
    'dvr': 'models/dvr-model',
    'sssc': 'models/sssc-model',
    'active-filter': 'models/active-filter-model',
    'passive-filter': 'models/passive-filter-model',
    'harmonic-filter': 'models/harmonic-filter-model',
    'notch-filter': 'methods/notch-filter',
    'band-pass-filter': 'methods/band-pass-filter',
    'low-pass-filter': 'methods/low-pass-filter',
    'high-pass-filter': 'methods/high-pass-filter',
    'emt-modelica': 'tools/modelica-emt',
    'pscad': 'tools/pscad-emtdc',
    'emtp-rv': 'tools/emtp-rv',
    'atp': 'tools/atp-emtp',
    'rtds': 'tools/rtds',
    'opal-rt': 'tools/opal-rt',
    'hypersim': 'tools/hypersim',
    'powerfactory': 'tools/digsilent-powerfactory',
    'pss-e': 'tools/pss-e',
    'psat': 'tools/psat',
    'matlab': 'tools/matlab-simulink',
    'simulink': 'tools/matlab-simulink',
    'simpowersystems': 'tools/matlab-simpower',
    'plecs': 'tools/plecs',
    'ltspice': 'tools/ltspice',
    'psim': 'tools/psim',
    ' Saber': 'tools/saber',
    'ansys': 'tools/ansys-maxwell',
    'maxwell': 'tools/ansys-maxwell',
    'jmag': 'tools/jmag',
    'flux': 'tools/flux',
    'comsol': 'tools/comsol',
    'openmodelica': 'tools/openmodelica',
    'dymola': 'tools/dymola',
    'maple': 'tools/maple',
    'maplesim': 'tools/maplesim',
    'fmu': 'tools/fmi-fmu',
    'fmi': 'tools/fmi-standard',
    'tla': 'tools/tla-plus',
    'ieee-14-bus': 'test-systems/ieee-14-bus',
    'ieee-30-bus': 'test-systems/ieee-30-bus',
    'ieee-39-bus': 'test-systems/ieee-39-bus',
    'ieee-57-bus': 'test-systems/ieee-57-bus',
    'ieee-118-bus': 'test-systems/ieee-118-bus',
    'ieee-300-bus': 'test-systems/ieee-300-bus',
    'wscc-9-bus': 'test-systems/wscc-9-bus',
    'nordic-32': 'test-systems/nordic-32',
    'cigre-benchmark': 'test-systems/cigre-benchmark',
    '4-machine-2-area': 'test-systems/kundur-4-machine',
    'kundur': 'test-systems/kundur-4-machine',
    'western-system': 'test-systems/western-interconnect',
    'npc-converter': 'models/npc-converter-model',
    'anpc-converter': 'models/anpc-converter-model',
    't-type-converter': 'models/t-type-converter-model',
    'flying-capacitor': 'models/flying-capacitor-converter',
    'cascaded-h-bridge': 'models/chb-converter-model',
    'modular-multilevel-converter': 'models/mmc-model',
    'half-bridge-smb': 'models/half-bridge-smb',
    'full-bridge-smb': 'models/full-bridge-smb',
    'clamp-double-smb': 'models/clamp-double-smb',
    'nearest-level-control': 'methods/nearst-level-modulation',
    'nlm': 'methods/nearst-level-modulation',
    'sort-and-select': 'methods/sort-and-select-balancing',
    'carrier-based-pwm': 'methods/carrier-based-pwm',
    'spwm': 'methods/sinusoidal-pwm',
    'svpwm': 'methods/space-vector-pwm',
    'dpwm': 'methods/discontinuous-pwm',
    'third-harmonic-injection': 'methods/third-harmonic-injection',
    'selective-harmonic-elimination': 'methods/she-pwm',
    'she': 'methods/she-pwm',
    'optimized-pwm': 'methods/optimized-pwm',
    'hysteresis-control': 'methods/hysteresis-current-control',
    'predictive-control': 'methods/model-predictive-control',
    'mpc': 'methods/model-predictive-control',
    'deadbeat-control': 'methods/deadbeat-control',
    'repetitive-control': 'methods/repetitive-control',
    'resonant-control': 'methods/resonant-control',
    'pr-control': 'methods/proportional-resonant',
    'proportional-resonant': 'methods/proportional-resonant',
    'sliding-mode-control': 'methods/sliding-mode-control',
    'adaptive-control': 'methods/adaptive-control',
    'fuzzy-control': 'methods/fuzzy-control',
    'neural-network-control': 'methods/neural-network-control',
    'ai-control': 'methods/ai-based-control',
    'virtual-synchronous-generator': 'models/vsg-model',
    'vsg': 'models/vsg-model',
    'sync-power-controller': 'models/spc-model',
    'droop-controller': 'models/droop-control-model',
    'virtual-impedance': 'methods/virtual-impedance',
    'current-limiting': 'methods/current-limiting-control',
    'fault-ride-through': 'methods/fault-ride-through',
    'lvrt': 'methods/low-voltage-ride-through',
    'hvrt': 'methods/high-voltage-ride-through',
    'rocof': 'methods/rocof-analysis',
    'frequency-nadir': 'methods/frequency-nadir-analysis',
    'inertia-response': 'methods/inertia-emulation',
    'primary-frequency-response': 'methods/primary-frequency-control',
    'secondary-frequency-response': 'methods/secondary-frequency-control',
    'tertiary-control': 'methods/tertiary-control',
    'agc': 'methods/automatic-generation-control',
    'ace': 'methods/area-control-error',
    'tie-line-bias': 'methods/tie-line-bias-control',
    'economic-dispatch': 'methods/economic-dispatch',
    'optimal-power-flow': 'methods/optimal-power-flow',
    'opf': 'methods/optimal-power-flow',
    'scopf': 'methods/security-constrained-opf',
    'unit-commitment': 'methods/unit-commitment',
    'state-estimation': 'methods/state-estimation',
    'bad-data-detection': 'methods/bad-data-detection',
    'observability-analysis': 'methods/observability-analysis',
    'contingency-analysis': 'methods/contingency-analysis',
    'n-1-criterion': 'methods/n-1-security',
    'voltage-control': 'methods/voltage-control',
    'reactive-power-management': 'methods/reactive-power-control',
    'loss-minimization': 'methods/loss-minimization',
    'emergency-control': 'methods/emergency-control',
    'under-frequency-load-shedding': 'methods/ufls',
    'ufls': 'methods/under-frequency-load-shedding',
    'uvls': 'methods/under-voltage-load-shedding',
    'sps': 'methods/special-protection-scheme',
    'remedial-action': 'methods/remedial-action-scheme',
    'system-splitting': 'methods/system-splitting',
    'islanding': 'methods/intentional-islanding',
    'black-start': 'methods/black-start',
    'restoration': 'methods/system-restoration',
    'frequency-dependent-load': 'models/frequency-dependent-load',
    'zip-load': 'models/zip-load-model',
    'exponential-load': 'models/exponential-load-model',
    'polynomial-load': 'models/polynomial-load-model',
    'induction-motor': 'models/induction-motor-model',
    'synchronous-motor': 'models/synchronous-motor-model',
    'doubly-fed-machine': 'models/dfig-model',
    'dfim': 'models/dfig-model',
    'wound-rotor': 'models/wound-rotor-machine',
    'permanent-magnet-machine': 'models/pmsm-model',
    'switched-reluctance': 'models/switched-reluctance-model',
    'brushless-dc': 'models/bldc-model',
    'reluctance-machine': 'models/reluctance-machine-model',
    'sync-reluctance': 'models/synchronous-reluctance-model',
    'solar-pv': 'models/solar-pv-model',
    'photovoltaic': 'models/pv-array-model',
    'pv-panel': 'models/pv-panel-model',
    'fuel-cell': 'models/fuel-cell-model',
    'microturbine': 'models/microturbine-model',
    'diesel-generator': 'models/diesel-generator-model',
    'small-hydro': 'models/small-hydro-model',
    'biomass': 'models/biomass-generator-model',
    'geothermal': 'models/geothermal-model',
    'wave-energy': 'models/wave-energy-model',
    'tidal-energy': 'models/tidal-energy-model',
    'storage-system': 'models/energy-storage-model',
    'battery-model': 'models/battery-model',
    'lithium-ion': 'models/lithium-ion-battery',
    'lead-acid': 'models/lead-acid-battery',
    'flow-battery': 'models/flow-battery-model',
    'supercapacitor': 'models/supercapacitor-model',
    'flywheel': 'models/flywheel-model',
    'superconducting-magnetic': 'models/smes-model',
    'compressed-air': 'models/caess-model',
    'pumped-hydro': 'models/pumped-hydro-model',
    'power-electronics': 'topics/power-electronics-modeling',
    'power-quality': 'topics/power-quality-analysis',
    'flicker': 'methods/flicker-analysis',
    'voltage-sag': 'methods/voltage-sag-analysis',
    'voltage-swell': 'methods/voltage-swell-analysis',
    'voltage-interruption': 'methods/interruption-analysis',
    'unbalance': 'methods/unbalance-analysis',
    'harmonic-distortion': 'methods/thd-analysis',
    'thd': 'methods/total-harmonic-distortion',
    'interharmonics': 'methods/interharmonic-analysis',
    'notching': 'methods/notching-analysis',
    'noise': 'methods/noise-analysis',
    'dc-offset-voltage': 'methods/dc-offset-analysis',
    'rapid-voltage-change': 'methods/rvc-analysis',
    'mains-signaling': 'methods/mains-signaling-voltage',
    'emission-limit': 'methods/emission-limit-compliance',
    'immunity-testing': 'methods/immunity-test',
    'compatibility-level': 'methods/compatibility-level',
    'planning-level': 'methods/planning-level',
    'assessment-level': 'methods/assessment-level',
    'probabilistic-analysis': 'methods/probabilistic-analysis',
    'monte-carlo': 'methods/monte-carlo-simulation',
    'latin-hypercube': 'methods/latin-hypercube-sampling',
    'point-estimate': 'methods/point-estimate-method',
    'cumulant': 'methods/cumulant-method',
    'cornish-fisher': 'methods/cornish-fisher-expansion',
    'gram-charlier': 'methods/gram-charlier-expansion',
    'risk-assessment': 'methods/risk-assessment',
    'reliability-analysis': 'methods/reliability-analysis',
    'adequacy-assessment': 'methods/adequacy-assessment',
    'security-assessment': 'methods/security-assessment',
    'dynamic-security': 'methods/dynamic-security-assessment',
    'transient-security': 'methods/transient-security-assessment',
    'voltage-security': 'methods/voltage-security-assessment',
    'small-disturbance-security': 'methods/small-disturbance-security',
    'probabilistic-stability': 'methods/probabilistic-stability',
    'energy-function': 'methods/energy-function-method',
    'lyapunov': 'methods/lyapunov-stability',
    'direct-method': 'methods/direct-stability-method',
    'extended-equal-area': 'methods/eeac',
    'single-machine-equivalent': 'methods/sime',
    'clustering': 'methods/machine-clustering',
    'coherency': 'methods/coherency-analysis',
    'slow-coherency': 'methods/slow-coherency',
    'modal-analysis': 'methods/modal-analysis',
    'participation-factor': 'methods/participation-factor',
    'eigenvalue-analysis': 'methods/eigenvalue-analysis',
    'sensitivity-analysis': 'methods/sensitivity-analysis',
    'trajectory-sensitivity': 'methods/trajectory-sensitivity',
    'continuation-power-flow': 'methods/continuation-power-flow',
    'cpf': 'methods/continuation-power-flow',
    'pv-curve': 'methods/pv-curve-analysis',
    'qv-curve': 'methods/qv-curve-analysis',
    'voltage-collapse': 'methods/voltage-collapse-analysis',
    'bifurcation': 'methods/bifurcation-analysis',
    'saddle-node': 'methods/saddle-node-bifurcation',
    'hopf-bifurcation': 'methods/hopf-bifurcation',
    'limit-induced': 'methods/limit-induced-bifurcation',
    'induction-generator': 'models/induction-generator-model',
    'squirrel-cage': 'models/squirrel-cage-machine',
    'deep-bar': 'models/deep-bar-rotor-model',
    'double-cage': 'models/double-cage-rotor-model',
    'single-cage': 'models/single-cage-rotor-model',
    'wound-field': 'models/wound-field-machine',
    'separately-excited': 'models/separately-excited-machine',
    'self-excited': 'models/self-excited-machine',
    'series-wound': 'models/series-wound-machine',
    'shunt-wound': 'models/shunt-wound-machine',
    'compound-wound': 'models/compound-wound-machine',
    'universal-motor': 'models/universal-motor',
    'repulsion-motor': 'models/repulsion-motor',
    'hysteresis-motor': 'models/hysteresis-motor',
    'stepping-motor': 'models/stepping-motor',
    'synchro': 'models/synchro-model',
    'resolver': 'models/resolver-model',
    'induction-regulator': 'models/induction-regulator',
    'phase-shifter': 'models/phase-shifting-transformer',
    'pst': 'models/phase-shifting-transformer',
    'tcps': 'models/thyristor-controlled-pst',
    'ipfc': 'models/interline-power-flow-controller',
    'gupfc': 'models/generalized-upfc',
    'hpfc': 'models/hybrid-power-flow-controller',
    'genetic-algorithm': 'methods/genetic-algorithm',
    'ga': 'methods/genetic-algorithm',
    'particle-swarm': 'methods/particle-swarm-optimization',
    'pso': 'methods/particle-swarm-optimization',
    'differential-evolution': 'methods/differential-evolution',
    'ant-colony': 'methods/ant-colony-optimization',
    'simulated-annealing': 'methods/simulated-annealing',
    'tabu-search': 'methods/tabu-search',
    'evolutionary': 'methods/evolutionary-algorithm',
    'multi-objective': 'methods/multi-objective-optimization',
    'pareto-optimal': 'methods/pareto-optimization',
    'nsga': 'methods/nsga-ii',
    'weighted-sum': 'methods/weighted-sum-method',
    'epsilon-constraint': 'methods/epsilon-constraint',
    'goal-programming': 'methods/goal-programming',
    'fuzzy-optimization': 'methods/fuzzy-optimization',
    'interval-optimization': 'methods/interval-optimization',
    'robust-optimization': 'methods/robust-optimization',
    'stochastic-programming': 'methods/stochastic-programming',
    'chance-constrained': 'methods/chance-constrained',
    'two-stage': 'methods/two-stage-optimization',
    'benders-decomposition': 'methods/benders-decomposition',
    'dantzig-wolfe': 'methods/dantzig-wolfe-decomposition',
    'column-generation': 'methods/column-generation',
    'dynamic-programming': 'methods/dynamic-programming',
    'dp': 'methods/dynamic-programming',
    'approximate-dynamic': 'methods/adp',
    'reinforcement-learning': 'methods/reinforcement-learning',
    'q-learning': 'methods/q-learning',
    'actor-critic': 'methods/actor-critic',
    'deep-learning': 'methods/deep-learning',
    'neural-network': 'methods/neural-network',
    'cnn': 'methods/convolutional-network',
    'rnn': 'methods/recurrent-network',
    'lstm': 'methods/lstm-network',
    'gru': 'methods/gru-network',
    'transformer': 'methods/transformer-network',
    'attention': 'methods/attention-mechanism',
    'autoencoder': 'methods/autoencoder',
    'gan': 'methods/generative-adversarial-network',
    'vae': 'methods/variational-autoencoder',
    'rl': 'methods/reinforcement-learning',
    'transfer-learning': 'methods/transfer-learning',
    'meta-learning': 'methods/meta-learning',
    'few-shot': 'methods/few-shot-learning',
    'zero-shot': 'methods/zero-shot-learning',
    'contrastive-learning': 'methods/contrastive-learning',
    'self-supervised': 'methods/self-supervised-learning',
    'supervised-learning': 'methods/supervised-learning',
    'unsupervised-learning': 'methods/unsupervised-learning',
    'semi-supervised': 'methods/semi-supervised-learning',
    'ensemble': 'methods/ensemble-learning',
    'bagging': 'methods/bagging',
    'boosting': 'methods/boosting',
    'random-forest': 'methods/random-forest',
    'gradient-boosting': 'methods/gradient-boosting',
    'xgboost': 'methods/xgboost',
    'lightgbm': 'methods/lightgbm',
    'catboost': 'methods/catboost',
    'svm': 'methods/support-vector-machine',
    'support-vector': 'methods/support-vector-machine',
    'kernel-method': 'methods/kernel-method',
    'gaussian-process': 'methods/gaussian-process',
    'bayesian': 'methods/bayesian-inference',
    'mcmc': 'methods/mcmc-sampling',
    'gibbs-sampling': 'methods/gibbs-sampling',
    'metropolis-hastings': 'methods/metropolis-hastings',
    'hamiltonian-monte-carlo': 'methods/hmc',
    'variational-inference': 'methods/variational-inference',
    'expectation-propagation': 'methods/expectation-propagation',
    'belief-propagation': 'methods/belief-propagation',
    'loopy-bp': 'methods/loopy-belief-propagation',
    'mean-field': 'methods/mean-field-approximation',
    'laplace-approximation': 'methods/laplace-approximation',
    'importance-sampling': 'methods/importance-sampling',
    'rejection-sampling': 'methods/rejection-sampling',
    'slice-sampling': 'methods/slice-sampling',
    'nested-sampling': 'methods/nested-sampling',
}


def extract_wikilinks(content):
    """提取所有wiki链接 [[target|display]] 或 [[target]]"""
    pattern = r'\[\[([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'
    return re.findall(pattern, content)


def fix_links_in_file(filepath, dry_run=False):
    """修复单个文件中的缩写链接"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    fixed_count = 0
    fixed_links = []

    # 查找所有wiki链接
    pattern = r'\[\[([^\]]+?)(?:\\?\|([^\]]*?))?\]\]'

    def replace_link(match):
        nonlocal fixed_count
        target = match.group(1)
        display = match.group(2)

        # 检查目标是否在映射中
        if target in ABBREV_TO_FULL:
            new_target = ABBREV_TO_FULL[target]
            fixed_count += 1
            fixed_links.append((target, new_target))
            if display:
                return f'[[{new_target}|{display}]]'
            else:
                return f'[[{new_target}]]'

        return match.group(0)

    new_content = re.sub(pattern, replace_link, content)

    if fixed_count > 0 and not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return fixed_count, fixed_links, new_content != original_content


def main():
    import argparse
    parser = argparse.ArgumentParser(description='修复缩写链接到完整页面名')
    parser.add_argument('--dry-run', action='store_true', help='仅预览，不实际修改')
    parser.add_argument('--file', type=str, help='仅处理指定文件')
    args = parser.parse_args()

    # 统计映射覆盖率
    print("=" * 60)
    print("缩写链接修复工具")
    print("=" * 60)
    print(f"\n映射字典包含 {len(ABBREV_TO_FULL)} 个缩写术语")
    print()

    if args.file:
        # 处理单个文件
        filepath = Path(args.file)
        if not filepath.exists():
            print(f"文件不存在: {filepath}")
            return

        fixed, links, changed = fix_links_in_file(filepath, args.dry_run)
        print(f"处理文件: {filepath}")
        print(f"修复链接数: {fixed}")
        if links:
            print("\n修复详情:")
            for old, new in links:
                print(f"  [[{old}]] → [[{new}]]")
    else:
        # 批量处理所有来源页
        source_files = list(SOURCES_DIR.glob("*.md"))
        print(f"扫描 {len(source_files)} 个来源页...")
        print()

        total_fixed = 0
        processed = 0
        all_fixed = []

        for filepath in source_files:
            try:
                fixed, links, changed = fix_links_in_file(filepath, args.dry_run)

                if fixed > 0:
                    total_fixed += fixed
                    all_fixed.extend(links)
                    processed += 1
                    if processed % 100 == 0:
                        action = "预览" if args.dry_run else "处理"
                        print(f"{action}进度: {processed}/{len(source_files)} 文件，已修复 {total_fixed} 个链接")

            except Exception as e:
                print(f"错误处理 {filepath}: {e}")

        print()
        print("=" * 60)
        if args.dry_run:
            print("📋 预览模式 - 未实际修改文件")
        else:
            print("✅ 修复完成！")
        print("=" * 60)
        print(f"处理文件数: {processed}")
        print(f"修复链接数: {total_fixed}")

        if all_fixed:
            print()
            print("修复摘要（前30）:")
            summary = Counter(f"{old} → {new}" for old, new in all_fixed)
            for mapping, count in summary.most_common(30):
                print(f"  {mapping}: {count}次")


if __name__ == "__main__":
    main()
