import csv
import os


class CSVSectionReader(object):
    """
    Reads section data from a csv file.
    Can optionally specify filters to only select specific rows.
    """
    def __init__(self, filters=[]):
        self.filters = filters

    def readSection(self, section):
        if not os.path.isfile(section['metadataFile']):
            fieldnames = []
            rows = []
        else:
            reader = csv.DictReader(open(section['metadataFile'], "rb"))
            fieldnames = reader.fieldnames
            rows = []
            for row in reader:
                passes = True
                for f in self.filters:
                    if not f(row):
                        passes = False
                        break
                if passes:
                    rows.append(row)

        return {
            'fieldnames': fieldnames,
            'rows': rows,
        }
