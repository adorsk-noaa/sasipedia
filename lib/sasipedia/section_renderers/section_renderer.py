import os
import shutil


class SectionRenderer(object):

    def __init__(self, indexTemplate=None):
        self.indexTemplate = indexTemplate

    """
    Renders a metadata directory for a given section.
    """
    def renderSection(self, section=None, targetDir=None, sectionData=None,
                        baseUrl=""):
        # Setup the target dir.
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)

        # Generate the index file.
        indexFile = os.path.join(targetDir, "index.html")
        self.renderIndexFile(
            section=section,
            sectionData=sectionData,
            indexFile=indexFile,
            baseUrl=baseUrl
        )

        # Generate and return the section's menu.
        return self.generateMenu(section=section, sectionData=sectionData)

    def renderIndexFile(self, section={}, sectionData=[], indexFile=None,
                        baseUrl="", **kwargs):
        """
        Renders a section index file from section data.
        """
        # Setup the index file.
        fh = open(indexFile, "wb")

        # Render the index file template.
        content = self.indexTemplate.render(
            baseUrl=baseUrl,
            section=section,
            sectionData=sectionData,
        )
        fh.write(content)
        fh.close()

    def generateMenu(self, section={}, **kwargs):
        """
        Default menu generation function.
        Most subclasses will override or wrap this.
        """
        # Initialize menu with section link.
        menu = {
            'href': '%s/index.html' % section.get('menuBasePath'),
            'label': section.get('label')
        }
        return menu
