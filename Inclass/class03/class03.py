#Exercise 1: Use for to print every odd number between 1 and 100 in 2 different way
# for i in range(1,101):
#     print(i)
#     i+=2

    

#Exercise 2: Use while to solve exercise 1
# i=1
# while i<101:
#      print(i)
#      i+=2


#Exercise 3: Use continue and for to print all the numbers from 0 to 100 except number divided by 10.
# for i in range(0,101):
#     if i%10==0:
#         continue
#     print(i)


#Exercise 4: Use while to solve exercise 3
#Solution 1:


# i=0
# while i<101:
#     if i%10==0:
#         i+=1
#         continue
#     else:
#         print(i)
#         i+=1    


#Solution 2:
# i=0 
# while i<101:
#     if i%10!=0:
#         print(i)
#     i+=1


    

#Exercise 5: Create a simple chat bot in terminal following these rules:
#Firtsly, print "I can do 2 options. 1) calculate sum of two numbers. 2) calculate product of two numbers"
#Secondly, use input ask options (1 or 2)
#Thirdly, use input ask 2 number: number1 and number2
#If user choose 1 print sum of number 1 and number 2
#If user choose 2 print product of number 1 and number 2
#After print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again



# print("""I can do 2 options
# 1) calculate sum of two numbers.
# 2) calculate product of two numbers""" )
# ask='yes'
# while ask=='yes':
#     option=int(input('option 1 or 2: '))
#     number1=int(input('number1: '))
#     number2=int(input('number2: '))
#     if option==1:
#         sum=number2+number1
#         print(sum)
#     else:
#         product=number1*number2
#         print(product)
#     print('Do u want to continue using chat box(Y/N)? ')
#     ask=input()
#     ask=ask.lower()
