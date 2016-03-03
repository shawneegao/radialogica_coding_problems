import sys

original = sys.argv[1]
testRotation = sys.argv[2]

#function cycles through indexes to compare 2 strings
def compareStrings(startIndex, originalStartIndex, testRotation, original):
    test_index = startIndex
    stop = False
    while not stop:
        if original[originalStartIndex] != testRotation[test_index]:
            return False
        else:
            originalStartIndex += 1
            test_index += 1
         
            if originalStartIndex >= len(original):
                originalStartIndex = 0
            if test_index >= len(testRotation):
                test_index = 0
                
            if test_index == startIndex:
                stop = True
                
    return True
    
#locates and tries all possible start indexes
def rotation(original, testRotation):
    originalStartIndex = None
    
    if(len(original) != len(testRotation)):
        return False
    else:
        firstChar = None
        followChar = None
        for i in range(len(testRotation)):
            if i == len(testRotation)-1:
                #this means a string is all one char or just one char
                for c in testRotation:
                    if c != orginal[0]: 
                        return False
                return True
            #finds a 2 character pattern to look for incase string looks like 'abcabdabgabk'   
            elif original[i] != original[i+1]:
               firstChar = original[i]
               originalStartIndex = i
               followChar= original[i+1]
               break
     
    
    start_index = None #start index of testRotation
    first_time = True  #checks if this is our first time entire the while loop
    
    #looks for the 2 character pattern, and repetitly checks for rotations at every occurence of the 2 char pattern
    while (start_index is not None or first_time):
        first_time = False
        if start_index is not None:
            if compareStrings(start_index,originalStartIndex,original,testRotation):
                return True
            start_index += 1
        if start_index > len(testRotation):
            return False
            
      #If we get to this point we need to look for a start_index
        elif start_index is None:
            start_index = 0
            new_start_index = None
        for i in range(start_index, len(testRotation)):
            if testRotation[i]== firstChar:
                if i != len(testRotation)-1:
                    if testRotation[i+1] == followChar:
                        new_start_index = i
                elif testRotation[0] == followChar:
                    new_start_index = i
                else:
                    break
        if new_start_index is None:
            return False
        else:
            start_index = new_start_index
 

if rotation(original,testRotation):
    print "is rotation"
else:
    print "not rotation"
