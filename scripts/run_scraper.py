"""CLI entrypoint to run the full CMQ pipeline."""

from __future__ import annotations

from src.pipeline import extract, transform, load


def main() -> None:
    raw_artifacts = extract.run()
    rows = transform.run(raw_artifacts)
    output_path = load.run(rows)
    print(f"Wrote cleaned dataset to {output_path}")


if __name__ == "__main__":
    main()
