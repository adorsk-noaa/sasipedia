from sasipedia.sasipedia_renderer import SASIPediaRenderer
import sasipedia.section_renderers as section_renderers

import sys
import os
import shutil
import tempfile

def main():
    targetDir = "/tmp/sasipedia.vaSection"
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)
    os.mkdir(targetDir)
    print >> sys.stderr, "targetDir is: ", targetDir

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "..", "testData")

    sections = [
        {
            'name': 'va',
            'label': 'Vulnerability Assessment',
            'dir': os.path.join(dataDir, 'va'),
            'menuPath': 'va/index.html',
            'renderer': section_renderers.VASectionRenderer()
        },
    ]

    renderer = SASIPediaRenderer()
    renderer.renderSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        sections=sections
    )

if __name__ == '__main__':
    main()
