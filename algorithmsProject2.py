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

# MERGE SORT ******

# QUICK SORT ******

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



# MAIN ************

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
    
    
    
    # Just some testing for us to see the best avg and worst to make sure it works correctly
    '''
    for i in range(4):
        n = 100 * pow(10, i)
        print("Best array of size", n, ":", best_arr[i])
        print("\n")
        print("Average array of size", n, ":", avg_arr[i])
        print("\n")
        print("Worst array of size", n, ":", worst_arr[i])
        print("\n")
    '''
    
    
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
        sorted_list = radix_sort(arr[i])
        t1 = time.perf_counter()  
        # Replace "Radix sort" with sort_name when more sorts are implemented into an if-else chain
        print("Time cost of: ", "Radix sort,", len(arr[i]), "elements,", arr_name, ":", t1-t0, "seconds.\n")


if __name__ == "__main__":
    main()