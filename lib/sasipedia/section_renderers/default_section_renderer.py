import sasipedia.templates as templates
from section_renderer import SectionRenderer


class DefaultSectionRenderer(SectionRenderer):

    def __init__(self, **kwargs):
        super(DefaultSectionRenderer, self).__init__(**kwargs)
        if not self.indexTemplate:
            template = templates.env.get_template('default_section_index.html')
            self.indexTemplate = template

    def generateMenu(self, section={}, sectionData=[]):

        # Sort rows if sorting flag set.
        if section.get('sort'):
            def sortFunc(row):
                return row.get('label', row.get('id'))
            if (sectionData['rows']):
                sectionData['rows'].sort(key=sortFunc)

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
                    'label': row.get('label', row.get('id', 'Unknown'))
                }
                menu['children'].append(menuItem)

        return menu
