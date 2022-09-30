def primeSum(arr):
    result = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            if arr[i] not in result:
                result.append(arr[i])
    return result

arr =[1,2,2,3,3,4,5,6,6,6,7]

print(primeSum(arr))
