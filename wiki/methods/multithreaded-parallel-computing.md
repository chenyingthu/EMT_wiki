---
title: "多线程并行计算 (Multithreaded Parallel Computing)"
type: method
tags: [multithreading, openmp, parallel, cpu, shared-memory]
created: "2026-05-02"
---

# 多线程并行计算 (Multithreaded Parallel Computing)

## 概述

多线程并行计算是利用多核CPU的共享内存架构，通过多个线程同时执行来提高计算效率的技术。在电力系统EMT仿真中，多线程并行能够有效利用现代多核处理器，加速大规模系统的仿真计算。

## 基本架构

### 共享内存
- **多核CPU**: 共享地址空间
- **缓存一致**: 硬件保证
- `shared-memory` - 共享内存
- **NUMA**: 非均匀内存访问
- `numa` - NUMA架构

### 线程模型
- **Pthreads**: POSIX线程
- `pthreads` - Pthreads
- **OpenMP**: 编译制导
- `openmp` - OpenMP
- **TBB**: Intel线程库
- `tbb` - TBB

## 并行计算理论基础

### Amdahl定律

Amdahl定律描述了并行计算的理论加速上限，由Gene Amdahl于1967年提出。

**公式**:
$$S_{\text{latency}}(s) = \frac{1}{(1-p) + \frac{p}{s}}$$

其中：
- $S$: 加速比
- $p$: 可并行化部分的比例（0 < p < 1）
- $s$: 处理器数量
- $(1-p)$: 串行部分比例

**关键洞察**:
- 当 $s \to \infty$ 时，$S_{\text{max}} = \frac{1}{1-p}$
- 即使使用无限多处理器，加速比也受限于串行部分
- 若10%代码必须串行执行，最大加速比为10倍

**示例计算**:
- 95%可并行化($p=0.95$)：最大加速比 = 1/(1-0.95) = **20倍**
- 90%可并行化($p=0.90$)：最大加速比 = 1/(1-0.90) = **10倍**
- 50%可并行化($p=0.50$)：最大加速比 = 1/(1-0.50) = **2倍**

`amdahl-law` - Amdahl定律

### Gustafson定律

Gustafson定律（1988年）提供了不同的视角，强调问题规模随处理器增加而扩展。

**公式**:
$$S_{\text{latency}} = s - \alpha(s-1)$$

其中：
- $s$: 处理器数量
- $\alpha$: 串行时间比例（$\alpha = 1-p$）

**与Amdahl定律的区别**:
- Amdahl定律：固定问题规模，增加处理器
- Gustafson定律：问题规模随处理器线性增长
- Gustafson定律表明并行计算的可扩展性更好

**缩放加速比**:
$$S_{\text{scaled}} = \alpha + s(1-\alpha)$$

对于大规模EMT仿真，当问题规模随核心数增加时，Gustafson定律更适用。

`gustafson-law` - Gustafson定律

### 并行效率度量

**加速比**:
$$\text{Speedup} = \frac{T_1}{T_s}$$

**效率**:
$$\text{Efficiency} = \frac{\text{Speedup}}{s} = \frac{T_1}{s \cdot T_s}$$

**可扩展性效率**:
$$\text{Scale Efficiency} = \frac{T_1(s)}{s \cdot T_s}$$

其中$T_1(s)$是在单处理器上执行规模为$s$问题的时间。

**理想目标**:
- 加速比 ≈ $s$（线性加速）
- 效率 > 80%（良好并行）
- 效率 > 60%（可接受）
- 效率 < 50%（需要优化）

## OpenMP编程详细指南

### 并行区域指令

#### 基本并行区域
```c
#pragma omp parallel
{
    // 并行区域 - 每个线程执行相同代码
    int thread_id = omp_get_thread_num();
    int num_threads = omp_get_num_threads();
    printf("Thread %d of %d\n", thread_id, num_threads);
}
```

#### 带子句的并行区域
```c
#pragma omp parallel default(none) \n    shared(data, n) private(i, sum) \n    num_threads(8)
{
    // 控制数据作用域
    // default(none): 必须显式声明所有变量
    // shared: 所有线程共享
    // private: 每个线程私有副本
}
```

### 循环并行化

#### 基本for指令
```c
#pragma omp parallel for
for (int i = 0; i < n; i++) {
    result[i] = compute(data[i]);
}
```

