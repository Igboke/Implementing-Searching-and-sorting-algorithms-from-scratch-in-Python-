#Binary search algorithm
'''Implementation of the binary search algorithm from scratch.
It works by taking a ranfom guess in the middle, if the guess is lesser than the item searched we change the upper boundary to 1 position lesser that the original upper boundary while splitting the list and if the guess is higher that means the lower boundary needs to be changed amd the list chopped off, this is repeated till we guess correctly '''
def binary_search(lst,item):
    #start of the list
    start = 0
    #end of list
    end = len(lst) - 1
    #Binary search works only for sorted lists
    lst.sort()
    while start <= end:
        mid = (start + end) // 2
        guess = lst[mid]
        if guess == item:
            print(f'this is item {item}"s position', mid)
            break
        elif guess > item: #i.e the guess is too high
            end = mid - 1
        else: #guess is too low
            start = mid + 1
    else:
        print (f'{item} not found')        


j= [1,3,4,5,7,8,2,6,9,11,10]    
binary_search(j,11)                              