def main():
    n = int(input("Please enter no. of rows: "))
    for i in range(1,n+1):
        for z in range(1,i+1):
            print(i*z, end="\t")
        print()

main()