denomination1 = [200, 100, 50, 20, 10]
denom = ["£2", "£1", "50p", "20p", "10p"]

def coinsort(amount, d):
    '''
    describe function
    '''
    #returns a tuple of the number of coins (integer division), and the remainder (modulo)
    return((amount // denomination1[d]), (amount % denomination1[d]))

'''#Get the data from the user
while True:
    try:
        Value = int(input("enter amount: "))

        count = 0
        for coin in denom:
            print(str(count) + " - " + coin)
            count += 1

        deno = int(input("enter denom: "))
        break

    except:
        print("try again")

coinsort(amount, deno)
'''

def MultipleCoinSort(value, NodeToRemove):
    '''
    describe function
    '''

    #Copies the list and removes the denomination to exclude
    denomination2 = denomination1
    denomination2.pop(NodeToRemove)

    #Initiates emty list for the results and initiates the first value
    resultlist = []
    rem = value

    #Loop through the updated denomination list 
    for d in denomination2:
       #Call original coinsort, store the number of coins that fit into it and the remainder 
       ResultTup = coinsort(rem, denomination2.index(d))
       #Update remainder for the next iteration
       rem = ResultTup[1]
       #Append number of coins to the result list
       resultlist.append(ResultTup[0])
    
    return (resultlist, rem)

def UserFriendlyPrint():
    pass

def GetUserData():
    pass

def PrintConfigurationList():
    pass

def ConvertCurrency():
    pass

'''#Get the data from the user
while True:
    try:
        Value = int(input("enter amount: "))

        count = 0
        for coin in denom:
            print(str(count) + " - " + coin)
            count += 1

        deno = int(input("enter denom: "))
        break

    except:
        print("try again")

coinsort(amount, deno)
'''
