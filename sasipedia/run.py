from sasipedia.sasipedia_generator import SASIPediaGenerator

import sys
import os
import tempfile


def main():
    #targetDir = tempfile.mkdtemp(suffix=".sasipedia")
    targetDir = "/tmp/sasipedia"
    if os.path.exists(targetDir):
        os.removedirs(targetDir)
    os.mkdir(targetDir)
    print >> sys.stderr, "targetDir is: ", targetDir

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "testData")

    sections = [
        {
            'name': 'substrates',
            'label': 'Substrates',
            'dir': os.path.join(dataDir, 'substrates')
        },
    ]

    generator = SASIPediaGenerator()
    generator.generateSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        sections=sections
    )

if __name__ == '__main__':
    main()
