
n = 1000000

print("using while loop")
num = 0
total = 0

while num < n:
    num += 1
    total += num

print(num, total)

print("using for loop")

num = 0
for b in range(1,n +1):
    num += b

print(num)

print("using math")

result =int( n*(n+1)/2)
print(result)