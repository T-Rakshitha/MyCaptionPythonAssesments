n=int(input("enter noum of elements in list:"))
list=[]
for i in range(n):
    x=int(input("enter  the element:"))
    list.append(x)
for i in list:
    if(i>=0):
        print(i)

