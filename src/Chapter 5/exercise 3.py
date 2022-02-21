# Group 2 members
#1. Mwesigye Jordan Alvin 2021/BSE/088/PS
#2. Allio Jedidiah         2021/BSE/015/PS
#3. NAMUGGA SHARIFAH       2021/BSE/162/PS
#4. Namayanja Florence     2021/BSE/093/PS
#5. Ampe Sheenah           2021/BSE/019/PS
#6. Ahimbisibwe Orishaba K 2021/BSE/007/PS
#7. Alinda Samuel          2021/BSE/192/PS
#Below is a program of a change maker in a vending machine. we break down step by step of the operation.
#>step one (Basics):
# Assigning global variables 
amtdue = None
nickel =25
dimes = 25
quarter = 25
Ones = 0
fives = 0
change_keep = 0
price2 = None
#>initialize welcome message
print("\n Welcome to the vending machine change maker program \n Change maker initialized ")
#>step two (Defining functions):
#create function to convert money to dollars and cents
def dols_n_cents(cash):
    dollars = int(cash /100)
    cents = int(cash % 100)
    if dollars == 0:
        print("Payment due is:",cents,"cents\n")
    else:
        print("Payment due is:",dollars,"dollars and",cents,"cents\n")
#>Step 3
#> Introduce loops to manipulate data input
# first loop to display stock contents and prompt for price
while True:
    print ("Current Stock contains:\n"+str(nickel)+"nickels\n"+str(dimes)+" dimes\n"+str(quarter)+"quarters\n"+str(Ones)+"ones\n"+str(fives)+"fives")
    #Now we need the price of the product to be purchased
    price_in = input("Enter the price in form of XX.XX or q to quit..: ")
    if price_in.lower() == "q":
        print("Program Exited....")
        break
    elif price_in != "q":
        try:
            #introducing a try to check if input is a correct data type
            price2 = float(price_in)
            #We multiply the float by 100 to make it easier to deal with and avoid errors
            amtdue = price2*100
            #Here we display the menu for the different types of deposits
            print ("'n' - deposit a nickel\n"+"'d' - deposit a dime\n"+"'q - deposit a quarter\n"+"'o' deposit a one dollar bill\n"+"'f' - deposit a five dollar bill\n"+"'c' - cancel the purchase")
            #introuducing the second loop for user deposits
            while True:
                if amtdue > 0 and (amtdue % 5 == 0):
                    dols_n_cents(amtdue)
                    choice = input("Deposit:")
                    #Now we filter the selection using if statements
                    if choice.lower() == "d":
                        amtdue -= 10
                        dimes += 1
                        change_keep += 10
                    elif choice.lower() == "n":
                        amtdue -= 5
                        nickel += 1
                        change_keep += 5
                    elif choice.lower() == "q":
                        amtdue -= 25
                        quarter += 1
                        change_keep += 25
                    elif choice.lower() == "o":
                        amtdue -= 100
                        Ones += 1
                        change_keep += 100
                    elif choice.lower() == "f":
                        amtdue -= 500
                        fives += 1
                        change_keep += 500
                    elif choice.lower() == "c":
                        amtdue_2 = change_keep
                        break
                    else:
                        print(choice,"Invalid selection,try again:")
                # Adding an elif incase of correct data type but invalid input
                elif price2 < 0:
                    print("Invalid Input")
                elif amtdue < 0:
                    amtdue_2 = amtdue * -1
                    break
                else:
                    print("Invalid value, must be a non-negative multiple of 5")
                    amtdue_2 = 0
                    break
            #>Step three (calculating the change)
            if amtdue_2 != 0:
                print("Your change is :")
                # calculating for one dollar bills
                ones_2 = amtdue_2 // 100
                amtdue_2 = amtdue_2 % 100
                if ones_2 > Ones:
                    amtdue_2 = amtdue_2 + (ones_2 - Ones)*100
                    ones_2 = Ones
                    Ones = 0
                else:
                    Ones = Ones - ones_2
                if ones_2 != 0:
                    print(int(ones_2),"Ones\n")
                #calculating for quarters
                quarters_2 = amtdue_2 // 25
                amtdue_2 = amtdue_2 % 25
                if quarters_2 > quarter:
                    amtdue_2 = amtdue_2 + (quarters_2 - quarter)*25
                    quarters_2 == quarter
                    quarter = 0
                else:
                    quarter = int(quarter - quarters_2)
                if quarters_2 != 0:
                    print(int(quarters_2),"Quarters\n")
                # calculating for dimes
                dimes_2 = amtdue_2 // 10
                amtdue_2 = amtdue_2 % 10
                if dimes_2 > dimes:
                    amtdue_2 = amtdue_2 + (dimes_2 - dimes)*10
                    quarters_2 == quarter
                    dimes = 0
                else:
                    dimes = int(dimes - dimes_2)
                if dimes_2 != 0:
                    print(int(dimes_2),"Dimes\n")
                # calculating for nickels
                nickels_2 = amtdue_2 // 5
                amtdue_2 = amtdue_2 % 5
                if nickels_2 > nickel:
                    amtdue_2 = amtdue_2 + (nickels_2 - nickel)*5
                    nickels_2 == nickel
                    nickel = 0
                else:
                    nickel = int(nickel - nickels_2)
                if nickels_2 != 0:
                    print(int(nickels_2),"Nickels\n")
                if amtdue_2 != 0:
                    print("Machine out of change.\n"+"See the store manager for remaining change.\n")
                    dols_n_cents(amtdue_2)
        except:
            print ("Bad Data")
            break
    else:
        print("Invalid data")