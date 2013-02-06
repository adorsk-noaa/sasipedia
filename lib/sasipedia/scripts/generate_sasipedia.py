import sasipedia
import tempfile
import shutil
import os
import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument('input')
argparser.add_argument('--output', '-o')
args = argparser.parse_args()

if not args.output:
    args.output = tempfile.mkdtemp(prefix="sasipedia.")

sasipedia.generate_sasipedia(targetDir=args.output, dataDir=args.input)
print "Generated sasipedia at '%s'."  % args.output
