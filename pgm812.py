#   Joshua Neil Gable :: WsuID B877D833
#   Program :: pgm812.py
#   Description -
#       Heating and cooling degree-day totals
#       accept input of average daily temps
#       print out summation of degrees above cooling and below heating
#       input is taken from file "temps"
#
#   Psuedo Code
#   Algorythim main
#       open "temps" and loop through all values
#       summate numbers beyond thresholds
#       output the cooling and heating temps
#   pre - temps must exist & one temp per line
#   post - output cooling and heating degree-day totals
#
#   infile = open("temps.txt")
#   hsum,csum = 0.0
#   while not EOF
#       temp = line
#       if temp > cooling_threshold
#           csum += (temp - cooling_threshold)
#       if temp < heating_threshold
#           hsum += (heating_threshold - temp)
#   output csum and hsum
def main():
    filename = "temps.txt"
    infile = open(filename,'r')
    hsum = 0.0
    csum = 0.0
    for line in infile:
        temp = eval(line)
        if (temp > 80):
            csum = csum + (temp - 80)

        if (temp < 60):
            hsum = hsum + (60 - temp)

    print("The total heating needed was {0:0.2f} degrees".format(hsum))
    print("The total cooling needed was {0:0.2f} degrees".format(csum))
main()
