# #1:
# name='Bao'
# age=18
# characteristic="handsome"
# friend="Thanh"
# print('His name is {1}. {0} is {2} years old and {1} is {2}. {0} is {3}.'.format(name,friend,age,characteristic))

# #2:
# a=3
# b=9
# print(not((True and (True or False))and a**2>=b))

# #4:
# for i in range(1,1000):
#     if i%10==0 or i==5:
#         continue
#     print(i)

# #5:
# i=1
# while i<100:
#     if i%5==0:
#         print(i)
#     i+=1

# #6:
# num1=input('Enter your number: ')
# num2=input('Enter your number: ')
# print(num1+num2)

# #7:
# list=[1,2,3,5,6,9,10]
# list.insert(len(list)+1,11)
# list.remove(2)
# print(list)

# #10:
# def mysterious_function(n,a):
#     if n%2==0 and n not in a:
#         return True
#     return False
# print(mysterious_function(5,[1,2,3,]))

# #12:
def mysterious_function(numbers):
    dic={}
    for number in numbers:
        dic[number]=0
        dic[number]+=1
    return dic
print(mysterious_function([1,2,3,4,2,5,6,7]))
