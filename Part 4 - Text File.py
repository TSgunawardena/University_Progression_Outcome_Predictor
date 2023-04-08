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

#Create and open file
while True:
    try:
        file = open("records.txt", "x")                       #create a new records.txt file to store data
    except FileExistsError:                                     #if an old file exists give an error
        print('Remove or rename the old records.txt file.')   #print user to remove or rename old .txt file
        retry = input('Press the enter key when you done.')     #after removing the old file user can continue by pressing enter key
        continue
    break

#define counter variables for histogram
progress = 0
trailer = 0
exclude = 0
retriever = 0

#Main Version
repeat = ''
while repeat != 'q':
    passCredits = getValidCredit('Please enter your credits at pass: ')
    deferCredits = getValidCredit('Please enter your credits at defer: ')
    failCredits = getValidCredit('Please enter your credits at fail: ')
    creditValues = (passCredits, deferCredits, failCredits)
    if passCredits + deferCredits + failCredits == 120:
        if passCredits == 120:
            print('Progress')
            progress += 1
            file.write(f'Progress - {creditValues[0]}, {creditValues[1]}, {creditValues[2]}\n')
        elif passCredits == 100:
            print('Progress (Module Trailer)')
            trailer += 1
            file.write(f'Progress (module trailer) - {creditValues[0]}, {creditValues[1]}, {creditValues[2]}\n')
        elif failCredits >= 80:
            print('Exclude')
            exclude += 1
            file.write(f'Exclude - {creditValues[0]}, {creditValues[1]}, {creditValues[2]}\n')
        else:
            print('Module retriever')
            retriever += 1
            file.write(f'Module retriever - {creditValues[0]}, {creditValues[1]}, {creditValues[2]}\n')
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
#update data to file
file.flush()
#save and close the file
file.close()
#open file in read only mode
file = open("records.txt", "r")
#print ithe file
print(file.read())
#close the file
file.close()
