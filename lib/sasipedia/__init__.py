from sasipedia.sasipedia_renderer import SASIPediaRenderer
import sasipedia.section_readers as section_readers
import sasipedia.section_renderers as section_renderers
import sasipedia.templates as templates

import csv
import os


def generate_sasipedia(targetDir=None, dataDir=None):

    # Create basic section definitions, in the
    # order in which the sections should be listed.
    sections = [
        {'id': 'substrates', 'label': 'Substrates'},
        {'id': 'gears', 'label': 'Gears',
         'renderer': section_renderers.DefaultSectionRenderer(
             indexTemplate=templates.env.get_template(
                 'gears_section_index.html'))
        },
        {'id': 'energies', 'label': 'Habitat Energy'},
        {'id': 'va', 'label': 'Vulnerability Assessment'},
    ]

    # Decorate sections w/ defaults.
    for section in sections:
        section['dir'] = os.path.join(dataDir, section['id'])
        section['menuBasePath'] = section['id']

    # Create sections lookup.
    sectionsDict = {}
    for section in sections:
        sectionsDict[section['id']] = section

    # Customize sections in which the metadata is stored
    # with the data.
    for sectionId in ['substrates', 'gears', 'va', 'energies']:
        section = sectionsDict.get(sectionId)
        section['metadataFile'] = os.path.join(
            dataDir, '%s.csv' % section['id'])

    # Add in features section.
    featureCategoriesPath = os.path.join(dataDir, 'feature_categories.csv')
    featuresPath = os.path.join(dataDir, 'features.csv')

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
        'id': 'features',
        'label': 'Features',
        'menuBasePath': 'features',
        'data': featuresData,
        'sort': True,
        'renderer': section_renderers.FeaturesSectionRenderer()
    }
    sections.append(featuresSection)

    # Generate model parameters section.
    paramsPath = os.path.join(dataDir, 'model_parameters.csv')
    if os.path.isfile(paramsPath):
        with open(paramsPath, 'rb') as f:
            params = csv.DictReader(f).next()

        paramsSection = {
            'id': 'model_parameters',
            'label': 'Model Parameters',
            'menuBasePath': 'model_parameters',
            'data': {
                'params': params
            },
            'renderer': section_renderers.ParametersSectionRenderer()
        }
        sections.append(paramsSection)

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
        sections=sections,
    )
