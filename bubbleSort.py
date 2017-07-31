#!/usr/bin/python
#Python implementation of Bubble Sort

def bubbleSort(list):
        print("Unsorted list: ",list)
        for x in range(len(list)-1): #range 0 to length of array (10)-1 = range(9)
                for y in range(len(list)-x-1): #Length of array=10, initial value of x = 0. 10-0-9 = 1. Traverse 0 to 1
                        if (list[y] > list[y+1]):
                                list[y], list[y+1] = list[y+1], list[y]
        return list

arrlist = [67,90,0,-40,9,192,333,3892,-22,-434] #sample array to be sorted
bubbleSort(arrlist)
print("Sorted list: ",arrlist)
