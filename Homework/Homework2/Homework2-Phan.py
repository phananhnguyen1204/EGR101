#Exercise 1: Use input ask year. 
#print "yes" if this year is leap year
#print "no" if this year is not leap year


# print('Wanna know whether it is a leap year or not?')
# a=int(input('Enter a year: '))
# if a%4==0:
#      print('yes')
# else:
#      print('no')


#Exercise 2: Create a simple chat bot in terminal following these rules:
#Firstly, use input ask name
#Then print "Hello {0}, how can I help you" with 0 is the value of name
#print "I can do 2 options. 1) calculate substraction of two numbers. 2) calculate division of two numbers"
#Secondly, use input ask options (1 or 2)
#Thirdly, use input ask 2 number: number1 and number2
#If user choose 1 print substraction of number 1 and number 2
#If user choose 2 print division of number 1 and number 2


# name=input('What is ur name? ')
# print('Hello {0}, how can I help you?'.format(name))
# print("""I can do 2 options
# 1) Calculate subtraction of two numbers
# 2) Calculate division of two numbers""")
# option=int(input('Option 1 or 2: '))
# number1=int(input('number1: '))
# number2=int(input('number2: '))
# if option==1:
#     subtract=number1-number2
#     print(subtract)
# else:
#     division=number1/number2
#     print(division)

name=input()
print( "Hello {0}, how can I help you".format(name))
print("""
I can do 2 options. 
1) calculate substraction of two numbers. 
2) calculate division of two numbers
""")

while(True):
    option=input()
    
    if option != "1" and option!="2":
        print('Do it again! Option should be either 1 or 2')
    else:
        number1=int(input())
        number2=int(input())
        if option=='1':
            print(number1-number2)
        else:
            print(number1/number2)
        break