import random


score = 0
while(True):

    x = random.randint(0,2)

    opcje = ['kamień', 'papier', 'nożyce']

    komputer = opcje[x] # Wybór komputera

    wybor = input("Co wyrzucasz? [kamień, papier, nożyce]:")

    wybor_lower = wybor.lower()

    if wybor_lower == komputer:
        score -= 1
        print(F'Remis! Tracisz punkt xd')
    elif wybor_lower == "kamień" and komputer == "papier":
        score = 0
        print(F"Przegrałeś! Tracisz wszystkie {score} punkty xd")
    elif wybor_lower == "papier" and komputer == "nożyce":
        score = 0
        print(F"Przegrałeś! Tracisz wszystkie {score} punkty xd")
    elif wybor_lower == "nożyce" and komputer == "kamień":
        score = 0
        print(F"Przegrałeś! Tracisz wszystkie {score} punkty xd")
    else:
        score += 1
        print(F"Wygrałeś! Zyskujesz 1 punkt do puli {score}")
