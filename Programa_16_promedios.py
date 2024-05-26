
print ("Inserte 3 promedios")

prom1 = float(input("Promedio 1: "))
prom2 = float(input("Promedio 2: "))
prom3 = float(input("Promedio 3: "))

if prom1 > prom2 and prom1 > prom3:
    print ("El promedio 1 es el mayor:" , prom1)

elif prom2 > prom1 and prom2 > prom3:
    print ("El promedio 2 es el mayor:" ,  prom2)

elif prom3 > prom1 and prom3 > prom2:
  print("El promedio 3 es el mayor:" , prom3)
    