List = []
with open ('romeo.txt','r') as mainfile:
    for line in mainfile:
        spliter= line.split
        List.append(spliter)
    List.sort()
    print (List)