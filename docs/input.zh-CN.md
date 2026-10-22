# 输入与输出

[English](INPUT.md) | 简体中文 · [教程](tutorial.zh-CN.md)

对应 **v0.2.1**。输入为 UTF-8 JSON 对象，最大 10 MiB。支持 --input 文件路径与 --input -；拒绝重复 JSON 键和非有限常量。

| 字段 | 约定 |
| --- | --- |
| task_id / goal | 非空字符串。 |
| events | 有序数组，每项含严格递增的正整数 seq、action_id、state（planned / dispatched / completed / failed / cancelled）。planned 必须有布尔 replay_safe，completed 必须有 receipt。 |

## 样例

```json
{
  "task_id": "task-17",
  "goal": "Prepare and deliver a report",
  "events": [
    {
      "seq": 1,
      "action_id": "draft",
      "state": "planned",
      "replay_safe": true
    },
    {
      "seq": 2,
      "action_id": "draft",
      "state": "dispatched"
    },
    {
      "seq": 3,
      "action_id": "draft",
      "state": "completed",
      "receipt": "report.md"
    },
    {
      "seq": 4,
      "action_id": "email",
      "state": "planned",
      "replay_safe": false
    },
    {
      "seq": 5,
      "action_id": "email",
      "state": "dispatched"
    }
  ]
}
```

[完整预期结果](../examples/expected.json)。JSON 键名保留英文以匹配程序接口；字符串内容使用你的实际记录。退出码 0 代表处理完成，不代表所报告问题已经通过。

## 错误与副作用

工具不联网，不执行提交的命令。只读取输入及约定中明确指出的本地路径；默认向终端输出，只在明确 --output 时写入新文件。无效输入退出码为 2，已有结果文件不覆盖。写入失败可能留下不完整新文件，应先检查。安装是独立的明确操作。
