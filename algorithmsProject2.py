"""
Algorithms Project 2

Members:
Fathia Tafesh
Sera Yang

"""

import random as rd
import time
import sys

# BUBBLE SORT *********************************************************************************************************

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

# MERGE SORT ***************************************************************************************************************

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

# QUICK SORT ******************************************************************************************************************

# Funct (find divi pos.)
def divider(arr, low, high):
    pivot = arr[high] #pivot left/right
    i = low - 1 # ptr i

    # traverse all ele.// ele. compare pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i]) # swap i/j
            
    # Swap the pivot ele. w/ higher ele
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1

# actual quick sort
def quick(arr, low, high):
    if low < high:

        # Find pivot ele
        pi = divider(arr, low, high)

        # Recursive call left 
        quick(arr, low, pi - 1)

        # Recursive call right
        quick(arr, pi + 1, high) 


# RADIX SORT **********************************************************************************************************************

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



# MAIN ***************************************************************************************************************************
"""
Order of menu content:
    - indiv sort menus
    - sortType
    - front end
    - menu
    
"""
def radixMenu(best_arr, avg_arr, worst_arr):
    boolsub2 = False
    choice2 = ''
    while (boolsub2 == False):
        print ("\nCase Scenarios for Radix Sort\n---------------")
        print("    1. Best case")
        print("    2. Average case")
        print("    3. Worst case")
        print("    4. Exit Radix sort test")
        choice2 = input("    \nSelect the case (1-4): ")
        caseN = ''
        arr = [] 
        
        # time complexity options
        if choice2== '1': # best case
            arr = best_arr
            caseN = 'best'
        elif choice2 == '2': # avg case
            arr = avg_arr
            caseN = 'average'
        elif choice2 == '3': # worst case
            arr = worst_arr
            caseN = 'worse'
        elif choice2 == '4': # exit menu
            boolsub2 = True 
            continue
        else:
            choice2 = input("Invalid choice made. Please enter one of the available options (1-4): ")
        
        # run cases
        sys.setrecursionlimit(100001)
        # counts time for sort
        for i in range(len(arr)):
            if len(arr[i]) > 10000:  # stop at 10,000
                break
            
            t0 = time.perf_counter()
            radix_sort(arr[i])
            t1 = time.perf_counter()
            print ("\nIn the ", caseN, " case,")
            print("For N = ", {len(arr[i])}, " it takes ", (t1 - t0), "seconds")
            
        choiceN = input("Do you want to input another value of N (Y/N)? ")
        if choiceN == 'y' or choiceN == 'Y':
            choiceN2 = int(input("What is the N? "))
            t0 = time.perf_counter()
            radix_sort(arr[i])
            t1 = time.perf_counter()
            print("\nFor N = ", choiceN2, ", it takes ", (t1 - t0)," seconds")
            
        elif choiceN == "n" or choiceN =="N":
            continue
 


def quickMenu(best_arr, avg_arr, worst_arr):
    boolsub2 = False
    choice2 = ''
    while (boolsub2 == False):
        print ("\nCase Scenarios for Quick Sort\n---------------")
        print("    1. Best case")
        print("    2. Average case")
        print("    3. Worst case")
        print("    4. Exit Quick sort test")
        choice2 = input("    \nSelect the case (1-4): ")
        caseN = ''
        arr = [] 
        
        # time complexity options
        if choice2== '1': # best case
            arr = best_arr
            caseN = 'best'
        elif choice2 == '2': # avg case
            arr = avg_arr
            caseN = 'average'
        elif choice2 == '3': # worst case
            arr = worst_arr
            caseN = 'worse'
        elif choice2 == '4': # exit menu
            boolsub2 = True 
            continue
        else:
            choice2 = input("Invalid choice made. Please enter one of the available options (1-4): ")
        
        # run cases
        sys.setrecursionlimit(100001)
        # counts time for sort
        for i in range(len(arr)):
            if len(arr[i]) > 10000:  # stop at 10,000
                break
            
            t0 = time.perf_counter()
            quick(arr[i], 0, len(arr[i]) - 1)
            t1 = time.perf_counter()
            print ("\nIn the ", caseN, " case,")
            print("For N = ", {len(arr[i])}, " it takes ", (t1 - t0), "seconds")
            
        choiceN = input("Do you want to input another value of N (Y/N)? ")
        if choiceN == 'y' or choiceN == 'Y':
            choiceN2 = int(input("What is the N? "))
            t0 = time.perf_counter()
            quick(arr[i], 0, choiceN2 - 1)
            t1 = time.perf_counter()
            print("\nFor N = ", choiceN2, ", it takes ", (t1 - t0)," seconds")
            
        elif choiceN == "n" or choiceN =="N":
            continue
 
