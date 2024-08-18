''' Implementing selection sort from scratch. 0(n**2) '''

def selection_sort(lst):
    x= len(lst[:]) #copy of the list before mutation
    
    jax =[] #empty list to olace the new sorted list
    
    for _ in range(x): #iterate x times, n times
        i = 0 #getting the first element [index = 0]        
        number = lst[0]
        while i < len(lst) - 1: #iterate throughout the list, n times
            i += 1  #second element
            if number < lst[i]: 
                number = number #
            else:
                number = lst[i] #
        dax = lst.pop(lst.index(number))
        jax.append(dax)
    return jax
      
dd= [4,2, 5,6,1,0,3,8]      
print(selection_sort(dd))     