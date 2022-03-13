#Defining Functions
def open_file():
    while True:
        file_name = input("Enter filename: ")
        try:
            file_handle = open(file_name)
            return file_handle
        except:
            print("File not Found")
# Defined function to open file

# defining new function to process data in opened file
def process_file(file):
    while True: #Create loop to chech for validity of data
        try:
            year = input("Enter year: ")
            years = int(year) #years is an unused variable but will still invalidate the input if its a string
            if len(year) <= 4:
                break
            else:
                print('Please enter valid year')
        except:
            print ("Invalid Entry")
            continue 
    while True: #Second loop to display and select income level
        try:
            options = ["1","2","3","4"]
            print("Choose Income level")
            print ( "1- Lower income\n","2- Lower Middle income\n","3- Upper Middle income\n","4- High income")
            Inc =input("Enter income level: ")
            if Inc in options:
                break
            else:
                print("Choose valid option")
        except:
            print('Income level should be 1 to 4')
    # Declaring Variables to be used
    Percent = 0
    Percent_Total = 0
    count = 0
    lowest = None
    highest = None
# Sorting Valid option
    if Inc == "1":
        inc_val = "WB_LI"
    elif Inc == "2":
        inc_val = "WB_LMI"
    elif Inc == "3":
        inc_val = "WB_UMI"
    elif Inc == "4":
        inc_val = "WB_HI"
    else:
        print("Enter Valid Input")
    # Introducing for loop to lookup and compare data values
    for line in file:
        Percent = int(line[59:61])
        if year in (line[88:93]) and inc_val in line[51:58]:
            count += 1
            Percent_Total += Percent
            country = line[0:49]
            if lowest is None or Percent<lowest:
                lowest = Percent
                low_C = country
            if highest is None or Percent> highest:
                highest = Percent
                high_C = country
# Print Statements
    print("Number of records",count,'\n',"Average Percentage",round(Percent_Total/count,1),'\n',"Country with lowest Percentage: ",low_C.strip() ,"with: ",lowest)
    print("Country with highest Percent: ",high_C.strip(), "with: ", highest)
    
process_file(open_file())