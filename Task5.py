def main():
    A = int(input("Please enter value of A: "))
    B = int(input("Please enter value of B: "))
    list = []
    if(A,B > 0 and int):
        for i in range(A,0,-1):
            if A % i == 0 and B % i == 0:
                list.append(i)
                list.sort()
    result = str(list).strip('[]')
    if len(list) == 0:
        result = "none"
    print("The following divide both",A,"and",B,"are",result)

main()