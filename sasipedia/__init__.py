import os

def generateSASIpedia(targetDir=None, dataDir=None, sections=None):
    """
    Generate a set of static 'SASIpedia' pages at the given target
    directory.
    """

    # Setup the directory.
    if not os.path.exists(targetDir):
        os.makedirs(targetDir)

    # Create sections.
    sectionPaths = []
    for sectionName in sections:
        sectionPath = generateSection(sectionName)
        sectionPaths.push(sectionPath)

    # Create index page.
    generateIndexPage(sectionPaths=sectionPaths)


def generateSection(sectionName):
    pass
    

def generateIndexPage(sectionPaths=[]):
    pass
    # Make navigation menu for subsections on the left.

    # Make overview page.


