#P2_JAB.py
num_range = int(input("What is the range? 1 to : "))
num = num_range//2
theMin = 1
theMax = num_range
print("Is the number", num, "?")
selection = str(input("If the number is lower type '<', if it is higher type '>', or 'y' if I got it: "))
while selection is ">" or "<":
    if selection is "<":
        if theMax == num-1:
            print("That can't be right") #Prints if there is no solution
            break
        theMax = num
        num = (theMin + theMax)//2
        print("Is the number", num, "?")
        selection = str(input("If the number is lower type '<', if it is higher type '>', or 'y' if I got it: "))
    if selection is ">":
        if theMin == num-1:
            print("That can't be right") #Prints if there is no solution
            break
        theMin = num
        num = (theMin + theMax)//2 
        print("Is the number", num, "?")
        selection = str(input("If the number is lower type '<', if it is higher type '>', or 'y' if I got it: "))
    if selection is "y":
        print("Your number was", num)
        break
