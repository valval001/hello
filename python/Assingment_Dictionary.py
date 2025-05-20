# Ques2.
# a. Find out how many students are in the list
# b. Change Lisa’s favourite colour
# c. Remove 'Jenny' and her favourite colour


"""people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}

print("a.  ", len(people.keys()), "  students are there")

people["Lisa"]= "Green"

print("b.  ", people["Lisa"], "  is Lisa's new fav colour")

del people["Jenny"]

print("c.  ", people)

sort= sorted(people)
# print(sorted(people.items))
print(sort)"""

# Ques3.


"""d=dict()

def new_user():
    global d
    a=input("Enter a name: ")
    d[a]= input("Enter vehicle number: ")
    print("New user added: ", d[a])
    menu()

def del_user():
    global d
    a=input("Enter a name to find: ")
    if a in d:
        print("Name found: ",a, " ", d[a])
        print("press   y: delete / n: to cancel")
        choice= input("Enter your choice: ")
        match(choice):
            case 'y':
                del d[a]
                print("User deleted")
            case 'n':
                print("Canceled")
        menu()
    else:
        print("Name not found")
        menu()

def mod_vehicle():
    global d
    a=input("Enter a name to find: ")
    if a in d:
        print("Name found: ", d[a])
        d[a]=input("Enter new vehicle: ")
        print("Updated ", d[a])
        menu()
    else:
        print("Name not found")
        menu()

def srch_vehicle():
    global d
    a=input("Enter a name to find: ")
    if a in d:
        print("Name found: ", d[a])
        menu()
    else:
        print("Name not found")
        menu()

def name():
    print(list(d.keys()))
    menu()

def vehicle():
    print(list(d.values()))
    menu()

def menu():
    print("Menu / 1:Add New User / 2:Delete User / 3:Modify Vehicle / 4:Search Vehicle / 5:All Name / 6:All Vehicles / 7:Exit")
    choice= int(input("Enter your choice: "))
    match(choice):
        case 1:
            print("You have selected to add new user")
            new_user()
        case 2:
            print("You have selected to delete a user")
            del_user()
        case 3:
            print("You have selected to update a vehicle")
            mod_vehicle()
        case 4:
            print("You have selected search a vehicle")
            srch_vehicle()
        case 5:
            print("You have selected to show all names")
            name()
        case 6:
            print("You have selected to show all vehicle")
            vehicle()
        case 7:
            print("Bye Bye")
        case _:
            print("Invalid")


menu()"""

# Ques1.  



"""d= {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# end= ("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")
# end= ("Caesar cipher? I much prefer Caesar salad!")
a=str()
for char in end:
    # a=str()
    if char.isalpha():
        a=a+d[char]
    else:
        a=a+char
print(a)"""


# Ques5.
# Wrong

# a= input("Enter a line or para")
# b=a.split(" ")
# # d=dict()
# for i in range(1,10):
#     d=dict()
#     for e in b:
#         count=0
#         if len(e)==i:
#             count=count+1
#             d[i]=count       
#     print(d)

# Wrong

# Ques5.
# a= input("Enter a line or para")
# b=a.split(" ")
# # count=0
# d=dict()
# for i in b:
#     # count=0
#     # d=dict()
#     len(i) in d
#     d[len(i)]=1

#     d[len(i)]=d[len(i)]+1
# print(d)

# Ques5.

# Correct

"""a=input("Enter a line or para")
b=a.split(" ")
word_count=dict()
suffix=dict()
suffix_words=["s","es","ed","y","en"]

def word_no(b):
    for i in b:
        if len(i) in word_count:
            word_count[len(i)]=word_count[len(i)]+1

        else:
            word_count[len(i)]=1
    print("length of word : no. of words with this length")
    print(word_count)

def suffix_count(b):
    for i in b:
        for e in suffix_words:
            if i.endswith(e):
                if e in suffix:
                    suffix[e] +=1
                else:
                    suffix[e]=1
    print(suffix)


word_no(b)
suffix_count(b)"""







