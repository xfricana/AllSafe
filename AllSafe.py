alert = [
    [" # ", "# #", "###", "# #", "# #"],  # A
    ["#  ", "#  ", "#  ", "#  ", "###"],  # L
    ["###", "#  ", "## ", "#  ", "###"],  # E
    ["## ", "# #", "## ", "# #", "# #"],  # R
    ["###", " # ", " # ", " # ", " # "],  # T
    [" # ", " # ", " # ", "   ", " # "]   # !
]

#stores username and password
user = {
    "tosin67": "t5647", "evelyn": "jamite7890", "tofa567": "8763",
    "pezel1997": "lock4678", "tosin45": "2940", "bimpe20": "7390()"
}

#for brute force message
def brute_force():
    for row in range(5):
        for letter in alert:
            print(letter[row], end= "    ")
        print()

#welcome_page
def welcome():
    print("=====[AllSafe Cybersecurity]=====")
    print("\nEnter Username and Password to log in to the Network")
    
    attempt = 0
    option1 = input("username: ")
    while True:
        option2 = input("password: ")
        
        if option2 not in user.values():
            attempt += 1
            print("Error! You entered a wrong password")
            
            if attempt == 5 and option1 not in user.keys():
                brute_force()
                print("\nBRUTE FORCE Attack detected!")
                print("\nUnidentified user attempt multiple failed login!")
                break
        
            else:
                if attempt == 5 and option1 in user.keys():
                    brute_force()
                    print("\nPossible BRUTE FORCE Attack detected!")
                    print(option1, "attempts multiple failed log in!")
                    break
                continue         

        else:
            if option1 in user and user[option1] == option2:
                return success_log()      

