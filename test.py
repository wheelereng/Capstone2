denominationValue = [200, 100, 50, 20, 10]
denominationText = ["£2", "£1", "50p", "20p", "10p"]

def CoinSort(userTup):
    '''
    A function that, given the denomination, will give the number of coins of that denomination that will fit
    into the value, and the remainder
    '''
    #returns a tuple of the number of coins (integer division), and the remainder (modulo)
    return(userTup[0], (userTup[0] // denominationValue[userTup[1]]), userTup[1], (userTup[0] % denominationValue[userTup[1]]))


def MultipleCoinSort(userTup):
    '''
    A function that, given a denomination to exclude, will return how many coins it can be split into, 
    prioritising larger denominations.
    '''
    value = userTup[0]
    NodeToRemove = userTup[1]
    global denominationText2
    
    #Copies the lists (don't just refer to them!) and removes the denominations to exclude
    denominationValue2 = denominationValue.copy()
    denominationText2 = denominationText.copy()
    denominationText2.pop(NodeToRemove)
    denominationValue2.pop(NodeToRemove)

    #Initiates emty list for the results and initiates the first value
    resultlist = []
    rem = value

    #Loop through the updated denomination list 
    for dIndex in denominationValue2:
        #Call original coinsort, store the number of coins that fit into it and the remainder 
        MCSResultTup = CoinSort((rem, denominationValue2.index(dIndex)))
        #Update remainder for the next iteration
        rem = MCSResultTup[3]
        #Append number of coins to the result list
        resultlist.append(MCSResultTup[1])
    
    #Return number of coins list, the remainder and the value we were given.
    return (resultlist, rem, value)
    
    

def GetUserData(MCS=False):
    '''
    A function that gets the data required from the user for the multiplecoin sorter

    Note: I have added extra precautions to only allow the user to input an integer!! changes 
    made are the try and except.

    Note: I have also added an if statement to see if the data is going to be used for normal coin
    sort or the mutliple one. This is because we need the same data for both, it's just in different 
    contexts. (Message me if I'm unclear.)
    '''

    #init. value variable and NodeToRemove varaible for loop logic.
    value = -1
    NodeToRemove = -1

    #Continue to ask for a value until we get it between 0 and 10,000 inclusive and until it's an integer.
    while value < 0 or value > 10000:
        #Try and Except to make sure only integers are entered
        try:
            value = int(input("Please choose a number between 0 and 10,000: "))
        except:
            print("Integers only!")
    else:
        print("You have chosen to exchange " + str(value) + "p\n")

        #Continue to ask for a value until we get it between 0 and 4 inclusive and until it's an integer.

        #Depending if we're using multiple coin sort or not, change the end of the sentence.
        EndString = "exclude" if MCS else "consider"

        while NodeToRemove < 0 or NodeToRemove > 4:
            #Try and Except to make sure only integers are entered
            try:
                NodeToRemove = int(input("What denomination would you like to " + EndString + "? (0 = £2, 1 = £1, 2 = 50p, 3 = 20p, 4 = 10p) "))
            except:
                print("Integers only!")
        else:
            print("You have chosen to " + EndString + " " + str(denominationText[NodeToRemove]))
    #return the data in tuple format 
    return (value, NodeToRemove)
    

def UserFriendlyPrintCoinSort(ResultTup):
    '''
    A function that prints the results of CoinSort() in a human friendly manner.
    case of 0p considered first.
    '''
    if ResultTup[0]==0:
         print("You can't break down 0p any further\n")

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
    if MCSResultTup[2]==0: 
        print("You can't break down 0p any further\n")
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


def PrintConfigurationList():
    pass

def ConvertCurrency():
    pass


UserFriendlyPrintMultipleCoin(MultipleCoinSort(GetUserData(True)))

UserFriendlyPrintCoinSort(CoinSort(GetUserData(False)))

