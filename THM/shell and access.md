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
