spisok=[]
numbers=[1,2,3,4,5]
abc=['Abc','B','C']
slovo="Programmerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)
while True:
    print("1-Add a letter")
    print("2-add a list")
    print("3-add a letter and where to put it")
    print("4-delete a element")
    print("5-delete a position")
    print("6-index")
    print("7-reverse")

    valik=int(input())
    if valik==1:
        a=input("add a letter")
        slovo_list.append(a)
        print(f"add {a} new letter into list",slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("add a letter, what ever letter you want")
        i=int(input("put a number for position"))
        slovo_list.insert(i-1,a)
        print(slovo_list)
    elif valik==4:
        a=input("delete a element")
        n=slovo_list.count(a.lower())
        if n>0:
            for i in range(n):
                slovo_list.remove(a)
        else:
            print("null")
        print(slovo_list)
    elif valik==5:
        i=int(input("delete a position"))
        n=len(slovo_list)
        if i<n:
            slovo_list.pop(i)
            print(slovo_list)
        else:
            print("null")
    elif valik==6:
        a=input("put letter, the position of which you want to know")
        i=slovo_list.index(a)
        print(f"element {a} put {i+1}")
    elif valik==7:
        slovo_list.reverse()
        print(slovo_list)