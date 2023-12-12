x = input ("Zadejte proměnou x: ")
y = input ("Zadejte proměnou y: ")

x = int(x)
y = int(y)

print ("Zadejte pro Sčitaní - S")
print ("Zadejte pro Odčitaní - O")
print ("Zadejte pro Násobení - N")
print ("Zadejte pro Dělení - D")
print ("Zadejte pro Mocnění - M")
print ("Zadejte pro Odmocnění - Od")

d = input("Vyběr možnosti: ")

#Sčitaní
if (d == "S"):
    print (x + y)

#Odčitaní
if (d == "O"):
    print (x - y)

#Násobení
if (d == "N"):
    if (x >= 0):
        if (y >= 0):
            print (x * y)
        else:
            print ("Proměna ne muže být 0")
    else:
        print ("Proměna ne muže být 0")

#Dělení
if (d == "D"):
    if (x >= 0):
        if (y >= 0):
            print (x / y)
        else:
            print ("Proměna ne muže být 0")
    else:
        print ("Proměna ne muže být 0")

#Mocnění
if (d == "M"):
    if (x >= 0):
        if (y >= 0):
            print (x ** y)
        else:
            print ("Proměna ne muže být 0")
    else:
        print ("Proměna ne muže být 0")

#Odmocnění
if (d == "Od"):
    if (x >= 0):
        if (y >= 0):
            print (x**(1/y))
        else:
            print ("Proměna ne muže být 0")
    else:
        print ("Proměna ne muže být 0")
        