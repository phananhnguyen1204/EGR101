# numbers=[1,3,4,5,2]

# #Exercise 1: Do not use len(). print the length of list numbers.
# #Hint: Use for in list
# length=0
# for i in list:
#     length+=1
# print(length)



#Exercise 2: Use input to ask number. Add this number at the end of list numbers.
# list=[]
# number=int(input('Type ur number: '))
# list=list.append(number)



#Exercise 3: Similar to exercise 2 but if add number already exist in list numbers. Do not add and print "This number already exists"
#Solution 1:
# list=[1,2,3,6,3,7]
# num=int(input('What is ur number? '))
# already_exists=False
# for i in list:
#     if i==num:
#         already_exists=True
#         break
# if already_exists==False:
#     list.append(num)
#     print(list)
# else:
#     print('This number already exists')

#Solution 2:
# list=[1,2,3,6,3,7]
# num=int(input('What is ur number? '))
# if num in list:
#     print('This number already exists')
# else:
#     list.append(num)
#     print(list)



    
#Exercise 4: Use input to ask index. 
#If this index is valid, remove element at this list at index
#If not, print index is invalid
# list=[1,2,3,6,4,7]
# index=int(input('Index u wanna remove is? '))
# if index<len(list)and index>=0:
#     list.pop(index)
#     print(list)
# else:
#     print('This index is not valid')


# #Exercise 5: Use input to ask number. Remove this number from list numbers if it exists

# list=[1,2,3,4,5,10]
# num=int(input('What is ur number? '))
# if num in list:
#     list.remove(num)
#     print(list)
# else:
#     print('number does not exist')

# #Exercise 6: Print all element larger than 3 in list numbers
# list=[1,2,1,4,7,2,8]
# for num in list:
#     if num>3:
#         print(num)
    

# #Exercise 7: Print second smallest number and second largest number in list numbers
list=[1,3,2,6,2,2,10]
list.sort()
print(list[len(list)-2])
print(list[1])


# #Exercise 8: Add even numbers from 1 to 100 to a new list and print it
list=[]
for i in range(1,101):
    if i%2==0:
        list.append(i)
print(list)

