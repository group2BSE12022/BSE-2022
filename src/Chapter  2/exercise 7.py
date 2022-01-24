y =float (input ("Cash"))
print ("You have:")
if y >= 20:
    print (int(y//20) ,"twenties" )
else:
    print ( 0 ,"twenties")
y = y % 20
if y >= 10:
    print (int(y//10),"tens")
else:
    print (0 , "tens")
y = y % 10
if y>= 5:
    print (int(y//5) ,  "Fives")
else:
    print ( 0 , "Fives")
y= y % 5
if y >= 1:
    print( int(y//1) , "ones")
else:
    print( 0 , "ones")
y= y % 1
if y >= 0.25:
    print(int(y//0.25) , "quarters")
else:
    print( 0 , "quarters")
y= y % 0.25
if y >= 0.1:
    print( int(y//0.1) , "dimes")
else:
    print( 0 , "dimes")
y= y % 0.1
if y >= 0.05:
    print( int(y//0.05) , "nickels")
else:
    print( 0 , "nickels")
y= y % 0.05
if y>=0.01:
    print( int(y//0.01) ,"pennies")
else:
    print( 0 , "pennies")