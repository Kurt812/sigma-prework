
def find_min_max(num_list):
    if not num_list:  # Handle the case where the list is empty
        return None

    min_val, max_val = float('inf'), float('-inf')

    for num in num_list:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    print([min_val, max_val])
    return [min_val, max_val]
