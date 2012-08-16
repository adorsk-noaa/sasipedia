import templates
from section_renderer import SectionRenderer


class VASectionRenderer(SectionRenderer):
    """
    Generates a metadata section for the Vulnerability Assessment.
    """

    indexTemplate = templates.env.get_template('va_section_index.html')

    def generateMenu(self, section={}, sectionData=[]):
        menu = {
            'href': section.get('menuPath'),
            'label': section.get('label')
        }

        return menu
