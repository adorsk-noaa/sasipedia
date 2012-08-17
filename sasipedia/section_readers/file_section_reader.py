class FileSectionReader(object):
    """
    Reads section content from a file.
    """
    def readSection(self, section):
        content = open(section['metadataFile'], "rb").read()
        return {
            'content': content
        }
