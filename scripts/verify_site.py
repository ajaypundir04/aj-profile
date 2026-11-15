#!/usr/bin/env python3
"""
CI verification script for GitHub Actions deployment pipeline.
Validates question data integrity, asset references, and essential pages.
"""
import os
import re
import json
import sys

def verify():
    print("=" * 60)
    print("Starting CI Pre-Deployment Verification...")
    print("=" * 60)

    # 1. Essential files
    essential_files = [
        'index.html',
        '.nojekyll',
        'resume_ajay_pundir.pdf',
        'blog/index.html',
        'blog/dsa.html',
        'blog/system-design.html',
        'blog/security.html',
        'blog/ai.html',
        'assets/css/style.css',
        'assets/css/blog.css',
        'assets/js/main.js',
        'assets/js/blog.js'
    ]
    for f in essential_files:
        if not os.path.isfile(f):
            print(f"❌ Missing essential file: {f}")
            sys.exit(1)
        print(f"✅ Found file: {f}")

    # 2. Check question data counts
    data_files = [
        ('DSA', 'assets/js/data/dsa.js'),
        ('System Design', 'assets/js/data/system-design.js'),
        ('Security & IAM', 'assets/js/data/security.js'),
        ('AI & Machine Learning', 'assets/js/data/ai.js')
    ]
    total_questions = 0
    for name, path in data_files:
        if not os.path.isfile(path):
            print(f"❌ Missing dataset: {path}")
            sys.exit(1)
        with open(path, 'r', encoding='utf-8') as fp:
            content = fp.read()
        try:
            start = content.index('[')
            end = content.rindex(']') + 1
            data = json.loads(content[start:end])
        except Exception as e:
            print(f"❌ Failed to parse JSON in {path}: {e}")
            sys.exit(1)
        
        count = len(data)
        if count < 100:
            print(f"❌ Track {name} has only {count} questions, expected >= 100")
            sys.exit(1)
        print(f"✅ Track '{name}': {count} questions verified")
        total_questions += count

    print(f"🎉 Total Verified Questions: {total_questions}")

    # 3. Check HTML asset links
    html_files = [
        'index.html',
        'blog/index.html',
        'blog/dsa.html',
        'blog/system-design.html',
        'blog/security.html',
        'blog/ai.html'
    ]
    for h in html_files:
        with open(h, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Script tags
        scripts = re.findall(r'<script[^>]+src=[\"\'](.*?)[\"\']', content)
        for s in scripts:
            target = os.path.normpath(os.path.join(os.path.dirname(h), s))
            if not os.path.isfile(target):
                print(f"❌ Broken script reference in {h}: {s} -> {target}")
                sys.exit(1)
        # CSS links
        styles = re.findall(r'<link[^>]+href=[\"\'](assets/css/.*?\.css|\.\./assets/css/.*?\.css)[\"\']', content)
        for st in styles:
            target = os.path.normpath(os.path.join(os.path.dirname(h), st))
            if not os.path.isfile(target):
                print(f"❌ Broken stylesheet reference in {h}: {st} -> {target}")
                sys.exit(1)
        print(f"✅ Verified asset references in: {h}")

    print("=" * 60)
    print("✅ All Pre-Deployment Checks Passed Successfully!")
    print("=" * 60)

if __name__ == '__main__':
    verify()
