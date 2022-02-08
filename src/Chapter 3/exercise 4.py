# Ask user for age
A = input ("Enter Age:")
# Set alternative for wrong data input
try:
    age = int (A)
    if age >= 18:
        print (" You can vote.")
    elif 17 >= age >= 0 :
        print ("Too young to vote.")
    elif age < 0 :
        print ("You are a Time Traveller")
except:
    print ("Not a numeric Character")

