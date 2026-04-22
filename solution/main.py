from __future__ import annotations

from pathlib import Path

from solution.app.pipeline import run_pipeline


def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    final_sum, total_entries, valid_entries, invalid_counts, report_path = run_pipeline(base_dir)

    print("Processing completed successfully.")
    print(f"Total entries scanned: {total_entries}")
    print(f"Valid entries: {valid_entries}")
    print(f"Invalid entries: {total_entries - valid_entries}")
    print(f"Final sum: {final_sum:.2f}")
    print(f"Report file: {report_path}")

    if invalid_counts:
        print("\nTop anomaly reasons:")
        for reason, count in invalid_counts.most_common(10):
            print(f"- {reason}: {count}")


if __name__ == "__main__":
    main()
