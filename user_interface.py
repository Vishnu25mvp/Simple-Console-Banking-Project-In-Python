import business_logic as logic

def main_menu():
    while True:
        print("WELOCME TO MVP BANK")
        print("1. Log in")
        print("Sing-up")
        option = int(input("Enter Your Option(1,2):"))
        if option == 1:
            email=input("Enter Your E-mail ID : ")
            password = input("Enter Your Password : ")
            log = logic.login(email,password)
            # print(log)
            while bool(log) is True:
                print("Choice Your Option:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transaction")
                print("4. Balance")
                print("5. Exit")
                opt = int(input("Enter (1,2,3,4) :"))
                if opt ==1:
                    amt = int(input("Enter Your Amount to Deposit : "))
                    logic.deposit(log,amt)
                elif opt ==2:
                    amt = int(input("Enter Your Amount to Withdraw : "))
                    logic.withdraw(log,amt)
                elif opt==3:
                    logic.transccation(log)
                elif opt==4:
                    logic.bal(log)
                elif opt==5:
                    log = False
                else:
                    print("Invaild Number")

        elif option ==2:
            name = input("Enter Your Name : ")
            ph = input("Enter Your Phone Number : ")
            email = input("Enter Your Mail id")
            passwd = input("Enter Your Password : ")
            logic.singin(name,ph,email,passwd)
        else:
            print("Invaild Option")

if __name__ == "__main__":
    main_menu()
