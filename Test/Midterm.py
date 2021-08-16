#Week1
#Exercise 1: Use input to ask name, age, and hometown.
#Print Hello, my name is {}. I am {} years old and I live in {}

#Solution:
# name=input('What is your name? ')
# age=int(input('What is ur age? '))
# hometown=input('Where is ur hometown? ')
# print('Hello, my name is {}. I am {} years old and I live in {}.'.format(name,age,hometown))


#Exercise 2: Use input to ask 3 numbers
#Print average of these 3 numbers

#Solution:
# num1=int(input('number1= '))
# num2=int(input('number2= '))
# num3=int(input('number3= '))
# avr=(num1+num2+num3)/3
# print(avr)


#Exercise 3: Use input to ask gpa of student
#If gpa bigger than 9.0 print excellent
#if gpa bigger than 6.5 print good
#If gpa bigger than 5.0 print average
#Else print Weak

#Solution:
# gpa=int(input('Enter ur GPA: '))
# if gpa>9:
#     print('excellent')
# elif gpa>6.5:
#     print('good')
# elif gpa>5:
#     print('average')
# else:
#     print('weak')

#Exercise 4: Use input to ask a number 
#After that print result of number after going through flow chart in this link
#https://drive.google.com/file/d/1CXpx60fYVfJGWxP79jlwADtn2aNjj1Ju/view?usp=sharing

#Solution:
# num=float(input('Type ur number: '))
# if num<5:
#     num*=10
#     if num<2:
#         num-=6
#     else:
#         num+=5
# elif num>10:
#     num=num*num
# else:
#     num*=6
#     if num<8:
#         num=num**3
# print(num)

#Week2
#Exercise 5: Use input to ask number 
#Print every number divisible by three from 1 to this number

# #Solution:
# num=int(input('Choose a number: '))
# for i in range(1,num+1):
#     if i %3==0:
#         print(i)
    

#Exercise 6: Use input to ask number
#Print yes if this number is a prime number, else print no

#Solution:
# num=int(input('Type ur number: '))
# count=0
# if num<1:
#     print('no')
# else:
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print('yes')
#     else:
#         print('no')


#We have list zoo = ['cat', 'elephant', 'panda', 'lion']
#Exercise 7: Print the number of animal in zoo

#Solution:
# zoo = ['cat', 'elephant', 'panda', 'lion']
# length=len(zoo)
# print(length)

#Exercise 8: Use input to ask a animal
#If this animal is not already in zoo print zoo after adding this animal
#Else print This animal already in zoo and ask again (#Hint: use while)

#Solution:
# zoo = ['cat', 'elephant', 'panda', 'lion']
# while(True):
#     animal=input('Ask an animal: ')
#     if animal in zoo:
#         print("""This animal already in zoo.
# Try again""")
#     else:
#         zoo.append(animal)
#         print(zoo)
#         break
