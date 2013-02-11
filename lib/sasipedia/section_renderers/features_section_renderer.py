import sasipedia.templates as templates
from section_renderer import SectionRenderer


class FeaturesSectionRenderer(SectionRenderer):

    def __init__(self, **kwargs):
        super(FeaturesSectionRenderer, self).__init__(**kwargs)
        if not self.indexTemplate:
            template = templates.env.get_template('features_section_index.html')
            self.indexTemplate = template

    def generateMenu(self, section={}, sectionData=[]):
        # Get default menu item for section.
        menu = super(FeaturesSectionRenderer, self).generateMenu(
            section=section,
            sectionData=sectionData
        )

        # Add menu items for categories.
        if sectionData.get('categories'):
            indexPath = menu['href']
            menu['children'] = []
            for category in sectionData['categories']:
                categoryItem = {
                    'href': "%s#%s" % (indexPath, category.get('id')),
                    'label': category.get('label', category.get('id', 'Unknown'))
                }
                menu['children'].append(categoryItem)

                featureItems = categoryItem.setdefault('children', [])
                for feature in category['features']:
                    featureItems.append({
                        'href': "%s#%s__%s" % (indexPath, category.get('id'),
                                               feature.get('id')),
                        'label': feature.get(
                            'label', feature.get('id', 'Unknown')),
                    })

        return menu
