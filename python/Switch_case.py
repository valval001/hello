print("Menu / 1:Misal / 2:Kheer / 3:Karahi / 4:Qorma / 5:Kabab")
choice= int(input("Enter your choice: "))
match(choice):
    case 1:
        print("You have selected Misal")
    case 2:
        print("You have selected Kheer")
    case 3:
        print("You have selected Karahi")
    case 4:
        print("You have selected Qorma")
    case 5:
        print("You have selected Kabab")
    case _:
        print("Invalid choice")
