from sasipedia.sasipedia_renderer import SASIPediaRenderer

import sys
import os
import shutil
import tempfile


def main():
    #targetDir = tempfile.mkdtemp(suffix=".sasipedia")
    targetDir = "/tmp/sasipedia"
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)
    os.mkdir(targetDir)
    print >> sys.stderr, "targetDir is: ", targetDir

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "testData")

    # Create basic section definitions.
    sections = {
        'substrates': {
            'label': 'Substrates',
        },
        'map_layers': {
            'label': 'Map Layers',
        },
    }

    # Decorate sections w/ defaults.
    for sectionId, section in sections.items():
        section['id'] = sectionId
        section['dir'] = os.path.join(dataDir, sectionId)
        section['metadataFile'] = os.path.join(dataDir, sectionId, 'metadata', 
                                               '%s.csv' % sectionId)
        section['metadataAssetsDir'] = os.path.join(dataDir, sectionId, 'metadata',
                                           'assets')
        section['menuBasePath'] = sectionId

    # Customize substrates to use data file as metadat file.
    for sectionId in ['substrates']:
        section = sections[sectionId]
        section['metadataFile'] = os.path.join(dataDir, sectionId, 'data',
                                               '%s.csv' % sectionId)

    # Set order for sections.
    orderedSectionIds = [
        'substrates',
        'map_layers'
    ]
    orderedSections = []
    for sectionId in orderedSectionIds:
        orderedSections.append(sections[sectionId])

    renderer = SASIPediaRenderer()
    renderer.renderSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        sections=orderedSections,
    )

if __name__ == '__main__':
    main()
