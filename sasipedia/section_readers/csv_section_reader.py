import os
import csv

class CSVSectionReader(object):
    """
    Reads section data from a csv file.
    """
    def readSection(self, section):
        reader = csv.DictReader(open(section['metadataFile'], "rb"))
        rows = [row for row in reader]
        return {
            'fieldnames': reader.fieldnames,
            'rows': rows,
        }


