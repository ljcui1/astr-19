#This program does addition, subtraction and multiplication with various floating points and ints. The program also prints the results and the respective result data types.

def sesMath(): #function does math with floating points and ints
    sum_in1 = 4.5
    sum_in2 = 6.7
    sum = sum_in1 + sum_in2
    print("Sum: " + str(sum))
    print("Data Type: " + str(type(sum)))
    diff_in1 = 35
    diff_in2 = 23
    diff = diff_in1 - diff_in2
    print("Difference: " + str(diff))
    print("Data Type: " + str(type(diff)))
    prod_in1 = 8.3
    prod_in2 = 6
    prod = prod_in1 * prod_in2
    print("Product: " + str(prod))
    print("Data Type: " + str(type(prod)))

def main(): #main function that calls sesMath()
    sesMath()

if __name__ == "__main__":
    main()