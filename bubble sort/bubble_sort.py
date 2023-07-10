def bubble_sort(lst:list):
    '''
It's basically swapping the large elements to the right side of the list
if the left side is larger than the right side we swape them. 

'''
    for i in range(len(lst),1,-1):
        for j in range(1,i):
            if lst[j-1] > lst[j]:
                lst[j-1],lst[j] = lst[j],lst[j-1]  # Swape if the left side is bigger than the right one 
    return lst

my_lst= [5,4,1,8,9,10]
print(bubble_sort(my_lst))

