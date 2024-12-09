def remove_smallest(numbers):
    
    if not numbers:
        return numbers
    
    # make a copy
    result = numbers[:]

    lowest_index = 0
    
    for i in range(len(result)):
        if result[i] < result[lowest_index]:
            lowest_index = i
    
    del result[lowest_index]
    
    return result


    # Solution using built in helper functions
    
#     if len(numbers) == 0:    
#         return []
    
#     result = []
    
#     for num in numbers:
#         result.append(num)
    
#     lowest_value = min(result)
#     result.remove(lowest_value)
    
#     return result