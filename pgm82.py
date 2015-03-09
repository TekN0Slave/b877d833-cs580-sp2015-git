#   Joshua Neil Gable :: WsuID B877D833
#   Program :: pgm82.py
#   Description -
#       Wind Chill Index Calculator
#       2 options
#       A. convert input from user
#       B. Print generic table
#
#   Psuedo Code -
#   Algorthim Main
#       ask for inputs then call appropreate function
#   Pre - Input for V and T correct units
#   Post - Print out table or single temp
#
#   Get option from user (Table:Single)
#   if table 
#       call print_chart()
#   if single then get inputs from user
#       output = call wind_chill()
#       Print output
#
#   Algorthim wind_chill
#       calculates wind chill
#       35.74 + (0.6215)T - (35.75)(V^0.16) + (0.4275)T(V^0.16)
#       T = Temp in fahrenheit || V = wind velocity in mph
#   pre - none
#   post - return wind chill or print error
#   
#   if speed < 0
#       output error
#       return error
#   if speed >= 3
#       calculate with formula
#       set return to calculation
#   else
#       set return to input temp
#   return wind chill temp
#
#   Algorthim print_char
#       print values row by row for the wind chill using wind_chill
#   pre - none
#   post - print wind chill chart
#
#   row , col = 0, -20
#   print top chart values
#   while row < 51
#       print row val
#       while col < 61
#           print wind_chill(row,col)
#           col += 10
#       row += 5
#       col = -20

def wind_chill(temp,speed):
    if (speed < 0.0):
        print("Error with input to wind_chill, negative wind speed")
        return 9000.1

    if (speed >= 3.0):
        x = (35.74) + (temp * 0.6215) - (35.75 * (speed ** 0.16)) + (0.4275 * temp * (speed ** 0.16))

    else:
        x = temp

    return x

def print_chart():
    row , col = 0 , -20
    print("    | -20.00 | -10.00 | 00.00 | 10.00 | 20.00 | 30.00 | 40.00 | 50.00 | 60.00")

    while row < 51:
        print(" {:0>2d} " .format(row) ,end = "")
        while col < 61 :
            output = wind_chill(col,row)
            print("| {:05.2f} " .format( output ), end = "")
            col = col + 10

        row = row + 5
        col = -20
        print(" ")

def main():
    print("This program has two functions\n  1) Print wind chill chart\n  2) Calculate specific wind chill")
    choice = 0
    temp = 0.0
    speed = 0.0
    output = 0.0
    while ( (choice < 1) or (choice > 2) ):
        choice = eval ( input ("Please make your choice 1 or 2 : "))

    if (choice == 1):
        print("Now printing the wind chill chart\nThe far left col is the wind speed for that row\nThe top row is the temp for that col")
        print_chart()

    if (choice == 2):
        temp = eval ( input ( "Please enter the tempreture : "))
        speed = eval ( input ( "Please enter the wind speed : "))
        output = wind_chill( temp, speed )
        if output != 9000.1
            print("The wind chill is {0:0.2f} degrees".format(output))

main()