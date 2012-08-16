import os
import shutil


class SectionRenderer(object):

    indexTemplate = None

    """
    Renders a metadata directory for a given section.
    """
    def renderSection(self, section=None, targetDir=None, sectionData=None,
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
        self.renderIndexFile(
            section=section,
            sectionData=sectionData,
            indexFile=indexFile,
            imagesDir="assets/images",
            baseUrl=baseUrl
        )

        # Generate and return the section's menu.
        return self.generateMenu(section=section, sectionData=sectionData)

    def renderIndexFile(self, section={}, sectionData=[], indexFile=None,
                          imagesDir="", baseUrl=""):
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
            imagesDir=imagesDir,
        )
        fh.write(content)
        fh.close()

    def generateMenu(self):
        pass
