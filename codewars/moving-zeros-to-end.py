def move_zeros(lst):
    numbers = [n for n in lst if n != 0] 
    zeros = [0] * (len(lst) - len(numbers))
    return numbers + zeros