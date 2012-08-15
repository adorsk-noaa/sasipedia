import sasipedia

import sys
import tempfile

def main():
    targetDir = tempfile.mkdtemp(suffix=".sasipedia")
    print >> sys.stderr, "targetDir is: ", targetDir


if __name__ == '__main__':
    main()

