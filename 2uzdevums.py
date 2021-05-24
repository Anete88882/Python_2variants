  """
    Funkcija akrs akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to kvadrātu starpību un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    parādot skaitli ar četriem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu summa
 """
import math
import decimal
a=input()
b=input()
c=input()
def akrs (a, b, c):
    kvadrats=float(pow(a,2)+pow(b,2)+pow(c,2))
    return kvadrats
print( '%.4f'% akrs(a, b, c))