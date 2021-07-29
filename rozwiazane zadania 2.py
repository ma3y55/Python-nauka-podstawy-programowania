




"""
1. Napisz program, który liczy za użytkownika. Umożliw użytkownikowi
wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między
kolejnymi liczbami."""

#zad 1
while True:
    a=int(input("podaj od jakiel liczby mam zaczac"))

    b= int(input("podaj na jakiej liczbie mam zakonczyć liczenie"))

    c= int(input("co jaka wartosc mam liczyc"))
    break
for i in range(a, b+1, c ):
    print(i)


"""
2. Utwórz program, który wczytuje komunikat użytkownika, a następnie wypisuje
go w odwrotnej kolejności.
"""
#zad2






komunikat=input("podaj swój komunikat")
x=(-len(komunikat))

i=0
while x<i:
    i-=1
    print(komunikat[i],end=" ")
"""
3. Popraw program Wymieszane litery tak, żeby każdemu słowu towarzyszyła
podpowiedź. Gracz powinien mieć możliwość zobaczenia podpowiedzi, jeśli
utknie w martwym punkcie. Dodaj system punktacji, który nagradza graczy
rozwiązujących anagram bez uciekania się do podpowiedzi.
"""
#zad3
import random

WORDS =("python", "anagram", "łatwy")
len(WORDS)
podpowiedzi = ("jezyk programowania")
podpowiedzi2= ("anagraamooo ")
podpowiedzi3=("ezz")
word= random.choice(WORDS)
print( word)
correct = word
jumble= " "
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word = word[:position] + word[(position + 1):]

print("witaj w grze")
print(jumble)


guess= input("twoja odpowiedz")
ujemne=0
punkty=0
p="podpowiedz"
x=0
while guess!= correct and guess!= " ":
    if guess != correct:
        print("nie zgadza sie ")
    print("jesli potrzebujesz podpowiedzi nacisnij '1'")
    guess= input("twoja odpowiedz")
    if guess==p and correct=="python" :
        ujemne = -2
        print(punkty)
        print(podpowiedzi)

        guess=input("podoaj odpowiedz")
    elif guess=="p" and correct=="anagram":
        ujemne=-2
        print(podpowiedzi2)
        guess = input("podoaj odpowiedz")
    elif guess=="p"and correct=="łatwy":
        ujemne = -2
        print(podpowiedzi3)
        guess = input("podoaj odpowiedz")

    if guess== correct:
        print("zgadza sie ")
        punkty+=3
        print("liczba punktów", ujemne+punkty)
"""
4. Utwórz grę, w której komputer wybiera losowo słowo, które gracz musi
odgadnąć. Komputer informuje gracza, ile liter znajduje się w wybranym
słowie. Następnie gracz otrzymuje pięć szans na zadanie pytania, czy jakaś litera
jest zawarta w tym słowie. Komputer może odpowiedzieć tylko „tak” lub „nie”.
Potem gracz musi odgadnąć słowo.
"""
#zad4
import random
#gra jakie to słowo

#komputer wybiera losowe słowo
słowa = ("krokiet",
         "pszenica",
         "motocykl",
         "programowanie",
         "gra")
odpowiedz= random.choice(słowa)

#liczenie losci liter w słowie

litery= len(odpowiedz)

#odgadywanie
print(odpowiedz)

print("ODGADNIJ SŁOWO")
x=0
while x!="":
    x = input("jesli chces zaczac nacisnij jaki Enter")

print("słowo ktore odgadujesz ma ",litery,"liter" )

#5 prób
próba=0
while próba<5:
    próba+=1

    traf= input("spróbuj odgadnąć jaka litere zawiera haslo ")
    for głos in odpowiedz:
        print(głos)
        if traf in odpowiedz :
            print("tak ")

            break
        else:
            print("nie")
            break

    print("próba ",próba)
odgadywaniehasła=input("odgadnij jakie to słowo")
if odgadywaniehasła== odpowiedz:
    print("zgadłes")
else:
    print("niestety nie błedna odpowiedz" )

print("koniec gry")



