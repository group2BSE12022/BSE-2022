userlist = []
while True:
    numbers = input("Enter Numbers: ")
    try:
         num = int(numbers)
         userlist.append(num)
    except:
        if numbers.lower()=='done':
            break
        else:
            print ('Invalid Input')

print("Maximum is:",max(userlist),'\nMinimum is:',min(userlist))

