#Exercise 1: Create a simple chat bot in terminal following these rules:
#Firstly, use input ask name
#Then print "Hello {0}, welcome to our service" with 0 is the value of name
#Print current list refrigerator (if first time it is empty)
#Print "We can do 2 options. 1) Add new food to refrigerator 2) remove food from refrigerator"
#Use input to ask options
#If user choose 1 use input ask new food
#Print "Here is your refrigerator after adding new food"
#Then print list refrigerator after add newfood
#If user choose 2 print "Here is your current refrigerator"
#Then print list refrigerator
#Then use input to ask the index user want to remove
#If this index is valid, print "Here is your refrigerator after removing food", then print list refrigerator
#If not, print "The index you input must larger than {0} and smaller than {1}", then ask again until index is valid
#After finishing print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again
list=[]

name=input('What is ur name? ')
print("""Hello {0}, welcome to our service""".format(name))
print('Your current refrigerator is empty')
print("""We can do two options
1) Add new food to  refrigerator
2) remove food from refrigerator
""")
ask='yes'
while ask=='yes':
    option=int(input('What is ur option? 1 or 2 '))
    if option==1:
        add=input('What do u wanna add? ')
        list.append(add)
        print('Here is ur refrigerator after adding new food')
        print(list)
    else:     
        print('Here is ur current refrigerator list')
        print(list)
        if len(list)==0:
            print("""You have nothing food on ur refrigerator to remove.
Please choose option 1 to add new food""")
        else:
            while(True):
                index=int(input('What index on the list u wanna remove? '))        
                if 0<=index and index<len(list):
                    list.pop(index)
                    print('Here is ur refrigerator after removing food')
                    print(list)
                    break
                else:
                    print("""The index you input must larger than {0} and smaller than {1}
Please try again""".format(-1,len(list)))
    print('Do u want to continue using chat box(Y/N)?')
    ask=input()
    ask=ask.lower()        


