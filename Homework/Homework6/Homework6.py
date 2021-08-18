#Exercise 1: Create a simple chatbot following these rules:
#Firstly, create a dictionary named manage_subjects
#Use input to ask number of subjects want to manage
#After that use input to ask each name of subject and its score (out of 10) and add them to dictionary
#Secondly print "We can do 3 options. 1) Check every subjects with score lower than 5 2) print average score of all subjects 3) add new subject score or change subject score"
#Use input to ask options
#If user choose 1 
#Print "Here is a list of your weak subjects {0}" with 0 is a value of list contain every weak subjects
#If user choose 2 
#Print "Here is your average scores: {0}" with 0 is a average score
#If user choose 3
#Use input to ask name of subject and its score and add it to or change it in dictionary
#After finishing print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again

manage_subjects={}
numb=int(input('Number of subjects you wanna add? '))
for i in range(1,numb+1):
    name=input('Subject: ')
    score=int(input('Score: '))
    manage_subjects[name]=score
print("""
I can do three option.
1) Check every subjects with score lower than 5
2) Print average score of all subjects
3) Add new subject score or change subject score
""")
ask='Y'
while(ask=='Y'):
    option=int(input("What is ur option? "))
    if option==1:
        for x in manage_subjects:
                list=[]
                if manage_subjects[x]< 5:
                    list.append(manage_subjects[x])
        print('Here is a list of your weak subject {0}'.format(list))
    elif option==2:
            sum=0
            for x in manage_subjects:
                sum+=manage_subjects[x]
            average=(sum)/numb
            print('Here is ur average score {0}'.format(average))
    elif option==3:
            name=input()
            score=int(input())
            manage_subjects[name]=score
            numb+=1
    print("Do u want to continue using chat box?(Y/N) ")
    ask=input()


