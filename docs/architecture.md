# Architecture Overview

## Modules
- `codex_testnet.app`: core greeting logic.
- `codex_testnet.cli`: command-line interface.

## Data flow
1. CLI parses arguments.
2. Greeting helper normalizes names.
3. Greeting string is printed to stdout.
