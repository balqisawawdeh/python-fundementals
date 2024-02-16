#Countdown
def a():
    for i in range (5,0,-1):
        print(i)
print (a())

#Print and Return
def b():
    list =[2,1]
    print(list[0])
    return list[1]
print (b())

#FirstpPlusLength
def s():
    list=[5,10,20]
    sum = list[0]+list[-1]
    return sum
print (s())

#Values Greater than Second
def f():
    list=[5,2,3,2,1,4]
    low=0
    high=len(list)
    s=list[1]
    for i in range(low,high):
        if list[i]>s:
            list2=[]
            list2.append(list[i])
            list2=list2
            print(len(list2))
            print(list2)
        else:
            if len(list)<2:
                False 
print(f())

#This Length, That Value
def L(size,value):
    list=[]
    list=[size,value]
    print(list)
    for i in range (0,len(list)):
        new_list=[value]*size
    print (new_list)
print(L(4,7))
print(L(6,2))
print(L(10,1))
