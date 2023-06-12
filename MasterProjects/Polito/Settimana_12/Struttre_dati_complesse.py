contacts = { "Fred":7235591, "Mary": 3841212,"Bob": 3841212, "Sarah":2213278 }

copy_of_contacts = dict(contacts)

if "Bob" in contacts:
    print("Bob c'è nella tua lista dimmerda")
else:
    print("Soooooca")
#oppure
print(contacts.get("Bob", "Soooooooca" ))

contacts["Mary"] = 56780
print(contacts["Fred"])
print(contacts)

elemento_cancellato = contacts.pop("Mary")
print(f"hai cancellato {elemento_cancellato}")
print(contacts)

for key in contacts:
    print(key)
#oppure
for item in contacts.items():
    print(item[0],item[1])