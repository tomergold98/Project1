def checklist(a):
    for i in range(len(a)):
        for x in range(i+1,len(a)):
            if a[i] == a[x]:
                return False
    return True

def Program2():
    list1 = [1,2,3,4,5]
    list2 = [1,2,3,4,2]
    for i in list1,list2:
        if checklist(i):
            print(i,"no duplicates")
        else:
            print(i,"with duplicates")

Program2()