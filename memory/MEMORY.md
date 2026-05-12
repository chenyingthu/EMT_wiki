- [reading-notes-hbsm](reading-notes-hbsm.md) — HBSM半桥子模块EMT建模，覆盖Gao 2023混合积分、Zhang 2023同步预判、Xu 2015综述、Xu 2018二极管钳位四种建模路线
- [reading-notes-hierarchical-control](reading-notes-hierarchical-control.md) — 分层控制EMT建模，覆盖Nguyen 2021 GFM黑启动、Nurunnabi 2025 PQ能力、Rashidirad 2023多微电网、Liu 2010云广UHVDC四种场景
- [reading-notes-chb-dab](reading-notes-chb-dab.md) — CHB-DAB级联H桥双有源桥PET建模，覆盖Xu 2025 GSSA状态平均、Wang 2025多速率、许明旺2023半隐式解耦、丁江萍2022等效电路、Qi 2024实时聚合五条路线
- [reading-notes-inertia-control](reading-notes-inertia-control.md) — 惯量控制EMT建模，覆盖Hu 2025 VSG自适应惯量+暂态补偿、林继灿2023多VSG一致性互阻尼、姜继恒2024风电多时间尺度等效惯量三类场景
- [reading-notes-dc-fcl](reading-notes-dc-fcl.md) — DC-FCL直流故障限流器EMT建模，覆盖Li 2020电抗器+电容协同配置、Li 2019 CL-DCCB电感切换限流、Shen & Dinavahi 2019 CDSM自限流三种路线
- [reading-notes-mppt-control](reading-notes-mppt-control.md) — MPPT控制EMT建模，覆盖Trevisan 2018风能最优转速励磁MPPT、Hariri & Faruque 2016光伏增量电导法MPPT、Di Fazio & Russo 2012 PV数值稳定性三种路线

- [reading-notes-dual-active-bridge](reading-notes-dual-active-bridge.md) — Qi 2024实时聚合+DAB高频IFP、Berger 2018 GSSA 3p-DAB、Gao 2023端口分析DAB验证、Xu 2024 N端口DAB等效

- [reading-notes-lvrt-control](reading-notes-lvrt-control.md) — Mu 2019 DFIG仿真步长10x+Crowbar统一等效、Schwanka Trevisan 2018全功率风机FRT场测验证、高峰2022 PMSG机电暂态LVRT

- [reading-notes-nearest-level-modulation](reading-notes-nearest-level-modulation.md) — Zhao 2023电压闭环NLM等效(0-500Hz误差<0.5%, 15-40x加速)、Yu 2014平均比较均衡(~5000x加速)、Lian 2022双向堆排序(O(K log K))、Xu 2015综述三路线

- [reading-notes-srf-pll](reading-notes-srf-pll.md) — Carreño 2026 SRF-PLL双模失稳(跨临界+Hopf分岔)、Ranasinghe 2024 DSOGI-PLL基线(ωc=62rad/s, SCR 2.3→1.0)、Luchini 2023 ATP等效模型(Kp=0.8, Ki=61.69)、Guilherme 2023 PLL初始化(θ̂=θ+∠H(jω))
- [reading-notes-half-bridge-submodule](reading-notes-half-bridge-submodule.md) — HBSM EMT建模四层级(开关级/戴维南等效/混合积分/AVM)，覆盖Zhang 2023同步预判(80模块SST·20x加速)、Gao 2023混合积分(5~15x加速·稳态误差<0.5%)、Xu 2015综述(梯形vs后退欧拉偏差0.2~0.4%)、Xu 2018二极管钳位自均压, Lai 2026 GaN ADC模型
- [reading-notes-control-system](reading-notes-control-system.md) — EMT控制系统接口方法，覆盖Lefebvre & Mahseredjian 1994补偿法(消除接口一步延迟)、de León 2011 SSN联合求解、Mengjia & Xiao 2015 HVDC频率控制(CCT+22.93%)、Guo 2022 MMC高频振荡(165μs延时阈值·阻尼控制相位差185°→177°)
- [reading-notes-pet](reading-notes-pet.md) — PET四篇核心来源:Gao 2022 Kron消去端口等效(10-100x加速), Wang 2025多速率CHB-DAB分区(步长比10:1-20:1), Li 2025开关函数解耦(大步长<0.5%偏差), Li 2026 ImEx-Gear实时仿真(171x加速·<0.5%稳态误差)
- [reading-notes-frequency-scan](reading-notes-frequency-scan.md) — 频扫四篇核心来源:Jiang 2025 dq0多频扫CSCR=3.7/1.15Hz, Meng 2023 CSD-scan 108Hz谐振+镜像12Hz/p-scan误判, Fan 2023高斯脉冲200→2次实验/σ=0.01s覆30Hz, Cifuentes 2025 Z-tool多端AC/DC 3×3导纳
