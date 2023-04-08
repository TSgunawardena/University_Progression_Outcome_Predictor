def getValidCredit(message):
    creditRange = (0, 20, 40, 60, 80, 100, 120)
    while True:
        try:
            credit = int(input(message))
        except ValueError:
            print('Integer required')
            continue
        if credit in creditRange:
            break
        else:
            print('Out of range')
    return credit

progress = 0    #To count how many progress outputs
trailer = 0     #To count how many trailer outputs
exclude = 0     #To count how many exclude outputs
retriever = 0   #To count how many retriever outputs
outcomes = 0 #To count how many outcomes 

repeat = ''
while repeat != 'q':
    passCredits = getValidCredit('Please enter your credits at pass: ')
    deferCredits = getValidCredit('Please enter your credits at defer: ')
    failCredits = getValidCredit('Please enter your credits at fail: ')
    if passCredits + deferCredits + failCredits == 120:
        if passCredits == 120:
            print('Progress')
            progress += 1
        elif passCredits == 100:
            print('Progress (Module Trailer)')
            trailer += 1
        elif failCredits >= 80:
            print('Exclude')
            exclude += 1
        else:
            print('Module retriever')
            retriever += 1
        outcomes += 1
    elif passCredits + deferCredits + failCredits != 120:
        print('Total incorrect')
    print('Would you like to enter another set of data?')
    repeat = input("Enter  'y' for yes or 'q' to quit and get results: ")

#Vertical Histogram
print('-'*60)   
print('Progress\t\tTrailing\t\tRetriever\t\tExcluded')        #print topics
counters = [progress, trailer, retriever, exclude]      #make a list of counters
while sum(counters) !=0:                                #while the sum of counters equals to zero
    line = ''                                           # store a single line to print
    for count in range(len(counters)):                  #a for loop to check all counter variables
        if counters[count] != 0:                        #if counter variable is not equals to zero
            line = line + '    *\t\t'                   #concatenate line with a star
            counters[count] -= 1                        #decrease counter by 1
        else:                                           
            line = line + '\t\t'                        #concatenate line with a blank tab spaces
    print(line)                                         #print each line stored in line variable
print(outcomes, 'outcomes in total')    #print outcomes as a toatal
print('-'*60)                                           #print dash line 
