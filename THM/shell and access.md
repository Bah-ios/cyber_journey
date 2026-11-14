Obtained interactive shell access through command injection and retrieved the root-directory flag, confirming the first exploitation path.

Demonstrates end-to-end exploitation from injection to evidence collection.

Flow:
- Command injection triggered reverse shell
- Shell enumerated root directory
- Flag file read successfully
  
Uploaded a PHP web shell through the unrestricted upload endpoint and confirmed command execution via the cmd parameter.

Shows how file upload flaws lead directly to remote command execution on the server.

Flow:
- Uploaded shell.php to upload endpoint
- Verified execution through cmd parameter
- Enumerated system via web shell

Multiple reverse shell payloads were submitted with malformed syntax and wrong separators before a working callback was established.

Careful payload construction and testing reduces noise and avoids tripping defenses with repeated failed exploit attempts.

Flow:
- Submit reverse shell payload via command injection
- Payload separators and quoting were inconsistent
- Retried several variants before shell connected

• Stabilize shells before enumerating
  Upgrade the TTY (python3 -c 'import pty; pty.spawn("/bin/bash")') for better stability before exploring.
