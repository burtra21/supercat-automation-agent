import re

# Read the file
with open('scrapers/website_evidence.py', 'r') as f:
    content = f.read()

# Fix the type hints - replace | None with Optional
content = content.replace('-> str | None:', '-> Optional[str]:')

# Make sure Optional is imported
if 'from typing import' in content and 'Optional' not in content:
    # Add Optional to the imports
    content = content.replace(
        'from typing import Dict, List, Any',
        'from typing import Dict, List, Any, Optional'
    )

# Write back
with open('scrapers/website_evidence.py', 'w') as f:
    f.write(content)

print("✅ Fixed type hints for Python 3.9 compatibility")
