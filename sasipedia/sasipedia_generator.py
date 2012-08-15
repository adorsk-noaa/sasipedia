import os
import sys
from default_section_generator import DefaultSectionGenerator
from csv_section_reader import CSVSectionReader

class SASIPediaGenerator(object):
    """
    A Class for generating SASIPedia metadata.
    """
    def generateSASIPedia(self, targetDir=None, dataDir=None, sections=None):
        """
        Generate a set of static 'SASIpedia' pages at the given target
        directory.
        """
        # Setup the directory.
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)

        # Create sections.
        sectionPaths = []
        for section in sections:
            sectionPath = self.generateSection(section, targetDir, dataDir)
            sectionPaths.append(sectionPath)

        # Create index page.
        self.generateIndexPage(sectionPaths=sectionPaths)

    def generateSection(self, section, targetDir, dataDir):
        """
        Generate metadata for a section.
        """
        print >> sys.stderr, "section is: ", section

        # Get section reader.
        sectionReader = section.get('reader')
        if not sectionReader:
            sectionReader = self.getSectionReader(section)

        # Get section data.
        sectionData = sectionReader.readSection(
            section=section,
            dataDir=dataDir
        )

        # Get section generator.
        sectionGenerator = section.get('generator')
        if not sectionGenerator:
            sectionGenerator = self.getSectionGenerator(section)

        # Generate the section's metadata directory and return the 
        # relative link.
        sectionDir = section.get('name')
        sectionGenerator.generateSection(
            section=section,
            targetDir=os.path.join(targetDir, sectionDir),
            sectionData=sectionData
        )

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

    def generateIndexPage(self, sectionPaths=[]):
        """
        Generate a SASIPedia index page.
        """
        pass
        # Make navigation menu for subsections on the left.

        # Make overview page.
