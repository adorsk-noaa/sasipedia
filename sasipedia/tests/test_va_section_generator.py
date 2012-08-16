from sasipedia.sasipedia_generator import SASIPediaGenerator

import sys
import os
import shutil
import tempfile
import section_renderers

def main():
    #targetDir = tempfile.mkdtemp(suffix=".sasipedia")
    targetDir = "/tmp/sasipedia.vaSection"
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)
    os.mkdir(targetDir)
    print >> sys.stderr, "targetDir is: ", targetDir

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "..", "testData")

    sections = [
        {
            'name': 'vulernabilityAssessment',
            'label': 'Vulnerability Assessment',
            'dir': os.path.join(dataDir, 'substrates'),
            'menuPath': 'va/index.html',
            'renderer': section_renderers.VASectionRenderer
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