
#zad1
print("hello ")
imie= input("napisz jak sie nazywasz: ")
print("czesc ", imie)

wiek =int(input("napisz ile masz lat: "))
sto =(100-wiek )
sto1=(sto+2021)

print("za sto lat skonczysz za ", sto1)"""

"""#zad2

print("hello")
liczba=int(input("podaj mi liczbe a ja ci powiem czy jest parzysta czy nie: "))
parzystosć= liczba%2
podzielnosc= liczba %4
print(parzystosć)
if parzystosć!=0:
    print("liczba jest nieparzysta")
elif parzystosć==0 and podzielnosc!=0:
    print("liczba jest parzysta ale nie podzielna przez 4")
elif parzystosć==0 and podzielnosc==0:
    print("liczba jest parzysta i podzielna przez 4")
"""
"""#zad 3

a=[1,1,2,3,5,8,13,21,34,55,89]

i=-1
while i<10:
    #print(a[i])
    i=i+1
    if a[i]<5 :
        print (a[i])
    pass
    #else:
    #    print("?")"""

#zad4

print("program który pokazuje dzielnik kazdej liczby")
dzielnik=int(input("podaj liczbe: "))





d=0
while d<=dzielnik:
    d=d+1

    #print(d-1)
    wynik=dzielnik%d

    if wynik == 0:
        print(d)
    pass

#zad 5

a=[1,1,2,3,5,8,13,21,55,89]
b=[1,2,3,4,5,6,7,8,9,10,11,12,13]


a.remove(b)
print(a)
