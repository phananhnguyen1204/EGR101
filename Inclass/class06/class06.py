#Exercise 1: Use input to ask a number. 
#Create a dictionary named square_numbers with key is from 1 to number and value is square of its key
# num=int(input('Enter ur number: '))
# square_number={}
# for i in range(1,num+1):
#      square_number[i]=i**2
# print(len(square_number))

# #Exercise 2: Print average of all value in square_numbers
# sum=0
# for key in square_number:
#     sum+=square_number[key]
# average=sum/num
# print(average)
    


#Excersie 3: number=[1,1,1,2,2,3,3,4,4,4,5,5]
#Create a dictionary named frequency with key is a element in list number and value is number of this element appears
# number=[1,1,1,2,2,3,3,4,4,4,5,5]
# frequency={}
# for i in number:
#     if i in frequency:
#         frequency[i]+=1
#     else: 
#         frequency[i]=1
# print(frequency)
    


#Exercise 4: Create a simple chat bot following these rules:
#Firstly, create a empty dictionary named students
#Secondly, use input to ask number of students want to add
#After use input to ask name of each students and their weigth and add them to dictionary
#Thirdly, ask what student do you want to see his weight
#After print this student's weight
#Finally, print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again

# student={}
# num=int(input('Number of students you wanna add '))
# for i in range(1,num+1):
#      name=input('name: ')
#      weight=input('What is ur w')
#      student[name]=weight
# ask='Y'
# while(ask=='Y'):
#      name=input('Which student do u want to see weight? ')
#      print(student[name])
#      ask=input('Do u want to continue using chat Box(Y or N)? ')
