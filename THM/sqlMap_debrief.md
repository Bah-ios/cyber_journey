Reached the dump stage against the ai database's user table, demonstrating end-to-end SQL injection impact through automated extraction.

Proving exploitability with data extraction shows real risk to the business.

Flow:
- Enumerate databases with --dbs
- Identify ai database and user table
- Dump user table records

Improvement
Repeated sqlmap runs used placeholder credentials and truncated URLs without isolating the vulnerable parameter. This widens the test surface and slows discovery.

Scoping tests to a confirmed parameter reduces noise and avoids wasted scan cycles during real assessments.

Flow:
- Capture the full GET request from DevTools
- Target the suspected parameter with -p
- Escalate to --dbs only after confirmation

• Practice scoping SQLMap to a specific parameter
  Use -p to pin the vulnerable parameter and -C to select only the needed columns when dumping.
