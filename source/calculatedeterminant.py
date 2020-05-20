def calculateDeterminant(size,array):
    if size == 1:
        return array[0][0]
    if size == 2:
        return array[0][0]*array[1][1] - array[1][0]*array[0][1]

    det = 0
    i = 0

    while i < size:
        smallArray = []

        j = 1
        
        while j < size:
            internalArray = []
            k = 0
            while k < size:

                if k != i:
                    internalArray.append(array[j][k])
                k = k+1
            smallArray.append(internalArray)
            j = j +1
        if i % 2 == 0:
            det = det +  array[0][i]* calculateDeterminant(size-1, smallArray)
        else:
            det = det -  array[0][i]* calculateDeterminant(size-1, smallArray)
        i = i+1

    return det
   

print("outside")

size = int(input())
i = 0
array = []

while i < size:
    str = input()
    array.append(list(map(int,str.split())))
    i = i+1


det = calculateDeterminant(size, array)

print(det)