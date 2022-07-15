def increasing(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]:
            return False
    return True

def decreasing(x):
    for z in range(len(x)-1):
        if x[z] < x[z+1]:
            return False
    return True

def listDescription(a,b,c,d):
    for i in a,b,c,d:
        if increasing(i):
            print(i,"increasing")
        elif decreasing(i):
            print(i,"decreasing")
        else:
            print(i)

def program1():
    list1 = [1,2,4,5]
    list2 = [6,4,3]
    list3 = [-3,-2,-1]
    list4 = [1,3,2]
    listDescription(list1,list2,list3,list4)

program1()