#### 带调度策略的循环
```c
#pragma omp parallel for \n    schedule(static, 64)      // 静态块调度，块大小64
    // schedule(dynamic, 32)   // 动态调度
    // schedule(guided, 16)    // 导向调度
    // schedule(auto)          // 编译器决定
    // schedule(runtime)       // 运行时环境变量决定
```

#### 归约操作
```c
// 标量归约
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < n; i++) {
    sum += array[i];
}

// 多操作符归约
#pragma omp parallel for reduction(+:sum, *:product, max:maximum)
for (int i = 0; i < n; i++) {
    sum += a[i];
    product *= b[i];
    if (c[i] > maximum) maximum = c[i];
}
```

支持的归约操作符：`+`, `*`, `-`, `&`, `|`, `^`, `&&`, `||`, `min`, `max`

`loop-parallelization` - 循环并行
[[model-order-reduction]] - 归约操作

### 任务并行

#### 基本任务
```c
#pragma omp parallel
{
    #pragma omp single
    {
        #pragma omp task
        process_subtree(left_child);
        
        #pragma omp task
        process_subtree(right_child);
        
        #pragma omp taskwait  // 等待所有任务完成
    }
}
```

#### 任务依赖
```c
#pragma omp task depend(out: a)
compute_a();

#pragma omp task depend(in: a) depend(out: b)
compute_b();  // 依赖于a完成

#pragma omp task depend(in: a, b)
compute_c();  // 依赖于a和b完成
```

`task-parallelism` - 任务并行

### OpenMP子句详解

#### 数据作用域子句
```c
#pragma omp parallel \
    private(x)        // 每个线程独立副本（未初始化）\
    firstprivate(y)   // 每个线程独立副本（初始化为原值）\
    lastprivate(z)    // 最后迭代值复制回原变量\
    shared(array)     // 所有线程共享\
    default(shared)   // 默认共享（除循环变量）
```

#### 线程控制子句
```c
#pragma omp parallel \
    num_threads(8)           // 指定线程数\
    if(n > 1000)             // 条件并行化\
    proc_bind(close)         // 线程绑定策略\
    copyin(thread_local_var) // 复制主线程值到所有线程
```

`openmp-clauses` - OpenMP子句

## 线程同步机制详解

### 互斥锁（Mutex）

#### 临界区
```c
#pragma omp critical
{
    // 同时只有一个线程执行
    shared_counter++;
}
```

#### 命名临界区
```c
#pragma omp critical(section_name)
{
    // 不同名称的临界区可以并发执行
    update_resource_a();
}

#pragma omp critical(other_section)
{
    update_resource_b();  // 可与section_name并发
}
```

#### 原子操作
```c
#pragma omp atomic
shared_counter++;  // 原子自增

#pragma omp atomic update
shared_value += local_value;  // 原子加法

#pragma omp atomic capture
old_value = ++shared_value;  // 原子自增并捕获旧值
```

原子操作比临界区更高效，但功能有限。

`critical-section` - 临界区
`atomic-operation` - 原子操作

### 锁（Lock）机制

#### OpenMP锁
```c
omp_lock_t my_lock;
omp_init_lock(&my_lock);

#pragma omp parallel
{
    omp_set_lock(&my_lock);
    // 临界区
    shared_data[index++] = local_value;
    omp_unset_lock(&my_lock);
}

omp_destroy_lock(&my_lock);
```

#### 嵌套锁
```c
omp_nest_lock_t nest_lock;
omp_init_nest_lock(&nest_lock);

// 同一线程可多次获取
omp_set_nest_lock(&nest_lock);
omp_set_nest_lock(&nest_lock);  // 允许嵌套
omp_unset_nest_lock(&nest_lock);
omp_unset_nest_lock(&nest_lock);
```

### 条件变量

POSIX线程条件变量示例：
```c
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
int ready = 0;

// 等待线程
void* waiter(void* arg) {
    pthread_mutex_lock(&mutex);
    while (!ready) {
        pthread_cond_wait(&cond, &mutex);
    }
    // 处理数据
    pthread_mutex_unlock(&mutex);
    return NULL;
}

// 通知线程
void* notifier(void* arg) {
    pthread_mutex_lock(&mutex);
    ready = 1;
    pthread_cond_broadcast(&cond);  // 唤醒所有等待线程
    pthread_mutex_unlock(&mutex);
    return NULL;
}
```

`condition-variable` - 条件变量

### 屏障同步

