An Apache-style access log is at /app/access.log. Parse it and write a JSON summary to /app/report.json.

The log has one request per line in the common/combined format: the client IP is the first whitespace-separated token, and the request line appears in double quotes as "METHOD path protocol" (for example "GET /index.html HTTP/1.1"). Ignore blank lines.

Write /app/report.json as a single JSON object with exactly these three keys:

- "total_requests": integer, the number of non-blank log lines.
- "unique_ips": integer, the number of distinct client IP addresses.
- "top_path": string, the request path that appears most often.

Do not modify /app/access.log.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.