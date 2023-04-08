
def student(): #define a function
   
    passCredits = int (input('Please enter your credits at pass: '))     #Get user input for pass credit and validate
    deferCredits = int(input('Please enter your credits at defer: ') )  #Get user input for defer credit and validate
    failCredits = int(input('Please enter your credits at fail: ') )    #Get user input for fail credit and validate
    
    if passCredits + deferCredits + failCredits != 120:     #check the total of User input credits
        print('Total incorrect')                            #if total incorrect, print  Total incorrect
    elif passCredits == 120:                    #check pass credits equals to 120
        print('Progress')                       #print progress

    elif passCredits == 100:                    #check pass credits equals to 100
        print('Progress (module trailer)')      #print  Progress (module trailer) 
 
    elif failCredits >= 80:                     #check fail credits >= 80
        print('Exclude')                        #print  Exclude
      
    else:
        print('Module retriever')               #print Module retriever
   
    