```c
#pragma omp parallel
{
    // 阶段1：并行计算
    compute_phase1();
    
    #pragma omp barrier  // 等待所有线程
    
    // 阶段2：依赖阶段1结果
    compute_phase2();
}
```

隐式屏障：
- `parallel for` 结束后隐式同步
- `sections` 结束后隐式同步

```c
#pragma omp parallel for nowait  // 禁用隐式屏障
for (int i = 0; i < n; i++) {
    result[i] = compute(data[i]);
}
// 无需等待，继续执行
```

`barrier` - 屏障同步

### 读写锁

POSIX读写锁：
```c
pthread_rwlock_t rwlock;
pthread_rwlock_init(&rwlock, NULL);

// 读操作（多个读线程可同时持有）
pthread_rwlock_rdlock(&rwlock);
read_data();
pthread_rwlock_unlock(&rwlock);

// 写操作（独占访问）
pthread_rwlock_wrlock(&rwlock);
write_data();
pthread_rwlock_unlock(&rwlock);

pthread_rwlock_destroy(&rwlock);
```

适用于读多写少的场景，如EMT仿真中的参数查询。

`read-write-lock` - 读写锁

## 负载均衡策略

### 静态调度（Static Scheduling）

```c
#pragma omp parallel for schedule(static, chunk_size)
for (int i = 0; i < n; i++) {
    work[i] = compute(i);
}
```

**特点**:
- 迭代预先分配给线程
- 低开销，适合均匀工作负载
- 块大小缺省为 `n / num_threads`

**调度公式**:
- 线程$t$获得迭代范围：$[t \cdot chunk, (t+1) \cdot chunk - 1]$

**适用场景**:
- 每次迭代工作量相等
- 数据访问模式规律

`load-balancing` - 负载均衡

### 动态调度（Dynamic Scheduling）

```c
#pragma omp parallel for schedule(dynamic, chunk_size)
for (int i = 0; i < n; i++) {
    work[i] = variable_compute(i);  // 工作量不均
}
```

**特点**:
- 线程动态获取工作块
- 高开销，但负载更均衡
- 适合不规则计算

**调度开销**:
$$T_{\text{overhead}} = N_{\text{chunks}} \cdot T_{\text{scheduling}}$$

**适用场景**:
- 迭代工作量变化大
- 无法预知执行时间
- 需要动态负载平衡

### 导向调度（Guided Scheduling）

```c
#pragma omp parallel for schedule(guided, min_chunk)
for (int i = 0; i < n; i++) {
    work[i] = compute(i);
}
```

**特点**:
- 块大小递减：$chunk = \frac{\text{remaining}}{\text{num_threads}}$
- 平衡了静态和动态调度的优点
- 减少调度开销，同时保持负载均衡

**块大小变化**:
| 迭代轮次 | 剩余迭代 | 块大小(8线程) |
|----------|----------|---------------|
| 1 | 1000 | 125 |
| 2 | 875 | 109 |
| 3 | 766 | 95 |
| ... | ... | ... |

### 调度策略选择指南

```
工作量均匀 → schedule(static)
工作量随机 → schedule(dynamic, 64)
前期重后期轻 → schedule(guided, 16)
不知道 → schedule(auto) 或 schedule(runtime)
```

## 假共享问题和解决方案

### 假共享（False Sharing）原理

假共享发生在多个线程修改同一缓存行（Cache Line）的不同变量时，导致缓存一致性流量激增。

**缓存行结构**（典型64字节）：
```
+--------------------------------------------------+
| 变量A (8B) | 变量B (8B) | 变量C (8B) | ...       |
+--------------------------------------------------+
|                   缓存行 (64B)                    |
+--------------------------------------------------+
```

**问题场景**:
- 线程1修改变量A
- 线程2修改变量B（同一缓存行）
- 导致缓存行在核心间来回传递
- 严重性能下降（可能慢10-100倍）

`false-sharing` - 假共享

### 假共享检测

```c
// 问题代码 - 假共享
struct Counter {
    long count;  // 线程频繁修改
} counters[8];   // 8个线程的计数器

// 结构体大小可能小于64字节，导致假共享
```

### 解决方案

#### 1. 填充（Padding）
```c
struct PaddedCounter {
    long count;
    char padding[64 - sizeof(long)];  // 填充到缓存行大小
} __attribute__((aligned(64)));  // 64字节对齐

PaddedCounter counters[8];
```

#### 2. 按缓存行对齐
```c
// OpenMP对齐声明
#pragma omp parallel for simd aligned(data:64)
for (int i = 0; i < n; i++) {
    data[i] *= scale;
}
```

