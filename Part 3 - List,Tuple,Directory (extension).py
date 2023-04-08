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
#add extentions     
def printFromList(caption, creditList):
    for eachTuple in creditList:
        print(f'{caption} - {eachTuple[0]}, {eachTuple[1]}, {eachTuple[2]}')
        
repeat = 'y'
progress = 0
trailer = 0
exclude = 0
retriever = 0
progressList = []
trailerList = []
excludeList = []
retrieverList = []

#Main Version 
while repeat != 'q':
    passCredits = getValidCredit('Please enter your credits at pass: ')
    deferCredits = getValidCredit('Please enter your credits at defer: ')
    failCredits = getValidCredit('Please enter your credits at fail: ')
    creditValues = (passCredits, deferCredits, failCredits)
    if passCredits + deferCredits + failCredits == 120:
        if passCredits == 120:
            print('Progress')
            progress += 1
            progressList.append(creditValues)
        elif passCredits == 100:
            print('Progress (Module Trailer)')
            trailer += 1
            trailerList.append(creditValues)
        elif failCredits >= 80:
            print('Exclude')
            exclude += 1
            excludeList.append(creditValues)
        else:
            print('Module retriever')
            retriever += 1
            retrieverList.append(creditValues)
    else:
        print('Total incorrect')
    print('Would you like to enter another set of data?')
    repeat = input("Enter 'y' for yes or 'q' to quit and get results: ")

#Vertical Histogram
print('-'*60)   
print('Progress\tTrailing\tRetriever\tExcluded')
counters = [progress, trailer, retriever, exclude]
while sum(counters) !=0:
    line = ''
    for count in range(len(counters)):
        if counters[count] != 0:
            line = line + '    *\t\t'
            counters[count] -= 1
        else:
            line = line + '\t\t'
    print(line)
print('-'*60)

#List/Tuple/Directory 
printFromList('Progress', progressList)  #print  progress data as a list
printFromList('Progress (module trailer)', trailerList) #print  module trailer data as a list
printFromList('Module retriever', retrieverList) #print  Module retriever data as a list
printFromList('Exclude', excludeList) #print  Exclude data as a list
