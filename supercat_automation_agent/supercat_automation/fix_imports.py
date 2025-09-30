# Fix the imports in website_evidence.py

with open('scrapers/website_evidence.py', 'r') as f:
    lines = f.readlines()

# Find and fix the typing import line
for i, line in enumerate(lines):
    if 'from typing import' in line and 'Optional' not in line:
        # Add Optional to the imports
        if line.strip().endswith('Any'):
            lines[i] = line.rstrip() + ', Optional\n'
        else:
            lines[i] = line.replace('\n', ', Optional\n')
        print(f"✅ Added Optional to imports on line {i+1}")
        break

# Write back
with open('scrapers/website_evidence.py', 'w') as f:
    f.writelines(lines)

print("✅ Fixed imports!")
