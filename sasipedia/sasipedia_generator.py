import os
import shutil
import sys

import templates
from default_section_generator import DefaultSectionGenerator
from csv_section_reader import CSVSectionReader

class SASIPediaGenerator(object):
    """
    A Class for generating SASIPedia metadata.
    """
    def generateSASIPedia(self, targetDir=None, dataDir=None, sections=None,
                          baseUrl=""):
        """
        Generate a set of static 'SASIpedia' pages at the given target
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
            sectionMenu = self.generateSection(section, targetDir, dataDir,
                                               baseUrl="")
            sectionMenus.append(sectionMenu)

        # Define the index file path.
        indexFile = os.path.join(targetDir, "index.html")

        # Combine the section menus into a master menu.
        menu = [{
            'href': 'index.html',
            'label': 'Overview',
            'children': sectionMenus
        }]

        # Create index page.
        self.generateIndexPage(
            indexFile=indexFile, 
            menu=menu
        )

    def generateSection(self, section={}, targetDir="", dataDir="", baseUrl=""):
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
        sectionGenerator = section.get('generator')
        if not sectionGenerator:
            sectionGenerator = self.getSectionGenerator(section)

        # Generate the section's metadata directory and return the 
        # section's menu.
        sectionDir = section.get('name')
        sectionMenu = sectionGenerator.generateSection(
            section=section,
            targetDir=os.path.join(targetDir, sectionDir),
            sectionData=sectionData,
            baseUrl="%s../" % baseUrl
        )
        return sectionMenu

    def getSectionGenerator(self, section):
        """
        Get a generator for a section.
        """

        # Default generator is CSV generator.
        return DefaultSectionGenerator()

    def getSectionReader(self, section):
        """
        Get a reader for a section.
        """

        # Default generator is CSV generator.
        return CSVSectionReader()

    def generateIndexPage(self, indexFile="", menu={}):
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
            menu=menu
        )
        fh.write(content)
        fh.close()
