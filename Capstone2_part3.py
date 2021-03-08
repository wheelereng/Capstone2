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

def UserFriendlyPrintCoinSort(ResultTup):
    '''
    A function that prints the results of CoinSort() in a user-friendly way.

    '''
    
    # If the user enters a number below the denomination, the program will print a message stating that the chosen value cannot be broken down any further. 
    if ResultTup[0] < denominationValue[ResultTup[2]]:
       return("You can't break down " + str(ResultTup[0]) + "p any further\n")
    # If the chosen number is above 10p, the else statement will follow.
    else:
        StringToPrint = "You can break down " + str(ResultTup[0]) + "p into " + str(ResultTup[1]) + " x " + denominationText[ResultTup[2]] + "\n"

        # If there is a remainder, the if statement will concatenate the value to create a new string.
        if ResultTup[3] != 0:
            StringToPrint += "with a remainder of " + str(ResultTup[3]) + "p"
        
        # This will print the results in a user-friendly way.
        return StringToPrint

    

def UserFriendlyPrintMultipleCoin(MCSResultTup):
    '''
    A function that will display the user data and the calculated values from MultipleCoinSort function
    to the console in a user-friendly way.

    note:
    MCSResultTup is the return from the MultipleCoinSort function.

    '''
    
    # If the user enters a number below 10p, the program will print a message stating that the chosen value cannot be broken down any further. 
    # If the user excludes the 10p denomination and enters 10p as the value, the program will print a message stating that the chosen value cannot be broken down any further. 
    if MCSResultTup[2] < 10 or MCSResultTup[2]==MCSResultTup[1]:
        print("You can't break down " + str(MCSResultTup[2]) + "p any further\n")
    # If the chosen number is 10p and the 10p denominataion has not been excluded, the else statement will follow.
    else:
        StringToPrint = "You can convert " + str(MCSResultTup[2]) + "p into\n"

        # This will loop through the list of number of coins and concatenates them to the string
        for nCoinsIndex in range(4):
            # If the chosen value fits into a denomination, for example 10p into 15p, then the program will state that 15p fits into 1 x  10p
            if MCSResultTup[0][nCoinsIndex] != 0:
                StringToPrint += str(MCSResultTup[0][nCoinsIndex]) + " x " +  denominationText2[nCoinsIndex] + ", "
        #Removes the final comma and adds a space
        StringToPrint = StringToPrint[0:-2] + " \n"

        # If there is a remainder, the if statement will concatenate the value to create a new string stating the remainder.
        if MCSResultTup[1] != 0:
            StringToPrint += "with a remainder of " + str(MCSResultTup[1]) + "p"

        # This will print the results in a user-friendly way.
        return StringToPrint   

def UpdateConfiguration(minval, maxval, currencytype):
    ''' 
    This function will update the values in the configuration dictionary to be used throughout the program.

    '''

    Configurations["Minimum Value"] = minval
    Configurations["Maximum Value"] = maxval
    Configurations["Current Currency"] = currencytype

def PrintConfigurations():
    '''
    This function will return the current configurations of the program in a user friendly string.

    '''
    stringToPrint = "The current configurations are:\n"
    # This will list the current configurations as defined in Configurations at the top of the code.
    for key in Configurations:
        stringToPrint += key + ": " +str(Configurations[key]) + "\n"
    return stringToPrint

def PrintCoinList():
    '''
    This function will print the available denominations in a friendly manner.

    '''
    #This initiates the string to return.
    StringToPrint = "The available denominations are:\n"

    #Loop through the available denominations and concatenate them to the string with a new line after each.
    for denom in denominationText:
        StringToPrint += denom + "\n"

    return StringToPrint


