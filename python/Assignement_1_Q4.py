marks= int(input("Enter your marks: "))
if marks>0 and marks<25:
    print("You have failed")
elif marks>=25 and marks<45:
    print("You have E grade")
elif marks>=45 and marks<50:
    print("You have D grade")
elif marks>=50 and marks<60:
    print("You have C grade")
elif marks>=60 and marks<80:
    print("You have B grade")
elif marks>=80 and marks<=100:
    print("You have A grade")
else:
    print("Invalid marks")