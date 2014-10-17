############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

Africa = raw_input()
sick = raw_input()
temperature = raw_input()
keepGoing = True

while keepGoing == True:
    print "What is your temperature?"
    temperature = raw_input()
    print temperature
    print "Have you been sick in the last 24 hours?"
    sick = raw_input()
    print sick
    print "Have you recently traveled to West Africa?"
    Africa = raw_input()
    print Africa    
    print "Are there more people in the line?"
    keepGoing = True
    print keepGoing
    #if temperature > "105":
         #print "Go to the hospital immediately."