#for successful log in
def success_log():   
    attempt = 0
    while True:
        print("\n[====Welcome to AllSafe Cybersecurity Network====]")
        print("\n1. Security Department\n2. HR\n3. Management")
        
        try:
            suc_option = int(input("Enter an option: "))
        except ValueError:
            print("Error! Invalid Option. ")
            continue

        #for log into security department    
        if suc_option == 1:
            attempt == 0
            
            print("Enter Username and Password to continue")
            sec_option1 = input("username: ")
            while True:
                sec_option2 = input("password: ")
                
                #for successful login
                if (sec_option1 == "tosin67" and sec_option2 == "t5647") or (sec_option1 == "evelyn" and sec_option2 == "jamite7890") or (sec_option1 == "tofa567" and sec_option2 == "8763"):
                    print("[====AllSafe Security Department====]")
                    print("\n\nWelcome to the Security Department. Your access has been verified.\n\n\nSecure the network. Protect the system.")
                    
                    #security dep. log out
                    while True:
                        try:
                            log_out = int(input('Enter "1" to log out'))
                        except ValueError:
                            print("Error! Your input is invalid. ")
                            continue
                
                        if log_out == 1:
                            print("Your have successfully being logged out.")
                            return
                        else:
                            print("Error! Enter a valid option ")
                            continue
                #for unauthorized legit users
                elif (sec_option1 == "pezel1997" and sec_option2 == "lock4678") or (sec_option1 == "tosin45" and sec_option2 == "2940") or (sec_option1 == "bimpe20" and sec_option2 == "7390()"):
                    print(sec_option1, ", you're not authorized to log into this department.\n")
                    break

                #brute force activity    
                elif sec_option2 != "t5647" and sec_option2 != "jamite7890" and sec_option2 != "8763":
                    attempt += 1
                    print("Error! Wrong password ")
                    
                    if attempt == 5:
                        if sec_option1 != "tosin67" and sec_option1 != "evelyn" and sec_option1 != "tofa567":
                            brute_force()
                            print("\nBRUTE FORCE Attack Detected!")
                            print("\nUnidentified User attempt a multiple failed log in")
                            break  
                            
                        else:        
                            brute_force()
                            print("\nPossile BRUTE FORCE Attack Detected!")
                            print(sec_option1, "attempt a multiple failed log in")
                            break
                        continue
                break
        
        #for log into HR
        elif suc_option == 2:
            attempt == 0
            print("Enter username and password to continue ")
            HR_option1 = input("username: ")
            
            while True:
                HR_option2 = input("password: ")

                #for successful log in
                if (HR_option1 == "pezel1997" and HR_option2 == "lock4678") or (HR_option1 == "tosin45" and HR_option2 == "2940"):
                    print("[====AllSafe Human Resources Department====]")
                    print("\n\nWelcome to the Human Resources Department. Your access has been verified.\n\n\nManage people. Build the organization.")

                    #for log out
                    while True:
                        try:
                            HR_log_out = int(input('Enter "1" to logout. '))
                        except ValueError:
                            print("Error! Your input is invalid ")
                            continue
                        if HR_log_out == 1:
                            print("You have successfully being logged out ")
                            return
                        else:
                            print("Error! Enter a valid option ")
                            continue
                
                #for unauthorized legit users
                elif (HR_option1 == "tosin67" and HR_option2 == "t5647") or (HR_option1 == "evelyn" and HR_option2 == "jamite7890") or (HR_option1 == "bimpe20" and HR_option2 == "7390()"):
                    print(HR_option2, ",You're not authourized to log into this department")
                    break
                
                #for brute force activity
                elif HR_option2 != "lock4678" and HR_option2 != "2940":
                    attempt += 1
                    print("Error! Wrong password! ")

                    if attempt == 5:
                        if HR_option1 != "pezel1997" and HR_option1 != "tosin67":
                            brute_force()
                            print("\nBRUTE FORCE Attack Detected!")
                            print("Unidentified user attempts multiple failed log in")
                            break

                        else:
                            brute_force()
                            print("Possible BRUTE FORCE Attack Detected!")
                            print(HR_option1, "attempts multiple failed log in")
                            break
                        continue
                break
        
        #for log into managment
        elif suc_option == 3:
            attempt == 0
            print("Enter username and password to continue")
            manag_option1 = input("username: ")

            while True:
                manag_option2 = input("password: ")
                
                #for successful log in
                if manag_option1 == "bimpe20" and manag_option2 == "7390()":
                    print("[====AllSafe Management====]")
                    print("\n\nWelcome to the Management Department. Your access has been verified.\n\n\nAccess granted. Welcome back.")

                    while True:
                        try:
                            manag_log_out = int(input('Enter "1" to log out'))
                        except ValueError:
                            print("Error! Your input is invalid")
                            continue
                        
                        #for successful log out
                        if manag_log_out == 1:
                            print("Your have successfully being logged out")
                            return
                        else:
                            print("Error! Enter a valid option ")
                            continue

                #for unauthorized legit users
                elif (manag_option1 == "tosin67" and manag_option2 == "t5647") or (manag_option1 == "evelyn" and manag_option2 == "jamite7890") or (manag_option1 == "tofa567" and manag_option2 == "8763") or (manag_option1 == "pezel1997" and manag_option2 == "lock4678") or (manag_option1 == "tosin45" and manag_option2 == "2940"):
                    print(manag_option1, ",you're not authourized to log in this department.")
                    break
                
                #for brute force attack
                elif manag_option2 != "7390()":
                    attempt += 1
                    print("Error! Wrong password ")

                    if attempt == 5:
                        if manag_option1 != "bimpe20" and manag_option2 != "7390()":
                            brute_force()
                            print("BRUTE FORCE Attack Detected!")
                            print("Unidentified user attempt multiple failed log in!")
                            break

                        else:
                            brute_force()
                            print("Possible BRUTE FORCE Attack Detected!")
                            print(manag_option2, ", attempt multiple failef log in")
                            break
                        continue
                break
        
        else:
            print("Error! Enter a valid option ")
            continue
        break

welcome()
