with open('project/measles.txt','r') as copy_file:
    while True: #Prompting user for correct lengh of required input
        year = input("Enter year or 'All':")
        if len (year) > 4:
            print('Input out of Range')
        elif len (year) <= 4:
            break
# Initialising The output file name and adding .txt extention
    file = input ("Output file: ")
    file_ext = file +'.txt'
    copy = open (file_ext, 'a')
    # Checking for data criteria
    if year.lower() == "all" or '':
        for line in copy_file:
            copy.write(line)
    if len (year) > 4:
            print('Input out of Range')
    try:
        for line in copy_file:
            if len(year) == 1:
                if year == line[88]:
                    copy.write(line)
            elif len (year) == 2:
                if ((year [0] == line[88]) and (year[1] == line [89])):
                    copy.write(line)
            elif len (year) == 3:
                if ((year [0] == line[88]) and (year[1] == line [89])and (year[2]==line[90])):
                    copy.write(line)
            elif len (year) == 4:
                if ((year [0] == line[88]) and (year[1] == line [89])and (year[2]==line[90])and (year[3] == line [91])):
                    copy.write(line)
            else:
                pass
        print('succesful')

    except:
        print ('Invalid Input')