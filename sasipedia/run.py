import sasipedia

import sys
import os
import tempfile


def main():
    targetDir = tempfile.mkdtemp(suffix=".sasipedia")
    print >> sys.stderr, "targetDir is: ", targetDir

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "testData")

    sections = [
        {'name': 'substrates'},
    ]

    generator = sasipedia.SASIPediaGenerator()
    generator.generateSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        sections=sections
    )

if __name__ == '__main__':
    main()
