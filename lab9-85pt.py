############################################
#                                          # 
#                   85pt                   #
#             Who has a fever?             #
############################################

# Create a for loop that will search through temperatureList
# and create a new list that includes only numbers greater than 100

temperatureList = [102,98,96,101,100,99,103,97,98,105]

# Insert for loop here

myList = []

for x in temperatureList:
    if x > 100:
        temperatureList = x
        myList.append(temperatureList)

# This should print [102,101,103,105]
print myList
