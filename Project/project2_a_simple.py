with open('project/measles.txt','r') as copy_file, open ("New file",'a') as copy:
    year = input("Enter year or 'All':")
    if year.lower() == 'all' or '':
        for lines in copy_file:
            copy.write(lines)
        print("Copy Successful")
    for lines in copy_file:
        if year [0] == lines[88]:
            copy.write(lines)