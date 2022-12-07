def search(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i] == x:
            return i
 
    return -1

'''Time complexity is O(N) which is not very efficient'''