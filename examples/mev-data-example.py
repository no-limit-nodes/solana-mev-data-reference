#!/usr/bin/env python3
"""Summarize Solana MEV JSONL data using the repository schema's core fields."""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


def read_events(path: Path):
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc}") from exc
            if not isinstance(event, dict):
                raise ValueError(f"Line {line_number} must contain a JSON object")
            yield event


def summarize(path: Path) -> None:
    events = list(read_events(path))
    types = Counter(event.get("event_type", "unknown") for event in events)
    net_profit = sum(event.get("profit_lamports") or 0 for event in events)

    print(f"events: {len(events)}")
    print(f"net profit (lamports): {net_profit}")
    print("event types:")
    for event_type, count in sorted(types.items()):
        print(f"  {event_type}: {count}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python examples/mev-data-example.py events.jsonl")
    summarize(Path(sys.argv[1]))
