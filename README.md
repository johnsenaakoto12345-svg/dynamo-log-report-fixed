# dynamo-log-report-fixed

Repaired Terminal-Bench 2 (Harbor) task for the Project Dynamo assessment.

## Task
Parse an Apache-style access log at `/app/access.log` into a JSON summary at `/app/report.json` with three keys: `total_requests`, `unique_ips`, and `top_path`.

## What was fixed
- **task.toml**: `artifacts` changed from a string to a top-level array pointing at the real output path.
- **environment/Dockerfile**: replaced the unpinned `python:latest` base with an approved digest-pinned base image, and removed a `solution_hint.py` file that leaked the solution into the agent image.
- **tests/**: rewrote the verifier to recompute ground truth from the log and assert on the real values instead of only checking that the file exists; fixed `test.sh` to write the reward to `/logs/verifier/reward.txt` and produce `ctrf.json`.
- **instruction.md**: rewrote it to name the exact output path and JSON schema and to end with the required timeout line.

## Verification
- `harbor run -p . -a oracle` scores reward 1.0
- `harbor run -p . --agent nop` scores reward 0.0
- A deliberately bugged solution scores reward 0.0, confirming the verifier rejects wrong answers.
