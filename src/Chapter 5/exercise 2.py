Max = 0
Min = None
while True:
    Numb = input ("Enter Number: ")
    if Numb.lower() == "done":
        break
    try:
        nb = float (Numb)
        if nb > Max:
            Max = nb
        elif nb is None or nb < Min:
            Min = nb
    except:
        print ("Invalid input")
print ("Max",Max, "Min:",Min)