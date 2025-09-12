#!/usr/bin/env python3
import os
import re

def extract_permlink(file_path):
    """Extract permlink from front matter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for permlink in front matter
        permlink_match = re.search(r'permlink:\s*([^\n]+)', content)
        if permlink_match:
            permlink = permlink_match.group(1).strip()
            if permlink.startswith('/'):
                return permlink
            else:
                return '/' + permlink
    except:
        pass
    return None

def get_url_from_path(file_path):
    """Determine URL from file path"""
    # Remove leading ./ and file extension
    path = file_path.replace('./', '').replace('.md', '').replace('.html', '')
    
    # For index.md files, use the directory name
    if path.endswith('/index'):
        return '/' + path.replace('/index', '')
    
    # For root index.md, use /
    if path == 'index':
        return '/'
    
    # For other files, use the path
    return '/' + path

def main():
    print("Jekyll Page URL Mapping")
    print("=" * 50)
    
    # Find all markdown and html files
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and _site
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '_site' and d != 'vendor']
        
        for file in files:
            if file.endswith(('.md', '.html')) and not file.startswith('.'):
                file_path = os.path.join(root, file)
                permlink = extract_permlink(file_path)
                
                if permlink:
                    url = permlink
                else:
                    url = get_url_from_path(file_path)
                
                print(f"File: {file_path}")
                print(f"URL:  {url}")
                print("-" * 30)

if __name__ == "__main__":
    main()
