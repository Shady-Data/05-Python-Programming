'''
5. Recursive List Sum
    Design a function that accepts a list of numbers as an argument. The function should recursively 
    calculate the sum of all the numbers in the list and return that value.
'''

def main():
    # Create a list of numbers
    num_list = [x for x in range(1, 21)]

    # Display the return of recurse_list_sum with the num_list and the list length as arguments
    print(recurse_list_sum(num_list, len(num_list)))
    # print(sum(num_list))

# define the recurse_list_sum
# parameters: p_list, p_times
def recurse_list_sum(p_list, p_times):
    # base case: if p_times < 1 return 0
    if p_times < 1:
        return 0
    else:
        # recursive case: return p_list[p_times - 1] + recurse_item_list(p_list, p_times -1)
        return p_list[p_times - 1] + recurse_list_sum(p_list, p_times - 1)

# Call the main function
main()