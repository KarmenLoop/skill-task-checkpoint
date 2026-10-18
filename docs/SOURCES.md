# Sources and provenance

Research date: 2026-10-19.

## Public references

- [DeepSeek Harness: checkpoints](https://github.com/deepseek-ai/deepseek-harness/blob/687f282e8625c6b8d11ff58211a90524be2e4317/packages/session/session-checkpoint-policy/README.md)
- [Grok Build: planning](https://github.com/xai-org/grok-build/blob/2bdd1d6a6369de0e8c68132ea4539e9abd9e14a8/crates/codegen/xai-grok-pager/docs/user-guide/19-plan-mode.md)

## Design decision

We use an explicit event ledger and report uncertain effects without granting execution permission.

## Distribution

KarmenLoop wrote these instructions, helpers, examples, tests, and packaging. No upstream source tree, model weights, proprietary prompts, logos, or credentials are bundled. Python's standard library is the only runtime dependency.

Links identify research sources, not endorsement or certification. GitHub references are pinned to the revisions reviewed. Meta's Muse announcement describes a product; it does not establish that the personal-agent implementation is available as source.

Any future imported code must record its exact revision, files, copyright, license, and modifications in NOTICE.md.
