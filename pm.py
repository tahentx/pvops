import csv
def create_model_wo(description,status,currency):
    description = input("Description of the WO: ")
    status = input("What is the default status: ")
    currency = input("What is the default currency: ")
    return description,status,currency


# create_model_wo("test","In Planning","USD - U.S. Dollar")

def create_pmgs(tag,starting_month):
    tag = input("Asset tag:")
    starting_month = input("Starting Month")
    day_input = input("Please specific: will the work order be due on a specific day, or a weekday. Input 'day' or 'weekday'")
    if day_input == "Day":
        day_of_month = 'Day of the Month'
        calendar_day = input("What day?")
    else:
        weekday_of_the_month = 'Weekday of the Month'
    print("all good")

# create_pmgs('9999',2)
#
def create_group_detail():
    """
    The PM Group Schedule needs to be created before one can add associated group details

    """

def write_to_file():
    outputFile = open('output.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    outputWriter.writerow(["Asset Tag","Asset Description","Model WO","Calendar Interval"])
    outputFile.close()

write_to_file()
