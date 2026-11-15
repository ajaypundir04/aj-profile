#!/usr/bin/env python3
"""
CI verification script for GitHub Actions deployment pipeline.
Validates question data integrity, German grammar hub integrity (A1-C2), asset references, and essential pages.
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
        'assets/js/blog.js',
        # German Grammar Hub files
        'deutsche/index.html',
        'deutsche/a1.html',
        'deutsche/a2.html',
        'deutsche/b1.html',
        'deutsche/b2.html',
        'deutsche/c1.html',
        'deutsche/c2.html',
        'deutsche/css/german.css',
        'deutsche/js/german.js'
    ]
    for f in essential_files:
        if not os.path.isfile(f):
            print(f"❌ Missing essential file: {f}")
            sys.exit(1)
        print(f"✅ Found file: {f}")

    # 2. Check question data counts (Blog Tracks)
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

    print(f"🎉 Total Verified Blog Questions: {total_questions}")

    # 3. Check German Grammar Datasets (A1 to C2 >= 100 topics each)
    german_files = [
        ('A1 - Grundstufe I', 'deutsche/data/a1.js'),
        ('A2 - Grundstufe II', 'deutsche/data/a2.js'),
        ('B1 - Mittelstufe I', 'deutsche/data/b1.js'),
        ('B2 - Mittelstufe II', 'deutsche/data/b2.js'),
        ('C1 - Oberstufe I', 'deutsche/data/c1.js'),
        ('C2 - Meisterschaft', 'deutsche/data/c2.js')
    ]
    total_german_topics = 0
    for name, path in german_files:
        if not os.path.isfile(path):
            print(f"❌ Missing German dataset: {path}")
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
            print(f"❌ German level {name} has only {count} topics, expected >= 100")
            sys.exit(1)
        print(f"✅ German Level '{name}': {count} topics verified")
        total_german_topics += count

    print(f"🎉 Total Verified German Grammar Topics: {total_german_topics}")

    # 4. Check HTML asset links across all pages
    html_files = [
        'index.html',
        'blog/index.html',
        'blog/dsa.html',
        'blog/system-design.html',
        'blog/security.html',
        'blog/ai.html',
        'deutsche/index.html',
        'deutsche/a1.html',
        'deutsche/a2.html',
        'deutsche/b1.html',
        'deutsche/b2.html',
        'deutsche/c1.html',
        'deutsche/c2.html'
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
        styles = re.findall(r'<link[^>]+(?:rel=[\"\']stylesheet[\"\'][^>]+)?href=[\"\']([^\"\']+\.css)[\"\']', content)
        for st in styles:
            if st.startswith('http'):
                continue
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
