# -*- coding: utf-8 -*-
"""
#Spyder Editor

#This is a temporary script file.


print('Starting')        
     

#end = 6
#iSum = 0
#iCounter = 1
#while iCounter <= end:
#    iSum += iCounter
#    iCounter += 1
#print(iSum)
#    
#
#print('Hello!')
#for iNum in range(10,0,-2):
#    print(iNum)
    
    
    
#for iNum in range(1,end+1) :
#    iSum += iNum
#print (iSum)


#num = 10
#for num in range(5):
#    print(num)
#print(num)


#divisor = 2
#for num in range(0, 10, 2):
#    print(num/divisor) 
    
#for variable in range(20):
#    if variable % 4 == 0:
#        print(variable)
#    if variable % 16 == 0:
#        print('Foo!')    
        
        
#for letter in 'hola':
#    print(letter)       
    
#count = 0
#for letter in 'Snow!':
#    print('Letter # ' + str(count) + ' is ' + str(letter))
#    count += 1
#    break
#print(count)    

#myStr = '6.00x'
#
#for char in myStr:
#    print(char)
#
#print('done')


#greeting = 'Hello!'
#count = 0
#
#for letter in greeting:
#    count += 1
#    if count % 2 == 0:
#        print(letter)
#    print(letter)
#
#print('done')


#school = 'Massachusetts Institute of Technology'
#numVowels = 0
#numCons = 0
#
#for char in school:
#    if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#        numVowels += 1
#    elif char == 'o' or char == 'M':
#        print(char)
#    else:
#        numCons -= 1
#
#print('numVowels is: ' + str(numVowels))
#print('numCons is: ' + str(numCons)) 

#iteration = 0
#count = 0
#while iteration < 5:
#    for letter in "hello, world":
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
#
#
#print('second')
#
#count = 0
#phrase = "hello, world"
#for iteration in range(5):
#    while True:
#        count += len(phrase)
#        break
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    
#print('third')    
#    
#count = 0
#phrase = "hello, world"
#for iteration in range(5):
#    count += len(phrase)
#    print("Iteration " + str(iteration) + "; count is: " + str(count))    
#
#
#print ('another')
#
#s = "astring"
#
#school = 'abcdefiou'
#numVowels = 0
#numCons = 0
#
#for char in school:
#    if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#        numVowels += 1
#
#print('numVowels is: ' + str(numVowels))


print ('string counting')

s = 'azcbobobegghakl'
#iCounter = 0
#iFound = 0
#for char in s:
#    
#    if char == 'b':
#        # print(char + ' in position ' + str(iCounter))
#        if (s[iCounter:iCounter+3]) == 'bob':
#            iFound += 1
#    iCounter = iCounter + 1
#    
#print('Number of times bob occurs is: ' + str(iFound))
    
#s = 'abcbcd'

#maxSub, currentSub, previousChar = '', '', ''
#for char in s:
#    if char >= previousChar:
#        currentSub = currentSub + char
#        if len(currentSub) > len(maxSub):
#            maxSub = currentSub
#    else: currentSub = char
#    previousChar = char
#print ('Longest substring in alphabetical order is: ' + maxSub)



#iteration = 0
#count = 0
#while iteration < 5:
#    # the variable 'letter' in the loop stands for every 
#    # character, including spaces and commas!
#    for letter in "hello, world": 
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 

#
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
#    
    
#iteration = 0
#while iteration < 5:
#    count = 0
#    for letter in "hello, world":
#        count += 1
#        if iteration % 2 == 0:
#            break
#    print("Iteration " + str(iteration) + "; count is: " + str(count))
#    iteration += 1 
    
    
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) < epsilon:
#        break
#    else:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))    
    
    
#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))  

x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

  