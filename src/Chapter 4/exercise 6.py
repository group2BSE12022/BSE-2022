# Get values of hours and rate
H = input ("Enter Hours ")
R = input ("Enter Rate")
# Convert values to floats
hours = float (H)
rate = float (R)
def computepay(hours,rate):
    if hours > 40:
        over = hours-40
        print ((40*rate) + (over*1.5 * rate))
    else:
        print (hours * rate)

computepay(hours,rate)