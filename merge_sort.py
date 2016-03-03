#in place merge sort
def merge_sort(item):
    if (len(item) == 1):
        return item
    else:
        mid = len(item)/2
        lside = item[:mid]
        rside = item[mid:]
        
        merge_sort(lside)
        merge_sort(rside)
        
        i = j = k = 0
        while (i<len(lside) and j < len(rside)):
            print lside
            print rside
            if lside[i] < rside[j]:
                item[k]=lside[i]
                i+=1
            else:
                item[k]=rside[j]
                j+=1
            k += 1 

        while i < len(lside):
                item[k]=lside[i]
                i+=1
                k+=1

        while j < len(rside):
                item[k]=rside[j]
                j+=1
                k+=1
            
item = [5,4,3,1]
merge_sort(item)
print item
