#This program will declare a class that will describe my favorite animal.
#The data members of this class represent:
#The length of the arms (float)
#The length of the legs (float)
#The number of eyes (int)
#Does it have a tail? (bool)
#Is it furry? (bool)
#There is an initialization function that sets the values of the data members when an instance of the class is created.
#A member of the class will be printed out and described based off the physical characteristics.

class favAnimal: #class holding default information about a common rat
    def __init__(self, armLen = 1.0, legLen = 1.2, eyeNum = 2, haveTail = True, isFurry = True):
        self.armLen = armLen
        self.legLen = legLen
        self.eyeNum = eyeNum
        self.haveTail = haveTail
        self.isFurry = isFurry

    def arm(self): #access function to retrieve arm length
        return self.armLen
    
    def leg(self): #access function to retrieve leg length
        return self.legLen
    
    def eyes(self): #access function to retrieve number of eyes
        return self.eyeNum
    
    def tail(self): #access function to retrieve whether or not the animal has a tail
        return self.haveTail
    
    def fur(self): #access function to retrieve whether or not the animal has fur
        return self.isFurry
    
    def printInfo(self): #print function to print out animal/object information
        print("Arm Length: " + str(self.armLen) + "\nLeg Length: " + str(self.legLen) + "\nNumber of Eyes: " + str(self.eyeNum) + "\nHas Tail?: " + str(self.haveTail) + "\nIs Furry?: " + str(self.isFurry))
    

def main(): #main function that defines a favAnimal object and calls printInfo()
    rat = favAnimal()
    rat.printInfo()

if __name__ == "__main__":
    main()
    