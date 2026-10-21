Successfully executed John with rockyou against a RAR hash file and recovered the password. Immediately accessed and read the extracted flag file (`cat flag.txt`), demonstrating end-to-end archive cracking.

Archive password recovery is a critical real-world skill—encrypted archives often contain sensitive data. Executing this attack chain cleanly shows competence in offline cracking workflows.

Flow:
- RAR hash targeted with rockyou wordlist
- Password cracked and verified
- Flag file read from extracted archive

Located and inspected the SSH private key file (id_rsa) in Task11, displaying the key content and preparing for passphrase cracking. This demonstrates understanding of SSH key structure and the setup required for ssh2john conversion.

Recognizing and accessing SSH keys is fundamental to credential recovery. Inspecting key format before cracking ensures correct tool selection (ssh2john for passphrase-protected keys).

Flow:
- Navigated to Task11 directory
- Read and examined id_rsa private key file
- Prepared for subsequent cracking workflow