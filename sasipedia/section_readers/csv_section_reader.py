import os
import csv

class CSVSectionReader(object):
    """
    Reads section data from a csv file.
    Assumes that the data is in a file named '<section[dir]>/<section>.csv'
    in the dataDir.
    """
    def readSection(self, section):
        sectionFile = os.path.join(section['dir'], "%s.csv" % section['name'])
        reader = csv.DictReader(open(sectionFile, "rb"))
        records = [record for record in reader]
        return records


