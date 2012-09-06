import os


class FileSectionReader(object):
    """
    Reads section content from a file.
    """
    def readSection(self, section):
        if os.path.isfile(section['metadataFile']):
            content = open(section['metadataFile'], "rb").read()
        else:
            content = ""

        return {
            'content': content
        }
