# Task Checkpoint

English | [简体中文](README.zh-CN.md)

Before resuming interrupted work, inspect what was planned, dispatched, and actually completed. A checkpoint makes uncertain side effects visible instead of assuming that an unfinished call is safe to repeat.

[Download v0.2.1](https://github.com/KarmenLoop/skill-task-checkpoint/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-task-checkpoint/issues)

## What it does

The draft has a completion receipt. The dispatched email has no confirmed outcome, so the resume queue asks to verify_external_outcome.

This summarizes an event log. It does not execute queued work, verify external receipts, restore permissions, or resume a process by itself.

![Task Checkpoint sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-task-checkpoint-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-task-checkpoint 0.2.1`. The draft has a completion receipt. The dispatched email has no confirmed outcome, so the resume queue asks to verify_external_outcome.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Keep seq strictly increasing. Start each action with planned and an explicit replay_safe Boolean; completed events need a receipt.

Compare a replay-safe calculation with a non-replay-safe send. Preserve the checkpoint hash and inspect the external outcome before deciding whether to repeat an uncertain operation.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Will it resend a message after a crash?** No. The queue is advice. A dispatched non-replay-safe action requires outcome verification before any new authorized execution.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
