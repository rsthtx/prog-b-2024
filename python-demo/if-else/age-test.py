# Lav et program, der beder brugeren om deres alder og udskriver en besked om  de er barn, teenager, voksen eller pensionist.

age = int(input("Hvad er din alder? "))

if age < 13:
    print("Du er et barn")
elif age < 20:
    print("Du er teenager")
elif age < 67:
    print("Du er voksen")
else:
    print("Du er pensionist")