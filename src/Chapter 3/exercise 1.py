# Get values of hours and rate
H = input ("Enter Hours ")
R = input ("Enter Rate")
# Convert values to floats
hours = float (H)
rate = float (R)
if hours > 40:
    over = hours-40
    print (40 * rate + (1.5 * rate*over))
else:
    print (hours * rate)