#### 3. 使用线程本地存储
```c
#pragma omp threadprivate(local_counter)
static __thread long local_counter = 0;

#pragma omp parallel
{
    // 每个线程独立修改本地计数器
    local_counter++;
    
    #pragma omp critical
    global_counter += local_counter;
}
```

### 内存对齐技术

```c
// C11对齐
#include <stdalign.h>
alignas(64) double cache_aligned_array[1024];

// POSIX对齐
posix_memalign(&ptr, 64, size);

// OpenMP SIMD对齐
#pragma omp simd aligned(ptr:64)
for (int i = 0; i < n; i++) {
    ptr[i] = compute(i);
}
```

## 缓存优化

### 缓存层次结构

| 级别 | 大小 | 延迟 | 带宽 |
|------|------|------|------|
| L1 | 32-64KB | 4 cycles | ~100 GB/s |
| L2 | 256-512KB | 12 cycles | ~50 GB/s |
| L3 | 8-64MB | 40 cycles | ~25 GB/s |
| RAM | GB级 | 100+ cycles | ~10 GB/s |

### 缓存优化策略

#### 1. 时间局部性
```c
// 好：重复访问相同数据
for (int t = 0; t < timesteps; t++) {
    for (int i = 0; i < n; i++) {
        voltage[i] += delta_t * current[i];
    }
}
```

#### 2. 空间局部性
```c
// 好：顺序访问
for (int i = 0; i < n; i++) {
    sum += array[i];  // 连续内存访问
}

// 差：跳跃访问
for (int i = 0; i < n; i += 16) {
    sum += array[i];
}
```

#### 3. 循环分块（Loop Tiling）
```c
// 提高缓存命中率
const int BLOCK = 256;
for (int ii = 0; ii < n; ii += BLOCK) {
    for (int jj = 0; jj < n; jj += BLOCK) {
        for (int i = ii; i < min(ii+BLOCK, n); i++) {
            for (int j = jj; j < min(jj+BLOCK, n); j++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}
```

`cache-optimization` - 缓存优化

## EMT仿真中的并行策略

### 节点分解并行（Nodal Parallelism）

将导纳矩阵的行分配给不同线程。

```c
// 节点电压更新并行
#pragma omp parallel for schedule(guided, 128)
for (int node = 0; node < num_nodes; node++) {
    double sum = 0.0;
    for (int col = row_ptr[node]; col < row_ptr[node+1]; col++) {
        sum += Y_matrix[col] * V_old[col_indices[col]];
    }
    V_new[node] = (I_inj[node] - sum) / Y_diag[node];
}
```

**优缺点**:
- 优点：自然分解，负载易平衡
- 缺点：需要全局同步，节点间依赖

`nodal-parallelism` - 节点并行

### 支路分解并行（Branch Parallelism）

将支路（元件）计算分配给不同线程。

```c
// 支路电流和历史项更新
#pragma omp parallel for schedule(dynamic, 64)
for (int branch = 0; branch < num_branches; branch++) {
    Branch* b = branches[branch];
    
    // 计算支路电流
    double v_diff = V[b->from_node] - V[b->to_node];
    b->current = b->conductance * v_diff + b->history_current;
    
    // 更新历史项（为下一时步）
    b->update_history();
}

#pragma omp barrier  // 等待所有支路计算完成

// 节点注入电流汇总
#pragma omp parallel for
for (int node = 0; node < num_nodes; node++) {
    I_inj[node] = 0.0;
    for (Branch* b : node_branches[node]) {
        I_inj[node] += b->get_injection(node);
    }
}
```

`element-parallelism` - 元件并行

### 流水线并行（Pipeline Parallelism）

将仿真分解为多个阶段，形成流水线。

```c
// 三阶段流水线
#pragma omp parallel sections
{
    #pragma omp section
    while (running) {
        // 阶段1：支路计算
        compute_branches();
        stage1_done = 1;
    }
    
    #pragma omp section
    while (running) {
        // 阶段2：节点求解
        wait(stage1_done);
        solve_nodes();
        stage2_done = 1;
    }
    
    #pragma omp section
    while (running) {
        // 阶段3：输出
        wait(stage2_done);
        output_results();
    }
}
```

### 多场景并行（Scenario Parallelism）

同时运行多个独立仿真场景。

