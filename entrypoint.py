#!/usr/bin/env python
import argparse
from subprocess import call
import re

parser = argparse.ArgumentParser(description='Create MPEG DASH')
parser.add_argument('sourcefiles', metavar='SRC', nargs='+', help='source media files')
args = parser.parse_args()

mp4fragments = []
for srcfile in args.sourcefiles:
  m = re.match('^(.*).mp4$', srcfile)
  if m:
    outfile = '%s.fmp4' % m.groups(2)
    cmdline = ['mp4fragment', '/mnt/%s' % srcfile, outfile]
    call(cmdline)
    mp4fragments.append(outfile)

if len(mp4fragments) > 0:
  cmdline = ['python', '/opt/Bento4/Python/utils/mp4-dash.py', '--exec-dir', '/opt/Bento4/', '-o', '/mnt/output']
  cmdline.extend(mp4fragments)
  call(cmdline)