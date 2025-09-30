#!/usr/bin/env python3
"""
Generate complete project context for Claude Code
"""

import os
import json
from pathlib import Path
from datetime import datetime
import argparse

class ProjectContextGenerator:
    def __init__(self, project_root='.', output_file='PROJECT_CONTEXT_FULL.md'):
        self.project_root = Path(project_root)
        self.output_file = output_file
        self.ignore_patterns = {
            '__pycache__', '.git', 'venv', 'env', '.venv',
            '.pytest_cache', 'node_modules', '*.pyc',
            '.DS_Store', '*.log'
        }
        
    def should_include(self, path):
        """Check if file should be included"""
        path_str = str(path)
        for pattern in self.ignore_patterns:
            if pattern in path_str:
                return False
        return True
    
    def get_file_tree(self):
        """Generate file tree structure"""
        tree_lines = []
        for root, dirs, files in os.walk(self.project_root):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if not any(p in d for p in self.ignore_patterns)]
            
            level = root.replace(str(self.project_root), '').count(os.sep)
            indent = '  ' * level
            tree_lines.append(f"{indent}{os.path.basename(root)}/")
            
            subindent = '  ' * (level + 1)
            for file in files:
                if not any(p in file for p in self.ignore_patterns):
                    tree_lines.append(f"{subindent}{file}")
        
        return '\n'.join(tree_lines)
    
    def generate_context(self):
        """Generate the complete context file"""
        with open(self.output_file, 'w') as f:
            # Header
            f.write("# Complete Project Context\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n\n")
            
            # Project structure
            f.write("## Project Structure\n")
            f.write("```\n")
            f.write(self.get_file_tree())
            f.write("\n```\n\n")
            
            # Python files
            f.write("## Python Source Files\n\n")
            for py_file in self.project_root.rglob("*.py"):
                if self.should_include(py_file):
                    relative_path = py_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```python\n")
                    try:
                        f.write(py_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # Configuration files
            f.write("## Configuration Files\n\n")
            
            # YAML files
            for yaml_file in list(self.project_root.rglob("*.yaml")) + list(self.project_root.rglob("*.yml")):
                if self.should_include(yaml_file):
                    relative_path = yaml_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```yaml\n")
                    try:
                        f.write(yaml_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # JSON files
            for json_file in self.project_root.rglob("*.json"):
                if self.should_include(json_file) and 'package-lock' not in str(json_file):
                    relative_path = json_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```json\n")
                    try:
                        f.write(json_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # SQL files
            f.write("## Database Schema\n\n")
            for sql_file in self.project_root.rglob("*.sql"):
                if self.should_include(sql_file):
                    relative_path = sql_file.relative_to(self.project_root)
                    f.write(f"### {relative_path}\n")
                    f.write("```sql\n")
                    try:
                        f.write(sql_file.read_text())
                    except:
                        f.write("# Could not read file\n")
                    f.write("\n```\n\n")
            
            # Requirements
            if (self.project_root / "requirements.txt").exists():
                f.write("## Requirements\n")
                f.write("```\n")
                try:
                    f.write((self.project_root / "requirements.txt").read_text())
                except:
                    f.write("# Could not read file\n")
                f.write("\n```\n\n")
            
            # README
            if (self.project_root / "README.md").exists():
                f.write("## README\n")
                try:
                    f.write((self.project_root / "README.md").read_text())
                except:
                    f.write("# Could not read file\n")
                f.write("\n\n")
        
        # Print summary
        file_size = os.path.getsize(self.output_file) / 1024 / 1024  # MB
        with open(self.output_file, 'r') as f:
            line_count = sum(1 for _ in f)
        
        print(f"✅ Context file generated: {self.output_file}")
        print(f"�� File size: {file_size:.2f} MB")
        print(f"📝 Total lines: {line_count:,}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate project context')
    parser.add_argument('--root', default='.', help='Project root directory')
    parser.add_argument('--output', default='PROJECT_CONTEXT_FULL.md', help='Output file name')
    
    args = parser.parse_args()
    
    generator = ProjectContextGenerator(args.root, args.output)
    generator.generate_context()
