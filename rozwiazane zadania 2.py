#zad 1
while True:
    a=int(input("podaj od jakiel liczby mam zaczac"))

    b= int(input("podaj na jakiej liczbie mam zakonczyć liczenie"))

    c= int(input("co jaka wartosc mam liczyc"))
    break
for i in range(a, b+1, c ):
    print(i)




#zad2






komunikat=input("podaj swój komunikat")
x=(-len(komunikat))

i=0
while x<i:
    i-=1
    print(komunikat[i],end=" ")


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



