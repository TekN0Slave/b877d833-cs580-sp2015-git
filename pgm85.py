#   Joshua Gable : WsuID B877D833
#   program :: pgm85.py
#   Description -
#       Print all prime numbers between 1 and the user input
#
#   Psuedo Code
#   Algorythim main
#       create list of prime numbers from 2 thru user input and print
#       Useses coralary about composites(non primes) being made of primes
#   pre - must be positive integer input
#   post - output prime numbers
#
#   prompt user for integer
#   index = 2
#   plist = [2]
#   while index < input
#       if(isPrime(plist,index))
#           plist = plist + [index]
#       index++
#
#   Algorythim isPrime
# 
#    itterate thru prime list and return false if % compare = 0
#       return true if end of list is passed
#
#   i = 0
#   while i < len(plist)
#       if index % plist[i] == 0
#          return 0
#       i++
#   return 1
def isPrime(plist , index):
    i = 0    while i < len(plist)
        if (index % plist[i] == 0):
            return 0

        i = i + 1

    return 1

def main():
    plist = [2]
    index = 2
    print("This program will print the list of prime numbers")
    print("The list will span from 2 - user input")
    num = eval(input("Enter a positive integer please : "))

    while (index < num):
        if (isPrime(plist,index)):
            plist = plist + [index]

        index = index + 1

    print(plist)
main()