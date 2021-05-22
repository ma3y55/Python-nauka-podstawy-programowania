"""#rzut koścmi
# generuj liczby losowe z zakresu 1-6
import random

die1=random.randint(1,6)
die2= random.randrange(6)+1

total = die1 + die2

print("wyrzuciłeś ", die1,die2, ",i uzyskałeś sume: ",total)

# Hasło
#demonstruje instrukcje if

print("Witaj w systemie firmy Bezpieczny komputer S.A")
print("-- bezpieczeństwo to podstawa naszego działania\n")

password=input("wprowadz hasło: ")

if password=="sekret":
    print("dostęp został udzielony ")
else:
    print("odmowa dostepu")

input("\nAby zakończyć program, nacisniuj klawisz: Enter.")

#komputer nastrojów
#Demonstruje klauzulę elif

import random
print("wyczuwam twoja energie. Twoje prawdziwe emocje znajdują odbicie na moim ekranie ")

print("Jestes...")

mood= random.randint(1,3)

if mood == 1:
    print(" :)")
elif mood == 2:
    print( " :| ")
elif mood == 3:
    print(" :( ")
else:
    print("nieprawidzłowa wartość nastroju! (musisz być naprawdę w złym nastroju)")
print("...dzisiaj.")

input("\n aby zakonczyc program nacisnij ")
"""

"""#symulator trzylatka
#demonstruje pętle while

print("witaj w symulatorze trzylatka")
print("ten program symuluje rozmowe z trzylatkiem dzieckiem.")
print("spróbuj przerwac to szaleństwo ")
response=""
while response!="dlatego":
    response =input("dlaczego ?\n")
print("aha juz wiem" )
input("")"""

#przegrana bitwa
#demonstruje
"""
print("twój samotny bohater otoczony jest przez bande troli. ")
print("zostałeś zaatakowany!")

health = 10
trolls = 0
damage = 3

while health>=0:
    trolls+=1
    health-= damage
    print("bohater pokonuje złego trolla "+"\n ale odnosi obrażenia i traci ", damage,"punkty zdrowia \n")

print("twój bohater walczył dzielnie i pokonał ", trolls,"trolli")
print("lecz twoj bohater juz nie zyje")
"""

count=0
while True:
    count+=1
    if count>10 :
        break
    if count== 5:
        continue
    print(count)
