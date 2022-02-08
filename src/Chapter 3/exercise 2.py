H = input ("Enter Hours")
R = input ("Enter Rate")
try:
    hours = float (H)
    rate = float (R)
    print ( hours * rate)
except:
    print ("Error, please enter numeric input")