```c
// 蒙特卡洛仿真并行
#pragma omp parallel for schedule(dynamic)
for (int scenario = 0; scenario < num_scenarios; scenario++) {
    // 每个线程独立运行完整仿真
    EMT_Simulator sim(circuit);
    sim.set_parameters(scenario_params[scenario]);
    results[scenario] = sim.run();
}
```

`monte-carlo` - 蒙特卡洛

## 性能分析和调优方法

### 性能剖析工具

#### Intel VTune
```bash
# 热点分析
vtune -collect hotspots -result-dir vtune_data ./emt_sim

# 线程分析
vtune -collect threading -result-dir vtune_data ./emt_sim

# 内存访问分析
vtune -collect memory-access -result-dir vtune_data ./emt_sim
```

#### GNU Profiler (gprof)
```bash
gcc -pg -O2 emt_sim.c -o emt_sim
./emt_sim
gprof emt_sim gmon.out > analysis.txt
```

#### OpenMP专用工具
```c
// 设置环境变量
export OMP_DISPLAY_ENV=VERBOSE
export OMP_DISPLAY_AFFINITY=TRUE

// 编译时添加调试信息
gcc -fopenmp -g -O2 emt.c
```

`profiler` - 性能分析器

### 性能调优检查清单

```
□ 确认并行区域覆盖主要计算
□ 检查负载均衡（静态/动态调度）
□ 验证无假共享（缓存行对齐）
□ 减少临界区大小
□ 使用原子操作替代锁
□ 避免屏障同步
□ 优化内存访问模式
□ 线程绑定到物理核心
```

### 线程亲和性设置

```c
// 绑定线程到核心
#pragma omp parallel proc_bind(close)
{
    int thread_id = omp_get_thread_num();
    int cpu_id = thread_id % num_cores;
    // 绑定到特定CPU
    cpu_set_t cpuset;
    CPU_ZERO(&cpuset);
    CPU_SET(cpu_id, &cpuset);
    pthread_setaffinity_np(pthread_self(), sizeof(cpuset), &cpuset);
}
```

环境变量设置：
```bash
export OMP_PROC_BIND=close  # 紧密绑定
export OMP_PLACES=cores     # 绑定到核心
export OMP_NUM_THREADS=16   # 线程数
```

`thread-affinity` - 线程亲和性

## 混合并行（OpenMP + MPI）

### 混合架构

```
+----------------+  +----------------+  +----------------+
|   Node 0       |  |   Node 1       |  |   Node 2       |
| +---+---+---+  |  | +---+---+---+  |  | +---+---+---+  |
| |T0 |T1 |T2 |  |  | |T0 |T1 |T2 |  |  | |T0 |T1 |T2 |  |
| +---+---+---+  |  | +---+---+---+  |  | +---+---+---+  |
|   OpenMP       |  |   OpenMP       |  |   OpenMP       |
+-------+--------+  +-------+--------+  +-------+--------+
        |                   |                   |
        +-------------------+-------------------+
                    MPI通信
```

### 混合并行实现

```c
#include <mpi.h>
#include <omp.h>

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);
    
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    
    // 每个MPI进程负责一部分网络
    int local_nodes = total_nodes / size;
    int start_node = rank * local_nodes;
    
    // 节点内使用OpenMP
    #pragma omp parallel for
    for (int n = start_node; n < start_node + local_nodes; n++) {
        compute_local_node(n);
    }
    
    // MPI交换边界数据
    MPI_Allgather(local_voltages, local_nodes, MPI_DOUBLE,
                  global_voltages, local_nodes, MPI_DOUBLE,
                  MPI_COMM_WORLD);
    
    MPI_Finalize();
    return 0;
}
```

### 混合并行最佳实践

1. **线程数设置**: 节点内核心数 = OpenMP线程数
2. **MPI进程数**: 通常等于节点数
3. **通信优化**: 合并小消息，减少通信次数
4. **重叠计算通信**: 使用非阻塞通信

```c
// 重叠计算和通信
#pragma omp parallel
{
    #pragma omp for nowait
    for (int i = 0; i < n_local; i++) {
        compute_interior(i);  // 内部点
    }
    
    // 准备边界数据
    #pragma omp single
    {
        MPI_Isend(boundary_data, ...);
    }
    
    // 继续计算边界
    #pragma omp for
    for (int i = n_local - boundary; i < n_local; i++) {
        compute_boundary(i);
    }
}
```

[[chen-等-a-hybrid-parallel-computation-algorithm-and-its-application-to-multi-phas]] - 混合并行
[[numerical-damping-optimization]] - MPI

