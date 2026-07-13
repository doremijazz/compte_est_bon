from random import choice, sample

CYBLE = list(range(101,1000))
PLAQUE = 2*list(range(1,11))+[25, 50, 75, 100]


def operation(choice_1, choice_2, choice_3):
    if choice_3 == "addition":
        return choice_1 + choice_2
    elif choice_3 == "multiplication":
        return choice_1 * choice_2
    elif choice_3 == "division":
        return choice_1 / choice_2
    elif choice_3 == "soustraction":
        return choice_1 - choice_2
    return None


def ceb():
    c = choice(CYBLE)
    plaques = list(sample(PLAQUE, 6))

    while len(plaques) > 1:
        print(f"Cyble : {c}")
        print(f"Plaque : {plaques}")

        choice_1 = int(input("Choisisez une premiére plaque"))
        choice_2 = int(input("Choisissez une deuxiéme plaque"))
        choice_3 = input("addition, soustraction, mutiplication, division")

        plaques.remove(choice_1)
        plaques.remove(choice_2)

        resultat = operation(choice_1, choice_2, choice_3)
        plaques.append(resultat)
        print(f"\n Resulatat {resultat} \n")

        if resultat == c:
            print("\nBravo, le compte est bon !")
            return

    print("\nTu n'as plus assez de plaques.")
    print(f"Résultat obtenu : {plaques[0]}")
    print(f"Cible : {c}")
    print(f"Écart : {abs(c - plaques[0])}")


if __name__ == "__main__":
    ceb()