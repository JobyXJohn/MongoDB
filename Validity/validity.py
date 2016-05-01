"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in the range as described above,
  write that line to the output_good file
- if the value of the field is not a valid year as described above, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def isnot_int(value):
  try:
    int(value)
    return False
  except:
    return True

def process_file(input_file, output_good, output_bad):
    out_bad=[]
    out_good=[]
    good_year = []
    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            if isnot_int(row['productionStartYear'][:4]):
                out_bad.append(row)
            else:
                if int(1886) <= int(row['productionStartYear'][:4]) and  int(row['productionStartYear'][:4]) <= int(2014):
                    good_year.append( int(row['productionStartYear'][:4]))
                    out_good.append(row)
                else:
                    out_bad.append(row)
    for i in set(good_year):
        print i

        #COMPLETE THIS FUNCTION



    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(output_good, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in out_good:
            writer.writerow(row)
    with open(output_bad, "w") as b:
        writer = csv.DictWriter(b, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in out_bad:
            writer.writerow(row)


def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()