# notes:
# check the comment wording of the return in the multiplecoinsort function at the end

# come back to 'if MCSResultTup[0][nCoinsIndex] != 0:' to double-check the meaning.

# come back to 'symbol = "Ar" if value[1]=="MGA" else "$"' and double check the index referencing for currency

# Imports the 'requests' library and saves it as 'rq' to be used within this program.
# The 'requests' library allows the user to send HTTP requests.
# Here we will be requesting information from a live currency converter.
# If the 'requests' library is not installed on your machine, type 'pip install requests' in your terminal to install the library.
# If pip is not installed on your machine, install pip by typing 'get-pip.py' into the terminal, and then install the 'requests' library.
import requests as rq

# This creates a dictionary called 'Configurations'.
# This holds all of the program configuration details.
Configurations = {
    "Minimum Value" : 0,
    "Maximum Value" : 10000,
    "Current Currency" : "GBP (£)"
}

# This is a list with the denomination values.
denominationValue = [200, 100, 50, 20, 10]
# This is a list with the coins available within the scope of this program.
denominationText = ["£2", "£1", "50p", "20p", "10p"]


def CoinSort(userTup, MCS=False):
    '''
    A function that, given the denomination, will give the number of coins of that denomination that will fit
    into the value, along with the remainder.
    '''
    # This returns a tuple of the value, number of coins that can fit into that value (integer division),
    # the index of the denomination we're considering, and the remainder (modulo).
    # If we're inside the MultipleCoinSort(MCS) we use the updated list without the excluded denomination.
    if MCS: 
        return(userTup[0], (userTup[0] // denominationValue2[userTup[1]]), userTup[1], (userTup[0] % denominationValue2[userTup[1]]))
    else:
        return(userTup[0], (userTup[0] // denominationValue[userTup[1]]), userTup[1], (userTup[0] % denominationValue[userTup[1]]))


def MultipleCoinSort(userTup):
    '''
    A function that, given a denomination to exclude, will return how many coins it can be split into, 
    prioritising larger denominations.
    '''
    # The value variable stores the 1st item (index 0) of the userTup. Here, the number of coins.
    value = userTup[0]
    # The NodeToRemove variable stores the 2nd item (index 1) of the userTup. Here, the denomination to exclude.
    NodeToRemove = userTup[1]

    # 'global' allows us to use these variables outside of the scope of the MultipleCoinSort function
    global denominationText2, denominationValue2
    
    # This creates deep copies of the lists denominationValue and denominationText. We create deep copies so that the original lists are not affected.
    denominationValue2 = denominationValue.copy()
    denominationText2 = denominationText.copy()
    # The pop function removes NodeToRemove from the denominationText2 and denominationValue2.
    denominationText2.pop(NodeToRemove)
    denominationValue2.pop(NodeToRemove)

    # This initiates empty list for the results.
    resultlist = []
    # This stores the value as the variable 'rem'.
    rem = value

    # This loops through the updated denomination list indexes.
    for dIndex in range(len(denominationValue2)):
        # This calls the original coinsort function and stores the number of coins that fit into the existing denominations.
        MCSResultTup = CoinSort((rem, dIndex), True)
        # This updates the remainder (rem) for the next iteration of the loop.
        rem = MCSResultTup[3]
        # This appends the number of coins to the result list. When an item is appended, it is added to the end of a list.
        resultlist.append(MCSResultTup[1])
    # This returns the number of coins in the list, the remainder, and the value we were originally given.
    return (resultlist, rem, value)
    

def GetUserData(MCS=False):
    '''
    This function gets the data required from the user for the coin sorter (CoinSort) and the multiple coin sorter (MultipleCoinSort).
    '''

    # This initiates the value variable and NodeToRemove variable.
    value = -1
    NodeToRemove = -1

    # This loop will continue to ask for a value until the user enters an integer value between the Minimum Value and Maximum Value, here between 0 and 10,000 (both inclusive).
    while value < Configurations["Minimum Value"] or value > Configurations["Maximum Value"]:
        #Try and Except to make sure the user only enters integers.
        try:
            value = int(input("Please choose a number between " + str(Configurations["Minimum Value"]) + " and " + str(Configurations["Maximum Value"]) + ": "))
        # Except catches the ValueError and prints "Integers only!".
        except ValueError:
            print("Integers only!")
    # Once the user has entered a correct value, they will see a message stating the number they have chosen to exchange.
    else:
        print("You have chosen to exchange " + str(value) + "p\n")

        # This will set the variable "EndString" as "exclue" if the user is using the MultipleCoinSort function (MCS), and as "consider" if the user is using the CoinSort function.
        EndString = "exclude" if MCS else "consider"
        
        # This will continue to ask for a value until the user enters an integer value between 0 and 4 (both inclusive).
        while NodeToRemove < 0 or NodeToRemove > 4:
            #Try and Except to make sure the user only enters integers.
            try:
                NodeToRemove = int(input("What denomination would you like to " + EndString + "? (0 = £2, 1 = £1, 2 = 50p, 3 = 20p, 4 = 10p) "))
            # Except catches the ValueError and prints "Integers only!".
            except ValueError:
                print("Integers only!")
        # Once the user has entered a correct value, they will see a message stating the denomination they have chosen.
        else:
            print("You have chosen to " + EndString + " " + str(denominationText[NodeToRemove]))

    # This will return the data in a tuple format for consistency.
    return (value, NodeToRemove)
   

def UserFriendlyPrintCoinSort(ResultTup):
    '''
    A function that prints the results of CoinSort() in a user-friendly way.

    note:
    ResultTup is the return from the CoinSort function
    '''
    
    # If the user enters a number below 10p, the program will print a message stating that the chosen value cannot be broken down any further. 
    if ResultTup[0] < 10:
       print("You can't break down " + str(ResultTup[0]) + "p any further\n")
    # If the chosen number is above 10p, the else statement will follow.
    else:
        StringToPrint = "You can break down " + str(ResultTup[0]) + "p into " + str(ResultTup[1]) + " x " + denominationText[ResultTup[2]] 

        # If there is a remainder, the if statement will concatenate the value to create a new string.
        if ResultTup[3] != 0:
            StringToPrint += " with a remainder of " + str(ResultTup[3]) + "p."
        # If there is no remainder, the program will print a full stop at the end of the StringToPrint variable.
        else:
            StringToPrint += "."
        
        # This will print the results in a user-friendly way.
        print("\n" + StringToPrint + "\n")
    

def UserFriendlyPrintMultipleCoin(MCSResultTup):
    '''
    A function that will display the user data and the calculated values from MultipleCoinSort function
    to the console in a user-friendly way.

    note:
    MCSResultTup is the return from the MultipleCoinSort function
    '''
    
    # If the user enters a number below 10p, the program will print a message stating that the chosen value cannot be broken down any further. 
    # If the user excludes the 10p denomination and enters 10p as the value, the program will print a message stating that the chosen value cannot be broken down any further. 
    if MCSResultTup[2] < 10 or MCSResultTup[2]==MCSResultTup[1]:
        print("You can't break down " + str(MCSResultTup[2]) + "p any further\n")
    # If the chosen number is 10p and the 10p denominataion has not been excluded, the else statement will follow.
    else:
        StringToPrint = "You can convert " + str(MCSResultTup[2]) + "p into   "

        # This will loop through the list of number of coins and concatenates them to the string
        for nCoinsIndex in range(4):
            # If the chosen value fits into a denomination, for example 15p into 10p, then the program will state that 15p fits into 1 x  10p
            if MCSResultTup[0][nCoinsIndex] != 0:
                StringToPrint += str(MCSResultTup[0][nCoinsIndex]) + " x " +  denominationText2[nCoinsIndex] + "   "

        # If there is a remainder, the if statement will concatenate the value to create a new string stating the remainder.
        if MCSResultTup[1] != 0:
            StringToPrint += "with remainder " + str(MCSResultTup[1]) + "p."

        # This will print the results in a user-friendly way.
        print("\n" + StringToPrint + "\n")    


def PrintConfigurations():
    '''
    This function will print the current configurations of the program.
    '''
    # This will list the current configurations as defined in Configurations at the top of the code.
    for key in Configurations:
        print(key + ": " +str(Configurations[key]))


def GetCurrencyData():

    '''
    This function will allow the user to choose the currency they would like to convert to.
    '''

    # This initiates the value variable.
    value = -10000

    # This loop will continue to ask for a value until the user enters an integer value between the Minimum Value and Maximum Value, here between 0 and 10,000 (both inclusive).
    while value < Configurations["Minimum Value"] or value > Configurations["Maximum Value"]:
        #Try and Except to make sure the user only enters integers.
        try:
            value = int(input("Please choose a number between " + str(Configurations["Minimum Value"]) + " and " + str(Configurations["Maximum Value"]) + ": "))
        # Except catches the ValueError and prints "Integers only!".
        except ValueError:
            print("Integers only!")

    # This initiates the Cvalue variable.
    CValue = -1
    # This will continue to ask the user for a value between 0 and 1
    while CValue < 0 or CValue > 1:
        #Try and Except to make sure the user only enters integers.
        try:
            CValue = int(input("Please choose a currency (0 = MGA, 1 = USD): "))
        # Except catches the ValueError and prints "Integers only!".
        except ValueError:
            print("Integers only!")
    
    # The Currencyto variable is set to "MGA" if the chosen number is 0, otherwise it is set to "USD".
    Currencyto = "MGA" if CValue==0 else "USD"

    # This will return the value and the Currencyto variable
    return (value, Currencyto)

def PrintCurrencyNicely(value):
    '''
    This function will print the message in a user-friendly way.
    '''

    # This sets the currency symbol depending on the chosen value.
    symbol = "Ar" if value[1]=="MGA" else "$"
    # This will print the initial £ value and then state its value in the currency that the user has chosen to convert to.
    print("£" + str(value[0]) + " = " + symbol + str(ConvertCurrency(value[1], value[0])))


def ConvertCurrency(Currencyto, value):
    '''
    describe func
    '''
    Currencyfrom = "GBP"
    url="https://free.currconv.com/api/v7/convert?q=" + Currencyfrom + "_" + Currencyto + "&compact=ultra&apiKey=4be37014813c4016a9ae"
    response = rq.get(url)
    ConvertDict = response.json()

    return round((ConvertDict[Currencyfrom + "_" + Currencyto]*value), 2)

def SubMenu():
    case = -1
    while case != 4:
        try:
            print("*** Set Details - Sub Menu ***")
            print("1 - Set Currency")
            print("2 - Set Minimum Coin Input Value")
            print("3 - Set Maximum Coin Input Value")
            print("4 - Return To Main Menu")

            case = int(input("Enter option here: "))

            if case==1:
                CValue = -1
                while CValue < 0 or CValue > 1:
                    try:
                        CValue = int(input("Please choose a currency (0 = MGA, 1 = USD): "))
                    except ValueError:
                        print("Integers only!")
    
                    Currencyset = "MGA" if CValue==0 else "USD"  

                    Configurations["Current Currency"] = Currencyset
            if case==2: 
                NewMin = -2
                while NewMin < 0:
                    try:
                        NewMin = int(input("Please enter a new minimum: "))
                    except ValueError:
                        print("Integers only!")
                Configurations["Minimum Value"]=NewMin

            if case==3:
                NewMax = -1
                while NewMax < 0 or NewMax < Configurations["Minimum Value"]:
                    try:
                        NewMax = int(input("Please enter a new maximum: "))
                    except ValueError:
                        print("Integers only!")
                Configurations["Maximum Value"]=NewMax            

        except ValueError:
            print("Integers only!")

def MainMenu():
    case = -1

    while case != 6:
        try:
            print("***Coin Sorter - Main Menu***\n")
            print("1 - Coin Calculator")
            print("2 - Multiple Coin Calculator")
            print("3 - Print Coin List")
            print("4 - Set Details")
            print("5 - Display Program Configurations")
            print("6 - Quit Program")

            case = int(input("Enter option here: "))

            if case==1:
                UserFriendlyPrintCoinSort(CoinSort(GetUserData(False)))
            elif case==2:
                UserFriendlyPrintMultipleCoin(MultipleCoinSort(GetUserData(True)))
            elif case==3:
                print("\nThe available denominations are: ")
                for denom in denominationText:
                    print(denom)
                print("\n")
            elif case==4:
                SubMenu()
            elif case==5:
                print("\n")
                PrintConfigurations()
                print("\n")
    
        except ValueError:
            print("integers only!")
        
        
        




#MainMenu()






