nb = input ("Enter Number Of Guests:")
try:
    nk = int (nb)
    if nk > 200 :
        print ("Cost is $20,000")
    elif 200>= nk > 100:
        print ("Cost is $15,000")
    elif 100 >= nk > 50:
        print ("Cost is $10,000")
    elif 50 >= nk > 0 :
        print ("Cost is $4,000")
except:
    print ("Invalid Entry")