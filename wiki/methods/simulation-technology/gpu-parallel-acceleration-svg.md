<div style="text-align:center;margin:16px 0;">
<svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
    <marker id="arrow-red" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#dc2626"/>
    </marker>
  </defs>
  
  <!-- Title -->
  <text x="450" y="28" text-anchor="middle" font-size="16" font-weight="bold" fill="#333">GPU 并行 EMT 仿真架构</text>
  
  <!-- CPU Host Box -->
  <rect x="30" y="50" width="200" height="440" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="2"/>
  <text x="130" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#2563eb">CPU Host</text>
  
  <!-- Host tasks -->
  <rect x="50" y="90" width="160" height="45" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="130" y="108" text-anchor="middle" font-size="11" fill="#333">系统数据加载</text>
  <text x="130" y="123" text-anchor="middle" font-size="11" fill="#333">Power Flow 初始化</text>
  
  <rect x="50" y="150" width="160" height="40" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="130" y="167" text-anchor="middle" font-size="11" fill="#333">符号因子化 (Y矩阵)</text>
  <text x="130" y="182" text-anchor="middle" font-size="10" fill="#666">仅结构变化时执行</text>
  
  <rect x="50" y="205" width="160" height="40" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="130" y="222" text-anchor="middle" font-size="11" fill="#333">结果后处理与输出</text>
  
  <rect x="50" y="260" width="160" height="40" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1" stroke-dasharray="4,2"/>
  <text x="130" y="277" text-anchor="middle" font-size="11" fill="#dc2626">网络拓扑变化检测</text>
  <text x="130" y="292" text-anchor="middle" font-size="10" fill="#dc2626">故障/开关事件</text>
  
  <rect x="50" y="320" width="160" height="40" rx="4" fill="#ffffff" stroke="#2563eb" stroke-width="1"/>
  <text x="130" y="337" text-anchor="middle" font-size="11" fill="#333">BNA 节点映射</text>
  <text x="130" y="352" text-anchor="middle" font-size="10" fill="#666">块对角重组</text>
  
  <!-- PCIe Arrow -->
  <line x1="230" y1="280" x2="320" y2="280" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="275" y="270" text-anchor="middle" font-size="10" fill="#666">PCIe</text>
  
  <!-- GPU Device Box -->
  <rect x="330" y="50" width="540" height="440" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="600" y="75" text-anchor="middle" font-size="13" font-weight="bold" fill="#16a34a">GPU Device (CUDA)</text>
  
  <!-- GPU Memory -->
  <rect x="350" y="90" width="500" height="50" rx="4" fill="#ffffff" stroke="#16a34a" stroke-width="1"/>
  <text x="600" y="108" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">全局内存 (Global Memory)</text>
  <text x="600" y="125" text-anchor="middle" font-size="10" fill="#666">Y 矩阵 · 节点电压 · 历史电流 · 系统参数 (驻留设备侧)</text>
  
  <!-- Time Step Loop -->
  <rect x="350" y="155" width="500" height="250" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="600" y="178" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">每个时间步 Δt 循环</text>
  
  <!-- Kernel 1: Update Current Sources -->
  <rect x="370" y="190" width="220" height="55" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="480" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">Kernel 1: 电流源更新</text>
  <text x="480" y="223" text-anchor="middle" font-size="10" fill="#666">并行更新非动态元件历史电流</text>
  <text x="480" y="238" text-anchor="middle" font-size="10" fill="#666">SIMT · FMA 操作</text>
  
  <!-- Kernel 2: Generator Model -->
  <rect x="610" y="190" width="220" height="55" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="720" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">Kernel 2: 发电机求解</text>
  <text x="720" y="223" text-anchor="middle" font-size="10" fill="#666">求解励磁/阻尼绕组方程</text>
  <text x="720" y="238" text-anchor="middle" font-size="10" fill="#666">补偿法接口非线性</text>
  
  <!-- Kernel 3: Passive Elements -->
  <rect x="370" y="260" width="220" height="55" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="480" y="278" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">Kernel 3: 无源元件更新</text>
  <text x="480" y="293" text-anchor="middle" font-size="10" fill="#666">RLC 支路伴生模型更新</text>
  <text x="480" y="308" text-anchor="middle" font-size="10" fill="#666">ULM 卷积/插值 (4阶段)</text>
  
  <!-- Kernel 4: Network Solve -->
  <rect x="610" y="260" width="220" height="55" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
  <text x="720" y="278" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">Kernel 4: 网络求解</text>
  <text x="720" y="293" text-anchor="middle" font-size="10" fill="#666">cuDSS 前代/后代</text>
  <text x="720" y="308" text-anchor="middle" font-size="10" fill="#666">Woodbury 公式 (k 变化)</text>
  
  <!-- Arrows between kernels -->
  <line x1="590" y1="217" x2="610" y2="217" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="480" y1="245" x2="480" y2="260" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="590" y1="287" x2="610" y2="287" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)"/>
  
  <!-- GPU Arrows back to Host -->
  <line x1="330" y1="280" x2="240" y2="280" stroke="#666" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="285" y="270" text-anchor="middle" font-size="10" fill="#666">PCIe</text>
  
  <!-- GPU Shared Memory -->
  <rect x="350" y="420" width="500" height="50" rx="4" fill="#ede9fe" stroke="#7c3aed" stroke-width="1"/>
  <text x="600" y="438" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">共享内存 (Shared Memory, 48 kB/block)</text>
  <text x="600" y="455" text-anchor="middle" font-size="10" fill="#666">ULM 矩阵运算 · LPE 电流注入 · UMM 向量化计算</text>
  
  <!-- GPU Architecture Note -->
  <rect x="350" y="480" width="500" height="5" rx="2" fill="#16a34a" opacity="0.3"/>
  <text x="600" y="495" text-anchor="middle" font-size="9" fill="#666">SM (Streaming Multiprocessor) → Warp (32 threads) → CUDA Core | SIMT 执行模式</text>
</svg>
</div>
<p style="text-align:center;font-size:12px;color:#666;margin-top:8px;">图1 · GPU 并行 EMT 仿真架构：CPU Host 与 GPU Device 的数据流与 kernel 执行流程</p>