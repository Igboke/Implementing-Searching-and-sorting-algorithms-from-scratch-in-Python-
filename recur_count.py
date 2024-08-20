#Write a recursive function to count the number of  items in a list.
#base case ==> lst = []
def count_(lst):
    if lst:
        lst.pop()
        return 1 + count_(lst)
    else:
        return 0

                              