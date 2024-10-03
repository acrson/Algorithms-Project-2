"""
Algorithms Project 2

TO-DO:
    FAY:
    - Implement bubble sort
    - Implement merge sort
    
    
    CARSON:
    - Premake arrays before testing for best, avg, worst cases depending on array size n
    - Document how long best, avg, worst case took for each sort, with array size n = 100, 1000, 10000
    
    SERA:
    - Implement quick sort
    - Front end

Also, maybe we should implement front end / main last this time? I think we had
a good idea trying to do it first last time but it bit us in the booties a little.
We could discuss this in greater detail though
"""

import random as rd
import time

# BUBBLE SORT *****

def bubbleSort(myList):
    sorted = False;
    for i in range(len(myList)-1):
        swap = False;
        if not sorted:
            for j in range(len(myList)-i-1):
                if myList[j] > myList[j + 1]:
                    myList[j], myList[j+1] = myList[j+1], myList[j]
                    swap = True;
                if not swap:
                    break
    return myList;

# MERGE SORT ******

# Divide
def merge_sort(m):
    if len(m) <= 1:
        return m
    middle = len(m) //2
    left = m[:middle]
    right = m[middle:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

#Conquer
def merge(left,right):
    result = []
    left_in , right_in = 0,0
    while left_in < len(left) and right_in < len(right):
        if left[left_in] <= right[right_in]:
            result.append(left[left_in])
            left_in += 1
        else:
            result.append(right[right_in])
            right_in += 1
    if left_in < len(left):
        result.extend(left[left_in:])
    if right_in < len(right):
        result.extend(right[right_in:])
    return result
# QUICK SORT ******

# Funct (find divi pos.)
def divider(array, low, high):
    pivot = array[high] #pivot left/right
    i = low - 1 # ptr i

    # traverse all ele.// ele. compare pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i]) # swap i/j

    # Swap the pivot ele. w/ higher ele
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

# actual quick sort
def quick(array, low, high):
    if low < high:

        # Find pivot ele
        pi = divider(array, low, high)

        # Recursive call left 
        quick(array, low, pi - 1)

        # Recursive call right
        quick(array, pi + 1, high) 


# RADIX SORT ******

# Set current_digit to be the digit of the element currently being operated on
def current_digit(element, digit):
    exp = pow(10, digit)
    
    current_digit = (element // exp) % 10
    
    return current_digit


# Sort the passed array using radix sort
def radix_sort(arr):
    num = 0 # Initialization of current_digit
    new_arr = arr # Initialize new_arr as a new array copy of arr
        
    for digit in range(len(str(max(arr)))): # Iterate for each digit found in the largest element of arr
        # Initialization of 10 bucket lists stored within a list of lists, "buckets"
        buckets = [[] for i in range(10)]
        
        for element in new_arr: # Iterate through the array
            # Set current_digit to appropriate current digit (ex: 283, one's place -> 3)
            num = current_digit(element, digit)
            # Put the current element of arr into its respective bucket (ex: num == 3; element -> bucket[3])
            buckets[num].append(element)
        
        # Unpack the list of lists "buckets" into a singular list in new_arr, ready to sort through the next
        # most significant digit in the next iteration if possible
        new_arr = [item for bucket in buckets for item in bucket]
            
    return new_arr



# MAIN ***********************************************************************************************************************************************
"""
Order of menu content:
    - indiv sort menus
    - sortType
    - front end
    - menu
    
"""

def quickMenu():
    boolsub = False
    choice2 = ['']
    while (boolsub == False):
        print ("\n Case Scenarios for Quick Sort\n---------------")
        print("    1. Best case")
        print("    2. Average case")
        print("    3. Worst case")
        print("    4. Exit Quick sort test")
        choice2[0] = input("    \nSelect a sorting algorithm (1-5): ")

def sortType(choice1):
    boolsub = False
    
    # calls one of these functions
    while (boolsub == False):
        #calls each sort
        if choice1[0] == '1': # Bubble
            print("no info yet")
     
        elif choice1[0] == '2': # Merge
            print("no info yet")
 
        elif choice1[0] == '3': # Quick
            quickMenu(choice1)
     
        elif choice1[0] == '4': # Radix
            print("no info yet")
            
        else:
            choice1 = input("Invalid choice made. Please enter one of the available options: ")

def frontEnd():
    bool = False
    choice1 = ['']
    while(bool == False):
        print("\nWelcome to the test suite of selected sorting algorithms!\n")
        print("Select the Sorting Algorithm you want to test.\n-------------------------")
        print("    1. Bubble Sort")
        print("    2. Merge Sort")
        print("    3. Quick Sort")
        print("    4. Radix Sort")
        print("    5. Exit")
        choice1[0] = input("    \nSelect a sorting algorithm (1-5): ")
        
        # call sort types
        sortType(choice1)
        
        if choice1[0] == '5':  # Check if exit was chosen
            print("\nBye!") 
            break

def main():
    print("- SORT TESTER -\n")
    avg_arr = []
    best_arr = []
    worst_arr = []
        
    # Creates a randomly generated array of size n based on user input:
    # (ex: avg_arr[0] is average sorted arr with size 100, best_arr[0] and worst_arr[0] are both
    #  created based upon avg_arr[0]; avg_arr[1] is average sorted arr with size 1000 . . .)
    for i in range(4):
        n = 100 * pow(10, i)
        avg_arr.append([rd.randint(1,2*n) for i in range(n)])
        best_arr.append(radix_sort(avg_arr[i]))
        worst_arr.append(best_arr[i][::-1])
    
    # front end I/O
    frontEnd() 
    
    print("Best:  1")
    print("Avg:   2")
    print("Worst: 3\n")
    
    arr_option = input("Which array would you like to sort? : ")
    print("\n")
    
    if arr_option == '1':
        arr = best_arr
        arr_name = "Best case"
    elif arr_option == '2':
        arr = avg_arr
        arr_name = "Average case"
    elif arr_option == '3':
        arr = worst_arr
        arr_name = "Worst case"
    else:
        # gotta make this into an error handling loop
        print("ERROR: INVALID ARRAY OPTION SELECTED. PLEASE SELECT A NUMBER 1 - 3.\n")
    
    for i in range(4):
        # If selected sort is radix sort:
        t0 = time.perf_counter()
        sorted_list = radix_sort(arr[i]) # hey loook this thongy, need? yes? no?
        t1 = time.perf_counter()  
        # Replace "Radix sort" with sort_name when more sorts are implemented into an if-else chain
        print("Time cost of: ", "Radix sort,", len(arr[i]), "elements,", arr_name, ":", t1-t0, "seconds.\n")


if __name__ == "__main__":
    main()