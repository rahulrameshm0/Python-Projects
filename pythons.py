bank_detail ={
    "person1" : {
    "name" : "A",
    "balance" : 1000},
    "person2" : {
    "name" : "B",
    "balance" : 2000},
    "person3" : {
    "name" : "C",
    "balance" : 2000}
}

def listall():
    for b in bank_detail.values():
        print(f"NAME: { b['name']}, DETAILS: {b['balance']}")

def create():
    name = input("Enter the name : ")
    balance = int(input("Enter the amound : "))
    a=len(bank_detail)+1

    new=f"person{a}"
    print(a)
    bank_detail[new] = {"name": name, "balance": balance}
def delect():
    a = input("Enter the name")
    found = False
    for x in bank_detail.values():
        if a == x["name"]:
            del x
            print(f"{a} is Deleted")
            found=True

    if found == False:
        print(f"Not found {a}")
def widraw():
    a = input("Enter the name : ")
    found = False
    for x in bank_detail.values():
        if a == x["name"]:
            found = True
            amount = int(input("Enter the amount : "))
            if x["balance"] < amount:
                print("Insufficent Balance")
                pass
            else:
                x["balance"] = x["balance"] - amount
                print(f"Remaing balance : {x["balance"]}")
        if found == False:
            print(f"Not found {a}")

    def deposit():
        a = input("Enter the name : ")
        found = False
        for x in bank_detail.values():
            if a == x["name"]:
                found = True
                amount = int(input("Enter the amount : "))
                x["balance"] = x["balance"] + amount
                print(f"Remaing balance : {x["balance"]}")
        if found == False:
            print(f"Not found {a}")

    def transfer():
        sender = input("Enter the name : ")
        found1 = False
        found2 = False
        for x in bank_detail.values():
            if sender == x["name"]:
                found1 = True
                recever = input("Enter the name : ")
                for y in bank_detail.values():
                    if recever == y["name"]:
                        found2 = True
                        amount = int(input("Enter the amount : "))
                        if amount > x["balance"]:
                            print("Insufficient funds.")
                        else:
                            x["balance"] = x["balance"] - amount
                            y["balance"] = y["balance"] + amount
                            print(f"Remaing balance : {x["balance"]}")
                            print(f"Remaing balance : {y["balance"]}")
            if found1 == False:
                print(f"Not found {sender}")
            if found1 == True and found2 == False:
                print(f"Not found {recever}")

            def check_balance():
                a = input("Enter the name")
                found = False
                for x in bank_detail.values():
                    if a == x["name"]:
                        print(f"The remaining Balance is {x['balance']}")
                        found = True

                if found == False:
                    print(f"Not found {a}")

            while (True):
                print("MALLU_BANK")
                print("1 . LIST\n2 . CREATE\n3 . DELETE\n4 . WIDRAW \n5 . DEPOSIT\n6 . TRANSFER\n7 . CHECK_BALANCE")
                slt = int(input("Enter the Choice : "))
                if slt == 1:
                    listall()
                elif slt == 2:
                    create()
                elif slt == 3:
                    delect()
                elif slt == 4:
                    widraw()
                elif slt == 5:
                    deposit()
                elif slt == 6:
                    transfer()
                elif slt == 7:
                    check_balance()
                else:
                    print("Enter Wrong Choice")
