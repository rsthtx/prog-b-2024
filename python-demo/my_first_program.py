# Dette er et eksempel på et python program. Denne linje er en kommentar
print("Hej Programmering")
print("Hvad hedder du?")
name = input().strip()

print("Hej: " + name)
print('Længden af dit navn er:')
print(len(name))
print("Hvor gammel er du?")

age = input()

print("Din alder: " + age)
print("Du bliver " + str(int(age) +1)  + "år næste gang du har fødselsdag")
