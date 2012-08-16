import os
import shutil
import sys

import templates
import section_readers
import section_renderers

class SASIPediaRenderer(object):
    """
    A Class for rendering SASIPedia metadata.
    """
    def renderSASIPedia(self, targetDir=None, dataDir=None, sections=None,
                          baseUrl=""):
        """
        Render a set of static 'SASIpedia' pages at the given target
        directory.
        """
        # Setup the directory.
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)

        # Copy the assets dir.
        thisDir = os.path.dirname(os.path.realpath(__file__))
        assetsSrcDir = os.path.join(thisDir, "assets")
        assetsTargetDir = os.path.join(targetDir, "assets")
        shutil.copytree(assetsSrcDir, assetsTargetDir)

        # Create sections.
        sectionMenus = []
        for section in sections:
            sectionMenu = self.renderSection(section, targetDir, dataDir,
                                               baseUrl="")
            sectionMenus.append(sectionMenu)

        # Initialize list of menu items.
        menuItems = []

        # Create overview page.
        overviewFile = os.path.join(targetDir, "overview.html")
        overviewFh = open(overviewFile, "wb")
        overviewFh.write("foo")
        overviewFh.close()
        menuItems.append({
            "label": "Overview",
            "href": "overview.html"
        })

        # Define the index file path.
        indexFile = os.path.join(targetDir, "index.html")

        # Add the section menus.
        menuItems.extend(sectionMenus)

        # Create index page.
        self.renderIndexPage(
            indexFile=indexFile, 
            menuItems=menuItems
        )


    def renderSection(self, section={}, targetDir="", dataDir="", baseUrl=""):
        """
        Generate metadata for a section.
        """
        print >> sys.stderr, "section is: ", section

        # Get section reader.
        sectionReader = section.get('reader')
        if not sectionReader:
            sectionReader = self.getSectionReader(section)

        # Get section data.
        sectionData = sectionReader.readSection(section=section)

        # Get section generator.
        sectionRenderer= section.get('renderer')
        if not sectionRenderer:
            sectionRenderer = self.getSectionRenderer(section)

        # Generate the section's metadata directory and return the 
        # section's menu.
        sectionDir = section.get('name')
        sectionMenu = sectionRenderer.renderSection(
            section=section,
            targetDir=os.path.join(targetDir, sectionDir),
            sectionData=sectionData,
            baseUrl="%s../" % baseUrl
        )
        return sectionMenu

    def getSectionRenderer(self, section):
        """
        Get a generator for a section.
        """

        # Default generator is CSV generator.
        return section_renderers.DefaultSectionRenderer()

    def getSectionReader(self, section):
        """
        Get a reader for a section.
        """

        # Default generator is CSV generator.
        return section_readers.CSVSectionReader()

    def renderIndexPage(self, indexFile="", menuItems=[]):
        """
        Generate a SASIPedia index page.
        """
        # Setup the index file.
        fh = open(indexFile, "wb")
        # Make navigation menu for subsections on the left.

        # Render the index file template.
        template = templates.env.get_template('sasipedia_main_index.html')
        content = template.render(
            baseUrl="",
            menuItems=menuItems
        )
        fh.write(content)
        fh.close()
