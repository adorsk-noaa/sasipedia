from sasipedia.sasipedia_renderer import SASIPediaRenderer
import sasipedia.section_renderers as section_renderers
import sasipedia.templates as templates

import sys
import os
import shutil


def main():
    targetDir = "/tmp/sasipedia.vaSection"
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)
    os.mkdir(targetDir)
    print >> sys.stderr, "targetDir is: ", targetDir

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "..", "testData")

    sections = [
        {'id': 'va', 'label': 'Vulnerability Assessment'},
    ]

    # Decorate sections w/ defaults.
    for section in sections:
        section['dir'] = os.path.join(dataDir, section['id'])
        section['metadataFile'] = os.path.join(dataDir, section['id'],
            'metadata', '%s.csv' % section['id'])
        section['metadataAssetsDir'] = os.path.join(dataDir, section['id'],
            'metadata', 'assets')
        section['menuBasePath'] = section['id']

    # Create sections lookup.
    sectionsDict = {}
    for section in sections:
        sectionsDict[section['id']] = section

    # Customize va to use data file as metadata file,
    # and to use custom renderer.
    for sectionId in ['va']:
        section = sectionsDict[sectionId]
        section['metadataFile'] = os.path.join(dataDir, section['id'], 'data',
                                               '%s.csv' % section['id'])
        section['renderer'] = section_renderers.SectionRenderer(
            indexTemplate=templates.env.get_template('va_section_index.html')
        )

    renderer = SASIPediaRenderer()
    renderer.renderSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        sections=sections
    )

if __name__ == '__main__':
    main()
