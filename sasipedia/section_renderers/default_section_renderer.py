import sasipedia.templates as templates
from section_renderer import SectionRenderer


class DefaultSectionRenderer(SectionRenderer):

    indexTemplate = templates.env.get_template('default_section_index.html')

    def generateMenu(self, section={}, sectionData=[]):
        basePath = section.get('menuBasePath')

        # Initialize menu with section link.
        indexPath = '%s/index.html' % basePath
        menu = {
            'href': indexPath,
            'label': section.get('label')
        }

        # If there were rows , add menu items for them.
        if sectionData.get('rows'):
            menu['children'] = []
            for row in sectionData['rows']:
                menuItem = {
                    'href': "%s#%s" % (indexPath, row.get('id')),
                    'label': row.get('label')
                }
                menu['children'].append(menuItem)

        return menu
