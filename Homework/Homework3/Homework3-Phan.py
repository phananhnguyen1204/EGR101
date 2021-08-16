#Exercise 1: Use for to print every square number between 1 and 100
# for i in range(1,11):
#     print(i**2)

#Exercise 2: Use while to solve exercise 1
# i=1
# while i*i < 101:
#     print(i*i)
#     i+=1


#Exercise 3: Create a simple chat bot in terminal following these rules:
#Firstly, use input ask name
#Then print "Hello {0}, how can I help you" with 0 is the value of name
#Use input ask current_money
#print "I can do 2 options. 1) withdraw money 2) add more money"
#Use input to ask option
#If user choose 1 use input ask withdraw money
#Then print "Now you have {0} $" with 0 is the current money AFTER WITHDRAW
#If user choose 2 use input ask withdraw money
#Then print "Now you have {0) $" with 0 is the current money AFTER ADD
#After print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again


# name=(input('What is ur name? '))
# print('Hello {}, how can I help u? '.format(name))
# current_money=int(input('What is ur current money? '))
# print("""I can do two options
# 1) Withdraw money
# 2) Add more money""")
# ask='yes'
# while ask=='yes':
#     option=int(input('Choose ur options (1 or 2) '))
#     if option==1:
        
#         while(True):
#             withdraw=int(input('How much do u want to withdraw? '))
#             if withdraw>current_money:
#                 print("""U dont have enough money on ur account.
#                 Please try again""")
#             else:
#                 result=current_money-withdraw
#                 break
            
#     else:
#         add=int(input('How much do u wanna add? '))
#         result=add+current_money
#     print('Now u have {}$ on your account'.format(result))
#     print('Do u want to continue using chat box?(Yes or No)')
#     ask=input()
#     ask=ask.lower()
# name=input('What is your name? ')
# print('Hello {}. How can I help you?'.format(name))
# money=int(input('Type your current money here: '))
# ask='yes'
# while ask=='yes':
#     print("""I can do two options.
#     1) Withdraw money
#     2) Add more money
#     """)
#     option=int(input('Choose your option: '))
#     if option==1:
#         withdraw=int(input('How much money do u wanna withdraw? '))
#         if withdraw<=money:
#             result=money-withdraw

#             print("Now u have {} $ on ur account".format(result))
#         else:
#             print('Not enough value. Try again!')
#     else:
#         add=int(input('How much money do u wanna add?'))
#         result=money+add
#         print('Now u have {} $ on ur account'.format(result))
#     print('Do u want to continue using chat box(Y/N)? ')
#     ask=input('Yes or No? ')
#     ask=ask.lower()
#     money=result
