#Create a simple version of Projectube
#When run program:
#1. Use program
#2. Stop program
#If user choose 2 stop program immediately
#If user choose 1:
#1. User
#2. Orgination
#Then even user choose 1 or 2:
#1. Sign in 
#2. Sign up
#If user choose 1:
# Email: 
# Password:
#If email and password is not correct ask email and password again
#If user choose 2:
# Email:
# Password:
# Confirm password:
#If 2 passowrd is not the same ask email and 2 password again
#After user login as a User
#1. See events
#2. See orgs
#If user choose 1 list all current events with their number
#If user choose number print decriptions of this events
#If user choose 2 list all current organizations with their number
#If user choose number print decriptions of this organization
#Then:
#1. Continue to see 
#2. Logout
#If user choose 1 return to ask see events or see orgs
#If user choose 2 return to ask use program or stop program
#after user login as a Organization
#If this organation is new ask their description
#After that
#1. See events
#2. See orgs
#3. Create events
#If user choose 1 or 2 will be the same action above
#If use choose 3
#Ask how many events want to add (maximum 5)
#Then ask name of events and description
#Then:
#1. Continue to see or creaete event
#2. Logout
#If user choose 1 return to ask see events or see orgs or create events
#If user choose 2 return to ask use program or stop programs

def sign_in(account):

    print("""
    1. Use program
    2. Stop program
    """)
    use_program=int(input(''))
    while(use_program==1):
        print("""
        1. User
        2. Orgination
        """)
        user_or_org=int(input('User or org? '))
        if user_or_org==1:
            print("""
            1. Sign in 
            2. Sign up
            """)
            sign_in_or_sign_up=int(input())
            if sign_in_or_sign_up==1:
                
                while(True):
                    email=input("")
                    password=input("")
                    if email not in account:
                        print("Your account does not exit")
                    elif password!=account(email):
                        print("Your password is not correct")
                    else:
                        break
            else:
                while(True):
                    email=input("")
                    password=input("")
                    confirm=input("")
                    if email in account:
                        print("Your email has been used")
                    elif password==account(email):
                        print("Your password has been used")
                    elif confirm!=password:
                        print("Your password doesn't match")
                    else:
                        account[email]=password
                        break
    def user_actions(events, des_events, orgs, des_orgs):
        print("""
        1. See events
        2. See orgs
        """)
        option=input()
        if(option=="1"):
            for i in range(0, len(events)):
                print("{0}, {1}".format(i,events[i]))
            number=int(input())
            repeat=True
            while repeat:
                if number>=0 and number<len(des_events):
                    print(des_events[number])
                    repeat=False
        if(option=="2"):
            for i in range(0, len(orgs)):
                print("{0}, {1}".format(i,orgs[i]))
            number=int(input())
            repeat=True
            while repeat:
                if number>=0 and number<len(des_orgs):
                    print(des_orgs[number])
                    repeat=False
    def create_event(events,des_event):
        while(True):
            num=int(input("number of events: "))
            if num<=5:
                break
            else:
                print('Your numb is bigger than 5')
        for i in range(1,num+1):
            new_event=input()
            new_des_event=input()
            events.append(new_event)
            des_event.append(new_des_event)
        

                    

                


        
