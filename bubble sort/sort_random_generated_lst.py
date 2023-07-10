import random 

def generate_lst(n:int):
    my_lst = []
    
    for i in range(n):
        my_lst.append(random.randint(0,n*4))
    return my_lst


def bubble_sort(my_lst):
    for i in range(len(my_lst),1,-1):
        for j in range(1,i):
            if my_lst[j-1] > my_lst[j]:
                my_lst[j-1],my_lst[j] = my_lst[j],my_lst[j-1]
    return my_lst


def main():
    x= generate_lst(20)
    print(x,'Unsorted')
    y= bubble_sort(x)
    print(y,'sorted')



if __name__ == '__main__':
    main()



