with open('email.txt','r') as copy:
    count = 0
    for line in copy:
        if line.startswit('From'):
            m = line.split()
            n = m[1]
            count += 1
            print (n)
    print("There were",count,'lines with from')