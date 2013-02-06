from sasipedia.sasipedia_renderer import SASIPediaRenderer
import sasipedia.section_readers as section_readers
import sasipedia.section_renderers as section_renderers
import sasipedia.templates as templates

import csv
import os


def generate_sasipedia(targetDir=None, dataDir=None):

    # Set location of overview file.
    overviewFile = os.path.join(dataDir, 'description.txt')

    # Create basic section definitions, in the
    # order in which the sections should be listed.
    sections = [
        {'id': 'substrates', 'label': 'Substrates'},
        {'id': 'gears', 'label': 'Gears'},
        {'id': 'energies', 'label': 'Habitat Energy'},
        {'id': 'efforts', 'label': 'Fishing Efforts'},
        {'id': 'model_parameters', 'label': 'Model Parameters'},
        {'id': 'map_layers', 'label': 'Map Layers'},
        {'id': 'glossary', 'label': 'Glossary'},
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

    # Customize sections in which the metadata is stored
    # with the data.
    for sectionId in ['substrates', 'gears', 'va', 'energies']:
        section = sectionsDict.get(sectionId)
        if (section):
            section['metadataFile'] = os.path.join(dataDir, section['id'],
                'data', '%s.csv' % section['id'])

    # Add in sections for feature categories.
    featureCategoriesPath = os.path.join(dataDir, 'feature_categories', 'data',
                                         'feature_categories.csv')
    featuresDir = os.path.join(dataDir, 'features')
    if os.path.isfile(featureCategoriesPath):

        def getFilterFn(category_id):
            def categoryFilter(row):
                return row['category'] == category_id
            return categoryFilter

        with open(featureCategoriesPath, 'rb') as f:
            for category_row in csv.DictReader(f):
                sectionId = 'feature_category_' + category_row['id']
                section = {
                    'dir': featuresDir,
                    'id': sectionId,
                    'label': category_row['label'],
                    'metadataFile': os.path.join(featuresDir, 'data', 
                                                 'features.csv'),
                    'description': category_row.get('description'),
                    'menuBasePath': sectionId,
                    'sort': True,
                }


                section['reader'] = section_readers.CSVSectionReader(
                    filters=[getFilterFn(category_row['id'])])
                sections.append(section)

    # Customize sections which use description.txt files
    # for metadata.
    for sectionId in ['efforts', 'model_parameters']:
        section = sectionsDict.get(sectionId)
        if (section):
            indexTemplate = templates.env.get_template('content_section_index.html')
            section['metadataFile'] = os.path.join(dataDir, section['id'],
                'metadata', 'description.txt')
            section['reader'] = section_readers.FileSectionReader()
            section['renderer'] = section_renderers.SectionRenderer(
                indexTemplate=indexTemplate
            )

    # Customize va.
    for sectionId in ['va']:
        section = sectionsDict.get(sectionId)
        if (section):
            indexTemplate = templates.env.get_template('va_section_index.html')
            section['renderer'] = section_renderers.SectionRenderer(
                indexTemplate=indexTemplate
            )

    renderer = SASIPediaRenderer()
    renderer.renderSASIPedia(
        targetDir=targetDir,
        dataDir=dataDir,
        overviewFile=overviewFile,
        sections=sections,
    )
