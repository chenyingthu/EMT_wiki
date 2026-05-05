#!/usr/bin/env python3
"""
Wiki修订主循环
实现五阶段闭环：问题定位→工作计划→问题修订→工作记录→进展提交
"""
import os
import sys
import json
import time
import subprocess
from datetime import datetime
from pathlib import Path

# 配置
LOOP_INTERVAL = 600  # 10分钟
MAX_ROUNDS_WITHOUT_PROGRESS = 3  # 连续3轮无进展则暂停
STATE_FILE = '.revision_loop_state.json'
TASK_REGISTRY = 'plans/task-registry.json'
REGISTRY_FILE = 'wiki/standards/page-revision-registry.md'

class RevisionLoop:
    def __init__(self):
        self.state = self.load_state()
        self.round_count = self.state.get('round_count', 0)
        self.last_progress = self.state.get('last_progress', 0)
        self.consecutive_no_progress = self.state.get('consecutive_no_progress', 0)

    def load_state(self):
        """加载循环状态"""
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except:
            return {
                'round_count': 0,
                'last_progress': 0,
                'consecutive_no_progress': 0,
                'status': 'running'
            }

    def save_state(self):
        """保存循环状态"""
        self.state['round_count'] = self.round_count
        self.state['last_progress'] = self.last_progress
        self.state['last_update'] = datetime.now().isoformat()
        with open(STATE_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)

    def log(self, message, level='INFO'):
        """记录日志"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_line = f"[{timestamp}] [{level}] {message}"
        print(log_line)

        # 追加到日志文件
        with open('wiki/log.md', 'a', encoding='utf-8') as f:
            f.write(f"{log_line}\n")

    # ========== Phase 1: 问题定位 ==========
    def phase_1_diagnostic(self):
        """执行诊断扫描"""
        self.log("=" * 70)
        self.log("Phase 1: 问题定位 (诊断扫描)")
        self.log("=" * 70)

        # 运行质量审计
        self.log("运行质量审计...")
        result = subprocess.run(
            ['python3', 'tools/audit_wiki_quality.py'],
            capture_output=True, text=True
        )

        # 运行诊断扫描
        self.log("运行诊断扫描...")
        try:
            from diagnostic_scan import main as diagnostic_main
            summary = diagnostic_main()
        except Exception as e:
            self.log(f"诊断扫描失败: {e}", 'ERROR')
            return None

        total_issues = summary.get('pages_with_issues', 0)
        self.log(f"诊断完成: {total_issues}个页面有问题")

        return summary

    # ========== Phase 2: 工作计划 ==========
    def phase_2_planning(self, diagnostic):
        """创建工作计划"""
        self.log("")
        self.log("=" * 70)
        self.log("Phase 2: 工作计划 (任务分片)")
        self.log("=" * 70)

        if not diagnostic:
            self.log("无诊断数据，跳过计划", 'WARN')
            return []

        # 加载优先级队列
        tasks = []

        # 优先处理高优先级队列
        for level in ['high', 'medium']:
            queue_file = f'reports/diagnostic-reports/priority-queue-{level}.json'
            try:
                with open(queue_file, 'r') as f:
                    pages = json.load(f)

                # 每批最多10个页面
                batch_size = 10
                for i in range(0, len(pages), batch_size):
                    batch = pages[i:i+batch_size]
                    task = {
                        'task_id': f'wave-{self.round_count:03d}-{level}-{i//batch_size}',
                        'shard_type': 'diagnostic-priority',
                        'pages': [p['path'] for p in batch],
                        'priority': level,
                        'status': 'pending',
                        'created': datetime.now().isoformat(),
                        'expected_outcomes': ['fix-structural', 'fix-evidence', 'add-boundary']
                    }
                    tasks.append(task)

                self.log(f"{level}优先级: 创建{len(range(0, len(pages), batch_size))}个任务")

            except Exception as e:
                self.log(f"加载{level}队列失败: {e}", 'WARN')

        # 保存任务注册表
        self.save_task_registry(tasks)

        self.log(f"计划完成: 共{len(tasks)}个任务")
        return tasks[:5]  # 每次只执行前5个任务

    def save_task_registry(self, tasks):
        """保存任务注册表"""
        try:
            with open(TASK_REGISTRY, 'r') as f:
                registry = json.load(f)
        except:
            registry = {'tasks': [], 'completed': []}

        registry['tasks'].extend(tasks)
        registry['last_updated'] = datetime.now().isoformat()

        with open(TASK_REGISTRY, 'w') as f:
            json.dump(registry, f, indent=2)

    # ========== Phase 3: 问题修订 ==========
    def phase_3_revision(self, tasks):
        """执行问题修订"""
        self.log("")
        self.log("=" * 70)
        self.log("Phase 3: 问题修订 (执行修改)")
        self.log("=" * 70)

        if not tasks:
            self.log("无任务，跳过修订")
            return []

        completed_tasks = []

        for task in tasks:
            self.log(f"\n执行任务: {task['task_id']}")
            self.log(f"  页面: {len(task['pages'])}个")

            # 检查页面锁定状态
            if not self.check_page_lock(task['pages']):
                self.log(f"  页面被锁定，跳过", 'WARN')
                continue

            # 锁定页面
            self.lock_pages(task['pages'], task['task_id'])

            # 执行修订
            try:
                result = self.execute_revision_task(task)
                completed_tasks.append({
                    'task': task,
                    'result': result
                })

                self.log(f"  完成: {result.get('pages_fixed', 0)}个页面修复")

            except Exception as e:
                self.log(f"  失败: {e}", 'ERROR')

            finally:
                # 解锁页面
                self.unlock_pages(task['pages'])

        return completed_tasks

    def check_page_lock(self, pages):
        """检查页面是否被锁定"""
        try:
            with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
                content = f.read()

            for page in pages:
                page_name = os.path.basename(page)
                # 简单检查：如果页面在registry中且状态不是open，则视为锁定
                # 实际应解析markdown表格
                if page_name in content and 'in-progress' in content:
                    return False
            return True
        except:
            return True

    def lock_pages(self, pages, task_id):
        """锁定页面"""
        self.update_registry(pages, 'in-progress', task_id)

    def unlock_pages(self, pages):
        """解锁页面"""
        self.update_registry(pages, 'open', None)

    def update_registry(self, pages, status, task_id):
        """更新注册表"""
        # 简化实现：记录到状态文件
        for page in pages:
            self.state[f'lock_{page}'] = {
                'status': status,
                'task_id': task_id,
                'time': datetime.now().isoformat()
            }
        self.save_state()

    def execute_revision_task(self, task):
        """执行单个修订任务"""
        pages_fixed = 0
        issues_fixed = {
            'structural': 0,
            'evidence': 0,
            'network': 0,
            'format': 0
        }

        for page_path in task['pages']:
            if not os.path.exists(page_path):
                continue

            try:
                # 读取页面
                with open(page_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                original = content
                changed = False

                # 自动修复：替换"待补充"为有意义的内容
                if '- 待补充' in content:
                    # 从相关source提取内容
                    new_content = self.enrich_from_sources(page_path, content)
                    if new_content != content:
                        content = new_content
                        changed = True
                        issues_fixed['structural'] += 1

                # 自动修复：降级强断言
                content, evidence_changes = self.fix_strong_assertions(content)
                if evidence_changes > 0:
                    changed = True
                    issues_fixed['evidence'] += evidence_changes

                # 保存修改
                if changed:
                    with open(page_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    pages_fixed += 1

            except Exception as e:
                self.log(f"    修复{page_path}失败: {e}", 'WARN')

        return {
            'pages_fixed': pages_fixed,
            'issues_fixed': issues_fixed
        }

    def enrich_from_sources(self, page_path, content):
        """从source提取内容丰富页面"""
        # 简化实现：调用已有的enrich_c_pages_batch.py逻辑
        # 实际应实现更复杂的source匹配和内容提取
        return content

    def fix_strong_assertions(self, content):
        """修复强断言"""
        changes = 0

        # 强断言替换规则
        replacements = [
            (r'该方法完全消除', '该方法在该算例中报告可缓解'),
            (r'首次提出', '作者报告'),
            (r'最优解', '在该工况下的较好解'),
            (r'适用于所有', '适用于该论文测试的'),
        ]

        for pattern, replacement in replacements:
            new_content, count = re.subn(pattern, replacement, content)
            if count > 0:
                content = new_content
                changes += count

        return content, changes

    # ========== Phase 4: 工作记录 ==========
    def phase_4_recording(self, completed_tasks):
        """更新工作记录"""
        self.log("")
        self.log("=" * 70)
        self.log("Phase 4: 工作记录 (状态登记)")
        self.log("=" * 70)

        if not completed_tasks:
            self.log("无完成任务，跳过记录")
            return

        # 更新任务注册表
        try:
            with open(TASK_REGISTRY, 'r') as f:
                registry = json.load(f)
        except:
            registry = {'tasks': [], 'completed': []}

        for item in completed_tasks:
            task = item['task']
            result = item['result']

            # 移动到completed
            registry['tasks'] = [t for t in registry['tasks'] if t['task_id'] != task['task_id']]
            registry['completed'].append({
                **task,
                'status': 'completed',
                'completed_at': datetime.now().isoformat(),
                'result': result
            })

        registry['last_updated'] = datetime.now().isoformat()

        with open(TASK_REGISTRY, 'w') as f:
            json.dump(registry, f, indent=2)

        self.log(f"更新任务注册表: {len(completed_tasks)}个任务标记为完成")

        # 更新进度仪表板
        self.update_dashboard(completed_tasks)

    def update_dashboard(self, completed_tasks):
        """更新进度仪表板"""
        try:
            with open('reports/progress-dashboard.json', 'r') as f:
                dashboard = json.load(f)
        except:
            dashboard = {
                'last_updated': datetime.now().isoformat(),
                'overall': {'total_pages': 1386, 'A_grade': 0, 'B_grade': 0},
                'current_wave': {'progress': 0}
            }

        # 更新统计
        pages_fixed = sum(t['result'].get('pages_fixed', 0) for t in completed_tasks)
        dashboard['last_updated'] = datetime.now().isoformat()
        dashboard['current_wave']['progress'] += pages_fixed

        with open('reports/progress-dashboard.json', 'w') as f:
            json.dump(dashboard, f, indent=2)

        self.log("更新进度仪表板")

    # ========== Phase 5: 进展提交 ==========
    def phase_5_submission(self, completed_tasks):
        """进展提交与验证"""
        self.log("")
        self.log("=" * 70)
        self.log("Phase 5: 进展提交 (验证归档)")
        self.log("=" * 70)

        if not completed_tasks:
            self.log("无完成任务，跳过提交")
            return 0

        # 运行验证
        self.log("运行质量验证...")

        # 质量审计
        result = subprocess.run(
            ['python3', 'tools/audit_wiki_quality.py'],
            capture_output=True, text=True
        )

        # 检查质量倒退
        if result.returncode == 0:
            self.log("✓ 质量审计通过")
        else:
            self.log("✗ 质量审计发现问题", 'WARN')

        # 计算进展
        total_pages_fixed = sum(
            t['result'].get('pages_fixed', 0)
            for t in completed_tasks
        )

        self.log(f"本轮进展: 修复{total_pages_fixed}个页面")

        return total_pages_fixed

    # ========== 主循环 ==========
    def run_single_round(self):
        """执行单轮循环"""
        self.round_count += 1
        self.log("")
        self.log("#" * 70)
        self.log(f"# 第 {self.round_count} 轮迭代")
        self.log("#" * 70)

        # Phase 1: 问题定位
        diagnostic = self.phase_1_diagnostic()

        # 检查是否完成
        if diagnostic and diagnostic.get('pages_with_issues', 0) == 0:
            self.log("\n🎉 所有问题已解决! 退出循环。")
            self.state['status'] = 'completed'
            self.save_state()
            return False

        # Phase 2: 工作计划
        tasks = self.phase_2_planning(diagnostic)

        # Phase 3: 问题修订
        completed_tasks = self.phase_3_revision(tasks)

        # Phase 4: 工作记录
        self.phase_4_recording(completed_tasks)

        # Phase 5: 进展提交
        progress = self.phase_5_submission(completed_tasks)

        # 检查进展
        if progress == 0:
            self.consecutive_no_progress += 1
            self.log(f"\n⚠ 连续{self.consecutive_no_progress}轮无进展")

            if self.consecutive_no_progress >= MAX_ROUNDS_WITHOUT_PROGRESS:
                self.log("\n⛔ 连续多轮无进展，暂停循环等待人工干预")
                self.state['status'] = 'paused'
                self.save_state()
                return False
        else:
            self.consecutive_no_progress = 0
            self.last_progress = progress

        self.save_state()
        return True

    def run(self):
        """运行主循环"""
        self.log("=" * 70)
        self.log("Wiki修订主循环启动")
        self.log("=" * 70)
        self.log(f"状态: {self.state.get('status', 'running')}")
        self.log(f"已执行轮次: {self.round_count}")

        if self.state.get('status') == 'completed':
            self.log("任务已完成，退出")
            return

        if self.state.get('status') == 'paused':
            self.log("任务已暂停，退出")
            return

        # 执行单轮
        should_continue = self.run_single_round()

        if should_continue:
            self.log(f"\n下一轮将在{LOOP_INTERVAL}秒后执行...")
            # 不在这里sleep，由cron控制间隔
        else:
            self.log("\n循环结束")

def main():
    loop = RevisionLoop()
    loop.run()

if __name__ == '__main__':
    main()