## 实际应用案例

### 大规模EMT仿真平台

**测试配置**:
- CPU: Intel Xeon Gold 6248R (24核 × 2 = 48核)
- 内存: 512GB DDR4
- 网络规模: 10,000节点，20,000支路
- 仿真时长: 10秒，步长50μs

**性能结果**:

| 线程数 | 仿真时间 | 加速比 | 效率 |
|--------|----------|--------|------|
| 1 | 3600s | 1.0 | 100% |
| 4 | 950s | 3.79 | 95% |
| 8 | 495s | 7.27 | 91% |
| 16 | 270s | 13.3 | 83% |
| 24 | 195s | 18.5 | 77% |
| 48 | 140s | 25.7 | 54% |

**分析**:
- 16线程以内效率>80%，表现良好
- 48线程时效率下降，受内存带宽和同步开销限制
- 适合生产环境使用16-24线程

### 实时仿真应用

**RT-LAB实时仿真器配置**:
- 目标步长: 50μs
- 最小计算时间: < 40μs（保证实时性）
- 并行策略: 节点分解 + 支路分解

**性能数据**:
- 单核: 65μs/步（不满足实时）
- 4核: 22μs/步（满足实时，余量78%）
- 8核: 14μs/步（余量72%）

[[real-time-simulation]] - 实时仿真

### 暂态稳定性并行计算

**案例**: 1000机系统，1000个故障场景

```c
// 场景级并行
#pragma omp parallel for schedule(dynamic)
for (int fault = 0; fault < num_faults; fault++) {
    TransientStability ts(system);
    ts.apply_fault(faults[fault]);
    ts.simulate(10.0);  // 10秒仿真
    stability_margin[fault] = ts.get_stability_margin();
}
```

**加速效果**:
- 32线程: 加速比28.5倍（效率89%）
- 每个场景独立，无数据竞争
- 动态调度平衡不同故障的计算量

[[transient-stability]] - 暂态稳定

## 调试与线程安全

### ThreadSanitizer

```bash
# 编译时启用ThreadSanitizer
gcc -fopenmp -fsanitize=thread -g -O1 emt.c -o emt_tsan

# 运行检测
./emt_tsan
```

检测问题：
- 数据竞争
- 死锁
- 线程泄漏

`threadsanitizer` - ThreadSanitizer

### 常见线程问题

#### 数据竞争
```c
// 错误：无保护访问共享变量
#pragma omp parallel for
for (int i = 0; i < n; i++) {
    shared_sum += local_sum[i];  // 数据竞争！
}

// 正确：使用归约
#pragma omp parallel for reduction(+:shared_sum)
for (int i = 0; i < n; i++) {
    shared_sum += local_sum[i];
}
```

`data-race` - 数据竞争

#### 死锁
```c
// 错误：嵌套锁顺序不一致
Thread A: lock(X); lock(Y);  // 顺序1
Thread B: lock(Y); lock(X);  // 顺序2 → 死锁

// 正确：统一顺序
Thread A: lock(X); lock(Y);
Thread B: lock(X); lock(Y);
```

## 在EMT中的应用

### 节点并行
- **节点分组**: 每组一个线程
- `nodal-parallelism` - 节点并行
- **导纳矩阵**: 并行构建

### 支路并行
- **元件计算**: 并行更新
- `element-parallelism` - 元件并行
- **历史电流**: 并行计算

### 多场景
- **蒙特卡洛**: 场景并行
- `monte-carlo` - 蒙特卡洛
- **参数扫描**: 批量并行

## 与MPI对比

| 特性 | 多线程 | MPI |
|------|--------|-----|
| 内存 | 共享 | 分布式 |
| 通信 | 内存访问 | 消息传递 |
| 开销 | 低 | 高 |
| 扩展 | 有限 | 好 |
| 适用 | 单机 | 集群 |

## 异构计算
- [[heterogeneous-computing]] - 异构计算
- **CPU+GPU**: 异构
- **OpenMP+CUDA**: 混合编程

## 相关方法
- [[parallel-computing]] - 并行计算
- [[high-performance-computing]] - 高性能计算
- `openmp` - OpenMP
- [[computational-acceleration]] - 计算加速
- [[gpu-accelerated-simulation]] - GPU加速仿真
- `distributed-computing` - 分布式计算

## 来源论文

参见 [[index.md]] 获取更多多线程并行计算相关文献。
