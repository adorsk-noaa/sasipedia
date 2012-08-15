import templates
import os
import shutil

class DefaultSectionGenerator(object):
    """
    Generates a metadata directory for a given section.
    """
    def generateSection(self, section=None, targetDir=None, sectionData=None,
                        baseUrl=""):
        # Setup the target dir.
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)

        # Setup the assets dir.
        assetsDir = os.path.join(targetDir, "assets")
        if not os.path.exists(assetsDir):
            os.makedirs(assetsDir)

        # Copy images.
        imagesSrcDir = os.path.join(section.get('dir'), 'images')
        if os.path.exists(imagesSrcDir):
            imagesTargetDir = os.path.join(assetsDir, "images")
            shutil.copytree(imagesSrcDir, imagesTargetDir)

        # Generate the index file.
        indexFile = os.path.join(targetDir, "index.html")
        self.generateIndexFile(
            section=section,
            sectionData=sectionData,
            indexFile=indexFile,
            imagesDir="assets/images",
            baseUrl=baseUrl
        )

        # Generate and return the section's menu.
        return self.generateMenu(section=section, sectionData=sectionData)

    def generateIndexFile(self, section={}, sectionData=[], indexFile=None,
                          imagesDir="", baseUrl=""):
        """
        Generates a section index file from section data.
        """
        # Setup the index file.
        fh = open(indexFile, "wb")

        # Render the index file template.
        template = templates.env.get_template('default_section_index.html')
        content = template.render(
            baseUrl=baseUrl,
            section=section,
            sectionData=sectionData,
            imagesDir=imagesDir,
        )
        fh.write(content)
        fh.close()

    def generateMenu(self, section={}, sectionData=[]):
        rootPath = section.get('menuPath')

        # Initialize menu with section link.
        menu = {
            'href': rootPath,
            'label': section.get('label')
        }

        # If there were records, add menu items for them.
        if sectionData:
            menu['children'] = []
            for record in sectionData:
                menuItem = {
                    'href': "%s#%s" % (rootPath, record.get('id')),
                    'label': record.get('label')
                }
                menu['children'].append(menuItem)

        return menu
