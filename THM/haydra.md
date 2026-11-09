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
