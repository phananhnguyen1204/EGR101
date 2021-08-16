#Exercise 1: Create function with parameter n to print all square number from 1 to n

#Solution1:

# def function(n):
#     i=1
#     while i*i<=n:
#         print(i*i)
#         i+=1
# function(10)

#Exercise 2: Create function with parameter list a to print sum of all number divided by 3 in list a 

#Solution 2:

# def print_list_a(a):
#     for i in a:
#         if i%3==0:
#             print (i) 
# print_list_a([1,100,99,28,66,90])


#Exercise 3: Create function with parameter n to receive True if n is a leap year, else recieve False

#Solution 3:

# def check_a_leaf_year(a):
#     if a%4==0:
#         return True
#     else:
#         return False
# print(check_a_leaf_year(2002))

#Exercise 4: Create function with parameter n to receive n factorial

#Solution 4:

# def factorial(n):
#     result=1
#     for i in range(1,n+1):
#         result*=i
#     return result
# print(factorial(4))

#Exercise 5: Create function with parameter list a and number n to recieve True if n in a, else receive False

#Solution 5:

# def hello(a,n):
#     if n in a:
#         return 'True'
#     else:
#         return 'False'
# print(hello([1,2,4,5,6],2))

#Exercise 6: Create function with parameter list a to receive reverse of list a

#Solution 6:

# def reverse_list(a):
#     result=[]
#     for i in range(len(a)-1, -1, -1):
#         result.append(a[i])
#     return result
# print(reverse_list([1,2,3,4]))