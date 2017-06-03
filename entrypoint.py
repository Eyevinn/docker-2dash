#!/usr/bin/env python
import argparse
from subprocess import call
import re
import glob

parser = argparse.ArgumentParser(description='Create MPEG DASH')
parser.add_argument('sourcefiles', metavar='SRC', nargs='+', help='source media files')
parser.add_argument('--hls', action='store_true', help='source is an HLS manifest URL')
parser.add_argument('--workdir', help='specify a working directory, default is /mnt/')
args = parser.parse_args()

workdir = '/mnt'
if args.workdir:
  workdir = args.workdir

mp4fragments = []
sources = []
if args.hls:
  cmdline = ['hls-downloader', args.sourcefiles[0], 'tmpfile']
  call(cmdline)
  sources.extend(glob.glob('tmpfile-*.mp4'))
  if len(sources) < 1:
    print "HLS could not be downloaded"
else:
  sources.extend(args.sourcefiles)

for srcfile in sources:
  m = re.match('^(.*).mp4$', srcfile)
  if m:
    outfile = '%s.fmp4' % m.groups(2)
    cmdline = ['mp4fragment', '%s/%s' % (workdir, srcfile), outfile]
    call(cmdline)
    mp4fragments.append(outfile)

if len(mp4fragments) > 0:
  cmdline = ['python', '/opt/Bento4/Python/utils/mp4-dash.py', '--exec-dir', '/opt/Bento4/', '-o', '%s/output' % workdir]
  cmdline.extend(mp4fragments)
  call(cmdline)