file_name = input ("Enter file name: ")
with open (file_name,'r') as print_file:
    for line in print_file:
        print(line.upper())