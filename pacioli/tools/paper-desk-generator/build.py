#!/usr/bin/env python3
"""Assemble a Paper Desk page: shared helpers + accordion helpers + a page body.

Usage:  python3 -I build.py bodies/np_body.py > out.html
Then:   python3 -I validate.py out.html     (needs tok.css next to it)
        python3 shot.py                     (edit the filenames at the top)
"""
import sys
s = open(__file__.replace('build.py', 'helpers_source.py')).read()
head = s[:s.index('# =====================================================================\n# 1. HERO')]
acc = s[s.index('def acc_item'):s.index('\ncore = [')]
body = open(sys.argv[1]).read()
exec(compile(head + '\n' + acc + '\n' + body, 'paper_desk_page', 'exec'), {'__name__': 'paper_desk'})
