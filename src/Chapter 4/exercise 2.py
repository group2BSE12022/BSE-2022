c = float(input("initial amount of money: "))
r = float(input("yearly rate of interest: "))
t = float(input("number of years until maturation: "))
n = float(input("number of times the interest is compounded: "))

def invest (p):
    p = (c*(int(1)+(r/n))**(t*n))
    print ("Investment = ",( "{:.2f}".format(p)))

invest('p')
pass
