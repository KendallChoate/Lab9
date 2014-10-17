############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "Input a Celsius temperatue to convert to a Fahrenheit temperature."

userInput = int(raw_input())

print int(((userInput * 9)/5)+32)
    
