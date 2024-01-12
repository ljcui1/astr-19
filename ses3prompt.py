#This program defines a function f(x) that will return x**3 + 8.
#The main function will call f(x) with x = 9 and print the result. If the result is greater than 27, then the program will print "YAY!".

def f(x): #function that returns x ** 3 + 8
    return (x ** 3 + 8)

def main(): #main function that calls f(x) and prints "YAY!" if the result is greater than 27.
    x = 9
    y = f(x)
    print(str(y))
    if y > 27:
        print("YAY!")

if __name__ == "__main__":
    main()