import json
import re
from collections import Counter
from pathlib import Path

REPORT = Path("/app/report.json")
LOG = Path("/app/access.log")


def _ground_truth():
    paths, ips, total = Counter(), set(), 0
    for line in LOG.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1
    return total, len(ips), paths.most_common(1)[0][0]


def _load():
    return json.loads(REPORT.read_text())


def test_report_exists():
    # Criterion: agent must write the report to /app/report.json.
    """Verifies report.json was created at the required path."""
    assert REPORT.exists(), "no report.json found"


def test_report_valid_json_object():
    # Criterion: report.json is a JSON object with exactly the three named keys.
    """Verifies the output is a JSON object with keys total_requests, unique_ips, top_path."""
    data = _load()
    assert isinstance(data, dict)
    assert set(data.keys()) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    # Criterion: "total_requests" = number of non-blank log lines.
    """Verifies total_requests matches the recomputed count of non-blank lines."""
    total, _, _ = _ground_truth()
    assert _load()["total_requests"] == total


def test_unique_ips():
    # Criterion: "unique_ips" = number of distinct client IPs.
    """Verifies unique_ips matches the recomputed distinct-IP count."""
    _, uniq, _ = _ground_truth()
    assert _load()["unique_ips"] == uniq


def test_top_path():
    # Criterion: "top_path" = most frequently requested path.
    """Verifies top_path matches the recomputed most-common path."""
    _, _, top = _ground_truth()
    assert _load()["top_path"] == top