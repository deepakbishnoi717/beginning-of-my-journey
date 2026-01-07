import json
import os      

def load_account():
    if not os.path.exists("account.json"):
        raise FileNotFoundError("account.json not found. Please create it first.")
    
    with open("account.json", "r") as file :
        return json.load(file)
        
def save_account(account):
    with open("account.json","w") as f:
        json.dump(account,f,indent=4)

#############  ATM METHODS ##############
def security():
    account = load_account()
    try :
       p = int(input("Enter the pin :"))
    except ValueError :
        print("Invalid input! Please enter a number.")
        return False
    if int(account["pin"]) == p :
        return True
    
    print("Wrong Pin!")
    return False

def deposit():
    account = load_account()
    amount = int(input("Enter amount for deposit :"))
    account["balance"] += amount
    save_account(account)
    print(f"{amount} Rs is deposited in your account {account['account']}" )

def withdraw():
    account = load_account()
    amount = int(input("Enter the amount for withraw :"))
    if amount > account["balance"] :
        print("insufficent balance !")
        return
    
    account["balance"] -= amount 
    save_account(account)
    print(f"{amount} Rs is dabited from your account {account['account']}")

def check_balance():
    account = load_account()
    print(f"Avilable Balance :Rs {account['balance']}")

#################### MAIN CLASS ##################

def main():
    if not security():
        return
    
    while True :
        print("ATM Buttons!")
        print("press 1 for deposite.")
        print("press 2 for withdraw.")
        print("press 3 for check balance.")
        print("press 4 for exit.")
        
        try :
           choice = int(input("Enter your choice :"))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1 :
            deposit()
        elif choice == 2 :
            withdraw()
        elif choice == 3 :
            check_balance()
        elif choice == 4 :
            print("Thank you for using my Atm!")
            break 
        else :
            print("invalid input !")


if __name__=="__main__" :
    main()

