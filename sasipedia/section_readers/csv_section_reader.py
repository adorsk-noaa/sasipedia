import csv


class CSVSectionReader(object):
    """
    Reads section data from a csv file.
    Can optionally specify filters to only select specific rows.
    """
    def __init__(self, filters=[]):
        self.filters = filters

    def readSection(self, section):
        reader = csv.DictReader(open(section['metadataFile'], "rb"))
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
            'fieldnames': reader.fieldnames,
            'rows': rows,
        }
