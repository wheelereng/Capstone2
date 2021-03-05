import requests as rq

Configurations = {
    "Minimum Value" : 0,
    "Maximum Value" : 10000,
    "Current Currency" : "GBP (£)"
}

denominationValue = [200, 100, 50, 20, 10]
denominationText = ["£2", "£1", "50p", "20p", "10p"]

def CoinSort(userTup, MCS=False):
    '''
    A function that, given the denomination, will give the number of coins of that denomination that will fit
    into the value, along with the remainder.
    '''
    #returns a tuple of the value, number of coins that can fit into that value (integer division),
    #the index of the denomination we're considering and the remainder (modulo)
    #If we're inside the MCS we use the updated list without the excluded denomination.
    if MCS: 
        return(userTup[0], (userTup[0] // denominationValue2[userTup[1]]), userTup[1], (userTup[0] % denominationValue2[userTup[1]]))
    else:
        return(userTup[0], (userTup[0] // denominationValue[userTup[1]]), userTup[1], (userTup[0] % denominationValue[userTup[1]]))


def MultipleCoinSort(userTup):
    '''
    A function that, given a denomination to exclude, will return how many coins it can be split into, 
    prioritising larger denominations.
    '''
    value = userTup[0]
    NodeToRemove = userTup[1]

    global denominationText2, denominationValue2
    
    #Copies the lists (Deep copy not shallow copy! don't just point to them!) and removes the denominations to exclude
    denominationValue2 = denominationValue.copy()
    denominationText2 = denominationText.copy()
    denominationText2.pop(NodeToRemove)
    denominationValue2.pop(NodeToRemove)

    #Initiates emty list for the results and initiates the first value
    resultlist = []
    rem = value

    #Loop through the updated denomination list indexes 
    for dIndex in range(len(denominationValue2)):
        #Call original coinsort alg, store the number of coins that fit into it and the remainder 
        MCSResultTup = CoinSort((rem, dIndex), True)
        #Update remainder for the next iteration
        rem = MCSResultTup[3]
        #Append number of coins to the result list
        resultlist.append(MCSResultTup[1])
    #Return number of coins list, the remainder and the value we were originally given.
    return (resultlist, rem, value)
    
    

def GetUserData(MCS=False):
    '''
    A function that gets the data required from the user for the coin sorter and the multiple coin sorter.

    '''

    #init. value variable and NodeToRemove varaible for loop logic.
    value = -1
    NodeToRemove = -1

    #Continue to ask for a value until we get it between 0 and 10,000 inclusive.
    while value < Configurations["Minimum Value"] or value > Configurations["Maximum Value"]:
        #Try and Except to make sure only integers are entered
        try:
            value = int(input("Please choose a number between " + str(Configurations["Minimum Value"]) + " and " + str(Configurations["Maximum Value"]) + ": "))
        except ValueError:
            print("Integers only!")
    else:
        print("You have chosen to exchange " + str(value) + "p\n")

        #Continue to ask for a value until we get it between 0 and 4 inclusive.

        #Depending if we're using multiple coin sort or not, change the end of the sentence.
        EndString = "exclude" if MCS else "consider"

        while NodeToRemove < 0 or NodeToRemove > 4:
            #Try and Except to make sure only integers are entered
            try:
                NodeToRemove = int(input("What denomination would you like to " + EndString + "? (0 = £2, 1 = £1, 2 = 50p, 3 = 20p, 4 = 10p) "))
            except ValueError:
                print("Integers only!")
        else:
            print("You have chosen to " + EndString + " " + str(denominationText[NodeToRemove]))

    #return the data in tuple format for consistency.
    return (value, NodeToRemove)
    

def UserFriendlyPrintCoinSort(ResultTup):
    '''
    A function that prints the results of CoinSort() in a human friendly manner.
    case of less than 10p considered first.
    '''
    
    if ResultTup[0] < 10:
       print("You can't break down " + str(ResultTup[0]) + "p any further\n")
    else:
        StringToPrint = "You can break down " + str(ResultTup[0]) + "p into " + str(ResultTup[1]) + " x " + denominationText[ResultTup[2]] 

        #If there's a remainder, concatenate it to the string.
        if ResultTup[3] != 0:
            StringToPrint += " with a remainder of " + str(ResultTup[3]) + "p."
        else:
            StringToPrint += "."
        
        print("\n" + StringToPrint + "\n")
    


def UserFriendlyPrintMultipleCoin(MCSResultTup):
    '''
    A function that will display the user data and the calculated values from MultipleCoin
    sort to the console in a human friendly manner.

    note:
    MCSResultTup is the return from MultipleCoin() function
    '''
    #if we have a value less than 10p then it can't be broken down AND
    #Special case for value=10p and removing 10p as it's the smallest denomination,
    #we won't be able to break it down any further.

    if MCSResultTup[2] < 10 or MCSResultTup[2]==MCSResultTup[1]:
        print("You can't break down " + str(MCSResultTup[2]) + "p any further\n")
    else:
        #Inititiates start of string with user given value
        StringToPrint = "You can convert " + str(MCSResultTup[2]) + "p into   "

        #Loops through list of number of coins and concatenates them to the string
        for nCoinsIndex in range(4):
            if MCSResultTup[0][nCoinsIndex] != 0:
                StringToPrint += str(MCSResultTup[0][nCoinsIndex]) + " x " +  denominationText2[nCoinsIndex] + "   "

        #If there's a remainder, concatentate it to the end of the string
        if MCSResultTup[1] != 0:
            StringToPrint += "with remainder " + str(MCSResultTup[1]) + "p."

        #print to the console
        print("\n" + StringToPrint + "\n")    


def PrintConfigurations():
    '''
    describe func
    '''
    for key in Configurations:
        print(key + ": " +str(Configurations[key]))


def GetCurrencyData():
    value = -10000
    #Continue to ask for a value until we get it between 0 and 10,000 inclusive.
    while value < Configurations["Minimum Value"] or value > Configurations["Maximum Value"]:
        #Try and Except to make sure only integers are entered
        try:
            value = int(input("Please choose a number between " + str(Configurations["Minimum Value"]) + " and " + str(Configurations["Maximum Value"]) + ": "))
        except ValueError:
            print("Integers only!")

    CValue = -1
    while CValue < 0 or CValue > 1:
        try:
            CValue = int(input("Please choose a currency (0 = MGA, 1 = USD): "))
        except ValueError:
            print("Integers only!")
    
    Currencyto = "MGA" if CValue==0 else "USD"

    return (value, Currencyto)

def PrintCurrencyNicely(value):

    symbol = "Ar" if value[1]=="MGA" else "$"
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
        
        
        




MainMenu()





