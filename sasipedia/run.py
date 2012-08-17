from sasipedia.sasipedia_renderer import SASIPediaRenderer
import sasipedia.section_readers as section_readers

import os
import shutil


def main():
    targetDir = "/tmp/sasipedia"
    if os.path.exists(targetDir):
        shutil.rmtree(targetDir)
    os.mkdir(targetDir)

    thisDir = os.path.dirname(os.path.realpath(__file__))
    dataDir = os.path.join(thisDir, "..", "testData")

    # Create basic section definitions, in the
    # order in which the sections should be listed.
    sections = [
        {'id': 'substrates', 'label': 'Substrates'},
        {'id': 'bio_features', 'label': 'Biological Features'},
        {'id': 'geo_features', 'label': 'Geological Features'},
        {'id': 'map_layers', 'label': 'Map Layers'},
        {'id': 'glossary', 'label': 'Glossary'},
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

    # Customize substrates to use data file as metadata file.
    for sectionId in ['substrates']:
        section = sectionsDict[sectionId]
        section['metadataFile'] = os.path.join(dataDir, section['id'], 'data',
                                               '%s.csv' % section['id'])

    # Customize features to use data file, and to filter by feature category.
    for featureCategory in ['bio', 'geo']:
        section = sectionsDict[featureCategory + '_features']
        section['metadataFile'] = os.path.join(dataDir, 'features', 'data',
                                               'features.csv')

        def categoryFilter(row, category=featureCategory):
            return row['category'] == category

        section['reader'] = section_readers.CSVSectionReader(
            filters=[categoryFilter])

    renderer = SASIPediaRenderer()
    renderer.renderSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        sections=sections,
    )

if __name__ == '__main__':
    main()
