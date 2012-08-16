import templates
from section_renderer import SectionRenderer


class DefaultSectionRenderer(SectionRenderer):

    indexTemplate = templates.env.get_template('default_section_index.html')

    def generateMenu(self, section={}, sectionData=[]):
        rootPath = section.get('menuPath')

        # Initialize menu with section link.
        menu = {
            'href': rootPath,
            'label': section.get('label')
        }

        # If there were rows , add menu items for them.
        if sectionData.get('rows'):
            menu['children'] = []
            for row in sectionData['rows']:
                menuItem = {
                    'href': "%s#%s" % (rootPath, row.get('id')),
                    'label': row.get('label')
                }
                menu['children'].append(menuItem)

        return menu
