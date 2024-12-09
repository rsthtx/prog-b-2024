def filter_list(l):
    return [x for x in l if  isinstance(x, int)]

input_list = [1,2,'aasf','1','123',123]
expected = [1,2,123]
actual = filter_list(input_list)
is_success = expected == actual
assert is_success