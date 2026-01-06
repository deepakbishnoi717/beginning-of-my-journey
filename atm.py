import json
import os
import os         
FILE = "account.json"

def load_Account():
    if not os.path.exists(FILE):
        raise FileNotFoundError("account.json not found. Please create it first.")
    
    with open("account.json", "r") as file :
        return json.load(file)
        
def save_account(account):
    with open("account.json","w") as f:
        json.dump(account,f,indent=4)

#############  ATM METHODS ##############
def secority():
    account = load_Account()
    p = int(input("Enter the pin :"))
    if int(account["pin"]) == p :
        return True
    
    print("Wrong Pin!")
    return False

def deposit():
    account = load_Account()
    amount = int(input("Enter amount for deposit :"))
    account["balance"] += amount
    save_account(account)
    print(f"{amount} is deposited in your account {account['account']}" )

def withdraw():
    account = load_Account()
    amount = int(input("Enter the amount for withraw :"))
    if amount > account["balance"] :
        print("insufficent balance !")
        return
    
    account["balance"] -= amount 
    save_account(account)
    print(f"{amount} is dabited from your account {account['account']}")

def check_balence():
    account = load_Account()
    print(f"Avilable Balance :{account['balance']}")

#################### MAIN CLASS ##################

def main():
    if not secority():
        return
    
    while True :
        print("ATM Buttons!")
        print("press 1 for deposite.")
        print("press 2 for withdraw.")
        print("press 3 for check balance.")
        print("press 4 for exit.")
        
        choice = int(input("Enter your choice :"))
        if choice == 1 :
            deposit()
        elif choice == 2 :
            withdraw()
        elif choice == 3 :
            check_balence()
        elif choice == 4 :
            print("Thanku for using my atm!")
            break 
        else :
            print("invalid input !")


if __name__=="__main__" :
    main()

