'''
4. Largest List Item
    Design a function that accepts a list as an argument, and returns the largest value in the list.
    The function should use recursion to find the largest item.
'''

def main():
    # Create a list
    item_list = [1, 21, 53, 6, 9, 18, 5, 26]
    # Display the largest list item with the list as an argument and the first item in the list as the largest item
    print(largest_list_item(item_list, item_list[0]))

# define the largest list item funtion
# parameters: p_list, p_largest item, p_current index
def largest_list_item(p_list, p_largest, p_index=0):
    # base case: if len(p_list) == p_index: return p_largest
    if len(p_list) == p_index:
        return p_largest
    else:
        # recursive case if p_list[p_index] > p_largest set p_largest to p_list[p_index]
        if p_list[p_index] > p_largest:
            p_largest = p_list[p_index]
        # recursive return with p_index + 1
        return largest_list_item(p_list, p_largest, p_index + 1)


# Call the main function
main()