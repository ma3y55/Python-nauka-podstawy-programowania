#zad 1
"""import random

print("Program Ciastko z wróżbą")

wrozba= random.randint(1,5)
#print(wrozba)

if wrozba == 1:
    print("dobry dzien")
elif wrozba == 2:
    print("zły dzien")
elif wrozba == 3:
    print("poznasz kogos")
elif wrozba == 4:
    print("czas na zmiany")
elif wrozba == 5:
    print("czas zaryzykować")
else:
    print("braz wrózby")

input("\n nacisniej kalwisz")

#zad2
print("rzut monetą")
orzeł=0
reszka=0

i=0
while i<100:
    i+=1
    print(i)
    x= random.randint(1,2)
    if x==1:
        print("orzeł")
        orzeł += 1
    elif x==2:
        print("reszka")
        reszka+=1

print("orzeł" , orzeł)
print("reszka", reszka)"""

#zad3
import random

print("gra jaka to liczba")

print("własnie losuje liczbe")
liczba=random.randint(1,100)

i=0
while i<3:
    i+=1

    print(i,"próba")
    #print(liczba)

    odpowiedz=int(input("odgadnij jaka to liczba?: "))

    if odpowiedz < liczba:
        print("za mało\n")
    elif odpowiedz > liczba:
        print("za duzo\n")
    elif odpowiedz==liczba:
        print("poprawna odpowiedz")

        break
print( "nie udało Ci sie odgadnąć" )