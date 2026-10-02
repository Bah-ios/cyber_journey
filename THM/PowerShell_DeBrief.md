Successfully navigated nested directories and retrieved file contents using sequential Get-Location, Get-ChildItem, and Get-Content cmdlets to expose hidden captain cabin artifacts.

Demonstrates practical file discovery workflow—essential for locating configuration files, logs, and forensic evidence on Windows systems.

Flow:
- Navigated cabin subdirectory
- Listed directory contents
- Read file contents sequentially

Systematically explored cmdlet discovery using Get-Command filters and consulted Get-Help with specific examples to understand command syntax and usage patterns.

Effective tool discovery and documentation consultation accelerates independent problem-solving and reduces trial-and-error approaches.

Flow:
- Listed available commands
- Filtered by name pattern
- Retrieved targeted help examples

Multiple navigation and discovery attempts were incomplete or abandoned. Tasks like listing captain directory contents and exploring Users directory lack follow-through or verification.

Incomplete reconnaissance leaves critical information unverified. In real administration, unfinished checks create blind spots and miss configuration issues.

Flow:
- Navigate captain directory
- Attempt command with typo
- Abandon exploration without resolution

Action Points 

• Complete directory inventory workflows
  When navigating to a target directory, always list contents with Get-ChildItem and verify the result. Avoid abandoning partial explorations; document findings before moving on.

• Combine file discovery with filtering and output control
  Use Get-ChildItem with Where-Object and Select-Object to filter results by property (e.g., size, date) and return only essential columns, reducing clutter in large directory listings.

• Apply aliases for speed without sacrificing clarity in scripts
  Recognize that ls and dir are aliases for Get-ChildItem, and cd for Set-Location. Use full names in production scripts and shared code; use aliases in interactive sessions for efficiency.