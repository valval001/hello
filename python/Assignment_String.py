#Ques1: Given a string of odd length greater than 7, return a new string made of the middle three characters of a given String

"""S1="RakeshzipPetabb"
mid=len(S1)//2
print(S1[mid-1:mid+2])

S2="JazzBonAyxx"
mid=len(S2)//2
print(S2[mid-1:mid+2])"""

#Ques2: Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1

"""S1="Ault"
S2="Kelly"
mid=len(S1)//2
print(S1[:mid]+S2+S1[mid:])"""

#Ques3: Given two string, S1 and S2 return a new string made of the first, middle and last characters each input string

"""S1="America"
S2="Japan"
mid1=len(S1)//2
mid2=len(S2)//2
S3=S1[0]+S2[0]+S1[mid1]+S2[mid2]+S1[-1]+S2[-1]
print(S3)"""

#Ques4: Given String S1 print all the upper letters first and then lower letters
"""S1="PyThOnPrOgRaMmInG"
S2=str()
S3=str()
for char in S1:
    if char.isupper():
        S2=S2+char
    else:
        S3=S3+char
print(S2+S3)"""

#Ques5: create a third-string made of the first char of s1 then the last char of s2, Next, the second char of s1 and second last
#       char of s2, and so on. Any leftover chars go at the end of the result.

"""S1="ABC"
S2="XYZ"
S3=S2[::-1]
S4=str()
for idx in range(len(S1)):
    S4=S4+S1[idx]+S3[idx]
print(S4)"""

#Ques6: Find all occurrences of “USA” from right to left in a given string ignoring the case. also display the starting position
"""S1 = "Welcome to USA. usa awesome, isn't it?"
print(S1.count("USA"))
print(S1.find("USA"))"""

#print(S1.find("USA")[-1:])

#Ques8:
#1st way
"""S1=input("Enter your name:Enter your ID")
S2=S1.split(":")                           #Splitted S1 in two parts
empid=int(S2[1])                           #Converted S2[1] to integer
vowels=str()                               #Checked for vowels in S2[0]
for char in S2[0]:
    if char in "AEIOUaeiou":
        vowels=vowels+char
alt=S2[0][::2]                             #A string for alternate characters in S2[0]
sum=0
for char1 in S2[0]:
    sum=sum+ord(char1)

prftscr=0
for i in range(1,empid):
    if i**2==empid:
        prftscr=prftscr+1
        break

if prftscr==1:
    print("empid is perfect square")
    print(vowels)
elif empid>2:
    i=2
    while i<empid:
        if empid%i==0:
            break
        i=i+1
    else:
        print("empid is prime")
        print(alt)
    

if empid%2!=0:
    print("empid is odd")
    print(sum)
else:
    print("None")"""


#2nd way
"""S1=input("Enter your name:Enter your ID")
S2=S1.split(":")                           #Splitted S1 in two parts
empid=int(S2[1])                           #Converted S2[1] to integer
vowels=str()                               #Checked for vowels in S2[0]
for char in S2[0]:
    if char in "AEIOUaeiou":
        vowels=vowels+char
alt=S2[0][::2]                             #A string for alternate characters in S2[0]
sum=0
for char1 in S2[0]:
    sum=sum+ord(char1)

prftscr=0
for i in range(1,empid):
    if i**2==empid:
        prftscr=1
        break
isprime=0
if empid>2:
    i=2
    while i<empid:
        if empid%i==0:
            break
        i=i+1
    else:
        isprime=1

if prftscr==1:
    print("empid is perfect square")
    print(vowels)
elif isprime==1:
    print("empid is prime")
    print(alt)
elif empid%2!=0:
    print("empid is odd")
    print(sum)
else:
    print("None")"""


#Ques9: 
"""S1="this is a good number 9089786756 and 8900000000 is a desired number"
S2=S1.split(" ")
S3=str()
for idx in range(len(S2)):
    if len(S2[idx])==10:
        S3=S3+S2[idx]+" "
print(S3)"""

#Ques7: Find all overlapping occurrences of given substring in given string
"""S1="ANANAAAANNN"
S2="AA"
count=0
for idx in range(len(S1)):
    if S1[idx:idx+len(S2)]==S2:
        count=count+1
print(count)"""

#Ques12:You are given a string S and width w. Your task is to wrap the string into a paragraph of width w

S1=input("Enter a string")
width=int(input("Enter a width"))
for idx in range(len(S1)):
    if idx%width==0:
        print(S1[idx:idx+width])



