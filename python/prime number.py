num=int(input("Enter a number: "))

i=2
if num<2:
    print("Number is not prime")
    exit()
while i<num:
    if num%i==0:
        print("Number is not prime")
        break
    i=i+1
else:
    print("Number is prime")

# Write a for loop to ask a number from user 5 times
# for i in range(5):
#     num= int(input("Enter a number:"))
