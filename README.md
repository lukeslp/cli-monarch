# cli-monarch

Standalone Monarch Money CLI and Python client.

This repository is a standalone extraction of the local Monarch tooling previously kept inside `geepers-kernel`. It preserves the existing `mm` command, keeps the Python client import path as `monarchmoney`, and adds a `monarch` console alias.

## Status

- Distribution/package name: `cli-monarch`
- Python import package: `monarchmoney`
- Console commands: `mm`, `monarch`

## Installation

### From source

```bash
git clone https://github.com/lukeslp/cli-monarch.git
cd cli-monarch
python3 -m pip install -e .
```

### Verify

```bash
mm --help
monarch --help
```

## Quick Start

```bash
mm login
mm accounts
mm transactions list --limit 25
mm budgets summary
mm insights analyze
```

## Project Layout

```text
cli-monarch/
├── monarchmoney/    # Core Monarch client library
├── cli/             # Click-based CLI
├── mcp_server/      # Optional MCP server wrapper
├── tests/           # Test suite
└── .github/workflows/
```

## Notes

- This repo is derived from the upstream `hammem/monarchmoney` project plus local CLI and MCP additions.
- The new repository identity is intentionally separate from the upstream package to avoid publishing collisions.
- The CLI stores encrypted session data in `~/.mm/`.
