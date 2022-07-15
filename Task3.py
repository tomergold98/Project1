def triangle(y,x):
    for i in range(x):
        z = x-i
        print(y*z)

def main():
    ch = input("Please enter a letter: ")
    n = int(input("Please enter no. of rows: "))
    triangle(ch,n)

main()

