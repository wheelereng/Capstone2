# Imports the 'requests' library and sets an alias for it as 'rq' to be used within this program.
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
            StringToPrint += " with a remainder of " + str(ResultTup[3]) + "p"
        
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
        StringToPrint = "You can convert " + str(MCSResultTup[2]) + "p into "

        # This will loop through the list of number of coins and concatenates them to the string.
        for nCoinsIndex in range(4):
            # If the chosen value fits into a denomination, for example 15p into 10p, then the program will state that 15p fits into 1 x  10p.
            if MCSResultTup[0][nCoinsIndex] != 0:
                StringToPrint += str(MCSResultTup[0][nCoinsIndex]) + " x " +  denominationText2[nCoinsIndex] + ", "
        # This will delete the last 2 characters. We do this to remove the comma at the end of the StringToPrint message.
        StringToPrint = StringToPrint[0:-2] + " "

        # If there is a remainder, the if statement will concatenate the value to create a new string stating the remainder.
        if MCSResultTup[1] != 0:
            StringToPrint += "with a remainder of " + str(MCSResultTup[1]) + "p"

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
    This function converts the chosen GBP amount to another currency. Here, the user can choose between MGA and USD.
    '''
    # This states the starting currency, here GBP.
    Currencyfrom = "GBP"
    # The url below links the program to a live currency converter api.
    url="https://free.currconv.com/api/v7/convert?q=" + Currencyfrom + "_" + Currencyto + "&compact=ultra&apiKey=4be37014813c4016a9ae"
    # This fetches the information from the url above using the 'get' function (found in the 'requests' library).
    response = rq.get(url)
    # Accesses the dictionary using the 'json' function (found in the 'requests' library).
    ConvertDict = response.json()

    # This returns the converted amount and rounds the amount to 2 decimal points.  
    return round((ConvertDict[Currencyfrom + "_" + Currencyto]*value), 2)

def SubMenu():
    '''
    This creates a sub-menu (as part of the text menu), and presents the user with 4 choices.
    The sub-menu opens when the user selects number 4 on the main menu.
    '''

    # This initiates the variable 'case'
    case = -1

    # This creates a loop which will continue to appear on screen, until the user presses number 4.
    while case != 4:
        # This presents the user with the sub-menu, and lists the options.
        try:
            print("\n\n*** Set Details - Sub Menu ***\n")
            print("1 - Set Currency")
            print("2 - Set Minimum Coin Input Value")
            print("3 - Set Maximum Coin Input Value")
            print("4 - Return To Main Menu")

            # This prompts the user to choose an option.
            case = int(input("\nEnter option here: "))

            # If the user selects number 1, they will be able to set the currency.
            if case==1:
                # This initiates the variable CValue.
                CValue = -1
                # This limits the user's choice to 0 and 1.
                while CValue < 0 or CValue > 1:
                    # Try and Except to make sure the user only enters integers.
                    try:
                        # This prompts the user to choose a currency to convert to.
                        CValue = int(input("Please choose a currency (0 = MGA, 1 = USD): "))
                    # Except catches the ValueError and prints "Integers only!".
                    except ValueError:
                        print("Integers only!")

                    # If the user picks 0, MGA will be selected. If the user picks 1, USD will be selected.
                    Currencyset = "MGA" if CValue==0 else "USD"  

                    # This sets the "Current Currency" of the Configurations dictionary to the chosen currency. Here MGA or USD.
                    Configurations["Current Currency"] = Currencyset
            # If the user selects number 2, they will be able to configure a new minimum amount.
            if case==2: 
                # This initiates the variable NewMin
                NewMin = -2
                # This ensures the minimum amount never goes below 0.
                while NewMin < 0:
                    # Try and Except to make sure the user only enters integers.
                    try:
                        # This prompts the user to select a new minimum amount.
                        NewMin = int(input("Please enter a new minimum: "))
                    # Except catches the ValueError and prints "Integers only!".
                    except ValueError:
                        print("Integers only!")
                # This sets the "Minimum Value" of the Configurations dictionary to the new chosen minimum amount. 
                Configurations["Minimum Value"]=NewMin

            # If the user selects number 3, they will be able to configure a new maximum amount.
            if case==3:
                # This initiates the variable NewMax
                NewMax = -1
                # This ensures that the new maximum amount never goes below 0 or below the configured minimum amount.
                while NewMax < 0 or NewMax < Configurations["Minimum Value"]:
                    # Try and Except to make sure the user only enters integers.
                    try:
                        # This prompts the user to select a new maximum amount.
                        NewMax = int(input("Please enter a new maximum that is above " + str(Configurations["Minimum Value"]) + ": "))
                    # Except catches the ValueError and prints "Integers only!".
                    except ValueError:
                        print("Integers only!")
                # This sets the "Maximum Value" of the Configurations dictionary to the new chosen maximum amount.
                Configurations["Maximum Value"]=NewMax            
        
        # Except catches the ValueError and prints "Integers only!".
        except ValueError:
            print("Integers only!")

def MainMenu():
    '''
    This function brings the main menu (as part of the text menu), and presents the user with 6 choices.
    '''
    # This initiates the variable case
    case = -1

    # This creates a loop which will continue to appear on screen, until the user presses number 6. 
    while case != 6:
        # This presents the user with the main menu, and lists the options.
        try:
            print("\n***Coin Sorter - Main Menu***\n")
            print("1 - Coin Calculator")
            print("2 - Multiple Coin Calculator")
            print("3 - Print Coin List")
            print("4 - Set Details")
            print("5 - Display Program Configurations")
            print("6 - Quit Program")

            # This prompts the user to choose an option.
            case = int(input("\nEnter option here: "))

            # If the user selects number 1, the coin sorter will be launched.
            if case==1:
                UserFriendlyPrintCoinSort(CoinSort(GetUserData(False)))
            # If the user selects number 2, the multiple coin sorter will be launched.
            elif case==2:
                UserFriendlyPrintMultipleCoin(MultipleCoinSort(GetUserData(True)))
            # If the user selects number 3, the program will list the available denominations.
            elif case==3:
                print("\nThe available denominations are: ")
                for denom in denominationText:
                    print(denom)
                print("\n")
            # If the user selects number 4, the Set Details sub-menu will be launched.
            elif case==4:
                SubMenu()
            # If the user selects number 5, the program will display the current configurations.
            elif case==5:
                print("\n")
                PrintConfigurations()
                print("\n")
        
        # Except catches the ValueError and prints "Integers only!".
        except ValueError:
            print("integers only!")

# This will call the MainMenu function and allow the user to interact with the program in the terminal.
MainMenu()