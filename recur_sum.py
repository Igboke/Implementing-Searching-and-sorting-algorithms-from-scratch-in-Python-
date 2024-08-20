#practicing recursion
def recur_sum(arr):
    #base case when arr is empty
    if arr:
        return arr.pop() + recur_sum(arr)
    #base case when arr is empty
    else:
        return 0

            