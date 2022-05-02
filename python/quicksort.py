from pathlib import Path
inFile = open("quicksortfile.txt", 'r')
with inFile as f:
    lines = [x.split() for x in f]  # a list of lists
    f.close()

    tempList =  zip(*lines)           # a list of tuples := transposed lines
    tempList = list(tempList)
    tempList = tempList[0]      # a list of strings
    
    A = map(int,tempList)               # a list of integers
    


def choosePivot(alist,first,last,pivotID):
    if pivotID == 'first':
        pass
    
    if pivotID == 'last':
        (alist[first], alist[last]) = (alist[last], alist[first])
        
    elif pivotID == 'middle':
        mid = (last-first)//2 + first
        listTemp = [alist[first], alist[last], alist[mid]]
        listTemp.sort()
        if listTemp[1] == alist[first]:
            pivotIndex = first
        elif listTemp[1] == alist[last]:
            pivotIndex = last
        else:
            pivotIndex = mid
        (alist[first], alist[pivotIndex]) = (alist[pivotIndex], alist[first])
        
        
    
def partition(alist, first, last):
    pivotVal = alist[first] # initialise pivot as the first element
    leftmark = first+1
    for rightmark in range(first+1,last+1):
        if alist[rightmark] < pivotVal:
            (alist[leftmark],alist[rightmark]) = (alist[rightmark],alist[leftmark])
            leftmark = leftmark + 1
    (alist[leftmark-1],alist[first]) = (alist[first],alist[leftmark-1])

    return leftmark-1       # partition point := where pivot finally occupies
    
    
    
def quickSort(alist,first,last,pivotID):
    pivotID = "middle"
    numComp = last -first
    if last <= first:
        return (alist, 0)
    else:
        choosePivot(alist,first,last,pivotID)
        splitpoint = partition(alist,first,last)
        (Lsorted,numCompL) = quickSort(alist, first, splitpoint-1, pivotID)
        (Rsorted,numCompR) = quickSort(alist, splitpoint+1, last, pivotID)
        numComp =  numComp + numCompL + numCompR
    return (alist, numComp)
    

def main(fileName):
    pivotList =  ['last', 'middle', 'first']
    
    for pivotID in pivotList:
        A = list(fileName)
        (A, n) = quickSort(A,0,len(A)-1,pivotID)
        print ("number of comparisons: %d", n)

def main2(fileName):
    pivotList =  ['first', 'middle', 'last']
    mainList = list(fileName)
    for pivotID in pivotList:
        A = mainList[:]
        (A, n) = quickSort(A,0,len(A)-1,pivotID)
        print ("number of comparisons: %d", n)
    
if __name__ == '__main__':
        # unit test
#        main('test.txt')
        main(A)
        # main2(A)