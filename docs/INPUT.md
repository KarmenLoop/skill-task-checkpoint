# Input and output

Supply a UTF-8 JSON object (maximum 10 MiB). Duplicate JSON keys and non-finite JSON constants are rejected. Arrays are required unless documented as optional. IDs must be stable and unique. Dates use ISO 8601; timestamps require an explicit UTC offset.

| Field | Contract |
| --- | --- |
| task_id/goal | Nonempty strings. |
| events | Ordered objects: seq positive integer, action_id, state (planned/dispatched/completed/failed/cancelled), replay_safe boolean on planned event, receipt required on completed. |

## Example

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

## Result

task_id, goal, actions, resume_queue, and sha256 over the normalized checkpoint content.

See [the complete sample result](../examples/expected.json). Exit 0 means processing completed, not that all reported findings passed.

## Errors and side effects

The helper makes no network requests and executes no submitted commands. It reads the input and explicitly documented local paths. It writes only a requested new output file; stdout is the default. Invalid input exits 2. Existing output is preserved. An output write failure can leave a partial new file; remove that file before retrying. Installation is a separate explicit action.
