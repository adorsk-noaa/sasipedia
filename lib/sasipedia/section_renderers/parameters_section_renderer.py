import sasipedia.templates as templates
from section_renderer import SectionRenderer


class ParametersSectionRenderer(SectionRenderer):

    def __init__(self, **kwargs):
        super(ParametersSectionRenderer, self).__init__(**kwargs)
        if not self.indexTemplate:
            template = templates.env.get_template('parameters_section_index.html')
            self.indexTemplate = template

    def generateMenu(self, section={}, **kwargs):
        # Get default menu item for section.
        menu = super(ParametersSectionRenderer, self).generateMenu(section=section)
        return menu
