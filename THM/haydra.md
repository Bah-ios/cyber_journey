I successfully navigated SSH authentication and accessed molly's home directory to retrieve Flag 2, demonstrating effective credential recovery and shell access.

Recovering valid credentials and obtaining shell access are core penetration testing milestones; file enumeration validates post-compromise access.

Flow:
- Target machine accessed via HTTP
- SSH shell access confirmed via file read
- Flag 2 retrieved from home directory

I demonstrated HTTP-based reconnaissance and accessed the target web application, establishing the foundation for form-based credential testing.

Proper target enumeration and form analysis prevent brute force failures from missing field names or incorrect endpoints.

Flow:
- Target web application reached
- Login form identified
- Form parameters confirmed for brute force

Improvements

• Capture live login traffic with a proxy
  Use Burp Suite or OWASP ZAP to intercept a real login attempt. Copy the exact POST body, path, and response to eliminate field-name guessing.

• Detect and handle CSRF tokens in forms
  Before brute forcing, inspect the HTML for hidden inputs (CSRF tokens, nonces). Extract and rotate them if the server enforces freshness.
