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

    # Add in features section.
    featureCategoriesPath = os.path.join(dataDir, 'feature_categories', 'data',
                                         'feature_categories.csv')
    featuresDir = os.path.join(dataDir, 'features')
    featuresPath = os.path.join(featuresDir, 'data', 'features.csv')

    # Get feature rows.
    featureRows = {}
    if os.path.isfile(featuresPath):
        with open(featuresPath, 'rb') as f:
            featureRows = [row for row in csv.DictReader(f)]

    featuresData = {'categories': []}
    if os.path.isfile(featureCategoriesPath):
        with open(featureCategoriesPath, 'rb') as f:
            for categoryRow in csv.DictReader(f):
                categoryFeatures = []
                for featureRow in featureRows:
                    if featureRow.get('category') == categoryRow['id']:
                        categoryFeatures.append(featureRow)
                categoryFeatures.sort(
                    key=lambda r: row.get('label', row.get('id')))
                featuresData['categories'].append({
                    'id': categoryRow['id'],
                    'label': categoryRow.get('label'),
                    'description': categoryRow.get('description'),
                    'features': categoryFeatures,
                })

    featuresSection = {
        'dir': featuresDir,
        'id': 'features',
        'label': 'Features',
        'menuBasePath': 'features',
        'data': featuresData,
        'sort': True,
        'renderer': section_renderers.FeaturesSectionRenderer()
    }
    sections.append(featuresSection)

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
