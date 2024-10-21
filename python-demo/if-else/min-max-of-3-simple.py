# Skriv et program, som finder det største og det mindste af tre tal.

a = int(input('Skriv første tal: '))
b = int(input('Skriv andet tal: '))
c = int(input('Skriv tredje tal: '))

# Find det største tal
if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

# Find det mindste tal
if a <= b and a <= c:
    min_num = a
elif b <= a and b <= c:
    min_num = b
else:
    min_num = c

print(f"Det største tal er: {max_num}")
print(f"Det mindste tal er: {min_num}")