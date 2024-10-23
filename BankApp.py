customers = {
    "18244710058": {"name": "Erhan", "surname": "Aktas", "password": "1996", "amount": 99999},
    "98765432101": {"name": "Ahmet", "surname": "Yilmaz", "password": "1234", "amount": 50000},
    "11223344556": {"name": "Ayse", "surname": "Demir", "password": "5678", "amount": 75000},
    "55667788900": {"name": "Mehmet", "surname": "Kara", "password": "4321", "amount": 120000},
    "99887766554": {"name": "Fatma", "surname": "Celik", "password": "8765", "amount": 30000}
}

cid = input("Enter your id: ")
password = input("Enter your password: ")
if cid in customers and customers[cid]["password"] == password:
    print("Login successful!")
    print(
            "What do you want to do?\n"
            "Press 1 to withdraw money.\n"
            "Press 2 to deposit money.\n"
            "Press 3 to check your balance.\n"
            "Press 4 to view all information.\n"
            "Press 5 to exit.\n"
            "Press 6 to get menü informations again.\n"
        )
    key=True
    while(key):
        
            
        choice=input("Enter a operator:")
        if(choice == "1"):
            print(f"you have {customers[cid]['amount']} money")
            tAmount=int(input("enter amoun of money to withdraw: "))
            if(tAmount <= customers[cid]['amount']):
                customers[cid]["amount"] -= tAmount
                print(f"your new money amount is {customers[cid]['amount']}")
            else:
                print(f"you dont have {tAmount} TL money ")

        elif(choice == "2"):
            dAmount=int(input("enter amoun of money to deposit: "))
            customers[cid]["amount"] += dAmount
            print(f"your new money amount is {customers[cid]['amount']}")
        
        elif(choice == "3"):
            print(f"your new money amount is {customers[cid]['amount']}")

        elif(choice == "4"):
            print(customers[cid])

        elif(choice == "5"):
            print("thank you to chooose us , have a good day")
            exit()

        elif(choice == "6"):
            print( "What do you want to do?\n"
            "Press 1 to withdraw money.\n"
            "Press 2 to deposit money.\n"
            "Press 3 to check your balance.\n"
            "Press 4 to view all information.\n"
            "Press 5 to exit.\n"
            "Press 6 to get menü informations again.\n")
        else:
            print("you entered wrong expreccion!!!")
else:
    print("Login Failed!")