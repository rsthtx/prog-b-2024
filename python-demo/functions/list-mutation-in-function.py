
def foo(l):
    l[1] = 42
    print("inside foo", l)

def bar(l):
    l2 = l.copy()
    l2[1] = 42
    print("inside bar", l2)

def hmm(x):
    x = 7
    print("inside hmm", x)

my_list = [2,3,5]

print(my_list)

bar(my_list)

print(my_list)
foo(my_list)
print(my_list)

a = 31
print(a)
hmm(a)
print(a)
