def selection_sort(list):
    for i in range(len(list)):
        for j in range (i+1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

def insertion_sort(list, n=None):
    if n == None:
        n = len(list)
    if n <= 1:
        return list
    insertion_sort(list,n-1)
    last = list[n-1]
    j = n-2

    while j>=0 and list[j]>last:
        list[j+1] = list[j]
        j = j-1
    
    list[j+1] = last
    return list
