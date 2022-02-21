count = 0
total = 0
while True:
    numb = input ("Enter Number: ")
    if numb.lower() == "done":
        break
    try:
        ng = float (numb)
        count = count + 1
        total = total + ng
        average = total / count
    except:
        print ("Ivalid input, try numeric characters")
