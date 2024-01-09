#This program requests the user to input various floating point and integer numbers and does addition, subtraction and multiplication with the given inputs. The program also prints the results and the respective result data types.

def sesMath():
    sum_in1 = float(input("Please input a floating point number: "))
    sum_in2 = float(input("Please input another floating point number: "))
    sum = sum_in1 + sum_in2
    print("Sum: " + str(sum))
    print("Data Type: " + str(type(sum)))
    diff_in1 = int(input("Please input an integer: "))
    diff_in2 = int(input("Please input another integer: "))
    diff = diff_in1 - diff_in2
    print("Difference: " + str(diff))
    print("Data Type: " + str(type(diff)))
    prod_in1 = float(input("Please input a floating point number: "))
    prod_in2 = int(input("Please input an integer: "))
    prod = prod_in1 * prod_in2
    print("Product: " + str(prod))
    print("Data Type: " + str(type(prod)))

def main():
    sesMath()

if __name__ == "__main__":
    main()