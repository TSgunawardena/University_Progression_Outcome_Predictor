## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID UOW :  W1912873   Student ID IIT : 20210271
# Date: 17/04/2022
import Version.StudentVersion
#define a function called  getValidCredit for validate credit inputs
def getValidCredit(message):
    creditRange = (0, 20, 40, 60, 80, 100, 120)     #define the valid credit ranges 
    while True:
        try:                                                                                                        
            credit = int(input(message))       
        except ValueError:
            print('Integer Required')   #Integer Required, Print that When User didnt input a Integer
            continue
        if credit in creditRange:
            break       #if user input valid stop
        else:
            print('Out of Range')       #User Inputs Data over the range Print Out of Range
    return credit

#define a function called horizontalHistogram for print single line of horizontal histogram
def horizontalHistogram(caption,count):
    print(caption, count, '\t:', count*"*")

progress = 0    #To count how many progress outputs
trailer = 0     #To count how many trailer outputs
exclude = 0     #To count how many exclude outputs
retriever = 0   #To count how many retriever outputs
#creat a menu
print("student version: 1\nStaff version : 2")
version =input("Select student version or Staff version: ")
if version == '1':
    Version.StudentVersion.student()
elif version == '2':
    print ("staff version")
else:
    print("Invalid input")
    
repeat = ''     #for repeat while loop   
while repeat.lower() != 'q':
    passCredits = getValidCredit('Please enter your credits at pass: ')     #Get user input for pass credit and validate
    deferCredits = getValidCredit('Please enter your credits at defer: ')   #Get user input for defer credit and validate
    failCredits = getValidCredit('Please enter your credits at fail: ')     #Get user input for fail credit and validate
    
    if passCredits + deferCredits + failCredits != 120:     #check the total of User input credits
        print('Total incorrect')                            #if total incorrect, print  Total incorrect
    elif passCredits == 120:                    #check pass credits equals to 120
        print('Progress')                       #print progress
        progress += 1                           #increase related credit  by +1
    elif passCredits == 100:                    #check pass credits equals to 100
        print('Progress (module trailer)')      #print  Progress (module trailer) 
        trailer += 1                            #increase related credit count by +1
    elif failCredits >= 80:                     #check fail credits >= 80
        print('Exclude')                        #print  Exclude
        exclude += 1                            #increase exclude credit count by +1 
    else:
        print('Module retriever')               #print Module retriever
        retriever += 1                          #increase retriever credit count
    print('Would you like to enter another set of data?')               #ask  from the user to, enter another set of data
    repeat = input("Enter 'y' for yes or 'q' to quit and get results: ")   #get user input for quit or continue


print('-'*60)   #print line to separate sections 
print('Horizontal Histogram')    #print and display Horizontal Histogram
horizontalHistogram('Progress', progress)  #print "Progress"   
horizontalHistogram('Trailer ', trailer)            #print "Trailer"
horizontalHistogram('Retriever', retriever)    #print "Retriever"
horizontalHistogram('Excluded', exclude)    #print  "Excluded"
print(progress + trailer + retriever + exclude, 'outcome in total.') #print outcome as an integer
print('-'*60)  #Print Line to End Section



