from datetime import datetime

status = False

def door():
    trials = 2
    password = "abc123"                                     #preset password: use this password to gain acces to the door
    bl = True
    while bl:
        user_password = input("enter your password: ")
        if password == user_password:                       #password comparison
            print("welcome")
            bl = False                              #once the password is accepted, the boolean variable becomes false hence program breaks out of while loop
        elif trials == 0:
            
            return 0
        else:

            print(f"wrong password\nyou have {trials} remaining trials")
            trials -=1
if door()==0:
    print("you have entered the wrong password 3 times\ncontact group36 members")
else:
    command_list = ["open","close","quit"]                 #list of accepted commands
    bol = True
    count = 0
    while bol:
        val = True
        while val:
            command = input("enter your command: ")
            if command in command_list:                 #checks to see if command issued is part of the commands suite
                val = False
            else:
                print("invalid input")
                print("use one of the following commands!!:",command_list)
        if count == 0 and command == "open":
            open_date=datetime.now()                    #datetime.now records the first time oor is opened
            print("door last open at ",open_date)       
            print("the door is now open")
            count += 1
        elif count!= 0 and command == "open":
            print("door last open at ",open_date)
            print("the door is already open!")                #since count variable is more than zero, it means the door was already opened
        elif count!=0 and command == "close":
            close_date=datetime.now()                      #datetime.now records last time door was closed
            print("door last closed at ",close_date)
            print("the door is now locked")
            count = 0                                       #reset the count to zero since door is now closed
        elif count == 0 and command == "close":
            print("the door is already locked!")           #since count variable is more than  zero, it means the door was already closed
        else:
            print("goodbye!!")
            bol = False

