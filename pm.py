import csv

def write_to_file():
    outputFile = open('output.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(["Asset Tag","Asset Description","Model WO","Calendar Interval"])
    outputFile.close()

write_to_file()
