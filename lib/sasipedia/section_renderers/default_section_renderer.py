import sasipedia.templates as templates
from section_renderer import SectionRenderer


class DefaultSectionRenderer(SectionRenderer):

    def __init__(self, **kwargs):
        super(DefaultSectionRenderer, self).__init__(**kwargs)
        if not self.indexTemplate:
            template = templates.env.get_template('default_section_index.html')
            self.indexTemplate = template

    def generateMenu(self, section={}, sectionData=[]):
        # Get default menu item for section.
        menu = super(DefaultSectionRenderer, self).generateMenu(
            section=section,
            sectionData=sectionData
        )

        # If there were rows , add menu items for them.
        if sectionData.get('rows'):
            menu['children'] = []
            indexPath = menu['href']
            for row in sectionData['rows']:
                menuItem = {
                    'href': "%s#%s" % (indexPath, row.get('id')),
                    'label': row.get('label')
                }
                menu['children'].append(menuItem)

        return menu