def mergeMenu(best_arr, avg_arr, worst_arr):
     boolsub2 = False
     choice2 = ''
     while (boolsub2 == False):
         print ("\nCase Scenarios for Merge Sort\n---------------")
         print("    1. Best case")
         print("    2. Average case")
         print("    3. Worst case")
         print("    4. Exit Merge sort test")
         choice2 = input("    \nSelect the case (1-4): ")
         caseN = ''
         arr = [] 
         
         # time complexity options
         if choice2== '1': # best case
             arr = best_arr
             caseN = 'best'
         elif choice2 == '2': # avg case
             arr = avg_arr
             caseN = 'average'
         elif choice2 == '3': # worst case
             arr = worst_arr
             caseN = 'worse'
         elif choice2 == '4': # exit menu
             boolsub2 = True 
             continue
         else:
             choice2 = input("Invalid choice made. Please enter one of the available options (1-4): ")
         
         # run cases
         sys.setrecursionlimit(100001)
         # counts time for sort
         for i in range(len(arr)):
             if len(arr[i]) > 10000:  # stop at 10,000
                 break
             
             t0 = time.perf_counter()
             merge_sort(arr[i])
             t1 = time.perf_counter()
             print ("\nIn the ", caseN, " case,")
             print("For N = ", {len(arr[i])}, " it takes ", (t1 - t0), "seconds")
             
         choiceN = input("Do you want to input another value of N (Y/N)? ")
         if choiceN == 'y' or choiceN == 'Y':
             choiceN2 = int(input("What is the N? "))
             t0 = time.perf_counter()
             merge_sort(arr[i])
             t1 = time.perf_counter()
             print("\nFor N = ", choiceN2, ", it takes ", (t1 - t0)," seconds")
             
         elif choiceN == "n" or choiceN =="N":
             continue
         

def bubbleMenu(best_arr, avg_arr, worst_arr):
    boolsub2 = False
    choice2 = ''
    while (boolsub2 == False):
        print ("\nCase Scenarios for Bubble Sort\n---------------")
        print("    1. Best case")
        print("    2. Average case")
        print("    3. Worst case")
        print("    4. Exit Bubble sort test")
        choice2 = input("    \nSelect the case (1-4): ")
        caseN = ''
        arr = [] 
        
        # time complexity options
        if choice2== '1': # best case
            arr = best_arr
            caseN = 'best'
        elif choice2 == '2': # avg case
            arr = avg_arr
            caseN = 'average'
        elif choice2 == '3': # worst case
            arr = worst_arr
            caseN = 'worse'
        elif choice2 == '4': # exit menu
            boolsub2 = True 
            continue
        else:
            choice2 = input("Invalid choice made. Please enter one of the available options (1-4): ")
        
        # run cases
        sys.setrecursionlimit(100001)
        # counts time for sort
        for i in range(len(arr)):
            if len(arr[i]) > 10000:  # stop at 10,000
                break
            
            t0 = time.perf_counter()
            bubbleSort(arr[i])
            t1 = time.perf_counter()
            print ("\nIn the ", caseN, " case,")
            print("For N = ", {len(arr[i])}, " it takes ", (t1 - t0), "seconds")
            
        choiceN = input("Do you want to input another value of N (Y/N)? ")
        if choiceN == 'y' or choiceN == 'Y':
            choiceN2 = int(input("What is the N? "))
            t0 = time.perf_counter()
            bubbleSort(arr[i])
            t1 = time.perf_counter()
            print("\nFor N = ", choiceN2, ", it takes ", (t1 - t0)," seconds")
            
        elif choiceN == "n" or choiceN =="N":
            continue
 

def sortType(choice1, best_arr, avg_arr, worst_arr):
    boolsub = False
    
    # calls one of these functions
    while (boolsub == False):
        #calls each sort
        if choice1[0] == '1': # Bubble
            bubbleMenu(best_arr, avg_arr, worst_arr)
            return 
     
        elif choice1[0] == '2': # Merge
            mergeMenu(best_arr, avg_arr, worst_arr)
            return
 
        elif choice1[0] == '3': # Quick
            quickMenu(best_arr, avg_arr, worst_arr)
            return
            
        elif choice1[0] == '4': # Radix
            radixMenu(best_arr, avg_arr, worst_arr)
            return
            
        elif choice1[0] == '5':
            print("Bye!")
            boolsub = True 
        else:
            choice1 = input("Invalid choice made. Please enter one of the available options: ")

def main():
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
    
    # front end
    choice1 = ['']
    repeat = True 
    while(repeat == True):
        print("\nWelcome to the test suite of selected sorting algorithms!\n")
        print("Select the Sorting Algorithm you want to test.\n-------------------------")
        print("    1. Bubble Sort")
        print("    2. Merge Sort")
        print("    3. Quick Sort")
        print("    4. Radix Sort")
        print("    5. Exit")
        choice1[0] = input("    \nSelect a sorting algorithm (1-5): ")
        
        # Calls sort type
        sortType(choice1, best_arr, avg_arr, worst_arr)
       
        if choice1[0] == '5': # Check if exit was chosen
            break
    

# calls main :))))) 
if __name__ == "__main__":
    main()
 