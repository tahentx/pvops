import csv
import pandas as pd
swt = {
  "Std Task ID": "3016.17.001",
  "Description": "Safety Audits",
  "WO Task Type": "Preventive",
  "Instructions": "Perform visual inspection of the following site grounds/buildings: perimeter fencing, walkways, lighting, fire extinguishers",
  "Est Hrs": "4"
}
swt2 = {
  "Std Task ID": "3016.17.001",
  "Description": "Eye Wash Stations",
  "WO Task Type": "Preventive",
  "Instructions": "Perform visual inspection of eye wash stations. Replace eye wash station fluid per manufacturers recommendations",
  "Est Hrs": "1"
}
swt3 = {
  "Std Task ID": "3016.17.001",
  "Description": "Environmental Protections",
  "WO Task Type": "Preventive",
  "Instructions": "Perform visual inspection of oil containment structures. Perform visual inspection of site vegetation and site drainage. Reporting of abnormal events which a component operator may assume may require reporting.",
  "Est Hrs": "4"
}

all_tasks = [swt,swt2,swt3]

def write_taskstocsv(tasks):
    for task in tasks:
        df = pd.DataFrame.from_dict(task, orient="index")
        df.to_csv('misae.csv')

print(swt2)
# write_taskstocsv(all_tasks)
#

# def write_to_file():
#     outputFile = open('output.csv', 'w', newline='')
#     outputWriter = csv.writer(outputFile)
#     outputWriter.writerow(["Asset Tag","Asset Description","Model WO","Calendar Interval"])
#     outputFile.close()
#
# write_to_file()
