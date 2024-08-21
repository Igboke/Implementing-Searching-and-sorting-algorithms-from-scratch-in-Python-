#quicksort utilizes divide and conquer algorithm, pick a random pivot and separate the list into items greater than it and less than it
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        b1 = [i for i in arr if i > arr[0]]
        b2 = [i for i in arr if i < arr[0]]
        return quicksort(b2) + [pivot] + quicksort(b1)           
            
v=[9,6,7,4,32,24,1,20,1,0,5]    
print(quicksort(v))        
        
        
        
        
    