Successfully enumerated AWS EC2 metadata service (22 successful requests with HTTP 200). Demonstrates working knowledge of cloud reconnaissance.

AWS metadata service is a high-value recon target; successful access often yields credentials and instance roles.

Flow:
- Identified metadata endpoint
- Confirmed HTTP 200 availability
- Repeated queries demonstrate persistence


Successfully downloaded ELF payload via HTTP, escalated to root (sudo su), and accessed /etc/shadow—the most sensitive Linux credential store. Demonstrates complete privilege escalation chain.

Reading /etc/shadow is the culmination of a privilege escalation chain. Access to hashed passwords enables offline cracking and lateral movement.

Flow:
- Downloaded reverse shell payload
- Escalated permissions with sudo
- Accessed shadow file successfully


Imporvement 

Flow:
- Execute grep with varying patterns
- Commands fail (returnValue=1)
- No validation of prior step output