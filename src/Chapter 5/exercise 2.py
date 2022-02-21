Numbs = []
while True:
    Ng = input("Enter Numbers or done: ")
    if len(Ng) == 0:
        print("Invalid data")
    elif Ng.lower() == "done":
        break

    try:
        Nga = float(Ng)
        Numbs.append(Nga)
    except:
        print("Invalid data Type")

Max= None
Min = None
for i in Numbs:
    if(Max is None or i > Max):
        Max = i
    if(Min is None or i < Min):
        Min = i
print("Maximum:", Max,"Minimum:", Min)

