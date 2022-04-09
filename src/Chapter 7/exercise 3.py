#
while True:
    file_name = input("Enter File: ")
    if file_name.lower() == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        try:
            file_handle = open(file_name)
            break
        except:
            print('File cannot be opened:',file_name)
#Initiating Count function
count = 0
for line in file_handle:
    count += 1
print(f"There are {count} subject lines in {file_name}")