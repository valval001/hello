#Ques3: print the square root of the list

"""L1=[1,4,9,16,25,36,79]
L2=[]
for e in L1:
    t=e**0.5
    L2.append(t)
print(L2)"""

#Ques1: Reverse the list

"""L1=[100,200,300,400,500]
print(L1[ : :-1])"""


#Ques4: Merge two lists as given L1[5,6,7] and L2[0,1] and output shoud be L3[50,51,60,61,70,71]

"""L1=[5,6,7]
L2=[0,1]
L3=[]

for e in L1:
    for f in L2:
        L3.append(str(e)+str(f))
print(L3)"""

#Ques5: merge two lists as given L1[10,20,30,40] and L2[100,200,300,400] and output should be same L1 bur L2 should be in reverse order


"""trial"""
"""L1=[10,20,30,40]
L2=[100,200,300,400]
L3=[]
for e in L1:
    L3.append(e)
for e in L2[ : :-1]:
    L3.append(e)    
print(L3)"""




"""solved"""
"""L1=[10,20,30,40]
L2=[100,200,300,400]
L3=L2[ : :-1]
for idx in range(len(L1)):
    print(L1[idx],L3[idx])"""

#Ques6: Remove empty strings from the list of strings

"""L1=["Ashish","","Atharva","Amit","","Revati",""]
L2=[]
for e in L1:
    if e!="":
        L2.append(e)
print(L2)"""

#Ques10 : Remove 20 from the list

"""L1=[5,20,15,20,25,50,20]
L2=[]
for e in L1:
    if e!=20:
        L2.append(e)
print(L2)"""

#Ques7: Add item 7000 after 6000 in the following Python List

"""L1=[10,20,[300,400,[5000,6000],500],30,40]
L1[2][2].insert(2,7000)
print(L1)"""

#Ques8: 
#Different Approach
"""L1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
L2=["h", "i", "j"]
L3=L1[2][1][2]+L2
L1[2][1][2]=L3
print(L1)"""

#Short Approach
"""L1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
L2=["h", "i", "j"]
L1[2][1][2].extend(L2)
print(L1)"""

#Ques9:

"""L1=[5,10,15,20,25,50,20]
occ_idx=L1.index(20)
L1[occ_idx]=200
print(L1)"""

#Ques10:
"""L1= [5, 20, 15, 20, 25, 50, 20]
L2=[]
for e in L1:
    if e!=20:
        L2.append(e)
print(L2)"""

#Ques11:Take a number as input from user.Print maximum and minimum integer which can be generated using all the digits in the
#       input number

"""num=input("Enter a number:")
digits=list(num)
min=digits[0]
MIN=[]
for e in digits:
    if e>min:
        MIN.append(e)
        min=e
print(MIN)"""
#wrong
"""num=input("Enter a number:")
digits=list(num)
digits.sort()
min=digits[0]
min_list=[digits[0]]
#print(min_list)
for e in digits:
    if e>min:
        min_list.append(e)
print(min_list)"""
#Correct
"""num=input("enter a number")
digits=list(num)
digits.sort()
#print(digits)
#print(digits[::-1])
print("".join(digits))
print("".join(digits[::-1]))"""


#Ques12:

"""num=input("enter a number")
digits=list(num)
L2=[]
for idx in range(len(digits)):
    if digits[idx]%2==1:
        L2.append(digits[idx])
print(L2)"""

"""num=input("enter a number")
digits=list(num)
L1=digits[::1]
L2=[]
for e in L1:
    if e%2==1:
        L2.append(e)
print(L2)"""

#Ques13:Take integer from user and print all odd numbers which can be generated using any number of digits from given number

num=input("Enter a number:")
digits=list(num)
L2=[]

        


